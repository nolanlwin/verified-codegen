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
    def IsLowercaseChar(ch):
        return ((ord(_dafny.CodePoint('a'))) <= (ord(ch))) and ((ord(ch)) <= (ord(_dafny.CodePoint('z'))))

    @staticmethod
    def LowercaseString(s):
        if (len(s)) == (0):
            return True
        elif True:
            return (default__.IsLowercaseChar((s)[0])) and (default__.LowercaseString(_dafny.SeqWithoutIsStrInference((s)[1::])))

    @staticmethod
    def DecodeShiftChar(ch):
        d_0_shifted_ = _dafny.euclidian_modulus((((ord(ch)) - (ord(_dafny.CodePoint('a')))) - (5)) + (26), 26)
        return _dafny.CodePoint(chr((d_0_shifted_) + (ord(_dafny.CodePoint('a')))))

    @staticmethod
    def DecodeShiftSpec(s):
        d_0___accumulator_ = _dafny.SeqWithoutIsStrInference([])
        while True:
            with _dafny.label():
                if (len(s)) == (0):
                    return (d_0___accumulator_) + (_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "")))
                elif True:
                    d_0___accumulator_ = (d_0___accumulator_) + (_dafny.SeqWithoutIsStrInference([default__.DecodeShiftChar((s)[0])]))
                    in0_ = _dafny.SeqWithoutIsStrInference((s)[1::])
                    s = in0_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def decode__shift(s):
        result: _dafny.Seq = _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, ""))
        if (len(s)) == (0):
            result = _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, ""))
        elif True:
            d_0_tail_: _dafny.Seq
            out0_: _dafny.Seq
            out0_ = default__.decode__shift(_dafny.SeqWithoutIsStrInference((s)[1::]))
            d_0_tail_ = out0_
            result = (_dafny.SeqWithoutIsStrInference([default__.DecodeShiftChar((s)[0])])) + (d_0_tail_)
        return result

