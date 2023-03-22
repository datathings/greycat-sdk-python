from __future__ import annotations
from typing import *

from ai.greycat.greycat import GreyCat

T = TypeVar('T')


class std_n:
    class core:
        class nodeTimeCursor(GreyCat.Object):
            def __init__(self: std_n.core.nodeTimeCursor, type: GreyCat.Type) -> None:
                super(type, None)
                raise NotImplementedError

            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat.Stream) -> object:
                raise NotImplementedError

        class Array(Generic[T], GreyCat.Object):
            def __init__(self: std_n.core.Array[T], type: GreyCat.Type) -> None:
                super(type, None)

            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat.Stream) -> object:
                size = stream.read_i32().value
                array: std_n.core.Array[object] = type.factory(type)
                array = [None] * size
                for offset in range(size):
                    array.set(offset, stream.read())
                return array
            
        class Date(GreyCat.Object):
            def __init__(self: std_n.core.Date, type: GreyCat.Type) -> None:
                super(type, None)
