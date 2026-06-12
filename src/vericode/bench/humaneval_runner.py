from __future__ import annotations

import io
import json
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

from pydantic import BaseModel, Field
from rich.console import Console
from rich.table import Table

from vericode.artifacts.store import SessionStore
from vericode.bench.evaluate import resolve_generated_dir, run_humaneval_tests, spec_generation_ok
from vericode.bench.humaneval_prompt import list_static_methods, pick_impl_method, to_vericode_prompt
from vericode.models import SessionStatus
from vericode.pipeline import Pipeline
from vericode.preflight import preflight


class BenchResult(BaseModel):
    task_id: str
    session_id: str | None = None
    entry_point: str
    status: str
    spec_ok: bool = False
    verified: bool = False
    compiled: bool = False
    tests_passed: bool = False
    test_result: str | None = None
    dafny_method: str | None = None
    error_stage: str | None = None
    error_message: str | None = None
    duration_sec: float = 0.0
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


def load_problems() -> dict[str, dict]:
    from human_eval.data import read_problems

    return read_problems()


def load_all_results(results_path: Path) -> list[BenchResult]:
    if not results_path.is_file():
        return []
    rows: list[BenchResult] = []
    for line in results_path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        rows.append(BenchResult.model_validate(json.loads(line)))
    return rows


def load_results_deduped(results_path: Path) -> list[BenchResult]:
    """Return the latest result per task_id (file order wins)."""
    by_id: dict[str, BenchResult] = {}
    for row in load_all_results(results_path):
        by_id[row.task_id] = row
    return [by_id[task_id] for task_id in sorted(by_id)]


def load_completed_task_ids(results_path: Path) -> set[str]:
    return {row.task_id for row in load_results_deduped(results_path)}


def save_results(results_path: Path, rows: list[BenchResult]) -> None:
    results_path.parent.mkdir(parents=True, exist_ok=True)
    lines = [row.model_dump_json() for row in rows]
    results_path.write_text("\n".join(lines) + ("\n" if lines else ""), encoding="utf-8")


def upsert_result(results_path: Path, result: BenchResult) -> None:
    rows = [row for row in load_all_results(results_path) if row.task_id != result.task_id]
    rows.append(result)
    save_results(results_path, rows)


def summarize_results(results: Iterable[BenchResult]) -> dict[str, Any]:
    rows = list(results)
    total = len(rows)
    if total == 0:
        return {"total": 0}

    def rate(field: str) -> float:
        return sum(1 for r in rows if getattr(r, field)) / total

    return {
        "total": total,
        "spec_ok_rate": rate("spec_ok"),
        "verified_rate": rate("verified"),
        "compiled_rate": rate("compiled"),
        "tests_passed_rate": rate("tests_passed"),
        "done_rate": sum(1 for r in rows if r.status == SessionStatus.DONE.value) / total,
    }


def run_humaneval_benchmark(
    *,
    results_path: Path,
    bench_root: Path,
    limit: int | None = None,
    offset: int = 0,
    task_ids: list[str] | None = None,
    resume: bool = True,
    spec_model: str = "gpt-4o-mini",
    codegen_model: str = "gpt-4o",
    max_retries: int = 10,
    test_timeout: float = 5.0,
    quiet: bool = False,
    console: Console | None = None,
) -> list[BenchResult]:
    check = preflight(require_openai=True, require_dafny=True)
    if not check.ok:
        raise RuntimeError("\n".join(check.errors or []))

    console = console or Console(quiet=quiet)
    problems = load_problems()
    ordered_ids = sorted(problems.keys())
    if task_ids:
        ordered_ids = [tid for tid in task_ids if tid in problems]
    else:
        ordered_ids = ordered_ids[offset:]
        if limit is not None:
            ordered_ids = ordered_ids[:limit]

    completed = load_completed_task_ids(results_path) if resume else set()
    results: list[BenchResult] = []

    pipeline_console = Console(file=io.StringIO()) if quiet else console

    for task_id in ordered_ids:
        if task_id in completed:
            continue

        problem = problems[task_id]
        entry_point = problem["entry_point"]
        started = time.time()
        store = SessionStore(root=bench_root / "sessions")
        pipeline = Pipeline(store=store, console=pipeline_console)

        if not quiet:
            console.print(f"[bold]Task[/bold] {task_id} ({entry_point})")

        result = BenchResult(
            task_id=task_id,
            entry_point=entry_point,
            status=SessionStatus.FAILED.value,
        )

        session_id: str | None = None
        try:
            session_id = pipeline.new_session(
                to_vericode_prompt(problem),
                spec_model=spec_model,
                codegen_model=codegen_model,
                max_verify_retries=max_retries,
                auto_approve=True,
            )
        except Exception as exc:  # noqa: BLE001 - record and continue benchmark
            sessions = store.list_sessions()
            if sessions:
                session_id = sessions[0].session_id
            result.error_stage = result.error_stage or "pipeline"
            result.error_message = f"{type(exc).__name__}: {exc}"
            if session_id:
                meta = store.read_meta(session_id)
                result.session_id = session_id
                result.status = meta.status.value
                result.spec_ok = spec_generation_ok(meta.error_message)
                result.verified = meta.verified
                result.compiled = (store.session_dir(session_id) / "final.py").is_file()
                if meta.error_message and not result.error_message:
                    result.error_message = meta.error_message
                elif meta.error_message and "spec skeleton" in meta.error_message.lower():
                    result.error_message = meta.error_message
                if meta.error_message and "spec skeleton" in meta.error_message.lower():
                    result.error_stage = "spec"
                elif not meta.verified and result.spec_ok:
                    result.error_stage = "verify"
            result.duration_sec = round(time.time() - started, 2)
            upsert_result(results_path, result)
            results.append(result)
            if not quiet:
                console.print(f"  [red]FAIL[/red] {result.error_stage}: {result.error_message}")
            continue

        try:
            result.session_id = session_id
            meta = store.read_meta(session_id)
            result.status = meta.status.value
            result.spec_ok = spec_generation_ok(meta.error_message)
            result.verified = meta.verified
            result.compiled = (store.session_dir(session_id) / "final.py").is_file()
            result.error_message = meta.error_message

            if meta.status == SessionStatus.DONE:
                generated_dir = resolve_generated_dir(store.session_dir(session_id))
                final_py = store.session_dir(session_id) / "final.py"
                source = final_py.read_text(encoding="utf-8") if final_py.is_file() else ""
                dafny_method = pick_impl_method(list_static_methods(source), entry_point)

                if not generated_dir or not dafny_method:
                    result.error_stage = "adapter"
                    result.error_message = "Could not locate generated module or entry method"
                    result.test_result = "failed: adapter error"
                else:
                    result.dafny_method = dafny_method
                    test_outcome = run_humaneval_tests(
                        problem,
                        generated_dir,
                        dafny_method,
                        timeout=test_timeout,
                    )
                    result.tests_passed = test_outcome["passed"]
                    result.test_result = test_outcome["result"]
            else:
                if meta.error_message and "spec skeleton" in meta.error_message.lower():
                    result.error_stage = "spec"
                elif not meta.verified:
                    result.error_stage = "verify"
                else:
                    result.error_stage = "compile"

        except Exception as exc:  # noqa: BLE001 - record benchmark failure
            result.error_stage = result.error_stage or "pipeline"
            result.error_message = str(exc)

        result.duration_sec = round(time.time() - started, 2)
        upsert_result(results_path, result)
        results.append(result)

        if not quiet:
            status = "[green]PASS[/green]" if result.tests_passed else "[red]FAIL[/red]"
            console.print(
                f"  {status} verified={result.verified} compiled={result.compiled} "
                f"({result.duration_sec}s)"
            )
            if result.test_result and not result.tests_passed:
                console.print(f"  [dim]{result.test_result[:200]}[/dim]")

    return results


def print_summary(
    console: Console,
    results_path: Path | None = None,
    *,
    run_results: list[BenchResult] | None = None,
) -> None:
    if run_results is not None:
        rows = run_results
        title = "HumanEval Benchmark Summary (this run)"
    elif results_path is not None and results_path.is_file():
        rows = load_results_deduped(results_path)
        title = "HumanEval Benchmark Summary (all tasks)"
    else:
        console.print("No results yet.")
        return

    if not rows:
        console.print("No tasks in this summary.")
        return

    summary = summarize_results(rows)

    table = Table(title=title)
    table.add_column("Metric")
    table.add_column("Rate")
    table.add_row("Tasks", str(summary["total"]))
    table.add_row("Spec OK", f"{summary.get('spec_ok_rate', 0):.1%}")
    table.add_row("Dafny verified", f"{summary.get('verified_rate', 0):.1%}")
    table.add_row("Compiled", f"{summary.get('compiled_rate', 0):.1%}")
    table.add_row("HumanEval tests passed", f"{summary.get('tests_passed_rate', 0):.1%}")
    table.add_row("Pipeline done", f"{summary.get('done_rate', 0):.1%}")
    console.print(table)
