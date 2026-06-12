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
    def MaxInt(a, b):
        if (a) >= (b):
            return a
        elif True:
            return b

    @staticmethod
    def RollingMaxSpec(numbers):
        if (len(numbers)) == (0):
            return _dafny.SeqWithoutIsStrInference([])
        elif True:
            d_0_rest_ = default__.RollingMaxSpec(_dafny.SeqWithoutIsStrInference((numbers)[:(len(numbers)) - (1):]))
            d_1_lastValue_ = (numbers)[(len(numbers)) - (1)]
            d_2_lastMax_ = (d_1_lastValue_ if (len(d_0_rest_)) == (0) else default__.MaxInt((d_0_rest_)[(len(d_0_rest_)) - (1)], d_1_lastValue_))
            return (d_0_rest_) + (_dafny.SeqWithoutIsStrInference([d_2_lastMax_]))

    @staticmethod
    def rolling__max(numbers):
        result: _dafny.Seq = _dafny.Seq({})
        if (len(numbers)) == (0):
            result = _dafny.SeqWithoutIsStrInference([])
        elif True:
            d_0_restResult_: _dafny.Seq
            out0_: _dafny.Seq
            out0_ = default__.rolling__max(_dafny.SeqWithoutIsStrInference((numbers)[:(len(numbers)) - (1):]))
            d_0_restResult_ = out0_
            d_1_lastValue_: int
            d_1_lastValue_ = (numbers)[(len(numbers)) - (1)]
            d_2_lastMax_: int
            if (len(d_0_restResult_)) == (0):
                d_2_lastMax_ = d_1_lastValue_
            elif True:
                d_2_lastMax_ = default__.MaxInt((d_0_restResult_)[(len(d_0_restResult_)) - (1)], d_1_lastValue_)
            result = (d_0_restResult_) + (_dafny.SeqWithoutIsStrInference([d_2_lastMax_]))
        return result

