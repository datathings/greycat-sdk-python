from __future__ import annotations
from ctypes import *
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
            localizedEpochS: c_int64
            epochUs: c_int64
            timeZone: c_int32

            def __init__(self: std_n.core.Date, type: GreyCat.Type) -> None:
                super(type, None)

            def save(self: std_n.core.Date, stream: GreyCat.Stream) -> None:
                stream.write_i8(GreyCat.PrimitiveType.OBJECT)
                stream.write_i32(self.type.offset)
                stream.write_i64(self.localizedEpochS)
                stream.write_i64(self.epochUs)
                stream.write_i32(self.timeZone)

            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat.Stream) -> object:
                res: std_n.core.Date = type.factory(type)
                res.localizedEpochS = stream.read_i64()
                res.epochUs = stream.read_i64()
                res.timeZone = stream.read_i32()
                return res

        class duration(GreyCat.Object):
            value: c_int64

            def __init__(self: std_n.core.duration, type: GreyCat.Type) -> None:
                super(type, None)

            def save(self: std_n.core.duration, stream: GreyCat.Stream) -> None:
                stream.write_i8(GreyCat.PrimitiveType.DURATION)
                stream.write_i64(self.value)

            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat.Stream) -> object:
                res: std_n.core.duration = type.factory(type)
                res.value = stream.read_i64()
                return res

        class Error(GreyCat.Object):
            code: c_int32
            frames: list[std_n.core.Error.Frame]
            msg: str
            value: object

            def __init__(self: std_n.core.Error, type: GreyCat.Type):
                super(type, None)

            def save(self: std_n.core.Error, stream: GreyCat.Stream) -> None:
                stream.write_i8(GreyCat.PrimitiveType.OBJECT)
                stream.write_i32(self.type.offset)
                stream.write_i32(self.code)
                stream.write_i32(c_int32(len(self.frames)))
                msg_bytes = self.msg.encode('utf-8')
                stream.write_i32(c_int32(len(msg_bytes)))
                for offset in range(len(self.frames)):
                    frame: std_n.core.Error.Frame = self.frames[offset]
                    stream.write_i32(frame.modSymbol)
                    stream.write_i32(frame.typeSymbol)
                    stream.write_i32(frame.fnSymbol)
                    stream.write_i32(frame.line)
                    stream.write_i32(frame.column)
                stream.write_i8_array(msg_bytes, 0, len(msg_bytes))
                stream.write_object(self.value)

            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat.Stream)->object:
                code: c_int32 = stream.read_i32()
                framesLen: c_int32 = stream.read_i32()
                msgLen: c_int32 = stream.read_i32()
                frames: list[std_n.core.Error.Frame] = [None] * framesLen
                for offset in range(framesLen):
                    modSymbol: c_int32 = stream.read_i32()
                    typeSymbol: c_int32 = stream.read_i32()
                    fnSymbol: c_int32 = stream.read_i32()
                    line: c_int32 = stream.read_i32()
                    column: c_int32 = stream.read_i32()
                    frames[offset] = std_n.core.Error.Frame(modSymbol, typeSymbol, fnSymbol, line, column)
                res: std_n.core.Error = type.factory(type)
                res.code = code
                res.frames = frames
                res.msg = stream.read_string(msgLen)
                res.value = stream.read()
                return res

            class Frame:
                modSymbol: c_int32
                typeSymbol: c_int32
                fnSymbol: c_int32
                line: c_int32
                column: c_int32

                def __init__(self: std_n.core.Error.Frame, modSymbol: c_int32, typeSymbol: c_int32, fnSymbol: c_int32, line: c_int32, column: c_int32) -> None:
                    self.modSymbol = modSymbol
                    self.typeSymbol = typeSymbol
                    self.fnSymbol = fnSymbol
                    self.line = line
                    self.column = column
