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
    def TruncateNumberSpec(number):
        while True:
            with _dafny.label():
                if (number) < (_dafny.BigRational('1e0')):
                    return number
                elif True:
                    in0_ = (number) - (_dafny.BigRational('1e0'))
                    number = in0_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def truncate__number(number):
        while True:
            with _dafny.label():
                result: _dafny.BigRational = _dafny.BigRational()
                if (number) < (_dafny.BigRational('1e0')):
                    result = number
                elif True:
                    in0_ = (number) - (_dafny.BigRational('1e0'))
                    number = in0_
                    raise _dafny.TailCall()
                return result
                break

