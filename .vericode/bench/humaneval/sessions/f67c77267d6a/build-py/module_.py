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
    def InsertIntoFirstWord(c, t):
        d_0___accumulator_ = _dafny.SeqWithoutIsStrInference([])
        while True:
            with _dafny.label():
                if (len(t)) == (0):
                    return (d_0___accumulator_) + (_dafny.SeqWithoutIsStrInference([c]))
                elif ((t)[0]) == ((_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, " ")))[0]):
                    return (d_0___accumulator_) + ((_dafny.SeqWithoutIsStrInference([c])) + (t))
                elif (ord(c)) <= (ord((t)[0])):
                    return (d_0___accumulator_) + ((_dafny.SeqWithoutIsStrInference([c])) + (t))
                elif True:
                    d_0___accumulator_ = (d_0___accumulator_) + (_dafny.SeqWithoutIsStrInference([(t)[0]]))
                    in0_ = c
                    in1_ = _dafny.SeqWithoutIsStrInference((t)[1::])
                    c = in0_
                    t = in1_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def AntiShuffleSpec(s):
        if (len(s)) == (0):
            return _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, ""))
        elif ((s)[0]) == ((_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, " ")))[0]):
            return (_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, " "))) + (default__.AntiShuffleSpec(_dafny.SeqWithoutIsStrInference((s)[1::])))
        elif True:
            return default__.InsertIntoFirstWord((s)[0], default__.AntiShuffleSpec(_dafny.SeqWithoutIsStrInference((s)[1::])))

    @staticmethod
    def anti__shuffle(s):
        result: _dafny.Seq = _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, ""))
        if (len(s)) == (0):
            result = _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, ""))
        elif ((s)[0]) == ((_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, " ")))[0]):
            d_0_tail_: _dafny.Seq
            out0_: _dafny.Seq
            out0_ = default__.anti__shuffle(_dafny.SeqWithoutIsStrInference((s)[1::]))
            d_0_tail_ = out0_
            result = (_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, " "))) + (d_0_tail_)
        elif True:
            d_1_tail_: _dafny.Seq
            out1_: _dafny.Seq
            out1_ = default__.anti__shuffle(_dafny.SeqWithoutIsStrInference((s)[1::]))
            d_1_tail_ = out1_
            out2_: _dafny.Seq
            out2_ = default__.InsertIntoFirstWordMethod((s)[0], d_1_tail_)
            result = out2_
        return result

    @staticmethod
    def InsertIntoFirstWordMethod(c, t):
        result: _dafny.Seq = _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, ""))
        if (len(t)) == (0):
            result = _dafny.SeqWithoutIsStrInference([c])
        elif ((t)[0]) == ((_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, " ")))[0]):
            result = (_dafny.SeqWithoutIsStrInference([c])) + (t)
        elif (ord(c)) <= (ord((t)[0])):
            result = (_dafny.SeqWithoutIsStrInference([c])) + (t)
        elif True:
            d_0_rest_: _dafny.Seq
            out0_: _dafny.Seq
            out0_ = default__.InsertIntoFirstWordMethod(c, _dafny.SeqWithoutIsStrInference((t)[1::]))
            d_0_rest_ = out0_
            result = (_dafny.SeqWithoutIsStrInference([(t)[0]])) + (d_0_rest_)
        return result

