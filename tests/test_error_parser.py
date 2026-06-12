from vericode.dafny.errors import format_errors_for_llm, parse_dafny_errors


SAMPLE_LOG = """
implementation.dfy(12,5): Error: a postcondition could not be proved on this return path
implementation.dfy(15,9): Error: assignment might update an array element not in the slice
Error: 2 resolution/type errors detected in implementation.dfy
"""


def test_parse_dafny_errors_extracts_locations() -> None:
    errors = parse_dafny_errors(SAMPLE_LOG)
    assert len(errors) >= 2
    assert errors[0].line == 12
    assert errors[0].column == 5
    assert "postcondition" in errors[0].message.lower()


def test_format_errors_for_llm() -> None:
    errors = parse_dafny_errors(SAMPLE_LOG)
    text = format_errors_for_llm(errors)
    assert "line 12" in text
    assert "postcondition" in text


def test_parse_empty_returns_fallback() -> None:
    errors = parse_dafny_errors("something went wrong")
    assert len(errors) == 1
    assert "something went wrong" in errors[0].message
