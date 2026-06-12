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
    def ContainsCharSpec(chars, ch):
        if (len(chars)) == (0):
            return False
        elif True:
            return (((chars)[0]) == (ch)) or (default__.ContainsCharSpec(_dafny.SeqWithoutIsStrInference((chars)[1::]), ch))

    @staticmethod
    def DeleteCharsSpec(s, c):
        d_0___accumulator_ = _dafny.SeqWithoutIsStrInference([])
        while True:
            with _dafny.label():
                if (len(s)) == (0):
                    return (d_0___accumulator_) + (_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "")))
                elif default__.ContainsCharSpec(c, (s)[0]):
                    in0_ = _dafny.SeqWithoutIsStrInference((s)[1::])
                    in1_ = c
                    s = in0_
                    c = in1_
                    raise _dafny.TailCall()
                elif True:
                    d_0___accumulator_ = (d_0___accumulator_) + (_dafny.SeqWithoutIsStrInference([(s)[0]]))
                    in2_ = _dafny.SeqWithoutIsStrInference((s)[1::])
                    in3_ = c
                    s = in2_
                    c = in3_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def IsPalindromeSpec(s):
        if (len(s)) <= (1):
            return True
        elif True:
            return (((s)[0]) == ((s)[(len(s)) - (1)])) and (default__.IsPalindromeSpec(_dafny.SeqWithoutIsStrInference((s)[1:(len(s)) - (1):])))

    @staticmethod
    def ReverseDeleteSpec(s, c):
        d_0_filtered_ = default__.DeleteCharsSpec(s, c)
        return (d_0_filtered_, default__.IsPalindromeSpec(d_0_filtered_))

    @staticmethod
    def reverse__delete(s, c):
        result: tuple = (_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "")), False)
        result = default__.ReverseDeleteSpec(s, c)
        return result

