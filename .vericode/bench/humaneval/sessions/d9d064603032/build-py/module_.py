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
    def CountEvenSpec(nums):
        d_0___accumulator_ = 0
        while True:
            with _dafny.label():
                if (len(nums)) == (0):
                    return (0) + (d_0___accumulator_)
                elif True:
                    d_0___accumulator_ = (d_0___accumulator_) + ((1 if (_dafny.euclidian_modulus((nums)[0], 2)) == (0) else 0))
                    in0_ = _dafny.SeqWithoutIsStrInference((nums)[1::])
                    nums = in0_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def ExchangeSpec(lst1, lst2):
        if ((default__.CountEvenSpec(lst1)) + (default__.CountEvenSpec(lst2))) >= (len(lst1)):
            return _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "YES"))
        elif True:
            return _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "NO"))

    @staticmethod
    def exchange(lst1, lst2):
        result: _dafny.Seq = _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, ""))
        if ((default__.CountEvenSpec(lst1)) + (default__.CountEvenSpec(lst2))) >= (len(lst1)):
            result = _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "YES"))
        elif True:
            result = _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "NO"))
        return result

