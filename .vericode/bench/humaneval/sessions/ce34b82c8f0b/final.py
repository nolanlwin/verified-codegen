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
    def DerivativeSpec(xs, degree):
        d_0___accumulator_ = _dafny.SeqWithoutIsStrInference([])
        while True:
            with _dafny.label():
                if (len(xs)) == (0):
                    return (d_0___accumulator_) + (_dafny.SeqWithoutIsStrInference([]))
                elif (degree) == (0):
                    in0_ = _dafny.SeqWithoutIsStrInference((xs)[1::])
                    in1_ = (degree) + (1)
                    xs = in0_
                    degree = in1_
                    raise _dafny.TailCall()
                elif True:
                    d_0___accumulator_ = (d_0___accumulator_) + (_dafny.SeqWithoutIsStrInference([(degree) * ((xs)[0])]))
                    in2_ = _dafny.SeqWithoutIsStrInference((xs)[1::])
                    in3_ = (degree) + (1)
                    xs = in2_
                    degree = in3_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def derivative(xs):
        result: _dafny.Seq = _dafny.Seq({})
        out0_: _dafny.Seq
        out0_ = default__.DerivativeFrom(xs, 0)
        result = out0_
        return result

    @staticmethod
    def DerivativeFrom(xs, degree):
        result: _dafny.Seq = _dafny.Seq({})
        if (len(xs)) == (0):
            result = _dafny.SeqWithoutIsStrInference([])
        elif (degree) == (0):
            out0_: _dafny.Seq
            out0_ = default__.DerivativeFrom(_dafny.SeqWithoutIsStrInference((xs)[1::]), (degree) + (1))
            result = out0_
        elif True:
            d_0_tail_: _dafny.Seq
            out1_: _dafny.Seq
            out1_ = default__.DerivativeFrom(_dafny.SeqWithoutIsStrInference((xs)[1::]), (degree) + (1))
            d_0_tail_ = out1_
            result = (_dafny.SeqWithoutIsStrInference([(degree) * ((xs)[0])])) + (d_0_tail_)
        return result

