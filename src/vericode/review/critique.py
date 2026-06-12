from __future__ import annotations

import json

from vericode.dafny.errors import format_errors_for_llm
from vericode.dafny.toolchain import extract_ensures_clauses
from vericode.models import CritiqueFinding, CritiqueOutcome, CritiqueReport, DafnyError, ScopedSymbol, TaskContext


def build_critique(
    *,
    outcome: CritiqueOutcome,
    summary: str,
    context: TaskContext | None = None,
    verified: bool = False,
    errors: list[DafnyError] | None = None,
    skeleton: str = "",
    extra_findings: list[CritiqueFinding] | None = None,
) -> CritiqueReport:
    findings: list[CritiqueFinding] = list(extra_findings or [])
    focus = context.verification_scope if context else None

    if errors:
        for err in errors[:10]:
            loc = None
            if context and context.focus:
                loc = f"{context.focus.path}:{err.line or context.focus.start_line}"
            findings.append(
                CritiqueFinding(
                    category="verifier_error",
                    message=err.message,
                    pr_location=loc,
                )
            )

    if outcome == CritiqueOutcome.PROOF_FAILED and skeleton:
        for clause in extract_ensures_clauses(skeleton)[:5]:
            findings.append(
                CritiqueFinding(
                    category="spec_clause",
                    message="Postcondition may be unmet by PR translation.",
                    spec_clause=clause,
                    pr_location=context.focus.path if context and context.focus else None,
                )
            )

    if context:
        for note in _unresolved_comment_requirements(context):
            findings.append(
                CritiqueFinding(
                    category="unresolved_comment",
                    message=note,
                    pr_location=context.focus.path if context.focus else None,
                )
            )

    return CritiqueReport(
        outcome=outcome,
        summary=summary,
        findings=findings,
        focus_symbol=focus,
        verified=verified,
    )


def _unresolved_comment_requirements(context: TaskContext) -> list[str]:
    notes: list[str] = []
    for c in context.review_comments:
        body = c.body.strip()
        if not body:
            continue
        loc = f"{c.path}:{c.line}" if c.path else "thread"
        notes.append(f"Review comment at {loc} may impose requirements: {body[:200]}")
    return notes[:5]


def format_critique_md(report: CritiqueReport) -> str:
    lines = [
        f"# Verification Critique: {report.outcome.value}",
        "",
        report.summary,
        "",
    ]
    if report.focus_symbol:
        lines.extend([f"**Focus:** `{report.focus_symbol}`", ""])
    if report.findings:
        lines.append("## Findings")
        for item in report.findings:
            lines.append(f"- **{item.category}**: {item.message}")
            if item.spec_clause:
                lines.append(f"  - Spec: `{item.spec_clause}`")
            if item.pr_location:
                lines.append(f"  - Location: `{item.pr_location}`")
    return "\n".join(lines) + "\n"


def format_critique_json(report: CritiqueReport) -> str:
    return json.dumps(report.model_dump(mode="json"), indent=2) + "\n"


def critique_from_verify_failure(
    context: TaskContext,
    skeleton: str,
    errors: list[DafnyError],
    *,
    resource_limit: bool = False,
) -> CritiqueReport:
    if resource_limit:
        outcome = CritiqueOutcome.RESOURCE_LIMIT
        summary = "Dafny verification timed out or exceeded resource limits."
    else:
        outcome = CritiqueOutcome.PROOF_FAILED
        summary = (
            f"Translation of `{context.verification_scope}` did not verify against the approved spec. "
            f"{format_errors_for_llm(errors)[:500]}"
        )
    return build_critique(
        outcome=outcome,
        summary=summary,
        context=context,
        verified=False,
        errors=errors,
        skeleton=skeleton,
    )


def critique_proved(context: TaskContext) -> CritiqueReport:
    return build_critique(
        outcome=CritiqueOutcome.PROVED,
        summary=f"PR logic for `{context.verification_scope}` verified against the approved specification.",
        context=context,
        verified=True,
    )


def critique_out_of_scope(message: str, context: TaskContext | None = None) -> CritiqueReport:
    return build_critique(
        outcome=CritiqueOutcome.OUT_OF_SCOPE,
        summary=message,
        context=context,
    )


def critique_translation_gap(message: str, context: TaskContext) -> CritiqueReport:
    return build_critique(
        outcome=CritiqueOutcome.TRANSLATION_GAP,
        summary=message,
        context=context,
        extra_findings=[CritiqueFinding(category="translation", message=message)],
    )


def critique_inherently_unverifiable(message: str, context: TaskContext) -> CritiqueReport:
    return build_critique(
        outcome=CritiqueOutcome.INHERENTLY_UNVERIFIABLE,
        summary=message,
        context=context,
    )
