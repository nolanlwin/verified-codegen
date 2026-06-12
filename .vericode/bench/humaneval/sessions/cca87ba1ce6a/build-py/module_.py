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
    def IsEqualToSumEvenSpec(n):
        while True:
            with _dafny.label():
                if (n) < (8):
                    return False
                elif (n) == (8):
                    return True
                elif True:
                    in0_ = (n) - (2)
                    n = in0_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def is__equal__to__sum__even(n):
        while True:
            with _dafny.label():
                result: bool = False
                if (n) < (8):
                    result = False
                elif (n) == (8):
                    result = True
                elif True:
                    in0_ = (n) - (2)
                    n = in0_
                    raise _dafny.TailCall()
                return result
                break

