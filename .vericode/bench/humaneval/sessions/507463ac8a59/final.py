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
    def StripLastTwo(s):
        if (len(s)) <= (2):
            return _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, ""))
        elif True:
            return _dafny.SeqWithoutIsStrInference((s)[:(len(s)) - (2):])

    @staticmethod
    def BitChar(n):
        if (_dafny.euclidian_modulus(n, 2)) == (0):
            return _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "0"))
        elif True:
            return _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "1"))

    @staticmethod
    def DecimalToBinarySpec(decimal):
        if (decimal) < (2):
            return ((_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "db"))) + ((_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "0")) if (decimal) == (0) else _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "1"))))) + (_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "db")))
        elif True:
            return ((default__.StripLastTwo(default__.DecimalToBinarySpec(_dafny.euclidian_division(decimal, 2)))) + (default__.BitChar(decimal))) + (_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "db")))

    @staticmethod
    def decimal__to__binary(decimal):
        result: _dafny.Seq = _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, ""))
        if (decimal) < (2):
            if (decimal) == (0):
                result = _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "db0db"))
            elif True:
                result = _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "db1db"))
        elif True:
            d_0_partial_: _dafny.Seq
            out0_: _dafny.Seq
            out0_ = default__.decimal__to__binary(_dafny.euclidian_division(decimal, 2))
            d_0_partial_ = out0_
            result = ((default__.StripLastTwo(d_0_partial_)) + (default__.BitChar(decimal))) + (_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "db")))
        return result

