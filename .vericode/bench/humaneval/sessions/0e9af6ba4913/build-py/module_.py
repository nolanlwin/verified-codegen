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
    def SmallestChangeSpec(arr):
        d_0___accumulator_ = 0
        while True:
            with _dafny.label():
                if (len(arr)) <= (1):
                    return (0) + (d_0___accumulator_)
                elif True:
                    d_0___accumulator_ = (d_0___accumulator_) + ((0 if ((arr)[0]) == ((arr)[(len(arr)) - (1)]) else 1))
                    in0_ = _dafny.SeqWithoutIsStrInference((arr)[1:(len(arr)) - (1):])
                    arr = in0_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def smallest__change(arr):
        result: int = int(0)
        if (len(arr)) <= (1):
            result = 0
        elif True:
            d_0_inner_: int
            out0_: int
            out0_ = default__.smallest__change(_dafny.SeqWithoutIsStrInference((arr)[1:(len(arr)) - (1):]))
            d_0_inner_ = out0_
            if ((arr)[0]) == ((arr)[(len(arr)) - (1)]):
                result = d_0_inner_
            elif True:
                result = (d_0_inner_) + (1)
        return result

