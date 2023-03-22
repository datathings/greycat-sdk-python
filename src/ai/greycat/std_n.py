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

            def __init__(self: std_n.core.Date, type: GreyCat.Type) -> None:
                super(type, None)
                self.localizedEpochS: c_int64
                self.epochUs: c_int64
                self.timeZone: c_int32

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
            def __init__(self: std_n.core.duration, type: GreyCat.Type) -> None:
                super(type, None)
                self.value: c_int64

            def save(self: std_n.core.duration, stream: GreyCat.Stream) -> None:
                stream.write_i8(GreyCat.PrimitiveType.DURATION)
                stream.write_i64(self.value)

            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat.Stream) -> object:
                res: std_n.core.duration = type.factory(type)
                res.value = stream.read_i64()
                return res

        class Error(GreyCat.Object):
            def __init__(self: std_n.core.Error, type: GreyCat.Type):
                super(type, None)
                self.code: c_int32
                self.frames: list[std_n.core.Error.Frame]
                self.msg: str
                self.value: object

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
            def load(type: GreyCat.Type, stream: GreyCat.Stream) -> object:
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
                    frames[offset] = std_n.core.Error.Frame(
                        modSymbol, typeSymbol, fnSymbol, line, column)
                res: std_n.core.Error = type.factory(type)
                res.code = code
                res.frames = frames
                res.msg = stream.read_string(msgLen)
                res.value = stream.read()
                return res

            class Frame:
                def __init__(self: std_n.core.Error.Frame, modSymbol: c_int32, typeSymbol: c_int32, fnSymbol: c_int32, line: c_int32, column: c_int32) -> None:
                    self.modSymbol = modSymbol
                    self.typeSymbol = typeSymbol
                    self.fnSymbol = fnSymbol
                    self.line = line
                    self.column = column

        class geo(GreyCat.Object):
            GC_CORE_GEO_LAT_EPS: float = 0.00000001
            GC_CORE_GEO_LAT_MIN: float = -85.05112878
            GC_CORE_GEO_LAT_MAX: float = 85.05112878
            GC_CORE_GEO_LNG_MIN: float = -180
            GC_CORE_GEO_LNG_MAX: float = 180

            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat.Stream) -> object:
                geo: std_n.core.geo = type.factory(type)
                geocode: c_int64 = stream.read_i64()
                geo.geocode = geocode
                decoded: Tuple[int, int] = std_n.core.geo.deinterleave64(
                    geocode.value)
                geo.lat = std_n.core.geo.GC_CORE_GEO_LAT_MIN + ((decoded[0] + 0.5) / 4294967296.0) * (
                    std_n.core.geo.GC_CORE_GEO_LAT_MAX + std_n.core.geo.GC_CORE_GEO_LAT_MIN)
                geo.lng = std_n.core.geo.GC_CORE_GEO_LNG_MIN + ((decoded[1] + 0.5) / 4294967296.0) * (
                    std_n.core.geo.GC_CORE_GEO_LNG_MAX + std_n.core.geo.GC_CORE_GEO_LNG_MIN)
                return geo

            def interleave64(xlo: int, ylo: int) -> int:
                pass  # TODO

            @staticmethod
            def deinterleave64(interleaved: int) -> Tuple[int, int]:
                pass  # TODO

            def __init__(self: std_n.core.geo, type: GreyCat.Type) -> None:
                super(type, None)
                self.geocode: c_int64
                self.lat: float
                self.lng: float

            def save(self: std_n.core.geo, stream: GreyCat.Stream) -> None:
                stream.write_i8(GreyCat.PrimitiveType.GEO)
                stream.write_i64(self.geocode)

        class GeoPoly(GreyCat.Object):
            type_name: str = 'core.GeoPoly'

            def __init__(self: std_n.core.GeoPoly, type: GreyCat.Type) -> None:
                super(type, None)

            def save(self: std_n.core.GeoPoly, stream: GreyCat.Stream) -> None:
                stream.write_i8(GreyCat.PrimitiveType.OBJECT)
                stream.write_i32(self.type.offset)
                if self.attributes is None:
                    stream.write_i32(c_int32(0))
                else:
                    stream.write_i32(c_int32(len(self.attributes)))
                    for offset in range(len(self.attributes)):
                        point: std_n.core.geo = self.attributes[offset]
                        stream.write_i64(point.geocode)

            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat.Stream)->object:
                size: int = stream.read_i32().value
                geoType: GreyCat.Type = type.greycat.types[type.greycat.type_offset_core_geo]
                points: list[std_n.core.geo] = [None] * size
                for offset in range(size):
                    points[offset] = std_n.core.geo(geoType)
                    points[offset].geocode = stream.read_i64()
                    # TODO: update
                gp: std_n.core.GeoPoly = type.factory(type)
                gp.attributes = points
                return gp
