from pathlib import Path

from vericode.bench.evaluate import build_check_program, resolve_generated_dir, run_humaneval_tests
from vericode.bench.humaneval_prompt import pick_impl_method, list_static_methods, to_pascal_case, to_vericode_prompt


SAMPLE_PY = '''
class default__:
    @staticmethod
    def HasCloseElements(numbers, threshold):
        return True

    @staticmethod
    def HasCloseElementsSpec(numbers, threshold):
        return True
'''


def test_to_pascal_case() -> None:
    assert to_pascal_case("has_close_elements") == "HasCloseElements"


def test_pick_impl_method() -> None:
    methods = list_static_methods(SAMPLE_PY)
    assert pick_impl_method(methods, "has_close_elements") == "HasCloseElements"


def test_spec_agent_does_not_load_few_shot_prompts() -> None:
    from vericode.llm.client import PROMPTS_DIR
    from vericode.llm.spec_agent import SpecAgent

    assert not list(PROMPTS_DIR.glob("*few_shot*"))
    agent = SpecAgent.__new__(SpecAgent)
    agent.pr_mode = False
    from vericode.llm.client import load_prompt

    agent.system_prompt = load_prompt("spec_system.txt")
    assert "function ProblemSpec" in agent.system_prompt or "Spec functions" in agent.system_prompt


def test_to_vericode_prompt_includes_entry_point() -> None:
    problem = {
        "entry_point": "has_close_elements",
        "prompt": "def has_close_elements(...):\n    \"\"\"doc\"\"\"\n",
    }
    prompt = to_vericode_prompt(problem)
    assert "has_close_elements" in prompt
    assert "doc" in prompt


def test_build_check_program_contains_wrapper() -> None:
    program = build_check_program(
        generated_dir=Path("/tmp/out"),
        entry_point="has_close_elements",
        dafny_method="HasCloseElements",
        test_code="def check(candidate):\n    assert candidate(1, 2) == True",
    )
    assert "HasCloseElements" in program
    assert "check(has_close_elements)" in program


def test_spec_generation_ok() -> None:
    from vericode.bench.evaluate import spec_generation_ok

    assert not spec_generation_ok("Spec skeleton failed verification after repair.")
    assert spec_generation_ok("Verification failed after 5 retries.")
    assert spec_generation_ok(None)


def test_upsert_result_replaces_duplicate_task(tmp_path: Path) -> None:
    from vericode.bench.humaneval_runner import BenchResult, load_results_deduped, upsert_result

    path = tmp_path / "results.jsonl"
    first = BenchResult(task_id="HumanEval/0", entry_point="f", status="failed", spec_ok=False)
    second = BenchResult(task_id="HumanEval/0", entry_point="f", status="done", spec_ok=True)
    upsert_result(path, first)
    upsert_result(path, second)
    rows = load_results_deduped(path)
    assert len(rows) == 1
    assert rows[0].status == "done"
    assert rows[0].spec_ok is True


def test_summarize_run_results_only() -> None:
    from vericode.bench.humaneval_runner import BenchResult, summarize_results

    rows = [
        BenchResult(task_id="HumanEval/0", entry_point="a", status="done", spec_ok=True, verified=True),
        BenchResult(task_id="HumanEval/1", entry_point="b", status="failed", spec_ok=True, verified=False),
    ]
    summary = summarize_results(rows)
    assert summary["total"] == 2
    assert summary["spec_ok_rate"] == 1.0
    assert summary["verified_rate"] == 0.5


def test_resolve_generated_dir_prefers_output_generated(tmp_path: Path) -> None:
    session = tmp_path / "sess"
    gen = session / "output" / "generated"
    gen.mkdir(parents=True)
    (gen / "module_.py").write_text("# stub", encoding="utf-8")
    assert resolve_generated_dir(session) == gen.resolve()


def test_adapter_on_verified_session_if_present() -> None:
    """Regression: verified Dafny output must pass HumanEval after type conversion."""
    from pathlib import Path
    import json

    results = Path(__file__).resolve().parents[1] / ".vericode" / "bench" / "humaneval" / "results.jsonl"
    if not results.is_file():
        return

    try:
        from human_eval.data import read_problems
    except ImportError:
        return

    problems = read_problems()
    base = results.parent / "sessions"
    for line in results.read_text().splitlines():
        if not line.strip():
            continue
        row = json.loads(line)
        if not row.get("verified") or row.get("task_id") != "HumanEval/103":
            continue
        session = base / row["session_id"]
        gen = resolve_generated_dir(session)
        if not gen:
            continue
        final = session / "final.py"
        if not final.is_file():
            continue
        method = pick_impl_method(list_static_methods(final.read_text()), row["entry_point"])
        if not method:
            continue
        outcome = run_humaneval_tests(problems[row["task_id"]], gen, method)
        assert outcome["passed"], outcome["result"][:200]
        return
