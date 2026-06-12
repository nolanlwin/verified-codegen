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
    def LetterGradeSpec(g):
        if (g) == (_dafny.BigRational('4e0')):
            return _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "A+"))
        elif (g) > (_dafny.BigRational('37e-1')):
            return _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "A"))
        elif (g) > (_dafny.BigRational('33e-1')):
            return _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "A-"))
        elif (g) > (_dafny.BigRational('3e0')):
            return _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "B+"))
        elif (g) > (_dafny.BigRational('27e-1')):
            return _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "B"))
        elif (g) > (_dafny.BigRational('23e-1')):
            return _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "B-"))
        elif (g) > (_dafny.BigRational('2e0')):
            return _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "C+"))
        elif (g) > (_dafny.BigRational('17e-1')):
            return _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "C"))
        elif (g) > (_dafny.BigRational('13e-1')):
            return _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "C-"))
        elif (g) > (_dafny.BigRational('1e0')):
            return _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "D+"))
        elif (g) > (_dafny.BigRational('7e-1')):
            return _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "D"))
        elif (g) > (_dafny.BigRational('0e0')):
            return _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "D-"))
        elif True:
            return _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "E"))

    @staticmethod
    def NumericalLetterGradeSpec(grades):
        d_0___accumulator_ = _dafny.SeqWithoutIsStrInference([])
        while True:
            with _dafny.label():
                if (len(grades)) == (0):
                    return (d_0___accumulator_) + (_dafny.SeqWithoutIsStrInference([]))
                elif True:
                    d_0___accumulator_ = (d_0___accumulator_) + (_dafny.SeqWithoutIsStrInference([default__.LetterGradeSpec((grades)[0])]))
                    in0_ = _dafny.SeqWithoutIsStrInference((grades)[1::])
                    grades = in0_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def numerical__letter__grade(grades):
        result: _dafny.Seq = _dafny.Seq({})
        if (len(grades)) == (0):
            result = _dafny.SeqWithoutIsStrInference([])
        elif True:
            d_0_rest_: _dafny.Seq
            out0_: _dafny.Seq
            out0_ = default__.numerical__letter__grade(_dafny.SeqWithoutIsStrInference((grades)[1::]))
            d_0_rest_ = out0_
            result = (_dafny.SeqWithoutIsStrInference([default__.LetterGradeSpec((grades)[0])])) + (d_0_rest_)
        return result

