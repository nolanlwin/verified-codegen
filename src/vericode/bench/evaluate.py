from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any


def build_check_program(
    *,
    generated_dir: Path,
    entry_point: str,
    dafny_method: str,
    test_code: str,
) -> str:
    return f"""import sys
sys.path.insert(0, {str(generated_dir)!r})

from module_ import default__
from vericode.bench.dafny_adapter import call_dafny_method


def {entry_point}(*args, **kwargs):
    if kwargs:
        raise TypeError("Dafny wrapper does not support keyword arguments")
    return call_dafny_method(default__, {dafny_method!r}, args)


{test_code}

check({entry_point})
"""


def run_humaneval_tests(
    problem: dict,
    generated_dir: Path,
    dafny_method: str,
    *,
    timeout: float = 5.0,
) -> dict[str, Any]:
    generated_dir = generated_dir.resolve()
    if not generated_dir.is_dir():
        return {"passed": False, "result": "failed: missing generated module directory"}

    program = build_check_program(
        generated_dir=generated_dir,
        entry_point=problem["entry_point"],
        dafny_method=dafny_method,
        test_code=problem["test"],
    )

    with tempfile.TemporaryDirectory() as tmp:
        script = Path(tmp) / "check.py"
        script.write_text(program, encoding="utf-8")
        try:
            proc = subprocess.run(
                [sys.executable, str(script)],
                capture_output=True,
                text=True,
                timeout=timeout + 1,
                cwd=tmp,
            )
        except subprocess.TimeoutExpired:
            return {"passed": False, "result": "timed out"}

        if proc.returncode == 0:
            return {"passed": True, "result": "passed"}

        detail = proc.stderr.strip() or proc.stdout.strip() or f"exit {proc.returncode}"
        return {"passed": False, "result": f"failed: {detail[:500]}"}


def resolve_generated_dir(session_dir: Path) -> Path | None:
    session_dir = session_dir.resolve()
    candidates = [
        session_dir / "output" / "generated",
        session_dir / "build-py",
    ]
    for path in candidates:
        if (path / "module_.py").is_file():
            return path.resolve()
    output = session_dir / "output"
    if output.is_dir():
        for path in sorted(output.rglob("module_.py")):
            return path.parent.resolve()
    return None


def spec_generation_ok(error_message: str | None) -> bool:
    if not error_message:
        return True
    lowered = error_message.lower()
    if "spec skeleton" in lowered:
        return False
    return True
