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
    def DigitName(d):
        if (d) == (1):
            return _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "One"))
        elif (d) == (2):
            return _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "Two"))
        elif (d) == (3):
            return _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "Three"))
        elif (d) == (4):
            return _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "Four"))
        elif (d) == (5):
            return _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "Five"))
        elif (d) == (6):
            return _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "Six"))
        elif (d) == (7):
            return _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "Seven"))
        elif (d) == (8):
            return _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "Eight"))
        elif (d) == (9):
            return _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "Nine"))
        elif True:
            return _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, ""))

    @staticmethod
    def InsertDesc(d, s):
        d_0___accumulator_ = _dafny.SeqWithoutIsStrInference([])
        while True:
            with _dafny.label():
                if (len(s)) == (0):
                    return (d_0___accumulator_) + (_dafny.SeqWithoutIsStrInference([d]))
                elif (d) >= ((s)[0]):
                    return (d_0___accumulator_) + ((_dafny.SeqWithoutIsStrInference([d])) + (s))
                elif True:
                    d_0___accumulator_ = (d_0___accumulator_) + (_dafny.SeqWithoutIsStrInference([(s)[0]]))
                    in0_ = d
                    in1_ = _dafny.SeqWithoutIsStrInference((s)[1::])
                    d = in0_
                    s = in1_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def SortValidDesc(arr):
        if (len(arr)) == (0):
            return _dafny.SeqWithoutIsStrInference([])
        elif True:
            d_0_rest_ = default__.SortValidDesc(_dafny.SeqWithoutIsStrInference((arr)[1::]))
            if ((1) <= ((arr)[0])) and (((arr)[0]) <= (9)):
                return default__.InsertDesc((arr)[0], d_0_rest_)
            elif True:
                return d_0_rest_

    @staticmethod
    def MapDigitsToNames(digits):
        d_0___accumulator_ = _dafny.SeqWithoutIsStrInference([])
        while True:
            with _dafny.label():
                if (len(digits)) == (0):
                    return (d_0___accumulator_) + (_dafny.SeqWithoutIsStrInference([]))
                elif True:
                    d_0___accumulator_ = (d_0___accumulator_) + (_dafny.SeqWithoutIsStrInference([default__.DigitName((digits)[0])]))
                    in0_ = _dafny.SeqWithoutIsStrInference((digits)[1::])
                    digits = in0_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def ByLengthSpec(arr):
        return default__.MapDigitsToNames(default__.SortValidDesc(arr))

    @staticmethod
    def by__length(arr):
        result: _dafny.Seq = _dafny.Seq({})
        result = default__.ByLengthSpec(arr)
        return result

