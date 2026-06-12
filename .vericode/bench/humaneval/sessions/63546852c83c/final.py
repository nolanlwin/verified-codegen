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
    def EncryptChar(c):
        if (c) == (_dafny.CodePoint('a')):
            return _dafny.CodePoint('e')
        elif (c) == (_dafny.CodePoint('b')):
            return _dafny.CodePoint('f')
        elif (c) == (_dafny.CodePoint('c')):
            return _dafny.CodePoint('g')
        elif (c) == (_dafny.CodePoint('d')):
            return _dafny.CodePoint('h')
        elif (c) == (_dafny.CodePoint('e')):
            return _dafny.CodePoint('i')
        elif (c) == (_dafny.CodePoint('f')):
            return _dafny.CodePoint('j')
        elif (c) == (_dafny.CodePoint('g')):
            return _dafny.CodePoint('k')
        elif (c) == (_dafny.CodePoint('h')):
            return _dafny.CodePoint('l')
        elif (c) == (_dafny.CodePoint('i')):
            return _dafny.CodePoint('m')
        elif (c) == (_dafny.CodePoint('j')):
            return _dafny.CodePoint('n')
        elif (c) == (_dafny.CodePoint('k')):
            return _dafny.CodePoint('o')
        elif (c) == (_dafny.CodePoint('l')):
            return _dafny.CodePoint('p')
        elif (c) == (_dafny.CodePoint('m')):
            return _dafny.CodePoint('q')
        elif (c) == (_dafny.CodePoint('n')):
            return _dafny.CodePoint('r')
        elif (c) == (_dafny.CodePoint('o')):
            return _dafny.CodePoint('s')
        elif (c) == (_dafny.CodePoint('p')):
            return _dafny.CodePoint('t')
        elif (c) == (_dafny.CodePoint('q')):
            return _dafny.CodePoint('u')
        elif (c) == (_dafny.CodePoint('r')):
            return _dafny.CodePoint('v')
        elif (c) == (_dafny.CodePoint('s')):
            return _dafny.CodePoint('w')
        elif (c) == (_dafny.CodePoint('t')):
            return _dafny.CodePoint('x')
        elif (c) == (_dafny.CodePoint('u')):
            return _dafny.CodePoint('y')
        elif (c) == (_dafny.CodePoint('v')):
            return _dafny.CodePoint('z')
        elif (c) == (_dafny.CodePoint('w')):
            return _dafny.CodePoint('a')
        elif (c) == (_dafny.CodePoint('x')):
            return _dafny.CodePoint('b')
        elif (c) == (_dafny.CodePoint('y')):
            return _dafny.CodePoint('c')
        elif (c) == (_dafny.CodePoint('z')):
            return _dafny.CodePoint('d')
        elif True:
            return c

    @staticmethod
    def EncryptSpec(s):
        d_0___accumulator_ = _dafny.SeqWithoutIsStrInference([])
        while True:
            with _dafny.label():
                if (len(s)) == (0):
                    return (d_0___accumulator_) + (_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "")))
                elif True:
                    d_0___accumulator_ = (d_0___accumulator_) + (_dafny.SeqWithoutIsStrInference([default__.EncryptChar((s)[0])]))
                    in0_ = _dafny.SeqWithoutIsStrInference((s)[1::])
                    s = in0_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def encrypt(s):
        result: _dafny.Seq = _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, ""))
        if (len(s)) == (0):
            result = _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, ""))
        elif True:
            d_0_tail_: _dafny.Seq
            out0_: _dafny.Seq
            out0_ = default__.encrypt(_dafny.SeqWithoutIsStrInference((s)[1::]))
            d_0_tail_ = out0_
            result = (_dafny.SeqWithoutIsStrInference([default__.EncryptChar((s)[0])])) + (d_0_tail_)
        return result

