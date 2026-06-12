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
    def FilterIntegersSpec(values):
        d_0___accumulator_ = _dafny.SeqWithoutIsStrInference([])
        while True:
            with _dafny.label():
                if (len(values)) == (0):
                    return (d_0___accumulator_) + (_dafny.SeqWithoutIsStrInference([]))
                elif ((values)[0]).is_PyInt:
                    d_0___accumulator_ = (d_0___accumulator_) + (_dafny.SeqWithoutIsStrInference([((values)[0]).i]))
                    in0_ = _dafny.SeqWithoutIsStrInference((values)[1::])
                    values = in0_
                    raise _dafny.TailCall()
                elif True:
                    in1_ = _dafny.SeqWithoutIsStrInference((values)[1::])
                    values = in1_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def filter__integers(values):
        result: _dafny.Seq = _dafny.Seq({})
        if (len(values)) == (0):
            result = _dafny.SeqWithoutIsStrInference([])
        elif True:
            d_0_tail_: _dafny.Seq
            out0_: _dafny.Seq
            out0_ = default__.filter__integers(_dafny.SeqWithoutIsStrInference((values)[1::]))
            d_0_tail_ = out0_
            if ((values)[0]).is_PyInt:
                result = (_dafny.SeqWithoutIsStrInference([((values)[0]).i])) + (d_0_tail_)
            elif True:
                result = d_0_tail_
        return result


class PyValue:
    @classmethod
    def default(cls, ):
        return lambda: PyValue_PyInt(int(0))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_PyInt(self) -> bool:
        return isinstance(self, PyValue_PyInt)
    @property
    def is_PyOther(self) -> bool:
        return isinstance(self, PyValue_PyOther)

class PyValue_PyInt(PyValue, NamedTuple('PyInt', [('i', Any)])):
    def __dafnystr__(self) -> str:
        return f'PyValue.PyInt({_dafny.string_of(self.i)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, PyValue_PyInt) and self.i == __o.i
    def __hash__(self) -> int:
        return super().__hash__()

class PyValue_PyOther(PyValue, NamedTuple('PyOther', [])):
    def __dafnystr__(self) -> str:
        return f'PyValue.PyOther'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, PyValue_PyOther)
    def __hash__(self) -> int:
        return super().__hash__()

