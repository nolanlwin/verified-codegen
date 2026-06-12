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
    def Count(numbers, x):
        d_0___accumulator_ = 0
        while True:
            with _dafny.label():
                if (len(numbers)) == (0):
                    return (0) + (d_0___accumulator_)
                elif True:
                    d_0___accumulator_ = (d_0___accumulator_) + ((1 if ((numbers)[0]) == (x) else 0))
                    in0_ = _dafny.SeqWithoutIsStrInference((numbers)[1::])
                    in1_ = x
                    numbers = in0_
                    x = in1_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def RemoveDuplicatesSpec(numbers):
        d_0___accumulator_ = _dafny.SeqWithoutIsStrInference([])
        while True:
            with _dafny.label():
                if (len(numbers)) == (0):
                    return (d_0___accumulator_) + (_dafny.SeqWithoutIsStrInference([]))
                elif (default__.Count(numbers, (numbers)[0])) == (1):
                    d_0___accumulator_ = (d_0___accumulator_) + (_dafny.SeqWithoutIsStrInference([(numbers)[0]]))
                    in0_ = _dafny.SeqWithoutIsStrInference((numbers)[1::])
                    numbers = in0_
                    raise _dafny.TailCall()
                elif True:
                    in1_ = _dafny.SeqWithoutIsStrInference((numbers)[1::])
                    numbers = in1_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def remove__duplicates(numbers):
        result: _dafny.Seq = _dafny.Seq({})
        if (len(numbers)) == (0):
            result = _dafny.SeqWithoutIsStrInference([])
        elif True:
            d_0_tailResult_: _dafny.Seq
            out0_: _dafny.Seq
            out0_ = default__.remove__duplicates(_dafny.SeqWithoutIsStrInference((numbers)[1::]))
            d_0_tailResult_ = out0_
            if (default__.Count(numbers, (numbers)[0])) == (1):
                result = (_dafny.SeqWithoutIsStrInference([(numbers)[0]])) + (d_0_tailResult_)
            elif True:
                result = d_0_tailResult_
        return result

