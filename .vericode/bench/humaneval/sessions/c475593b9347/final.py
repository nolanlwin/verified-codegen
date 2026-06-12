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
    def AddElementsSpec(arr, k):
        d_0___accumulator_ = 0
        while True:
            with _dafny.label():
                if (k) <= (0):
                    return (0) + (d_0___accumulator_)
                elif (k) > (len(arr)):
                    in0_ = arr
                    in1_ = len(arr)
                    arr = in0_
                    k = in1_
                    raise _dafny.TailCall()
                elif ((-99) <= ((arr)[(k) - (1)])) and (((arr)[(k) - (1)]) <= (99)):
                    d_0___accumulator_ = ((arr)[(k) - (1)]) + (d_0___accumulator_)
                    in2_ = arr
                    in3_ = (k) - (1)
                    arr = in2_
                    k = in3_
                    raise _dafny.TailCall()
                elif True:
                    in4_ = arr
                    in5_ = (k) - (1)
                    arr = in4_
                    k = in5_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def AddElementsHelper(arr, k):
        sum_: int = int(0)
        if (k) == (0):
            sum_ = 0
        elif True:
            d_0_previous_: int
            out0_: int
            out0_ = default__.AddElementsHelper(arr, (k) - (1))
            d_0_previous_ = out0_
            if ((-99) <= ((arr)[(k) - (1)])) and (((arr)[(k) - (1)]) <= (99)):
                sum_ = (d_0_previous_) + ((arr)[(k) - (1)])
            elif True:
                sum_ = d_0_previous_
        return sum_

    @staticmethod
    def AddElements(arr, k):
        sum_: int = int(0)
        out0_: int
        out0_ = default__.AddElementsHelper(arr, k)
        sum_ = out0_
        return sum_

