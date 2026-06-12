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
    def BelowThresholdSpec(l, t):
        if (len(l)) == (0):
            return True
        elif True:
            return (((l)[0]) < (t)) and (default__.BelowThresholdSpec(_dafny.SeqWithoutIsStrInference((l)[1::]), t))

    @staticmethod
    def below__threshold(l, t):
        result: bool = False
        if (len(l)) == (0):
            result = True
        elif True:
            d_0_tailResult_: bool
            out0_: bool
            out0_ = default__.below__threshold(_dafny.SeqWithoutIsStrInference((l)[1::]), t)
            d_0_tailResult_ = out0_
            result = (((l)[0]) < (t)) and (d_0_tailResult_)
        return result

