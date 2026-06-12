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
    def LargestDivisorSearch(n, d):
        while True:
            with _dafny.label():
                if (d) <= (1):
                    return 1
                elif (_dafny.euclidian_modulus(n, d)) == (0):
                    return d
                elif True:
                    in0_ = n
                    in1_ = (d) - (1)
                    n = in0_
                    d = in1_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def LargestDivisorSpec(n):
        return default__.LargestDivisorSearch(n, (n) - (1))

    @staticmethod
    def largest__divisor(n):
        result: int = int(0)
        result = default__.LargestDivisorSpec(n)
        return result

