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
    def ContainsValue(s, x):
        if (len(s)) == (0):
            return False
        elif True:
            return (((s)[0]) == (x)) or (default__.ContainsValue(_dafny.SeqWithoutIsStrInference((s)[1::]), x))

    @staticmethod
    def PairsSumToZeroSpec(l):
        if (len(l)) < (2):
            return False
        elif True:
            return (default__.ContainsValue(_dafny.SeqWithoutIsStrInference((l)[1::]), (0) - ((l)[0]))) or (default__.PairsSumToZeroSpec(_dafny.SeqWithoutIsStrInference((l)[1::])))

    @staticmethod
    def pairs__sum__to__zero(l):
        while True:
            with _dafny.label():
                result: bool = False
                if (len(l)) < (2):
                    result = False
                elif True:
                    if default__.ContainsValue(_dafny.SeqWithoutIsStrInference((l)[1::]), (0) - ((l)[0])):
                        result = True
                    elif True:
                        in0_ = _dafny.SeqWithoutIsStrInference((l)[1::])
                        l = in0_
                        raise _dafny.TailCall()
                return result
                break

