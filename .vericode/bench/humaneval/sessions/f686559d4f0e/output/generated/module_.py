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
    def DigitString(d):
        if (d) == (0):
            return _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "0"))
        elif (d) == (1):
            return _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "1"))
        elif (d) == (2):
            return _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "2"))
        elif (d) == (3):
            return _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "3"))
        elif (d) == (4):
            return _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "4"))
        elif (d) == (5):
            return _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "5"))
        elif (d) == (6):
            return _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "6"))
        elif (d) == (7):
            return _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "7"))
        elif (d) == (8):
            return _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "8"))
        elif True:
            return _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "9"))

    @staticmethod
    def IntToStringSpec(n):
        d_0___accumulator_ = _dafny.SeqWithoutIsStrInference([])
        while True:
            with _dafny.label():
                if (n) < (10):
                    return (default__.DigitString(n)) + (d_0___accumulator_)
                elif True:
                    d_0___accumulator_ = (default__.DigitString(_dafny.euclidian_modulus(n, 10))) + (d_0___accumulator_)
                    in0_ = _dafny.euclidian_division(n, 10)
                    n = in0_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def ReverseStringSpec(s):
        d_0___accumulator_ = _dafny.SeqWithoutIsStrInference([])
        while True:
            with _dafny.label():
                if (len(s)) == (0):
                    return (_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, ""))) + (d_0___accumulator_)
                elif True:
                    d_0___accumulator_ = (_dafny.SeqWithoutIsStrInference([(s)[0]])) + (d_0___accumulator_)
                    in0_ = _dafny.SeqWithoutIsStrInference((s)[1::])
                    s = in0_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def CircularShiftSpec(digits, shift):
        if (shift) < (0):
            return _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, ""))
        elif (shift) > (len(digits)):
            return default__.ReverseStringSpec(digits)
        elif True:
            return (_dafny.SeqWithoutIsStrInference((digits)[(len(digits)) - (shift)::])) + (_dafny.SeqWithoutIsStrInference((digits)[:(len(digits)) - (shift):]))

    @staticmethod
    def circular__shift(x, shift):
        result: _dafny.Seq = _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, ""))
        result = default__.CircularShiftSpec(default__.IntToStringSpec(x), shift)
        return result

