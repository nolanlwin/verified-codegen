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
    def PluckSpec(arr):
        if (len(arr)) == (0):
            return _dafny.SeqWithoutIsStrInference([])
        elif True:
            d_0_tail_ = default__.PluckSpec(_dafny.SeqWithoutIsStrInference((arr)[1::]))
            if (_dafny.euclidian_modulus((arr)[0], 2)) == (0):
                if (len(d_0_tail_)) < (2):
                    return _dafny.SeqWithoutIsStrInference([(arr)[0], 0])
                elif ((arr)[0]) <= ((d_0_tail_)[0]):
                    return _dafny.SeqWithoutIsStrInference([(arr)[0], 0])
                elif True:
                    return _dafny.SeqWithoutIsStrInference([(d_0_tail_)[0], ((d_0_tail_)[1]) + (1)])
            elif (len(d_0_tail_)) < (2):
                return _dafny.SeqWithoutIsStrInference([])
            elif True:
                return _dafny.SeqWithoutIsStrInference([(d_0_tail_)[0], ((d_0_tail_)[1]) + (1)])

    @staticmethod
    def pluck(arr):
        result: _dafny.Seq = _dafny.Seq({})
        if (len(arr)) == (0):
            result = _dafny.SeqWithoutIsStrInference([])
        elif True:
            d_0_tail_: _dafny.Seq
            out0_: _dafny.Seq
            out0_ = default__.pluck(_dafny.SeqWithoutIsStrInference((arr)[1::]))
            d_0_tail_ = out0_
            if (_dafny.euclidian_modulus((arr)[0], 2)) == (0):
                if (len(d_0_tail_)) < (2):
                    result = _dafny.SeqWithoutIsStrInference([(arr)[0], 0])
                elif ((arr)[0]) <= ((d_0_tail_)[0]):
                    result = _dafny.SeqWithoutIsStrInference([(arr)[0], 0])
                elif True:
                    result = _dafny.SeqWithoutIsStrInference([(d_0_tail_)[0], ((d_0_tail_)[1]) + (1)])
            elif True:
                if (len(d_0_tail_)) < (2):
                    result = _dafny.SeqWithoutIsStrInference([])
                elif True:
                    result = _dafny.SeqWithoutIsStrInference([(d_0_tail_)[0], ((d_0_tail_)[1]) + (1)])
        return result

