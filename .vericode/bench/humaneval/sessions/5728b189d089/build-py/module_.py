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
    def DigitSumNonNegative(n):
        d_0___accumulator_ = 0
        while True:
            with _dafny.label():
                if (n) < (10):
                    return (n) + (d_0___accumulator_)
                elif True:
                    d_0___accumulator_ = (d_0___accumulator_) + (_dafny.euclidian_modulus(n, 10))
                    in0_ = _dafny.euclidian_division(n, 10)
                    n = in0_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def LeadingDigitNonNegative(n):
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
    def SignedDigitSumSpec(n):
        if (n) >= (0):
            return default__.DigitSumNonNegative(n)
        elif True:
            return (default__.DigitSumNonNegative((0) - (n))) - ((2) * (default__.LeadingDigitNonNegative((0) - (n))))

    @staticmethod
    def CountNumsSpec(arr):
        d_0___accumulator_ = 0
        while True:
            with _dafny.label():
                if (len(arr)) == (0):
                    return (0) + (d_0___accumulator_)
                elif True:
                    d_0___accumulator_ = (d_0___accumulator_) + ((1 if (default__.SignedDigitSumSpec((arr)[0])) > (0) else 0))
                    in0_ = _dafny.SeqWithoutIsStrInference((arr)[1::])
                    arr = in0_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def count__nums(arr):
        result: int = int(0)
        if (len(arr)) == (0):
            result = 0
        elif True:
            d_0_tailResult_: int
            out0_: int
            out0_ = default__.count__nums(_dafny.SeqWithoutIsStrInference((arr)[1::]))
            d_0_tailResult_ = out0_
            if (default__.SignedDigitSumSpec((arr)[0])) > (0):
                result = (1) + (d_0_tailResult_)
            elif True:
                result = d_0_tailResult_
        return result

