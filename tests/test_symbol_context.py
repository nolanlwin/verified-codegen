from pathlib import Path

import pytest

from vericode.dafny.spec_semantics import validate_spec_semantics
from vericode.sources.github import ingest_pr
from vericode.sources.symbol_context import analyze_symbol_context, render_symbol_context_for_prompt

FIXTURES = Path(__file__).parent / "fixtures" / "pr"


def test_analyze_slack_symbol_context() -> None:
    ctx = ingest_pr(fixture=FIXTURES / "slack_response_style.json")
    assert ctx.focus is not None
    symbol_context = analyze_symbol_context(ctx)

    assert len(symbol_context.abstract_parameters) == 1
    assert symbol_context.abstract_parameters[0].dafny_name == "has_slack_thread_context"
    assert symbol_context.abstract_parameters[0].replaces_python_param == "config"

    assert len(symbol_context.external_constants) == 1
    assert symbol_context.external_constants[0].name == "SLACK_RESPONSE_STYLE_PROMPT"
    assert symbol_context.external_constants[0].marker == "slack_response_style"

    assert symbol_context.test_oracles
    rendered = render_symbol_context_for_prompt(symbol_context)
    assert "has_slack_thread_context" in rendered
    assert "slack_response_style" in rendered


def test_semantic_validation_flags_constant_stub() -> None:
    ctx = ingest_pr(fixture=FIXTURES / "slack_response_style.json")
    symbol_context = analyze_symbol_context(ctx)
    bad_skeleton = """
function SlackResponseStyleSpec(has_slack_thread_context: bool): seq<string>
{
  []
}

method SlackResponseStyle(has_slack_thread_context: bool) returns (result: seq<string>)
  ensures result == SlackResponseStyleSpec(has_slack_thread_context)
{
  assume false;
}
"""
    issues = validate_spec_semantics(bad_skeleton, symbol_context)
    assert any("branch" in issue.lower() or "conditional" in issue.lower() for issue in issues)


def test_semantic_validation_flags_stub_with_decreases_clause() -> None:
    """Regression: decreases between signature and body must not disable extraction."""
    ctx = ingest_pr(fixture=FIXTURES / "slack_response_style.json")
    symbol_context = analyze_symbol_context(ctx)
    bad_skeleton = """
function SlackResponseStyleSpec(has_slack_thread_context: bool): seq<string>
  decreases 0
{
  []
}

method SlackResponseStyle(has_slack_thread_context: bool) returns (result: seq<string>)
  ensures result == SlackResponseStyleSpec(has_slack_thread_context)
{
  assume false;
}
"""
    issues = validate_spec_semantics(bad_skeleton, symbol_context)
    assert issues
    assert any("branch" in issue.lower() or "conditional" in issue.lower() for issue in issues)


def test_semantic_validation_accepts_conditional_spec() -> None:
    ctx = ingest_pr(fixture=FIXTURES / "slack_response_style.json")
    symbol_context = analyze_symbol_context(ctx)
    good_skeleton = """
function SlackResponseStyleSpec(has_slack_thread_context: bool): seq<string>
{
  if has_slack_thread_context then ["slack_response_style"] else []
}

method SlackResponseStyle(has_slack_thread_context: bool) returns (result: seq<string>)
  ensures result == SlackResponseStyleSpec(has_slack_thread_context)
{
  assume false;
}
"""
    issues = validate_spec_semantics(good_skeleton, symbol_context)
    assert not issues
