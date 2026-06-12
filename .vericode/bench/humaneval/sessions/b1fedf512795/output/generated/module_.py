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
    def DigitSumSpec(n):
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
    def BinaryStringSpec(n):
        d_0___accumulator_ = _dafny.SeqWithoutIsStrInference([])
        while True:
            with _dafny.label():
                if (n) < (2):
                    if (n) == (0):
                        return (_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "0"))) + (d_0___accumulator_)
                    elif True:
                        return (_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "1"))) + (d_0___accumulator_)
                elif True:
                    d_0___accumulator_ = ((_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "0")) if (_dafny.euclidian_modulus(n, 2)) == (0) else _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "1")))) + (d_0___accumulator_)
                    in0_ = _dafny.euclidian_division(n, 2)
                    n = in0_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def SolveSpec(N):
        return default__.BinaryStringSpec(default__.DigitSumSpec(N))

    @staticmethod
    def solve(N):
        result: _dafny.Seq = _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, ""))
        d_0_s_: int
        out0_: int
        out0_ = default__.DigitSum(N)
        d_0_s_ = out0_
        out1_: _dafny.Seq
        out1_ = default__.BinaryString(d_0_s_)
        result = out1_
        return result

    @staticmethod
    def DigitSum(n):
        s: int = int(0)
        if (n) < (10):
            s = n
        elif True:
            d_0_t_: int
            out0_: int
            out0_ = default__.DigitSum(_dafny.euclidian_division(n, 10))
            d_0_t_ = out0_
            s = (_dafny.euclidian_modulus(n, 10)) + (d_0_t_)
        return s

    @staticmethod
    def BinaryString(n):
        r: _dafny.Seq = _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, ""))
        if (n) < (2):
            if (n) == (0):
                r = _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "0"))
            elif True:
                r = _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "1"))
        elif True:
            d_0_prefix_: _dafny.Seq
            out0_: _dafny.Seq
            out0_ = default__.BinaryString(_dafny.euclidian_division(n, 2))
            d_0_prefix_ = out0_
            if (_dafny.euclidian_modulus(n, 2)) == (0):
                r = (d_0_prefix_) + (_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "0")))
            elif True:
                r = (d_0_prefix_) + (_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "1")))
        return r

