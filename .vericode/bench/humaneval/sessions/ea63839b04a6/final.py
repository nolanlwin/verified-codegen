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
    def OnlySquareBrackets(s):
        if (len(s)) == (0):
            return True
        elif True:
            return ((((s)[0]) == (_dafny.CodePoint('['))) or (((s)[0]) == (_dafny.CodePoint(']')))) and (default__.OnlySquareBrackets(_dafny.SeqWithoutIsStrInference((s)[1::])))

    @staticmethod
    def IsNestedAux(s, matched):
        while True:
            with _dafny.label():
                if (matched) == (4):
                    return True
                elif (len(s)) == (0):
                    return False
                elif ((matched) == (0)) or ((matched) == (1)):
                    if ((s)[0]) == (_dafny.CodePoint('[')):
                        in0_ = _dafny.SeqWithoutIsStrInference((s)[1::])
                        in1_ = (matched) + (1)
                        s = in0_
                        matched = in1_
                        raise _dafny.TailCall()
                    elif True:
                        in2_ = _dafny.SeqWithoutIsStrInference((s)[1::])
                        in3_ = matched
                        s = in2_
                        matched = in3_
                        raise _dafny.TailCall()
                elif ((s)[0]) == (_dafny.CodePoint(']')):
                    in4_ = _dafny.SeqWithoutIsStrInference((s)[1::])
                    in5_ = (matched) + (1)
                    s = in4_
                    matched = in5_
                    raise _dafny.TailCall()
                elif True:
                    in6_ = _dafny.SeqWithoutIsStrInference((s)[1::])
                    in7_ = matched
                    s = in6_
                    matched = in7_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def IsNestedSpec(s):
        return default__.IsNestedAux(s, 0)

    @staticmethod
    def is__nested(s):
        result: bool = False
        out0_: bool
        out0_ = default__.IsNestedAuxMethod(s, 0)
        result = out0_
        return result

    @staticmethod
    def IsNestedAuxMethod(s, matched):
        while True:
            with _dafny.label():
                result: bool = False
                if (matched) == (4):
                    result = True
                elif (len(s)) == (0):
                    result = False
                elif ((matched) == (0)) or ((matched) == (1)):
                    if ((s)[0]) == (_dafny.CodePoint('[')):
                        in0_ = _dafny.SeqWithoutIsStrInference((s)[1::])
                        in1_ = (matched) + (1)
                        s = in0_
                        matched = in1_
                        raise _dafny.TailCall()
                    elif True:
                        in2_ = _dafny.SeqWithoutIsStrInference((s)[1::])
                        in3_ = matched
                        s = in2_
                        matched = in3_
                        raise _dafny.TailCall()
                elif True:
                    if ((s)[0]) == (_dafny.CodePoint(']')):
                        in4_ = _dafny.SeqWithoutIsStrInference((s)[1::])
                        in5_ = (matched) + (1)
                        s = in4_
                        matched = in5_
                        raise _dafny.TailCall()
                    elif True:
                        in6_ = _dafny.SeqWithoutIsStrInference((s)[1::])
                        in7_ = matched
                        s = in6_
                        matched = in7_
                        raise _dafny.TailCall()
                return result
                break

