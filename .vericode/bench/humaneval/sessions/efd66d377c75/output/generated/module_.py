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
    def TotalChars(lst):
        d_0___accumulator_ = 0
        while True:
            with _dafny.label():
                if (len(lst)) == (0):
                    return (0) + (d_0___accumulator_)
                elif True:
                    d_0___accumulator_ = (d_0___accumulator_) + (len((lst)[0]))
                    in0_ = _dafny.SeqWithoutIsStrInference((lst)[1::])
                    lst = in0_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def TotalMatchSpec(lst1, lst2):
        if (default__.TotalChars(lst1)) <= (default__.TotalChars(lst2)):
            return lst1
        elif True:
            return lst2

    @staticmethod
    def total__match(lst1, lst2):
        result: _dafny.Seq = _dafny.Seq({})
        if (default__.TotalChars(lst1)) <= (default__.TotalChars(lst2)):
            result = lst1
        elif True:
            result = lst2
        return result

