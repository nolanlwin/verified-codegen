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
    def IsPalindromeSpec(text):
        if (len(text)) <= (1):
            return True
        elif True:
            return (((text)[0]) == ((text)[(len(text)) - (1)])) and (default__.IsPalindromeSpec(_dafny.SeqWithoutIsStrInference((text)[1:(len(text)) - (1):])))

    @staticmethod
    def is__palindrome(text):
        while True:
            with _dafny.label():
                result: bool = False
                if (len(text)) <= (1):
                    result = True
                elif ((text)[0]) != ((text)[(len(text)) - (1)]):
                    result = False
                elif True:
                    in0_ = _dafny.SeqWithoutIsStrInference((text)[1:(len(text)) - (1):])
                    text = in0_
                    raise _dafny.TailCall()
                return result
                break

