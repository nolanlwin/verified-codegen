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
    def IsVowel(c):
        return ((((((((((c) == (_dafny.CodePoint('a'))) or ((c) == (_dafny.CodePoint('e')))) or ((c) == (_dafny.CodePoint('i')))) or ((c) == (_dafny.CodePoint('o')))) or ((c) == (_dafny.CodePoint('u')))) or ((c) == (_dafny.CodePoint('A')))) or ((c) == (_dafny.CodePoint('E')))) or ((c) == (_dafny.CodePoint('I')))) or ((c) == (_dafny.CodePoint('O')))) or ((c) == (_dafny.CodePoint('U')))

    @staticmethod
    def IsConsonant(c):
        return not(default__.IsVowel(c))

    @staticmethod
    def GetClosestVowelAux(word, i):
        while True:
            with _dafny.label():
                if ((i) <= (0)) or ((i) >= ((len(word)) - (1))):
                    return _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, ""))
                elif ((default__.IsVowel((word)[i])) and (default__.IsConsonant((word)[(i) - (1)]))) and (default__.IsConsonant((word)[(i) + (1)])):
                    return _dafny.SeqWithoutIsStrInference((word)[i:(i) + (1):])
                elif True:
                    in0_ = word
                    in1_ = (i) - (1)
                    word = in0_
                    i = in1_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def GetClosestVowelSpec(word):
        if (len(word)) < (3):
            return _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, ""))
        elif True:
            return default__.GetClosestVowelAux(word, (len(word)) - (2))

    @staticmethod
    def get__closest__vowel(word):
        result: _dafny.Seq = _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, ""))
        if (len(word)) < (3):
            result = _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, ""))
        elif True:
            out0_: _dafny.Seq
            out0_ = default__.GetClosestVowelAuxMethod(word, (len(word)) - (2))
            result = out0_
        return result

    @staticmethod
    def GetClosestVowelAuxMethod(word, i):
        while True:
            with _dafny.label():
                res: _dafny.Seq = _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, ""))
                if ((i) <= (0)) or ((i) >= ((len(word)) - (1))):
                    res = _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, ""))
                elif ((default__.IsVowel((word)[i])) and (default__.IsConsonant((word)[(i) - (1)]))) and (default__.IsConsonant((word)[(i) + (1)])):
                    res = _dafny.SeqWithoutIsStrInference((word)[i:(i) + (1):])
                elif True:
                    in0_ = word
                    in1_ = (i) - (1)
                    word = in0_
                    i = in1_
                    raise _dafny.TailCall()
                return res
                break

