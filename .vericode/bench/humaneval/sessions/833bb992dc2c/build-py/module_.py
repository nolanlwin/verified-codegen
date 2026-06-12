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
    def AValueSpec(i):
        return (((i) * (i)) - (i)) + (1)

    @staticmethod
    def CountPairsForISpec(k, i, j):
        d_0___accumulator_ = 0
        while True:
            with _dafny.label():
                if (j) >= (k):
                    return (0) + (d_0___accumulator_)
                elif True:
                    d_0___accumulator_ = (d_0___accumulator_) + ((1 if (_dafny.euclidian_modulus(((default__.AValueSpec(i)) + (default__.AValueSpec(j))) + (default__.AValueSpec(k)), 3)) == (0) else 0))
                    in0_ = k
                    in1_ = i
                    in2_ = (j) + (1)
                    k = in0_
                    i = in1_
                    j = in2_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def CountPairsWithThirdSpec(k, i):
        d_0___accumulator_ = 0
        while True:
            with _dafny.label():
                if (i) >= ((k) - (1)):
                    return (0) + (d_0___accumulator_)
                elif True:
                    d_0___accumulator_ = (d_0___accumulator_) + (default__.CountPairsForISpec(k, i, (i) + (1)))
                    in0_ = k
                    in1_ = (i) + (1)
                    k = in0_
                    i = in1_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def GetMaxTriplesSpec(n):
        d_0___accumulator_ = 0
        while True:
            with _dafny.label():
                if (n) < (3):
                    return (0) + (d_0___accumulator_)
                elif True:
                    d_0___accumulator_ = (default__.CountPairsWithThirdSpec(n, 1)) + (d_0___accumulator_)
                    in0_ = (n) - (1)
                    n = in0_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def get__max__triples(n):
        result: int = int(0)
        if (n) < (3):
            result = 0
        elif True:
            d_0_previous_: int
            out0_: int
            out0_ = default__.get__max__triples((n) - (1))
            d_0_previous_ = out0_
            d_1_added_: int
            out1_: int
            out1_ = default__.CountPairsWithThird(n, 1)
            d_1_added_ = out1_
            result = (d_0_previous_) + (d_1_added_)
        return result

    @staticmethod
    def CountPairsForI(k, i, j):
        result: int = int(0)
        if (j) >= (k):
            result = 0
        elif True:
            d_0_rest_: int
            out0_: int
            out0_ = default__.CountPairsForI(k, i, (j) + (1))
            d_0_rest_ = out0_
            if (_dafny.euclidian_modulus(((default__.AValueSpec(i)) + (default__.AValueSpec(j))) + (default__.AValueSpec(k)), 3)) == (0):
                result = (1) + (d_0_rest_)
            elif True:
                result = d_0_rest_
        return result

    @staticmethod
    def CountPairsWithThird(k, i):
        result: int = int(0)
        if (i) >= ((k) - (1)):
            result = 0
        elif True:
            d_0_first_: int
            out0_: int
            out0_ = default__.CountPairsForI(k, i, (i) + (1))
            d_0_first_ = out0_
            d_1_rest_: int
            out1_: int
            out1_ = default__.CountPairsWithThird(k, (i) + (1))
            d_1_rest_ = out1_
            result = (d_0_first_) + (d_1_rest_)
        return result

