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
    def GetPositiveSpec(l):
        d_0___accumulator_ = _dafny.SeqWithoutIsStrInference([])
        while True:
            with _dafny.label():
                if (len(l)) == (0):
                    return (d_0___accumulator_) + (_dafny.SeqWithoutIsStrInference([]))
                elif ((l)[0]) > (0):
                    d_0___accumulator_ = (d_0___accumulator_) + (_dafny.SeqWithoutIsStrInference([(l)[0]]))
                    in0_ = _dafny.SeqWithoutIsStrInference((l)[1::])
                    l = in0_
                    raise _dafny.TailCall()
                elif True:
                    in1_ = _dafny.SeqWithoutIsStrInference((l)[1::])
                    l = in1_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def get__positive(l):
        result: _dafny.Seq = _dafny.Seq({})
        if (len(l)) == (0):
            result = _dafny.SeqWithoutIsStrInference([])
        elif ((l)[0]) > (0):
            d_0_tail_: _dafny.Seq
            out0_: _dafny.Seq
            out0_ = default__.get__positive(_dafny.SeqWithoutIsStrInference((l)[1::]))
            d_0_tail_ = out0_
            result = (_dafny.SeqWithoutIsStrInference([(l)[0]])) + (d_0_tail_)
        elif True:
            out1_: _dafny.Seq
            out1_ = default__.get__positive(_dafny.SeqWithoutIsStrInference((l)[1::]))
            result = out1_
        return result

