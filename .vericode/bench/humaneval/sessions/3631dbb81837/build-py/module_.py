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
    def AddSpec(x, y):
        while True:
            with _dafny.label():
                if (y) == (0):
                    return x
                elif (y) > (0):
                    in0_ = (x) + (1)
                    in1_ = (y) - (1)
                    x = in0_
                    y = in1_
                    raise _dafny.TailCall()
                elif True:
                    in2_ = (x) - (1)
                    in3_ = (y) + (1)
                    x = in2_
                    y = in3_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def add(x, y):
        while True:
            with _dafny.label():
                result: int = int(0)
                if (y) == (0):
                    result = x
                elif (y) > (0):
                    in0_ = (x) + (1)
                    in1_ = (y) - (1)
                    x = in0_
                    y = in1_
                    raise _dafny.TailCall()
                elif True:
                    in2_ = (x) - (1)
                    in3_ = (y) + (1)
                    x = in2_
                    y = in3_
                    raise _dafny.TailCall()
                return result
                break

