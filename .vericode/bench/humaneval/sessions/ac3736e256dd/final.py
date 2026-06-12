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
    def StrlenSpec(s):
        d_0___accumulator_ = 0
        while True:
            with _dafny.label():
                if (len(s)) == (0):
                    return (0) + (d_0___accumulator_)
                elif True:
                    d_0___accumulator_ = (d_0___accumulator_) + (1)
                    in0_ = _dafny.SeqWithoutIsStrInference((s)[1::])
                    s = in0_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def strlen(s):
        result: int = int(0)
        if (len(s)) == (0):
            result = 0
        elif True:
            d_0_tailResult_: int
            out0_: int
            out0_ = default__.strlen(_dafny.SeqWithoutIsStrInference((s)[1::]))
            d_0_tailResult_ = out0_
            result = (1) + (d_0_tailResult_)
        return result

