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
    def CanArrangeSpec(arr):
        while True:
            with _dafny.label():
                if (len(arr)) <= (1):
                    return -1
                elif ((arr)[(len(arr)) - (1)]) < ((arr)[(len(arr)) - (2)]):
                    return (len(arr)) - (1)
                elif True:
                    in0_ = _dafny.SeqWithoutIsStrInference((arr)[:(len(arr)) - (1):])
                    arr = in0_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def CanArrange(arr):
        while True:
            with _dafny.label():
                r: int = int(0)
                if (len(arr)) <= (1):
                    r = -1
                elif ((arr)[(len(arr)) - (1)]) < ((arr)[(len(arr)) - (2)]):
                    r = (len(arr)) - (1)
                elif True:
                    in0_ = _dafny.SeqWithoutIsStrInference((arr)[:(len(arr)) - (1):])
                    arr = in0_
                    raise _dafny.TailCall()
                return r
                break

