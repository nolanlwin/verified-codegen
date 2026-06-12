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
    def UpdateNegative(x, current):
        if (x) < (0):
            if (current).is_NoneInt:
                return MaybeInt_SomeInt(x)
            elif (x) > ((current).value):
                return MaybeInt_SomeInt(x)
            elif True:
                return current
        elif True:
            return current

    @staticmethod
    def UpdatePositive(x, current):
        if (x) > (0):
            if (current).is_NoneInt:
                return MaybeInt_SomeInt(x)
            elif (x) < ((current).value):
                return MaybeInt_SomeInt(x)
            elif True:
                return current
        elif True:
            return current

    @staticmethod
    def LargestSmallestIntegersSpec(lst):
        if (len(lst)) == (0):
            return (MaybeInt_NoneInt(), MaybeInt_NoneInt())
        elif True:
            d_0_tail_ = default__.LargestSmallestIntegersSpec(_dafny.SeqWithoutIsStrInference((lst)[1::]))
            return (default__.UpdateNegative((lst)[0], (d_0_tail_)[0]), default__.UpdatePositive((lst)[0], (d_0_tail_)[1]))

    @staticmethod
    def largest__smallest__integers(lst):
        result: tuple = (MaybeInt.default()(), MaybeInt.default()())
        if (len(lst)) == (0):
            result = (MaybeInt_NoneInt(), MaybeInt_NoneInt())
        elif True:
            d_0_tail_: tuple
            out0_: tuple
            out0_ = default__.largest__smallest__integers(_dafny.SeqWithoutIsStrInference((lst)[1::]))
            d_0_tail_ = out0_
            result = (default__.UpdateNegative((lst)[0], (d_0_tail_)[0]), default__.UpdatePositive((lst)[0], (d_0_tail_)[1]))
        return result


class MaybeInt:
    @classmethod
    def default(cls, ):
        return lambda: MaybeInt_NoneInt()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_NoneInt(self) -> bool:
        return isinstance(self, MaybeInt_NoneInt)
    @property
    def is_SomeInt(self) -> bool:
        return isinstance(self, MaybeInt_SomeInt)

class MaybeInt_NoneInt(MaybeInt, NamedTuple('NoneInt', [])):
    def __dafnystr__(self) -> str:
        return f'MaybeInt.NoneInt'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, MaybeInt_NoneInt)
    def __hash__(self) -> int:
        return super().__hash__()

class MaybeInt_SomeInt(MaybeInt, NamedTuple('SomeInt', [('value', Any)])):
    def __dafnystr__(self) -> str:
        return f'MaybeInt.SomeInt({_dafny.string_of(self.value)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, MaybeInt_SomeInt) and self.value == __o.value
    def __hash__(self) -> int:
        return super().__hash__()

