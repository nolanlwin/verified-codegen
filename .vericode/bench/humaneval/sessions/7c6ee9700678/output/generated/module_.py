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
    def FactorialSpec(i):
        d_0___accumulator_ = 1
        while True:
            with _dafny.label():
                if (i) <= (1):
                    return (1) * (d_0___accumulator_)
                elif True:
                    d_0___accumulator_ = (d_0___accumulator_) * (i)
                    in0_ = (i) - (1)
                    i = in0_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def SumToSpec(i):
        d_0___accumulator_ = 0
        while True:
            with _dafny.label():
                if (i) == (0):
                    return (0) + (d_0___accumulator_)
                elif True:
                    d_0___accumulator_ = (d_0___accumulator_) + (i)
                    in0_ = (i) - (1)
                    i = in0_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def ElementSpec(i):
        if (_dafny.euclidian_modulus(i, 2)) == (0):
            return default__.FactorialSpec(i)
        elif True:
            return default__.SumToSpec(i)

    @staticmethod
    def FSpec(n):
        d_0___accumulator_ = _dafny.SeqWithoutIsStrInference([])
        while True:
            with _dafny.label():
                if (n) == (0):
                    return (_dafny.SeqWithoutIsStrInference([])) + (d_0___accumulator_)
                elif True:
                    d_0___accumulator_ = (_dafny.SeqWithoutIsStrInference([default__.ElementSpec(n)])) + (d_0___accumulator_)
                    in0_ = (n) - (1)
                    n = in0_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def f(n):
        result: _dafny.Seq = _dafny.Seq({})
        if (n) == (0):
            result = _dafny.SeqWithoutIsStrInference([])
        elif True:
            d_0_prev_: _dafny.Seq
            out0_: _dafny.Seq
            out0_ = default__.f((n) - (1))
            d_0_prev_ = out0_
            result = (d_0_prev_) + (_dafny.SeqWithoutIsStrInference([default__.ElementSpec(n)]))
        return result

