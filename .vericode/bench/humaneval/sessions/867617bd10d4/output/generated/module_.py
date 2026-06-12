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
    def CountDigitsNonNegSpec(n):
        if (n) < (10):
            if (_dafny.euclidian_modulus(n, 2)) == (0):
                return (1, 0)
            elif True:
                return (0, 1)
        elif True:
            d_0_rest_ = default__.CountDigitsNonNegSpec(_dafny.euclidian_division(n, 10))
            if (_dafny.euclidian_modulus(_dafny.euclidian_modulus(n, 10), 2)) == (0):
                return (((d_0_rest_)[0]) + (1), (d_0_rest_)[1])
            elif True:
                return ((d_0_rest_)[0], ((d_0_rest_)[1]) + (1))

    @staticmethod
    def EvenOddCountSpec(num):
        d_0_n_ = ((0) - (num) if (num) < (0) else num)
        return default__.CountDigitsNonNegSpec(d_0_n_)

    @staticmethod
    def even__odd__count(num):
        result: tuple = (int(0), int(0))
        d_0_n_: int
        if (num) < (0):
            d_0_n_ = (0) - (num)
        elif True:
            d_0_n_ = num
        out0_: tuple
        out0_ = default__.CountDigitsNonNeg(d_0_n_)
        result = out0_
        return result

    @staticmethod
    def CountDigitsNonNeg(n):
        result: tuple = (int(0), int(0))
        if (n) < (10):
            if (_dafny.euclidian_modulus(n, 2)) == (0):
                result = (1, 0)
            elif True:
                result = (0, 1)
        elif True:
            d_0_rest_: tuple
            out0_: tuple
            out0_ = default__.CountDigitsNonNeg(_dafny.euclidian_division(n, 10))
            d_0_rest_ = out0_
            if (_dafny.euclidian_modulus(_dafny.euclidian_modulus(n, 10), 2)) == (0):
                result = (((d_0_rest_)[0]) + (1), (d_0_rest_)[1])
            elif True:
                result = ((d_0_rest_)[0], ((d_0_rest_)[1]) + (1))
        return result

