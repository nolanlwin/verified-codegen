"""Convert between HumanEval Python values and Dafny-compiled Python runtime types."""

from __future__ import annotations

from typing import Any


def python_to_dafny(value: Any) -> Any:
    """Convert native Python arguments for a Dafny-compiled method."""
    if isinstance(value, str):
        import _dafny

        return _dafny.Seq(map(_dafny.CodePoint, value), isStr=True)
    if isinstance(value, list):
        import _dafny

        return _dafny.SeqWithoutIsStrInference(python_to_dafny(item) for item in value)
    return value


def dafny_to_python(value: Any) -> Any:
    """Convert Dafny-compiled return values to native Python for HumanEval asserts."""
    if value is None:
        return None

    try:
        import _dafny
    except ImportError:
        return value

    if isinstance(value, _dafny.Seq):
        return _seq_to_python(value)

    name = type(value).__name__
    if name.endswith("_IntResult"):
        return value.i
    if name.endswith("_StringResult"):
        return dafny_to_python(value.s)

    return value


def _seq_to_python(seq: Any) -> Any:
    import _dafny

    if not isinstance(seq, _dafny.Seq):
        return seq

    if len(seq) == 0:
        return "" if seq.isStr else []

    elems = list(seq.Elements)
    if seq.isStr or _is_char_seq(elems):
        return seq.VerbatimString(False)

    if elems and all(isinstance(item, _dafny.Seq) for item in elems):
        return [dafny_to_python(item) for item in elems]

    if elems and all(isinstance(item, int) for item in elems):
        return list(elems)

    return [dafny_to_python(item) for item in elems]


def _is_char_seq(elems: list[Any]) -> bool:
    import _dafny

    return bool(elems) and all(isinstance(item, (str, _dafny.CodePoint)) for item in elems)


def call_dafny_method(default_cls: Any, method_name: str, args: tuple[Any, ...]) -> Any:
    fn = getattr(default_cls, method_name)
    dafny_args = [python_to_dafny(arg) for arg in args]
    return dafny_to_python(fn(*dafny_args))
