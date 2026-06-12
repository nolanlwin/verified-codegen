from __future__ import annotations

from pathlib import Path
from typing import Optional

import typer
from rich.console import Console
from rich.table import Table

from vericode.artifacts.store import SessionStore
from vericode.pipeline import Pipeline
from vericode.preflight import preflight

app = typer.Typer(
    name="vericode",
    help="AI-assisted verified code generation via Dafny.",
    no_args_is_help=True,
)
console = Console()


def _store(sessions_root: Optional[Path]) -> SessionStore:
    if sessions_root:
        return SessionStore(root=sessions_root)
    return SessionStore()


def _resolve_session(store: SessionStore, session: Optional[str]) -> str:
    if session:
        if not store.exists(session):
            raise typer.BadParameter(f"Session not found: {session}")
        return session
    sessions = store.list_sessions()
    if not sessions:
        raise typer.BadParameter("No sessions found. Run `vericode new` first.")
    return sessions[0].session_id


@app.command("check")
def check_cmd() -> None:
    """Verify Dafny and OpenAI are configured."""
    result = preflight(require_openai=True, require_dafny=True)
    if result.ok:
        console.print("[green]Toolchain OK[/green]")
        console.print(f"  dafny: {result.dafny_path}")
        console.print("  openai: configured")
    else:
        for err in result.errors or []:
            console.print(f"[red]{err}[/red]")
        raise typer.Exit(code=1)


@app.command("pr")
def pr_cmd(
    pr_url: Optional[str] = typer.Argument(None, help="GitHub pull request URL."),
    focus: Optional[str] = typer.Option(None, help="Scoped symbol path:symbol (e.g. src/util.py:max_value)."),
    fixture: Optional[Path] = typer.Option(None, help="Recorded PR fixture JSON (offline/CI)."),
    patch: Optional[Path] = typer.Option(None, help="Local unified diff file."),
    meta: Optional[Path] = typer.Option(None, help="Metadata JSON for --patch mode."),
    spec_model: str = typer.Option("gpt-4o-mini", help="Model for spec generation."),
    codegen_model: str = typer.Option("gpt-4o", help="Model for translation."),
    auto: bool = typer.Option(False, "--auto", help="Auto-approve spec (not recommended for PRs)."),
    skip_run: bool = typer.Option(False, help="Stop after spec review without verification."),
    check_only: bool = typer.Option(
        False,
        "--check-only",
        help="Only ingest and assess verifiability; skip spec generation.",
    ),
    sessions_root: Optional[Path] = typer.Option(None, help="Custom sessions directory."),
) -> None:
    """Ingest a GitHub PR and run verify_pr workflow."""
    if not pr_url and not fixture and not patch:
        raise typer.BadParameter("Provide PR URL, --fixture, or --patch.")

    pipeline = Pipeline(store=_store(sessions_root), console=console)
    try:
        session_id = pipeline.new_pr_session(
            pr_url=pr_url,
            fixture=fixture,
            focus=focus,
            patch_file=patch,
            meta_file=meta,
            spec_model=spec_model,
            codegen_model=codegen_model,
            auto_approve=auto,
            skip_run=skip_run,
            check_only=check_only,
        )
        console.print(f"Session: {session_id}")
    except RuntimeError as exc:
        console.print(f"[red]{exc}[/red]")
        raise typer.Exit(code=1) from exc


@app.command("new")
def new_cmd(
    prompt: str = typer.Argument(..., help="Natural language programming request."),
    spec_model: str = typer.Option("gpt-4o-mini", help="Model for spec generation."),
    codegen_model: str = typer.Option("gpt-4o", help="Model for Dafny codegen."),
    max_retries: int = typer.Option(5, help="Max verification retries."),
    auto: bool = typer.Option(False, "--auto", help="Auto-approve spec (dev/testing)."),
    skip_run: bool = typer.Option(False, help="Stop after spec review without codegen."),
    sessions_root: Optional[Path] = typer.Option(None, help="Custom sessions directory."),
) -> None:
    """Start a new verified codegen session."""
    pipeline = Pipeline(store=_store(sessions_root), console=console)
    try:
        session_id = pipeline.new_session(
            prompt,
            spec_model=spec_model,
            codegen_model=codegen_model,
            max_verify_retries=max_retries,
            auto_approve=auto,
            skip_run=skip_run,
        )
        console.print(f"Session: {session_id}")
    except RuntimeError as exc:
        console.print(f"[red]{exc}[/red]")
        raise typer.Exit(code=1) from exc


@app.command("review")
def review_cmd(
    session: Optional[str] = typer.Option(None, help="Session ID."),
    auto: bool = typer.Option(False, "--auto", help="Auto-approve spec."),
    sessions_root: Optional[Path] = typer.Option(None, help="Custom sessions directory."),
) -> None:
    """Review and approve a draft specification."""
    store = _store(sessions_root)
    session_id = _resolve_session(store, session)
    pipeline = Pipeline(store=store, console=console)
    try:
        if not store.read_text_optional(session_id, "draft_spec.md"):
            pipeline.generate_spec(session_id)
        from vericode.review.interactive import ReviewAction

        action, feedback = pipeline.review_session(session_id, auto_approve=auto)
        if action == ReviewAction.REVISE and feedback:
            pipeline.revise_spec(session_id, feedback)
            action, _ = pipeline.review_session(session_id, auto_approve=auto)
        if action == ReviewAction.ABORT:
            store.fail_session(session_id, "Aborted during spec review.")
            raise typer.Exit(code=1)
    except RuntimeError as exc:
        console.print(f"[red]{exc}[/red]")
        raise typer.Exit(code=1) from exc


@app.command("run")
def run_cmd(
    session: Optional[str] = typer.Option(None, help="Session ID."),
    sessions_root: Optional[Path] = typer.Option(None, help="Custom sessions directory."),
) -> None:
    """Run codegen/translation, verification, and optional Python compilation."""
    store = _store(sessions_root)
    session_id = _resolve_session(store, session)
    pipeline = Pipeline(store=store, console=console)
    try:
        meta = store.read_meta(session_id)
        if meta.verification_mode == "verify_pr":
            pipeline.run_pr_verification(session_id)
        else:
            pipeline.run_codegen(session_id)
    except RuntimeError as exc:
        console.print(f"[red]{exc}[/red]")
        raise typer.Exit(code=1) from exc


@app.command("resume")
def resume_cmd(
    session_id: str = typer.Argument(..., help="Session ID to resume."),
    auto: bool = typer.Option(False, "--auto", help="Auto-approve spec if awaiting review."),
    sessions_root: Optional[Path] = typer.Option(None, help="Custom sessions directory."),
) -> None:
    """Resume an interrupted session."""
    pipeline = Pipeline(store=_store(sessions_root), console=console)
    try:
        pipeline.resume(session_id, auto_approve=auto)
    except RuntimeError as exc:
        console.print(f"[red]{exc}[/red]")
        raise typer.Exit(code=1) from exc


@app.command("show")
def show_cmd(
    session_id: str = typer.Argument(..., help="Session ID."),
    debug: bool = typer.Option(False, "--debug", help="Show internal Dafny artifacts."),
    sessions_root: Optional[Path] = typer.Option(None, help="Custom sessions directory."),
) -> None:
    """Display session status and artifacts."""
    store = _store(sessions_root)
    if not store.exists(session_id):
        console.print(f"[red]Session not found: {session_id}[/red]")
        raise typer.Exit(code=1)

    meta = store.read_meta(session_id)
    console.print(f"[bold]Session[/bold] {session_id}")
    console.print(f"Status: {meta.status.value}")
    console.print(f"Verified: {meta.verified} (attempts: {meta.verify_attempts})")
    if meta.error_message:
        console.print(f"[red]Error:[/red] {meta.error_message}")

    if meta.source_type == "github_pr":
        console.print(f"Source: {meta.source_ref or 'github_pr'}")
        if meta.focus_symbol:
            console.print(f"Focus: {meta.focus_symbol} ({meta.focus_language or 'unknown'})")

    for name in ("prompt.txt", "draft_spec.md", "verified_spec.md", "critique.md", "final.py"):
        path = store.session_dir(session_id) / name
        if path.exists():
            console.print(f"\n[bold]{name}[/bold]\n{path.read_text(encoding='utf-8')[:4000]}")

    if debug:
        for name in ("context.json", "internal_spec.dfy", "translation.dfy", "implementation.dfy", "verify.log", "critique.json"):
            path = store.session_dir(session_id) / name
            if path.exists():
                console.print(f"\n[dim bold]{name}[/dim bold]\n{path.read_text(encoding='utf-8')[:4000]}")


@app.command("list")
def list_cmd(
    sessions_root: Optional[Path] = typer.Option(None, help="Custom sessions directory."),
) -> None:
    """List recent sessions."""
    store = _store(sessions_root)
    sessions = store.list_sessions()
    if not sessions:
        console.print("No sessions yet.")
        return

    table = Table(title="Vericode Sessions")
    table.add_column("ID")
    table.add_column("Status")
    table.add_column("Verified")
    table.add_column("Source")
    table.add_column("Created")

    for meta in sessions:
        table.add_row(
            meta.session_id,
            meta.status.value,
            "yes" if meta.verified else "no",
            meta.source_type,
            meta.created_at.isoformat(timespec="seconds"),
        )
    console.print(table)


bench_app = typer.Typer(help="Benchmark vericode on standard datasets.")
app.add_typer(bench_app, name="bench")


@bench_app.command("humaneval")
def bench_humaneval_cmd(
    limit: Optional[int] = typer.Option(None, help="Max number of tasks to run."),
    offset: int = typer.Option(0, help="Skip first N tasks (sorted by task id)."),
    task_id: Optional[list[str]] = typer.Option(None, "--task-id", help="Run specific task(s)."),
    output: Path = typer.Option(
        Path(".vericode/bench/humaneval/results.jsonl"),
        help="JSONL results file (one row per task_id, updated in place).",
    ),
    bench_root: Path = typer.Option(
        Path(".vericode/bench/humaneval"),
        help="Benchmark workspace root.",
    ),
    resume: bool = typer.Option(True, help="Skip task_ids already present in output."),
    spec_model: str = typer.Option("gpt-4o-mini", help="Model for spec generation."),
    codegen_model: str = typer.Option("gpt-4o", help="Model for Dafny codegen."),
    max_retries: int = typer.Option(10, help="Max Dafny verification retries per task."),
    test_timeout: float = typer.Option(5.0, help="HumanEval test timeout (seconds)."),
    quiet: bool = typer.Option(False, help="Reduce pipeline output."),
    summary_only: bool = typer.Option(False, help="Print summary of existing results and exit."),
) -> None:
    """Run vericode on OpenAI HumanEval and evaluate compiled Python with official tests."""
    from vericode.bench.humaneval_runner import print_summary, run_humaneval_benchmark

    if summary_only:
        print_summary(console, output)
        return

    try:
        run_results = run_humaneval_benchmark(
            results_path=output,
            bench_root=bench_root,
            limit=limit,
            offset=offset,
            task_ids=task_id,
            resume=resume,
            spec_model=spec_model,
            codegen_model=codegen_model,
            max_retries=max_retries,
            test_timeout=test_timeout,
            quiet=quiet,
            console=console,
        )
    except RuntimeError as exc:
        console.print(f"[red]{exc}[/red]")
        raise typer.Exit(code=1) from exc

    print_summary(console, run_results=run_results)


def main() -> None:
    app()


if __name__ == "__main__":
    main()
