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
    def SeparateParenGroupsAux(s, i, depth, current, groups):
        while True:
            with _dafny.label():
                if (i) == (len(s)):
                    return groups
                elif ((s)[i]) == (_dafny.CodePoint(' ')):
                    in0_ = s
                    in1_ = (i) + (1)
                    in2_ = depth
                    in3_ = current
                    in4_ = groups
                    s = in0_
                    i = in1_
                    depth = in2_
                    current = in3_
                    groups = in4_
                    raise _dafny.TailCall()
                elif ((s)[i]) == (_dafny.CodePoint('(')):
                    d_0_nextCurrent_ = (_dafny.SeqWithoutIsStrInference([_dafny.CodePoint('(')]) if (depth) == (0) else (current) + (_dafny.SeqWithoutIsStrInference([_dafny.CodePoint('(')])))
                    in5_ = s
                    in6_ = (i) + (1)
                    in7_ = (depth) + (1)
                    in8_ = d_0_nextCurrent_
                    in9_ = groups
                    s = in5_
                    i = in6_
                    depth = in7_
                    current = in8_
                    groups = in9_
                    raise _dafny.TailCall()
                elif ((s)[i]) == (_dafny.CodePoint(')')):
                    if (depth) == (1):
                        in10_ = s
                        in11_ = (i) + (1)
                        in12_ = 0
                        in13_ = _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, ""))
                        in14_ = (groups) + (_dafny.SeqWithoutIsStrInference([(current) + (_dafny.SeqWithoutIsStrInference([_dafny.CodePoint(')')]))]))
                        s = in10_
                        i = in11_
                        depth = in12_
                        current = in13_
                        groups = in14_
                        raise _dafny.TailCall()
                    elif (depth) > (1):
                        in15_ = s
                        in16_ = (i) + (1)
                        in17_ = (depth) - (1)
                        in18_ = (current) + (_dafny.SeqWithoutIsStrInference([_dafny.CodePoint(')')]))
                        in19_ = groups
                        s = in15_
                        i = in16_
                        depth = in17_
                        current = in18_
                        groups = in19_
                        raise _dafny.TailCall()
                    elif True:
                        in20_ = s
                        in21_ = (i) + (1)
                        in22_ = depth
                        in23_ = current
                        in24_ = groups
                        s = in20_
                        i = in21_
                        depth = in22_
                        current = in23_
                        groups = in24_
                        raise _dafny.TailCall()
                elif True:
                    in25_ = s
                    in26_ = (i) + (1)
                    in27_ = depth
                    in28_ = current
                    in29_ = groups
                    s = in25_
                    i = in26_
                    depth = in27_
                    current = in28_
                    groups = in29_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def SeparateParenGroupsSpec(paren__string):
        return default__.SeparateParenGroupsAux(paren__string, 0, 0, _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "")), _dafny.SeqWithoutIsStrInference([]))

    @staticmethod
    def separate__paren__groups(paren__string):
        result: _dafny.Seq = _dafny.Seq({})
        out0_: _dafny.Seq
        out0_ = default__.SeparateParenGroupsAuxMethod(paren__string, 0, 0, _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "")), _dafny.SeqWithoutIsStrInference([]))
        result = out0_
        return result

    @staticmethod
    def SeparateParenGroupsAuxMethod(s, i, depth, current, groups):
        while True:
            with _dafny.label():
                result: _dafny.Seq = _dafny.Seq({})
                if (i) == (len(s)):
                    result = groups
                elif ((s)[i]) == (_dafny.CodePoint(' ')):
                    in0_ = s
                    in1_ = (i) + (1)
                    in2_ = depth
                    in3_ = current
                    in4_ = groups
                    s = in0_
                    i = in1_
                    depth = in2_
                    current = in3_
                    groups = in4_
                    raise _dafny.TailCall()
                elif ((s)[i]) == (_dafny.CodePoint('(')):
                    d_0_nextCurrent_: _dafny.Seq
                    if (depth) == (0):
                        d_0_nextCurrent_ = _dafny.SeqWithoutIsStrInference([_dafny.CodePoint('(')])
                    elif True:
                        d_0_nextCurrent_ = (current) + (_dafny.SeqWithoutIsStrInference([_dafny.CodePoint('(')]))
                    in5_ = s
                    in6_ = (i) + (1)
                    in7_ = (depth) + (1)
                    in8_ = d_0_nextCurrent_
                    in9_ = groups
                    s = in5_
                    i = in6_
                    depth = in7_
                    current = in8_
                    groups = in9_
                    raise _dafny.TailCall()
                elif ((s)[i]) == (_dafny.CodePoint(')')):
                    if (depth) == (1):
                        in10_ = s
                        in11_ = (i) + (1)
                        in12_ = 0
                        in13_ = _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, ""))
                        in14_ = (groups) + (_dafny.SeqWithoutIsStrInference([(current) + (_dafny.SeqWithoutIsStrInference([_dafny.CodePoint(')')]))]))
                        s = in10_
                        i = in11_
                        depth = in12_
                        current = in13_
                        groups = in14_
                        raise _dafny.TailCall()
                    elif (depth) > (1):
                        in15_ = s
                        in16_ = (i) + (1)
                        in17_ = (depth) - (1)
                        in18_ = (current) + (_dafny.SeqWithoutIsStrInference([_dafny.CodePoint(')')]))
                        in19_ = groups
                        s = in15_
                        i = in16_
                        depth = in17_
                        current = in18_
                        groups = in19_
                        raise _dafny.TailCall()
                    elif True:
                        in20_ = s
                        in21_ = (i) + (1)
                        in22_ = depth
                        in23_ = current
                        in24_ = groups
                        s = in20_
                        i = in21_
                        depth = in22_
                        current = in23_
                        groups = in24_
                        raise _dafny.TailCall()
                elif True:
                    in25_ = s
                    in26_ = (i) + (1)
                    in27_ = depth
                    in28_ = current
                    in29_ = groups
                    s = in25_
                    i = in26_
                    depth = in27_
                    current = in28_
                    groups = in29_
                    raise _dafny.TailCall()
                return result
                break

