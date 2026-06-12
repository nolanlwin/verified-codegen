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
    def IscubeSearch(n, i):
        while True:
            with _dafny.label():
                if (i) > (n):
                    return False
                elif (((i) * (i)) * (i)) == (n):
                    return True
                elif True:
                    in0_ = n
                    in1_ = (i) + (1)
                    n = in0_
                    i = in1_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def IscubeSpec(a):
        if (a) < (0):
            return default__.IscubeSearch((0) - (a), 0)
        elif True:
            return default__.IscubeSearch(a, 0)

    @staticmethod
    def iscube(a):
        result: bool = False
        if (a) < (0):
            out0_: bool
            out0_ = default__.IscubeSearchMethod((0) - (a), 0)
            result = out0_
        elif True:
            out1_: bool
            out1_ = default__.IscubeSearchMethod(a, 0)
            result = out1_
        return result

    @staticmethod
    def IscubeSearchMethod(n, i):
        while True:
            with _dafny.label():
                result: bool = False
                if (i) > (n):
                    result = False
                elif (((i) * (i)) * (i)) == (n):
                    result = True
                elif True:
                    in0_ = n
                    in1_ = (i) + (1)
                    n = in0_
                    i = in1_
                    raise _dafny.TailCall()
                return result
                break

