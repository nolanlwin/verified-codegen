from vericode.bench.dafny_adapter import dafny_to_python, python_to_dafny


def test_python_str_roundtrip() -> None:
    try:
        import _dafny
    except ImportError:
        return

    s = "hello"
    dafny_s = python_to_dafny(s)
    assert isinstance(dafny_s, _dafny.Seq)
    assert dafny_to_python(dafny_s) == s
    assert dafny_to_python(python_to_dafny("")) == ""


def test_python_list_int_roundtrip() -> None:
    try:
        import _dafny
    except ImportError:
        return

    xs = [1, 2, 3]
    dafny_xs = python_to_dafny(xs)
    assert isinstance(dafny_xs, _dafny.Seq)
    assert dafny_to_python(dafny_xs) == xs
    assert dafny_to_python(python_to_dafny([])) == []


def test_seq_of_strings() -> None:
    try:
        import _dafny
    except ImportError:
        return

    inner = [python_to_dafny("ab"), python_to_dafny("cd")]
    outer = _dafny.SeqWithoutIsStrInference(inner)
    assert dafny_to_python(outer) == ["ab", "cd"]
