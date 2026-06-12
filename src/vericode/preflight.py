from __future__ import annotations

import os
import shutil
from dataclasses import dataclass
from typing import Optional


@dataclass
class PreflightResult:
    ok: bool
    dafny_path: Optional[str] = None
    openai_configured: bool = False
    errors: list[str] | None = None


def find_dafny() -> Optional[str]:
    return shutil.which("dafny")


def check_openai_key() -> bool:
    return bool(os.environ.get("OPENAI_API_KEY"))


def preflight(*, require_openai: bool = True, require_dafny: bool = True) -> PreflightResult:
    errors: list[str] = []
    dafny_path = find_dafny()
    openai_configured = check_openai_key()

    if require_dafny and not dafny_path:
        errors.append(
            "Dafny not found on PATH. Install Dafny 4.x from https://dafny.org/latest/Installation"
        )
    if require_openai and not openai_configured:
        errors.append("OPENAI_API_KEY environment variable is not set.")

    return PreflightResult(
        ok=len(errors) == 0,
        dafny_path=dafny_path,
        openai_configured=openai_configured,
        errors=errors,
    )
