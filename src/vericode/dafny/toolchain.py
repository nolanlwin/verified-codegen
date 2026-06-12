from __future__ import annotations

import glob
import re
import subprocess
from pathlib import Path
from typing import Optional

from vericode.dafny.errors import parse_dafny_errors
from vericode.models import BuildResult, VerificationResult


def verify(
    dfy_path: Path,
    *,
    timeout: int = 120,
    dafny_bin: str = "dafny",
    allow_warnings: bool = False,
) -> VerificationResult:
    cmd = [dafny_bin, "verify"]
    if allow_warnings:
        cmd.append("--allow-warnings")
    cmd.append(str(dfy_path))
    return _run_dafny(cmd, dfy_path, timeout)


def resolve(
    dfy_path: Path,
    *,
    timeout: int = 60,
    dafny_bin: str = "dafny",
    allow_warnings: bool = False,
) -> VerificationResult:
    cmd = [dafny_bin, "resolve"]
    if allow_warnings:
        cmd.append("--allow-warnings")
    cmd.append(str(dfy_path))
    return _run_dafny(cmd, dfy_path, timeout)


def _run_dafny(cmd: list[str], dfy_path: Path, timeout: int) -> VerificationResult:
    try:
        proc = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=timeout,
            check=False,
        )
    except subprocess.TimeoutExpired as exc:
        output = (exc.stdout or "") + (exc.stderr or "")
        return VerificationResult(
            ok=False,
            stdout=exc.stdout or "",
            stderr=output,
            errors=parse_dafny_errors(output),
            returncode=-1,
        )

    combined = proc.stdout + proc.stderr
    errors = parse_dafny_errors(combined)
    return VerificationResult(
        ok=proc.returncode == 0,
        stdout=proc.stdout,
        stderr=proc.stderr,
        errors=errors,
        returncode=proc.returncode,
    )


def build_python(
    dfy_path: Path,
    output_dir: Path,
    *,
    timeout: int = 180,
    dafny_bin: str = "dafny",
) -> BuildResult:
    output_dir.mkdir(parents=True, exist_ok=True)
    output_base = output_dir if output_dir.suffix != "-py" else output_dir.with_name(output_dir.stem)
    cmd = [
        dafny_bin,
        "build",
        "-t",
        "py",
        "-o",
        str(output_base),
        str(dfy_path),
    ]
    try:
        proc = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=timeout,
            check=False,
        )
    except subprocess.TimeoutExpired as exc:
        output = (exc.stdout or "") + (exc.stderr or "")
        return BuildResult(
            ok=False,
            stdout=exc.stdout or "",
            stderr=output,
            returncode=-1,
        )

    generated_dir = Path(f"{output_base}-py")
    main_py = _find_main_py(generated_dir, dfy_path)
    return BuildResult(
        ok=proc.returncode == 0 and main_py is not None,
        stdout=proc.stdout,
        stderr=proc.stderr,
        output_dir=str(generated_dir) if generated_dir.exists() else str(output_dir),
        main_py=main_py,
        returncode=proc.returncode,
    )


def _find_main_py(output_dir: Path, dfy_path: Path) -> Optional[str]:
    if not output_dir.is_dir():
        return None

    stem = dfy_path.stem
    candidates = [
        output_dir / f"{stem}.py",
        output_dir / "module_.py",
        output_dir / "__main__.py",
        output_dir / stem / f"{stem}.py",
    ]
    for candidate in candidates:
        if candidate.is_file():
            return str(candidate)

    py_files = sorted(glob.glob(str(output_dir / "**" / "*.py"), recursive=True))
    if py_files:
        for path in py_files:
            name = Path(path).name
            if name in ("module_.py", "__main__.py"):
                return path
        for path in py_files:
            if Path(path).stem == stem:
                return path
        return py_files[0]
    return None


def extract_ensures_clauses(source: str) -> list[str]:
    """Return normalized ensures clause bodies from Dafny source."""
    clauses: list[str] = []
    for match in re.finditer(r"\bensures\b", source):
        rest = source[match.end() :].lstrip()
        end = len(rest)
        for delim in (" ensures ", " requires ", " decreases ", " reads ", " modifies ", "{"):
            idx = rest.find(delim)
            if idx != -1:
                end = min(end, idx)
        body = re.sub(r"\s+", " ", rest[:end].strip())
        if body:
            clauses.append(body)
    return sorted(clauses)


def ensures_preserved(original: str, updated: str) -> bool:
    """True if updated source contains all ensures clauses from original."""
    original_clauses = extract_ensures_clauses(original)
    updated_clauses = extract_ensures_clauses(updated)
    return all(clause in updated_clauses for clause in original_clauses)
