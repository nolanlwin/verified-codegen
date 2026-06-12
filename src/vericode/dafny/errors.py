from __future__ import annotations

import re
from typing import Iterable

from vericode.models import DafnyError


# Dafny error lines often look like:
# file.dfy(12,5): Error: message
# or: file.dfy(12,5): Verification of 'Method' timed out
_ERROR_RE = re.compile(
    r"(?P<file>[^\(\s]+)\((?P<line>\d+),(?P<col>\d+)\):\s*(?P<kind>[\w ]+):\s*(?P<message>.+)"
)
_SIMPLE_ERROR_RE = re.compile(r"Error:\s*(?P<message>.+)")


def parse_dafny_errors(output: str) -> list[DafnyError]:
    errors: list[DafnyError] = []
    seen: set[str] = set()

    for line in output.splitlines():
        line = line.strip()
        if not line:
            continue
        match = _ERROR_RE.search(line)
        if match:
            message = match.group("message").strip()
            key = f"{match.group('line')}:{message}"
            if key in seen:
                continue
            seen.add(key)
            errors.append(
                DafnyError(
                    line=int(match.group("line")),
                    column=int(match.group("col")),
                    error_type=match.group("kind").strip(),
                    message=message,
                )
            )
            continue
        simple = _SIMPLE_ERROR_RE.search(line)
        if simple:
            message = simple.group("message").strip()
            if message not in seen:
                seen.add(message)
                errors.append(DafnyError(message=message))

    if not errors and output.strip():
        errors.append(DafnyError(message=output.strip()[:2000]))

    return errors


def format_errors_for_llm(errors: Iterable[DafnyError]) -> str:
    lines: list[str] = []
    for err in errors:
        loc = ""
        if err.line is not None:
            loc = f"line {err.line}"
            if err.column is not None:
                loc += f", col {err.column}"
            loc = f" ({loc})"
        kind = f" [{err.error_type}]" if err.error_type else ""
        lines.append(f"-{loc}{kind}: {err.message}")
    return "\n".join(lines) if lines else "Unknown verification error."
