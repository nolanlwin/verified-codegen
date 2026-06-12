"""End-to-end golden path tests (require OPENAI_API_KEY and Dafny)."""

from __future__ import annotations

import os
from pathlib import Path

import pytest

from vericode.artifacts.store import SessionStore
from vericode.dafny.toolchain import ensures_preserved
from vericode.pipeline import Pipeline
from vericode.preflight import preflight


def _e2e_ready() -> bool:
    return preflight(require_openai=True, require_dafny=True).ok


# Proven-easy prompts for reliable CI-style golden runs
PROMPTS = [
    "Double a non-negative integer and return the result.",
    "Add two integers and return their sum.",
    "Triple a non-negative integer and return the result.",
]

# Plan demo prompts (may require more retries / human review in practice)
COMPLEX_PROMPTS = [
    "Sort a list of customers by age. Each customer has a name and age.",
    "Return the maximum value in a non-empty list of integers.",
    "Filter a list of integers, keeping only those greater than a given threshold.",
]


@pytest.mark.skipif(not _e2e_ready(), reason="Requires OPENAI_API_KEY and Dafny")
@pytest.mark.parametrize("prompt", PROMPTS)
def test_golden_path_e2e(tmp_path: Path, prompt: str) -> None:
    store = SessionStore(root=tmp_path / "sessions")
    pipeline = Pipeline(store=store)

    session_id = pipeline.new_session(
        prompt,
        spec_model=os.environ.get("VERICODE_SPEC_MODEL", "gpt-4o-mini"),
        codegen_model=os.environ.get("VERICODE_CODEGEN_MODEL", "gpt-4o"),
        max_verify_retries=int(os.environ.get("VERICODE_MAX_RETRIES", "5")),
        auto_approve=True,
    )

    meta = store.read_meta(session_id)
    assert meta.status.value == "done", meta.error_message
    assert meta.verified

    final_py = store.session_dir(session_id) / "final.py"
    assert final_py.exists()
    assert len(final_py.read_text(encoding="utf-8")) > 0

    internal = store.read_text(session_id, "internal_spec.dfy")
    impl = store.read_text(session_id, "implementation.dfy")
    assert ensures_preserved(internal, impl)


@pytest.mark.skipif(
    not _e2e_ready() or not os.environ.get("VERICODE_RUN_COMPLEX"),
    reason="Set VERICODE_RUN_COMPLEX=1 to run complex demo prompts",
)
@pytest.mark.parametrize("prompt", COMPLEX_PROMPTS)
def test_golden_path_complex(tmp_path: Path, prompt: str) -> None:
    store = SessionStore(root=tmp_path / "sessions")
    pipeline = Pipeline(store=store)

    session_id = pipeline.new_session(
        prompt,
        spec_model=os.environ.get("VERICODE_SPEC_MODEL", "gpt-4o-mini"),
        codegen_model=os.environ.get("VERICODE_CODEGEN_MODEL", "gpt-4o"),
        max_verify_retries=int(os.environ.get("VERICODE_MAX_RETRIES", "10")),
        auto_approve=True,
    )

    meta = store.read_meta(session_id)
    assert meta.status.value == "done", meta.error_message
