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
    def AddSpec(lst):
        d_0___accumulator_ = 0
        while True:
            with _dafny.label():
                if (len(lst)) <= (1):
                    return (0) + (d_0___accumulator_)
                elif True:
                    d_0___accumulator_ = (d_0___accumulator_) + (((lst)[1] if (_dafny.euclidian_modulus((lst)[1], 2)) == (0) else 0))
                    if (len(lst)) <= (2):
                        return (0) + (d_0___accumulator_)
                    elif True:
                        in0_ = _dafny.SeqWithoutIsStrInference((lst)[2::])
                        lst = in0_
                        raise _dafny.TailCall()
                break

    @staticmethod
    def add(lst):
        result: int = int(0)
        if (len(lst)) <= (1):
            result = 0
        elif True:
            d_0_contribution_: int
            if (_dafny.euclidian_modulus((lst)[1], 2)) == (0):
                d_0_contribution_ = (lst)[1]
            elif True:
                d_0_contribution_ = 0
            if (len(lst)) <= (2):
                result = d_0_contribution_
            elif True:
                d_1_tailResult_: int
                out0_: int
                out0_ = default__.add(_dafny.SeqWithoutIsStrInference((lst)[2::]))
                d_1_tailResult_ = out0_
                result = (d_0_contribution_) + (d_1_tailResult_)
        return result

