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
    def SignSpec(x):
        if (x) > (0):
            return 1
        elif (x) < (0):
            return -1
        elif True:
            return 0

    @staticmethod
    def ProdSignsAux(arr, sumMag, prodSign):
        while True:
            with _dafny.label():
                if (len(arr)) == (0):
                    return OptionInt_Some((sumMag) * (prodSign))
                elif True:
                    in0_ = _dafny.SeqWithoutIsStrInference((arr)[1::])
                    in1_ = (sumMag) + (((0) - ((arr)[0]) if ((arr)[0]) < (0) else (arr)[0]))
                    in2_ = (prodSign) * (default__.SignSpec((arr)[0]))
                    arr = in0_
                    sumMag = in1_
                    prodSign = in2_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def ProdSignsSpec(arr):
        if (len(arr)) == (0):
            return OptionInt_None()
        elif True:
            return default__.ProdSignsAux(arr, 0, 1)

    @staticmethod
    def prod__signs(arr):
        result: OptionInt = OptionInt.default()()
        if (len(arr)) == (0):
            result = OptionInt_None()
        elif True:
            out0_: OptionInt
            out0_ = default__.ProdSignsAuxMethod(arr, 0, 1)
            result = out0_
        return result

    @staticmethod
    def ProdSignsAuxMethod(arr, sumMag, prodSign):
        while True:
            with _dafny.label():
                result: OptionInt = OptionInt.default()()
                if (len(arr)) == (0):
                    result = OptionInt_Some((sumMag) * (prodSign))
                elif True:
                    in0_ = _dafny.SeqWithoutIsStrInference((arr)[1::])
                    in1_ = (sumMag) + (((0) - ((arr)[0]) if ((arr)[0]) < (0) else (arr)[0]))
                    in2_ = (prodSign) * (default__.SignSpec((arr)[0]))
                    arr = in0_
                    sumMag = in1_
                    prodSign = in2_
                    raise _dafny.TailCall()
                return result
                break


class OptionInt:
    @classmethod
    def default(cls, ):
        return lambda: OptionInt_None()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_None(self) -> bool:
        return isinstance(self, OptionInt_None)
    @property
    def is_Some(self) -> bool:
        return isinstance(self, OptionInt_Some)

class OptionInt_None(OptionInt, NamedTuple('None_', [])):
    def __dafnystr__(self) -> str:
        return f'OptionInt.None'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, OptionInt_None)
    def __hash__(self) -> int:
        return super().__hash__()

class OptionInt_Some(OptionInt, NamedTuple('Some', [('value', Any)])):
    def __dafnystr__(self) -> str:
        return f'OptionInt.Some({_dafny.string_of(self.value)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, OptionInt_Some) and self.value == __o.value
    def __hash__(self) -> int:
        return super().__hash__()

