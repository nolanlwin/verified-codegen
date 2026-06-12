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
    def AbsReal(x):
        if (x) < (_dafny.BigRational('0e0')):
            return (_dafny.BigRational('0e0')) - (x)
        elif True:
            return x

    @staticmethod
    def CloseToAnySpec(x, numbers, threshold):
        if (len(numbers)) == (0):
            return False
        elif True:
            return ((default__.AbsReal((x) - ((numbers)[0]))) < (threshold)) or (default__.CloseToAnySpec(x, _dafny.SeqWithoutIsStrInference((numbers)[1::]), threshold))

    @staticmethod
    def HasCloseElementsSpec(numbers, threshold):
        if (len(numbers)) <= (1):
            return False
        elif True:
            return (default__.CloseToAnySpec((numbers)[0], _dafny.SeqWithoutIsStrInference((numbers)[1::]), threshold)) or (default__.HasCloseElementsSpec(_dafny.SeqWithoutIsStrInference((numbers)[1::]), threshold))

    @staticmethod
    def has__close__elements(numbers, threshold):
        result: bool = False
        if (len(numbers)) <= (1):
            result = False
        elif True:
            d_0_close_: bool
            out0_: bool
            out0_ = default__.close__to__any((numbers)[0], _dafny.SeqWithoutIsStrInference((numbers)[1::]), threshold)
            d_0_close_ = out0_
            d_1_rest_: bool
            out1_: bool
            out1_ = default__.has__close__elements(_dafny.SeqWithoutIsStrInference((numbers)[1::]), threshold)
            d_1_rest_ = out1_
            result = (d_0_close_) or (d_1_rest_)
        return result

    @staticmethod
    def AbsDistReal(a, b):
        return default__.AbsReal((a) - (b))

    @staticmethod
    def close__to__any(x, numbers, threshold):
        result: bool = False
        if (len(numbers)) == (0):
            result = False
        elif True:
            d_0_tailResult_: bool
            out0_: bool
            out0_ = default__.close__to__any(x, _dafny.SeqWithoutIsStrInference((numbers)[1::]), threshold)
            d_0_tailResult_ = out0_
            result = ((default__.AbsDistReal(x, (numbers)[0])) < (threshold)) or (d_0_tailResult_)
        return result

