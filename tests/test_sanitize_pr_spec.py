from pathlib import Path

import pytest

from vericode.dafny.sanitize import sanitize_dafny_skeleton
from vericode.dafny.toolchain import resolve
from vericode.preflight import preflight


BROKEN_SLACK_SPEC = """
module Spec {
    function SlackResponseStylePrompts(config: map<string, object>): seq<string>
{
  []
}
"""

FIXED_EXPECTATION_SNIPPETS = [
    "function SlackResponseStylePrompts",
    "method SlackResponseStylePrompts",
    "assume false",
]


def test_pr_sanitize_repairs_module_and_adds_method_stub() -> None:
    out = sanitize_dafny_skeleton(BROKEN_SLACK_SPEC, pr_mode=True)
    assert "module Spec" not in out
    for snippet in FIXED_EXPECTATION_SNIPPETS:
        assert snippet in out


@pytest.mark.skipif(not preflight(require_openai=False, require_dafny=True).ok, reason="Dafny not installed")
def test_pr_sanitize_valid_skeleton_resolves(tmp_path: Path) -> None:
    broken = """
module Spec {
    function FooSpec(x: bool): seq<string> {
      []
    }
}
"""
    out = sanitize_dafny_skeleton(broken, pr_mode=True)
    path = tmp_path / "spec.dfy"
    path.write_text(out, encoding="utf-8")
    result = resolve(path, allow_warnings=True)
    assert result.ok, result.stderr
    assert "method Foo" in out
