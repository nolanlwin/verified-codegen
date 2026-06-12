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
    def LongestSpec(strings):
        if (len(strings)) == (0):
            return OptionalString_NoneString()
        elif True:
            d_0_tail_ = default__.LongestSpec(_dafny.SeqWithoutIsStrInference((strings)[1::]))
            if (d_0_tail_).is_NoneString:
                return OptionalString_SomeString((strings)[0])
            elif (len((strings)[0])) >= (len((d_0_tail_).value)):
                return OptionalString_SomeString((strings)[0])
            elif True:
                return d_0_tail_

    @staticmethod
    def longest(strings):
        result: OptionalString = OptionalString.default()()
        if (len(strings)) == (0):
            result = OptionalString_NoneString()
        elif True:
            d_0_tail_: OptionalString
            out0_: OptionalString
            out0_ = default__.longest(_dafny.SeqWithoutIsStrInference((strings)[1::]))
            d_0_tail_ = out0_
            if (d_0_tail_).is_NoneString:
                result = OptionalString_SomeString((strings)[0])
            elif (len((strings)[0])) >= (len((d_0_tail_).value)):
                result = OptionalString_SomeString((strings)[0])
            elif True:
                result = d_0_tail_
        return result


class OptionalString:
    @classmethod
    def default(cls, ):
        return lambda: OptionalString_NoneString()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_NoneString(self) -> bool:
        return isinstance(self, OptionalString_NoneString)
    @property
    def is_SomeString(self) -> bool:
        return isinstance(self, OptionalString_SomeString)

class OptionalString_NoneString(OptionalString, NamedTuple('NoneString', [])):
    def __dafnystr__(self) -> str:
        return f'OptionalString.NoneString'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, OptionalString_NoneString)
    def __hash__(self) -> int:
        return super().__hash__()

class OptionalString_SomeString(OptionalString, NamedTuple('SomeString', [('value', Any)])):
    def __dafnystr__(self) -> str:
        return f'OptionalString.SomeString({self.value.VerbatimString(True)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, OptionalString_SomeString) and self.value == __o.value
    def __hash__(self) -> int:
        return super().__hash__()

