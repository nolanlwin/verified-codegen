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
    def Contains(s, x):
        if (len(s)) == (0):
            return False
        elif True:
            return (((s)[0]) == (x)) or (default__.Contains(_dafny.SeqWithoutIsStrInference((s)[1::]), x))

    @staticmethod
    def InsertSortedUnique(s, x):
        d_0___accumulator_ = _dafny.SeqWithoutIsStrInference([])
        while True:
            with _dafny.label():
                if (len(s)) == (0):
                    return (d_0___accumulator_) + (_dafny.SeqWithoutIsStrInference([x]))
                elif (x) == ((s)[0]):
                    return (d_0___accumulator_) + (s)
                elif (x) < ((s)[0]):
                    return (d_0___accumulator_) + ((_dafny.SeqWithoutIsStrInference([x])) + (s))
                elif True:
                    d_0___accumulator_ = (d_0___accumulator_) + (_dafny.SeqWithoutIsStrInference([(s)[0]]))
                    in0_ = _dafny.SeqWithoutIsStrInference((s)[1::])
                    in1_ = x
                    s = in0_
                    x = in1_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def CommonSpec(l1, l2):
        if (len(l1)) == (0):
            return _dafny.SeqWithoutIsStrInference([])
        elif default__.Contains(l2, (l1)[0]):
            return default__.InsertSortedUnique(default__.CommonSpec(_dafny.SeqWithoutIsStrInference((l1)[1::]), l2), (l1)[0])
        elif True:
            return default__.CommonSpec(_dafny.SeqWithoutIsStrInference((l1)[1::]), l2)

    @staticmethod
    def common(l1, l2):
        result: _dafny.Seq = _dafny.Seq({})
        if (len(l1)) == (0):
            result = _dafny.SeqWithoutIsStrInference([])
        elif True:
            d_0_tail_: _dafny.Seq
            out0_: _dafny.Seq
            out0_ = default__.common(_dafny.SeqWithoutIsStrInference((l1)[1::]), l2)
            d_0_tail_ = out0_
            if default__.Contains(l2, (l1)[0]):
                result = default__.InsertSortedUnique(d_0_tail_, (l1)[0])
            elif True:
                result = d_0_tail_
        return result

