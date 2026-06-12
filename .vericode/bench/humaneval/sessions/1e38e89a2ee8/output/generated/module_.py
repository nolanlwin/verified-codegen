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
    def GenerateIntegersSpec(a, b):
        d_0___accumulator_ = _dafny.SeqWithoutIsStrInference([])
        while True:
            with _dafny.label():
                if (a) > (b):
                    in0_ = b
                    in1_ = a
                    a = in0_
                    b = in1_
                    raise _dafny.TailCall()
                elif (a) > (9):
                    return (d_0___accumulator_) + (_dafny.SeqWithoutIsStrInference([]))
                elif (a) == (b):
                    if (_dafny.euclidian_modulus(a, 2)) == (0):
                        return (d_0___accumulator_) + (_dafny.SeqWithoutIsStrInference([a]))
                    elif True:
                        return (d_0___accumulator_) + (_dafny.SeqWithoutIsStrInference([]))
                elif True:
                    d_0___accumulator_ = (d_0___accumulator_) + ((_dafny.SeqWithoutIsStrInference([a]) if (_dafny.euclidian_modulus(a, 2)) == (0) else _dafny.SeqWithoutIsStrInference([])))
                    in2_ = (a) + (1)
                    in3_ = b
                    a = in2_
                    b = in3_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def generate__integers(a, b):
        result: _dafny.Seq = _dafny.Seq({})
        if (a) > (b):
            out0_: _dafny.Seq
            out0_ = default__.generate__integers(b, a)
            result = out0_
        elif (a) > (9):
            result = _dafny.SeqWithoutIsStrInference([])
        elif (a) == (b):
            if (_dafny.euclidian_modulus(a, 2)) == (0):
                result = _dafny.SeqWithoutIsStrInference([a])
            elif True:
                result = _dafny.SeqWithoutIsStrInference([])
        elif True:
            d_0_tail_: _dafny.Seq
            out1_: _dafny.Seq
            out1_ = default__.generate__integers((a) + (1), b)
            d_0_tail_ = out1_
            if (_dafny.euclidian_modulus(a, 2)) == (0):
                result = (_dafny.SeqWithoutIsStrInference([a])) + (d_0_tail_)
            elif True:
                result = d_0_tail_
        return result

