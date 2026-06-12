from __future__ import annotations

import shutil
from pathlib import Path

from rich.console import Console

from vericode.artifacts.store import SessionStore
from vericode.dafny.toolchain import build_python, resolve, verify
from vericode.llm.client import OpenAIClient
from vericode.llm.codegen_agent import CodegenAgent, EnsuresWeakenedError
from vericode.llm.spec_agent import SpecAgent
from vericode.llm.translate_agent import TranslateAgent, TranslationGapError
from vericode.models import CritiqueOutcome, SessionStatus, TaskContext
from vericode.preflight import find_dafny, preflight
from vericode.review.critique import (
    critique_from_verify_failure,
    critique_out_of_scope,
    critique_proved,
    critique_translation_gap,
    format_critique_json,
    format_critique_md,
)
from vericode.review.interactive import ReviewAction, review_spec
from vericode.review.pr_sources import format_sources_panel
from vericode.dafny.spec_semantics import format_semantic_issues, validate_spec_semantics
from vericode.sources.context import render_pr_prompt
from vericode.sources.github import ingest_pr
from vericode.sources.verifiability import assess_pr_verifiability


class Pipeline:
    def __init__(
        self,
        store: SessionStore | None = None,
        console: Console | None = None,
        *,
        verify_timeout: int = 120,
        build_timeout: int = 180,
    ) -> None:
        self.store = store or SessionStore()
        self.console = console or Console()
        self.verify_timeout = verify_timeout
        self.build_timeout = build_timeout
        self.dafny_bin = find_dafny() or "dafny"

    def new_session(
        self,
        prompt: str,
        *,
        spec_model: str = "gpt-4o-mini",
        codegen_model: str = "gpt-4o",
        max_verify_retries: int = 5,
        auto_approve: bool = False,
        skip_run: bool = False,
    ) -> str:
        check = preflight(require_openai=True, require_dafny=True)
        if not check.ok:
            raise RuntimeError("\n".join(check.errors or []))

        meta = self.store.create_session(
            prompt,
            spec_model=spec_model,
            codegen_model=codegen_model,
            max_verify_retries=max_verify_retries,
        )
        self.console.print(f"[green]Created session[/green] {meta.session_id}")
        self.generate_spec(meta.session_id)
        action, feedback = self.review_session(meta.session_id, auto_approve=auto_approve)
        if action == ReviewAction.ABORT:
            self.store.fail_session(meta.session_id, "Aborted during spec review.")
            return meta.session_id
        if action == ReviewAction.REVISE and feedback:
            self.revise_spec(meta.session_id, feedback)
            action, _ = self.review_session(meta.session_id, auto_approve=auto_approve)
            if action != ReviewAction.APPROVE:
                self.store.fail_session(meta.session_id, "Spec not approved.")
                return meta.session_id
        if not skip_run and (action == ReviewAction.APPROVE or auto_approve):
            self._run_post_approval(meta.session_id)
        return meta.session_id

    def new_pr_session(
        self,
        *,
        pr_url: str | None = None,
        fixture: Path | None = None,
        patch_file: Path | None = None,
        meta_file: Path | None = None,
        focus: str | None = None,
        spec_model: str = "gpt-4o-mini",
        codegen_model: str = "gpt-4o",
        auto_approve: bool = False,
        skip_run: bool = False,
        check_only: bool = False,
    ) -> str:
        check = preflight(require_openai=not check_only, require_dafny=True)
        if not check.ok:
            raise RuntimeError("\n".join(check.errors or []))

        context = ingest_pr(
            url=pr_url,
            fixture=fixture,
            focus=focus,
            patch_file=patch_file,
            meta_file=meta_file,
        )
        if context.focus is None:
            from vericode.sources.verifiability import suggest_focus_symbols

            hint = suggest_focus_symbols(context)
            raise RuntimeError(f"No focus symbol selected. Use --focus path:symbol. Candidates: {hint}")

        prompt = render_pr_prompt(context)
        meta = self.store.create_pr_session(
            context,
            prompt,
            spec_model=spec_model,
            codegen_model=codegen_model,
        )
        self.console.print(f"[green]Created PR session[/green] {meta.session_id}")
        if context.verification_scope:
            self.console.print(f"[dim]Focus: {context.verification_scope}[/dim]")

        assessment = assess_pr_verifiability(context)
        if not assessment.verifiable:
            self._persist_verifiability_critique(meta.session_id, context, assessment)
            self.console.print(f"[yellow]{assessment.summary}[/yellow]")
            return meta.session_id

        self.console.print(f"[green]{assessment.summary}[/green]")
        if check_only:
            self.store.update_status(meta.session_id, SessionStatus.AWAITING_REVIEW)
            self.console.print("[dim]Verifiability check passed. Re-run without --check-only to generate spec.[/dim]")
            return meta.session_id

        self.generate_spec(meta.session_id)
        action, feedback = self.review_session(meta.session_id, auto_approve=auto_approve)
        if action == ReviewAction.ABORT:
            self._save_critique_abort(meta.session_id)
            return meta.session_id
        if action == ReviewAction.REVISE and feedback:
            self.revise_spec(meta.session_id, feedback)
            action, _ = self.review_session(meta.session_id, auto_approve=auto_approve)
            if action != ReviewAction.APPROVE:
                self.store.fail_session(meta.session_id, "Spec not approved.")
                return meta.session_id
        if not skip_run and action == ReviewAction.APPROVE:
            self._run_post_approval(meta.session_id)
        return meta.session_id

    def _run_post_approval(self, session_id: str) -> None:
        meta = self.store.read_meta(session_id)
        if meta.verification_mode == "verify_pr":
            self.run_pr_verification(session_id)
        else:
            self.run_codegen(session_id)

    def generate_spec(self, session_id: str) -> None:
        meta = self.store.read_meta(session_id)
        prompt = self.store.read_text(session_id, "prompt.txt")
        client = OpenAIClient()
        pr_mode = meta.source_type == "github_pr"
        agent = SpecAgent(client, model=meta.spec_model, pr_mode=pr_mode)

        self.store.update_status(session_id, SessionStatus.DRAFT_SPEC)
        self.console.print("[bold]Generating draft specification...[/bold]")

        context = self.store.read_context_optional(session_id)
        symbol_context = self.store.read_symbol_context_optional(session_id)
        if pr_mode and context is not None:
            response = agent.generate_from_pr(
                context,
                symbol_context=symbol_context,
                revision_feedback=meta.revision_feedback,
            )
        else:
            response = agent.generate(prompt, revision_feedback=meta.revision_feedback)
        self._save_spec_response(session_id, response.internal_dafny, agent.format_draft_spec(response))

        verify_result = self._verify_spec_skeleton(session_id)
        semantic_issues = self._spec_semantic_issues(session_id)
        if verify_result.ok and semantic_issues:
            verify_result = self._semantic_verify_failure(session_id, semantic_issues)
        if not verify_result.ok:
            max_spec_repairs = 7
            for attempt in range(max_spec_repairs):
                self.console.print(f"[yellow]Repairing spec skeleton (attempt {attempt + 1})...[/yellow]")
                combined = verify_result.stdout + verify_result.stderr
                if semantic_issues:
                    combined += "\n\n" + format_semantic_issues(semantic_issues)
                if pr_mode and context is not None:
                    response = agent.repair_from_pr(
                        context,
                        response.internal_dafny,
                        combined,
                        symbol_context=symbol_context,
                    )
                else:
                    response = agent.repair(prompt, response.internal_dafny, combined)
                self._save_spec_response(session_id, response.internal_dafny, agent.format_draft_spec(response))
                verify_result = self._verify_spec_skeleton(session_id)
                semantic_issues = self._spec_semantic_issues(session_id)
                if verify_result.ok and semantic_issues:
                    verify_result = self._semantic_verify_failure(session_id, semantic_issues)
                if verify_result.ok:
                    break
            if not verify_result.ok:
                self.store.fail_session(session_id, "Spec skeleton failed verification.")
                from vericode.dafny.errors import format_errors_for_llm

                hint = format_errors_for_llm(verify_result.errors)
                self.console.print(f"[red]Spec skeleton errors:[/red]\n{hint}")
                self.console.print(
                    f"[dim]See {self.store.session_dir(session_id) / 'spec_verify.log'}[/dim]"
                )
                raise RuntimeError("Spec skeleton failed verification after repair.")

        self.store.update_status(session_id, SessionStatus.AWAITING_REVIEW)
        self.console.print("[green]Draft specification ready for review.[/green]")

    def _save_spec_response(self, session_id: str, internal_dafny: str, draft_spec: str) -> None:
        meta = self.store.read_meta(session_id)
        cleaned = SpecAgent.prepare_dafny_static(
            internal_dafny,
            pr_mode=meta.source_type == "github_pr",
        )
        self.store.write_text(session_id, "internal_spec.dfy", cleaned)
        self.store.write_text(session_id, "draft_spec.md", draft_spec.strip() + "\n")

    def _verify_spec_skeleton(self, session_id: str):
        path = self.store.session_dir(session_id) / "internal_spec.dfy"
        result = resolve(
            path,
            timeout=self.verify_timeout,
            dafny_bin=self.dafny_bin,
            allow_warnings=True,
        )
        log = result.stdout + result.stderr
        self.store.write_text(session_id, "spec_verify.log", log)
        return result

    def _spec_semantic_issues(self, session_id: str) -> list[str]:
        symbol_context = self.store.read_symbol_context_optional(session_id)
        if symbol_context is None:
            return []
        skeleton = self.store.read_text(session_id, "internal_spec.dfy")
        return validate_spec_semantics(skeleton, symbol_context)

    def _semantic_verify_failure(self, session_id: str, issues: list[str]):
        from vericode.models import DafnyError, VerificationResult

        message = format_semantic_issues(issues)
        self.store.write_text(session_id, "spec_verify.log", message + "\n")
        return VerificationResult(
            ok=False,
            stdout="",
            stderr=message,
            errors=[DafnyError(line=1, column=0, error_type="Error", message=issues[0])],
            returncode=1,
        )

    def review_session(self, session_id: str, *, auto_approve: bool = False) -> tuple[ReviewAction, str | None]:
        draft = self.store.read_text(session_id, "draft_spec.md")
        meta = self.store.read_meta(session_id)
        sources = None
        if meta.source_type == "github_pr":
            context = self.store.read_context_optional(session_id)
            if context is not None:
                sources = format_sources_panel(context)
        action, feedback = review_spec(
            self.console,
            draft,
            auto_approve=auto_approve,
            sources_panel=sources,
        )
        if action == ReviewAction.APPROVE:
            self.store.copy_verified_spec(session_id)
            self.store.update_status(session_id, SessionStatus.VERIFIED_SPEC)
            self.console.print("[green]Specification approved.[/green]")
        return action, feedback

    def revise_spec(self, session_id: str, feedback: str) -> None:
        meta = self.store.read_meta(session_id)
        meta.revision_feedback.append(feedback)
        self.store.write_meta(meta)
        self.generate_spec(session_id)

    def run_codegen(self, session_id: str) -> None:
        check = preflight(require_openai=True, require_dafny=True)
        if not check.ok:
            raise RuntimeError("\n".join(check.errors or []))

        meta = self.store.read_meta(session_id)
        if meta.status not in (SessionStatus.VERIFIED_SPEC, SessionStatus.GENERATING_DAFNY, SessionStatus.VERIFYING):
            verified = self.store.read_text_optional(session_id, "verified_spec.md")
            if not verified:
                raise RuntimeError("Specification not approved. Run review first.")
            self.store.update_status(session_id, SessionStatus.VERIFIED_SPEC)

        meta = self.store.read_meta(session_id)
        verified_spec = self.store.read_text(session_id, "verified_spec.md")
        skeleton = self.store.read_text(session_id, "internal_spec.dfy")

        client = OpenAIClient()
        agent = CodegenAgent(client, model=meta.codegen_model)

        self.store.update_status(session_id, SessionStatus.GENERATING_DAFNY)
        self.console.print("[bold]Generating Dafny implementation...[/bold]")

        try:
            source = agent.generate(verified_spec, skeleton)
        except EnsuresWeakenedError as exc:
            self.store.fail_session(session_id, str(exc))
            raise

        impl_path = self.store.write_text(session_id, "implementation.dfy", source.strip() + "\n")

        self.store.update_status(session_id, SessionStatus.VERIFYING)
        attempts = 0
        while attempts <= meta.max_verify_retries:
            self.console.print(f"[bold]Verifying[/bold] (attempt {attempts + 1})...")
            result = verify(impl_path, timeout=self.verify_timeout, dafny_bin=self.dafny_bin)
            log = result.stdout + result.stderr
            self.store.write_text(session_id, "verify.log", log)

            if result.ok:
                meta = self.store.update_status(
                    session_id,
                    SessionStatus.COMPILING,
                    verified=True,
                    verify_attempts=attempts + 1,
                )
                self.console.print(f"[green]Verified[/green] in {attempts + 1} attempt(s).")
                self._compile_python(session_id)
                return

            attempts += 1
            if attempts > meta.max_verify_retries:
                break

            self.console.print("[yellow]Verification failed; requesting fix from LLM...[/yellow]")
            try:
                source = agent.fix(verified_spec, skeleton, source, result.errors)
            except EnsuresWeakenedError as exc:
                self.store.fail_session(session_id, str(exc))
                raise
            impl_path = self.store.write_text(session_id, "implementation.dfy", source.strip() + "\n")

        self.store.fail_session(session_id, f"Verification failed after {meta.max_verify_retries} retries.")
        raise RuntimeError(f"Verification failed. See {self.store.session_dir(session_id) / 'verify.log'}")

    def run_pr_verification(self, session_id: str) -> None:
        check = preflight(require_openai=True, require_dafny=True)
        if not check.ok:
            raise RuntimeError("\n".join(check.errors or []))

        meta = self.store.read_meta(session_id)
        if meta.verification_mode != "verify_pr":
            raise RuntimeError("Session is not in verify_pr mode.")

        context = self.store.read_context(session_id)
        assessment = assess_pr_verifiability(context)
        if not assessment.verifiable:
            self._persist_verifiability_critique(session_id, context, assessment)
            return

        verified_spec = self.store.read_text(session_id, "verified_spec.md")
        skeleton = self.store.read_text(session_id, "internal_spec.dfy")
        assert context.focus is not None

        symbol_context = self.store.read_symbol_context_optional(session_id)
        spec_semantic_issues = (
            validate_spec_semantics(skeleton, symbol_context)
            if symbol_context is not None
            else []
        )
        if spec_semantic_issues:
            from vericode.models import CritiqueFinding
            from vericode.review.critique import build_critique

            report = build_critique(
                outcome=CritiqueOutcome.SPEC_UNFORMALIZABLE,
                summary=(
                    f"Approved spec for `{context.verification_scope}` does not reflect PR evidence: "
                    + spec_semantic_issues[0]
                ),
                context=context,
                extra_findings=[
                    CritiqueFinding(category="spec_semantic", message=issue)
                    for issue in spec_semantic_issues
                ],
            )
            self._persist_critique(session_id, report)
            self.console.print("[yellow]Spec does not match PR evidence — see critique.md[/yellow]")
            return

        client = OpenAIClient()
        translator = TranslateAgent(client, model=meta.codegen_model)

        self.store.update_status(session_id, SessionStatus.GENERATING_DAFNY)
        self.console.print("[bold]Translating PR source to Dafny...[/bold]")

        try:
            source = translator.translate(
                verified_spec,
                skeleton,
                context.focus,
                symbol_context=symbol_context,
                verification_mode=meta.verification_mode,
            )
        except TranslationGapError as exc:
            report = critique_translation_gap(str(exc), context)
            self._persist_critique(session_id, report)
            return
        except EnsuresWeakenedError as exc:
            self.store.fail_session(session_id, str(exc))
            raise

        self.store.write_text(session_id, "translation.dfy", source.strip() + "\n")
        impl_path = self.store.write_text(session_id, "implementation.dfy", source.strip() + "\n")

        self.store.update_status(session_id, SessionStatus.VERIFYING)
        self.console.print("[bold]Verifying PR translation (verify-only)...[/bold]")
        result = verify(impl_path, timeout=self.verify_timeout, dafny_bin=self.dafny_bin)
        log = result.stdout + result.stderr
        self.store.write_text(session_id, "verify.log", log)

        if result.ok:
            report = critique_proved(context)
            self.store.update_status(
                session_id,
                SessionStatus.DONE,
                verified=True,
                verify_attempts=1,
            )
            self._persist_critique(session_id, report)
            self.console.print("[green]PR logic proved against approved spec.[/green]")
            return

        resource_limit = result.returncode == -1 or "timeout" in log.lower()
        report = critique_from_verify_failure(
            context,
            skeleton,
            result.errors,
            resource_limit=resource_limit,
        )
        self._persist_critique(session_id, report)
        self.console.print("[yellow]Verification failed — see critique.md[/yellow]")

    def _persist_verifiability_critique(self, session_id: str, context: TaskContext, assessment) -> None:
        from vericode.models import CritiqueFinding
        from vericode.review.critique import build_critique

        findings = [
            CritiqueFinding(category="verifiability", message=reason)
            for reason in assessment.reasons
        ]
        report = build_critique(
            outcome=assessment.outcome or CritiqueOutcome.INHERENTLY_UNVERIFIABLE,
            summary=assessment.summary,
            context=context,
            extra_findings=findings,
        )
        self._persist_critique(session_id, report)

    def _persist_critique(self, session_id: str, report) -> None:
        self.store.write_critique(
            session_id,
            format_critique_md(report),
            format_critique_json(report),
        )
        status = SessionStatus.DONE if report.outcome == CritiqueOutcome.PROVED else SessionStatus.DONE_WITH_FINDINGS
        self.store.update_status(session_id, status, verified=report.verified)

    def _save_critique_abort(self, session_id: str) -> None:
        from vericode.review.critique import build_critique

        report = build_critique(
            outcome=CritiqueOutcome.SPEC_REJECTED,
            summary="Specification review aborted.",
            context=self.store.read_context_optional(session_id),
        )
        self._persist_critique(session_id, report)
        self.store.fail_session(session_id, "Aborted during spec review.")

    def _compile_python(self, session_id: str) -> None:
        meta = self.store.read_meta(session_id)
        impl_path = self.store.session_dir(session_id) / "implementation.dfy"
        output_dir = self.store.output_dir(session_id)
        # dafny writes to {output_dir}-py
        build_base = self.store.session_dir(session_id) / "build"
        build_base.mkdir(parents=True, exist_ok=True)

        self.console.print("[bold]Compiling to Python...[/bold]")
        result = build_python(
            impl_path,
            build_base,
            timeout=self.build_timeout,
            dafny_bin=self.dafny_bin,
        )
        if not result.ok or not result.main_py:
            self.store.fail_session(session_id, "Dafny Python compilation failed.")
            raise RuntimeError(result.stderr or "Dafny build failed.")

        final_path = self.store.session_dir(session_id) / "final.py"
        shutil.copy2(result.main_py, final_path)
        if result.output_dir:
            # Keep generated tree under session output/
            dest = output_dir / "generated"
            generated = Path(result.output_dir)
            if generated.exists() and generated != dest:
                if dest.exists():
                    shutil.rmtree(dest)
                shutil.copytree(generated, dest)
        self.store.update_status(session_id, SessionStatus.DONE)
        self.console.print(f"[green]Done.[/green] Python written to [bold]{final_path}[/bold]")

    def resume(self, session_id: str, *, auto_approve: bool = False) -> None:
        if not self.store.exists(session_id):
            raise RuntimeError(f"Session not found: {session_id}")
        meta = self.store.read_meta(session_id)

        if meta.status in (SessionStatus.DRAFT_SPEC, SessionStatus.AWAITING_REVIEW):
            if not self.store.read_text_optional(session_id, "draft_spec.md"):
                self.generate_spec(session_id)
            action, feedback = self.review_session(session_id, auto_approve=auto_approve)
            if action == ReviewAction.REVISE and feedback:
                self.revise_spec(session_id, feedback)
                action, _ = self.review_session(session_id, auto_approve=auto_approve)
            if action == ReviewAction.APPROVE:
                self._run_post_approval(session_id)
        elif meta.status == SessionStatus.VERIFIED_SPEC:
            self._run_post_approval(session_id)
        elif meta.status in (SessionStatus.GENERATING_DAFNY, SessionStatus.VERIFYING, SessionStatus.COMPILING):
            self._run_post_approval(session_id)
        elif meta.status in (SessionStatus.DONE, SessionStatus.DONE_WITH_FINDINGS):
            self.console.print(f"Session {session_id} already complete ({meta.status.value}).")
        elif meta.status == SessionStatus.FAILED:
            raise RuntimeError(meta.error_message or "Session failed.")
