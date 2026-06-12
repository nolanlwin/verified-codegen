from __future__ import annotations

import re
from dataclasses import dataclass, field

from vericode.models import CritiqueOutcome, TaskContext


@dataclass
class VerifiabilityAssessment:
    verifiable: bool
    outcome: CritiqueOutcome | None = None
    summary: str = ""
    reasons: list[str] = field(default_factory=list)


# Patterns in scoped source that v1 cannot model faithfully in Dafny.
_PYTHON_UNVERIFIABLE_SOURCE: list[tuple[str, str]] = [
    (r"\blogger\.(warning|info|error|debug|exception)\b", "logging side effect"),
    (r"\bstructlog\b", "structured logging"),
    (r"\bResponse\s*\(", "Django REST framework Response"),
    (r"\bHttpResponse", "Django HTTP response type"),
    (r"\brequest\.", "HTTP request object access"),
    (r"@(api_view|login_required|authentication_classes)", "web framework decorator"),
    (r"\.objects\.(get|filter|create|update)", "ORM database access"),
    (r"\bcache\.(get|set|delete)\b", "cache I/O"),
    (r"\bsettings\.", "Django settings access"),
    (r"\bcapture_exception\b", "exception reporting integration"),
    (r"\bposthoganalytics\b", "analytics capture"),
    (r"\bfetch\s*\(", "HTTP fetch"),
    (r"\bopen\s*\(", "filesystem I/O"),
]

_TYPESCRIPT_UNVERIFIABLE_SOURCE: list[tuple[str, str]] = [
    (r"\bconsole\.(log|warn|error|debug)\b", "console logging"),
    (r"\bfetch\s*\(", "HTTP fetch"),
    (r"\baxios\.", "HTTP client"),
    (r"\bwindow\.", "browser global"),
    (r"\bdocument\.", "DOM access"),
    (r"\bprocess\.env\b", "environment access"),
]

# PR description/title signals that the change is observability-only, not behavioral.
_OBSERVABILITY_INTENT: list[str] = [
    r"\blogging\b",
    r"\blog\s+entry\b",
    r"\bproduction\s+logs?\b",
    r"\bobservability\b",
    r"\bdiagnos(e|is|ing)\b.*\blogs?\b",
    r"\badd(ed)?\s+.*\blog(ger)?\b",
]


def assess_pr_verifiability(ctx: TaskContext) -> VerifiabilityAssessment:
    """Decide if a PR focus is worth formal verification before spec generation."""
    from vericode.sources.context import feasibility_precheck, list_translatable_symbols

    ok, message, outcome = feasibility_precheck(ctx)
    if not ok:
        return VerifiabilityAssessment(
            verifiable=False,
            outcome=outcome or CritiqueOutcome.OUT_OF_SCOPE,
            summary=message,
            reasons=[message],
        )

    assert ctx.focus is not None
    reasons: list[str] = []

    for pattern, label in _source_unverifiable_patterns(ctx.focus.language):
        if re.search(pattern, ctx.focus.source):
            reasons.append(f"Scoped source uses {label} (`{pattern}`)")

    intent_reasons = _observability_intent_reasons(ctx)
    reasons.extend(intent_reasons)

    if not _looks_pure_algorithm(ctx.focus.source, ctx.focus.language):
        if not reasons:
            reasons.append("Scoped symbol does not look like a pure algorithm (I/O or framework types suspected)")

    if reasons:
        return VerifiabilityAssessment(
            verifiable=False,
            outcome=CritiqueOutcome.INHERENTLY_UNVERIFIABLE,
            summary=(
                f"`{ctx.verification_scope}` is not verifiable in v1: "
                + "; ".join(reasons[:3])
                + ("." if len(reasons) <= 3 else f"; +{len(reasons) - 3} more.")
            ),
            reasons=reasons,
        )

    return VerifiabilityAssessment(
        verifiable=True,
        summary=f"`{ctx.verification_scope}` passes verifiability pre-check.",
    )


def _source_unverifiable_patterns(language: str) -> list[tuple[str, str]]:
    if language == "python":
        return _PYTHON_UNVERIFIABLE_SOURCE
    return _TYPESCRIPT_UNVERIFIABLE_SOURCE


def _observability_intent_reasons(ctx: TaskContext) -> list[str]:
    text = f"{ctx.title}\n{ctx.body}".lower()
    reasons: list[str] = []
    for pattern in _OBSERVABILITY_INTENT:
        if re.search(pattern, text, re.IGNORECASE):
            reasons.append(f"PR description suggests observability/logging intent (`{pattern}`)")
            break

    if ctx.focus and "logger." in ctx.focus.source and "return Response" in ctx.focus.source.replace(" ", ""):
        reasons.append("Change adds logging around an HTTP error response (side effect + framework type)")

    return reasons


def _looks_pure_algorithm(source: str, language: str) -> bool:
    """Heuristic: top-level function with primitive-ish returns and no framework calls."""
    if language == "python":
        if re.search(r"->\s*Response\b", source):
            return False
        if re.search(r"->\s*HttpResponse", source):
            return False
        if "logger." in source:
            return False
        # Positive signal: returns int, bool, str, list, dict literals
        if re.search(r"->\s*(int|bool|str|float|list|dict|tuple|Optional|None)", source):
            return True
        return not any(re.search(p, source) for p, _ in _PYTHON_UNVERIFIABLE_SOURCE)
    if language in ("typescript", "javascript"):
        if re.search(r":\s*Promise\b", source):
            return False
        return not any(re.search(p, source) for p, _ in _TYPESCRIPT_UNVERIFIABLE_SOURCE)
    return False


def suggest_focus_symbols(ctx: TaskContext) -> str:
    from vericode.sources.context import list_translatable_symbols

    syms = list_translatable_symbols(ctx)
    if not syms:
        return "(no Python/TypeScript symbols found in changed files)"
    return ", ".join(f"{p}:{n}" for p, n, _ in syms[:8])
