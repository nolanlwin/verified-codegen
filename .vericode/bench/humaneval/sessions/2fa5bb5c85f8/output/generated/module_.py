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
    def SumProductSpec(numbers):
        if (len(numbers)) == (0):
            return (0, 1)
        elif True:
            d_0_rest_ = default__.SumProductSpec(_dafny.SeqWithoutIsStrInference((numbers)[1::]))
            return (((numbers)[0]) + ((d_0_rest_)[0]), ((numbers)[0]) * ((d_0_rest_)[1]))

    @staticmethod
    def sum__product(numbers):
        result: tuple = (int(0), int(0))
        if (len(numbers)) == (0):
            result = (0, 1)
        elif True:
            d_0_rest_: tuple
            out0_: tuple
            out0_ = default__.sum__product(_dafny.SeqWithoutIsStrInference((numbers)[1::]))
            d_0_rest_ = out0_
            result = (((numbers)[0]) + ((d_0_rest_)[0]), ((numbers)[0]) * ((d_0_rest_)[1]))
        return result

