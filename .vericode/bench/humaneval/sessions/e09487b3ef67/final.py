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
    def ConcatenateSpec(strings):
        d_0___accumulator_ = _dafny.SeqWithoutIsStrInference([])
        while True:
            with _dafny.label():
                if (len(strings)) == (0):
                    return (d_0___accumulator_) + (_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "")))
                elif True:
                    d_0___accumulator_ = (d_0___accumulator_) + ((strings)[0])
                    in0_ = _dafny.SeqWithoutIsStrInference((strings)[1::])
                    strings = in0_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def concatenate(strings):
        result: _dafny.Seq = _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, ""))
        if (len(strings)) == (0):
            result = _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, ""))
        elif True:
            d_0_rest_: _dafny.Seq
            out0_: _dafny.Seq
            out0_ = default__.concatenate(_dafny.SeqWithoutIsStrInference((strings)[1::]))
            d_0_rest_ = out0_
            result = ((strings)[0]) + (d_0_rest_)
        return result

