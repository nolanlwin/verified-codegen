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
    def ReverseSpec(s):
        d_0___accumulator_ = _dafny.SeqWithoutIsStrInference([])
        while True:
            with _dafny.label():
                if (len(s)) == (0):
                    return (_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, ""))) + (d_0___accumulator_)
                elif True:
                    d_0___accumulator_ = (_dafny.SeqWithoutIsStrInference((s)[0:1:])) + (d_0___accumulator_)
                    in0_ = _dafny.SeqWithoutIsStrInference((s)[1::])
                    s = in0_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def IsPalindromeSpec(s):
        return (s) == (default__.ReverseSpec(s))

    @staticmethod
    def PrefixBeforeLongestPalindromicSuffixSpec(s):
        d_0___accumulator_ = _dafny.SeqWithoutIsStrInference([])
        while True:
            with _dafny.label():
                if (len(s)) == (0):
                    return (d_0___accumulator_) + (_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "")))
                elif default__.IsPalindromeSpec(s):
                    return (d_0___accumulator_) + (_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "")))
                elif True:
                    d_0___accumulator_ = (d_0___accumulator_) + (_dafny.SeqWithoutIsStrInference((s)[0:1:]))
                    in0_ = _dafny.SeqWithoutIsStrInference((s)[1::])
                    s = in0_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def MakePalindromeSpec(s):
        return (s) + (default__.ReverseSpec(default__.PrefixBeforeLongestPalindromicSuffixSpec(s)))

    @staticmethod
    def make__palindrome(s):
        result: _dafny.Seq = _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, ""))
        d_0_prefix_: _dafny.Seq
        out0_: _dafny.Seq
        out0_ = default__.PrefixBeforeLongestPalindromicSuffixImpl(s)
        d_0_prefix_ = out0_
        d_1_reversedPrefix_: _dafny.Seq
        out1_: _dafny.Seq
        out1_ = default__.ReverseImpl(d_0_prefix_)
        d_1_reversedPrefix_ = out1_
        result = (s) + (d_1_reversedPrefix_)
        return result

    @staticmethod
    def ReverseImpl(s):
        r: _dafny.Seq = _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, ""))
        if (len(s)) == (0):
            r = _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, ""))
        elif True:
            d_0_t_: _dafny.Seq
            out0_: _dafny.Seq
            out0_ = default__.ReverseImpl(_dafny.SeqWithoutIsStrInference((s)[1::]))
            d_0_t_ = out0_
            r = (d_0_t_) + (_dafny.SeqWithoutIsStrInference((s)[0:1:]))
        return r

    @staticmethod
    def PrefixBeforeLongestPalindromicSuffixImpl(s):
        p: _dafny.Seq = _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, ""))
        if (len(s)) == (0):
            p = _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, ""))
        elif default__.IsPalindromeSpec(s):
            p = _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, ""))
        elif True:
            d_0_q_: _dafny.Seq
            out0_: _dafny.Seq
            out0_ = default__.PrefixBeforeLongestPalindromicSuffixImpl(_dafny.SeqWithoutIsStrInference((s)[1::]))
            d_0_q_ = out0_
            p = (_dafny.SeqWithoutIsStrInference((s)[0:1:])) + (d_0_q_)
        return p

