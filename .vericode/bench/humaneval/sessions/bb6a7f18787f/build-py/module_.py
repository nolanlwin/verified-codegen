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
    def InsertSorted(x, s):
        d_0___accumulator_ = _dafny.SeqWithoutIsStrInference([])
        while True:
            with _dafny.label():
                if (len(s)) == (0):
                    return (d_0___accumulator_) + (_dafny.SeqWithoutIsStrInference([x]))
                elif (x) <= ((s)[0]):
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
    def SortSeq(s):
        if (len(s)) == (0):
            return _dafny.SeqWithoutIsStrInference([])
        elif True:
            return default__.InsertSorted((s)[0], default__.SortSeq(_dafny.SeqWithoutIsStrInference((s)[1::])))

    @staticmethod
    def StrangePickEnds(sorted_, takeMin):
        d_0___accumulator_ = _dafny.SeqWithoutIsStrInference([])
        while True:
            with _dafny.label():
                if (len(sorted_)) == (0):
                    return (d_0___accumulator_) + (_dafny.SeqWithoutIsStrInference([]))
                elif takeMin:
                    d_0___accumulator_ = (d_0___accumulator_) + (_dafny.SeqWithoutIsStrInference([(sorted_)[0]]))
                    in0_ = _dafny.SeqWithoutIsStrInference((sorted_)[1::])
                    in1_ = False
                    sorted_ = in0_
                    takeMin = in1_
                    raise _dafny.TailCall()
                elif True:
                    d_0___accumulator_ = (d_0___accumulator_) + (_dafny.SeqWithoutIsStrInference([(sorted_)[(len(sorted_)) - (1)]]))
                    in2_ = _dafny.SeqWithoutIsStrInference((sorted_)[:(len(sorted_)) - (1):])
                    in3_ = True
                    sorted_ = in2_
                    takeMin = in3_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def StrangeSortListSpec(lst):
        return default__.StrangePickEnds(default__.SortSeq(lst), True)

    @staticmethod
    def strange__sort__list(lst):
        result: _dafny.Seq = _dafny.Seq({})
        result = default__.StrangeSortListSpec(lst)
        return result

