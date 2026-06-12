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
    def InsertAsc(x, s):
        d_0___accumulator_ = _dafny.SeqWithoutIsStrInference([])
        while True:
            with _dafny.label():
                if (len(s)) == (0):
                    return (d_0___accumulator_) + (_dafny.SeqWithoutIsStrInference([x]))
                elif (x) <= ((s)[0]):
                    return (d_0___accumulator_) + ((_dafny.SeqWithoutIsStrInference([x])) + (s))
                elif True:
                    d_0___accumulator_ = (d_0___accumulator_) + (_dafny.SeqWithoutIsStrInference([(s)[0]]))
                    in0_ = x
                    in1_ = _dafny.SeqWithoutIsStrInference((s)[1::])
                    x = in0_
                    s = in1_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def SortAsc(s):
        if (len(s)) == (0):
            return _dafny.SeqWithoutIsStrInference([])
        elif True:
            return default__.InsertAsc((s)[0], default__.SortAsc(_dafny.SeqWithoutIsStrInference((s)[1::])))

    @staticmethod
    def InsertDesc(x, s):
        d_0___accumulator_ = _dafny.SeqWithoutIsStrInference([])
        while True:
            with _dafny.label():
                if (len(s)) == (0):
                    return (d_0___accumulator_) + (_dafny.SeqWithoutIsStrInference([x]))
                elif (x) >= ((s)[0]):
                    return (d_0___accumulator_) + ((_dafny.SeqWithoutIsStrInference([x])) + (s))
                elif True:
                    d_0___accumulator_ = (d_0___accumulator_) + (_dafny.SeqWithoutIsStrInference([(s)[0]]))
                    in0_ = x
                    in1_ = _dafny.SeqWithoutIsStrInference((s)[1::])
                    x = in0_
                    s = in1_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def SortDesc(s):
        if (len(s)) == (0):
            return _dafny.SeqWithoutIsStrInference([])
        elif True:
            return default__.InsertDesc((s)[0], default__.SortDesc(_dafny.SeqWithoutIsStrInference((s)[1::])))

    @staticmethod
    def SortArraySpec(a):
        if (len(a)) <= (1):
            return a
        elif (_dafny.euclidian_modulus(((a)[0]) + ((a)[(len(a)) - (1)]), 2)) == (1):
            return default__.SortAsc(a)
        elif True:
            return default__.SortDesc(a)

    @staticmethod
    def SortArray(a):
        result: _dafny.Seq = _dafny.Seq({})
        if (len(a)) <= (1):
            result = a
        elif (_dafny.euclidian_modulus(((a)[0]) + ((a)[(len(a)) - (1)]), 2)) == (1):
            result = default__.SortAsc(a)
        elif True:
            result = default__.SortDesc(a)
        return result

