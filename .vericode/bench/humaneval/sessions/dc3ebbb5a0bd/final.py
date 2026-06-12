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
    def ChooseNumSpec(x, y):
        while True:
            with _dafny.label():
                if (x) > (y):
                    return -1
                elif (_dafny.euclidian_modulus(y, 2)) == (0):
                    return y
                elif True:
                    in0_ = x
                    in1_ = (y) - (1)
                    x = in0_
                    y = in1_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def choose__num(x, y):
        while True:
            with _dafny.label():
                result: int = int(0)
                if (x) > (y):
                    result = -1
                elif (_dafny.euclidian_modulus(y, 2)) == (0):
                    result = y
                elif True:
                    in0_ = x
                    in1_ = (y) - (1)
                    x = in0_
                    y = in1_
                    raise _dafny.TailCall()
                return result
                break

