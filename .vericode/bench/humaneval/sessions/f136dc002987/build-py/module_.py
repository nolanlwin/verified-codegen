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
    def IncrListSpec(l):
        d_0___accumulator_ = _dafny.SeqWithoutIsStrInference([])
        while True:
            with _dafny.label():
                if (len(l)) == (0):
                    return (d_0___accumulator_) + (_dafny.SeqWithoutIsStrInference([]))
                elif True:
                    d_0___accumulator_ = (d_0___accumulator_) + (_dafny.SeqWithoutIsStrInference([((l)[0]) + (1)]))
                    in0_ = _dafny.SeqWithoutIsStrInference((l)[1::])
                    l = in0_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def incr__list(l):
        result: _dafny.Seq = _dafny.Seq({})
        if (len(l)) == (0):
            result = _dafny.SeqWithoutIsStrInference([])
        elif True:
            d_0_tail_: _dafny.Seq
            out0_: _dafny.Seq
            out0_ = default__.incr__list(_dafny.SeqWithoutIsStrInference((l)[1::]))
            d_0_tail_ = out0_
            result = (_dafny.SeqWithoutIsStrInference([((l)[0]) + (1)])) + (d_0_tail_)
        return result

