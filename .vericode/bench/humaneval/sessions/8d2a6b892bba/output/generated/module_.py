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
    def BelowZeroSpec(operations, balance):
        while True:
            with _dafny.label():
                if (len(operations)) == (0):
                    return False
                elif ((balance) + ((operations)[0])) < (0):
                    return True
                elif True:
                    in0_ = _dafny.SeqWithoutIsStrInference((operations)[1::])
                    in1_ = (balance) + ((operations)[0])
                    operations = in0_
                    balance = in1_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def below__zero(operations):
        result: bool = False
        out0_: bool
        out0_ = default__.BelowZeroHelper(operations, 0)
        result = out0_
        return result

    @staticmethod
    def BelowZeroHelper(operations, balance):
        while True:
            with _dafny.label():
                result: bool = False
                if (len(operations)) == (0):
                    result = False
                elif ((balance) + ((operations)[0])) < (0):
                    result = True
                elif True:
                    in0_ = _dafny.SeqWithoutIsStrInference((operations)[1::])
                    in1_ = (balance) + ((operations)[0])
                    operations = in0_
                    balance = in1_
                    raise _dafny.TailCall()
                return result
                break

