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
    def LowerAscii(c):
        if (c) == ((_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "A")))[0]):
            return (_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "a")))[0]
        elif (c) == ((_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "B")))[0]):
            return (_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "b")))[0]
        elif (c) == ((_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "C")))[0]):
            return (_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "c")))[0]
        elif (c) == ((_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "D")))[0]):
            return (_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "d")))[0]
        elif (c) == ((_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "E")))[0]):
            return (_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "e")))[0]
        elif (c) == ((_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "F")))[0]):
            return (_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "f")))[0]
        elif (c) == ((_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "G")))[0]):
            return (_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "g")))[0]
        elif (c) == ((_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "H")))[0]):
            return (_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "h")))[0]
        elif (c) == ((_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "I")))[0]):
            return (_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "i")))[0]
        elif (c) == ((_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "J")))[0]):
            return (_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "j")))[0]
        elif (c) == ((_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "K")))[0]):
            return (_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "k")))[0]
        elif (c) == ((_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "L")))[0]):
            return (_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "l")))[0]
        elif (c) == ((_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "M")))[0]):
            return (_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "m")))[0]
        elif (c) == ((_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "N")))[0]):
            return (_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "n")))[0]
        elif (c) == ((_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "O")))[0]):
            return (_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "o")))[0]
        elif (c) == ((_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "P")))[0]):
            return (_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "p")))[0]
        elif (c) == ((_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "Q")))[0]):
            return (_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "q")))[0]
        elif (c) == ((_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "R")))[0]):
            return (_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "r")))[0]
        elif (c) == ((_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "S")))[0]):
            return (_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "s")))[0]
        elif (c) == ((_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "T")))[0]):
            return (_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "t")))[0]
        elif (c) == ((_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "U")))[0]):
            return (_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "u")))[0]
        elif (c) == ((_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "V")))[0]):
            return (_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "v")))[0]
        elif (c) == ((_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "W")))[0]):
            return (_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "w")))[0]
        elif (c) == ((_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "X")))[0]):
            return (_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "x")))[0]
        elif (c) == ((_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "Y")))[0]):
            return (_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "y")))[0]
        elif (c) == ((_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "Z")))[0]):
            return (_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "z")))[0]
        elif True:
            return c

    @staticmethod
    def SameCharacterIgnoringCase(a, b):
        return (default__.LowerAscii(a)) == (default__.LowerAscii(b))

    @staticmethod
    def ContainsEquivalentCharacter(s, c):
        if (len(s)) == (0):
            return False
        elif True:
            return (default__.SameCharacterIgnoringCase((s)[0], c)) or (default__.ContainsEquivalentCharacter(_dafny.SeqWithoutIsStrInference((s)[1::]), c))

    @staticmethod
    def CountDistinctCharactersSpec(s):
        d_0___accumulator_ = 0
        while True:
            with _dafny.label():
                if (len(s)) == (0):
                    return (0) + (d_0___accumulator_)
                elif True:
                    d_0___accumulator_ = (d_0___accumulator_) + ((0 if default__.ContainsEquivalentCharacter(_dafny.SeqWithoutIsStrInference((s)[1::]), (s)[0]) else 1))
                    in0_ = _dafny.SeqWithoutIsStrInference((s)[1::])
                    s = in0_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def count__distinct__characters(s):
        result: int = int(0)
        if (len(s)) == (0):
            result = 0
        elif True:
            d_0_tailResult_: int
            out0_: int
            out0_ = default__.count__distinct__characters(_dafny.SeqWithoutIsStrInference((s)[1::]))
            d_0_tailResult_ = out0_
            if default__.ContainsEquivalentCharacter(_dafny.SeqWithoutIsStrInference((s)[1::]), (s)[0]):
                result = d_0_tailResult_
            elif True:
                result = (1) + (d_0_tailResult_)
        return result

