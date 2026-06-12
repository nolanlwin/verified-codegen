from __future__ import annotations

from vericode.dafny.sanitize import repair_hints, sanitize_dafny_skeleton
from vericode.llm.client import OpenAIClient, load_prompt
from vericode.models import SpecAgentResponse, SymbolContext, TaskContext
from vericode.sources.symbol_context import render_symbol_context_for_prompt
from vericode.sources.context import render_pr_prompt


class SpecAgent:
    def __init__(self, client: OpenAIClient, *, model: str = "gpt-4o-mini", pr_mode: bool = False) -> None:
        self.client = client
        self.model = model
        self.pr_mode = pr_mode
        self.system_prompt = load_prompt("spec_system_pr.txt" if pr_mode else "spec_system.txt")

    def generate(self, prompt: str, *, revision_feedback: list[str] | None = None) -> SpecAgentResponse:
        user_parts = [
            f"Natural language request:\n{prompt}",
        ]
        if revision_feedback:
            user_parts.append(
                "Revision feedback from human reviewer:\n"
                + "\n".join(f"- {item}" for item in revision_feedback)
            )
        user_parts.append(
            "Produce internal_dafny (spec skeleton with empty method body), "
            "nl_summary (plain English for human review), and notes (discrepancies/ambiguities)."
        )
        return self.client.complete(
            model=self.model,
            system=self.system_prompt,
            user="\n\n".join(user_parts),
            schema=SpecAgentResponse,
        )

    def generate_from_pr(
        self,
        context: TaskContext,
        *,
        symbol_context: SymbolContext | None = None,
        revision_feedback: list[str] | None = None,
    ) -> SpecAgentResponse:
        interface_block = (
            render_symbol_context_for_prompt(symbol_context) if symbol_context is not None else ""
        )
        prompt = render_pr_prompt(context, symbol_context_block=interface_block)
        user_parts = [
            f"Pull request evidence:\n{prompt}",
        ]
        if revision_feedback:
            user_parts.append(
                "Revision feedback from human reviewer:\n"
                + "\n".join(f"- {item}" for item in revision_feedback)
            )
        user_parts.append(
            "Produce internal_dafny scoped to the focused symbol when provided, "
            "nl_summary (plain English contract for review), and notes (conflicts/ambiguities)."
        )
        return self.client.complete(
            model=self.model,
            system=self.system_prompt,
            user="\n\n".join(user_parts),
            schema=SpecAgentResponse,
        )

    def repair_from_pr(
        self,
        context: TaskContext,
        broken_dafny: str,
        verify_output: str,
        *,
        symbol_context: SymbolContext | None = None,
    ) -> SpecAgentResponse:
        interface_block = (
            render_symbol_context_for_prompt(symbol_context) if symbol_context is not None else ""
        )
        prompt = render_pr_prompt(context, symbol_context_block=interface_block)
        return self.repair(prompt, broken_dafny, verify_output)

    def repair(self, prompt: str, broken_dafny: str, verify_output: str) -> SpecAgentResponse:
        hints = repair_hints(verify_output, broken_dafny)
        user = (
            f"Original request:\n{prompt}\n\n"
            f"The Dafny skeleton failed verification:\n{broken_dafny}\n\n"
            f"Verifier output:\n{verify_output}\n\n"
        )
        if hints:
            user += f"{hints}\n\n"
        user += "Repair the skeleton so it resolves (parse/type-check). Keep nl_summary aligned with the fixed spec."
        return self.client.complete(
            model=self.model,
            system=self.system_prompt,
            user=user,
            schema=SpecAgentResponse,
        )

    @staticmethod
    def format_draft_spec(response: SpecAgentResponse) -> str:
        notes_block = ""
        if response.notes:
            notes_block = "\n\nNotes from formalizer:\n" + "\n".join(
                f"- {note}" for note in response.notes
            )
        return response.nl_summary.strip() + notes_block

    def prepare_dafny(self, source: str) -> str:
        return sanitize_dafny_skeleton(source, pr_mode=self.pr_mode)

    @staticmethod
    def prepare_dafny_static(source: str, *, pr_mode: bool = False) -> str:
        return sanitize_dafny_skeleton(source, pr_mode=pr_mode)
