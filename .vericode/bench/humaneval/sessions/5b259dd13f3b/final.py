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
    def InsertUniqueSorted(x, s):
        d_0___accumulator_ = _dafny.SeqWithoutIsStrInference([])
        while True:
            with _dafny.label():
                if (len(s)) == (0):
                    return (d_0___accumulator_) + (_dafny.SeqWithoutIsStrInference([x]))
                elif (x) < ((s)[0]):
                    return (d_0___accumulator_) + ((_dafny.SeqWithoutIsStrInference([x])) + (s))
                elif (x) == ((s)[0]):
                    return (d_0___accumulator_) + (s)
                elif True:
                    d_0___accumulator_ = (d_0___accumulator_) + (_dafny.SeqWithoutIsStrInference([(s)[0]]))
                    in0_ = x
                    in1_ = _dafny.SeqWithoutIsStrInference((s)[1::])
                    x = in0_
                    s = in1_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def UniqueSpec(l):
        if (len(l)) == (0):
            return _dafny.SeqWithoutIsStrInference([])
        elif True:
            return default__.InsertUniqueSorted((l)[0], default__.UniqueSpec(_dafny.SeqWithoutIsStrInference((l)[1::])))

    @staticmethod
    def unique(l):
        result: _dafny.Seq = _dafny.Seq({})
        if (len(l)) == (0):
            result = _dafny.SeqWithoutIsStrInference([])
        elif True:
            d_0_tailResult_: _dafny.Seq
            out0_: _dafny.Seq
            out0_ = default__.unique(_dafny.SeqWithoutIsStrInference((l)[1::]))
            d_0_tailResult_ = out0_
            result = default__.InsertUniqueSorted((l)[0], d_0_tailResult_)
        return result

