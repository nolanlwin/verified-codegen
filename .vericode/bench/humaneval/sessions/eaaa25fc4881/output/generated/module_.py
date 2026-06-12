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
    def IsOddDigit(d):
        return (((((d) == (1)) or ((d) == (3))) or ((d) == (5))) or ((d) == (7))) or ((d) == (9))

    @staticmethod
    def FirstDigit(n):
        while True:
            with _dafny.label():
                if (n) < (10):
                    return n
                elif True:
                    in0_ = _dafny.euclidian_division(n, 10)
                    n = in0_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def SpecialNumberSpec(n):
        return (((n) > (10)) and (default__.IsOddDigit(default__.FirstDigit(n)))) and (default__.IsOddDigit(_dafny.euclidian_modulus(n, 10)))

    @staticmethod
    def SpecialfilterSpec(nums):
        d_0___accumulator_ = 0
        while True:
            with _dafny.label():
                if (len(nums)) == (0):
                    return (0) + (d_0___accumulator_)
                elif default__.SpecialNumberSpec((nums)[0]):
                    d_0___accumulator_ = (d_0___accumulator_) + (1)
                    in0_ = _dafny.SeqWithoutIsStrInference((nums)[1::])
                    nums = in0_
                    raise _dafny.TailCall()
                elif True:
                    in1_ = _dafny.SeqWithoutIsStrInference((nums)[1::])
                    nums = in1_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def specialFilter(nums):
        result: int = int(0)
        if (len(nums)) == (0):
            result = 0
        elif True:
            d_0_tailResult_: int
            out0_: int
            out0_ = default__.specialFilter(_dafny.SeqWithoutIsStrInference((nums)[1::]))
            d_0_tailResult_ = out0_
            if default__.SpecialNumberSpec((nums)[0]):
                result = (1) + (d_0_tailResult_)
            elif True:
                result = d_0_tailResult_
        return result

