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
    def DoubleTheDifferenceSpec(lst):
        d_0___accumulator_ = 0
        while True:
            with _dafny.label():
                if (len(lst)) == (0):
                    return (0) + (d_0___accumulator_)
                elif (((lst)[0]) >= (0)) and ((_dafny.euclidian_modulus((lst)[0], 2)) != (0)):
                    d_0___accumulator_ = (d_0___accumulator_) + (((lst)[0]) * ((lst)[0]))
                    in0_ = _dafny.SeqWithoutIsStrInference((lst)[1::])
                    lst = in0_
                    raise _dafny.TailCall()
                elif True:
                    in1_ = _dafny.SeqWithoutIsStrInference((lst)[1::])
                    lst = in1_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def double__the__difference(lst):
        result: int = int(0)
        if (len(lst)) == (0):
            result = 0
        elif True:
            d_0_tailResult_: int
            out0_: int
            out0_ = default__.double__the__difference(_dafny.SeqWithoutIsStrInference((lst)[1::]))
            d_0_tailResult_ = out0_
            if (((lst)[0]) >= (0)) and ((_dafny.euclidian_modulus((lst)[0], 2)) != (0)):
                result = (((lst)[0]) * ((lst)[0])) + (d_0_tailResult_)
            elif True:
                result = d_0_tailResult_
        return result

