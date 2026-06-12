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
    def MultiplySpec(a, b):
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
                elif (10) <= (a):
                    in4_ = (a) - (10)
                    in5_ = b
                    a = in4_
                    b = in5_
                    raise _dafny.TailCall()
                elif (10) <= (b):
                    in6_ = a
                    in7_ = (b) - (10)
                    a = in6_
                    b = in7_
                    raise _dafny.TailCall()
                elif True:
                    return (a) * (b)
                break

    @staticmethod
    def multiply(a, b):
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
                elif (10) <= (a):
                    in4_ = (a) - (10)
                    in5_ = b
                    a = in4_
                    b = in5_
                    raise _dafny.TailCall()
                elif (10) <= (b):
                    in6_ = a
                    in7_ = (b) - (10)
                    a = in6_
                    b = in7_
                    raise _dafny.TailCall()
                elif True:
                    result = (a) * (b)
                return result
                break

