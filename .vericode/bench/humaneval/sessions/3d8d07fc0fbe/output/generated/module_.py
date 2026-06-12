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
    def IsDigitChar(c):
        return ((_dafny.CodePoint('0')) <= (c)) and ((c) <= (_dafny.CodePoint('9')))

    @staticmethod
    def IsOddDigitChar(c):
        return (((((c) == (_dafny.CodePoint('1'))) or ((c) == (_dafny.CodePoint('3')))) or ((c) == (_dafny.CodePoint('5')))) or ((c) == (_dafny.CodePoint('7')))) or ((c) == (_dafny.CodePoint('9')))

    @staticmethod
    def IsDigitString(s):
        if (len(s)) == (0):
            return True
        elif True:
            return (default__.IsDigitChar((s)[0])) and (default__.IsDigitString(_dafny.SeqWithoutIsStrInference((s)[1::])))

    @staticmethod
    def AllDigitStrings(lst):
        if (len(lst)) == (0):
            return True
        elif True:
            return (default__.IsDigitString((lst)[0])) and (default__.AllDigitStrings(_dafny.SeqWithoutIsStrInference((lst)[1::])))

    @staticmethod
    def CountOddDigitsSpec(s):
        d_0___accumulator_ = 0
        while True:
            with _dafny.label():
                if (len(s)) == (0):
                    return (0) + (d_0___accumulator_)
                elif True:
                    d_0___accumulator_ = (d_0___accumulator_) + ((1 if default__.IsOddDigitChar((s)[0]) else 0))
                    in0_ = _dafny.SeqWithoutIsStrInference((s)[1::])
                    s = in0_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def DigitToString(n):
        if (n) == (0):
            return _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "0"))
        elif (n) == (1):
            return _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "1"))
        elif (n) == (2):
            return _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "2"))
        elif (n) == (3):
            return _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "3"))
        elif (n) == (4):
            return _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "4"))
        elif (n) == (5):
            return _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "5"))
        elif (n) == (6):
            return _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "6"))
        elif (n) == (7):
            return _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "7"))
        elif (n) == (8):
            return _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "8"))
        elif True:
            return _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "9"))

    @staticmethod
    def IntToString(n):
        if (n) < (0):
            return (_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "-"))) + (default__.IntToString((0) - (n)))
        elif (n) < (10):
            return default__.DigitToString(n)
        elif True:
            return (default__.IntToString(_dafny.euclidian_division(n, 10))) + (default__.DigitToString(_dafny.euclidian_modulus(n, 10)))

    @staticmethod
    def OddCountMessage(count):
        d_0_t_ = default__.IntToString(count)
        return ((((((((_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "the number of odd elements "))) + (d_0_t_)) + (_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "n the str")))) + (d_0_t_)) + (_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "ng ")))) + (d_0_t_)) + (_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, " of the ")))) + (d_0_t_)) + (_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "nput.")))

    @staticmethod
    def OddCountSpec(lst):
        d_0___accumulator_ = _dafny.SeqWithoutIsStrInference([])
        while True:
            with _dafny.label():
                if (len(lst)) == (0):
                    return (d_0___accumulator_) + (_dafny.SeqWithoutIsStrInference([]))
                elif True:
                    d_0___accumulator_ = (d_0___accumulator_) + (_dafny.SeqWithoutIsStrInference([default__.OddCountMessage(default__.CountOddDigitsSpec((lst)[0]))]))
                    in0_ = _dafny.SeqWithoutIsStrInference((lst)[1::])
                    lst = in0_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def odd__count(lst):
        result: _dafny.Seq = _dafny.Seq({})
        if (len(lst)) == (0):
            result = _dafny.SeqWithoutIsStrInference([])
        elif True:
            d_0_tail_: _dafny.Seq
            out0_: _dafny.Seq
            out0_ = default__.odd__count(_dafny.SeqWithoutIsStrInference((lst)[1::]))
            d_0_tail_ = out0_
            result = (_dafny.SeqWithoutIsStrInference([default__.OddCountMessage(default__.CountOddDigitsSpec((lst)[0]))])) + (d_0_tail_)
        return result

