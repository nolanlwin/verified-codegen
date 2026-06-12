from __future__ import annotations

from vericode.dafny.errors import format_errors_for_llm
from vericode.dafny.sanitize import (
    codegen_repair_hints,
    merge_skeleton_into_codegen,
    sanitize_dafny_implementation,
    sanitize_dafny_skeleton,
)
from vericode.dafny.toolchain import ensures_preserved
from vericode.llm.client import OpenAIClient, load_prompt
from vericode.models import CodegenAgentResponse, DafnyError


class EnsuresWeakenedError(ValueError):
    pass


class CodegenAgent:
    def __init__(self, client: OpenAIClient, *, model: str = "gpt-4o") -> None:
        self.client = client
        self.model = model
        self.system_prompt = load_prompt("codegen_system.txt")

    def _guidance(self, skeleton: str) -> str:
        hints: list[str] = []
        if "BinarySearchSpec" in skeleton:
            hints.append(
                "IMPORTANT: The postcondition equates the result to recursive function "
                "BinarySearchSpec. Implement BinarySearch as a recursive method with the "
                "same case structure and `decreases |nums|` — do NOT use a while loop."
            )
        if "seq<real>" in skeleton and "threshold" in skeleton.lower():
            hints.append(
                "For real distance comparisons use AbsDistReal(a, b) — never `|a - b|` "
                "(that is invalid in Dafny; `|x|` is collection size only)."
            )
        if "MakeAPileSpec" in skeleton:
            hints.append(
                "Use MakeAPileAux(start, count) with `requires count >= 0` and `decreases count`. "
                "Implement method MakeAPile mirroring MakeAPileAux; make_a_pile calls MakeAPile(n, n)."
            )
        if "WordsStringAcc" in skeleton or ("WordsStringSpec" in skeleton and "string" in skeleton.lower()):
            hints.append(
                "WordsStringAcc must have `requires 0 <= i <= |s|`. "
                "Implement WordsStringAccMethod with the same requires/decreases and mirror the spec recursion."
            )
        if "FSpec" in skeleton and "FactorialSpec" in skeleton:
            hints.append(
                "FactorialSpec, SumToSpec, ElementSpec need `requires i >= 0`; FSpec needs `requires n >= 0`. "
                "Implement method f recursively with `decreases n`."
            )
        if "string" in skeleton.lower() and "seq<string>" in skeleton:
            hints.append(
                "Copy every `function ...Spec` from the skeleton verbatim. "
                "Implement string parsing with a recursive method — no `while` inside functions."
            )
        return "\n".join(hints)

    def prepare_source(self, skeleton: str, generated: str) -> str:
        clean_skeleton = sanitize_dafny_skeleton(skeleton)
        merged = merge_skeleton_into_codegen(clean_skeleton, generated)
        return sanitize_dafny_implementation(merged)

    def generate(self, verified_spec: str, skeleton: str) -> str:
        guidance = self._guidance(skeleton)
        user = (
            f"Verified natural language specification:\n{verified_spec}\n\n"
            f"Dafny specification skeleton (preserve requires/ensures exactly):\n{skeleton}\n\n"
        )
        if guidance:
            user += f"Implementation guidance:\n{guidance}\n\n"
        user += "Generate the complete verifiable Dafny implementation."
        response = self.client.complete(
            model=self.model,
            system=self.system_prompt,
            user=user,
            schema=CodegenAgentResponse,
        )
        self._guard_ensures(skeleton, response.dafny_source)
        return self.prepare_source(skeleton, response.dafny_source)

    def fix(
        self,
        verified_spec: str,
        skeleton: str,
        current_source: str,
        errors: list[DafnyError],
    ) -> str:
        guidance = self._guidance(skeleton)
        user = (
            f"Verified natural language specification:\n{verified_spec}\n\n"
            f"Original skeleton (preserve requires/ensures exactly):\n{skeleton}\n\n"
            f"Current Dafny source:\n{current_source}\n\n"
            f"Verifier errors:\n{format_errors_for_llm(errors)}\n\n"
        )
        if guidance:
            user += f"Implementation guidance:\n{guidance}\n\n"
        hints = codegen_repair_hints(format_errors_for_llm(errors), current_source)
        if hints:
            user += f"{hints}\n\n"
        user += "Fix the implementation with minimal changes. Do not weaken ensures clauses."
        response = self.client.complete(
            model=self.model,
            system=self.system_prompt,
            user=user,
            schema=CodegenAgentResponse,
        )
        self._guard_ensures(skeleton, response.dafny_source)
        return self.prepare_source(skeleton, response.dafny_source)

    def _guard_ensures(self, skeleton: str, generated: str) -> None:
        if not ensures_preserved(skeleton, generated):
            raise EnsuresWeakenedError(
                "Generated Dafny weakened or removed ensures clauses from the agreed skeleton."
            )
