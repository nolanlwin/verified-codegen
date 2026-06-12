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
    def IntersperseSpec(numbers, delimeter):
        d_0___accumulator_ = _dafny.SeqWithoutIsStrInference([])
        while True:
            with _dafny.label():
                if (len(numbers)) <= (1):
                    return (d_0___accumulator_) + (numbers)
                elif True:
                    d_0___accumulator_ = (d_0___accumulator_) + (_dafny.SeqWithoutIsStrInference([(numbers)[0], delimeter]))
                    in0_ = _dafny.SeqWithoutIsStrInference((numbers)[1::])
                    in1_ = delimeter
                    numbers = in0_
                    delimeter = in1_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def intersperse(numbers, delimeter):
        result: _dafny.Seq = _dafny.Seq({})
        if (len(numbers)) <= (1):
            result = numbers
        elif True:
            d_0_rest_: _dafny.Seq
            out0_: _dafny.Seq
            out0_ = default__.intersperse(_dafny.SeqWithoutIsStrInference((numbers)[1::]), delimeter)
            d_0_rest_ = out0_
            result = (_dafny.SeqWithoutIsStrInference([(numbers)[0], delimeter])) + (d_0_rest_)
        return result

