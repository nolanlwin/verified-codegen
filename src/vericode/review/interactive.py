from __future__ import annotations

from enum import Enum

from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel


class ReviewAction(str, Enum):
    APPROVE = "approve"
    REVISE = "revise"
    ABORT = "abort"


def review_spec(
    console: Console,
    draft_spec: str,
    *,
    auto_approve: bool = False,
    sources_panel: str | None = None,
) -> tuple[ReviewAction, str | None]:
    if sources_panel:
        console.print(Panel(Markdown(sources_panel), title="PR Sources", border_style="blue"))
    console.print(Panel(Markdown(draft_spec), title="Draft Specification", border_style="cyan"))

    if auto_approve:
        console.print("[dim]Auto-approved (--auto)[/dim]")
        return ReviewAction.APPROVE, None

    while True:
        console.print("\n[bold][a][/bold] Approve  [bold][r][/bold] Revise with feedback  [bold][q][/bold] Abort")
        choice = console.input("[bold]Choice[/bold] (a/r/q): ").strip().lower()
        if choice in ("a", "approve"):
            return ReviewAction.APPROVE, None
        if choice in ("q", "abort", "quit"):
            return ReviewAction.ABORT, None
        if choice in ("r", "revise"):
            feedback = console.input("[bold]Revision feedback[/bold]: ").strip()
            if not feedback:
                console.print("[yellow]Please enter feedback or choose another option.[/yellow]")
                continue
            return ReviewAction.REVISE, feedback
        console.print("[yellow]Invalid choice. Enter a, r, or q.[/yellow]")
