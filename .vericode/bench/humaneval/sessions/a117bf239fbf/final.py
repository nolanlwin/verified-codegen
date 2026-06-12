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
    def DigitsSpec(n):
        if (n) < (10):
            if (_dafny.euclidian_modulus(n, 2)) == (1):
                return n
            elif True:
                return 0
        elif True:
            d_0_rest_ = default__.DigitsSpec(_dafny.euclidian_division(n, 10))
            d_1_digit_ = _dafny.euclidian_modulus(n, 10)
            if (_dafny.euclidian_modulus(d_1_digit_, 2)) == (1):
                if (d_0_rest_) == (0):
                    return d_1_digit_
                elif True:
                    return (d_0_rest_) * (d_1_digit_)
            elif True:
                return d_0_rest_

    @staticmethod
    def digits(n):
        result: int = int(0)
        if (n) < (10):
            if (_dafny.euclidian_modulus(n, 2)) == (1):
                result = n
            elif True:
                result = 0
        elif True:
            d_0_rest_: int
            out0_: int
            out0_ = default__.digits(_dafny.euclidian_division(n, 10))
            d_0_rest_ = out0_
            d_1_digit_: int
            d_1_digit_ = _dafny.euclidian_modulus(n, 10)
            if (_dafny.euclidian_modulus(d_1_digit_, 2)) == (1):
                if (d_0_rest_) == (0):
                    result = d_1_digit_
                elif True:
                    result = (d_0_rest_) * (d_1_digit_)
            elif True:
                result = d_0_rest_
        return result

