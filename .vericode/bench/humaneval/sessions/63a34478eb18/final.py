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
    def AllNonNegativeSpec(lst):
        if (len(lst)) == (0):
            return True
        elif True:
            return (((lst)[0]) >= (0)) and (default__.AllNonNegativeSpec(_dafny.SeqWithoutIsStrInference((lst)[1::])))

    @staticmethod
    def IsSortedSpec(lst):
        while True:
            with _dafny.label():
                if (len(lst)) <= (1):
                    return True
                elif ((lst)[0]) > ((lst)[1]):
                    return False
                elif ((len(lst)) >= (3)) and (((lst)[0]) == ((lst)[2])):
                    return False
                elif True:
                    in0_ = _dafny.SeqWithoutIsStrInference((lst)[1::])
                    lst = in0_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def is__sorted(lst):
        while True:
            with _dafny.label():
                result: bool = False
                if (len(lst)) <= (1):
                    result = True
                elif ((lst)[0]) > ((lst)[1]):
                    result = False
                elif ((len(lst)) >= (3)) and (((lst)[0]) == ((lst)[2])):
                    result = False
                elif True:
                    in0_ = _dafny.SeqWithoutIsStrInference((lst)[1::])
                    lst = in0_
                    raise _dafny.TailCall()
                return result
                break

