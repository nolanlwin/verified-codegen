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
    def CountLetter(s, letter):
        d_0___accumulator_ = 0
        while True:
            with _dafny.label():
                if (len(s)) == (0):
                    return (0) + (d_0___accumulator_)
                elif True:
                    d_0___accumulator_ = (d_0___accumulator_) + ((1 if (((s)[0]) != (_dafny.CodePoint(' '))) and ((_dafny.SeqWithoutIsStrInference((s)[0:1:])) == (letter)) else 0))
                    in0_ = _dafny.SeqWithoutIsStrInference((s)[1::])
                    in1_ = letter
                    s = in0_
                    letter = in1_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def MaxCountAux(original, rest):
        if (len(rest)) == (0):
            return 0
        elif True:
            d_0_tailMax_ = default__.MaxCountAux(original, _dafny.SeqWithoutIsStrInference((rest)[1::]))
            if ((rest)[0]) == (_dafny.CodePoint(' ')):
                return d_0_tailMax_
            elif True:
                d_1_count_ = default__.CountLetter(original, _dafny.SeqWithoutIsStrInference((rest)[0:1:]))
                if (d_1_count_) >= (d_0_tailMax_):
                    return d_1_count_
                elif True:
                    return d_0_tailMax_

    @staticmethod
    def MaxCountSpec(test):
        return default__.MaxCountAux(test, test)

    @staticmethod
    def HistogramBuild(original, rest, maxCount):
        if (len(rest)) == (0):
            return _dafny.Map({})
        elif True:
            d_0_tail_ = default__.HistogramBuild(original, _dafny.SeqWithoutIsStrInference((rest)[1::]), maxCount)
            if ((rest)[0]) == (_dafny.CodePoint(' ')):
                return d_0_tail_
            elif True:
                d_1_letter_ = _dafny.SeqWithoutIsStrInference((rest)[0:1:])
                d_2_count_ = default__.CountLetter(original, d_1_letter_)
                if ((maxCount) > (0)) and ((d_2_count_) == (maxCount)):
                    return (d_0_tail_).set(d_1_letter_, d_2_count_)
                elif True:
                    return d_0_tail_

    @staticmethod
    def HistogramSpec(test):
        d_0_maxCount_ = default__.MaxCountSpec(test)
        return default__.HistogramBuild(test, test, d_0_maxCount_)

    @staticmethod
    def histogram(test):
        result: _dafny.Map = _dafny.Map({})
        d_0_maxCount_: int
        out0_: int
        out0_ = default__.MaxCountAuxMethod(test, test)
        d_0_maxCount_ = out0_
        out1_: _dafny.Map
        out1_ = default__.HistogramBuildMethod(test, test, d_0_maxCount_)
        result = out1_
        return result

    @staticmethod
    def CountLetterMethod(s, letter):
        count: int = int(0)
        if (len(s)) == (0):
            count = 0
        elif True:
            d_0_tail_: int
            out0_: int
            out0_ = default__.CountLetterMethod(_dafny.SeqWithoutIsStrInference((s)[1::]), letter)
            d_0_tail_ = out0_
            if (((s)[0]) != (_dafny.CodePoint(' '))) and ((_dafny.SeqWithoutIsStrInference((s)[0:1:])) == (letter)):
                count = (1) + (d_0_tail_)
            elif True:
                count = d_0_tail_
        return count

    @staticmethod
    def MaxCountAuxMethod(original, rest):
        maxCount: int = int(0)
        if (len(rest)) == (0):
            maxCount = 0
        elif True:
            d_0_tailMax_: int
            out0_: int
            out0_ = default__.MaxCountAuxMethod(original, _dafny.SeqWithoutIsStrInference((rest)[1::]))
            d_0_tailMax_ = out0_
            if ((rest)[0]) == (_dafny.CodePoint(' ')):
                maxCount = d_0_tailMax_
            elif True:
                d_1_count_: int
                out1_: int
                out1_ = default__.CountLetterMethod(original, _dafny.SeqWithoutIsStrInference((rest)[0:1:]))
                d_1_count_ = out1_
                if (d_1_count_) >= (d_0_tailMax_):
                    maxCount = d_1_count_
                elif True:
                    maxCount = d_0_tailMax_
        return maxCount

    @staticmethod
    def HistogramBuildMethod(original, rest, maxCount):
        result: _dafny.Map = _dafny.Map({})
        if (len(rest)) == (0):
            result = _dafny.Map({})
        elif True:
            d_0_tail_: _dafny.Map
            out0_: _dafny.Map
            out0_ = default__.HistogramBuildMethod(original, _dafny.SeqWithoutIsStrInference((rest)[1::]), maxCount)
            d_0_tail_ = out0_
            if ((rest)[0]) == (_dafny.CodePoint(' ')):
                result = d_0_tail_
            elif True:
                d_1_letter_: _dafny.Seq
                d_1_letter_ = _dafny.SeqWithoutIsStrInference((rest)[0:1:])
                d_2_count_: int
                out1_: int
                out1_ = default__.CountLetterMethod(original, d_1_letter_)
                d_2_count_ = out1_
                if ((maxCount) > (0)) and ((d_2_count_) == (maxCount)):
                    result = (d_0_tail_).set(d_1_letter_, d_2_count_)
                elif True:
                    result = d_0_tail_
        return result

