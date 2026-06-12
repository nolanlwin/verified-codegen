import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_ as module_
import _dafny as _dafny
import System_ as System_

# Module: module_

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def IsVowel(c):
        return ((((((((((c) == (_dafny.CodePoint('a'))) or ((c) == (_dafny.CodePoint('e')))) or ((c) == (_dafny.CodePoint('i')))) or ((c) == (_dafny.CodePoint('o')))) or ((c) == (_dafny.CodePoint('u')))) or ((c) == (_dafny.CodePoint('A')))) or ((c) == (_dafny.CodePoint('E')))) or ((c) == (_dafny.CodePoint('I')))) or ((c) == (_dafny.CodePoint('O')))) or ((c) == (_dafny.CodePoint('U')))

    @staticmethod
    def CountConsonantsSpec(w):
        d_0___accumulator_ = 0
        while True:
            with _dafny.label():
                if (len(w)) == (0):
                    return (0) + (d_0___accumulator_)
                elif True:
                    d_0___accumulator_ = (d_0___accumulator_) + ((0 if (((w)[0]) == (_dafny.CodePoint(' '))) or (default__.IsVowel((w)[0])) else 1))
                    in0_ = _dafny.SeqWithoutIsStrInference((w)[1::])
                    w = in0_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def KeepWordSpec(w, n):
        if ((len(w)) > (0)) and ((default__.CountConsonantsSpec(w)) == (n)):
            return _dafny.SeqWithoutIsStrInference([w])
        elif True:
            return _dafny.SeqWithoutIsStrInference([])

    @staticmethod
    def SelectWordsAux(s, n, current):
        d_0___accumulator_ = _dafny.SeqWithoutIsStrInference([])
        while True:
            with _dafny.label():
                if (len(s)) == (0):
                    return (d_0___accumulator_) + (default__.KeepWordSpec(current, n))
                elif ((s)[0]) == (_dafny.CodePoint(' ')):
                    d_0___accumulator_ = (d_0___accumulator_) + (default__.KeepWordSpec(current, n))
                    in0_ = _dafny.SeqWithoutIsStrInference((s)[1::])
                    in1_ = n
                    in2_ = _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, ""))
                    s = in0_
                    n = in1_
                    current = in2_
                    raise _dafny.TailCall()
                elif True:
                    in3_ = _dafny.SeqWithoutIsStrInference((s)[1::])
                    in4_ = n
                    in5_ = (current) + (_dafny.SeqWithoutIsStrInference((s)[:1:]))
                    s = in3_
                    n = in4_
                    current = in5_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def SelectWordsSpec(s, n):
        return default__.SelectWordsAux(s, n, _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "")))

    @staticmethod
    def select__words(s, n):
        result: _dafny.Seq = _dafny.Seq({})
        out0_: _dafny.Seq
        out0_ = default__.SelectWordsAuxMethod(s, n, _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "")))
        result = out0_
        return result

    @staticmethod
    def SelectWordsAuxMethod(s, n, current):
        result: _dafny.Seq = _dafny.Seq({})
        if (len(s)) == (0):
            if ((len(current)) > (0)) and ((default__.CountConsonantsSpec(current)) == (n)):
                result = _dafny.SeqWithoutIsStrInference([current])
            elif True:
                result = _dafny.SeqWithoutIsStrInference([])
        elif ((s)[0]) == (_dafny.CodePoint(' ')):
            d_0_kept_: _dafny.Seq = _dafny.Seq({})
            if ((len(current)) > (0)) and ((default__.CountConsonantsSpec(current)) == (n)):
                d_0_kept_ = _dafny.SeqWithoutIsStrInference([current])
            elif True:
                d_0_kept_ = _dafny.SeqWithoutIsStrInference([])
            d_1_rest_: _dafny.Seq
            out0_: _dafny.Seq
            out0_ = default__.SelectWordsAuxMethod(_dafny.SeqWithoutIsStrInference((s)[1::]), n, _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "")))
            d_1_rest_ = out0_
            result = (d_0_kept_) + (d_1_rest_)
        elif True:
            out1_: _dafny.Seq
            out1_ = default__.SelectWordsAuxMethod(_dafny.SeqWithoutIsStrInference((s)[1::]), n, (current) + (_dafny.SeqWithoutIsStrInference((s)[:1:])))
            result = out1_
        return result

