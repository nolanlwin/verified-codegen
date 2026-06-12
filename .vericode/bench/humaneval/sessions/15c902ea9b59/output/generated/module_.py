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
    def IsAsciiLetter(c):
        return (((_dafny.CodePoint('a')) <= (c)) and ((c) <= (_dafny.CodePoint('z')))) or (((_dafny.CodePoint('A')) <= (c)) and ((c) <= (_dafny.CodePoint('Z'))))

    @staticmethod
    def CheckIfLastCharIsALetterSpec(txt):
        while True:
            with _dafny.label():
                if (len(txt)) == (0):
                    return False
                elif (len(txt)) == (1):
                    return default__.IsAsciiLetter((txt)[0])
                elif (len(txt)) == (2):
                    return (default__.IsAsciiLetter((txt)[1])) and (((txt)[0]) == (_dafny.CodePoint(' ')))
                elif True:
                    in0_ = _dafny.SeqWithoutIsStrInference((txt)[1::])
                    txt = in0_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def check__if__last__char__is__a__letter(txt):
        while True:
            with _dafny.label():
                result: bool = False
                if (len(txt)) == (0):
                    result = False
                elif (len(txt)) == (1):
                    result = default__.IsAsciiLetter((txt)[0])
                elif (len(txt)) == (2):
                    result = (default__.IsAsciiLetter((txt)[1])) and (((txt)[0]) == (_dafny.CodePoint(' ')))
                elif True:
                    in0_ = _dafny.SeqWithoutIsStrInference((txt)[1::])
                    txt = in0_
                    raise _dafny.TailCall()
                return result
                break

