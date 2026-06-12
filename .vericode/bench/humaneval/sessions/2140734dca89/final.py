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
    def LexLeq(a, b):
        while True:
            with _dafny.label():
                if (len(a)) == (0):
                    return True
                elif (len(b)) == (0):
                    return False
                elif ((a)[0]) < ((b)[0]):
                    return True
                elif ((b)[0]) < ((a)[0]):
                    return False
                elif True:
                    in0_ = _dafny.SeqWithoutIsStrInference((a)[1::])
                    in1_ = _dafny.SeqWithoutIsStrInference((b)[1::])
                    a = in0_
                    b = in1_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def WordLeq(a, b):
        if (len(a)) < (len(b)):
            return True
        elif (len(a)) > (len(b)):
            return False
        elif True:
            return default__.LexLeq(a, b)

    @staticmethod
    def InsertSorted(w, s):
        d_0___accumulator_ = _dafny.SeqWithoutIsStrInference([])
        while True:
            with _dafny.label():
                if ((len(s)) == (0)) or (default__.WordLeq(w, (s)[0])):
                    return (d_0___accumulator_) + ((_dafny.SeqWithoutIsStrInference([w])) + (s))
                elif True:
                    d_0___accumulator_ = (d_0___accumulator_) + (_dafny.SeqWithoutIsStrInference([(s)[0]]))
                    in0_ = w
                    in1_ = _dafny.SeqWithoutIsStrInference((s)[1::])
                    w = in0_
                    s = in1_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def SortedListSumSpec(lst):
        if (len(lst)) == (0):
            return _dafny.SeqWithoutIsStrInference([])
        elif (_dafny.euclidian_modulus(len((lst)[0]), 2)) == (1):
            return default__.SortedListSumSpec(_dafny.SeqWithoutIsStrInference((lst)[1::]))
        elif True:
            return default__.InsertSorted((lst)[0], default__.SortedListSumSpec(_dafny.SeqWithoutIsStrInference((lst)[1::])))

    @staticmethod
    def sorted__list__sum(lst):
        result: _dafny.Seq = _dafny.Seq({})
        if (len(lst)) == (0):
            result = _dafny.SeqWithoutIsStrInference([])
        elif (_dafny.euclidian_modulus(len((lst)[0]), 2)) == (1):
            out0_: _dafny.Seq
            out0_ = default__.sorted__list__sum(_dafny.SeqWithoutIsStrInference((lst)[1::]))
            result = out0_
        elif True:
            d_0_tail_: _dafny.Seq
            out1_: _dafny.Seq
            out1_ = default__.sorted__list__sum(_dafny.SeqWithoutIsStrInference((lst)[1::]))
            d_0_tail_ = out1_
            result = default__.InsertSorted((lst)[0], d_0_tail_)
        return result

