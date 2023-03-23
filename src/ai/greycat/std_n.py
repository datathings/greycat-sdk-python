from __future__ import annotations
from ctypes import *
from typing import *

from ai.greycat.greycat import GreyCat

T = TypeVar('T')
U = TypeVar('U')


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
            def load(type: GreyCat.Type, stream: GreyCat.Stream) -> object:
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

        class Map(Generic[T, U], GreyCat.Object):
            type_name: str = 'core.Map'

            def __init__(self: std_n.core.Map[T, U], type: GreyCat.Type) -> None:
                super(type, None)
                self.__map: dict[T, U] = dict()

            def save(self: std_n.core.Map[T, U], stream: GreyCat.Stream) -> None:
                stream.write_i8(GreyCat.PrimitiveType.OBJECT)
                stream.write_i32(self.type.offset)
                stream.write_i32(self.size())
                for key in self.__map:
                    stream.write_object(key)
                    stream.write_object(self.__map[key])

            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat.Stream) -> object:
                map: std_n.core.Map = type.factory(type)
                mapLength = stream.read_i32().value
                for _ in range(mapLength):
                    map[stream.read()] = stream.read()
                return map

            def size(self: std_n.core.Map[T, U]) -> int:
                return len(self.__map)

            def get(self: std_n.core.Map[T, U], o: object) -> U:
                return self.__map[o]

            def set(self: std_n.core.Map[T, U], t: T, u: U) -> None:
                self.__map[t] = u

            def remove(self: std_n.core.Map[T, U], o: object) -> None:
                self.__map.pop(o, None)

            def clear(self: std_n.core.Map[T, U]) -> None:
                self.__map.clear()

        class node(GreyCat.Object):
            def __init__(self: std_n.core.node, type: GreyCat.Type) -> None:
                super(type, None)
                self.ref: c_int64

            def save(self: std_n.core.node, stream: GreyCat.Stream) -> None:
                stream.write_i8(GreyCat.PrimitiveType.NODE)
                stream.write_i64(self.ref)

            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat.Stream) -> object:
                res: std_n.core.node = type.factory(type)
                res.ref = stream.read_i64()
                return res

        class nodeGeo(GreyCat.Object):
            def __init__(self: std_n.core.nodeGeo, type: GreyCat.Type) -> None:
                super(type, None)
                self.ref: c_int64

            def save(self: std_n.core.nodeGeo, stream: GreyCat.Stream) -> None:
                stream.write_i8(GreyCat.PrimitiveType.NODE_GEO)
                stream.write_i64(self.ref)

            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat.Stream) -> object:
                res: std_n.core.nodeGeo = type.factory(type)
                res.ref = stream.read_i64()
                return res

        class nodeIndex(GreyCat.Object):
            type_name: str = "core.nodeIndex"

            def __init__(self: std_n.core.nodeIndex, type: GreyCat.Type) -> None:
                super(type, None)
                self.ref: c_int64

            def save(self: std_n.core.nodeIndex, stream: GreyCat.Stream) -> None:
                stream.write_i8(GreyCat.PrimitiveType.NODE_INDEX)
                stream.write_i64(self.ref)

            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat.Stream) -> object:
                res: std_n.core.nodeIndex = type.factory(type)
                res.ref = stream.read_i64()
                return res

        class nodeIndexBucket(GreyCat.Object):
            def __init__(self: std_n.core.nodeIndexBucket, type: GreyCat.Type) -> None:
                super(type, None)

            def save(self: std_n.core.nodeIndexBucket, stream: GreyCat.Stream) -> None:
                stream.write_i8(GreyCat.PrimitiveType.OBJECT)
                stream.write_i32(self.type.offset)
                if self.attributes is None:
                    stream.write_i32(c_int32(0))
                else:
                    stream.write_i32(c_int32(len(self.attributes)))
                    for offset in range(len(self.attributes)):
                        stream.write_object(self.attributes[offset])

            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat.Stream) -> object:
                size = stream.read_i32()
                data: list[object] = [None] * size
                for offset in range(size):
                    data[offset] = stream.read()
                res: std_n.core.nodeIndexBucket = type.factory(type)
                res.attributes = data
                return res

        class nodeList(GreyCat.Object):
            def __init__(self: std_n.core.nodeList, type: GreyCat.Type) -> None:
                super(type, None)
                self.ref: c_int64

            def save(self: std_n.core.nodeList, stream: GreyCat.Stream) -> None:
                stream.write_i8(GreyCat.PrimitiveType.NODE_LIST)
                stream.write_i64(self.ref)

            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat.Stream) -> object:
                res: std_n.core.nodeList = type.factory(type)
                res.ref = stream.read_i64()
                return res

        class nodeTime(GreyCat.Object):
            def __init__(self: std_n.core.nodeTime, type: GreyCat.Type) -> None:
                super(type, None)
                self.ref: c_int64

            def save(self: std_n.core.nodeTime, stream: GreyCat.Stream) -> None:
                stream.write_i8(GreyCat.PrimitiveType.NODE_TIME)
                stream.write_i64(self.ref)

            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat.Stream) -> object:
                res: std_n.core.nodeTime = type.factory(type)
                res.ref = stream.read_i64()
                return res

        class Table(Generic[T], GreyCat.Object):
            def __init__(self: std_n.core.Table[T], type: GreyCat.Type) -> None:
                super(type, None)
                self.cols: c_int32
                self.rows: c_int32
                self.meta: list[std_n.core.Table.TableColumnMeta]
                self.data: list[T]

            def save(self: std_n.core.Table[T], stream: GreyCat.Stream) -> None:
                stream.write_i8(GreyCat.PrimitiveType.OBJECT)
                stream.write_i32(self.type.offset)
                stream.write_i32(self.cols)
                stream.write_i32(self.rows)
                stream.write_bool(self.meta is not None)
                if self.meta is not None:
                    for offset in len(self.meta):
                        colMeta: std_n.core.Table.TableColumnMeta = self.meta[offset]
                        stream.write_i32(colMeta.colType)
                        stream.write_i32(colMeta.type)
                        stream.write_i32(colMeta.size)
                        stream.write_f64(colMeta.sum)
                        stream.write_f64(colMeta.sumSq)
                        stream.write_i64(colMeta.min)
                        stream.write_i64(colMeta.max)
                        stream.write_bool(colMeta.index)
                        stream.write_i32(colMeta.tz)
                for offset in len(self.data):
                    stream.write_object(self.data[offset])

            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat.Stream) -> object:
                cols: c_int32 = stream.read_i32()
                rows: c_int32 = stream.read_i32()
                useMeta: bool = stream.read_bool()
                meta: list[std_n.core.Table.TableColumnMeta] = None
                if useMeta:
                    meta = [None] * cols.value
                    for col in range(cols.value):
                        meta[col] = std_n.core.Table.TableColumnMeta(stream.read_i32(), stream.read_i32(), stream.read_i32(
                        ), stream.read_f64(), stream.read_f64(), stream.read_i64(), stream.read_i64(), stream.read_bool(), stream.read_i32())
                capacity = cols.value = rows.value
                data: list[object] = [None] * capacity
                for offset in range(capacity):
                    data[offset] = stream.read()
                t: std_n.core.Table[object] = type.factory(type)
                t.cols = cols
                t.rows = rows
                t.meta = meta
                t.data = data
                return t

            class TableColumnMeta:
                def __init__(self: std_n.core.Table.TableColumnMeta, colType: c_int32, type: c_int32, size: c_int32, sum: c_double, sumSq: c_double, min: c_int64, max: c_int64, index: bool, tz: c_int32) -> None:
                    self.colType: c_int32 = colType
                    self.type: c_int32 = type
                    self.size: c_int32 = size
                    self.sum: c_double = sum
                    self.sumSq: c_double = sumSq
                    self.min: c_int64 = min
                    self.max: c_int64 = max
                    self.index: bool = index
                    self.tz: c_int32 = tz

        class Tensor(GreyCat.Object):
            def __init__(self: std_n.core.Tensor, type: GreyCat.Type) -> None:
                super(type, None)
                self.shape: list[c_int32]
                self.tensorType: c_byte
                self.size: c_int32
                self.data: bytes

            def save(self: std_n.core.Tensor, stream: GreyCat.Stream) -> None:
                stream.write_i8(GreyCat.PrimitiveType.OBJECT)
                stream.write_i32(self.type.offset)
                stream.write_i8(c_byte(len(self.shape)))
                stream.write_i8(self.tensorType)
                for offset in range(len(self.shape)):
                    stream.write_i32(self.shape[offset])
                stream.write_i32(self.size)
                stream.write_i8_array(self.data, 0, len(self.data))

            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat.Stream) -> object:
                nbDim: int = stream.read_i8().value
                tensorType: c_byte = stream.read_i8()
                shape: list[c_int32] = [None] * nbDim
                for offset in range(nbDim):
                    shape[offset] = stream.read_i32()
                size: c_int32 = stream.read_i32()
                bin_size: int = size.value
                match tensorType.value:
                    case 0 | 2:
                        size = c_int32(size.value * 4)
                    case 1 | 3 | 4:
                        size = c_int32(size.value * 8)
                    case 5:
                        size = c_int32(size.value * 16)
                    case _:
                        raise ValueError(tensorType)
                res: std_n.core.Tensor = type.factory(type)
                res.shape = shape
                res.tensorType = tensorType
                res.size = size
                res.data = stream.read_i8_array(bin_size)
                return res

        class time(GreyCat.Object):
            def __init__(self: std_n.core.time, type: GreyCat.Type) -> None:
                super(type, None)
                self.value: c_int64

            def save(self: std_n.core.time, stream: GreyCat.Stream) -> None:
                stream.write_i8(GreyCat.PrimitiveType.TIME)
                stream.write_i64(self.value)

            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat.Stream) -> object:
                res: std_n.core.time = type.factory(type)
                res.value = stream.read_i64()
                return res

        class String(GreyCat.Object):
            def __init__(self: std_n.core.String, type: GreyCat.Type) -> None:
                super(type, None)

            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat.Stream) -> object:
                return stream.read_string(stream.read_i32().value)

    class util:
        class Quantizer(GreyCat.Object):
            def __init__(self: std_n.util.Quantizer, type: GreyCat.Type) -> None:
                super(type, None)
                raise NotImplementedError

            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat.Stream) -> object:
                raise NotImplementedError

        class Buffer(GreyCat.Object):
            def __init__(self: std_n.util.Buffer, type: GreyCat.Type) -> None:
                super(type, None)
                self.data = bytes

            def save(self: std_n.util.Buffer, stream: GreyCat.Stream) -> None:
                stream.write_i8(GreyCat.PrimitiveType.OBJECT)
                stream.write_i32(self.type.offset)
                stream.write_i32(len(self.data))
                stream.write_i8_array(self.data, 0, len(self.data))

            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat.Stream) -> object:
                buf: std_n.util.Buffer = type.factory(type)
                buf.data = stream.read_i8_array(stream.read_i32().value)
                return buf

        class Gaussian(GreyCat.Object):
            def __init__(self: std_n.util.Gaussian, type: GreyCat.Type) -> None:
                super(type, None)
                self.sum: c_double
                self.sumSq: c_double
                self.size: c_int64
                self.nbAccepted: c_int64
                self.nbRejected: c_int64
                self.nbNull: c_int64
                self.min: c_double
                self.max: c_double
                self.minBound: c_double
                self.maxBound: c_double

            def save(self: std_n.util.Gaussian, stream: GreyCat.Stream) -> None:
                stream.write_i8(GreyCat.PrimitiveType.OBJECT)
                stream.write_i32(self.type.offset)
                stream.write_f64(self.sum)
                stream.write_f64(self.sumSq)
                stream.write_i64(self.size)
                stream.write_i64(self.nbAccepted)
                stream.write_i64(self.nbRejected)
                stream.write_i64(self.nbNull)
                stream.write_f64(self.min)
                stream.write_f64(self.max)
                stream.write_f64(self.minBound)
                stream.write_f64(self.maxBound)

            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat.Stream) -> object:
                g: std_n.util.Gaussian = type.factory(type)
                g.sum = stream.read_f64()
                g.sumSq = stream.read_f64()
                g.size = stream.read_i64()
                g.nbAccepted = stream.read_i64()
                g.nbRejected = stream.read_i64()
                g.nbNull = stream.read_i64()
                g.min = stream.read_f64()
                g.max = stream.read_f64()
                g.minBound = stream.read_f64()
                g.maxBound = stream.read_f64()
                return g

        class GaussianProfile(GreyCat.Object):
            def __init__(self: std_n.util.GaussianProfile, type: GreyCat.Type) -> None:
                super(type, None)
                # self.size: c_int32
                self.data: bytes

            def save(self: std_n.util.GaussianProfile, stream: GreyCat.Stream) -> None:
                stream.write_i8(GreyCat.PrimitiveType.OBJECT)
                stream.write_i32(self.type.offset)
                # stream.write_i32(self.size)
                stream.write_i32(c_int32(len(self.data)))
                stream.write_i8_array(self.data)

            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat.Stream) -> object:
                g: std_n.util.GaussianProfile = type.factory(type)
                # g.size = stream.read_i32()
                g.data = stream.read_i8_array(stream.read_i32().value)
                return g

        class HistogramF64(GreyCat.Object):
            def __init__(self: std_n.util.HistogramF64, type: GreyCat.Type) -> None:
                super(type, None)
                self.realMin: c_double
                self.realMax: c_double
                self.min: c_double
                self.max: c_double
                self.size: c_int64
                self.nullCount: c_int64
                self.maxRange: c_int64
                self.sum: c_double
                self.sumSq: c_double
                self.unitMagnitude: c_int32
                self.significantFigures: c_int32
                self.subBucketHalfCountMagnitude: c_int32
                self.subBucketHalfCount: c_int32
                self.subBucketMask: c_int64
                self.subBucketCount: c_int32
                self.bucketCount: c_int32
                self.minValue: c_int64
                self.maxValue: c_int64
                self.normalizingIndexOffset: c_int32
                self.countsLen: c_int32
                self.totalCount: c_int64
                self.counts: list[c_int64]

            def save(self: std_n.util.HistogramF64, stream: GreyCat.Stream) -> None:
                stream.write_i8(GreyCat.PrimitiveType.OBJECT)
                stream.write_i32(self.type.offset)
                stream.write_f64(self.realMin)
                stream.write_f64(self.realMax)
                stream.write_f64(self.min)
                stream.write_f64(self.max)
                stream.write_i64(self.size)
                stream.write_i64(self.nullCount)
                stream.write_i64(self.maxRange)
                stream.write_f64(self.sum)
                stream.write_f64(self.sumSq)
                stream.write_i32(self.unitMagnitude)
                stream.write_i32(self.significantFigures)
                stream.write_i32(self.subBucketHalfCountMagnitude)
                stream.write_i32(self.subBucketHalfCount)
                stream.write_i64(self.subBucketMask)
                stream.write_i32(self.subBucketCount)
                stream.write_i32(self.bucketCount)
                stream.write_i64(self.minValue)
                stream.write_i64(self.maxValue)
                stream.write_i32(self.normalizingIndexOffset)
                stream.write_i32(self.countsLen)
                stream.write_i64(self.totalCount)
                for offset in len(self.counts):
                    stream.write_i64(self.counts[offset])

            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat.Stream) -> object:
                realMin = stream.read_f64()
                realMax = stream.read_f64()
                min = stream.read_f64()
                max = stream.read_f64
                size = stream.read_i64()
                nullCount = stream.read_i64()
                maxRange = stream.read_i64()
                sum = stream.read_f64()
                sumSq = stream.read_f64()
                unitMagnitude = stream.read_i32()
                significantFigures = stream.read_i32()
                subBucketHalfCountMagnitude = stream.read_i32()
                subBucketHalfCount = stream.read_i32()
                subBucketMask = stream.read_i64()
                subBucketCount = stream.read_i32()
                bucketCount = stream.read_i32()
                minValue = stream.read_i64()
                maxValue = stream.read_i64()
                normalizingIndexOffset = stream.read_i32()
                countsLen = stream.read_i32()
                totalCount = stream.read_i64()
                counts = [None] * countsLen.value
                for offset in range(countsLen.value):
                    counts[offset] = stream.read_i64()
                h: std_n.util.HistogramF64 = type.factory(type)
                h.realMin = realMin
                h.realMax = realMax
                h.min = min
                h.max = max
                h.size = size
                h.nullCount = nullCount
                h.maxRange = maxRange
                h.sum = sum
                h.sumSq = sumSq
                h.unitMagnitude = unitMagnitude
                h.significantFigures = significantFigures
                h.subBucketHalfCountMagnitude = subBucketHalfCountMagnitude
                h.subBucketCount = subBucketHalfCount
                h.subBucketMask = subBucketMask
                h.subBucketCount = subBucketCount
                h.bucketCount = bucketCount
                h.minValue = minValue
                h.maxValue = maxValue
                h.normalizingIndexOffset = normalizingIndexOffset
                h.countsLen = countsLen
                h.totalCount = totalCount
                h.counts = counts
                return h

        class HistogramF64(GreyCat.Object):
            def __init__(self: std_n.util.HistogramF64, type: GreyCat.Type) -> None:
                super(type, None)
                self.realMin: c_int64
                self.realMax: c_int64
                self.min: c_int64
                self.max: c_int64
                self.size: c_int64
                self.nullCount: c_int64
                self.maxRange: c_int64
                self.sum: c_double
                self.sumSq: c_double
                self.unitMagnitude: c_int32
                self.significantFigures: c_int32
                self.subBucketHalfCountMagnitude: c_int32
                self.subBucketHalfCount: c_int32
                self.subBucketMask: c_int64
                self.subBucketCount: c_int32
                self.bucketCount: c_int32
                self.minValue: c_int64
                self.maxValue: c_int64
                self.normalizingIndexOffset: c_int32
                self.countsLen: c_int32
                self.totalCount: c_int64
                self.counts: list[c_int64]

            def save(self: std_n.util.HistogramF64, stream: GreyCat.Stream) -> None:
                stream.write_i8(GreyCat.PrimitiveType.OBJECT)
                stream.write_i32(self.type.offset)
                stream.write_i64(self.realMin)
                stream.write_i64(self.realMax)
                stream.write_i64(self.min)
                stream.write_i64(self.max)
                stream.write_i64(self.size)
                stream.write_i64(self.nullCount)
                stream.write_i64(self.maxRange)
                stream.write_f64(self.sum)
                stream.write_f64(self.sumSq)
                stream.write_i32(self.unitMagnitude)
                stream.write_i32(self.significantFigures)
                stream.write_i32(self.subBucketHalfCountMagnitude)
                stream.write_i32(self.subBucketHalfCount)
                stream.write_i64(self.subBucketMask)
                stream.write_i32(self.subBucketCount)
                stream.write_i32(self.bucketCount)
                stream.write_i64(self.minValue)
                stream.write_i64(self.maxValue)
                stream.write_i32(self.normalizingIndexOffset)
                stream.write_i32(self.countsLen)
                stream.write_i64(self.totalCount)
                for offset in len(self.counts):
                    stream.write_i64(self.counts[offset])

            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat.Stream) -> object:
                realMin = stream.read_i64()
                realMax = stream.read_i64()
                min = stream.read_i64()
                max = stream.read_i64
                size = stream.read_i64()
                nullCount = stream.read_i64()
                maxRange = stream.read_i64()
                sum = stream.read_f64()
                sumSq = stream.read_f64()
                unitMagnitude = stream.read_i32()
                significantFigures = stream.read_i32()
                subBucketHalfCountMagnitude = stream.read_i32()
                subBucketHalfCount = stream.read_i32()
                subBucketMask = stream.read_i64()
                subBucketCount = stream.read_i32()
                bucketCount = stream.read_i32()
                minValue = stream.read_i64()
                maxValue = stream.read_i64()
                normalizingIndexOffset = stream.read_i32()
                countsLen = stream.read_i32()
                totalCount = stream.read_i64()
                counts = [None] * countsLen.value
                for offset in range(countsLen.value):
                    counts[offset] = stream.read_i64()
                h: std_n.util.HistogramF64 = type.factory(type)
                h.realMin = realMin
                h.realMax = realMax
                h.min = min
                h.max = max
                h.size = size
                h.nullCount = nullCount
                h.maxRange = maxRange
                h.sum = sum
                h.sumSq = sumSq
                h.unitMagnitude = unitMagnitude
                h.significantFigures = significantFigures
                h.subBucketHalfCountMagnitude = subBucketHalfCountMagnitude
                h.subBucketCount = subBucketHalfCount
                h.subBucketMask = subBucketMask
                h.subBucketCount = subBucketCount
                h.bucketCount = bucketCount
                h.minValue = minValue
                h.maxValue = maxValue
                h.normalizingIndexOffset = normalizingIndexOffset
                h.countsLen = countsLen
                h.totalCount = totalCount
                h.counts = counts
                return h

        class ProgressTracker(GreyCat.Object):
            def __init__(self: std_n.util.ProgressTracker, type: GreyCat.Type) -> None:
                super(type, None)
                self.initialTime: c_int64
                self.lastTime: c_int64
                self.previousTime: c_int64
                self.previousSteps: c_int64
                self.maxStep: c_int64
                self.nbStep: c_int64
                self.duration: c_int64
                self.lapDuration: c_int64
                self.totalSpeed: c_double
                self.stepSpeed: c_double
                self.progress: c_double
                self.remainingTime: c_int64

            def save(self: std_n.util.ProgressTracker, stream: GreyCat.Stream) -> None:
                stream.write_i8(GreyCat.PrimitiveType.OBJECT)
                stream.write_i32(self.type.offset)
                stream.write_i64(self.initialTime)
                stream.write_i64(self.lastTime)
                stream.write_i64(self.previousTime)
                stream.write_i64(self.previousSteps)
                stream.write_i64(self.maxStep)
                stream.write_i64(self.nbStep)
                stream.write_i64(self.duration)
                stream.write_i64(self.lapDuration)
                stream.write_f64(self.totalSpeed)
                stream.write_f64(self.stepSpeed)
                stream.write_f64(self.progress)
                stream.write_i64(self.remainingTime)

            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat.Stream) -> object:
                initialTime: c_int64 = stream.read_i64()
                lastTime: c_int64 = stream.read_i64()
                previousTime: c_int64 = stream.read_i64()
                previousSteps: c_int64 = stream.read_i64()
                maxStep: c_int64 = stream.read_i64()
                nbStep: c_int64 = stream.read_i64()
                duration: c_int64 = stream.read_i64()
                lapDuration: c_int64 = stream.read_i64()
                totalSpeed: c_double = stream.read_f64()
                stepSpeed: c_double = stream.read_f64()
                progress: c_double = stream.read_f64()
                remainingTime: c_int64 = stream.read_i64()
                pt: std_n.util.ProgressTracker = type.factory(type)
                pt.initialTime = initialTime
                pt.lastTime = lastTime
                pt.previousTime = previousTime
                pt.previousSteps = previousSteps
                pt.maxStep = maxStep
                pt.nbStep = nbStep
                pt.duration = duration
                pt.lapDuration = lapDuration
                pt.totalSpeed = totalSpeed
                pt.stepSpeed = stepSpeed
                pt.progress = progress
                pt.remainingTime = remainingTime
                return pt

        class Iban(GreyCat.Object):
            def __init__(self: std_n.util.Iban, type: GreyCat.Type) -> None:
                super(type, None)
                self.infoOff: c_int32
                self.data: bytes

            def save(self: std_n.util.Iban, stream: GreyCat.Stream) -> None:
                stream.write_i8(GreyCat.PrimitiveType.OBJECT)
                stream.write_i32(self.type.offset)
                stream.write_i32(self.infoOff)
                stream.write_i32(c_int32(len(self.data)))
                stream.write_i8_array(self.data, 0, len(self.data))

            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat.Stream) -> object:
                iban: std_n.util.Iban = type.factory(type)
                iban.infoOff = stream.read_i32()
                iban.data = stream.read_i8_array(stream.read_i32())
                return iban

        class Queue(Generic[T], GreyCat.Object):
            def __init__(self: std_n.util.Queue[T], type: GreyCat.Type) -> None:
                super(type, None)
                self.__queue: list[T]

            def save(self: std_n.util.Queue[T], stream: GreyCat.Stream) -> None:
                stream.write_i8(GreyCat.PrimitiveType.OBJECT)
                stream.write_i32(self.type.offset)
                stream.write_i64(c_int64(self.size()))  # width
                stream.write_i32(c_int32(self.size()))  # size
                stream.write_i64(c_int32(self.size()))  # capacity
                stream.write_i64(c_int64(self.size()))  # TODO: head - values
                stream.write_i64(c_int64(0))  # TODO: tail - values
                for t in self.__queue:
                    stream.write_object(t)

            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat.Stream) -> object:
                stream.read_i64()  # width
                size: int = stream.read_i32().value
                capacity: int = stream.read_i32().value
                queue: std_n.util.Queue[object] = type.factory(type)
                for _ in range(size):
                    queue.enqueue(stream.read())
                for _ in range(size, capacity):
                    stream.read()
                return queue

            def size(self: std_n.util.Queue[T]) -> int:
                return len(self.__queue)

            def enqueue(self: std_n.util.Queue[T], t: T) -> None:
                self.__queue.append(t)

            def dequeue(self: std_n.util.Queue[T]) -> T | None:
                t: T = self.head()
                if len(self.__queue) > 0:
                    self.__queue = self.__queue[1:]
                return t

            def head(self: std_n.util.Queue[T]) -> T | None:
                return self.__queue[0] if len(self.__queue) > 0 else None

        class SlidingWindow(GreyCat.Object):
            def __init__(self: std_n.util.SlidingWindow, type: GreyCat.Type) -> None:
                super(type, None)
                self.width: c_int64
                self.sumType: c_byte
                self.sum: c_double
                self.sumSq: c_double
                self.size: c_int32
                self.capacity: c_int32
                self.toHead: c_int64
                self.toTail: c_int64
                self.values: list[object]

            def save(self: std_n.util.SlidingWindow, stream: GreyCat.Stream) -> None:
                stream.write_i8(GreyCat.PrimitiveType.OBJECT)
                stream.write_i32(self.type.offset)
                stream.write_i64(self.width)
                stream.write_i8(self.sumType)
                stream.write_f64(self.sum)
                stream.write_f64(self.sumSq)
                stream.write_i32(self.size)
                stream.write_i32(self.capacity)
                stream.write_i64(self.toHead)
                stream.write_i64(self.toTail)
                for offset in range(len(self.values)):
                    stream.write_object(self.values[offset])

            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat.Stream) -> object:
                width: c_int64 = stream.read_i64()
                sumType: c_byte = stream.read_i8()
                sum: c_double = stream.read_f64()
                sumSq: c_double = stream.read_f64()
                size: c_int32 = stream.read_i32()
                capacity: c_int32 = stream.read_i32()
                toHead: c_int64 = stream.read_i64()
                toTail: c_int64 = stream.read_i64()
                values: list[object] = [None] * capacity
                for offset in range(capacity):
                    values[offset] = stream.read()
                sw: std_n.util.SlidingWindow = type.factory(type)
                sw.width = width
                sw.sumType = sumType
                sw.sum = sum
                sw.sumSq = sumSq
                sw.size = size
                sw.capacity = capacity
                sw.toHead = toHead
                sw.toTail = toTail
                sw.values = values

        class TimeWindow(GreyCat.Object):
            def __init__(self: std_n.util.TimeWindow, type: GreyCat.Type) -> None:
                super(type, None)
                self.width: c_int64
                self.sumType: c_byte
                self.sum: c_double
                self.sumSq: c_double
                self.size: c_int32
                self.capacity: c_int32
                self.toHead: c_int64
                self.toTail: c_int64
                self.values: list[Tuple[object, c_int64]]

            def save(self: std_n.util.TimeWindow, stream: GreyCat.Stream) -> None:
                stream.write_i8(GreyCat.PrimitiveType.OBJECT)
                stream.write_i32(self.type.offset)
                stream.write_i64(self.width)
                stream.write_i8(self.sumType)
                stream.write_f64(self.sum)
                stream.write_f64(self.sumSq)
                stream.write_i32(self.size)
                stream.write_i32(self.capacity)
                stream.write_i64(self.toHead)
                stream.write_i64(self.toTail)
                for offset in range(len(self.values)):
                    valueTime = self.values[offset]
                    stream.write_object(valueTime[0])
                    stream.write_i64(valueTime[1])

            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat.Stream) -> object:
                width: c_int64 = stream.read_i64()
                sumType: c_byte = stream.read_i8()
                sum: c_double = stream.read_f64()
                sumSq: c_double = stream.read_f64()
                size: c_int32 = stream.read_i32()
                capacity: c_int32 = stream.read_i32()
                toHead: c_int64 = stream.read_i64()
                toTail: c_int64 = stream.read_i64()
                values: list[Tuple[object, c_int64]] = [
                    None] * capacity
                for offset in range(capacity):
                    values[offset] = (stream.read(), stream.read_i64())
                sw: std_n.util.TimeWindow = type.factory(type)
                sw.width = width
                sw.sumType = sumType
                sw.sum = sum
                sw.sumSq = sumSq
                sw.size = size
                sw.capacity = capacity
                sw.toHead = toHead
                sw.toTail = toTail
                sw.values = values
