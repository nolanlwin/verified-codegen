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
    def NatDigitSum(n):
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
    def NegativeDigitSum(m):
        d_0___accumulator_ = 0
        while True:
            with _dafny.label():
                if (m) < (10):
                    return ((0) - (m)) + (d_0___accumulator_)
                elif True:
                    d_0___accumulator_ = (d_0___accumulator_) + (_dafny.euclidian_modulus(m, 10))
                    in0_ = _dafny.euclidian_division(m, 10)
                    m = in0_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def PointValue(n):
        if (n) >= (0):
            return default__.NatDigitSum(n)
        elif True:
            return default__.NegativeDigitSum((0) - (n))

    @staticmethod
    def InsertByPoint(x, s):
        d_0___accumulator_ = _dafny.SeqWithoutIsStrInference([])
        while True:
            with _dafny.label():
                if (len(s)) == (0):
                    return (d_0___accumulator_) + (_dafny.SeqWithoutIsStrInference([x]))
                elif (default__.PointValue(x)) <= (default__.PointValue((s)[0])):
                    return (d_0___accumulator_) + ((_dafny.SeqWithoutIsStrInference([x])) + (s))
                elif True:
                    d_0___accumulator_ = (d_0___accumulator_) + (_dafny.SeqWithoutIsStrInference([(s)[0]]))
                    in0_ = x
                    in1_ = _dafny.SeqWithoutIsStrInference((s)[1::])
                    x = in0_
                    s = in1_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def OrderByPointsSpec(nums):
        if (len(nums)) <= (1):
            return nums
        elif True:
            return default__.InsertByPoint((nums)[0], default__.OrderByPointsSpec(_dafny.SeqWithoutIsStrInference((nums)[1::])))

    @staticmethod
    def order__by__points(nums):
        result: _dafny.Seq = _dafny.Seq({})
        if (len(nums)) <= (1):
            result = nums
        elif True:
            d_0_tail_: _dafny.Seq
            out0_: _dafny.Seq
            out0_ = default__.order__by__points(_dafny.SeqWithoutIsStrInference((nums)[1::]))
            d_0_tail_ = out0_
            out1_: _dafny.Seq
            out1_ = default__.InsertByPointMethod((nums)[0], d_0_tail_)
            result = out1_
        return result

    @staticmethod
    def InsertByPointMethod(x, s):
        r: _dafny.Seq = _dafny.Seq({})
        if (len(s)) == (0):
            r = _dafny.SeqWithoutIsStrInference([x])
        elif (default__.PointValue(x)) <= (default__.PointValue((s)[0])):
            r = (_dafny.SeqWithoutIsStrInference([x])) + (s)
        elif True:
            d_0_tail_: _dafny.Seq
            out0_: _dafny.Seq
            out0_ = default__.InsertByPointMethod(x, _dafny.SeqWithoutIsStrInference((s)[1::]))
            d_0_tail_ = out0_
            r = (_dafny.SeqWithoutIsStrInference([(s)[0]])) + (d_0_tail_)
        return r

