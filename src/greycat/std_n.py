from __future__ import annotations

from _collections_abc import dict_keys, dict_values, dict_items
from collections import deque
from ctypes import *
from itertools import repeat
from numbers import Number
from struct import pack, unpack
import sys
from types import MappingProxyType
from typing import *

try:
    import numpy
except ModuleNotFoundError:
    pass

if "numpy" in sys.modules:
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

        class _node(Generic[__T], GreyCat.Object):
            def __init__(self, type: GreyCat.Type) -> None:
                self.ref: c_uint64
                super().__init__(type, None)

            @final
            def _save_type(self, stream: GreyCat._Stream) -> None:
                stream.write_i8(PrimitiveType.NODE)

            @final
            def _save(self, stream: GreyCat._Stream) -> None:
                stream.write_vu64(self.ref)

            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat._Stream) -> Any:
                res: std_n.core._node = type.factory(type, [])
                res.ref = stream.read_vu64()
                return res

        class _nodeTime(Generic[__T], GreyCat.Object):
            def __init__(self, type: GreyCat.Type) -> None:
                self.ref: c_uint64
                super().__init__(type, None)

            @final
            def _save_type(self, stream: GreyCat._Stream) -> None:
                stream.write_i8(PrimitiveType.NODE_TIME)

            @final
            def _save(self, stream: GreyCat._Stream) -> None:
                stream.write_vu64(self.ref)

            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat._Stream) -> Any:
                res: std_n.core._nodeTime = type.factory(type, [])
                res.ref = stream.read_vu64()
                return res

        class _nodeIndex(Generic[__T, __U], GreyCat.Object):
            def __init__(self, type: GreyCat.Type) -> None:
                self.ref: c_uint64
                super().__init__(type, None)

            @final
            def _save_type(self, stream: GreyCat._Stream) -> None:
                stream.write_i8(PrimitiveType.NODE_INDEX)

            @final
            def _save(self, stream: GreyCat._Stream) -> None:
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
            def _save_type(self, stream: GreyCat._Stream) -> None:
                stream.write_i8(PrimitiveType.NODE_LIST)

            @final
            def _save(self, stream: GreyCat._Stream) -> None:
                stream.write_vu64(self.ref)

            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat._Stream) -> Any:
                res: std_n.core._nodeList = type.factory(type, [])
                res.ref = stream.read_vu64()
                return res

        class _nodeGeo(Generic[__T], GreyCat.Object):
            def __init__(self, type: GreyCat.Type) -> None:
                self.ref: c_uint64
                super().__init__(type, None)

            @final
            def _save_type(self, stream: GreyCat._Stream) -> None:
                stream.write_i8(PrimitiveType.NODE_GEO)

            @final
            def _save(self, stream: GreyCat._Stream) -> None:
                stream.write_vu64(self.ref)

            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat._Stream) -> Any:
                res: std_n.core._nodeGeo = type.factory(type, [])
                res.ref = stream.read_vu64()
                return res

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
                self.geocode: c_int64
                self.lat: float
                self.lng: float
                super().__init__(type, None)
                if lat is not None and lng is not None:
                    self.geocode = std_n.core._geo.__encode(lat, lng)
                    self.lat = lat
                    self.lns = lng

            @final
            def _save_type(self, stream: GreyCat._Stream) -> None:
                stream.write_i8(PrimitiveType.GEO)

            @final
            def _save(self, stream: GreyCat._Stream) -> None:
                stream.write_i64(self.geocode)

            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat._Stream) -> Any:
                geo: std_n.core._geo = type.factory(type, [])
                value: c_int64 = stream.read_i64()
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
            def __interleave64(xlo: int, ylo: int) -> c_int64:
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
            def __deinterleave64(interleaved: c_int64) -> tuple[int, int]:
                B: list[int] = [
                    6148914691236517205,
                    3689348814741910323,
                    1085102592571150095,
                    71777214294589695,
                    281470681808895,
                    4294967295,
                ]
                S: list[int] = [0, 1, 2, 4, 8, 16]
                x: int = interleaved.value
                y: int = interleaved.value >> 1
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
            def __encode(latitude: float, longitude: float) -> c_int64:
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

        class _time(GreyCat.Object):
            def __init__(self, type: GreyCat.Type) -> None:
                self.value: c_int64
                super().__init__(type, None)

            @final
            def _save_type(self, stream: GreyCat._Stream) -> None:
                stream.write_i8(PrimitiveType.TIME)

            @final
            def _save(self, stream: GreyCat._Stream) -> None:
                stream.write_vi64(self.value)

            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat._Stream) -> Any:
                res: std_n.core._time = type.factory(type, [])
                res.value = stream.read_vi64()
                return res

            if "numpy" in sys.modules:
                def to_numpy(self) -> numpy.datetime64:
                    return numpy.datetime64(self.value.value, "us")

                @staticmethod
                def from_numpy(greycat: GreyCat, dt: numpy.datetime64) -> std_n.core._time:
                    time = std_n.core._time(
                        greycat.types[greycat.type_offset_core_time])
                    time.value = c_int64(dt.astype(int)) if numpy.datetime_data(dt)[0] in [
                        "us", "μs"] else c_int64(dt.astype("datetime64[us]").astype(int))
                    return time

            def __str__(self) -> str:
                return f"time{{timestamp: {int(self.value.value / 1_000_000)}, us_offset: {self.value.value % 1_000_000}}}"

        class _duration(GreyCat.Object):
            def __init__(self, type: GreyCat.Type) -> None:
                self.value: c_int64
                super().__init__(type, None)

            @final
            def _save_type(self, stream: GreyCat._Stream) -> None:
                stream.write_i8(PrimitiveType.DURATION)

            @final
            def _save(self, stream: GreyCat._Stream) -> None:
                stream.write_vi64(self.value)

            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat._Stream) -> Any:
                res: std_n.core._duration = type.factory(type, [])
                res.value = stream.read_vi64()
                return res

            if "numpy" in sys.modules:
                def to_numpy(self) -> numpy.timedelta64:
                    return numpy.timedelta64(self.value.value, "us")

                @staticmethod
                def from_numpy(greycat: GreyCat, td: numpy.timedelta64) -> std_n.core._duration:
                    duration = std_n.core._duration(
                        greycat.type_offset_core_duration)
                    duration.value = c_int64(td.astype(int)) if numpy.datetime_data(td)[0] in [
                        "us", "μs"] else c_int64(td.astype("timedelta64[us]").astype(int))
                    return duration

        class _ti2d(GreyCat.Object):
            _INT32_MIN: int = -2147483648
            _UINT32_MIN: int = 2147483648

            def __init__(self, type: GreyCat.Type) -> None:
                self.x0: int
                self.x1: int
                super().__init__(type, None)

            @final
            def _save_type(self, stream: GreyCat._Stream) -> None:
                stream.write_i8(PrimitiveType.TU2D)

            @final
            def _save(self, stream: GreyCat._Stream) -> None:
                stream.write_i64(self.__interleave())

            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat._Stream) -> Any:
                res: std_n.core._ti2d = type.factory(type, [])
                res.__deinterleave(stream.read_i64())
                return res

            def __str__(self) -> str:
                return f"ti2d{{x0={self.x0},x1={self.x1}}}"

            def __interleave(self) -> c_int64:
                return std_n.core._interleave64_2d(
                    self.x0 + std_n.core._ti2d._UINT32_MIN,
                    self.x1 + std_n.core._ti2d._UINT32_MIN,
                )

            def __deinterleave(self, interleaved: c_int64) -> None:
                dc: int = std_n.core._deinterleave64_2d(interleaved)
                self.x0 = c_int32(dc + std_n.core._ti2d._INT32_MIN).value
                self.x1 = c_int32(
                    (dc >> 32) + std_n.core._ti2d._INT32_MIN).value

        class _ti3d(GreyCat.Object):
            _INT21_MIN: int = -1048575 - 1
            __INT21_MAX: int = 1048575
            _UINT21_MIN: int = 4293918720

            def __init__(self, type: GreyCat.Type) -> None:
                self.x0: int
                self.x1: int
                self.x2: int
                super().__init__(type, None)

            @final
            def _save_type(self, stream: GreyCat._Stream) -> None:
                stream.write_i8(PrimitiveType.TU3D)

            @final
            def _save(self, stream: GreyCat._Stream) -> None:
                stream.write_i64(self.__interleave())

            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat._Stream) -> Any:
                res: std_n.core._ti3d = type.factory(type, [])
                res.__deinterleave(stream.read_i64())
                return res

            def __str__(self) -> str:
                return f"ti3d{{x0={self.x0},x1={self.x1},x2={self.x2}}}"

            def __interleave(self) -> c_int64:
                return std_n.core._interleave64_3d(
                    self.x0 + std_n.core._ti3d._UINT21_MIN,
                    self.x1 + std_n.core._ti3d._UINT21_MIN,
                    self.x2 + std_n.core._ti3d._UINT21_MIN,
                )

            def __deinterleave(self, interleaved: c_int64) -> None:
                B: list[int] = [
                    0x10C30C30C30C30C3,
                    0x100F00F00F00F00F,
                    0x001F0000FF0000FF,
                    0xFFFF00000000FFFF,
                    0x0001FFFFF,
                ]
                S: list[int] = [2, 4, 8, 16, 32]

                self.x0 = (
                    std_n.core._deinterleave64_3d(interleaved)
                    + std_n.core._ti3d._INT21_MIN
                )
                self.x1 = (
                    std_n.core._deinterleave64_3d(
                        c_int64(interleaved.value >> 1))
                    + std_n.core._ti3d._INT21_MIN
                )
                self.x2 = (
                    std_n.core._deinterleave64_3d(
                        c_int64(interleaved.value >> 2))
                    + std_n.core._ti3d._INT21_MIN
                )

        class _ti4d(GreyCat.Object):
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
            def _save_type(self, stream: GreyCat._Stream) -> None:
                stream.write_i8(PrimitiveType.TU4D)

            @final
            def _save(self, stream: GreyCat._Stream) -> None:
                stream.write_i64(self.__interleave())

            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat._Stream) -> Any:
                res: std_n.core._ti4d = type.factory(type, [])
                res.__deinterleave(stream.read_i64())
                return res

            def __str__(self) -> str:
                return f"ti4d{{x0={self.x0},x1={self.x1},x2={self.x2},x3={self.x3}}}"

            def __interleave(self) -> c_int64:
                return std_n.core._interleave64_2d(
                    std_n.core._interleave64_2d(
                        self.x0 + std_n.core._ti4d._UINT16_MIN,
                        self.x2 + std_n.core._ti4d._UINT16_MIN,
                    ).value,
                    std_n.core._interleave64_2d(
                        self.x1 + std_n.core._ti4d._UINT16_MIN,
                        self.x3 + std_n.core._ti4d._UINT16_MIN,
                    ).value,
                )

            def __deinterleave(self, interleaved: c_int64) -> None:
                x3120: int = std_n.core._deinterleave64_2d(interleaved)
                x20: int = std_n.core._deinterleave64_2d(
                    c_int64(x3120 & 0xFFFFFFFF))
                x31: int = std_n.core._deinterleave64_2d(c_int64(x3120 >> 32))
                self.x0 = (x20 & 0xFFFF) + std_n.core._ti4d._INT16_MIN
                self.x1 = (x31 & 0xFFFF) + std_n.core._ti4d._INT16_MIN
                self.x2 = (x20 >> 32) + std_n.core._ti4d._INT16_MIN
                self.x3 = (x31 >> 32) + std_n.core._ti4d._INT16_MIN

        class _ti5d(GreyCat.Object):
            __INT12_MIN: int = -2047 - 1
            __INT12_MAX: int = 2047
            __UINT12_MIN = 63488

            def __init__(self, type: GreyCat.Type) -> None:
                self.x0: int
                self.x1: int
                self.x2: int
                self.x3: int
                self.x4: int
                super().__init__(type, None)

            @final
            def _save_type(self, stream: GreyCat._Stream) -> None:
                stream.write_i8(PrimitiveType.TU5D)

            @final
            def _save(self, stream: GreyCat._Stream) -> None:
                stream.write_i64(self.__interleave())

            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat._Stream) -> Any:
                res: std_n.core._ti5d = type.factory(type, [])
                res.__deinterleave(stream.read_i64())
                return res

            def __str__(self) -> str:
                return f"ti5d{{x0={self.x0},x1={self.x1},x2={self.x2},x3={self.x3},x4={self.x4}}}"

            def __interleave(self) -> c_int64:
                return std_n.core._interleave64_5d(
                    self.x0 + std_n.core._ti5d.__UINT12_MIN,
                    self.x1 + std_n.core._ti5d.__UINT12_MIN,
                    self.x2 + std_n.core._ti5d.__UINT12_MIN,
                    self.x3 + std_n.core._ti5d.__UINT12_MIN,
                    self.x4 + std_n.core._ti5d.__UINT12_MIN,
                )

            def __deinterleave(self, interleaved: c_int64) -> None:
                B: list[int] = [
                    0x0C0300C0300C03,
                    0x0F0000F0000F,
                    0x00F00000000FF,
                    0x0FFF,
                ]
                S: list[int] = [4, 8, 16, 32]

                self.x0 = (
                    std_n.core._deinterleave64_5d(interleaved)
                    + std_n.core._ti5d.__INT12_MIN
                )
                self.x1 = (
                    std_n.core._deinterleave64_5d(
                        c_int64(interleaved.value >> 1))
                    + std_n.core._ti5d.__INT12_MIN
                )
                self.x2 = (
                    std_n.core._deinterleave64_5d(
                        c_int64(interleaved.value >> 2))
                    + std_n.core._ti5d.__INT12_MIN
                )
                self.x3 = (
                    std_n.core._deinterleave64_5d(
                        c_int64(interleaved.value >> 3))
                    + std_n.core._ti5d.__INT12_MIN
                )
                self.x4 = (
                    std_n.core._deinterleave64_5d(
                        c_int64(interleaved.value >> 4))
                    + std_n.core._ti5d.__INT12_MIN
                )

        class _ti6d(GreyCat.Object):
            __INT10_MIN: int = -511 - 1
            __INT10_MAX: int = 511
            __UINT10_MIN = 65024

            def __init__(self, type: GreyCat.Type) -> None:
                self.x0: int
                self.x1: int
                self.x2: int
                self.x3: int
                self.x4: int
                self.x5: int
                super().__init__(type, None)

            @final
            def _save_type(self, stream: GreyCat._Stream) -> None:
                stream.write_i8(PrimitiveType.TU6D)

            @final
            def _save(self, stream: GreyCat._Stream) -> None:
                stream.write_i64(self.__interleave())

            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat._Stream) -> Any:
                res: std_n.core._ti6d = type.factory(type, [])
                res.__deinterleave(stream.read_i64())
                return res

            def __str__(self) -> str:
                return f"ti6d{{x0={self.x0},x1={self.x1},x2={self.x2},x3={self.x3},x4={self.x4},x5={self.x5}}}"

            def __interleave(self) -> c_int64:
                return std_n.core._interleave64_3d(
                    std_n.core._interleave64_2d(
                        (self.x0 + std_n.core._ti6d.__UINT10_MIN) & 0x3FF,
                        (self.x3 + std_n.core._ti6d.__UINT10_MIN) & 0x3FF,
                    ).value,
                    std_n.core._interleave64_2d(
                        (self.x1 + std_n.core._ti6d.__UINT10_MIN) & 0x3FF,
                        (self.x4 + std_n.core._ti6d.__UINT10_MIN) & 0x3FF,
                    ).value,
                    std_n.core._interleave64_2d(
                        (self.x2 + std_n.core._ti6d.__UINT10_MIN) & 0x3FF,
                        (self.x5 + std_n.core._ti6d.__UINT10_MIN) & 0x3FF,
                    ).value,
                )

            def __deinterleave(self, interleaved: c_int64) -> None:
                y30: int = std_n.core._deinterleave64_2d(
                    c_int64(std_n.core._deinterleave64_3d(interleaved))
                )
                y41: int = std_n.core._deinterleave64_2d(
                    c_int64(
                        std_n.core._deinterleave64_3d(
                            c_int64(interleaved.value >> 1))
                    )
                )
                y52: int = std_n.core._deinterleave64_2d(
                    c_int64(
                        std_n.core._deinterleave64_3d(
                            c_int64(interleaved.value >> 2))
                    )
                )

                self.x0 = (y30 & 0x3FF) + std_n.core._ti6d.__INT10_MIN
                self.x1 = (y41 & 0x3FF) + std_n.core._ti6d.__INT10_MIN
                self.x2 = (y52 & 0x3FF) + std_n.core._ti6d.__INT10_MIN
                self.x3 = (y30 >> 32) + std_n.core._ti6d.__INT10_MIN
                self.x4 = (y41 >> 32) + std_n.core._ti6d.__INT10_MIN
                self.x5 = (y52 >> 32) + std_n.core._ti6d.__INT10_MIN

        class _ti10d(GreyCat.Object):
            __INT6_MIN: int = -31 - 1
            __INT6_MAX: int = 31
            __UINT6_MIN: int = 224

            def __init__(self, type: GreyCat.Type) -> None:
                self.x0: int
                self.x1: int
                self.x2: int
                self.x3: int
                self.x4: int
                self.x5: int
                self.x6: int
                self.x7: int
                self.x8: int
                self.x9: int
                super().__init__(type, None)

            @final
            def _save_type(self, stream: GreyCat._Stream) -> None:
                stream.write_i8(PrimitiveType.TU10D)

            @final
            def _save(self, stream: GreyCat._Stream) -> None:
                stream.write_i64(self.__interleave())

            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat._Stream) -> Any:
                res: std_n.core._ti10d = type.factory(type, [])
                res.__deinterleave(stream.read_i64())
                return res

            def __str__(self) -> str:
                return f"ti2d{{x0={self.x0},x1={self.x1},x2={self.x2},x3={self.x3},x4={self.x4},x5={self.x5},x6={self.x6},x7={self.x7},x8={self.x8},x9={self.x9}}}"

            def __interleave(self) -> c_int64:
                return std_n.core._interleave64_5d(
                    std_n.core._interleave64_2d(
                        (self.x0 + std_n.core._ti10d.__UINT6_MIN) & 0x3F,
                        (self.x5 + std_n.core._ti10d.__UINT6_MIN) & 0x3F,
                    ).value,
                    std_n.core._interleave64_2d(
                        (self.x1 + std_n.core._ti10d.__UINT6_MIN) & 0x3F,
                        (self.x6 + std_n.core._ti10d.__UINT6_MIN) & 0x3F,
                    ).value,
                    std_n.core._interleave64_2d(
                        (self.x2 + std_n.core._ti10d.__UINT6_MIN) & 0x3F,
                        (self.x7 + std_n.core._ti10d.__UINT6_MIN) & 0x3F,
                    ).value,
                    std_n.core._interleave64_2d(
                        (self.x3 + std_n.core._ti10d.__UINT6_MIN) & 0x3F,
                        (self.x8 + std_n.core._ti10d.__UINT6_MIN) & 0x3F,
                    ).value,
                    std_n.core._interleave64_2d(
                        (self.x4 + std_n.core._ti10d.__UINT6_MIN) & 0x3F,
                        (self.x9 + std_n.core._ti10d.__UINT6_MIN) & 0x3F,
                    ).value,
                )

            def __deinterleave(self, interleaved: c_int64) -> None:
                self.x0 = (
                    std_n.core._deinterleave64_2d(
                        c_int64(std_n.core._deinterleave64_5d(interleaved))
                    )
                    & 0x3F
                ) + std_n.core._ti10d.__INT6_MIN
                self.x1 = (
                    std_n.core._deinterleave64_2d(
                        c_int64(
                            std_n.core._deinterleave64_5d(
                                c_int64(interleaved.value >> 1)
                            )
                        )
                    )
                    & 0x3F
                ) + std_n.core._ti10d.__INT6_MIN
                self.x2 = (
                    std_n.core._deinterleave64_2d(
                        c_int64(
                            std_n.core._deinterleave64_5d(
                                c_int64(interleaved.value >> 2)
                            )
                        )
                    )
                    & 0x3F
                ) + std_n.core._ti10d.__INT6_MIN
                self.x3 = (
                    std_n.core._deinterleave64_2d(
                        c_int64(
                            std_n.core._deinterleave64_5d(
                                c_int64(interleaved.value >> 3)
                            )
                        )
                    )
                    & 0x3F
                ) + std_n.core._ti10d.__INT6_MIN
                self.x4 = (
                    std_n.core._deinterleave64_2d(
                        c_int64(
                            std_n.core._deinterleave64_5d(
                                c_int64(interleaved.value >> 4)
                            )
                        )
                    )
                    & 0x3F
                ) + std_n.core._ti10d.__INT6_MIN
                self.x5 = (
                    std_n.core._deinterleave64_2d(
                        c_int64(
                            std_n.core._deinterleave64_5d(
                                c_int64(interleaved.value >> 5)
                            )
                        )
                    )
                    & 0x3F
                ) + std_n.core._ti10d.__INT6_MIN
                self.x6 = (
                    std_n.core._deinterleave64_2d(
                        c_int64(
                            std_n.core._deinterleave64_5d(
                                c_int64(interleaved.value >> 6)
                            )
                        )
                    )
                    & 0x3F
                ) + std_n.core._ti10d.__INT6_MIN
                self.x7 = (
                    std_n.core._deinterleave64_2d(
                        c_int64(
                            std_n.core._deinterleave64_5d(
                                c_int64(interleaved.value >> 7)
                            )
                        )
                    )
                    & 0x3F
                ) + std_n.core._ti10d.__INT6_MIN
                self.x8 = (
                    std_n.core._deinterleave64_2d(
                        c_int64(
                            std_n.core._deinterleave64_5d(
                                c_int64(interleaved.value >> 8)
                            )
                        )
                    )
                    & 0x3F
                ) + std_n.core._ti10d.__INT6_MIN
                self.x9 = (
                    std_n.core._deinterleave64_2d(
                        c_int64(
                            std_n.core._deinterleave64_5d(
                                c_int64(interleaved.value >> 9)
                            )
                        )
                    )
                    & 0x3F
                ) + std_n.core._ti10d.__INT6_MIN

        class _tf2d(GreyCat.Object):
            def __init__(self, type: GreyCat.Type) -> None:
                self.x0: float
                self.x1: float
                super().__init__(type, None)

            @final
            def _save_type(self, stream: GreyCat._Stream) -> None:
                stream.write_i8(PrimitiveType.TUF2D)

            @final
            def _save(self, stream: GreyCat._Stream) -> None:
                stream.write_i64(self.__interleave())

            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat._Stream) -> Any:
                res: std_n.core._tf2d = type.factory(type, [])
                res.__deinterleave(stream.read_i64())
                return res

            def __str__(self) -> str:
                return f"tf2d{{x0={self.x0},x1={self.x1}}}"

            def __interleave(self) -> c_int64:
                return std_n.core._interleave64_2d(
                    unpack("q", pack("d", self.x0))[
                        0] + std_n.core._ti2d._UINT32_MIN,
                    unpack("q", pack("d", self.x1))[
                        0] + std_n.core._ti2d._UINT32_MIN,
                )

            def __deinterleave(self, interleaved: c_int64) -> None:
                dc: int = std_n.core._deinterleave64_2d(interleaved)
                self.x0 = unpack(
                    "d", pack("q", c_int32(
                        dc + std_n.core._ti2d._INT32_MIN).value)
                )[0]
                self.x1 = unpack(
                    "d",
                    pack("q", c_int32((dc >> 32) +
                         std_n.core._ti2d._INT32_MIN).value),
                )[0]

        class _tf3d(GreyCat.Object):
            def __init__(self, type: GreyCat.Type) -> None:
                self.x0: float
                self.x1: float
                self.x2: float
                super().__init__(type, None)

            @final
            def _save_type(self, stream: GreyCat._Stream) -> None:
                stream.write_i8(PrimitiveType.TUF3D)

            @final
            def _save(self, stream: GreyCat._Stream) -> None:
                stream.write_i64(self.__interleave())

            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat._Stream) -> Any:
                res: std_n.core._tf3d = type.factory(type, [])
                res.__deinterleave(stream.read_i64())
                return res

            def __str__(self) -> str:
                return f"tf3d{{x0={self.x0},x1={self.x1},x2={self.x2}}}"

            def __interleave(self) -> c_int64:
                return std_n.core._interleave64_3d(
                    (unpack("i", pack("f", self.x0))[0] >> 11)
                    + std_n.core._ti3d._UINT21_MIN,
                    (unpack("i", pack("f", self.x1))[0] >> 11)
                    + std_n.core._ti3d._UINT21_MIN,
                    (unpack("i", pack("f", self.x2))[0] >> 11)
                    + std_n.core._ti3d._UINT21_MIN,
                )

            def __deinterleave(self, interleaved: c_int64) -> None:
                self.x0 = unpack(
                    "f",
                    pack(
                        "i",
                        c_int32(
                            (
                                std_n.core._deinterleave64_3d(interleaved)
                                + std_n.core._ti3d._INT21_MIN
                            )
                            << 11
                        ).value,
                    ),
                )[0]
                self.x1 = unpack(
                    "f",
                    pack(
                        "i",
                        c_int32(
                            (
                                std_n.core._deinterleave64_3d(
                                    c_int64(interleaved.value >> 1)
                                )
                                + std_n.core._ti3d._INT21_MIN
                            )
                            << 11
                        ).value,
                    ),
                )[0]
                self.x2 = unpack(
                    "f",
                    pack(
                        "i",
                        c_int32(
                            (
                                std_n.core._deinterleave64_3d(
                                    c_int64(interleaved.value >> 2)
                                )
                                + std_n.core._ti3d._INT21_MIN
                            )
                            << 11
                        ).value,
                    ),
                )[0]

        class _tf4d(GreyCat.Object):
            def __init__(self, type: GreyCat.Type) -> None:
                self.x0: float
                self.x1: float
                self.x2: float
                self.x3: float
                super().__init__(type, None)

            @final
            def _save_type(self, stream: GreyCat._Stream) -> None:
                stream.write_i8(PrimitiveType.TUF4D)

            @final
            def _save(self, stream: GreyCat._Stream) -> None:
                stream.write_i64(self.__interleave())

            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat._Stream) -> Any:
                res: std_n.core._tf4d = type.factory(type, [])
                res.__deinterleave(stream.read_i64())
                return res

            def __str__(self) -> str:
                return f"tf4d{{x0={self.x0},x1={self.x1},x2={self.x2},x3={self.x3}}}"

            def __interleave(self) -> c_int64:
                return std_n.core._interleave64_2d(
                    std_n.core._interleave64_2d(
                        (unpack("i", pack("f", self.x0))[0] >> 16)
                        + std_n.core._ti4d._UINT16_MIN,
                        (unpack("i", pack("f", self.x2))[0] >> 16)
                        + std_n.core._ti4d._UINT16_MIN,
                    ).value,
                    std_n.core._interleave64_2d(
                        (unpack("i", pack("f", self.x1))[0] >> 16)
                        + std_n.core._ti4d._UINT16_MIN,
                        (unpack("i", pack("f", self.x3))[0] >> 16)
                        + std_n.core._ti4d._UINT16_MIN,
                    ).value,
                )

            def __deinterleave(self, interleaved: c_int64) -> None:
                d3120: int = c_int64(
                    std_n.core._deinterleave64_2d(interleaved)).value
                d20: int = std_n.core._deinterleave64_2d(
                    c_int64(d3120 & 0xFFFFFFFF))
                d31: int = std_n.core._deinterleave64_2d(c_int64(d3120 >> 32))
                self.x0 = unpack(
                    "f",
                    pack(
                        "i",
                        c_int32(
                            ((d20 & 0xFFFF) + std_n.core._ti4d._INT16_MIN) << 16
                        ).value,
                    ),
                )[0]
                self.x1 = unpack(
                    "f",
                    pack(
                        "i",
                        c_int32(
                            ((d31 & 0xFFFF) + std_n.core._ti4d._INT16_MIN) << 16
                        ).value,
                    ),
                )[0]
                self.x2 = unpack(
                    "f",
                    pack(
                        "i",
                        c_int32(
                            ((d20 >> 32) + std_n.core._ti4d._INT16_MIN) << 16
                        ).value,
                    ),
                )[0]
                self.x3 = unpack(
                    "f",
                    pack(
                        "i",
                        c_int32(
                            ((d31 >> 32) + std_n.core._ti4d._INT16_MIN) << 16
                        ).value,
                    ),
                )[0]

        # Object types

        class _Array(Generic[__T], GreyCat.Object):
            def __init__(self, type: GreyCat.Type) -> None:
                super().__init__(type, [])

            @final
            def _save(self, stream: GreyCat._Stream) -> None:
                stream.write_vu32(c_uint32(len(self)))
                e: std_n.core.__T
                for e in self:
                    stream.write(e)

            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat._Stream) -> Any:
                size: int = stream.read_vu32().value
                array: std_n.core._Array = type.factory(type, [])
                array.attributes = [stream.read() for _ in repeat(None, size)]
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

            def __str__(self) -> str:
                res: str = "["
                for offset in range(len(self.attributes)):
                    if offset > 0:
                        res = f"{res},"
                    res = f"{res}{self.attributes[offset]}"
                return f"{res}]"

            def append(self, __value) -> None:
                self.attributes.append(__value)

            def extend(self, __iterable: Iterable) -> None:
                self.attributes.extend(__iterable)

            @staticmethod
            def from_list(greycat: GreyCat, l: list) -> std_n.core._Array:
                array: std_n.core._Array = std_n.core._Array(
                    greycat.types_by_name["core::Array"])
                array.extend(l)
                return array

        class _Date(GreyCat.Object):
            def __init__(self, type: GreyCat.Type) -> None:
                self.localized_epoch_s: int
                self.epoch_us: int
                self.time_zone: int
                super().__init__(type, None)

            @final
            def _save(self, stream: GreyCat._Stream) -> None:
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
            def _save(self, stream: GreyCat._Stream) -> None:
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
            def _save(self, stream: GreyCat._Stream) -> None:
                stream.write_vu32(c_int32(len(self)))
                key: std_n.core.__T
                value: std_n.core.__U
                for key, value in self.items():
                    stream.write(key)
                    stream.write(value)

            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat._Stream) -> Any:
                map: Final[std_n.core._Map] = type.factory(type, [])
                map_length: int = stream.read_vu32().value
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
                res: str = f"{{"
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
                len_: int = stream.read_vu32().value
                if 0 != (len_ & 1):
                    return type.greycat.symbols[len_ >> 1]
                return stream.read_string(len_ >> 1)

        class _Table(Generic[__T], GreyCat.Object):
            def __init__(self, type: GreyCat.Type) -> None:
                self.cols: int
                self.rows: int
                self.meta: list[std_n.core._Table.TableColumnMeta]
                self.data: list[std_n.core.__T]
                super().__init__(type, None)

            def _save(self, stream: GreyCat._Stream) -> None:
                stream.write_vu32(c_uint32(self.cols))
                stream.write_vu32(c_uint32(self.rows))
                meta_offset: int
                col_meta: std_n.core._Table.TableColumnMeta
                col_meta_header_bytes: bytes
                for meta_offset in range(len(self.meta)):
                    col_meta = self.meta[meta_offset]
                    stream.write_i8(col_meta.col_type)
                    stream.write_bool(col_meta.meta_index)
                    if col_meta.col_type in [PrimitiveType.OBJECT, PrimitiveType.ENUM]:
                        stream.write_vu32(col_meta.type)
                    if len(col_meta.header) > 0:
                        col_meta_header_bytes = col_meta.header.encode("utf-8")
                        stream.write_vu32(c_uint32(len(col_meta_header_bytes)))
                        stream.write_i8_array(
                            col_meta_header_bytes, 0, len(col_meta_header_bytes))
                    else:
                        stream.write_vu32(c_uint32(0))
                col: int
                row: int
                o: GreyCat.Object
                s: str
                col_type: int
                for col in range(self.cols):
                    col_type = self.meta[col].col_type.value
                    if col_type == PrimitiveType.NULL.value:
                        pass
                    elif col_type == PrimitiveType.INT.value:
                        for row in range(self.rows):
                            stream.write_vi64(self.data[col * self.rows + row])
                    elif col_type == PrimitiveType.FLOAT.value:
                        for row in range(self.rows):
                            stream.write_f64(self.data[col * self.rows + row])
                    elif col_type == PrimitiveType.TIME.value:
                        for row in range(self.rows):
                            o = self.data[col * self.rows + row]
                            o._save(stream)
                    elif col_type == PrimitiveType.DURATION.value:
                        for row in range(self.rows):
                            o = self.data[col * self.rows + row]
                            o._save(stream)
                    elif col_type == PrimitiveType.ENUM.value:
                        for row in range(self.rows):
                            o = self.data[col * self.rows + row]
                            o._save(stream)
                    elif col_type == PrimitiveType.OBJECT.value:
                        if self.meta[col].type.value == self.type_.greycat.type_offset_core_string:
                            for row in range(self.rows):
                                stream.write_string(
                                    self.data[col * self.rows + row], skip_type=True)
                        else:
                            for row in range(self.rows):
                                o = self.data[col * self.rows + row]
                                o._save(stream)
                    else:
                        for row in range(self.rows):
                            stream.write(self.data[col * self.rows + row])

            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat._Stream) -> Any:
                cols: Final[int] = stream.read_vu32().value
                rows: Final[int] = stream.read_vu32().value
                meta: list[std_n.core._Table.TableColumnMeta] = []
                meta_col_type: c_ubyte
                meta_index: bool
                meta_type: c_uint32
                meta_header_len: int
                meta_header: str
                for _ in repeat(None, cols):
                    meta_col_type = stream.read_i8()
                    meta_index = stream.read_bool()
                    meta_type: c_int32
                    if meta_col_type.value in [
                        PrimitiveType.OBJECT.value,
                        PrimitiveType.ENUM.value,
                    ]:
                        meta_type = stream.read_vu32()
                    else:
                        meta_type = c_uint32(0)
                    meta_header_len = stream.read_vu32().value
                    if meta_header_len > 0:
                        meta_header = stream.read_string(meta_header_len)
                    else:
                        meta_header = ''
                    meta.append(
                        std_n.core._Table.TableColumnMeta(
                            meta_col_type, meta_type, meta_index, meta_header
                        )
                    )

                data: list[Any] = []
                col: int
                greycat_type: GreyCat.Type
                col_type: int
                for col in range(cols):
                    col_type = meta[col].col_type.value
                    if col_type == PrimitiveType.NULL.value:
                        pass
                    elif col_type == PrimitiveType.INT.value:
                        for _ in repeat(None, rows):
                            data.append(stream.read_vi64())
                    elif col_type == PrimitiveType.FLOAT.value:
                        for _ in repeat(None, rows):
                            data.append(stream.read_f64())
                    elif col_type == PrimitiveType.TIME.value:
                        for _ in repeat(None, rows):
                            data.append(
                                std_n.core._time.load(
                                    type.greycat.types[
                                        type.greycat.type_offset_core_time
                                    ],
                                    stream,
                                )
                            )
                    elif col_type == PrimitiveType.DURATION.value:
                        for _ in repeat(None, rows):
                            data.append(
                                std_n.core._duration.load(
                                    type.greycat.types[
                                        type.greycat.type_offset_core_duration
                                    ],
                                    stream,
                                )
                            )
                    elif col_type == PrimitiveType.ENUM.value:
                        greycat_type = type.greycat.types[meta[col].type.value]
                        for _ in repeat(None, rows):
                            data.append(greycat_type.loader(
                                greycat_type, stream))
                    elif col_type == PrimitiveType.OBJECT.value:
                        greycat_type = type.greycat.types[meta[col].type.value]
                        for _ in repeat(None, rows):
                            data.append(greycat_type.loader(
                                greycat_type, stream))
                    else:
                        for _ in repeat(None, rows):
                            data.append(stream.read())
                t: std_n.core._Table = type.factory(type, [])
                t.cols = cols
                t.rows = rows
                t.meta = meta
                t.data = data
                return t

            class TableColumnMeta:
                def __init__(
                    self, col_type: c_ubyte, type: c_uint32, index: bool, header: str
                ) -> None:
                    self.col_type: Final[c_ubyte] = col_type
                    self.type: Final[c_uint32] = type
                    self.meta_index: Final[bool] = index
                    self.header: Final[str] = header

                def __str__(self) -> str:
                    ...

                def __repr__(self) -> str:
                    return f"{{header: {self.header}, col_type: {self.col_type}, type: {self.type}, index: {self.meta_index}}}"

            if "numpy" in sys.modules:

                def to_numpy(self) -> tuple[numpy.ndarray]:
                    nda: numpy.ndarray = numpy.reshape(
                        [
                            elem.value if type(elem) in [c_double, c_int64]
                            else elem.to_numpy() if isinstance(elem, std_n.core._time) or isinstance(elem, std_n.core._duration)
                            else elem.map if isinstance(elem, std_n.core._Map)
                            else elem
                            for elem in self.data
                        ],
                        (self.rows, self.cols),
                        "F",
                    )
                    null_indices: list[int] = []
                    for index, col_meta in enumerate(self.meta):
                        if col_meta.col_type == PrimitiveType.NULL:
                            null_indices.append(index - len(null_indices))
                    if len(null_indices) > 0:
                        nda = nda.astype(numpy.dtype(object))
                        nda = numpy.insert(nda, null_indices, None, axis=1)
                    return nda

                @staticmethod
                def __parse_numpy_elem(gc: GreyCat, elem) -> Any:
                    elem_type = type(elem)
                    if isinstance(elem, numpy.floating) or elem_type is float:
                        return c_double(elem)
                    if isinstance(elem, numpy.integer) or elem_type is int:
                        return c_int64(elem)
                    if isinstance(elem, numpy.complex128) or elem_type is complex:
                        return greycat.std.core.Tuple.create(gc, float(numpy.real(elem)), float(numpy.imag(elem)))
                    if isinstance(elem, numpy.datetime64):
                        return std_n.core._time.from_numpy(gc, elem)
                    if isinstance(elem, numpy.timedelta64):
                        return std_n.core._duration.from_numpy(gc, elem)
                    if "pandas" in sys.modules:
                        if isinstance(elem, pandas.Timestamp):
                            return std_n.core._time.from_numpy(gc, elem.to_numpy())
                        if isinstance(elem, pandas.Timedelta):
                            return std_n.core._duration.from_numpy(gc, elem.to_numpy())
                        if isinstance(elem, pandas.Period):
                            return greycat.std.core.Tuple.create(gc, std_n.core._time.from_numpy(gc, elem.start_time.to_numpy()), f"{elem.freq}")
                        if isinstance(elem, pandas.Interval):
                            return std_n.core._Table.__interval_to_map(gc, elem)
                    return elem

                @staticmethod
                def from_numpy(
                    gc: GreyCat, nda: numpy.ndarray, meta: Optional[list[std_n.core._Table.TableColumnMeta]] = None
                ) -> std_n.core._Table:
                    type_: GreyCat.Type = gc.types_by_name["core::Table"]
                    table: std_n.core._Table = type_.factory(type_, None)
                    if nda.dtype == numpy.dtype(float):
                        table.data = [c_double(elem)
                                      for elem in nda.flatten("F")]
                    elif nda.dtype == numpy.dtype(int):
                        table.data = [c_int64(elem)
                                      for elem in nda.flatten("F")]
                    elif nda.dtype == numpy.dtype(object):
                        if len(list(filter(lambda elem: type(elem) is int and not -2 ** 63 <= elem < 2 ** 63, nda))) > 0:
                            raise ValueError(
                                "Numpy array contains ints larger than max int64")
                        table.data = [
                            std_n.core._Table.__parse_numpy_elem(gc, elem)
                            for elem in nda.flatten("F")
                        ]
                    else:
                        raise ValueError(f"Unknown dtype: {nda.dtype}")
                    table.rows = nda.shape[0]
                    table.cols = nda.shape[1]
                    if meta is not None:
                        table.meta = meta
                    if not hasattr(table, "meta"):
                        table.meta = [
                            std_n.core._Table.TableColumnMeta(
                                PrimitiveType.UNDEFINED, c_uint32(0), False, ""
                            )
                            for _ in repeat(None, table.cols)
                        ]
                    return table

                if "pandas" in sys.modules:
                    @staticmethod
                    def __interval_to_map(gc: GreyCat, interval: pandas.Interval) -> std_n.core._Map[std_n.core._String, Any]:
                        map = std_n.core._Map(gc.types_by_name["core::Map"])
                        map["left"] = std_n.core._Table.__parse_numpy_elem(
                            gc, interval.left)
                        map["right"] = std_n.core._Table.__parse_numpy_elem(
                            gc, interval.right)
                        map["closed_left"] = interval.closed_left
                        map["closed_right"] = interval.closed_right
                        return map

                    def to_pandas(self) -> pandas.DataFrame:
                        nda = self.to_numpy()
                        columns: list[str | int] = list(
                            map(lambda meta: meta.header, self.meta))
                        dtypes: map[str | int, numpy.dtype] = {}
                        dtype: numpy.dtype
                        if len(set(columns)) < len(columns):
                            columns = list(range(len(columns)))
                        for offset, meta in enumerate(self.meta):
                            if PrimitiveType.FLOAT.value == meta.col_type.value:
                                dtype = numpy.dtype(float)
                            elif PrimitiveType.INT.value == meta.col_type.value:
                                dtype = numpy.dtype(int)
                            elif PrimitiveType.BOOL.value == meta.col_type.value:
                                dtype = numpy.dtype(bool)
                            elif PrimitiveType.TIME.value == meta.col_type.value:
                                dtype = numpy.dtype('datetime64[us]')
                            elif PrimitiveType.DURATION.value == meta.col_type.value:
                                dtype = numpy.dtype('timedelta64[us]')
                            elif meta.col_type.value == PrimitiveType.OBJECT.value:
                                if meta.type.value == self.type_.greycat.type_offset_core_string:
                                    dtype = pandas.StringDtype()
                                else:
                                    dtype = numpy.dtype(object)
                            elif meta.col_type.value == PrimitiveType.UNDEFINED.value:
                                dtype = numpy.dtype(object)
                            else:
                                raise ValueError(
                                    f"Unknown col type: {meta.col_type.value}")
                            dtypes[columns[offset]] = dtype
                        return pandas.DataFrame(nda, columns=columns).astype(dtypes)

                    @staticmethod
                    def from_pandas(
                        greycat: GreyCat, df: pandas.DataFrame
                    ) -> std_n.core._Table:
                        nda = df.to_numpy()
                        meta: list[std_n.core._Table.TableColumnMeta] = []
                        dtype: numpy.dtype
                        col_type: c_ubyte
                        _type: c_uint32
                        index: bool = False
                        header: str
                        for typed_header in df.dtypes.items():
                            dtype = typed_header[1]
                            _type = c_uint32(PrimitiveType.UNDEFINED.value)
                            if dtype is numpy.dtype(float):
                                col_type = PrimitiveType.FLOAT
                            elif dtype is numpy.dtype(int):
                                col_type = PrimitiveType.INT
                            elif type(dtype) is pandas.StringDtype:
                                col_type = PrimitiveType.OBJECT
                                _type = c_uint32(
                                    greycat.type_offset_core_string)
                            elif dtype.type is numpy.datetime64:
                                col_type = PrimitiveType.TIME
                            elif dtype.type is numpy.timedelta64:
                                col_type = PrimitiveType.DURATION
                            elif dtype is numpy.dtype(bool):
                                col_type = PrimitiveType.BOOL
                            # elif dtype is numpy.dtype(object):
                            #     col_type = PrimitiveType.UNDEFINED
                            else:
                                col_type = PrimitiveType.UNDEFINED
                            header = typed_header[0]
                            meta.append(std_n.core._Table.TableColumnMeta(
                                col_type, _type, index, header))
                        return std_n.core._Table.from_numpy(greycat, nda, meta=meta)

                if "tensorflow" in sys.modules:
                    def to_tf_tensor(self) -> tensorflow.Tensor:
                        return tensorflow.constant(self.to_numpy())

                    @staticmethod
                    def from_tf_tensor(greycat: GreyCat, tf_tensor: tensorflow.Tensor, session: tensorflow.compat.v1.Session | None = None) -> std_n.core._Table:
                        if tensorflow.executing_eagerly():
                            return std_n.core._Table.from_numpy(greycat, tf_tensor.numpy())
                        if session is not None:
                            return std_n.core._Table.from_numpy(greycat, session.run(tf_tensor))
                        return std_n.core._Table.from_numpy(greycat, tensorflow.compat.v1.Session().run(tf_tensor))

        class _Tensor(GreyCat.Object):
            def __init__(self, type: GreyCat.Type) -> None:
                self.shape: list[c_uint32]
                self.tensor_type: c_byte
                self.size: c_uint32
                self.data: bytes
                self.dtype: greycat.std.core.TensorType
                self.format: str
                super().__init__(type, None)

            @final
            def _save(self, stream: GreyCat._Stream) -> None:
                stream.write_i8(c_byte(len(self.shape)))
                stream.write_i8(self.tensor_type)
                dim: c_uint32
                for dim in self.shape:
                    stream.write_i32(dim)
                stream.write_i32(self.size)
                stream.write_i8_array(self.data)

            @staticmethod
            def load(type_: GreyCat.Type, stream: GreyCat._Stream) -> Any:
                nb_dim: Final[int] = stream.read_i8().value
                tensor_type: Final[c_byte] = stream.read_i8()
                shape: list[c_uint32] = [stream.read_i32()
                                         for _ in repeat(None, nb_dim)]
                size: c_uint32 = stream.read_i32()
                dtype = type_.greycat.types_by_name[greycat.std.core.TensorType.name_].enum_values[tensor_type.value]
                format_: str
                if dtype == greycat.std.core.TensorType.i32(type_.greycat):
                    format_ = "=i"
                elif dtype == greycat.std.core.TensorType.i64(type_.greycat):
                    format_ = "=q"
                elif dtype == greycat.std.core.TensorType.f32(type_.greycat):
                    format_ = "=f"
                elif dtype == greycat.std.core.TensorType.f64(type_.greycat):
                    format_ = "=d"
                elif dtype == greycat.std.core.TensorType.c64(type_.greycat):
                    format_ = "=ff"
                elif dtype == greycat.std.core.TensorType.c128(type_.greycat):
                    format_ = "=dd"
                else:
                    raise ValueError(f"${tensor_type}")
                bin_size: int = size.value * dtype.value
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
                            sum(dim.value for dim in self.shape[index + 1:])
                    else:
                        offset += dim_key
                unpacked: Tuple = unpack(self.format, self.data[slice(
                    offset * self.dtype.value, (offset + 1) * self.dtype.value)])
                if self.dtype in [greycat.std.core.TensorType.c64(self.type_.greycat), greycat.std.core.TensorType.c128(self.type_.greycat)]:
                    return unpacked
                return unpacked[0]

            if "numpy" in sys.modules:
                def to_numpy(self) -> numpy.ndarray:
                    dtype: numpy.dtype
                    if self.dtype == greycat.std.core.TensorType.i32(self.type_.greycat):
                        dtype = numpy.dtype('int32')
                    elif self.dtype == greycat.std.core.TensorType.i64(self.type_.greycat):
                        dtype = numpy.dtype('int64')
                    elif self.dtype == greycat.std.core.TensorType.f32(self.type_.greycat):
                        dtype = numpy.dtype('float32')
                    elif self.dtype == greycat.std.core.TensorType.f64(self.type_.greycat):
                        dtype = numpy.dtype('float64')
                    elif self.dtype == greycat.std.core.TensorType.c64(self.type_.greycat):
                        dtype = numpy.dtype('complex64')
                    elif self.dtype == greycat.std.core.TensorType.c128(self.type_.greycat):
                        dtype = numpy.dtype('complex128')
                    else:
                        raise ValueError(f"${self.tensor_type}")
                    return numpy.frombuffer(self.data, dtype=dtype).reshape([dim.value for dim in self.shape])

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
                    dtype: greycat.std.core.TensorType
                    format_: str
                    if nda.dtype == numpy.dtype('int32'):
                        dtype = greycat.std.core.TensorType.i32(greycat_)
                        format_ = "=i"
                    elif nda.dtype == numpy.dtype('int64'):
                        dtype = greycat.std.core.TensorType.i64(greycat_)
                        format_ = "=q"
                    elif nda.dtype == numpy.dtype('float32'):
                        dtype = greycat.std.core.TensorType.f32(greycat_)
                        format_ = "=f"
                    elif nda.dtype == numpy.dtype('float64'):
                        dtype = greycat.std.core.TensorType.f64(greycat_)
                        format_ = "=d"
                    elif nda.dtype == numpy.dtype('complex64'):
                        dtype = greycat.std.core.TensorType.c64(greycat_)
                        format_ = "=ff"
                    elif nda.dtype == numpy.dtype('complex128'):
                        dtype = greycat.std.core.TensorType.c128(greycat_)
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
                        if self.dtype == greycat.std.core.TensorType.i32(self.type_.greycat):
                            dtype = numpy.dtype('int32')
                        elif self.dtype == greycat.std.core.TensorType.i64(self.type_.greycat):
                            dtype = numpy.dtype('int64')
                        elif self.dtype == greycat.std.core.TensorType.f32(self.type_.greycat):
                            dtype = numpy.dtype('float32')
                        elif self.dtype == greycat.std.core.TensorType.f64(self.type_.greycat):
                            dtype = numpy.dtype('float64')
                        elif self.dtype == greycat.std.core.TensorType.c64(self.type_.greycat):
                            dtype = numpy.dtype('complex64')
                        elif self.dtype == greycat.std.core.TensorType.c128(self.type_.greycat):
                            dtype = numpy.dtype('complex128')
                        else:
                            raise ValueError(f"${self.tensor_type}")
                        return tensorflow.constant(numpy.frombuffer(self.data, dtype=dtype), [dim.value for dim in self.shape])

                    @staticmethod
                    def from_tf_tensor(greycat: GreyCat, tf_tensor: tensorflow.Tensor, tf_session: tensorflow.compat.v1.Session | None = None) -> std_n.core._Tensor:
                        if tensorflow.executing_eagerly():
                            return std_n.core._Tensor.from_numpy(greycat, tf_tensor.numpy())
                        if tf_session is not None:
                            return std_n.core._Tensor.from_numpy(greycat, tf_session.run(tf_tensor))
                        return std_n.core._Tensor.from_numpy(greycat, tensorflow.compat.v1.Session().run(tf_tensor))

            if "torch" in sys.modules:
                def to_torch_tensor(self, requires_grad: bool = False) -> torch.Tensor:
                    dtype: torch.dtype
                    if self.dtype == greycat.std.core.TensorType.i32(self.type_.greycat):
                        dtype = torch.int32
                    elif self.dtype == greycat.std.core.TensorType.i64(self.type_.greycat):
                        dtype = torch.int64
                    elif self.dtype == greycat.std.core.TensorType.f32(self.type_.greycat):
                        dtype = torch.float32
                    elif self.dtype == greycat.std.core.TensorType.f64(self.type_.greycat):
                        dtype = torch.float64
                    elif self.dtype == greycat.std.core.TensorType.c64(self.type_.greycat):
                        dtype = torch.complex64
                    elif self.dtype == greycat.std.core.TensorType.c128(self.type_.greycat):
                        dtype = torch.complex128
                    else:
                        raise ValueError(f"${self.tensor_type}")
                    return torch.frombuffer(self.data, dtype=dtype, requires_grad=requires_grad).reshape([dim.value for dim in self.shape])

                @staticmethod
                def from_torch_tensor(greycat_: GreyCat, torch_tensor: torch.Tensor) -> std_n.core._Table:
                    if torch_tensor.dtype in (torch.uint8, torch.int8, torch.int16):
                        torch_tensor = torch_tensor.type(torch.int32)
                    if torch_tensor.dtype in (torch.bfloat16, torch.float16):
                        torch_tensor = torch_tensor.type(torch.float32)
                    if torch_tensor.dtype == torch.complex32:
                        torch_tensor = torch_tensor.type(torch.complex64)
                    dtype: greycat.std.core.TensorType
                    format_: str
                    if torch_tensor.dtype == torch.int32:
                        dtype = greycat.std.core.TensorType.i32(greycat_)
                        format_ = "=i"
                    elif torch_tensor.dtype == torch.int64:
                        dtype = greycat.std.core.TensorType.i64(greycat_)
                        format_ = "=q"
                    elif torch_tensor.dtype == torch.float32:
                        dtype = greycat.std.core.TensorType.f32(greycat_)
                        format_ = "=f"
                    elif torch_tensor.dtype == torch.float64:
                        dtype = greycat.std.core.TensorType.f64(greycat_)
                        format_ = "=d"
                    elif torch_tensor.dtype == torch.complex64:
                        dtype = greycat.std.core.TensorType.c64(greycat_)
                        format_ = "=ff"
                    elif torch_tensor.dtype == torch.complex128:
                        dtype = greycat.std.core.TensorType.c128(greycat_)
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
            def _save(self, stream: GreyCat._Stream) -> None:
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
        def _interleave64_2d(x: int, y: int) -> c_int64:
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

            return c_int64(x | (y << 1))

        @staticmethod
        def _deinterleave64_2d(interleaved: c_int64) -> int:
            x: int = interleaved.value
            y: int = interleaved.value >> 1

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
        def _interleave64_3d(x: int, y: int, z: int) -> c_int64:
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

            return c_int64(x | (y << 1) | (z << 2))

        @staticmethod
        def _deinterleave64_3d(interleaved: c_int64) -> int:
            x: int = interleaved.value & std_n.core.__B_3D[0]
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
        def _deinterleave64_5d(interleaved: c_int64) -> int:
            x: int = interleaved.value & std_n.core.__B_5D[0]
            x = (x ^ (x >> std_n.core.__S_5D[0])) & std_n.core.__B_5D[1]
            x = (x ^ (x >> std_n.core.__S_5D[1])) & std_n.core.__B_5D[2]
            x = (x ^ (x >> std_n.core.__S_5D[2])) & std_n.core.__B_5D[3]
            x = (x ^ (x >> std_n.core.__S_5D[3])) & std_n.core.__B_5D[4]
            return x

    class util:
        __T = TypeVar("__T")

        class _Quantizer(GreyCat.Object):
            def __init__(self, type: GreyCat.Type) -> None:
                super().__init__(type, None)
                raise RuntimeError("unsupported")

            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat._Stream) -> Any:
                raise IOError("unsupported")

        class _Buffer(GreyCat.Object):
            def __init__(self, type: GreyCat.Type) -> None:
                self.data: bytes
                super().__init__(type, None)

            def _save(self, stream: GreyCat._Stream) -> None:
                stream.write_vu32(c_uint32(len(self.data)))
                stream.write_i8_array(self.data, 0, len(self.data))

            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat._Stream) -> Any:
                buf: std_n.util._Buffer = type.factory(type, [])
                buf.data = stream.read_i8_array(stream.read_vu32().value)
                return buf

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

            def _save(self, stream: GreyCat._Stream) -> None:
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

        class _GaussianProfile(GreyCat.Object):
            def __init__(self, type: GreyCat.Type) -> None:
                self.data: bytes
                self.size: c_int32
                super().__init__(type, None)

            def _save(self, stream: GreyCat._Stream) -> None:
                stream.write_i32(self.size)
                stream.write_i32(c_int32(len(self.data)))
                stream.write_i8_array(self.data, 0, len(self.data))

            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat._Stream) -> Any:
                gp: std_n.util._GaussianProfile = type.factory(type, [])
                gp.size = stream.read_i32()
                gp.data = stream.read_i8_array(stream.read_i32().value)
                return gp

        class _HistogramFloat(GreyCat.Object):
            pass

        class _HistogramInt(GreyCat.Object):
            pass

        class _ProgressTracker(GreyCat.Object):
            pass

        class _Iban(GreyCat.Object):
            def __init__(self, type: GreyCat.Type) -> None:
                self.info_off: c_uint32
                self.data: bytes
                super().__init__(type, None)

            def _save(self, stream: GreyCat._Stream) -> None:
                stream.write_vu32(self.info_off)
                stream.write_vu32(c_uint32(len(self.data)))
                stream.write_i8_array(self.data, 0, len(self.data))

            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat._Stream) -> Any:
                iban: std_n.util._Iban = type.factory(type, [])
                iban.info_off = stream.read_vu32()
                iban.data = stream.read_i8_array(stream.read_vu32().value)
                return iban

        class _Queue(Generic[__T], GreyCat.Object):
            def __init__(self, type: GreyCat.Type) -> None:
                self.queue: Final[deque] = deque()
                super().__init__(type, None)

            def _save(self, stream: GreyCat._Stream) -> None:
                stream.write_vi64(len(self))  # width
                stream.write_vi64(len(self))  # size
                stream.write_vi64(len(self))  # capacity
                stream.write_vi64(len(self))  # TODO: head - values
                stream.write_vi64(0)  # TODO: tail - values
                t: std_n.core.__T
                for t in self:
                    stream.write(t)

            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat._Stream) -> Any:
                stream.read_vi64()  # width
                size: Final[int] = stream.read_vi64().value
                capacity: Final[int] = stream.read_vi64().value
                stream.read_vi64()  # head - values
                stream.read_vi64()  # tail - values
                queue_: std_n.util._Queue = type.factory(type)
                for _ in range(size):
                    queue_.put(stream.read())
                for _ in range(capacity - size):
                    stream.read()
                return queue_

            def put(
                self, item: std_n.core.__T, block: bool = True, timeout: Number | None = None
            ) -> None:
                self.queue.appendleft(item, block, timeout)

            def __len__(self) -> int:
                return len(self.queue)

            def __reduce__(self) -> tuple[type[Self], tuple[()], None, Iterator[std_n.core.__T]]:
                return self.queue.__reduce__()

        class _SlidingWindow(GreyCat.Object):
            def __init__(self, type: GreyCat.Type) -> None:
                self.time_width: c_int64
                self.sum_type: c_ubyte
                self.sum: c_double
                self.sum_sq: c_double
                self.size: c_uint32
                self.capacity: int
                self.to_head: c_int64
                self.to_tail: c_int64
                self.values: list[Any]
                super().__init__(type, None)

            def _save(self, stream: GreyCat._Stream) -> None:
                stream.write_vi64(self.time_width)
                stream.write_i8(self.sum_type)
                stream.write_f64(self.sum)
                stream.write_f64(self.sum_sq)
                stream.write_vu32(self.size)
                stream.write_vu32(c_uint32(self.capacity))
                stream.write_vi64(self.to_head)
                stream.write_vi64(self.to_tail)
                values_offset: int
                for values_offset in range(len(self.values)):
                    stream.write(self.values[values_offset])

            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat._Stream) -> Any:
                time_width: c_int64 = stream.read_vi64()
                sum_type: c_ubyte = stream.read_i8()
                sum: c_double = stream.read_f64()
                sum_sq: c_double = stream.read_f64()
                size: c_uint32 = stream.read_vu32()
                capacity: int = stream.read_vu32().value
                to_head: c_int64 = stream.read_vi64()
                to_tail: c_int64 = stream.read_vi64()
                values: list[Any] = [stream.read()
                                     for _ in repeat(None, capacity)]
                sw: std_n.util._SlidingWindow = type.factory(type, [])
                sw.time_width = time_width
                sw.sum_type = sum_type
                sw.sum = sum
                sw.sum_sq = sum_sq
                sw.size = size
                sw.capacity = capacity
                sw.to_head = to_head
                sw.to_tail = to_tail
                sw.values = values
                return sw

        class _TimeWindow(GreyCat.Object):
            def __init__(self, type: GreyCat.Type) -> None:
                self.time_width: c_int64
                self.sum_type: c_ubyte
                self.sum: c_double
                self.sum_sq: c_double
                self.size: c_uint32
                self.capacity: int
                self.to_head: c_int64
                self.to_tail: c_int64
                self.value_times: list[std_n.util._TimeWindow.ValueTime]
                super().__init__(type, None)

            def _save(self, stream: GreyCat._Stream) -> None:
                stream.write_vi64(self.time_width)
                stream.write_i8(self.sum_type)
                stream.write_f64(self.sum)
                stream.write_f64(self.sum_sq)
                stream.write_vu32(self.size)
                stream.write_vu32(c_uint32(self.capacity))
                stream.write_vi64(self.to_head)
                stream.write_vi64(self.to_tail)
                value_time_offset: int
                value_time: std_n.util._TimeWindow.ValueTime
                for value_time_offset in range(len(self.value_times)):
                    value_time = self.value_times[value_time_offset]
                    stream.write(value_time.value)
                    stream.write_i64(value_time.time)

            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat._Stream) -> Any:
                time_width: c_int64 = stream.read_vi64()
                sum_type: c_ubyte = stream.read_i8()
                sum: c_double = stream.read_f64()
                sum_sq: c_double = stream.read_f64()
                size: c_uint32 = stream.read_vu32()
                capacity: int = stream.read_vu32().value
                to_head: c_int64 = stream.read_vi64()
                to_tail: c_int64 = stream.read_vi64()
                value_times: list[std_n.util._TimeWindow.ValueTime] = [
                    std_n.util._TimeWindow.ValueTime(
                        stream.read(), stream.read_vi64())
                    for _ in repeat(None, capacity)
                ]
                tw: std_n.util._TimeWindow = type.factory(type, [])
                tw.time_width = time_width
                tw.sum_type = sum_type
                tw.sum = sum
                tw.sum_sq = sum_sq
                tw.size = size
                tw.capacity = capacity
                tw.to_head = to_head
                tw.to_tail = to_tail
                tw.value_times = value_times
                return tw

            class ValueTime:
                def __init__(self, value: Any, time: c_int64) -> None:
                    self.value: Any = value
                    self.time: c_int64 = time
