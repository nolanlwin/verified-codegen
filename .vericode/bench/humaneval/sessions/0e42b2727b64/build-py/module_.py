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
    def DecodeCyclicSpec(s):
        d_0___accumulator_ = _dafny.SeqWithoutIsStrInference([])
        while True:
            with _dafny.label():
                if (len(s)) < (3):
                    return (d_0___accumulator_) + (s)
                elif True:
                    d_0___accumulator_ = (d_0___accumulator_) + (((_dafny.SeqWithoutIsStrInference((s)[2:3:])) + (_dafny.SeqWithoutIsStrInference((s)[0:1:]))) + (_dafny.SeqWithoutIsStrInference((s)[1:2:])))
                    in0_ = _dafny.SeqWithoutIsStrInference((s)[3::])
                    s = in0_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def decode__cyclic(s):
        result: _dafny.Seq = _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, ""))
        if (len(s)) < (3):
            result = s
        elif True:
            d_0_rest_: _dafny.Seq
            out0_: _dafny.Seq
            out0_ = default__.decode__cyclic(_dafny.SeqWithoutIsStrInference((s)[3::]))
            d_0_rest_ = out0_
            result = (((_dafny.SeqWithoutIsStrInference((s)[2:3:])) + (_dafny.SeqWithoutIsStrInference((s)[0:1:]))) + (_dafny.SeqWithoutIsStrInference((s)[1:2:]))) + (d_0_rest_)
        return result

