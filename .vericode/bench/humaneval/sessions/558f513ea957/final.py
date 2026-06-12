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
    def IsWordsStringDelimiter(c):
        return ((c) == (_dafny.CodePoint(' '))) or ((c) == (_dafny.CodePoint(',')))

    @staticmethod
    def IsSeparator(c):
        return ((c) == (_dafny.CodePoint(' '))) or ((c) == (_dafny.CodePoint(',')))

    @staticmethod
    def WordsStringAcc(s, i, current):
        d_0___accumulator_ = _dafny.SeqWithoutIsStrInference([])
        while True:
            with _dafny.label():
                if (i) == (len(s)):
                    if (len(current)) == (0):
                        return (d_0___accumulator_) + (_dafny.SeqWithoutIsStrInference([]))
                    elif True:
                        return (d_0___accumulator_) + (_dafny.SeqWithoutIsStrInference([current]))
                elif default__.IsSeparator((s)[i]):
                    if (len(current)) == (0):
                        in0_ = s
                        in1_ = (i) + (1)
                        in2_ = _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, ""))
                        s = in0_
                        i = in1_
                        current = in2_
                        raise _dafny.TailCall()
                    elif True:
                        d_0___accumulator_ = (d_0___accumulator_) + (_dafny.SeqWithoutIsStrInference([current]))
                        in3_ = s
                        in4_ = (i) + (1)
                        in5_ = _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, ""))
                        s = in3_
                        i = in4_
                        current = in5_
                        raise _dafny.TailCall()
                elif True:
                    in6_ = s
                    in7_ = (i) + (1)
                    in8_ = (current) + (_dafny.SeqWithoutIsStrInference([(s)[i]]))
                    s = in6_
                    i = in7_
                    current = in8_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def WordsStringSpec(s):
        return default__.WordsStringAcc(s, 0, _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "")))

    @staticmethod
    def words__string(s):
        result: _dafny.Seq = _dafny.Seq({})
        out0_: _dafny.Seq
        out0_ = default__.WordsStringAccMethod(s, 0, _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "")))
        result = out0_
        return result

    @staticmethod
    def WordsStringAccMethod(s, i, current):
        result: _dafny.Seq = _dafny.Seq({})
        if (i) == (len(s)):
            if (len(current)) == (0):
                result = _dafny.SeqWithoutIsStrInference([])
            elif True:
                result = _dafny.SeqWithoutIsStrInference([current])
        elif default__.IsSeparator((s)[i]):
            if (len(current)) == (0):
                out0_: _dafny.Seq
                out0_ = default__.WordsStringAccMethod(s, (i) + (1), _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "")))
                result = out0_
            elif True:
                d_0_rest_: _dafny.Seq
                out1_: _dafny.Seq
                out1_ = default__.WordsStringAccMethod(s, (i) + (1), _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "")))
                d_0_rest_ = out1_
                result = (_dafny.SeqWithoutIsStrInference([current])) + (d_0_rest_)
        elif True:
            out2_: _dafny.Seq
            out2_ = default__.WordsStringAccMethod(s, (i) + (1), (current) + (_dafny.SeqWithoutIsStrInference([(s)[i]])))
            result = out2_
        return result

