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
    def NoEvenDigit(n):
        if (n) < (10):
            return (_dafny.euclidian_modulus(n, 2)) == (1)
        elif True:
            return ((_dafny.euclidian_modulus(n, 2)) == (1)) and (default__.NoEvenDigit(_dafny.euclidian_division(n, 10)))

    @staticmethod
    def InsertIncreasing(v, s):
        d_0___accumulator_ = _dafny.SeqWithoutIsStrInference([])
        while True:
            with _dafny.label():
                if ((len(s)) == (0)) or ((v) <= ((s)[0])):
                    return (d_0___accumulator_) + ((_dafny.SeqWithoutIsStrInference([v])) + (s))
                elif True:
                    d_0___accumulator_ = (d_0___accumulator_) + (_dafny.SeqWithoutIsStrInference([(s)[0]]))
                    in0_ = v
                    in1_ = _dafny.SeqWithoutIsStrInference((s)[1::])
                    v = in0_
                    s = in1_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def UniqueDigitsSpec(x):
        if (len(x)) == (0):
            return _dafny.SeqWithoutIsStrInference([])
        elif True:
            d_0_tail_ = default__.UniqueDigitsSpec(_dafny.SeqWithoutIsStrInference((x)[1::]))
            if default__.NoEvenDigit((x)[0]):
                return default__.InsertIncreasing((x)[0], d_0_tail_)
            elif True:
                return d_0_tail_

    @staticmethod
    def unique__digits(x):
        result: _dafny.Seq = _dafny.Seq({})
        if (len(x)) == (0):
            result = _dafny.SeqWithoutIsStrInference([])
        elif True:
            d_0_tail_: _dafny.Seq
            out0_: _dafny.Seq
            out0_ = default__.unique__digits(_dafny.SeqWithoutIsStrInference((x)[1::]))
            d_0_tail_ = out0_
            if default__.NoEvenDigit((x)[0]):
                result = default__.InsertIncreasing((x)[0], d_0_tail_)
            elif True:
                result = d_0_tail_
        return result

