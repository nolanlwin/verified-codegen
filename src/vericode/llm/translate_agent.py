from __future__ import annotations

from vericode.dafny.sanitize import merge_skeleton_into_codegen, sanitize_dafny_implementation, sanitize_dafny_skeleton
from vericode.dafny.toolchain import ensures_preserved
from vericode.llm.client import OpenAIClient, load_prompt
from vericode.llm.codegen_agent import EnsuresWeakenedError
from vericode.llm.translators import get_translator
from vericode.models import CodegenAgentResponse, ScopedSymbol, SourceLanguage, SymbolContext
from vericode.sources.symbol_context import render_symbol_context_for_prompt


class TranslateAgent:
    def __init__(self, client: OpenAIClient, *, model: str = "gpt-4o") -> None:
        self.client = client
        self.model = model

    def translate(
        self,
        verified_spec: str,
        skeleton: str,
        scoped: ScopedSymbol,
        *,
        symbol_context: SymbolContext | None = None,
        verification_mode: str = "verify_pr",
    ) -> str:
        translator = get_translator(scoped.language)
        ok, reason = translator.can_translate(scoped.name, scoped.source)
        if not ok:
            raise TranslationGapError(reason)

        user_parts = [
            f"Verified natural language specification:\n{verified_spec}",
            f"Dafny specification skeleton (preserve requires/ensures exactly):\n{skeleton}",
            f"Source language: {scoped.language}",
            f"Scoped symbol: {scoped.path}:{scoped.name}",
            f"Source to translate faithfully:\n```{scoped.language}\n{scoped.source}\n```",
        ]
        if symbol_context is not None:
            block = render_symbol_context_for_prompt(symbol_context)
            if block:
                user_parts.append(block)
        user_parts.append(
            "Produce complete Dafny source with faithful implementation. Do not fix bugs. "
            "Use the skeleton method signature and spec sentinel strings — do not reference "
            "undefined Python import names."
        )
        user = "\n\n".join(user_parts)
        response = self.client.complete(
            model=self.model,
            system=load_prompt(translator.system_prompt_name()),
            user=user,
            schema=CodegenAgentResponse,
        )
        self._guard_ensures(skeleton, response.dafny_source)
        return self.prepare_source(skeleton, response.dafny_source, verification_mode=verification_mode)

    @staticmethod
    def prepare_source(skeleton: str, generated: str, *, verification_mode: str = "verify_pr") -> str:
        clean_skeleton = sanitize_dafny_skeleton(skeleton)
        merged = merge_skeleton_into_codegen(clean_skeleton, generated)
        skip_injection = verification_mode == "verify_pr"
        return sanitize_dafny_implementation(merged, skip_benchmark_injection=skip_injection)

    def _guard_ensures(self, skeleton: str, generated: str) -> None:
        if not ensures_preserved(skeleton, generated):
            raise EnsuresWeakenedError(
                "Translation weakened or removed ensures clauses from the agreed skeleton."
            )


class TranslationGapError(ValueError):
    pass
