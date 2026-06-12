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
    def AllTriplesDistinct(s, i):
        if ((i) + (2)) >= (len(s)):
            return True
        elif True:
            return (((((s)[i]) != ((s)[(i) + (1)])) and (((s)[i]) != ((s)[(i) + (2)]))) and (((s)[(i) + (1)]) != ((s)[(i) + (2)]))) and (default__.AllTriplesDistinct(s, (i) + (1)))

    @staticmethod
    def IsHappySpec(s):
        if (len(s)) < (3):
            return False
        elif True:
            return default__.AllTriplesDistinct(s, 0)

    @staticmethod
    def is__happy(s):
        result: bool = False
        if (len(s)) < (3):
            result = False
        elif True:
            out0_: bool
            out0_ = default__.CheckAllTriplesDistinct(s, 0)
            result = out0_
        return result

    @staticmethod
    def CheckAllTriplesDistinct(s, i):
        result: bool = False
        if ((i) + (2)) >= (len(s)):
            result = True
        elif True:
            d_0_tail_: bool
            out0_: bool
            out0_ = default__.CheckAllTriplesDistinct(s, (i) + (1))
            d_0_tail_ = out0_
            result = (((((s)[i]) != ((s)[(i) + (1)])) and (((s)[i]) != ((s)[(i) + (2)]))) and (((s)[(i) + (1)]) != ((s)[(i) + (2)]))) and (d_0_tail_)
        return result

