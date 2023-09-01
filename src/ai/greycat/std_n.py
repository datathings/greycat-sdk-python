from __future__ import annotations

from _collections_abc import dict_keys, dict_values, dict_items
from ctypes import *
from struct import pack, unpack
from typing import *

import numpy
try:
    numpy
except NameError:
    pass
else:
    import pandas

from ai.greycat.greycat import GreyCat, PrimitiveType

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
                lat_offset, lng_offset = std_n.core._geo.__deinterleave64(value)
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
                self.x1 = c_int32((dc >> 32) + std_n.core._ti2d._INT32_MIN).value

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
                    std_n.core._deinterleave64_3d(c_int64(interleaved.value >> 1))
                    + std_n.core._ti3d._INT21_MIN
                )
                self.x2 = (
                    std_n.core._deinterleave64_3d(c_int64(interleaved.value >> 2))
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
                x20: int = std_n.core._deinterleave64_2d(c_int64(x3120 & 0xFFFFFFFF))
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
                    std_n.core._deinterleave64_5d(c_int64(interleaved.value >> 1))
                    + std_n.core._ti5d.__INT12_MIN
                )
                self.x2 = (
                    std_n.core._deinterleave64_5d(c_int64(interleaved.value >> 2))
                    + std_n.core._ti5d.__INT12_MIN
                )
                self.x3 = (
                    std_n.core._deinterleave64_5d(c_int64(interleaved.value >> 3))
                    + std_n.core._ti5d.__INT12_MIN
                )
                self.x4 = (
                    std_n.core._deinterleave64_5d(c_int64(interleaved.value >> 4))
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
                        std_n.core._deinterleave64_3d(c_int64(interleaved.value >> 1))
                    )
                )
                y52: int = std_n.core._deinterleave64_2d(
                    c_int64(
                        std_n.core._deinterleave64_3d(c_int64(interleaved.value >> 2))
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
                    unpack("q", pack("d", self.x0))[0] + std_n.core._ti2d._UINT32_MIN,
                    unpack("q", pack("d", self.x1))[0] + std_n.core._ti2d._UINT32_MIN,
                )

            def __deinterleave(self, interleaved: c_int64) -> None:
                dc: int = std_n.core._deinterleave64_2d(interleaved)
                self.x0 = unpack(
                    "d", pack("q", c_int32(dc + std_n.core._ti2d._INT32_MIN).value)
                )[0]
                self.x1 = unpack(
                    "d",
                    pack("q", c_int32((dc >> 32) + std_n.core._ti2d._INT32_MIN).value),
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
                d3120: int = c_int64(std_n.core._deinterleave64_2d(interleaved)).value
                d20: int = std_n.core._deinterleave64_2d(c_int64(d3120 & 0xFFFFFFFF))
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
                super().__init__(type, None)

            @final
            def _save(self, stream: GreyCat._Stream) -> None:
                stream.write_vu32(c_uint32(len(self)))
                offset: int
                for offset in range(len(self)):
                    stream.write(self[offset])

            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat._Stream) -> Any:
                size: int = stream.read_vu32().value
                array: std_n.core._Array = type.factory(type, [])
                array.attributes = [None] * size
                offset: int
                for offset in range(size):
                    array[offset] = stream.read()
                return array

            def __len__(self) -> int:
                return len(self.attributes)

            def __iter__(self) -> Iterator[__T]:
                return self.attributes.__iter__()

            @overload
            def __getitem__(self, __i: SupportsIndex) -> __T:
                ...

            @overload
            def __getitem__(self, __s: slice) -> list[__T]:
                ...

            def __getitem__(self, __key):
                return self.attributes[__key]

            @overload
            def __setitem__(self, __key: SupportsIndex, __value: __T) -> None:
                pass

            @overload
            def __setitem__(self, __key: slice, __value: Iterable[__T]) -> None:
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
                frames: Final[list[std_n.core._Error.Frame]] = [None] * frames_len
                offset: int
                mod_symbol: int
                type_symbol: int
                fn_symbol: int
                line: int
                column: int
                for offset in range(frames_len):
                    mod_symbol = stream.read_vu32().value
                    type_symbol = stream.read_vu32().value
                    fn_symbol = stream.read_vu32().value
                    line = stream.read_vu32().value
                    column = stream.read_vu32().value
                    frames[offset] = std_n.core._Error.Frame(
                        mod_symbol, type_symbol, fn_symbol, line, column
                    )
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
                key: __T
                value: __U
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

            def keys(self) -> dict_keys[__T]:
                return self.map.keys()

            def values(self) -> dict_values[__U]:
                return self.map.values()

            def items(self) -> dict_items[__T, __U]:
                return self.map.items()

            def __len__(self) -> int:
                return len(self.map)

            def __getitem__(self, key: __T) -> __U:
                return self.map[key]

            def __setitem__(self, key: __T, value: __U) -> None:
                self.map[key] = value

            def __delitem__(self, key: __T) -> None:
                del self.map[key]

            def clear(self) -> None:
                self.map.clear()

            def __hashable(key: Any) -> Any:
                if type(key) in [c_char, c_int64, c_double, c_ubyte]:
                    return key.value

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
                self.data: list[__T]
                super().__init__(type, None)

            def _save(self, stream: GreyCat._Stream) -> None:
                stream.write_vu32(c_uint32(self.cols))
                stream.write_vu32(c_uint32(self.rows))
                meta_offset: int
                col_meta: std_n.core._Table.TableColumnMeta
                for meta_offset in range(len(self.meta)):
                    col_meta = self.meta[meta_offset]
                    stream.write_i8(col_meta.col_type)
                    stream.write_bool(col_meta.meta_index)
                    if col_meta.col_type in [PrimitiveType.OBJECT, PrimitiveType.ENUM]:
                        stream.write_vu32(col_meta.type)
                col: int
                row: int
                o: GreyCat.Object
                for col in range(self.cols):
                    match self.meta[col].col_type.value:
                        case PrimitiveType.NULL.value:
                            pass
                        case PrimitiveType.INT.value:
                            for row in range(self.rows):
                                stream.write_vi64(c_int64(self.data[col * self.rows + row]))
                        case PrimitiveType.FLOAT.value:
                            for row in range(self.rows):
                                stream.write_f64(c_double(self.data[col * self.rows + row]))
                        case PrimitiveType.TIME.value:
                            for row in range(self.rows):
                                o = self.data[col * self.rows + row]
                                o._save(stream)
                        case PrimitiveType.DURATION.value:
                            for row in range(self.rows):
                                o = self.data[col * self.rows + row]
                                o._save(stream)
                        case PrimitiveType.ENUM.value:
                            for row in range(self.rows):
                                o = self.data[col * self.rows + row]
                                o._save(stream)
                        case PrimitiveType.OBJECT.value:
                            for row in range(self.rows):
                                o = self.data[col * self.rows + row]
                                o._save(stream)
                        case _:
                            for row in range(self.rows):
                                stream.write(self.data[col * self.rows + row])

            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat._Stream) -> Any:
                cols: Final[int] = stream.read_vu32().value
                rows: Final[int] = stream.read_vu32().value
                meta: list[std_n.core._Table.TableColumnMeta] = [None] * cols
                meta_offset: int
                meta_col_type: c_ubyte
                meta_index: bool
                meta_type: c_uint32
                for meta_offset in range(cols):
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
                    meta[meta_offset] = std_n.core._Table.TableColumnMeta(
                        meta_col_type, meta_type, meta_index
                    )
                data: list[Any] = [None] * (cols * rows)
                col: int
                row: int
                greycat_type: GreyCat.Type
                for col in range(cols):
                    match meta[col].col_type.value:
                        case PrimitiveType.NULL.value:
                            pass
                        case PrimitiveType.INT.value:
                            for row in range(rows):
                                data[col * rows + row] = stream.read_vi64().value
                        case PrimitiveType.FLOAT.value:
                            for row in range(rows):
                                data[col * rows + row] = stream.read_f64().value
                        case PrimitiveType.TIME.value:
                            for row in range(rows):
                                data[col * rows + row] = std_n.core._time.load(
                                    type.greycat.types[
                                        type.greycat.type_offset_core_time
                                    ],
                                    stream,
                                )
                        case PrimitiveType.DURATION.value:
                            for row in range(rows):
                                data[col * rows + row] = std_n.core._duration.load(
                                    type.greycat.types[
                                        type.greycat.type_offset_core_duration
                                    ],
                                    stream,
                                )
                        case PrimitiveType.ENUM.value:
                            greycat_type = type.greycat.types[meta[col].type.value]
                            for row in range(rows):
                                data[col * rows + row] = greycat_type.loader(greycat_type, stream)
                        case PrimitiveType.OBJECT.value:
                            greycat_type = type.greycat.types[meta[col].type.value]
                            for row in range(rows):
                                data[col * rows + row] = greycat_type.loader(greycat_type, stream)
                        case _:
                            for row in range(rows):
                                data[col * rows + row] = stream.read()
                t: std_n.core._Table = type.factory(type, [])
                t.cols = cols
                t.rows = rows
                t.meta = meta
                t.data = data
                return t

            class TableColumnMeta:
                def __init__(
                    self, col_type: c_ubyte, type: c_uint32, index: bool
                ) -> None:
                    self.col_type: Final[c_ubyte] = col_type
                    self.type: Final[c_uint32] = type
                    self.meta_index: Final[bool] = index

            try:
                numpy
            except NameError:
                pass
            else:

                def to_numpy(self) -> numpy.ndarray:
                    return numpy.reshape(self.data, (self.rows, self.cols), 'F')

                @staticmethod
                def from_numpy(
                    greycat: GreyCat, nda: numpy.ndarray
                ) -> std_n.core._Table:
                    type: GreyCat.Type = greycat.types_by_name['core::Table']
                    table: std_n.core._Table = type.factory(type, None)
                    table.data = nda.flatten('F').tolist()
                    table.rows = nda.shape[0]
                    table.cols = nda.shape[1]
                    return table

                try:
                    pandas
                except NameError:
                    pass
                else:

                    def to_pandas(self) -> pandas.DataFrame:
                        return pandas.DataFrame(self.to_numpy())

                    @staticmethod
                    def from_pandas(
                        greycat: GreyCat, df: pandas.DataFrame
                    ) -> std_n.core._Table:
                        return std_n.core._Table.from_numpy(greycat, df.to_numpy())

        class _Tensor(GreyCat.Object):
            def __init__(self, type: GreyCat.Type) -> None:
                self.shape: list[c_uint32]
                self.tensor_type: c_byte
                self.size: c_uint32
                self.data: bytes
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
            def load(type: GreyCat.Type, stream: GreyCat._Stream) -> Any:
                nb_dim: Final[int] = stream.read_i8().value
                tensor_type: Final[c_byte] = stream.read_i8()
                shape: list[int] = [0] * nb_dim
                offset: int
                for offset in range(nb_dim):
                    shape[offset] = stream.read_i32()
                size: c_uint32 = stream.read_i32()
                bin_size: int = size.value
                match tensor_type.value:
                    case 0:
                        bin_size *= 4
                    case 1:
                        bin_size *= 8
                    case 2:
                        bin_size *= 4
                    case 3:
                        bin_size *= 8
                    case 4:
                        bin_size *= 8
                    case 5:
                        bin_size *= 16
                    case _:
                        raise ValueError(f"{tensor_type}")
                res: std_n.core._Tensor = type.factory(type, [])
                res.shape = shape
                res.tensor_type = tensor_type
                res.size = size
                res.data = stream.read_i8_array(bin_size)
                return res

        class _nodeIndexBucket(GreyCat.Object):
            def __init__(type: GreyCat.Type) -> None:
                super().__init__(type, None)

            @final
            def _save(self, stream: GreyCat._Stream) -> None:
                offset: int
                if self.attributes is None:
                    stream.write_i32(0)
                else:
                    stream.write_i32(len(self.attributes))
                    for offset in range(len(self.attributes)):
                        stream.write(self.attributes[offset])

            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat._Stream) -> Any:
                size: Final[int] = stream.read_i32().value
                data: Final[list[Any]] = [None] * size
                offset: int
                for offset in range(size):
                    data[offset] = stream.read()
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
            pass

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
            pass

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
            pass

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
                values: list[Any] = [None] * capacity
                values_offset: int
                for values_offset in range(capacity):
                    values[values_offset] = std_n.util._SlidingWindow.ValueTime(
                        stream.read(), stream.read_vi64()
                    )
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
                value_times: list[std_n.util._TimeWindow.ValueTime] = [None] * capacity
                value_time_offset: int
                for value_time_offset in range(capacity):
                    value_times[value_time_offset] = std_n.util._TimeWindow.ValueTime(
                        stream.read(), stream.read_vi64()
                    )
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
