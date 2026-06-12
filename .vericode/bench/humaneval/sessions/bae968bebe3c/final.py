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
    def HasProperDivisor(n, d):
        while True:
            with _dafny.label():
                if (d) < (2):
                    return False
                elif (_dafny.euclidian_modulus(n, d)) == (0):
                    return True
                elif True:
                    in0_ = n
                    in1_ = (d) - (1)
                    n = in0_
                    d = in1_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def IsPrime(n):
        if (n) < (2):
            return False
        elif True:
            return not(default__.HasProperDivisor(n, (n) - (1)))

    @staticmethod
    def PrimeLengthSpec(s):
        return default__.IsPrime(len(s))

    @staticmethod
    def prime__length(s):
        result: bool = False
        result = default__.PrimeLengthSpec(s)
        return result

