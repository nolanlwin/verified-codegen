from __future__ import annotations

from vericode.models import TaskContext


def format_sources_panel(context: TaskContext) -> str:
    lines = [
        f"**PR #{context.pr_number}:** {context.title}",
        f"**URL:** {context.url or '(local fixture)'}",
    ]
    if context.verification_scope:
        lines.append(f"**Focus:** `{context.verification_scope}`")
    if context.focus:
        lines.append(f"**Language:** {context.focus.language}")
        lines.append("")
        lines.append("### Scoped source")
        lines.append(f"```{context.focus.language}")
        lines.append(context.focus.source)
        lines.append("```")
    if context.review_comments:
        lines.append("")
        lines.append("### Review comments")
        for c in context.review_comments[:5]:
            loc = f" `{c.path}:{c.line}`" if c.path else ""
            lines.append(f"-{loc} @{c.author}: {c.body[:300]}")
    return "\n".join(lines)
