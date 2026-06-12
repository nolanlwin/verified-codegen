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
    def AllPrefixesSpec(s):
        d_0___accumulator_ = _dafny.SeqWithoutIsStrInference([])
        while True:
            with _dafny.label():
                if (len(s)) == (0):
                    return (_dafny.SeqWithoutIsStrInference([])) + (d_0___accumulator_)
                elif True:
                    d_0___accumulator_ = (_dafny.SeqWithoutIsStrInference([s])) + (d_0___accumulator_)
                    in0_ = _dafny.SeqWithoutIsStrInference((s)[:(len(s)) - (1):])
                    s = in0_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def AllPrefixes(s):
        r: _dafny.Seq = _dafny.Seq({})
        if (len(s)) == (0):
            r = _dafny.SeqWithoutIsStrInference([])
        elif True:
            d_0_prev_: _dafny.Seq
            out0_: _dafny.Seq
            out0_ = default__.AllPrefixes(_dafny.SeqWithoutIsStrInference((s)[:(len(s)) - (1):]))
            d_0_prev_ = out0_
            r = (d_0_prev_) + (_dafny.SeqWithoutIsStrInference([s]))
        return r

