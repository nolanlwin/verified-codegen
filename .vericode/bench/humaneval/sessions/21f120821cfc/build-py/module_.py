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
    def SpaceRunSpec(count):
        if (count) == (0):
            return _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, ""))
        elif (count) == (1):
            return _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "_"))
        elif (count) == (2):
            return _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "__"))
        elif True:
            return _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "-"))

    @staticmethod
    def FixSpacesSpec(text, pendingSpaces):
        d_0___accumulator_ = _dafny.SeqWithoutIsStrInference([])
        while True:
            with _dafny.label():
                if (len(text)) == (0):
                    return (d_0___accumulator_) + (default__.SpaceRunSpec(pendingSpaces))
                elif ((text)[0]) == (_dafny.CodePoint(' ')):
                    in0_ = _dafny.SeqWithoutIsStrInference((text)[1::])
                    in1_ = (pendingSpaces) + (1)
                    text = in0_
                    pendingSpaces = in1_
                    raise _dafny.TailCall()
                elif True:
                    d_0___accumulator_ = (d_0___accumulator_) + ((default__.SpaceRunSpec(pendingSpaces)) + (_dafny.SeqWithoutIsStrInference((text)[0:1:])))
                    in2_ = _dafny.SeqWithoutIsStrInference((text)[1::])
                    in3_ = 0
                    text = in2_
                    pendingSpaces = in3_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def fix__spaces(text):
        result: _dafny.Seq = _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, ""))
        out0_: _dafny.Seq
        out0_ = default__.FixSpacesAux(text, 0)
        result = out0_
        return result

    @staticmethod
    def FixSpacesAux(text, pendingSpaces):
        result: _dafny.Seq = _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, ""))
        if (len(text)) == (0):
            result = default__.SpaceRunSpec(pendingSpaces)
        elif ((text)[0]) == (_dafny.CodePoint(' ')):
            out0_: _dafny.Seq
            out0_ = default__.FixSpacesAux(_dafny.SeqWithoutIsStrInference((text)[1::]), (pendingSpaces) + (1))
            result = out0_
        elif True:
            d_0_rest_: _dafny.Seq
            out1_: _dafny.Seq
            out1_ = default__.FixSpacesAux(_dafny.SeqWithoutIsStrInference((text)[1::]), 0)
            d_0_rest_ = out1_
            result = ((default__.SpaceRunSpec(pendingSpaces)) + (_dafny.SeqWithoutIsStrInference((text)[0:1:]))) + (d_0_rest_)
        return result

