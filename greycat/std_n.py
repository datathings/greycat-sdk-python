from __future__ import annotations

from _collections_abc import dict_keys, dict_values, dict_items
from collections import deque
import ctypes
from ctypes import *
from itertools import repeat
import math
import numpy
from struct import pack, unpack
import sys
from typing import *


try:
    import pandas
except ModuleNotFoundError:
    pass
try:
    import tensorflow
except ModuleNotFoundError:
    pass

try:
    import torch
except ModuleNotFoundError:
    pass

from . import GreyCat, PrimitiveType

import greycat


class std_n:
    class core:
        __T = TypeVar("__T")
        __U = TypeVar("__U")

        # Primitive types

        class _duration(GreyCat.Object):
            def __init__(self, type: GreyCat.Type) -> None:
                self.value: int
                super().__init__(type, None)

            @final
            def _save_type(self, stream: GreyCat._Stream, _=None) -> None:
                stream.write_i8(PrimitiveType.DURATION)

            @final
            def _save(self, stream: GreyCat._Stream, type_offset: int | None = None) -> None:
                stream.write_vi64(self.value)

            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat._Stream) -> Any:
                res: std_n.core._duration = type.factory(type, [])
                res.value = stream.read_vi64()
                return res

            def to_numpy(self) -> numpy.timedelta64:
                return numpy.timedelta64(self.value, "us")

            @staticmethod
            def from_numpy(td: numpy.timedelta64, greycat: GreyCat | None = None) -> std_n.core._duration:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                duration = std_n.core._duration(
                    greycat.type_offset_core_duration)
                duration.value = td.astype(int) if numpy.datetime_data(td)[0] in [
                    "us", "μs"] else td.astype("timedelta64[us]").astype(int)
                return duration

        class _field(GreyCat.Object):
            pass  # TODO

        class _function(GreyCat.Object):
            def __init__(self, type: GreyCat.Type) -> None:
                super().__init__(type, None)

            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat._Stream) -> Any:
                raise RuntimeError("unsupported")

        class _geo(GreyCat.Object):
            __GC_CORE_GEO_LAT_EPS: Final[float] = 0.00000001
            __GC_CORE_GEO_LAT_MIN: Final[float] = -85.05112878
            __GC_CORE_GEO_LAT_MAX: Final[float] = 85.05112878
            __GC_CORE_GEO_LNG_MIN: Final[float] = -180
            __GC_CORE_GEO_LNG_MAX: Final[float] = 180

            def __init__(
                self,
                type: GreyCat.Type,
                lat: float | None = None,
                lng: float | None = None,
            ):
                self.geocode: int
                self.lat: float
                self.lng: float
                super().__init__(type, None)
                if lat is not None and lng is not None:
                    self.geocode = std_n.core._geo.__encode(lat, lng)
                    self.lat = lat
                    self.lns = lng

            @final
            def _save_type(self, stream: GreyCat._Stream, _=None) -> None:
                stream.write_i8(PrimitiveType.GEO)

            @final
            def _save(self, stream: GreyCat._Stream, type_offset: int | None = None) -> None:
                stream.write_i64(self.geocode)

            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat._Stream) -> Any:
                geo: std_n.core._geo = type.factory(type, [])
                value: int = stream.read_i64()
                geo.geocode = value
                lat_offset: int
                lng_offset: int
                lat_offset, lng_offset = std_n.core._geo.__deinterleave64(
                    value)
                geo.lat = std_n.core._geo.__GC_CORE_GEO_LAT_MIN + (
                    (lat_offset + 0.5) / 4294967296
                ) * (
                    std_n.core._geo.__GC_CORE_GEO_LAT_MAX
                    - std_n.core._geo.__GC_CORE_GEO_LAT_MIN
                )
                geo.lng = std_n.core._geo.__GC_CORE_GEO_LNG_MIN + (
                    (lng_offset + 0.5) / 4294967296
                ) * (
                    std_n.core._geo.__GC_CORE_GEO_LNG_MAX
                    - std_n.core._geo.__GC_CORE_GEO_LNG_MIN
                )
                return geo

            def __str__(self) -> str:
                return f"geo{{lat={self.lat},lng={self.lng}}}"

            @staticmethod
            def __interleave64(xlo: int, ylo: int) -> int:
                B: list[int] = [
                    6148914691236517205,
                    3689348814741910323,
                    1085102592571150095,
                    71777214294589695,
                    281470681808895,
                ]
                S: list[int] = [1, 2, 4, 8, 16]
                x: int = xlo
                y: int = ylo
                x = (x | (x << S[4])) & B[4]
                y = (y | (y << S[4])) & B[4]
                x = (x | (x << S[3])) & B[3]
                y = (y | (y << S[3])) & B[3]
                x = (x | (x << S[2])) & B[2]
                y = (y | (y << S[2])) & B[2]
                x = (x | (x << S[1])) & B[1]
                y = (y | (y << S[1])) & B[1]
                x = (x | (x << S[0])) & B[0]
                y = (y | (y << S[0])) & B[0]
                return x | (y << 1)

            @staticmethod
            def __deinterleave64(interleaved: int) -> tuple[int, int]:
                B: list[int] = [
                    6148914691236517205,
                    3689348814741910323,
                    1085102592571150095,
                    71777214294589695,
                    281470681808895,
                    4294967295,
                ]
                S: list[int] = [0, 1, 2, 4, 8, 16]
                x: int = interleaved
                y: int = interleaved >> 1
                x = (x | (x >> S[0])) & B[0]
                y = (y | (y >> S[0])) & B[0]
                x = (x | (x >> S[1])) & B[1]
                y = (y | (y >> S[1])) & B[1]
                x = (x | (x >> S[2])) & B[2]
                y = (y | (y >> S[2])) & B[2]
                x = (x | (x >> S[3])) & B[3]
                y = (y | (y >> S[3])) & B[3]
                x = (x | (x >> S[4])) & B[4]
                y = (y | (y >> S[4])) & B[4]
                x = (x | (x >> S[5])) & B[5]
                y = (y | (y >> S[5])) & B[5]
                return x, y

            @staticmethod
            def __encode(latitude: float, longitude: float) -> int:
                if latitude < std_n.core._geo.__GC_CORE_GEO_LAT_MIN:
                    latitude = std_n.core._geo.__GC_CORE_GEO_LAT_MIN
                if latitude >= std_n.core._geo.__GC_CORE_GEO_LAT_MAX:
                    latitude = (
                        std_n.core._geo.__GC_CORE_GEO_LAT_MAX
                        - std_n.core._geo.__GC_CORE_GEO_LAT_EPS
                    )
                if longitude < std_n.core._geo.__GC_CORE_GEO_LNG_MIN:
                    longitude = std_n.core._geo.__GC_CORE_GEO_LNG_MIN
                if longitude >= std_n.core._geo.__GC_CORE_GEO_LNG_MAX:
                    longitude = (
                        std_n.core._geo.__GC_CORE_GEO_LNG_MAX
                        - std_n.core._geo.__GC_CORE_GEO_LAT_EPS
                    )
                lat_offset: float = (
                    latitude - std_n.core._geo.__GC_CORE_GEO_LAT_MIN
                ) / (
                    std_n.core._geo.__GC_CORE_GEO_LAT_MAX
                    - std_n.core._geo.__GC_CORE_GEO_LAT_MIN
                )
                lng_offset: float = (
                    longitude - std_n.core._geo.__GC_CORE_GEO_LNG_MIN
                ) / (
                    std_n.core._geo.__GC_CORE_GEO_LNG_MAX
                    - std_n.core._geo.__GC_CORE_GEO_LNG_MIN
                )
                lat_offset *= 4294967296
                lng_offset *= 4294967296
                return std_n.core._geo.__interleave64(int(lat_offset), int(lng_offset))

        class _node(Generic[__T], GreyCat.Object):
            def __init__(self, type: GreyCat.Type) -> None:
                self.ref: c_uint64
                super().__init__(type, None)

            @final
            def _save_type(self, stream: GreyCat._Stream, _=None) -> None:
                stream.write_i8(PrimitiveType.NODE)

            @final
            def _save(self, stream: GreyCat._Stream, type_offset: int | None = None) -> None:
                stream.write_vu64(self.ref)

            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat._Stream) -> Any:
                res: std_n.core._node = type.factory(type, [])
                res.ref = stream.read_vu64()
                return res

        class _nodeGeo(Generic[__T], GreyCat.Object):
            def __init__(self, type: GreyCat.Type) -> None:
                self.ref: c_uint64
                super().__init__(type, None)

            @final
            def _save_type(self, stream: GreyCat._Stream, _=None) -> None:
                stream.write_i8(PrimitiveType.NODE_GEO)

            @final
            def _save(self, stream: GreyCat._Stream, type_offset: int | None = None) -> None:
                stream.write_vu64(self.ref)

            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat._Stream) -> Any:
                res: std_n.core._nodeGeo = type.factory(type, [])
                res.ref = stream.read_vu64()
                return res

        class _nodeIndex(Generic[__T, __U], GreyCat.Object):
            def __init__(self, type: GreyCat.Type) -> None:
                self.ref: c_uint64
                super().__init__(type, None)

            @final
            def _save_type(self, stream: GreyCat._Stream, _=None) -> None:
                stream.write_i8(PrimitiveType.NODE_INDEX)

            @final
            def _save(self, stream: GreyCat._Stream, type_offset: int | None = None) -> None:
                stream.write_vu64(self.ref)

            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat._Stream) -> Any:
                res: std_n.core._nodeIndex = type.factory(type, [])
                res.ref = stream.read_vu64()
                return res

        class _nodeList(Generic[__T], GreyCat.Object):
            def __init__(self, type: GreyCat.Type) -> None:
                self.ref: c_uint64
                super().__init__(type, None)

            @final
            def _save_type(self, stream: GreyCat._Stream, _=None) -> None:
                stream.write_i8(PrimitiveType.NODE_LIST)

            @final
            def _save(self, stream: GreyCat._Stream, type_offset: int | None = None) -> None:
                stream.write_vu64(self.ref)

            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat._Stream) -> Any:
                res: std_n.core._nodeList = type.factory(type, [])
                res.ref = stream.read_vu64()
                return res

        class _nodeTime(Generic[__T], GreyCat.Object):
            def __init__(self, type: GreyCat.Type) -> None:
                self.ref: c_uint64
                super().__init__(type, None)

            @final
            def _save_type(self, stream: GreyCat._Stream, _=None) -> None:
                stream.write_i8(PrimitiveType.NODE_TIME)

            @final
            def _save(self, stream: GreyCat._Stream, type_offset: int | None = None) -> None:
                stream.write_vu64(self.ref)

            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat._Stream) -> Any:
                res: std_n.core._nodeTime = type.factory(type, [])
                res.ref = stream.read_vu64()
                return res

        class _str(GreyCat.Object):
            pass  # TODO

        class _t2(GreyCat.Object):
            _INT32_MIN: int = -2147483648
            _UINT32_MIN: int = 2147483648

            def __init__(self, type: GreyCat.Type) -> None:
                self.x0: int
                self.x1: int
                super().__init__(type, None)

            @final
            def _save_type(self, stream: GreyCat._Stream, _=None) -> None:
                stream.write_i8(PrimitiveType.T2)

            @final
            def _save(self, stream: GreyCat._Stream, type_offset: int | None = None) -> None:
                stream.write_i64(self.__interleave())

            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat._Stream) -> Any:
                res: std_n.core._t2 = type.factory(type, [])
                res.__deinterleave(stream.read_i64())
                return res

            def __str__(self) -> str:
                return f"t2{{x0={self.x0},x1={self.x1}}}"

            def __interleave(self) -> int:
                return std_n.core._interleave64_2d(
                    self.x0 + std_n.core._t2._UINT32_MIN,
                    self.x1 + std_n.core._t2._UINT32_MIN,
                )

            def __deinterleave(self, interleaved: int) -> None:
                dc: int = std_n.core._deinterleave64_2d(interleaved)
                self.x0 = (dc & 0xFFFFFFFF) + std_n.core._t2._INT32_MIN
                self.x1 = (dc >> 32) + std_n.core._t2._INT32_MIN

        class _t2f(GreyCat.Object):  # TODO: fix
            def __init__(self, type: GreyCat.Type) -> None:
                self.x0: float
                self.x1: float
                super().__init__(type, None)

            @final
            def _save_type(self, stream: GreyCat._Stream, _=None) -> None:
                stream.write_i8(PrimitiveType.T2F)

            @final
            def _save(self, stream: GreyCat._Stream, type_offset: int | None = None) -> None:
                stream.write_i64(self.__interleave())

            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat._Stream) -> Any:
                res: std_n.core._t2f = type.factory(type, [])
                res.__deinterleave(stream.read_i64())
                return res

            def __str__(self) -> str:
                return f"t2f{{x0={self.x0},x1={self.x1}}}"

            def __interleave(self) -> int:
                return std_n.core._interleave64_2d(
                    unpack("I", pack("f", self.x0))[
                        0] + std_n.core._t2._UINT32_MIN,
                    unpack("I", pack("f", self.x1))[
                        0] + std_n.core._t2._UINT32_MIN,
                )

            def __deinterleave(self, interleaved: int) -> None:
                dc: int = std_n.core._deinterleave64_2d(interleaved)
                self.x0 = unpack(
                    "f", pack("I", (dc & 0xFFFFFFFF) + std_n.core._t2._INT32_MIN))[0]
                self.x1 = unpack("f", pack("I", (dc >> 32) +
                                 std_n.core._t2._INT32_MIN))[0]

        class _t3(GreyCat.Object):
            _INT21_MIN: int = -1048575 - 1
            __INT21_MAX: int = 1048575
            _UINT21_MIN: int = 4293918720

            def __init__(self, type: GreyCat.Type) -> None:
                self.x0: int
                self.x1: int
                self.x2: int
                super().__init__(type, None)

            @final
            def _save_type(self, stream: GreyCat._Stream, _=None) -> None:
                stream.write_i8(PrimitiveType.T3)

            @final
            def _save(self, stream: GreyCat._Stream, type_offset: int | None = None) -> None:
                stream.write_i64(self.__interleave())

            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat._Stream) -> Any:
                res: std_n.core._t3 = type.factory(type, [])
                res.__deinterleave(stream.read_i64())
                return res

            def __str__(self) -> str:
                return f"t3{{x0={self.x0},x1={self.x1},x2={self.x2}}}"

            def __interleave(self) -> int:
                return std_n.core._interleave64_3d(
                    self.x0 + std_n.core._t3._UINT21_MIN,
                    self.x1 + std_n.core._t3._UINT21_MIN,
                    self.x2 + std_n.core._t3._UINT21_MIN,
                )

            def __deinterleave(self, interleaved: int) -> None:
                B: list[int] = [
                    0x10C30C30C30C30C3,
                    0x100F00F00F00F00F,
                    0x001F0000FF0000FF,
                    0xFFFF00000000FFFF,
                    0x0001FFFFF,
                ]
                S: list[int] = [2, 4, 8, 16, 32]

                self.x0 = std_n.core._deinterleave64_3d(
                    interleaved) + std_n.core._t3._INT21_MIN
                self.x1 = std_n.core._deinterleave64_3d(
                    interleaved >> 1) + std_n.core._t3._INT21_MIN
                self.x2 = std_n.core._deinterleave64_3d(
                    interleaved >> 2) + std_n.core._t3._INT21_MIN

        class _t3f(GreyCat.Object):
            def __init__(self, type: GreyCat.Type) -> None:
                self.x0: float
                self.x1: float
                self.x2: float
                super().__init__(type, None)

            @final
            def _save_type(self, stream: GreyCat._Stream, _=None) -> None:
                stream.write_i8(PrimitiveType.T3F)

            @final
            def _save(self, stream: GreyCat._Stream, type_offset: int | None = None) -> None:
                stream.write_i64(self.__interleave())

            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat._Stream) -> Any:
                res: std_n.core._t3f = type.factory(type, [])
                res.__deinterleave(stream.read_i64())
                return res

            def __str__(self) -> str:
                return f"t3f{{x0={self.x0},x1={self.x1},x2={self.x2}}}"

            def __interleave(self) -> c_int64:
                return std_n.core._interleave64_3d(
                    (unpack("i", pack("f", self.x0))[0] >> 11)
                    + std_n.core._t3._UINT21_MIN,
                    (unpack("i", pack("f", self.x1))[0] >> 11)
                    + std_n.core._t3._UINT21_MIN,
                    (unpack("i", pack("f", self.x2))[0] >> 11)
                    + std_n.core._t3._UINT21_MIN,
                )

            def __deinterleave(self, interleaved: int) -> None:
                self.x0 = unpack("f", pack("i", (std_n.core._deinterleave64_3d(
                    interleaved) + std_n.core._t3._INT21_MIN) << 11))[0]
                self.x1 = unpack("f", pack("i", (std_n.core._deinterleave64_3d(
                    interleaved >> 1) + std_n.core._t3._INT21_MIN) << 11))[0]
                self.x2 = unpack("f", pack("i", (std_n.core._deinterleave64_3d(
                    interleaved >> 2) + std_n.core._t3._INT21_MIN) << 11))[0]

        class _t4(GreyCat.Object):
            _INT16_MIN: int = -32768
            __INT16_MAX: int = 32767
            _UINT16_MIN: int = 32768

            def __init__(self, type: GreyCat.Type) -> None:
                self.x0: int
                self.x1: int
                self.x2: int
                self.x3: int
                super().__init__(type, None)

            @final
            def _save_type(self, stream: GreyCat._Stream, _=None) -> None:
                stream.write_i8(PrimitiveType.T4)

            @final
            def _save(self, stream: GreyCat._Stream, type_offset: int | None = None) -> None:
                stream.write_i64(self.__interleave())

            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat._Stream) -> Any:
                res: std_n.core._t4 = type.factory(type, [])
                res.__deinterleave(stream.read_i64())
                return res

            def __str__(self) -> str:
                return f"t4{{x0={self.x0},x1={self.x1},x2={self.x2},x3={self.x3}}}"

            def __interleave(self) -> int:
                return std_n.core._interleave64_2d(
                    std_n.core._interleave64_2d(
                        self.x0 + std_n.core._t4._UINT16_MIN,
                        self.x2 + std_n.core._t4._UINT16_MIN,
                    ),
                    std_n.core._interleave64_2d(
                        self.x1 + std_n.core._t4._UINT16_MIN,
                        self.x3 + std_n.core._t4._UINT16_MIN,
                    )
                )

            def __deinterleave(self, interleaved: c_int64) -> None:
                x3120: int = std_n.core._deinterleave64_2d(interleaved)
                x20: int = std_n.core._deinterleave64_2d(x3120 & 0xFFFFFFFF)
                x31: int = std_n.core._deinterleave64_2d(x3120 >> 32)
                self.x0 = (x20 & 0xFFFF) + std_n.core._t4._INT16_MIN
                self.x1 = (x31 & 0xFFFF) + std_n.core._t4._INT16_MIN
                self.x2 = (x20 >> 32) + std_n.core._t4._INT16_MIN
                self.x3 = (x31 >> 32) + std_n.core._t4._INT16_MIN

        class _t4f(GreyCat.Object):
            def __init__(self, type: GreyCat.Type) -> None:
                self.x0: float
                self.x1: float
                self.x2: float
                self.x3: float
                super().__init__(type, None)

            @final
            def _save_type(self, stream: GreyCat._Stream, _=None) -> None:
                stream.write_i8(PrimitiveType.T4F)

            @final
            def _save(self, stream: GreyCat._Stream, type_offset: int | None = None) -> None:
                stream.write_i64(self.__interleave())

            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat._Stream) -> Any:
                res: std_n.core._t4f = type.factory(type, [])
                res.__deinterleave(stream.read_i64())
                return res

            def __str__(self) -> str:
                return f"t4f{{x0={self.x0},x1={self.x1},x2={self.x2},x3={self.x3}}}"

            def __interleave(self) -> int:
                return std_n.core._interleave64_2d(
                    std_n.core._interleave64_2d(
                        (unpack("i", pack("f", self.x0))[0] >> 16)
                        + std_n.core._t4._UINT16_MIN,
                        (unpack("i", pack("f", self.x2))[0] >> 16)
                        + std_n.core._t4._UINT16_MIN,
                    ),
                    std_n.core._interleave64_2d(
                        (unpack("i", pack("f", self.x1))[0] >> 16)
                        + std_n.core._t4._UINT16_MIN,
                        (unpack("i", pack("f", self.x3))[0] >> 16)
                        + std_n.core._t4._UINT16_MIN,
                    )
                )

            def __deinterleave(self, interleaved: c_int64) -> None:
                d3120: int = std_n.core._deinterleave64_2d(interleaved)
                d20: int = std_n.core._deinterleave64_2d(
                    d3120 & 0xFFFFFFFF)
                d31: int = std_n.core._deinterleave64_2d(d3120 >> 32)
                self.x0 = unpack(
                    "f", pack("i", ((d20 & 0xFFFF) + std_n.core._t4._INT16_MIN) << 16))[0]
                self.x1 = unpack(
                    "f", pack("i", ((d31 & 0xFFFF) + std_n.core._t4._INT16_MIN) << 16))[0]
                self.x2 = unpack(
                    "f", pack("i", ((d20 >> 32) + std_n.core._t4._INT16_MIN) << 16))[0]
                self.x3 = unpack(
                    "f", pack("i", ((d31 >> 32) + std_n.core._t4._INT16_MIN) << 16))[0]

        class _time(GreyCat.Object):
            def __init__(self, type: GreyCat.Type) -> None:
                self.value: int
                super().__init__(type, None)

            @final
            def _save_type(self, stream: GreyCat._Stream, _=None) -> None:
                stream.write_i8(PrimitiveType.TIME)

            @final
            def _save(self, stream: GreyCat._Stream, type_offset: int | None = None) -> None:
                stream.write_vi64(self.value)

            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat._Stream) -> Any:
                res: std_n.core._time = type.factory(type, [])
                res.value = stream.read_vi64()
                return res

            def to_numpy(self) -> numpy.datetime64:
                return numpy.datetime64(self.value, "us")

            @staticmethod
            def from_numpy(dt: numpy.datetime64, greycat: GreyCat | None = None) -> std_n.core._time:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                time = std_n.core._time(
                    greycat.types[greycat.type_offset_core_time])
                time.value = dt.astype(int) if numpy.datetime_data(dt)[0] in [
                    "us", "μs"] else dt.astype("datetime64[us]").astype(int)
                return time

            def __str__(self) -> str:
                return f"time{{timestamp: {int(self.value / 1_000_000)}, us_offset: {self.value % 1_000_000}}}"

        class _type(GreyCat.Object):
            pass  # TODO

        # Object types

        class _Array(Generic[__T], GreyCat.Object):
            def __init__(self, type: GreyCat.Type) -> None:
                super().__init__(type, [])

            def __save_typed(self, stream: GreyCat._Stream, type_offset: int, type_nullable: bool) -> None:
                nullables: bytearray | None = None
                if type_nullable:
                    for offset, e in enumerate(self):
                        if e is None:
                            if nullables is None:
                                nullables = bytearray(
                                    repeat(0, math.ceil(len(self) / 8)))
                            nullables[offset >> 3] |= 1 << (offset & 7)
                    stream.write_i8(0 if nullables is None else 1)
                    if nullables is not None:
                        stream.write_i8_array(nullables, 0, len(nullables))
                else:
                    stream.write_i8(0)
                b: bool
                char: c_char
                c: c_ubyte
                i: int
                f: float
                s: str
                o: GreyCat.Object
                if stream.greycat.type_offset_core_bool == type_offset:
                    stream.write_i8(PrimitiveType.BOOL)
                    stream.write_i8(0)  # TODO: manage monotonic
                    if type_nullable:
                        for b in self:
                            if b is not None:
                                stream.write_i8(1 if b else 0)
                    else:
                        for b in self:
                            stream.write_i8(1 if b else 0)
                elif stream.greycat.type_offset_core_char == type_offset:
                    stream.write_i8(PrimitiveType.CHAR)
                    stream.write_i8(0)  # TODO: manage monotonic
                    if type_nullable:
                        for char in self:
                            if char is None:
                                continue
                            c = c_ubyte(char.value)
                            if c > GreyCat._Stream.ASCII_MAX:
                                raise ValueError(
                                    f"Only ASCII characters are allowed: {c}")
                            stream.write_i8(c)
                    else:
                        for char in self:
                            c = c_ubyte(char.value)
                            if c > GreyCat._Stream.ASCII_MAX:
                                raise ValueError(
                                    f"Only ASCII characters are allowed: {c}")
                            stream.write_i8(c)
                elif stream.greycat.type_offset_core_int == type_offset:
                    stream.write_i8(PrimitiveType.INT)
                    stream.write_i8(0)  # TODO: manage monotonic
                    if type_nullable:
                        for i in self:
                            if i is not None:
                                stream.write_vi64(i)
                    else:
                        for i in self:
                            stream.write_vi64(i)
                elif stream.greycat.type_offset_core_float == type_offset:
                    stream.write_i8(PrimitiveType.FLOAT)
                    stream.write_i8(0)  # TODO: manage monotonic
                    if type_nullable:
                        for f in self:
                            if f is not None:
                                stream.write_f64(f)
                    else:
                        for f in self:
                            stream.write_f64(f)
                elif stream.greycat.type_offset_core_string == type_offset:
                    stream.write_i8(PrimitiveType.OBJECT)
                    stream.write_vu32(type_offset)
                    if type_nullable:
                        for s in self:
                            if s is  not None:
                                data = s.encode("utf8")
                                stream.write_vu32(len(data) << 1)
                                stream.write_i8_array(data, 0, len(data))
                    else:
                        for s in self:
                            data = s.encode("utf8")
                            stream.write_vu32(len(data) << 1)
                            stream.write_i8_array(data, 0, len(data))
                else:
                    if stream.greycat.type_offset_core_node == type_offset:
                        stream.write_i8(PrimitiveType.NODE)
                        stream.write_i8(0)  # TODO: manage monotonic
                    elif stream.greycat.type_offset_core_node_time == type_offset:
                        stream.write_i8(PrimitiveType.NODE_TIME)
                        stream.write_i8(0)  # TODO: manage monotonic
                    elif stream.greycat.type_offset_core_node_index == type_offset:
                        stream.write_i8(PrimitiveType.NODE_INDEX)
                        stream.write_i8(0)  # TODO: manage monotonic
                    elif stream.greycat.type_offset_core_node_list == type_offset:
                        stream.write_i8(PrimitiveType.NODE_LIST)
                        stream.write_i8(0)  # TODO: manage monotonic
                    elif stream.greycat.type_offset_core_node_geo == type_offset:
                        stream.write_i8(PrimitiveType.NODE_GEO)
                        stream.write_i8(0)  # TODO: manage monotonic
                    elif stream.greycat.type_offset_core_geo == type_offset:
                        stream.write_i8(PrimitiveType.GEO)
                        stream.write_i8(0)  # TODO: manage monotonic
                    elif stream.greycat.type_offset_core_time == type_offset:
                        stream.write_i8(PrimitiveType.TIME)
                        stream.write_i8(0)  # TODO: manage monotonic
                    elif stream.greycat.type_offset_core_duration == type_offset:
                        stream.write_i8(PrimitiveType.DURATION)
                        stream.write_i8(0)  # TODO: manage monotonic
                    elif stream.greycat.type_offset_core_t2 == type_offset:
                        stream.write_i8(PrimitiveType.T2)
                        stream.write_i8(0)  # TODO: manage monotonic
                    elif stream.greycat.type_offset_core_t3 == type_offset:
                        stream.write_i8(PrimitiveType.T3)
                        stream.write_i8(0)  # TODO: manage monotonic
                    elif stream.greycat.type_offset_core_t4 == type_offset:
                        stream.write_i8(PrimitiveType.T4)
                        stream.write_i8(0)  # TODO: manage monotonic
                    elif stream.greycat.type_offset_core_t2f == type_offset:
                        stream.write_i8(PrimitiveType.T2F)
                        stream.write_i8(0)  # TODO: manage monotonic
                    elif stream.greycat.type_offset_core_t3f == type_offset:
                        stream.write_i8(PrimitiveType.T3F)
                        stream.write_i8(0)  # TODO: manage monotonic
                    elif stream.greycat.type_offset_core_t4f == type_offset:
                        stream.write_i8(PrimitiveType.T4F)
                        stream.write_i8(0)  # TODO: manage monotonic
                    # elif […] TODO: other types
                    else:
                        stream.write_i8(PrimitiveType.OBJECT)
                        stream.write_vu32(type_offset)
                    if type_nullable:
                        for o in self:
                            if o is not None:
                                o._save(stream, type_offset)
                    else:
                        for o in self:
                            o._save(stream, type_offset)

            @final
            def _save(self, stream: GreyCat._Stream, type_offset: int | None = None) -> None:
                if (self.attributes is None or 0 == len(self)):
                    stream.write_vu32(0)
                    return
                stream.write_vu32(len(self))
                if type_offset is not None and 0 != stream.greycat.types[type_offset].genericAbiType:
                    g1AbiTypeDesc = stream.greycat.types[type_offset].g1AbiTypeDesc
                    self.__save_typed(
                        stream,
                        g1AbiTypeDesc >> 1,
                        1 == g1AbiTypeDesc & 1
                    )
                    return
                nullables: bytearray | None = None
                type_is_unique: bool = False
                unique_type: type | None = None
                value_is_monotonic: bool = False
                monotonic_value: Any | None = None
                e: std_n.core.__T
                for offset, e in enumerate(self):
                    if e is None:
                        if nullables is None:
                            nullables = bytearray(
                                repeat(0, math.ceil(len(self) / 8)))
                        nullables[offset >> 3] |= 1 << (offset & 7)
                    else:
                        _type = type(e)
                        if issubclass(_type, c_int64) or issubclass(_type, c_uint32) or issubclass(_type, c_int32) or issubclass(_type, c_uint16) or issubclass(_type, c_uint16) or issubclass(_type, c_uint8) or issubclass(_type, c_int8):
                            _type = int
                        elif issubclass(_type, c_double) or issubclass(_type, c_float):
                            _type = float
                        if unique_type is None:
                            type_is_unique = True
                            unique_type = _type
                        elif type_is_unique and unique_type is not _type:
                            type_is_unique = False
                        if monotonic_value is None:
                            value_is_monotonic = True
                            monotonic_value = e
                        elif value_is_monotonic and monotonic_value is not e:
                            value_is_monotonic = False
                stream.write_i8(0 if nullables is None else 1)
                if nullables is not None:
                    stream.write_i8_array(nullables, 0, len(nullables))
                char: c_char
                c: c_ubyte
                string: str
                object: GreyCat.Object
                if not type_is_unique:
                    stream.write_i8(PrimitiveType.UNDEFINED)
                    for e in self:
                        if e is not None:
                            stream.write(e)
                else:
                    if bool is unique_type:
                        stream.write_i8(PrimitiveType.BOOL)
                        stream.write_i8(0)  # TODO: manage monotonic
                        for e in self:
                            if e is not None:
                                stream.write_bool(e)
                    elif c_char is unique_type:
                        stream.write_i8(PrimitiveType.CHAR)
                        stream.write_i8(0)  # TODO: manage monotonic
                        for char in self:
                            if char is not None:
                                c = c_ubyte(char.value)
                                if c > GreyCat._Stream.ASCII_MAX:
                                    raise ValueError(
                                        f"Only ASCII characters are allowed: {c}")
                                stream.write_i8(c)
                    elif int is unique_type:
                        stream.write_i8(PrimitiveType.INT)
                        stream.write_i8(0)  # TODO: manage monotonic
                        for e in self:
                            if isinstance(e, c_int64):
                                stream.write_vi64(e.value)
                            elif e is not None:
                                if isinstance(e, ctypes._SimpleCData):
                                    e = e.value
                                stream.write_vi64(e)
                    elif float is unique_type:
                        stream.write_i8(PrimitiveType.FLOAT)
                        stream.write_i8(0)  # TODO: manage monotonic
                        for e in self:
                            if isinstance(e, c_double):
                                stream.write_f64(e.value)
                            elif e is not None:
                                if isinstance(e, ctypes._SimpleCData):
                                    e = e.value
                                stream.write_f64(e)
                    elif str is unique_type:
                        stream.write_i8(PrimitiveType.OBJECT)
                        stream.write_vu32(
                            stream.greycat.type_offset_core_string)
                        for string in self:
                            if string is not None:
                                data = string.encode("utf8")
                                stream.write_vu32(len(data) << 1)
                                stream.write_i8_array(data, 0, len(data))
                    elif issubclass(unique_type, GreyCat.Object):
                        object = monotonic_value
                        object._save_type(stream)
                        for object in self:
                            if object is not None:
                                object._save(stream)
                    else:
                        raise Exception("wrong state")

            @staticmethod
            def load(type_: GreyCat.Type, stream: GreyCat._Stream) -> Any:
                size: int = stream.read_vu32()
                array: std_n.core._Array = type_.factory(type_, [])
                array.attributes = list(repeat(None, size))
                if 0 == size:
                    return array
                nullables: list[bool] | None = None
                if 1 == stream.read_i8():
                    nullables = list(repeat(False, size))
                    for offset in range(0, size, 8):
                        flags = stream.read_i8()
                        for flags_offset in range(min(size-offset, 8)):
                            nullables[offset +
                                      flags_offset] = 1 == (flags >> flags_offset & 1)
                array_primitive_type: int = stream.read_i8()
                array_type: GreyCat.Type | None = None
                monotonic_value: Any | None = None
                if PrimitiveType.OBJECT == array_primitive_type or PrimitiveType.STATIC_FIELD == array_primitive_type:
                    type_offset: int = stream.read_vu32()
                    if -1 != type_offset:
                        array_type = stream.greycat.types[type_offset]
                if PrimitiveType.OBJECT != array_primitive_type and PrimitiveType.UNDEFINED != array_primitive_type:
                    if 1 == stream.read_i8():
                        monotonic_value = GreyCat._Stream._PRIMITIVE_LOADERS[array_primitive_type](
                            stream)
                if PrimitiveType.UNDEFINED == array_primitive_type:
                    for offset in range(size):
                        array[offset] = None if nullables is not None and nullables[offset] else stream.read(
                        )
                elif PrimitiveType.OBJECT == array_primitive_type or (PrimitiveType.STATIC_FIELD == array_primitive_type and monotonic_value is None):
                    if array_type is None:
                        for offset in range(size):
                            # TODO: check for enums
                            array[offset] = None if nullables is not None and nullables[offset] else stream.read_object(
                            )
                    else:
                        for offset in range(size):
                            array[offset] = None if nullables is not None and nullables[offset] else array_type.loader(
                                array_type, stream)
                elif monotonic_value is None:
                    for offset in range(size):
                        array[offset] = None if nullables is not None and nullables[
                            offset] else GreyCat._Stream._PRIMITIVE_LOADERS[array_primitive_type](stream)
                else:
                    for offset in range(size):
                        array[offset] = monotonic_value
                return array

            def __len__(self) -> int:
                return len(self.attributes)

            def __iter__(self) -> Iterator[std_n.core.__T]:
                return self.attributes.__iter__()

            @overload
            def __getitem__(self, __i: SupportsIndex) -> std_n.core.__T:
                ...

            @overload
            def __getitem__(self, __s: slice) -> list[std_n.core.__T]:
                ...

            def __getitem__(self, __key):
                return self.attributes[__key]

            @overload
            def __setitem__(self, __key: SupportsIndex, __value: std_n.core.__T) -> None:
                pass

            @overload
            def __setitem__(self, __key: slice, __value: Iterable[std_n.core.__T]) -> None:
                pass

            def __setitem__(self, __key, __value):
                self.attributes[__key] = __value

            def __delitem__(self, __key: SupportsIndex | slice) -> None:
                del self.attributes[__key]

            def __contains__(self, __key: object) -> bool:
                return __key in self.attributes

            def __repr__(self) -> str:
                return self.attributes.__repr__()

            def __str__(self) -> str:
                return self.attributes.__str__()

            def append(self, __value) -> None:
                self.attributes.append(__value)

            def extend(self, __iterable: Iterable) -> None:
                self.attributes.extend(__iterable)

            @staticmethod
            def from_list(l: list, greycat: GreyCat | None = None) -> std_n.core._Array:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                array: std_n.core._Array = std_n.core._Array(
                    greycat.types_by_name["core::Array"])
                array.extend(l)
                return array

        class _Buffer(GreyCat.Object):
            def __init__(self, type: GreyCat.Type) -> None:
                self.data: bytes
                super().__init__(type, None)

            def _save(self, stream: GreyCat._Stream, type_offset: int | None = None) -> None:
                stream.write_vu32(len(self.data))
                stream.write_i8_array(self.data, 0, len(self.data))

            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat._Stream) -> Any:
                buf: std_n.util._Buffer = type.factory(type, [])
                buf.data = stream.read_i8_array(stream.read_vu32())
                return buf

        class _Date(GreyCat.Object):
            def __init__(self, type: GreyCat.Type) -> None:
                self.localized_epoch_s: int
                self.epoch_us: int
                self.time_zone: int
                super().__init__(type, None)

            @final
            def _save(self, stream: GreyCat._Stream, type_offset: int | None = None) -> None:
                stream.write_vi64(self.localized_epoch_s)
                stream.write_vi64(self.epoch_us)
                stream.write_vu32(self.time_zone)

            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat._Stream) -> Any:
                res: std_n.core._Date = type.factory(type, [])
                res.localized_epoch_s = stream.read_vi64()
                res.epoch_us = stream.read_vi64()
                res.time_zone = stream.read_vu32()
                return res

        class _Error(GreyCat.Object):
            def __init__(self, type: GreyCat.Type) -> None:
                self.code: int
                self.frames: list[std_n.core._Error.Frame]
                self.msg: str
                self.value: Any | None
                super().__init__(type, None)

            @final
            def _save(self, stream: GreyCat._Stream, type_offset: int | None = None) -> None:
                stream.write_vu32(c_uint32(self.code))
                stream.write_vu32(c_uint32(len(self.frames)))
                bs: Final[bytes] = self.msg.encode("utf-8")
                stream.write_vu32(c_uint32(len(bs)))
                offset: int
                frame: std_n.core._Error.Frame
                for offset in range(len(self.frames)):
                    frame = self.frames[offset]
                    stream.write_vu32(c_uint32(frame.mod_symbol))
                    stream.write_vu32(c_uint32(frame.type_symbol))
                    stream.write_vu32(c_uint32(frame.fn_symbol))
                    stream.write_vu32(c_uint32(frame.line))
                    stream.write_vu32(c_uint32(frame.column))
                stream.write_i8_array(bs, 0, len(bs))
                stream.write(self.value)

            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat._Stream) -> Any:
                code: Final[int] = stream.read_vu32().value
                frames_len: Final[int] = stream.read_vu32().value
                msg_len: Final[int] = stream.read_vu32().value
                frames: Final[list[std_n.core._Error.Frame]] = [
                    std_n.core._Error.Frame(
                        stream.read_vu32().value,  # mod_symbol
                        stream.read_vu32().value,  # type_symbol
                        stream.read_vu32().value,  # fn_symbol
                        stream.read_vu32().value,  # line
                        stream.read_vu32().value,  # column
                    )
                    for _ in repeat(None, frames_len)
                ]
                res: std_n.core._Error = type.factory(type, [])
                res.code = code
                res.frames = frames
                res.msg = stream.read_string(msg_len)
                res.value = stream.read()
                return res

            def __str__(self) -> str:
                return f"{self.type_.name}{{msg='{self.msg}', value={self.value}}}"

            class Frame:
                def __init__(
                    self,
                    mod_symbol: int,
                    type_symbol: int,
                    fn_symbol: int,
                    line: int,
                    column: int,
                ) -> None:
                    self.mod_symbol: Final[int] = mod_symbol
                    self.type_symbol: Final[int] = type_symbol
                    self.fn_symbol: Final[int] = fn_symbol
                    self.line: Final[int] = line
                    self.column: Final[int] = column

        class _Map(Generic[__T, __U], GreyCat.Object):
            def __init__(self, type: GreyCat.Type) -> None:
                self.map: Final[dict] = {}
                super().__init__(type, None)

            @final
            def _save(self, stream: GreyCat._Stream, type_offset: int | None = None) -> None:
                stream.write_vu32(len(self))
                key: std_n.core.__T
                value: std_n.core.__U
                key_type_offset: int | None = None
                value_type_offset: int | None = None
                if type_offset is not None:
                    type_: GreyCat.Type = stream.greycat.types[type_offset]
                    if 0 != type_.genericAbiType:
                        key_type_offset = type_.g1AbiTypeDesc >> 1
                        value_type_offset = type_.g2AbiTypeDesc >> 1
                for key, value in self.items():
                    stream.write(key, type_offset=key_type_offset)
                    stream.write(value, type_offset=value_type_offset)

            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat._Stream) -> Any:
                map: Final[std_n.core._Map] = type.factory(type, [])
                map_length: int = stream.read_vu32()
                key: Any
                for _ in range(map_length):
                    key = std_n.core._Map.__hashable(stream.read())
                    map[key] = stream.read()
                return map

            def keys(self) -> dict_keys[std_n.core.__T]:
                return self.map.keys()

            def values(self) -> dict_values[std_n.core.__U]:
                return self.map.values()

            def items(self) -> dict_items[std_n.core.__T, std_n.core.__U]:
                return self.map.items()

            def __len__(self) -> int:
                return len(self.map)

            def __getitem__(self, key: std_n.core.__T) -> std_n.core.__U:
                return self.map[key]

            def __setitem__(self, key: std_n.core.__T, value: std_n.core.__U) -> None:
                self.map[key] = value

            def __delitem__(self, key: std_n.core.__T) -> None:
                del self.map[key]

            def clear(self) -> None:
                self.map.clear()

            def __hashable(key: Any) -> Any:
                if type(key) in [c_char, c_int64, c_double, c_ubyte]:
                    return key.value
                return key

            def __str__(self) -> str:
                res: str = f"{self.type_.name}{{"
                if len(self) > 0:
                    res = f"{res}\n"
                for key, value in self.items():
                    res = f"{res}\t{key}: {value},\n"
                return f"{res}}}"

        class _String(GreyCat.Object):
            def __init__(self, type: GreyCat.Type) -> None:
                super().__init__(type, None)

            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat._Stream) -> Any:
                len_: int = stream.read_vu32()
                if 0 != (len_ & 1):
                    return type.greycat.symbols[len_ >> 1]
                return stream.read_string(len_ >> 1)

        # Table is implemented as a thin wrapper around numpy.ndarray with boilerplate to map elements types back and forth
        class _Table(Generic[__T], GreyCat.Object):
            def __init__(self, type: GreyCat.Type) -> None:
                self.data: numpy.ndarray
                super().__init__(type, None)

            @property
            def shape(self):
                return self.data.shape

            def __save_typed(self, stream: GreyCat._Stream, type_offset: int, type_nullable: bool) -> None:
                rows = self.data.shape[0]
                cols = self.data.shape[1]
                nullables: bytearray | None
                b: bool
                char: c_char
                c: c_ubyte
                i: int
                f: float
                o: GreyCat.Object
                for col in range(cols):
                    nullables = None
                    if type_nullable:
                        for row in range(rows):
                            e = self.data[row, col]
                            if e is None:
                                if nullables is None:
                                    nullables = bytearray(repeat(
                                        0,
                                        math.ceil(rows / 8)
                                    ))
                                nullables[row >> 3] |= 1 << (row & 7)
                        stream.write_i8(0 if nullables is None else 1)
                        if nullables is not None:
                            stream.write_i8_array(nullables, 0, len(nullables))
                    else:
                        stream.write_i8(0)
                    if stream.greycat.type_offset_core_bool == type_offset:
                        stream.write_i8(PrimitiveType.BOOL)
                        stream.write_i8(0)  # TODO: manage monotonic
                        if type_nullable:
                            for row in range(rows):
                                b = self.data[row, col]
                                if b is not None:
                                    stream.write_i8(1 if b else 0)
                        else:
                            for row in range(rows):
                                b = self.data[row, col]
                                stream.write_i8(1 if b else 0)
                    elif stream.greycat.type_offset_core_char == type_offset:
                        stream.write_i8(PrimitiveType.CHAR)
                        stream.write_i8(0)  # TODO: manage monotonic
                        if type_nullable:
                            for row in range(rows):
                                char = self.data[row, col]
                                if char is None:
                                    continue
                                c = c_ubyte(char.value)
                                if c > GreyCat._Stream.ASCII_MAX:
                                    raise ValueError(
                                        f"Only ASCII characters are allowed: {c}")
                                stream.write_i8(c)
                        else:
                            for row in range(rows):
                                char = self.data[row, col]
                                c = c_ubyte(char.value)
                                if c > GreyCat._Stream.ASCII_MAX:
                                    raise ValueError(
                                        f"Only ASCII characters are allowed: {c}")
                                stream.write_i8(c)
                    elif stream.greycat.type_offset_core_int == type_offset:
                        stream.write_i8(PrimitiveType.INT)
                        stream.write_i8(0)  # TODO: manage monotonic
                        if type_nullable:
                            for row in range(rows):
                                i = self.data[row, col]
                                if i is not None:
                                    stream.write_vi64(i)
                        else:
                            for row in range(rows):
                                i = self.data[row, col]
                                stream.write_vi64(i)
                    elif stream.greycat.type_offset_core_float == type_offset:
                        stream.write_i8(PrimitiveType.FLOAT)
                        stream.write_i8(0)  # TODO: manage monotonic
                        if type_nullable:
                            for row in range(rows):
                                f = self.data[row, col]
                                if f is not None:
                                    stream.write_f64(f)
                        else:
                            for row in range(rows):
                                f = self.data[row, col]
                                stream.write_f64(f)
                    else:
                        if stream.greycat.type_offset_core_node == type_offset:
                            stream.write_i8(PrimitiveType.NODE)
                            stream.write_i8(0)  # TODO: manage monotonic
                        elif stream.greycat.type_offset_core_node_time == type_offset:
                            stream.write_i8(PrimitiveType.NODE_TIME)
                            stream.write_i8(0)  # TODO: manage monotonic
                        elif stream.greycat.type_offset_core_node_index == type_offset:
                            stream.write_i8(PrimitiveType.NODE_INDEX)
                            stream.write_i8(0)  # TODO: manage monotonic
                        elif stream.greycat.type_offset_core_node_list == type_offset:
                            stream.write_i8(PrimitiveType.NODE_LIST)
                            stream.write_i8(0)  # TODO: manage monotonic
                        elif stream.greycat.type_offset_core_node_geo == type_offset:
                            stream.write_i8(PrimitiveType.NODE_GEO)
                            stream.write_i8(0)  # TODO: manage monotonic
                        elif stream.greycat.type_offset_core_geo == type_offset:
                            stream.write_i8(PrimitiveType.GEO)
                            stream.write_i8(0)  # TODO: manage monotonic
                        elif stream.greycat.type_offset_core_time == type_offset:
                            stream.write_i8(PrimitiveType.TIME)
                            stream.write_i8(0)  # TODO: manage monotonic
                        elif stream.greycat.type_offset_core_duration == type_offset:
                            stream.write_i8(PrimitiveType.DURATION)
                            stream.write_i8(0)  # TODO: manage monotonic
                        elif stream.greycat.type_offset_core_t2 == type_offset:
                            stream.write_i8(PrimitiveType.T2)
                            stream.write_i8(0)  # TODO: manage monotonic
                        elif stream.greycat.type_offset_core_t3 == type_offset:
                            stream.write_i8(PrimitiveType.T3)
                            stream.write_i8(0)  # TODO: manage monotonic
                        elif stream.greycat.type_offset_core_t4 == type_offset:
                            stream.write_i8(PrimitiveType.T4)
                            stream.write_i8(0)  # TODO: manage monotonic
                        elif stream.greycat.type_offset_core_t2f == type_offset:
                            stream.write_i8(PrimitiveType.T2F)
                            stream.write_i8(0)  # TODO: manage monotonic
                        elif stream.greycat.type_offset_core_t3f == type_offset:
                            stream.write_i8(PrimitiveType.T3F)
                            stream.write_i8(0)  # TODO: manage monotonic
                        elif stream.greycat.type_offset_core_t4f == type_offset:
                            stream.write_i8(PrimitiveType.T4F)
                            stream.write_i8(0)  # TODO: manage monotonic
                        # elif […] TODO: other types
                        else:
                            stream.write_i8(PrimitiveType.OBJECT)
                            stream.write_vu32(type_offset)
                        if type_nullable:
                            for row in range(rows):
                                o = self.data[row, col]
                                if o is not None:
                                    o._save(stream, type_offset)
                        else:
                            for row in range(rows):
                                o = self.data[row, col]
                                o._save(stream, type_offset)

            def _save(self, stream: GreyCat._Stream, type_offset: int | None = None) -> None:
                rows = self.data.shape[0]
                cols = self.data.shape[1]
                stream.write_vu32(rows)
                stream.write_vu32(cols)
                if type_offset is not None and 0 != stream.greycat.types[type_offset].genericAbiType:
                    g1AbiTypeDesc = stream.greycat.types[type_offset].g1AbiTypeDesc
                    self.__save_typed(stream, g1AbiTypeDesc >>
                                      1, 1 == g1AbiTypeDesc & 1)
                    return
                for col in range(cols):
                    nullables: bytearray | None = None
                    type_is_unique: bool = False
                    unique_type: type | None = None
                    value_is_monotonic:  bool = False
                    monotonic_value: Any | None = None
                    e: std_n.core.__T
                    for row in range(rows):
                        e = self.data[row, col]
                        if e is None:
                            if nullables is None:
                                nullables = bytearray(
                                    repeat(0, math.ceil(rows / 8)))
                            nullables[row >> 3] |= 1 << (row & 7)
                        else:
                            _type = type(e)
                            if unique_type is None:
                                type_is_unique = True
                                unique_type = _type
                            elif type_is_unique and unique_type is not _type:
                                type_is_unique = False
                            if monotonic_value is None:
                                value_is_monotonic = True
                                monotonic_value = e
                            elif value_is_monotonic and monotonic_value is not e:
                                value_is_monotonic = False
                    stream.write_i8(0 if nullables is None else 1)
                    if nullables is not None:
                        stream.write_i8_array(nullables, 0, len(nullables))
                    char: c_char
                    c: c_ubyte
                    string: str
                    object: GreyCat.Object
                    dt: numpy.datetime64
                    td: numpy.timedelta64
                    if not type_is_unique:
                        stream.write_i8(PrimitiveType.UNDEFINED)
                        for row in range(rows):
                            e = self.data[row, col]
                            if e is not None:
                                stream.write(std_n.core._Table.ser(
                                    e, self.type_.greycat))
                    else:
                        if issubclass(unique_type, (bool, numpy.bool_)):
                            stream.write_i8(PrimitiveType.BOOL)
                            stream.write_i8(0)  # TODO: manage monotonic
                            for row in range(rows):
                                e = self.data[row, col]
                                if e is not None:
                                    stream.write_bool(e)
                        elif c_char is unique_type:  # TODO: numpy.(u)byte?
                            stream.write_i8(PrimitiveType.CHAR)
                            stream.write_i8(0)  # TODO: manage monotonic
                            for row in range(rows):
                                char = self.data[row, col]
                                if char is not None:
                                    c = c_ubyte(char.value)
                                    if c > GreyCat._Stream.ASCII_MAX:
                                        raise ValueError(
                                            f"Only ASCII characters are allowed: {c}")
                                    stream.write_i8(c)
                        elif issubclass(unique_type, (int, numpy.integer)):
                            stream.write_i8(PrimitiveType.INT)
                            stream.write_i8(0)  # TODO: manage monotonic
                            for row in range(rows):
                                e = self.data[row, col]
                                if e is not None:
                                    stream.write_vi64(e)
                        elif issubclass(unique_type, (float, numpy.floating)):
                            stream.write_i8(PrimitiveType.FLOAT)
                            stream.write_i8(0)  # TODO: manage monotonic
                            if nullables is None and numpy.float64 is unique_type:
                                # GreyCat’s Array<float> is stored the exact same as numpy.array[float64]
                                stream.write_i8_array(
                                    self.data[:, col].data.tobytes(), 0, 8 * rows)
                            else:
                                for row in range(rows):
                                    e = self.data[row, col]
                                    if e is not None:
                                        stream.write_f64(e)
                        elif numpy.datetime64 is unique_type:
                            stream.write_i8(PrimitiveType.TIME)
                            stream.write_i8(0)  # TODO: manage monotonic
                            for row in range(rows):
                                dt = self.data[row, col]
                                if dt is not None:
                                    std_n.core._time.from_numpy(
                                        self.type_.greycat, dt)._save(stream)
                        elif numpy.timedelta64 is unique_type:
                            stream.write_i8(PrimitiveType.DURATION)
                            stream.write_i8(0)  # TODO: manage monotonic
                            for row in range(rows):
                                td = self.data[row, col]
                                if td is not None:
                                    std_n.core._duration.from_numpy(
                                        self.type_.greycat, td)._save(stream)
                        elif issubclass(unique_type, (str, numpy.str_)):
                            stream.write_i8(PrimitiveType.OBJECT)
                            stream.write_vu32(
                                stream.greycat.type_offset_core_string)
                            for row in range(rows):
                                string = self.data[row, col]
                                if string is not None:
                                    data = string.encode("utf8")
                                    stream.write_vu32(len(data) << 1)
                                    stream.write_i8_array(data, 0, len(data))
                        elif issubclass(unique_type, GreyCat.Object):
                            object = monotonic_value
                            object._save_type(stream)
                            for row in range(rows):
                                object = self.data[row, col]
                                if object is not None:
                                    object._save(stream)
                        else:
                            raise Exception("wrong state")

            @staticmethod
            def load(type_: GreyCat.Type, stream: GreyCat._Stream) -> Any:
                rows: Final[int] = stream.read_vu32()
                cols: Final[int] = stream.read_vu32()
                cols_data: list[list | numpy.ndarray] = []
                col_data: list
                nda: numpy.ndarray
                for col in range(cols):
                    # Read column metadata
                    nullables: list[bool] | None = None
                    if 1 == stream.read_i8():
                        nullables = list(repeat(False, rows))
                        for row in range(0, rows, 8):
                            flags = stream.read_i8()
                            for offset in range(min(rows - row, 8)):
                                nullables[
                                    row + offset
                                ] = 1 == (flags >> offset & 1)
                    col_primitive_type: int = stream.read_i8()
                    col_type: GreyCat.Type | None = None
                    monotonic_value: Any | None = None
                    if PrimitiveType.OBJECT == col_primitive_type or PrimitiveType.STATIC_FIELD == col_primitive_type:
                        type_offset: int = c_int32(stream.read_vu32()).value
                        if -1 != type_offset:
                            col_type = stream.greycat.types[type_offset]
                    if PrimitiveType.OBJECT != col_primitive_type and PrimitiveType.UNDEFINED != col_primitive_type:
                        if 1 == stream.read_i8():
                            monotonic_value = GreyCat._Stream._PRIMITIVE_LOADERS[col_primitive_type](
                                stream
                            )
                    # Read column data
                    if monotonic_value is not None or (nullables is not None and all(nullables)):
                        cols_data.append(numpy.array(
                            [monotonic_value] * rows)
                        )
                    elif PrimitiveType.FLOAT == col_primitive_type:
                        if nullables is None:
                            # GreyCat’s Array<float> is stored the exact same as numpy.array[float64]
                            cols_data.append(numpy.frombuffer(
                                stream.read_i8_array(8 * rows)
                            )),
                        else:
                            cols_data.append(numpy.array([
                                None if nullables[row]
                                else stream.read_f64()
                                for row in range(rows)
                            ]))
                    elif col_primitive_type in [PrimitiveType.TIME, PrimitiveType.DURATION]:
                        cols_data.append(numpy.array([
                            None if nullables is not None and nullables[row]
                            else GreyCat._Stream._PRIMITIVE_LOADERS[col_primitive_type](stream).to_numpy()
                            for row in range(rows)
                        ]))
                    elif PrimitiveType.UNDEFINED == col_primitive_type:
                        cols_data.append(numpy.array([
                            None if nullables is not None and nullables[row]
                            else std_n.core._Table.deser(stream.read())
                            for row in range(rows)
                        ], dtype=object))
                    elif PrimitiveType.OBJECT == col_primitive_type or PrimitiveType.STATIC_FIELD == col_primitive_type:
                        if col_type is None:
                            cols_data.append(numpy.array(
                                [
                                    None if nullables is not None and nullables[row]
                                    else stream.read_object()
                                    for row in range(rows)
                                ],
                                dtype=object
                            ))
                        else:
                            col_data = [
                                None if nullables is not None and nullables[row]
                                else col_type.loader(col_type, stream)
                                for row in range(rows)
                            ]
                            if 0 < rows and isinstance(col_data[0], (Sequence, std_n.core._Array)):
                                nda = numpy.empty(rows, dtype=object)
                                nda[:] = col_data
                                cols_data.append(nda)
                            else:
                                cols_data.append(numpy.array(
                                    col_data,
                                    dtype=object
                                ))
                    else:
                        cols_data.append(numpy.array([
                            None if nullables is not None and nullables[row]
                            else GreyCat._Stream._PRIMITIVE_LOADERS[col_primitive_type](stream)
                            for row in range(rows)
                        ]))
                table: std_n.core._Table = type_.factory(type_, [])
                if 0 == cols:
                    table.data = numpy.empty((rows, cols), order="F")
                else:
                    table.data = numpy.empty(
                        (rows, cols),
                        dtype=numpy.result_type(
                            *[col_data.dtype for col_data in cols_data]
                        ),
                        order="F"
                    )
                for col in range(cols):
                    table.data[:, col] = cols_data[col]
                return table

            def __repr__(self) -> str:
                return self.data.__repr__()

            def __str__(self) -> str:
                return self.data.__str__()

            def to_numpy(self) -> numpy.ndarray:
                return self.data

            @staticmethod
            def from_numpy(nda: numpy.ndarray, gc: GreyCat | None = None) -> std_n.core._Table:
                if gc is None:
                    gc = GreyCat._DEFAULT
                type_: GreyCat.Type = gc.types_by_name["core::Table"]
                table: std_n.core._Table = type_.factory(type_, [])
                table.data = nda
                return table

            @staticmethod
            def ser(value: Any, gc: GreyCat) -> Any:
                if isinstance(value, numpy.datetime64):
                    return std_n.core._time.from_numpy(gc, value)
                if isinstance(value, numpy.timedelta64):
                    return std_n.core._duration.from_numpy(gc, value)
                return value

            @staticmethod
            def deser(value: Any) -> Any:
                if isinstance(value, (std_n.core._time, std_n.core._duration)):
                    return value.to_numpy()
                return value

            if "pandas" in sys.modules:

                def to_pandas(self) -> pandas.DataFrame:
                    return pandas.DataFrame(self.data)

                @staticmethod
                def from_pandas(
                    df: pandas.DataFrame,
                    greycat: GreyCat | None = None,
                ) -> std_n.core._Table:
                    if greycat is None:
                        greycat = GreyCat._DEFAULT
                    return std_n.core._Table.from_numpy(greycat, df.to_numpy())

            if "tensorflow" in sys.modules:

                def to_tf_tensor(self) -> tensorflow.Tensor:
                    return tensorflow.constant(self.to_numpy())

                @staticmethod
                def from_tf_tensor(tf_tensor: tensorflow.Tensor, session: tensorflow.compat.v1.Session | None = None, greycat: GreyCat | None = None) -> std_n.core._Table:
                    if greycat is None:
                        greycat = GreyCat._DEFAULT
                    if tensorflow.executing_eagerly():
                        return std_n.core._Table.from_numpy(greycat, tf_tensor.numpy())
                    if session is not None:
                        return std_n.core._Table.from_numpy(greycat, session.run(tf_tensor))
                        # return std_n.core._Table.from_numpy(greycat, tensorflow.compat.v1.Session().run(tf_tensor))

        class _Tensor(GreyCat.Object):
            def __init__(self, type: GreyCat.Type) -> None:
                self.shape: list[int]
                self.tensor_type: c_byte
                self.size: int
                self.data: bytes
                self.dtype: greycat.core.TensorType
                self.format: str
                super().__init__(type, None)

            @final
            def _save(self, stream: GreyCat._Stream, type_offset: int | None = None) -> None:
                stream.write_i8(c_byte(len(self.shape)))
                stream.write_i8(self.tensor_type)
                dim: c_uint32
                for dim in self.shape:
                    stream.write_i64(dim)
                stream.write_i64(self.size)
                stream.write_i8_array(self.data)

            @staticmethod
            def load(type_: GreyCat.Type, stream: GreyCat._Stream) -> Any:
                nb_dim: Final[int] = stream.read_i8()
                tensor_type: Final[c_byte] = stream.read_i8()
                shape: list[int] = [stream.read_i64()
                                         for _ in repeat(None, nb_dim)]
                size: int = stream.read_i64()
                dtype: greycat.core.TensorType = type_.greycat.types_by_name[greycat.core.TensorType.name_].enum_values[tensor_type]
                format_: str
                if dtype == greycat.core.TensorType[("i32", type_.greycat)]:
                    format_ = "=i"
                elif dtype == greycat.core.TensorType[("i64", type_.greycat)]:
                    format_ = "=q"
                elif dtype == greycat.core.TensorType[("f32", type_.greycat)]:
                    format_ = "=f"
                elif dtype == greycat.core.TensorType[("f64", type_.greycat)]:
                    format_ = "=d"
                elif dtype == greycat.core.TensorType[("c64", type_.greycat)]:
                    format_ = "=ff"
                elif dtype == greycat.core.TensorType[("c128", type_.greycat)]:
                    format_ = "=dd"
                else:
                    raise ValueError(f"${tensor_type}")
                bin_size: int = size * dtype.value
                res: std_n.core._Tensor = type_.factory(type_, [])
                res.shape = shape
                res.tensor_type = tensor_type
                res.dtype = dtype
                res.format = format_
                res.size = size
                res.data = stream.read_i8_array(bin_size)
                return res

            def __getitem__(self, key: Iterable[int]):
                offset: int = 0
                index: int
                dim_key: int
                for index, dim_key in enumerate(key):
                    if index < len(self.shape) - 1:
                        offset += dim_key * \
                            sum(dim for dim in self.shape[index + 1:])
                    else:
                        offset += dim_key
                unpacked: Tuple = unpack(self.format, self.data[slice(
                    offset * self.dtype.value, (offset + 1) * self.dtype.value)])
                if self.dtype in [greycat.core.TensorType[("c64", self.type_.greycat)], greycat.core.TensorType[("c128", self.type_.greycat)]]:
                    return unpacked
                return unpacked[0]

            def to_numpy(self) -> numpy.ndarray:
                dtype: numpy.dtype
                if self.dtype == greycat.core.TensorType[("i32", self.type_.greycat)]:
                    dtype = numpy.dtype('int32')
                elif self.dtype == greycat.core.TensorType[("i64", self.type_.greycat)]:
                    dtype = numpy.dtype('int64')
                elif self.dtype == greycat.core.TensorType[("f32", self.type_.greycat)]:
                    dtype = numpy.dtype('float32')
                elif self.dtype == greycat.core.TensorType[("f64", self.type_.greycat)]:
                    dtype = numpy.dtype('float64')
                elif self.dtype == greycat.core.TensorType[("c64", self.type_.greycat)]:
                    dtype = numpy.dtype('complex64')
                elif self.dtype == greycat.core.TensorType[("c128", self.type_.greycat)]:
                    dtype = numpy.dtype('complex128')
                else:
                    raise ValueError(f"${self.tensor_type}")
                return numpy.frombuffer(self.data, dtype=dtype).reshape([dim for dim in self.shape])

            @staticmethod
            def from_numpy(greycat_: GreyCat, nda: numpy.ndarray) -> std_n.core._Table:
                if nda.dtype in (numpy.dtype('int8'), numpy.dtype('int16')):
                    nda = nda.astype(numpy.dtype('int32'))
                elif nda.dtype == numpy.dtype('float16'):
                    nda = nda.astype(numpy.dtype('float32'))
                elif nda.dtype == numpy.dtype('float128'):
                    nda = nda.astype(numpy.dtype('float64'))
                elif nda.dtype == numpy.dtype('complex256'):
                    nda = nda.astype(numpy.dtype('complex128'))
                dtype: greycat.core.TensorType
                format_: str
                if nda.dtype == numpy.dtype('int32'):
                    dtype = greycat.core.TensorType[("i32", greycat_)]
                    format_ = "=i"
                elif nda.dtype == numpy.dtype('int64'):
                    dtype = greycat.core.TensorType[("i64", greycat_)]
                    format_ = "=q"
                elif nda.dtype == numpy.dtype('float32'):
                    dtype = greycat.core.TensorType[("f32", greycat_)]
                    format_ = "=f"
                elif nda.dtype == numpy.dtype('float64'):
                    dtype = greycat.core.TensorType[("f64", greycat_)]
                    format_ = "=d"
                elif nda.dtype == numpy.dtype('complex64'):
                    dtype = greycat.core.TensorType[("c64", greycat_)]
                    format_ = "=ff"
                elif nda.dtype == numpy.dtype('complex128'):
                    dtype = greycat.core.TensorType[("c128", greycat_)]
                    format_ = "=dd"
                else:
                    raise ValueError(
                        f"Only int, float and complex dtypes are allowed: {nda.dtype}")
                type_: GreyCat.Type = greycat_.types_by_name["core::Tensor"]
                tensor: std_n.core._Tensor = type_.factory(type_, None)
                tensor.shape = [c_uint32(dim) for dim in nda.shape]
                tensor.tensor_type = c_byte(dtype.offset)
                tensor.dtype = dtype
                tensor.format = format_
                tensor.data = nda.tobytes()
                tensor.size = len(tensor.data)
                return tensor

            if "tensorflow" in sys.modules:
                def to_tf_tensor(self) -> tensorflow.Tensor:
                    dtype: numpy.dtype
                    if self.dtype == greycat.core.TensorType[("i32", self.type_.greycat)]:
                        dtype = numpy.dtype('int32')
                    elif self.dtype == greycat.core.TensorType[("i64", self.type_.greycat)]:
                        dtype = numpy.dtype('int64')
                    elif self.dtype == greycat.core.TensorType[("f32", self.type_.greycat)]:
                        dtype = numpy.dtype('float32')
                    elif self.dtype == greycat.core.TensorType[("f64", self.type_.greycat)]:
                        dtype = numpy.dtype('float64')
                    elif self.dtype == greycat.core.TensorType[("c64", self.type_.greycat)]:
                        dtype = numpy.dtype('complex64')
                    elif self.dtype == greycat.core.TensorType[("c128", self.type_.greycat)]:
                        dtype = numpy.dtype('complex128')
                    else:
                        raise ValueError(f"${self.tensor_type}")
                    return tensorflow.constant(numpy.frombuffer(self.data, dtype=dtype), [dim for dim in self.shape])

                @staticmethod
                def from_tf_tensor(tf_tensor: tensorflow.Tensor, tf_session: tensorflow.compat.v1.Session | None = None, greycat: GreyCat | None = None) -> std_n.core._Tensor:
                    if greycat is None:
                        greycat = GreyCat._DEFAULT
                    if tensorflow.executing_eagerly():
                        return std_n.core._Tensor.from_numpy(greycat, tf_tensor.numpy())
                    if tf_session is not None:
                        return std_n.core._Tensor.from_numpy(greycat, tf_session.run(tf_tensor))
                    return std_n.core._Tensor.from_numpy(greycat, tensorflow.compat.v1.Session().run(tf_tensor))

            if "torch" in sys.modules:
                def to_torch_tensor(self, requires_grad: bool = False) -> torch.Tensor:
                    dtype: torch.dtype
                    if self.dtype == greycat.core.TensorType[("i32", self.type_.greycat)]:
                        dtype = torch.int32
                    elif self.dtype == greycat.core.TensorType[("i64", self.type_.greycat)]:
                        dtype = torch.int64
                    elif self.dtype == greycat.core.TensorType[("f32", self.type_.greycat)]:
                        dtype = torch.float32
                    elif self.dtype == greycat.core.TensorType[("f64", self.type_.greycat)]:
                        dtype = torch.float64
                    elif self.dtype == greycat.core.TensorType[("c64", self.type_.greycat)]:
                        dtype = torch.complex64
                    elif self.dtype == greycat.core.TensorType[("c128", self.type_.greycat)]:
                        dtype = torch.complex128
                    else:
                        raise ValueError(f"${self.tensor_type}")
                    return torch.frombuffer(self.data, dtype=dtype, requires_grad=requires_grad).reshape([dim for dim in self.shape])

                @staticmethod
                def from_torch_tensor(greycat_: GreyCat, torch_tensor: torch.Tensor) -> std_n.core._Table:
                    if torch_tensor.dtype in (torch.uint8, torch.int8, torch.int16):
                        torch_tensor = torch_tensor.type(torch.int32)
                    if torch_tensor.dtype in (torch.bfloat16, torch.float16):
                        torch_tensor = torch_tensor.type(torch.float32)
                    if torch_tensor.dtype == torch.complex32:
                        torch_tensor = torch_tensor.type(torch.complex64)
                    dtype: greycat.core.TensorType
                    format_: str
                    if torch_tensor.dtype == torch.int32:
                        dtype = greycat.core.TensorType[("i32", greycat_)]
                        format_ = "=i"
                    elif torch_tensor.dtype == torch.int64:
                        dtype = greycat.core.TensorType[("i64", greycat_)]
                        format_ = "=q"
                    elif torch_tensor.dtype == torch.float32:
                        dtype = greycat.core.TensorType[("f32", greycat_)]
                        format_ = "=f"
                    elif torch_tensor.dtype == torch.float64:
                        dtype = greycat.core.TensorType[("f64", greycat_)]
                        format_ = "=d"
                    elif torch_tensor.dtype == torch.complex64:
                        dtype = greycat.core.TensorType[("c64", greycat_)]
                        format_ = "=ff"
                    elif torch_tensor.dtype == torch.complex128:
                        dtype = greycat.core.TensorType[("c128", greycat_)]
                        format_ = "=dd"
                    else:
                        raise ValueError(
                            f"Only int, float and complex dtypes are allowed: {torch_tensor.dtype}")
                    type_: GreyCat.Type = greycat_.types_by_name["core::Tensor"]
                    tensor: std_n.core._Tensor = type_.factory(type_, None)
                    tensor.shape = [c_uint32(dim) for dim in tensor.shape]
                    tensor.tensor_type = c_byte(dtype.offset)
                    tensor.dtype = dtype
                    tensor.format = format_
                    tensor.data = bytes(
                        torch_tensor.flatten().view(torch.uint8))
                    tensor.size = len(tensor.data)
                    return tensor

        class _nodeIndexBucket(GreyCat.Object):
            def __init__(type: GreyCat.Type) -> None:
                super().__init__(type, None)

            @final
            def _save(self, stream: GreyCat._Stream, type_offset: int | None = None) -> None:
                attribute: Any
                if self.attributes is None:
                    stream.write_i32(0)
                else:
                    stream.write_i32(len(self.attributes))
                    for attribute in self.attributes:
                        stream.write(attribute)

            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat._Stream) -> Any:
                size: Final[int] = stream.read_i32().value
                data: Final[list[Any]] = [stream.read()
                                          for _ in repeat(None, size)]
                res: std_n.core._nodeIndexBucket = type.factory(type, [])
                res.attributes = data
                return res

        __B_2D: list[int] = [
            0x5555555555555555,
            0x3333333333333333,
            0x0F0F0F0F0F0F0F0F,
            0x00FF00FF00FF00FF,
            0x0000FFFF0000FFFF,
            0x00000000FFFFFFFF,
        ]
        __S_2D: list[int] = [0, 1, 2, 4, 8, 16]

        @staticmethod
        def _interleave64_2d(x: int, y: int) -> int:
            x = (x | (x << std_n.core.__S_2D[5])) & std_n.core.__B_2D[4]
            y = (y | (y << std_n.core.__S_2D[5])) & std_n.core.__B_2D[4]

            x = (x | (x << std_n.core.__S_2D[4])) & std_n.core.__B_2D[3]
            y = (y | (y << std_n.core.__S_2D[4])) & std_n.core.__B_2D[3]

            x = (x | (x << std_n.core.__S_2D[3])) & std_n.core.__B_2D[2]
            y = (y | (y << std_n.core.__S_2D[3])) & std_n.core.__B_2D[2]

            x = (x | (x << std_n.core.__S_2D[2])) & std_n.core.__B_2D[1]
            y = (y | (y << std_n.core.__S_2D[2])) & std_n.core.__B_2D[1]

            x = (x | (x << std_n.core.__S_2D[1])) & std_n.core.__B_2D[0]
            y = (y | (y << std_n.core.__S_2D[1])) & std_n.core.__B_2D[0]

            return x | (y << 1)

        @staticmethod
        def _deinterleave64_2d(interleaved: int) -> int:
            x: int = interleaved
            y: int = interleaved >> 1

            x = (x | (x >> std_n.core.__S_2D[0])) & std_n.core.__B_2D[0]
            y = (y | (y >> std_n.core.__S_2D[0])) & std_n.core.__B_2D[0]

            x = (x | (x >> std_n.core.__S_2D[1])) & std_n.core.__B_2D[1]
            y = (y | (y >> std_n.core.__S_2D[1])) & std_n.core.__B_2D[1]

            x = (x | (x >> std_n.core.__S_2D[2])) & std_n.core.__B_2D[2]
            y = (y | (y >> std_n.core.__S_2D[2])) & std_n.core.__B_2D[2]

            x = (x | (x >> std_n.core.__S_2D[3])) & std_n.core.__B_2D[3]
            y = (y | (y >> std_n.core.__S_2D[3])) & std_n.core.__B_2D[3]

            x = (x | (x >> std_n.core.__S_2D[4])) & std_n.core.__B_2D[4]
            y = (y | (y >> std_n.core.__S_2D[4])) & std_n.core.__B_2D[4]

            x = (x | (x >> std_n.core.__S_2D[5])) & std_n.core.__B_2D[5]
            y = (y | (y >> std_n.core.__S_2D[5])) & std_n.core.__B_2D[5]

            return x | (y << 32)

        __B_3D: list[int] = [
            0x1249249249249249,
            0x10C30C30C30C30C3,
            0x100F00F00F00F00F,
            0x001F0000FF0000FF,
            0xFFFF00000000FFFF,
            0x00000000001FFFFF,
        ]
        __S_3D: list[int] = [2, 4, 8, 16, 32]

        @staticmethod
        def _interleave64_3d(x: int, y: int, z: int) -> int:
            x &= std_n.core.__B_3D[5]
            x = (x ^ (x << std_n.core.__S_3D[4])) & std_n.core.__B_3D[4]
            x = (x ^ (x << std_n.core.__S_3D[3])) & std_n.core.__B_3D[3]
            x = (x ^ (x << std_n.core.__S_3D[2])) & std_n.core.__B_3D[2]
            x = (x ^ (x << std_n.core.__S_3D[1])) & std_n.core.__B_3D[1]
            x = (x ^ (x << std_n.core.__S_3D[0])) & std_n.core.__B_3D[0]

            y &= std_n.core.__B_3D[5]
            y = (y ^ (y << std_n.core.__S_3D[4])) & std_n.core.__B_3D[4]
            y = (y ^ (y << std_n.core.__S_3D[3])) & std_n.core.__B_3D[3]
            y = (y ^ (y << std_n.core.__S_3D[2])) & std_n.core.__B_3D[2]
            y = (y ^ (y << std_n.core.__S_3D[1])) & std_n.core.__B_3D[1]
            y = (y ^ (y << std_n.core.__S_3D[0])) & std_n.core.__B_3D[0]

            z &= std_n.core.__B_3D[5]
            z = (z ^ (z << std_n.core.__S_3D[4])) & std_n.core.__B_3D[4]
            z = (z ^ (z << std_n.core.__S_3D[3])) & std_n.core.__B_3D[3]
            z = (z ^ (z << std_n.core.__S_3D[2])) & std_n.core.__B_3D[2]
            z = (z ^ (z << std_n.core.__S_3D[1])) & std_n.core.__B_3D[1]
            z = (z ^ (z << std_n.core.__S_3D[0])) & std_n.core.__B_3D[0]

            return x | (y << 1) | (z << 2)

        @staticmethod
        def _deinterleave64_3d(interleaved: int) -> int:
            x: int = interleaved & std_n.core.__B_3D[0]
            x = (x ^ (x >> std_n.core.__S_3D[0])) & std_n.core.__B_3D[1]
            x = (x ^ (x >> std_n.core.__S_3D[1])) & std_n.core.__B_3D[2]
            x = (x ^ (x >> std_n.core.__S_3D[2])) & std_n.core.__B_3D[3]
            x = (x ^ (x >> std_n.core.__S_3D[3])) & std_n.core.__B_3D[4]
            x = (x ^ (x >> std_n.core.__S_3D[4])) & std_n.core.__B_3D[5]
            return x

        __B_5D: list[int] = [
            0x0084210842108421,
            0x000C0300C0300C03,
            0x00000F0000F0000F,
            0x0000FF00000000FF,
            0x0000000000000FFF,
        ]
        __S_5D: list[int] = [4, 8, 16, 32]

        @staticmethod
        def _interleave64_5d(x0: int, x1: int, x2: int, x3: int, x4: int) -> c_int64:
            x0 &= std_n.core.__B_5D[4]
            x0 = (x0 ^ (x0 << std_n.core.__S_5D[3])) & std_n.core.__B_5D[3]
            x0 = (x0 ^ (x0 << std_n.core.__S_5D[2])) & std_n.core.__B_5D[2]
            x0 = (x0 ^ (x0 << std_n.core.__S_5D[1])) & std_n.core.__B_5D[1]
            x0 = (x0 ^ (x0 << std_n.core.__S_5D[0])) & std_n.core.__B_5D[0]

            x1 &= std_n.core.__B_5D[4]
            x1 = (x1 ^ (x1 << std_n.core.__S_5D[3])) & std_n.core.__B_5D[3]
            x1 = (x1 ^ (x1 << std_n.core.__S_5D[2])) & std_n.core.__B_5D[2]
            x1 = (x1 ^ (x1 << std_n.core.__S_5D[1])) & std_n.core.__B_5D[1]
            x1 = (x1 ^ (x1 << std_n.core.__S_5D[0])) & std_n.core.__B_5D[0]

            x2 &= std_n.core.__B_5D[4]
            x2 = (x2 ^ (x2 << std_n.core.__S_5D[3])) & std_n.core.__B_5D[3]
            x2 = (x2 ^ (x2 << std_n.core.__S_5D[2])) & std_n.core.__B_5D[2]
            x2 = (x2 ^ (x2 << std_n.core.__S_5D[1])) & std_n.core.__B_5D[1]
            x2 = (x2 ^ (x2 << std_n.core.__S_5D[0])) & std_n.core.__B_5D[0]

            x3 &= std_n.core.__B_5D[4]
            x3 = (x3 ^ (x3 << std_n.core.__S_5D[3])) & std_n.core.__B_5D[3]
            x3 = (x3 ^ (x3 << std_n.core.__S_5D[2])) & std_n.core.__B_5D[2]
            x3 = (x3 ^ (x3 << std_n.core.__S_5D[1])) & std_n.core.__B_5D[1]
            x3 = (x3 ^ (x3 << std_n.core.__S_5D[0])) & std_n.core.__B_5D[0]

            x4 &= std_n.core.__B_5D[4]
            x4 = (x4 ^ (x4 << std_n.core.__S_5D[3])) & std_n.core.__B_5D[3]
            x4 = (x4 ^ (x4 << std_n.core.__S_5D[2])) & std_n.core.__B_5D[2]
            x4 = (x4 ^ (x4 << std_n.core.__S_5D[1])) & std_n.core.__B_5D[1]
            x4 = (x4 ^ (x4 << std_n.core.__S_5D[0])) & std_n.core.__B_5D[0]

            return c_int64(x0 | (x1 << 1) | (x2 << 2) | (x3 << 3) | (x4 << 4))

        @staticmethod
        def _deinterleave64_5d(interleaved: int) -> int:
            x: int = interleaved & std_n.core.__B_5D[0]
            x = (x ^ (x >> std_n.core.__S_5D[0])) & std_n.core.__B_5D[1]
            x = (x ^ (x >> std_n.core.__S_5D[1])) & std_n.core.__B_5D[2]
            x = (x ^ (x >> std_n.core.__S_5D[2])) & std_n.core.__B_5D[3]
            x = (x ^ (x >> std_n.core.__S_5D[3])) & std_n.core.__B_5D[4]
            return x

    class util:
        __T = TypeVar("__T")

        class _Gaussian(GreyCat.Object):
            def __init__(self, type: GreyCat.Type) -> None:
                self.sum: c_double
                self.sum_sq: c_double
                self.size: c_int64
                self.nb_accepted: c_int64
                self.nb_rejected: c_int64
                self.nb_null: c_int64
                self.min: c_double
                self.max: c_double
                self.min_bound: c_double
                self.max_bound: c_double
                super().__init__(type, None)

            def _save(self, stream: GreyCat._Stream, type_offset: int | None = None) -> None:
                stream.write_f64(self.sum)
                stream.write_f64(self.sum_sq)
                stream.write_vi64(self.size)
                stream.write_vi64(self.nb_accepted)
                stream.write_vi64(self.nb_rejected)
                stream.write_vi64(self.nb_null)
                stream.write_f64(self.min)
                stream.write_f64(self.max)
                stream.write_f64(self.min_bound)
                stream.write_f64(self.max_bound)

            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat._Stream) -> Any:
                g: std_n.util._Gaussian = type.factory(type)
                g.sum = stream.read_f64()
                g.sum_sq = stream.read_f64()
                g.size = stream.read_vi64()
                g.nb_accepted = stream.read_vi64()
                g.nb_rejected = stream.read_vi64()
                g.nb_null = stream.read_vi64()
                g.min = stream.read_f64()
                g.max = stream.read_f64()
                g.min_bound = stream.read_f64()
                g.max_bound = stream.read_f64
                return g

        class _ProgressTracker(GreyCat.Object):
            pass
