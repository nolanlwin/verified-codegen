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
    def GreatestCommonDivisorSpec(a, b):
        while True:
            with _dafny.label():
                if (a) < (0):
                    in0_ = (0) - (a)
                    in1_ = b
                    a = in0_
                    b = in1_
                    raise _dafny.TailCall()
                elif (b) < (0):
                    in2_ = a
                    in3_ = (0) - (b)
                    a = in2_
                    b = in3_
                    raise _dafny.TailCall()
                elif (b) == (0):
                    return a
                elif True:
                    in4_ = b
                    in5_ = _dafny.euclidian_modulus(a, b)
                    a = in4_
                    b = in5_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def greatest__common__divisor(a, b):
        while True:
            with _dafny.label():
                result: int = int(0)
                if (a) < (0):
                    in0_ = (0) - (a)
                    in1_ = b
                    a = in0_
                    b = in1_
                    raise _dafny.TailCall()
                elif (b) < (0):
                    in2_ = a
                    in3_ = (0) - (b)
                    a = in2_
                    b = in3_
                    raise _dafny.TailCall()
                elif (b) == (0):
                    result = a
                elif True:
                    in4_ = b
                    in5_ = _dafny.euclidian_modulus(a, b)
                    a = in4_
                    b = in5_
                    raise _dafny.TailCall()
                return result
                break

