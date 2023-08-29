from __future__ import annotations

from _collections_abc import dict_keys, dict_values, dict_items
from ctypes import *
from struct import pack, unpack
from typing import *

from ai.greycat.greycat import GreyCat, PrimitiveType

__T = TypeVar("__T")
__U = TypeVar("__U")


class std_n:
    class core:

        # Primitive types

        class _node(Generic[__T], GreyCat.Object):
            def __init__(self, type: GreyCat.Type) -> None:
                self.ref: c_int64
                super(type, None)

            @final
            def save_type(self, stream: GreyCat._Stream) -> None:
                stream.write_i8(PrimitiveType.NODE)

            @final
            def save(self, stream: GreyCat._Stream) -> None:
                stream.write_vu64(self.ref)

            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat._Stream) -> Any:
                res: std_n.core._node = type.factory(type)
                res.ref = stream.read_vu64()
                return res

        class _nodeTime(Generic[__T], GreyCat.Object):
            def __init__(self, type: GreyCat.Type) -> None:
                self.ref: c_int64
                super(type, None)

            @final
            def save_type(self, stream: GreyCat._Stream) -> None:
                stream.write_i8(PrimitiveType.NODE)

            @final
            def save(self, stream: GreyCat._Stream) -> None:
                stream.write_vu64(self.ref)

            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat._Stream) -> Any:
                res: std_n.core._nodeTime = type.factory(type)
                res.ref = stream.read_vu64()
                return res

        class _nodeIndex(Generic[__T, __U], GreyCat.Object):
            def __init__(self, type: GreyCat.Type) -> None:
                self.ref: c_int64
                super(type, None)

            @final
            def save_type(self, stream: GreyCat._Stream) -> None:
                stream.write_i8(PrimitiveType.NODE)

            @final
            def save(self, stream: GreyCat._Stream) -> None:
                stream.write_vu64(self.ref)

            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat._Stream) -> Any:
                res: std_n.core._nodeIndex = type.factory(type)
                res.ref = stream.read_vu64()
                return res

        class _nodeList(Generic[__T], GreyCat.Object):
            def __init__(self, type: GreyCat.Type) -> None:
                self.ref: c_int64
                super(type, None)

            @final
            def save_type(self, stream: GreyCat._Stream) -> None:
                stream.write_i8(PrimitiveType.NODE)

            @final
            def save(self, stream: GreyCat._Stream) -> None:
                stream.write_vu64(self.ref)

            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat._Stream) -> Any:
                res: std_n.core._nodeList = type.factory(type)
                res.ref = stream.read_vu64()
                return res

        class _nodeGeo(Generic[__T], GreyCat.Object):
            def __init__(self, type: GreyCat.Type) -> None:
                self.ref: c_int64
                super(type, None)

            @final
            def save_type(self, stream: GreyCat._Stream) -> None:
                stream.write_i8(PrimitiveType.NODE)

            @final
            def save(self, stream: GreyCat._Stream) -> None:
                stream.write_vu64(self.ref)

            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat._Stream) -> Any:
                res: std_n.core._nodeGeo = type.factory(type)
                res.ref = stream.read_vu64()
                return res

        class _function(GreyCat.Object):
            def __init__(self, type: GreyCat.Type) -> None:
                super(type, None)

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
                super(type, None)
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
                geo: std_n.core._geo = type.factory(type)
                value: c_int64 = stream.read_i64()
                geo.geocode = value
                lat_offset, lng_offset: tuple[int, int] = std_n.core._geo.__deinterleave64(value)
                geo.lat = std_n.core._geo.__GC_CORE_GEO_LAT_MIN + ((lat_offset + 0.5) / 4294967296) * (std_n.core._geo.__GC_CORE_GEO_LAT_MAX - std_n.core._geo.__GC_CORE_GEO_LAT_MIN)
                geo.lng = std_n.core._geo.__GC_CORE_GEO_LNG_MIN + ((lng_offset + 0.5) / 4294967296) * (std_n.core._geo.__GC_CORE_GEO_LNG_MAX - std_n.core._geo.__GC_CORE_GEO_LNG_MIN)

            def __str__(self) -> str:
                return f'geo{{lat={self.lat},lng={self.lng}}}'

            @staticmethod
            def __interleave64(xlo: int, ylo: int)->c_int64:
                B: list[int] = [6148914691236517205, 3689348814741910323, 1085102592571150095, 71777214294589695, 281470681808895]
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
                B: list[int] = [6148914691236517205, 3689348814741910323, 1085102592571150095, 71777214294589695, 281470681808895, 4294967295]
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
                    latitude = std_n.core._geo.__GC_CORE_GEO_LAT_MAX - std_n.core._geo.__GC_CORE_GEO_LAT_EPS
                if longitude < std_n.core._geo.__GC_CORE_GEO_LNG_MIN:
                    longitude = std_n.core._geo.__GC_CORE_GEO_LNG_MIN
                if longitude >= std_n.core._geo.__GC_CORE_GEO_LNG_MAX:
                    longitude = std_n.core._geo.__GC_CORE_GEO_LNG_MAX - std_n.core._geo.__GC_CORE_GEO_LAT_EPS
                lat_offset: float = (latitude - std_n.core._geo.__GC_CORE_GEO_LAT_MIN) / (std_n.core._geo.__GC_CORE_GEO_LAT_MAX - std_n.core._geo.__GC_CORE_GEO_LAT_MIN)
                lng_offset: float = (longitude - std_n.core._geo.__GC_CORE_GEO_LNG_MIN) / (std_n.core._geo.__GC_CORE_GEO_LNG_MAX - std_n.core._geo.__GC_CORE_GEO_LNG_MIN);
                lat_offset *= 4294967296
                lng_offset *= 4294967296
                return std_n.core._geo.__interleave64(int(lat_offset), int(lng_offset))

        class _time(GreyCat.Object):
            def __init__(self) -> None:
                self.value: c_int64
                super(type, None)
            
            @final
            def _save_type(self, stream: GreyCat._Stream)->None:
                stream.write_i8(PrimitiveType.TIME)
            
            @final
            def _save(self, stream:GreyCat._Stream)->None:
                stream.write_vi64(self.value)

            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat._Stream)->Any:
                res: std_n.core._time = type.factory(type)
                res.value = stream.read_vi64()
                return res

        class _duration(GreyCat.Object):
            def __init__(self) -> None:
                self.value: c_int64
                super(type, None)
            
            @final
            def _save_type(self, stream: GreyCat._Stream)->None:
                stream.write_i8(PrimitiveType.TIME)
            
            @final
            def _save(self, stream:GreyCat._Stream)->None:
                stream.write_vi64(self.value)

            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat._Stream)->Any:
                res: std_n.core._duration = type.factory(type)
                res.value = stream.read_vi64()
                return res

        class _ti2d(GreyCat.Object):
            __INT32_MIN: int = -2147483648
            __UINT32_MIN: int = 2147483648

            def __init__(self, type: GreyCat.Type) -> None:
                self.x0: int
                self.x1: int
                super(type, None)
            
            @final
            def _save_type(self, stream: GreyCat._Stream) -> None:
                stream.write_i8(PrimitiveType.TU2D)

            @final
            def _save(self, stream:GreyCat._Stream)->None:
                stream.write_i64(self.__interleave())

            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat._Stream) -> Any:
                res: std_n.core._ti2d = type.factory(type)
                res.__deinterleave(stream.read_i64)
                return res
            
            def __str__(self) -> str:
                return f'ti2d{{x0={self.x0},x1={self.x1}}}'
            
            def __interleave(self) -> c_int64:
                return std_n.core.__interleave64_2d(self.x0 + std_n.core._ti2d.__UINT32_MIN, self.x1 + std_n.core._ti2d.__UINT32_MIN)
            
            def __deinterleave(self, interleaved: c_int64)->None:
                dc: int = std_n.core.__deinterleave64_2d(interleaved)
                self.x0 = c_int32(dc + std_n.core._ti2d.__INT32_MIN).value
                self.x1 = c_int32((dc >> 32) + std_n.core._ti2d.__INT32_MIN).value

        class _ti3d(GreyCat.Object):
            __INT21_MIN: int = -1048575 - 1
            __INT21_MAX: int = 1048575
            __UINT21_MIN: int = 4293918720

            def __init__(self, type: GreyCat.Type)->None:
                self.x0: int
                self.x1: int
                self.x2: int
                super(type, None)

            @final
            def _save_type(self, stream: GreyCat._Stream)->None:
                stream.write_i8(PrimitiveType.TU3D)
            
            @final
            def _save(self, stream: GreyCat._Stream)->None:
                stream.write_i64(self.__interleave())

            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat._Stream) -> Any:
                res: std_n.core._ti3d = type.factory(type)
                res.__deinterleave(stream.read_i64())
                return res

            def __str__(self) -> str:
                return f'ti3d{{x0={self.x0},x1={self.x1},x2={self.x2}}}'
            
            def __interleave(self) -> c_int64:
                return std_n.core.__interleave64_3d(self.x0 + std_n.core._ti3d.__UINT21_MIN, self.x1 + std_n.core._ti3d.__UINT21_MIN, self.x2 + std_n.core._ti3d.__UINT21_MIN)
            
            def __deinterleave(self, interleaved: c_int64) -> None:
                B: list[int] = [0x10c30c30c30c30c3, 0x100f00f00f00f00f, 0x001f0000ff0000ff, 0xffff00000000ffff, 0x0001fffff]
                S: list[int] = [2, 4, 8, 16, 32]

                self.x0 = std_n.core.__deinterleave64_3d(interleaved) + std_n.core._ti3d.__INT21_MIN
                self.x1 = std_n.core.__deinterleave64_3d(c_int64(interleaved.value >> 1)) + std_n.core._ti3d.__INT21_MIN
                self.x2 = std_n.core.__deinterleave64_3d(c_int64(interleaved.value >> 2)) + std_n.core._ti3d.__INT21_MIN
        
        class _ti4d(GreyCat.Object):
            __INT16_MIN: int = -32768
            __INT16_MAX: int = 32767
            __UINT16_MIN: int = 32768

            def __init__(self, type: GreyCat.Type)->None:
                self.x0: int
                self.x1: int
                self.x2: int
                self.x3: int
                super(type, None)

            @final
            def _save_type(self, stream: GreyCat._Stream) -> None:
                stream.write_i8(PrimitiveType.TU4D)
            
            @final
            def _save(self, stream: GreyCat._Stream)->None:
                stream.write_i64(self.__interleave())

            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat._Stream) -> Any:
                res: std_n.core._ti4d = type.factory(type)
                res.__deinterleave(stream.read_i64())
                return res
            
            def __str__(self) -> str:
                return f'ti4d{{x0={self.x0},x1={self.x1},x2={self.x2},x3={self.x3}}}'
            
            def __interleave(self) -> c_int64:
                return std_n.core.__interleave64_2d(
                    std_n.core.__interleave64_2d(self.x0 + std_n.core._ti4d.__UINT16_MIN, self.x2 + std_n.core._ti4d.__UINT16_MIN).value, 
                    std_n.core.__interleave64_2d(self.x1 + std_n.core._ti4d.__UINT16_MIN, self.x3 + std_n.core._ti4d.__UINT16_MIN).value
                )
            
            def __deinterleave(self, interleaved: c_int64)->None:
                x3120: int = std_n.core.__deinterleave64_2d(interleaved)
                x20: int = std_n.core.__deinterleave64_2d(c_int64(x3120 & 0xffffffff))
                x31: int = std_n.core.__deinterleave64_2d(c_int64(x3120 >> 32))
                self.x0 = (x20 & 0xffff) + std_n.core._ti4d.__INT16_MIN
                self.x1 = (x31 & 0xffff) + std_n.core._ti4d.__INT16_MIN
                self.x2 = (x20 >> 32) + std_n.core._ti4d.__INT16_MIN
                self.x3 = (x31 >> 32) + std_n.core._ti4d.__INT16_MIN

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
                super(type, None)

            @final
            def _save_type(self, stream: GreyCat._Stream) -> None:
                stream.write_i8(PrimitiveType.TU5D)

            @final
            def _save(self, stream: GreyCat._Stream) -> None:
                stream.write_i64(self.__interleave())

            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat._Stream)->Any:
                res: std_n.core._ti5d = type.factory(type)
                res.__deinterleave(stream.read_i64())
                return res
            
            def __str__(self) -> str:
                return f'ti5d{{x0={self.x0},x1={self.x1},x2={self.x2},x3={self.x3},x4={self.x4}}}'
            
            def __interleave(self) -> c_int64:
                return std_n.core.__interleave64_5d(
                    self.x0 + std_n.core._ti5d.__UINT12_MIN,
                    self.x1 + std_n.core._ti5d.__UINT12_MIN,
                    self.x2 + std_n.core._ti5d.__UINT12_MIN,
                    self.x3 + std_n.core._ti5d.__UINT12_MIN,
                    self.x3 + std_n.core._ti5d.__UINT12_MIN
                    )

            def __deinterleave(self, interleaved: c_int64) -> None:
                B: list[int] = [0x0c0300c0300c03, 0x0f0000f0000f, 0x00f00000000ff, 0x0fff]
                S: list[int] = [4, 8, 16, 32]

                self.x0 = std_n.core.__deinterleave64_5d(interleaved) + std_n.core._ti5d.__INT12_MIN
                self.x1 = std_n.core.__deinterleave64_5d(c_int64(interleaved.value >> 1)) + std_n.core._ti5d.__INT12_MIN
                self.x2 = std_n.core.__deinterleave64_5d(c_int64(interleaved.value >> 2)) + std_n.core._ti5d.__INT12_MIN
                self.x3 = std_n.core.__deinterleave64_5d(c_int64(interleaved.value >> 3)) + std_n.core._ti5d.__INT12_MIN
                self.x4 = std_n.core.__deinterleave64_5d(c_int64(interleaved.value >> 4)) + std_n.core._ti5d.__INT12_MIN
        
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
                super(type)

            @final
            def _save_type(self, stream: GreyCat._Stream) -> None:
                stream.write_i8(PrimitiveType.TU6D)

            @final
            def _save(self, stream: GreyCat._Stream) -> None:
                stream.write_i64(self.__interleave())

            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat._Stream) -> Any:
                res: std_n.core._ti6d = type.factory(type)
                res.__deinterleave(stream.read_i64())
                return res
            
            def __str__(self) -> str:
                return f'ti6d{{x0={self.x0},x1={self.x1},x2={self.x2},x3={self.x3},x4={self.x4},x5={self.x5}}}'
            
            def __interleave(self) -> c_int64:
                return std_n.core.__interleave64_3d(
                    std_n.core.__interleave64_2d((self.x0 + std_n.core._ti6d.__UINT10_MIN) & 0x3ff, (self.x3 + std_n.core._ti6d.__UINT10_MIN) & 0x3ff).value,
                    std_n.core.__interleave64_2d((self.x1 + std_n.core._ti6d.__UINT10_MIN) & 0x3ff, (self.x4 + std_n.core._ti6d.__UINT10_MIN) & 0x3ff).value,
                    std_n.core.__interleave64_2d((self.x2 + std_n.core._ti6d.__UINT10_MIN) & 0x3ff, (self.x5 + std_n.core._ti6d.__UINT10_MIN) & 0x3ff).value,
                )
            
            def __deinterleave(self, interleaved: c_int64) -> None:
                y30: int = std_n.core.__deinterleave64_2d(c_int64(std_n.core.__deinterleave64_3d(interleaved)))
                y41: int = std_n.core.__deinterleave64_2d(c_int64(std_n.core.__deinterleave64_3d(c_int64(interleaved.value >> 1))))
                y52: int = std_n.core.__deinterleave64_2d(c_int64(std_n.core.__deinterleave64_3d(c_int64(interleaved.value >> 2))))

                self.x0 = (y30 & 0x3ff) + std_n.core._ti6d.__INT10_MIN
                self.x1 = (y41 & 0x3ff) + std_n.core._ti6d.__INT10_MIN
                self.x2 = (y52 & 0x3ff) + std_n.core._ti6d.__INT10_MIN
                self.x3 = (y30 >> 32) + std_n.core._ti6d.__INT10_MIN
                self.x4 = (y41 >> 32) + std_n.core._ti6d.__INT10_MIN
                self.x5 = (y52 >> 32) + std_n.core._ti6d.__INT10_MIN

        class _ti10d(GreyCat.Object):
            __INT6_MIN: -31 - 1
            __INT6_MAX: 31
            __UINT6_MIN: 224

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
                super(type, None)
            
            @final
            def _save_type(self, stream: GreyCat._Stream) -> None:
                stream.write_i8(PrimitiveType.TU10D)

            @final
            def _save(self, stream: GreyCat._Stream) -> None:
                stream.write_i64(self.__interleave())

            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat._Stream) -> Any:
                res: std_n.core._ti10d = type.factory(type)
                res.__deinterleave(stream.read_i64())
                return res
            
            def __str__(self) -> str:
                return f'ti2d{{x0={self.x0},x1={self.x1},x2={self.x2},x3={self.x3},x4={self.x4},x5={self.x5},x6={self.x6},x7={self.x7},x8={self.x8},x9={self.x9}}}'
            
            def __interleave(self) -> c_int64:
                return std_n.core.__interleave64_5d(
                    std_n.core.__interleave64_2d((self.x0 + std_n.core._ti10d.__UINT6_MIN) & 0x3f, (self.x5 + std_n.core._ti10d.__UINT6_MIN) & 0x3f),
                    std_n.core.__interleave64_2d((self.x1 + std_n.core._ti10d.__UINT6_MIN) & 0x3f, (self.x6 + std_n.core._ti10d.__UINT6_MIN) & 0x3f),
                    std_n.core.__interleave64_2d((self.x2 + std_n.core._ti10d.__UINT6_MIN) & 0x3f, (self.x7 + std_n.core._ti10d.__UINT6_MIN) & 0x3f),
                    std_n.core.__interleave64_2d((self.x3 + std_n.core._ti10d.__UINT6_MIN) & 0x3f, (self.x8 + std_n.core._ti10d.__UINT6_MIN) & 0x3f),
                    std_n.core.__interleave64_2d((self.x4 + std_n.core._ti10d.__UINT6_MIN) & 0x3f, (self.x9 + std_n.core._ti10d.__UINT6_MIN) & 0x3f)
                )
            
            def __deinterleave(self, interleaved: c_int64) -> None:
                self.x0 = (std_n.core.__deinterleave64_2d(c_int64(std_n.core.__deinterleave64_5d(interleaved))) & 0x3f) + std_n.core._ti10d.__INT6_MIN
                self.x1 = (std_n.core.__deinterleave64_2d(c_int64(std_n.core.__deinterleave64_5d(c_int64(interleaved.value >> 1)))) & 0x3f) + std_n.core._ti10d.__INT6_MIN
                self.x2 = (std_n.core.__deinterleave64_2d(c_int64(std_n.core.__deinterleave64_5d(c_int64(interleaved.value >> 2)))) & 0x3f) + std_n.core._ti10d.__INT6_MIN
                self.x3 = (std_n.core.__deinterleave64_2d(c_int64(std_n.core.__deinterleave64_5d(c_int64(interleaved.value >> 3)))) & 0x3f) + std_n.core._ti10d.__INT6_MIN
                self.x4 = (std_n.core.__deinterleave64_2d(c_int64(std_n.core.__deinterleave64_5d(c_int64(interleaved.value >> 4)))) & 0x3f) + std_n.core._ti10d.__INT6_MIN
                self.x5 = (std_n.core.__deinterleave64_2d(c_int64(std_n.core.__deinterleave64_5d(c_int64(interleaved.value >> 5)))) & 0x3f) + std_n.core._ti10d.__INT6_MIN
                self.x6 = (std_n.core.__deinterleave64_2d(c_int64(std_n.core.__deinterleave64_5d(c_int64(interleaved.value >> 6)))) & 0x3f) + std_n.core._ti10d.__INT6_MIN
                self.x7 = (std_n.core.__deinterleave64_2d(c_int64(std_n.core.__deinterleave64_5d(c_int64(interleaved.value >> 7)))) & 0x3f) + std_n.core._ti10d.__INT6_MIN
                self.x8 = (std_n.core.__deinterleave64_2d(c_int64(std_n.core.__deinterleave64_5d(c_int64(interleaved.value >> 8)))) & 0x3f) + std_n.core._ti10d.__INT6_MIN
                self.x9 = (std_n.core.__deinterleave64_2d(c_int64(std_n.core.__deinterleave64_5d(c_int64(interleaved.value >> 9)))) & 0x3f) + std_n.core._ti10d.__INT6_MIN
            
        class _tf2d(GreyCat.Object):
            def __init__(self, type: GreyCat.Type) -> None:
                self.x0: float
                self.x1: float
                super(type, None)

            @final
            def _save_type(self, stream: GreyCat._Stream) -> None:
                stream.write_i8(PrimitiveType.TUF2D)

            @final
            def _save(self, stream: GreyCat._Stream) -> None:
                stream.write_i64(self.__interleave())

            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat._Stream) -> Any:
                res: std_n.core._tf2d = type.factory(type)
                res.__deinterleave(stream.read_i64())
                return res

            def __str__(self) -> str:
                return f'tf2d{{x0={self.x0},x1={self.x1}}}'
            
            def __interleave(self) -> c_int64:
                return std_n.core.__interleave64_2d(
                    unpack("q", pack("d", self.x0))[0] + std_n.core._ti2d.__UINT32_MIN,
                    unpack("q", pack("d", self.x1))[0] + std_n.core._ti2d.__UINT32_MIN
                )

            def __deinterleave(self, interleaved: c_int64) -> None:
                dc: int = std_n.core.__deinterleave64_2d(interleaved)
                self.x0 = unpack("d", pack("q", c_int32(dc + std_n.core._ti2d.__INT32_MIN).value))[0]
                self.x1 = unpack("d", pack("q", c_int32((dc >> 32) + std_n.core._ti2d.__INT32_MIN).value))[0]

        class _tf3d(GreyCat.Object):
            def __init__(self, type: GreyCat.Type) -> None:
                self.x0: float
                self.x1: float
                self.x2: float
                super(type, None)
            
            @final
            def _save_type(self, stream: GreyCat._Stream) -> None:
                stream.write(PrimitiveType.TUF3D)

            @final
            def _save(self, stream: GreyCat._Stream) -> None:
                stream.write_i64(self.__interleave())

            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat._Stream) -> Any:
                res: std_n.core._tf3d = type.factory(type)
                res.__deinterleave(stream.read_i64())
                return res
            
            def __str__(self) -> str:
                return f'tf2d{{x0={self.x0},x1={self.x1},x2={self.x2}}}'
            
            def __interleave(self) -> c_int64:
                return std_n.core.__interleave64_3d(
                    (unpack("q", pack("d", self.x0))[0] >> 11) + std_n.core._ti3d.__UINT21_MIN,
                    (unpack("q", pack("d", self.x1))[0] >> 11) + std_n.core._ti3d.__UINT21_MIN,
                    (unpack("q", pack("d", self.x2))[0] >> 11) + std_n.core._ti3d.__UINT21_MIN,
                )

            def __deinterleave(self, interleaved: c_int64) -> None:
                self.x0 = unpack("d", pack("q", c_int32(
                    (std_n.core.__deinterleave64_3d(interleaved) + std_n.core._ti3d.__INT21_MIN) << 11
                ).value))[0]
                self.x1 = unpack("d", pack("q", c_int32(
                    (std_n.core.__deinterleave64_3d(c_int64(interleaved.value >> 1)) + std_n.core._ti3d.__INT21_MIN) << 11
                ).value))[0]
                self.x2 = unpack("d", pack("q", c_int32(
                    (std_n.core.__deinterleave64_3d(c_int64(interleaved.value >> 2)) + std_n.core._ti3d.__INT21_MIN) << 11
                ).value))[0]
        
        class _tf4d(GreyCat.Object):
            def __init__(self, type: GreyCat.Type) -> None:
                self.x0: float
                self.x1: float
                self.x2: float
                self.x3: float
                super(type, None)

            @final
            def _save_type(self, stream: GreyCat._Stream) -> None:
                stream.write_i8(PrimitiveType.TUF4D)

            @final
            def _save(self, stream: GreyCat._Stream) -> None:
                stream.write_i64(self.__interleave())

            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat._Stream) -> Any:
                res: std_n.core._tf4d = type.factory(type)
                res.__deinterleave(stream.read_i64())
                return res
            
            def __str__(self) -> str:
                return f'tf2d{{x0={self.x0},x1={self.x1},x2={self.x2},x3={self.x3}}}'
            
            def __interleave(self) -> c_int64:
                return std_n.core.__interleave64_2d(
                    std_n.core.__interleave64_2d(
                        (unpack("q", pack("d", self.x0))[0] >> 16) + std_n.core._ti4d.__UINT16_MIN,
                        (unpack("q", pack("d", self.x2))[0] >> 16) + std_n.core._ti4d.__UINT16_MIN
                    ).value,
                    std_n.core.__interleave64_2d(
                        (unpack("q", pack("d", self.x1))[0] >> 16) + std_n.core._ti4d.__UINT16_MIN,
                        (unpack("q", pack("d", self.x3))[0] >> 16) + std_n.core._ti4d.__UINT16_MIN
                    ).value
                )
            
            def __deinterleave(self, interleaved: c_int64) -> None:
                d3120: c_int64 = c_int64(std_n.core.__deinterleave64_2d(interleaved))
                d20: int = std_n.core.__deinterleave64_2d(d3120 & 0xffffffff)
                d31: int = std_n.core.__deinterleave64_2d(d3120 >> 32)
                self.x0 = unpack("d", pack("q", c_int32(((d20 & 0xffff) + std_n.core._ti4d.__INT16_MIN) << 16).value))[0]
                self.x1 = unpack("d", pack("q", c_int32(((d31 & 0xffff) + std_n.core._ti4d.__INT16_MIN) << 16).value))[0]
                self.x2 = unpack("d", pack("q", c_int32(((d20 >> 32) + std_n.core._ti4d.__INT16_MIN) << 16).value))[0]
                self.x3 = unpack("d", pack("q", c_int32(((d31 >> 32) + std_n.core._ti4d.__INT16_MIN) << 16).value))[0]

        # Object types

        class _Array(Generic[__T], GreyCat.Object):
            def __init__(self, type: GreyCat.Type) -> None:
                super(type, None)

            @final
            def _save(self, stream: GreyCat._Stream) -> None:
                stream.write_vu32(c_uint32(len(self)))
                offset: int
                for offset in range(len(self)):
                    stream.write(self[offset])

            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat._Stream) -> Any:
                size: int = stream.read_vu32().value
                array: std_n.core._Array = type.factory(type)
                array.attributes = [None] * size
                offset: int
                for offset in range(size):
                    array.set(offset, stream.read())
                return array
            
            def __len__(self) -> int:
                return len(self.attributes)
            
            def __iter__(self) -> Iterator[__T]:
                return self.attributes.__iter__()
            
            @overload
            def __getitem__(self, __i: SupportsIndex) -> __T:
                return self.attributes[__i]
            
            @overload
            def __getitem__(self, __s: slice) -> list[__T]:
                return self.attributes[__s]
            
            @overload
            def __setitem__(self, __key: SupportsIndex, __value: __T) -> None:
                self.attributes[__key] = __value

            @overload
            def __setitem__(self, __key: slice, __value: Iterable[__T]) -> None:
                self.attributes[__key] = __value
            
            def __delitem__(self, __key: SupportsIndex | slice) -> None:
                del self.attributes[__key]

            def __contains__(self, __key: object) -> bool:
                return __key in self.attributes
            
            def __str__(self) -> str:
                res: str = '['
                for offset in range(len(self.attributes)):
                    if (offset > 0):
                        res = f'{res},'
                    res = f'{res}{self.attributes[offset]}'
                return f'{res}]'
        
        class _Date(GreyCat.Object):
            def __init__(self, type: GreyCat.Type) -> None:
                self.localized_epoch_s: int
                self.epoch_us: int
                self.time_zone: int
                super(type, None)

            @final
            def _save(self, stream: GreyCat._Stream) -> None:
                stream.write_vi64(self.localized_epoch_s)
                stream.write_vi64(self.epoch_us)
                stream.write_vu32(self.time_zone)
            
            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat._Stream) -> Any:
                res: std_n.core._Date = type.factory(type)
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
                super(type, None)
            
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
                    frames[offset] = std_n.core._Error.Frame(mod_symbol, type_symbol, fn_symbol, line, column)
                res: std_n.core._Error = type.factory(type)
                res.code = code
                res.frames = frames
                res.msg = stream.read_string(msg_len)
                res.value = stream.read()
                return res
            
            def __str__(self) -> str:
                return f"{self.type_.name}{{msg='{self.msg}', value={self.value}}}"

            
            class Frame:
                def __init__(self, mod_symbol: int, type_symbol: int, fn_symbol: int, line: int, column: int) -> None:
                    self.mod_symbol: Final[int] = mod_symbol
                    self.type_symbol: Final[int] = type_symbol
                    self.fn_symbol: Final[int] = fn_symbol
                    self.line: Final[int] = line
                    self.column: Final[int] = column
        
        class _Map(Generic[__T, __U], GreyCat.Object):
            def __init__(self, type: GreyCat.Type) -> None:
                self.map: Final[dict] = {}
                self(type, None)
            
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
                map: Final[std_n.core._Map] = type.factory(type)
                map_length: int = stream.read_vu32().value
                for _ in range(map_length):
                    map[stream.read()] = stream.read()
                    # map.set(stream.read(), stream.read())
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

        class _String(GreyCat.Object):
            def __init__(self, type: GreyCat.Type) -> None:
                super(type, None)
            
            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat._Stream) -> Any:
                len_: int = stream.read_vu32()
                if 0 != (len_ & 1):
                    return type.greycat.symbols[len_ >> 1]
                stream.read_string(len_ >> 1)
        
        class _Table(Generic[__T], GreyCat.Object):
            def __init__(self, type: GreyCat.Type) -> None:
                self.cols: int
                self.rows: int
                self.meta: list[std_n.core._Table.TableColumnMeta]
                self.data: list[__T]
                super(type, None)
            
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
                    match self.meta[col].col_type:
                        case PrimitiveType.NULL:
                            pass
                        case PrimitiveType.INT:
                            for row in range(self.rows):
                                stream.write_vi64(c_int64(self.data[col + row]))
                        case PrimitiveType.FLOAT:
                            for row in range(self.rows):
                                stream.write_f64(c_double(self.data[col + row]))
                        case PrimitiveType.TIME:
                            for row in range(self.rows):
                                o = self.data[col + row]
                                o._save(stream)
                        case PrimitiveType.DURATION:
                            for row in range(self.rows):
                                o = self.data[col + row]
                                o._save(stream)
                        case PrimitiveType.ENUM:
                            for row in range(self.rows):
                                o = self.data[col + row]
                                o._save(stream)
                        case _:
                            for row in range(self.rows):
                                stream.write(self.data[col + row])

            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat._Stream) -> Any:
                cols: Final[int] = stream.read_vu32().value
                rows: Final[int] = stream.read_vu32().value
                meta: list[std_n.core._Table.TableColumnMeta] = [None] * cols
                meta_offset: int
                meta_col_type: c_byte
                meta_index: bool
                meta_type: c_uint32
                for meta_offset in range(cols):
                    meta_col_type = stream.read_i8()
                    meta_index = stream.read_bool()
                    meta_type = stream.read_vu32()
                    if meta_col_type in [PrimitiveType.OBJECT, PrimitiveType.ENUM]:
                        meta_type = stream.read_vu32()
                    else:
                        meta_type = c_uint32(0)
                    meta[meta_offset] = std_n.core._Table.TableColumnMeta(meta_col_type, meta_type, meta_index)
                data: list[Any] = [None] * (cols * rows)
                col: int
                row: int
                enum_type: GreyCat.Type
                for col in range(cols):
                    match meta[col].col_type:
                        case PrimitiveType.NULL:
                            pass
                        case PrimitiveType.INT:
                            for row in range(rows):
                                data[col + row] = stream.read_vi64().value
                        case PrimitiveType.FLOAT:
                            for row in range(rows):
                                data[col + row] = stream.read_f64().value
                        case PrimitiveType.TIME:
                            for row in range(rows):
                                data[col + row] = std_n.core._time.load(type.greycat.types[type.greycat.type_offset_core_time], stream)
                        case PrimitiveType.DURATION:
                            for row in range(rows):
                                data[col + row] = std_n.core._duration.load(type.greycat.types[type.greycat.type_offset_core_duration], stream)
                        case PrimitiveType.ENUM:
                            for row in range(rows):
                                enum_type = type.greycat.types[meta[col].type]
                                data[col + row] = enum_type.loader(enum_type, stream)
                        case _:
                            for row in range(rows):
                                data[col + row] = stream.read()
                t: std_n.core._Table = type.factory(type)
                t.cols = cols
                t.rows = rows
                t.meta = meta
                t.data = data
                return t
            
            class TableColumnMeta:
                def __init__(self, col_type: c_byte, type: c_uint32, index: bool) -> None:
                    self.col_type: Final[c_byte] = col_type
                    self.type: Final[c_uint32] = type
                    self.meta_index: Final[bool] * index

        class _Tensor(GreyCat.Object):
            def __init__(self, type: GreyCat.Type)->None:
                self.shape: list[c_uint32]
                self.tensor_type: c_byte
                self.size: c_uint32
                self.data: bytes
                super(type, None)

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
                        raise ValueError(f'{tensor_type}')
                res: std_n.core._Tensor = type.factory(type)
                res.shape = shape
                res.tensor_type = tensor_type
                res.size = size
                res.data = stream.read_i8_array(bin_size)
                return res

        class _nodeIndexBucket(GreyCat.Object):
            def __init__(type: GreyCat.Type) -> None:
                super(type, None)

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
                res: std_n.core._nodeIndexBucket = type.factory(type)
                res.attributes = data
                return res
        
        __B_2D: list[int] = [0x5555555555555555, 0x3333333333333333, 0x0F0F0F0F0F0F0F0F, 0x00FF00FF00FF00FF, 0x0000FFFF0000FFFF, 0x00000000FFFFFFFF]
        __S_2D: list[int] = [0, 1, 2, 4, 8, 16]

        @staticmethod
        def __interleave64_2d(x: int, y: int) -> c_int64:
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
        def __deinterleave64_2d(interleaved: c_int64)->int:
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

        __B_3D: list[int] = [0x1249249249249249, 0x10C30C30C30C30C3, 0x100F00F00F00F00F, 0x001F0000FF0000FF, 0xFFFF00000000FFFF, 0x00000000001FFFFF]
        __S_3D: list[int] = [2, 4, 8, 16, 32]
        
        @staticmethod
        def __interleave64_3d(x: int, y: int, z: int) -> c_int64:
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
        def __deinterleave64_3d(interleaved: c_int64) -> int:
            x: int = interleaved & std_n.core.__B_3D[0]
            x = (x ^ (x >> std_n.core.__S_3D[0])) & std_n.core.__B_3D[1]
            x = (x ^ (x >> std_n.core.__S_3D[1])) & std_n.core.__B_3D[2]
            x = (x ^ (x >> std_n.core.__S_3D[2])) & std_n.core.__B_3D[3]
            x = (x ^ (x >> std_n.core.__S_3D[3])) & std_n.core.__B_3D[4]
            x = (x ^ (x >> std_n.core.__S_3D[4])) & std_n.core.__B_3D[5]
            return x

        __B_5D: list[int] = [0x0084210842108421, 0x000C0300C0300C03, 0x00000F0000F0000F, 0x0000FF00000000FF, 0x0000000000000FFF]
        __S_5D: list[int] = [4, 8, 16, 32]
        
        @staticmethod
        def __interleave64_5d(x0: int, x1: int, x2: int, x3: int, x4: int) -> c_int64:
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
        def __deinterleave64_5d(interleaved: c_int64) -> int:
            x: int = interleaved.value & std_n.core.__B_5D[0]
            x = (x ^ (x >> std_n.core.__S_5D[0])) & std_n.core.__B_5D[1]
            x = (x ^ (x >> std_n.core.__S_5D[1])) & std_n.core.__B_5D[2]
            x = (x ^ (x >> std_n.core.__S_5D[2])) & std_n.core.__B_5D[3]
            x = (x ^ (x >> std_n.core.__S_5D[3])) & std_n.core.__B_5D[4]
            return  x;

# class std_n:
#     class core:
#         class nodeTimeCursor(GreyCat.Object):
#             def __init__(self: std_n.core.nodeTimeCursor, type: GreyCat.Type) -> None:
#                 super(type, None)
#                 raise NotImplementedError

#             @staticmethod
#             def load(type: GreyCat.Type, stream: GreyCat._Stream) -> object:
#                 raise NotImplementedError

#         class Array(Generic[T], GreyCat.Object):
#             def __init__(self: std_n.core.Array[T], type: GreyCat.Type) -> None:
#                 super(type, None)

#             @staticmethod
#             def load(type: GreyCat.Type, stream: GreyCat._Stream) -> object:
#                 size = stream.read_i32().value
#                 array: std_n.core.Array[object] = type.factory(type)
#                 array = [None] * size
#                 for offset in range(size):
#                     array.set(offset, stream.read())
#                 return array

#         class Date(GreyCat.Object):

#             def __init__(self: std_n.core.Date, type: GreyCat.Type) -> None:
#                 super(type, None)
#                 self.localizedEpochS: c_int64
#                 self.epochUs: c_int64
#                 self.timeZone: c_int32

#             def _save(self: std_n.core.Date, stream: GreyCat._Stream) -> None:
#                 stream.write_i8(PrimitiveType.OBJECT)
#                 stream.write_i32(self.type.offset)
#                 stream.write_i64(self.localizedEpochS)
#                 stream.write_i64(self.epochUs)
#                 stream.write_i32(self.timeZone)

#             @staticmethod
#             def load(type: GreyCat.Type, stream: GreyCat._Stream) -> object:
#                 res: std_n.core.Date = type.factory(type)
#                 res.localizedEpochS = stream.read_i64()
#                 res.epochUs = stream.read_i64()
#                 res.timeZone = stream.read_i32()
#                 return res

#         class duration(GreyCat.Object):
#             def __init__(self: std_n.core.duration, type: GreyCat.Type) -> None:
#                 super(type, None)
#                 self.value: c_int64

#             def _save(self: std_n.core.duration, stream: GreyCat._Stream) -> None:
#                 stream.write_i8(PrimitiveType.DURATION)
#                 stream.write_i64(self.value)

#             @staticmethod
#             def load(type: GreyCat.Type, stream: GreyCat._Stream) -> object:
#                 res: std_n.core.duration = type.factory(type)
#                 res.value = stream.read_i64()
#                 return res

#         class Error(GreyCat.Object):
#             def __init__(self: std_n.core.Error, type: GreyCat.Type):
#                 super(type, None)
#                 self.code: c_int32
#                 self.frames: list[std_n.core.Error.Frame]
#                 self.msg: str
#                 self.value: object

#             def _save(self: std_n.core.Error, stream: GreyCat._Stream) -> None:
#                 stream.write_i8(PrimitiveType.OBJECT)
#                 stream.write_i32(self.type.offset)
#                 stream.write_i32(self.code)
#                 stream.write_i32(c_int32(len(self.frames)))
#                 msg_bytes = self.msg.encode('utf-8')
#                 stream.write_i32(c_int32(len(msg_bytes)))
#                 for offset in range(len(self.frames)):
#                     frame: std_n.core.Error.Frame = self.frames[offset]
#                     stream.write_i32(frame.modSymbol)
#                     stream.write_i32(frame.typeSymbol)
#                     stream.write_i32(frame.fnSymbol)
#                     stream.write_i32(frame.line)
#                     stream.write_i32(frame.column)
#                 stream.write_i8_array(msg_bytes, 0, len(msg_bytes))
#                 stream.write_object(self.value)

#             @staticmethod
#             def load(type: GreyCat.Type, stream: GreyCat._Stream) -> object:
#                 code: c_int32 = stream.read_i32()
#                 framesLen: c_int32 = stream.read_i32()
#                 msgLen: c_int32 = stream.read_i32()
#                 frames: list[std_n.core.Error.Frame] = [None] * framesLen
#                 for offset in range(framesLen):
#                     modSymbol: c_int32 = stream.read_i32()
#                     typeSymbol: c_int32 = stream.read_i32()
#                     fnSymbol: c_int32 = stream.read_i32()
#                     line: c_int32 = stream.read_i32()
#                     column: c_int32 = stream.read_i32()
#                     frames[offset] = std_n.core.Error.Frame(
#                         modSymbol, typeSymbol, fnSymbol, line, column)
#                 res: std_n.core.Error = type.factory(type)
#                 res.code = code
#                 res.frames = frames
#                 res.msg = stream.read_string(msgLen)
#                 res.value = stream.read()
#                 return res

#             class Frame:
#                 def __init__(self: std_n.core.Error.Frame, modSymbol: c_int32, typeSymbol: c_int32, fnSymbol: c_int32, line: c_int32, column: c_int32) -> None:
#                     self.modSymbol = modSymbol
#                     self.typeSymbol = typeSymbol
#                     self.fnSymbol = fnSymbol
#                     self.line = line
#                     self.column = column

#         class geo(GreyCat.Object):
#             GC_CORE_GEO_LAT_EPS: float = 0.00000001
#             GC_CORE_GEO_LAT_MIN: float = -85.05112878
#             GC_CORE_GEO_LAT_MAX: float = 85.05112878
#             GC_CORE_GEO_LNG_MIN: float = -180
#             GC_CORE_GEO_LNG_MAX: float = 180

#             @staticmethod
#             def load(type: GreyCat.Type, stream: GreyCat._Stream) -> object:
#                 geo: std_n.core.geo = type.factory(type)
#                 geocode: c_int64 = stream.read_i64()
#                 geo.geocode = geocode
#                 decoded: Tuple[int, int] = std_n.core.geo.deinterleave64(
#                     geocode.value)
#                 geo.lat = std_n.core.geo.GC_CORE_GEO_LAT_MIN + ((decoded[0] + 0.5) / 4294967296.0) * (
#                     std_n.core.geo.GC_CORE_GEO_LAT_MAX + std_n.core.geo.GC_CORE_GEO_LAT_MIN)
#                 geo.lng = std_n.core.geo.GC_CORE_GEO_LNG_MIN + ((decoded[1] + 0.5) / 4294967296.0) * (
#                     std_n.core.geo.GC_CORE_GEO_LNG_MAX + std_n.core.geo.GC_CORE_GEO_LNG_MIN)
#                 return geo

#             @staticmethod
#             def interleave64(xlo: int, ylo: int) -> int:
#                 B: list[int] = [6148914691236517205, 3689348814741910323,
#                                 1085102592571150095, 71777214294589695, 281470681808895]
#                 S: list[int] = [1, 2, 4, 8, 16]
#                 x: int = xlo
#                 y: int = ylo
#                 x = (x | (x << S[4])) & B[4]
#                 y = (y | (y << S[4])) & B[4]
#                 x = (x | (x << S[3])) & B[3]
#                 y = (y | (y << S[3])) & B[3]
#                 x = (x | (x << S[2])) & B[2]
#                 y = (y | (y << S[2])) & B[2]
#                 x = (x | (x << S[1])) & B[1]
#                 y = (y | (y << S[1])) & B[1]
#                 x = (x | (x << S[0])) & B[0]
#                 y = (y | (y << S[0])) & B[0]
#                 return x | (y << 1)

#             @staticmethod
#             def deinterleave64(interleaved: int) -> Tuple[int, int]:
#                 B: list[int] = [6148914691236517205, 3689348814741910323,
#                                 1085102592571150095, 71777214294589695, 281470681808895, 4294967295]
#                 S: list[int] = [0, 1, 2, 4, 8, 16]
#                 x: int = interleaved
#                 y: int = interleaved >> 1
#                 x = (x | (x >> S[0])) & B[0]
#                 y = (y | (y >> S[0])) & B[0]
#                 x = (x | (x >> S[1])) & B[1]
#                 y = (y | (y >> S[1])) & B[1]
#                 x = (x | (x >> S[2])) & B[2]
#                 y = (y | (y >> S[2])) & B[2]
#                 x = (x | (x >> S[3])) & B[3]
#                 y = (y | (y >> S[3])) & B[3]
#                 x = (x | (x >> S[4])) & B[4]
#                 y = (y | (y >> S[4])) & B[4]
#                 x = (x | (x >> S[5])) & B[5]
#                 y = (y | (y >> S[5])) & B[5]
#                 return x, y

#             def __init__(self: std_n.core.geo, type: GreyCat.Type) -> None:
#                 super(type, None)
#                 self.geocode: c_int64
#                 self.lat: float
#                 self.lng: float

#             def _save(self: std_n.core.geo, stream: GreyCat._Stream) -> None:
#                 stream.write_i8(PrimitiveType.GEO)
#                 stream.write_i64(self.geocode)

#         class GeoPoly(GreyCat.Object):
#             type_name: str = 'core.GeoPoly'

#             def __init__(self: std_n.core.GeoPoly, type: GreyCat.Type) -> None:
#                 super(type, None)

#             def _save(self: std_n.core.GeoPoly, stream: GreyCat._Stream) -> None:
#                 stream.write_i8(PrimitiveType.OBJECT)
#                 stream.write_i32(self.type.offset)
#                 if self.attributes is None:
#                     stream.write_i32(c_int32(0))
#                 else:
#                     stream.write_i32(c_int32(len(self.attributes)))
#                     for offset in range(len(self.attributes)):
#                         point: std_n.core.geo = self.attributes[offset]
#                         stream.write_i64(point.geocode)

#             @staticmethod
#             def load(type: GreyCat.Type, stream: GreyCat._Stream) -> object:
#                 size: int = stream.read_i32().value
#                 geoType: GreyCat.Type = type.greycat.types[type.greycat.type_offset_core_geo]
#                 points: list[std_n.core.geo] = [None] * size
#                 for offset in range(size):
#                     points[offset] = std_n.core.geo(geoType)
#                     points[offset].geocode = stream.read_i64()
#                     # TODO: update
#                 gp: std_n.core.GeoPoly = type.factory(type)
#                 gp.attributes = points
#                 return gp

#         class Map(Generic[T, U], GreyCat.Object):
#             type_name: str = 'core.Map'

#             def __init__(self: std_n.core.Map[T, U], type: GreyCat.Type) -> None:
#                 super(type, None)
#                 self.__map: dict[T, U] = dict()

#             def _save(self: std_n.core.Map[T, U], stream: GreyCat._Stream) -> None:
#                 stream.write_i8(PrimitiveType.OBJECT)
#                 stream.write_i32(self.type.offset)
#                 stream.write_i32(self.size())
#                 for key in self.__map:
#                     stream.write_object(key)
#                     stream.write_object(self.__map[key])

#             @staticmethod
#             def load(type: GreyCat.Type, stream: GreyCat._Stream) -> object:
#                 map: std_n.core.Map = type.factory(type)
#                 mapLength = stream.read_i32().value
#                 for _ in range(mapLength):
#                     map[stream.read()] = stream.read()
#                 return map

#             def size(self: std_n.core.Map[T, U]) -> int:
#                 return len(self.__map)

#             def get(self: std_n.core.Map[T, U], o: object) -> U:
#                 return self.__map[o]

#             def set(self: std_n.core.Map[T, U], t: T, u: U) -> None:
#                 self.__map[t] = u

#             def remove(self: std_n.core.Map[T, U], o: object) -> None:
#                 self.__map.pop(o, None)

#             def clear(self: std_n.core.Map[T, U]) -> None:
#                 self.__map.clear()

#         class node(GreyCat.Object):
#             def __init__(self: std_n.core.node, type: GreyCat.Type) -> None:
#                 super(type, None)
#                 self.ref: c_int64

#             def _save(self: std_n.core.node, stream: GreyCat._Stream) -> None:
#                 stream.write_i8(PrimitiveType.NODE)
#                 stream.write_i64(self.ref)

#             @staticmethod
#             def load(type: GreyCat.Type, stream: GreyCat._Stream) -> object:
#                 res: std_n.core.node = type.factory(type)
#                 res.ref = stream.read_i64()
#                 return res

#         class nodeGeo(GreyCat.Object):
#             def __init__(self: std_n.core.nodeGeo, type: GreyCat.Type) -> None:
#                 super(type, None)
#                 self.ref: c_int64

#             def _save(self: std_n.core.nodeGeo, stream: GreyCat._Stream) -> None:
#                 stream.write_i8(PrimitiveType.NODE_GEO)
#                 stream.write_i64(self.ref)

#             @staticmethod
#             def load(type: GreyCat.Type, stream: GreyCat._Stream) -> object:
#                 res: std_n.core.nodeGeo = type.factory(type)
#                 res.ref = stream.read_i64()
#                 return res

#         class nodeIndex(GreyCat.Object):
#             type_name: str = "core.nodeIndex"

#             def __init__(self: std_n.core.nodeIndex, type: GreyCat.Type) -> None:
#                 super(type, None)
#                 self.ref: c_int64

#             def _save(self: std_n.core.nodeIndex, stream: GreyCat._Stream) -> None:
#                 stream.write_i8(PrimitiveType.NODE_INDEX)
#                 stream.write_i64(self.ref)

#             @staticmethod
#             def load(type: GreyCat.Type, stream: GreyCat._Stream) -> object:
#                 res: std_n.core.nodeIndex = type.factory(type)
#                 res.ref = stream.read_i64()
#                 return res

#         class nodeIndexBucket(GreyCat.Object):
#             def __init__(self: std_n.core.nodeIndexBucket, type: GreyCat.Type) -> None:
#                 super(type, None)

#             def _save(self: std_n.core.nodeIndexBucket, stream: GreyCat._Stream) -> None:
#                 stream.write_i8(PrimitiveType.OBJECT)
#                 stream.write_i32(self.type.offset)
#                 if self.attributes is None:
#                     stream.write_i32(c_int32(0))
#                 else:
#                     stream.write_i32(c_int32(len(self.attributes)))
#                     for offset in range(len(self.attributes)):
#                         stream.write_object(self.attributes[offset])

#             @staticmethod
#             def load(type: GreyCat.Type, stream: GreyCat._Stream) -> object:
#                 size = stream.read_i32()
#                 data: list[object] = [None] * size
#                 for offset in range(size):
#                     data[offset] = stream.read()
#                 res: std_n.core.nodeIndexBucket = type.factory(type)
#                 res.attributes = data
#                 return res

#         class nodeList(GreyCat.Object):
#             def __init__(self: std_n.core.nodeList, type: GreyCat.Type) -> None:
#                 super(type, None)
#                 self.ref: c_int64

#             def _save(self: std_n.core.nodeList, stream: GreyCat._Stream) -> None:
#                 stream.write_i8(PrimitiveType.NODE_LIST)
#                 stream.write_i64(self.ref)

#             @staticmethod
#             def load(type: GreyCat.Type, stream: GreyCat._Stream) -> object:
#                 res: std_n.core.nodeList = type.factory(type)
#                 res.ref = stream.read_i64()
#                 return res

#         class nodeTime(GreyCat.Object):
#             def __init__(self: std_n.core.nodeTime, type: GreyCat.Type) -> None:
#                 super(type, None)
#                 self.ref: c_int64

#             def _save(self: std_n.core.nodeTime, stream: GreyCat._Stream) -> None:
#                 stream.write_i8(PrimitiveType.NODE_TIME)
#                 stream.write_i64(self.ref)

#             @staticmethod
#             def load(type: GreyCat.Type, stream: GreyCat._Stream) -> object:
#                 res: std_n.core.nodeTime = type.factory(type)
#                 res.ref = stream.read_i64()
#                 return res

#         class Table(Generic[T], GreyCat.Object):
#             def __init__(self: std_n.core.Table[T], type: GreyCat.Type) -> None:
#                 super(type, None)
#                 self.cols: c_int32
#                 self.rows: c_int32
#                 self.meta: list[std_n.core.Table.TableColumnMeta]
#                 self.data: list[T]

#             def _save(self: std_n.core.Table[T], stream: GreyCat._Stream) -> None:
#                 stream.write_i8(PrimitiveType.OBJECT)
#                 stream.write_i32(self.type.offset)
#                 stream.write_i32(self.cols)
#                 stream.write_i32(self.rows)
#                 stream.write_bool(self.meta is not None)
#                 if self.meta is not None:
#                     for offset in len(self.meta):
#                         colMeta: std_n.core.Table.TableColumnMeta = self.meta[offset]
#                         stream.write_i32(colMeta.colType)
#                         stream.write_i32(colMeta.type)
#                         stream.write_i32(colMeta.size)
#                         stream.write_f64(colMeta.sum)
#                         stream.write_f64(colMeta.sumSq)
#                         stream.write_i64(colMeta.min)
#                         stream.write_i64(colMeta.max)
#                         stream.write_bool(colMeta.index)
#                         stream.write_i32(colMeta.tz)
#                 for offset in len(self.data):
#                     stream.write_object(self.data[offset])

#             @staticmethod
#             def load(type: GreyCat.Type, stream: GreyCat._Stream) -> object:
#                 cols: c_int32 = stream.read_i32()
#                 rows: c_int32 = stream.read_i32()
#                 useMeta: bool = stream.read_bool()
#                 meta: list[std_n.core.Table.TableColumnMeta] = None
#                 if useMeta:
#                     meta = [None] * cols.value
#                     for col in range(cols.value):
#                         meta[col] = std_n.core.Table.TableColumnMeta(stream.read_i32(), stream.read_i32(), stream.read_i32(
#                         ), stream.read_f64(), stream.read_f64(), stream.read_i64(), stream.read_i64(), stream.read_bool(), stream.read_i32())
#                 capacity = cols.value = rows.value
#                 data: list[object] = [None] * capacity
#                 for offset in range(capacity):
#                     data[offset] = stream.read()
#                 t: std_n.core.Table[object] = type.factory(type)
#                 t.cols = cols
#                 t.rows = rows
#                 t.meta = meta
#                 t.data = data
#                 return t

#             class TableColumnMeta:
#                 def __init__(self: std_n.core.Table.TableColumnMeta, colType: c_int32, type: c_int32, size: c_int32, sum: c_double, sumSq: c_double, min: c_int64, max: c_int64, index: bool, tz: c_int32) -> None:
#                     self.colType: c_int32 = colType
#                     self.type: c_int32 = type
#                     self.size: c_int32 = size
#                     self.sum: c_double = sum
#                     self.sumSq: c_double = sumSq
#                     self.min: c_int64 = min
#                     self.max: c_int64 = max
#                     self.index: bool = index
#                     self.tz: c_int32 = tz

#         class Tensor(GreyCat.Object):
#             def __init__(self: std_n.core.Tensor, type: GreyCat.Type) -> None:
#                 super(type, None)
#                 self.shape: list[c_int32]
#                 self.tensorType: c_byte
#                 self.size: c_int32
#                 self.data: bytes

#             def _save(self: std_n.core.Tensor, stream: GreyCat._Stream) -> None:
#                 stream.write_i8(PrimitiveType.OBJECT)
#                 stream.write_i32(self.type.offset)
#                 stream.write_i8(c_byte(len(self.shape)))
#                 stream.write_i8(self.tensorType)
#                 for offset in range(len(self.shape)):
#                     stream.write_i32(self.shape[offset])
#                 stream.write_i32(self.size)
#                 stream.write_i8_array(self.data, 0, len(self.data))

#             @staticmethod
#             def load(type: GreyCat.Type, stream: GreyCat._Stream) -> object:
#                 nbDim: int = stream.read_i8().value
#                 tensorType: c_byte = stream.read_i8()
#                 shape: list[c_int32] = [None] * nbDim
#                 for offset in range(nbDim):
#                     shape[offset] = stream.read_i32()
#                 size: c_int32 = stream.read_i32()
#                 bin_size: int = size.value
#                 match tensorType.value:
#                     case 0 | 2:
#                         bin_size = c_int32(size.value * 4)
#                     case 1 | 3 | 4:
#                         bin_size = c_int32(size.value * 8)
#                     case 5:
#                         bin_size = c_int32(size.value * 16)
#                     case _:
#                         raise ValueError(tensorType)
#                 res: std_n.core.Tensor = type.factory(type)
#                 res.shape = shape
#                 res.tensorType = tensorType
#                 res.size = size
#                 res.data = stream.read_i8_array(bin_size)
#                 return res

#         class time(GreyCat.Object):
#             def __init__(self: std_n.core.time, type: GreyCat.Type) -> None:
#                 super(type, None)
#                 self.value: c_int64

#             def _save(self: std_n.core.time, stream: GreyCat._Stream) -> None:
#                 stream.write_i8(PrimitiveType.TIME)
#                 stream.write_i64(self.value)

#             @staticmethod
#             def load(type: GreyCat.Type, stream: GreyCat._Stream) -> object:
#                 res: std_n.core.time = type.factory(type)
#                 res.value = stream.read_i64()
#                 return res

#         class String(GreyCat.Object):
#             def __init__(self: std_n.core.String, type: GreyCat.Type) -> None:
#                 super(type, None)

#             @staticmethod
#             def load(type: GreyCat.Type, stream: GreyCat._Stream) -> object:
#                 return stream.read_string(stream.read_i32().value)

#     class util:
#         class Quantizer(GreyCat.Object):
#             def __init__(self: std_n.util.Quantizer, type: GreyCat.Type) -> None:
#                 super(type, None)
#                 raise NotImplementedError

#             @staticmethod
#             def load(type: GreyCat.Type, stream: GreyCat._Stream) -> object:
#                 raise NotImplementedError

#         class Buffer(GreyCat.Object):
#             def __init__(self: std_n.util.Buffer, type: GreyCat.Type) -> None:
#                 super(type, None)
#                 self.data = bytes

#             def _save(self: std_n.util.Buffer, stream: GreyCat._Stream) -> None:
#                 stream.write_i8(PrimitiveType.OBJECT)
#                 stream.write_i32(self.type.offset)
#                 stream.write_i32(len(self.data))
#                 stream.write_i8_array(self.data, 0, len(self.data))

#             @staticmethod
#             def load(type: GreyCat.Type, stream: GreyCat._Stream) -> object:
#                 buf: std_n.util.Buffer = type.factory(type)
#                 buf.data = stream.read_i8_array(stream.read_i32().value)
#                 return buf

#         class Gaussian(GreyCat.Object):
#             def __init__(self: std_n.util.Gaussian, type: GreyCat.Type) -> None:
#                 super(type, None)
#                 self.sum: c_double
#                 self.sumSq: c_double
#                 self.size: c_int64
#                 self.nbAccepted: c_int64
#                 self.nbRejected: c_int64
#                 self.nbNull: c_int64
#                 self.min: c_double
#                 self.max: c_double
#                 self.minBound: c_double
#                 self.maxBound: c_double

#             def _save(self: std_n.util.Gaussian, stream: GreyCat._Stream) -> None:
#                 stream.write_i8(PrimitiveType.OBJECT)
#                 stream.write_i32(self.type.offset)
#                 stream.write_f64(self.sum)
#                 stream.write_f64(self.sumSq)
#                 stream.write_i64(self.size)
#                 stream.write_i64(self.nbAccepted)
#                 stream.write_i64(self.nbRejected)
#                 stream.write_i64(self.nbNull)
#                 stream.write_f64(self.min)
#                 stream.write_f64(self.max)
#                 stream.write_f64(self.minBound)
#                 stream.write_f64(self.maxBound)

#             @staticmethod
#             def load(type: GreyCat.Type, stream: GreyCat._Stream) -> object:
#                 g: std_n.util.Gaussian = type.factory(type)
#                 g.sum = stream.read_f64()
#                 g.sumSq = stream.read_f64()
#                 g.size = stream.read_i64()
#                 g.nbAccepted = stream.read_i64()
#                 g.nbRejected = stream.read_i64()
#                 g.nbNull = stream.read_i64()
#                 g.min = stream.read_f64()
#                 g.max = stream.read_f64()
#                 g.minBound = stream.read_f64()
#                 g.maxBound = stream.read_f64()
#                 return g

#         class GaussianProfile(GreyCat.Object):
#             def __init__(self: std_n.util.GaussianProfile, type: GreyCat.Type) -> None:
#                 super(type, None)
#                 self.data: bytes

#             def _save(self: std_n.util.GaussianProfile, stream: GreyCat._Stream) -> None:
#                 stream.write_i8(PrimitiveType.OBJECT)
#                 stream.write_i32(self.type.offset)
#                 stream.write_i32(c_int32(len(self.data)))
#                 stream.write_i8_array(self.data)

#             @staticmethod
#             def load(type: GreyCat.Type, stream: GreyCat._Stream) -> object:
#                 g: std_n.util.GaussianProfile = type.factory(type)
#                 g.data = stream.read_i8_array(stream.read_i32().value)
#                 return g

#         class HistogramF64(GreyCat.Object):
#             def __init__(self: std_n.util.HistogramF64, type: GreyCat.Type) -> None:
#                 super(type, None)
#                 self.realMin: c_double
#                 self.realMax: c_double
#                 self.min: c_double
#                 self.max: c_double
#                 self.size: c_int64
#                 self.nullCount: c_int64
#                 self.maxRange: c_int64
#                 self.sum: c_double
#                 self.sumSq: c_double
#                 self.unitMagnitude: c_int32
#                 self.significantFigures: c_int32
#                 self.subBucketHalfCountMagnitude: c_int32
#                 self.subBucketHalfCount: c_int32
#                 self.subBucketMask: c_int64
#                 self.subBucketCount: c_int32
#                 self.bucketCount: c_int32
#                 self.minValue: c_int64
#                 self.maxValue: c_int64
#                 self.normalizingIndexOffset: c_int32
#                 self.countsLen: c_int32
#                 self.totalCount: c_int64
#                 self.counts: list[c_int64]

#             def _save(self: std_n.util.HistogramF64, stream: GreyCat._Stream) -> None:
#                 stream.write_i8(PrimitiveType.OBJECT)
#                 stream.write_i32(self.type.offset)
#                 stream.write_f64(self.realMin)
#                 stream.write_f64(self.realMax)
#                 stream.write_f64(self.min)
#                 stream.write_f64(self.max)
#                 stream.write_i64(self.size)
#                 stream.write_i64(self.nullCount)
#                 stream.write_i64(self.maxRange)
#                 stream.write_f64(self.sum)
#                 stream.write_f64(self.sumSq)
#                 stream.write_i32(self.unitMagnitude)
#                 stream.write_i32(self.significantFigures)
#                 stream.write_i32(self.subBucketHalfCountMagnitude)
#                 stream.write_i32(self.subBucketHalfCount)
#                 stream.write_i64(self.subBucketMask)
#                 stream.write_i32(self.subBucketCount)
#                 stream.write_i32(self.bucketCount)
#                 stream.write_i64(self.minValue)
#                 stream.write_i64(self.maxValue)
#                 stream.write_i32(self.normalizingIndexOffset)
#                 stream.write_i32(self.countsLen)
#                 stream.write_i64(self.totalCount)
#                 for offset in len(self.counts):
#                     stream.write_i64(self.counts[offset])

#             @staticmethod
#             def load(type: GreyCat.Type, stream: GreyCat._Stream) -> object:
#                 realMin = stream.read_f64()
#                 realMax = stream.read_f64()
#                 min = stream.read_f64()
#                 max = stream.read_f64
#                 size = stream.read_i64()
#                 nullCount = stream.read_i64()
#                 maxRange = stream.read_i64()
#                 sum = stream.read_f64()
#                 sumSq = stream.read_f64()
#                 unitMagnitude = stream.read_i32()
#                 significantFigures = stream.read_i32()
#                 subBucketHalfCountMagnitude = stream.read_i32()
#                 subBucketHalfCount = stream.read_i32()
#                 subBucketMask = stream.read_i64()
#                 subBucketCount = stream.read_i32()
#                 bucketCount = stream.read_i32()
#                 minValue = stream.read_i64()
#                 maxValue = stream.read_i64()
#                 normalizingIndexOffset = stream.read_i32()
#                 countsLen = stream.read_i32()
#                 totalCount = stream.read_i64()
#                 counts = [None] * countsLen.value
#                 for offset in range(countsLen.value):
#                     counts[offset] = stream.read_i64()
#                 h: std_n.util.HistogramF64 = type.factory(type)
#                 h.realMin = realMin
#                 h.realMax = realMax
#                 h.min = min
#                 h.max = max
#                 h.size = size
#                 h.nullCount = nullCount
#                 h.maxRange = maxRange
#                 h.sum = sum
#                 h.sumSq = sumSq
#                 h.unitMagnitude = unitMagnitude
#                 h.significantFigures = significantFigures
#                 h.subBucketHalfCountMagnitude = subBucketHalfCountMagnitude
#                 h.subBucketCount = subBucketHalfCount
#                 h.subBucketMask = subBucketMask
#                 h.subBucketCount = subBucketCount
#                 h.bucketCount = bucketCount
#                 h.minValue = minValue
#                 h.maxValue = maxValue
#                 h.normalizingIndexOffset = normalizingIndexOffset
#                 h.countsLen = countsLen
#                 h.totalCount = totalCount
#                 h.counts = counts
#                 return h

#         class HistogramF64(GreyCat.Object):
#             def __init__(self: std_n.util.HistogramF64, type: GreyCat.Type) -> None:
#                 super(type, None)
#                 self.realMin: c_int64
#                 self.realMax: c_int64
#                 self.min: c_int64
#                 self.max: c_int64
#                 self.size: c_int64
#                 self.nullCount: c_int64
#                 self.maxRange: c_int64
#                 self.sum: c_double
#                 self.sumSq: c_double
#                 self.unitMagnitude: c_int32
#                 self.significantFigures: c_int32
#                 self.subBucketHalfCountMagnitude: c_int32
#                 self.subBucketHalfCount: c_int32
#                 self.subBucketMask: c_int64
#                 self.subBucketCount: c_int32
#                 self.bucketCount: c_int32
#                 self.minValue: c_int64
#                 self.maxValue: c_int64
#                 self.normalizingIndexOffset: c_int32
#                 self.countsLen: c_int32
#                 self.totalCount: c_int64
#                 self.counts: list[c_int64]

#             def _save(self: std_n.util.HistogramF64, stream: GreyCat._Stream) -> None:
#                 stream.write_i8(PrimitiveType.OBJECT)
#                 stream.write_i32(self.type.offset)
#                 stream.write_i64(self.realMin)
#                 stream.write_i64(self.realMax)
#                 stream.write_i64(self.min)
#                 stream.write_i64(self.max)
#                 stream.write_i64(self.size)
#                 stream.write_i64(self.nullCount)
#                 stream.write_i64(self.maxRange)
#                 stream.write_f64(self.sum)
#                 stream.write_f64(self.sumSq)
#                 stream.write_i32(self.unitMagnitude)
#                 stream.write_i32(self.significantFigures)
#                 stream.write_i32(self.subBucketHalfCountMagnitude)
#                 stream.write_i32(self.subBucketHalfCount)
#                 stream.write_i64(self.subBucketMask)
#                 stream.write_i32(self.subBucketCount)
#                 stream.write_i32(self.bucketCount)
#                 stream.write_i64(self.minValue)
#                 stream.write_i64(self.maxValue)
#                 stream.write_i32(self.normalizingIndexOffset)
#                 stream.write_i32(self.countsLen)
#                 stream.write_i64(self.totalCount)
#                 for offset in len(self.counts):
#                     stream.write_i64(self.counts[offset])

#             @staticmethod
#             def load(type: GreyCat.Type, stream: GreyCat._Stream) -> object:
#                 realMin = stream.read_i64()
#                 realMax = stream.read_i64()
#                 min = stream.read_i64()
#                 max = stream.read_i64
#                 size = stream.read_i64()
#                 nullCount = stream.read_i64()
#                 maxRange = stream.read_i64()
#                 sum = stream.read_f64()
#                 sumSq = stream.read_f64()
#                 unitMagnitude = stream.read_i32()
#                 significantFigures = stream.read_i32()
#                 subBucketHalfCountMagnitude = stream.read_i32()
#                 subBucketHalfCount = stream.read_i32()
#                 subBucketMask = stream.read_i64()
#                 subBucketCount = stream.read_i32()
#                 bucketCount = stream.read_i32()
#                 minValue = stream.read_i64()
#                 maxValue = stream.read_i64()
#                 normalizingIndexOffset = stream.read_i32()
#                 countsLen = stream.read_i32()
#                 totalCount = stream.read_i64()
#                 counts = [None] * countsLen.value
#                 for offset in range(countsLen.value):
#                     counts[offset] = stream.read_i64()
#                 h: std_n.util.HistogramF64 = type.factory(type)
#                 h.realMin = realMin
#                 h.realMax = realMax
#                 h.min = min
#                 h.max = max
#                 h.size = size
#                 h.nullCount = nullCount
#                 h.maxRange = maxRange
#                 h.sum = sum
#                 h.sumSq = sumSq
#                 h.unitMagnitude = unitMagnitude
#                 h.significantFigures = significantFigures
#                 h.subBucketHalfCountMagnitude = subBucketHalfCountMagnitude
#                 h.subBucketCount = subBucketHalfCount
#                 h.subBucketMask = subBucketMask
#                 h.subBucketCount = subBucketCount
#                 h.bucketCount = bucketCount
#                 h.minValue = minValue
#                 h.maxValue = maxValue
#                 h.normalizingIndexOffset = normalizingIndexOffset
#                 h.countsLen = countsLen
#                 h.totalCount = totalCount
#                 h.counts = counts
#                 return h

#         class ProgressTracker(GreyCat.Object):
#             def __init__(self: std_n.util.ProgressTracker, type: GreyCat.Type) -> None:
#                 super(type, None)
#                 self.initialTime: c_int64
#                 self.lastTime: c_int64
#                 self.previousTime: c_int64
#                 self.previousSteps: c_int64
#                 self.maxStep: c_int64
#                 self.nbStep: c_int64
#                 self.duration: c_int64
#                 self.lapDuration: c_int64
#                 self.totalSpeed: c_double
#                 self.stepSpeed: c_double
#                 self.progress: c_double
#                 self.remainingTime: c_int64

#             def _save(self: std_n.util.ProgressTracker, stream: GreyCat._Stream) -> None:
#                 stream.write_i8(PrimitiveType.OBJECT)
#                 stream.write_i32(self.type.offset)
#                 stream.write_i64(self.initialTime)
#                 stream.write_i64(self.lastTime)
#                 stream.write_i64(self.previousTime)
#                 stream.write_i64(self.previousSteps)
#                 stream.write_i64(self.maxStep)
#                 stream.write_i64(self.nbStep)
#                 stream.write_i64(self.duration)
#                 stream.write_i64(self.lapDuration)
#                 stream.write_f64(self.totalSpeed)
#                 stream.write_f64(self.stepSpeed)
#                 stream.write_f64(self.progress)
#                 stream.write_i64(self.remainingTime)

#             @staticmethod
#             def load(type: GreyCat.Type, stream: GreyCat._Stream) -> object:
#                 initialTime: c_int64 = stream.read_i64()
#                 lastTime: c_int64 = stream.read_i64()
#                 previousTime: c_int64 = stream.read_i64()
#                 previousSteps: c_int64 = stream.read_i64()
#                 maxStep: c_int64 = stream.read_i64()
#                 nbStep: c_int64 = stream.read_i64()
#                 duration: c_int64 = stream.read_i64()
#                 lapDuration: c_int64 = stream.read_i64()
#                 totalSpeed: c_double = stream.read_f64()
#                 stepSpeed: c_double = stream.read_f64()
#                 progress: c_double = stream.read_f64()
#                 remainingTime: c_int64 = stream.read_i64()
#                 pt: std_n.util.ProgressTracker = type.factory(type)
#                 pt.initialTime = initialTime
#                 pt.lastTime = lastTime
#                 pt.previousTime = previousTime
#                 pt.previousSteps = previousSteps
#                 pt.maxStep = maxStep
#                 pt.nbStep = nbStep
#                 pt.duration = duration
#                 pt.lapDuration = lapDuration
#                 pt.totalSpeed = totalSpeed
#                 pt.stepSpeed = stepSpeed
#                 pt.progress = progress
#                 pt.remainingTime = remainingTime
#                 return pt

#         class Iban(GreyCat.Object):
#             def __init__(self: std_n.util.Iban, type: GreyCat.Type) -> None:
#                 super(type, None)
#                 self.infoOff: c_int32
#                 self.data: bytes

#             def _save(self: std_n.util.Iban, stream: GreyCat._Stream) -> None:
#                 stream.write_i8(PrimitiveType.OBJECT)
#                 stream.write_i32(self.type.offset)
#                 stream.write_i32(self.infoOff)
#                 stream.write_i32(c_int32(len(self.data)))
#                 stream.write_i8_array(self.data, 0, len(self.data))

#             @staticmethod
#             def load(type: GreyCat.Type, stream: GreyCat._Stream) -> object:
#                 iban: std_n.util.Iban = type.factory(type)
#                 iban.infoOff = stream.read_i32()
#                 iban.data = stream.read_i8_array(stream.read_i32())
#                 return iban

#         class Queue(Generic[T], GreyCat.Object):
#             def __init__(self: std_n.util.Queue[T], type: GreyCat.Type) -> None:
#                 super(type, None)
#                 self.__queue: list[T]

#             def _save(self: std_n.util.Queue[T], stream: GreyCat._Stream) -> None:
#                 stream.write_i8(PrimitiveType.OBJECT)
#                 stream.write_i32(self.type.offset)
#                 stream.write_i64(c_int64(self.size()))  # width
#                 stream.write_i32(c_int32(self.size()))  # size
#                 stream.write_i64(c_int32(self.size()))  # capacity
#                 stream.write_i64(c_int64(self.size()))  # TODO: head - values
#                 stream.write_i64(c_int64(0))  # TODO: tail - values
#                 for t in self.__queue:
#                     stream.write_object(t)

#             @staticmethod
#             def load(type: GreyCat.Type, stream: GreyCat._Stream) -> object:
#                 stream.read_i64()  # width
#                 size: int = stream.read_i32().value
#                 capacity: int = stream.read_i32().value
#                 queue: std_n.util.Queue[object] = type.factory(type)
#                 for _ in range(size):
#                     queue.enqueue(stream.read())
#                 for _ in range(size, capacity):
#                     stream.read()
#                 return queue

#             def size(self: std_n.util.Queue[T]) -> int:
#                 return len(self.__queue)

#             def enqueue(self: std_n.util.Queue[T], t: T) -> None:
#                 self.__queue.append(t)

#             def dequeue(self: std_n.util.Queue[T]) -> T | None:
#                 t: T = self.head()
#                 if len(self.__queue) > 0:
#                     self.__queue = self.__queue[1:]
#                 return t

#             def head(self: std_n.util.Queue[T]) -> T | None:
#                 return self.__queue[0] if len(self.__queue) > 0 else None

#         class SlidingWindow(GreyCat.Object):
#             def __init__(self: std_n.util.SlidingWindow, type: GreyCat.Type) -> None:
#                 super(type, None)
#                 self.width: c_int64
#                 self.sumType: c_byte
#                 self.sum: c_double
#                 self.sumSq: c_double
#                 self.size: c_int32
#                 self.capacity: c_int32
#                 self.toHead: c_int64
#                 self.toTail: c_int64
#                 self.values: list[object]

#             def _save(self: std_n.util.SlidingWindow, stream: GreyCat._Stream) -> None:
#                 stream.write_i8(PrimitiveType.OBJECT)
#                 stream.write_i32(self.type.offset)
#                 stream.write_i64(self.width)
#                 stream.write_i8(self.sumType)
#                 stream.write_f64(self.sum)
#                 stream.write_f64(self.sumSq)
#                 stream.write_i32(self.size)
#                 stream.write_i32(self.capacity)
#                 stream.write_i64(self.toHead)
#                 stream.write_i64(self.toTail)
#                 for offset in range(len(self.values)):
#                     stream.write_object(self.values[offset])

#             @staticmethod
#             def load(type: GreyCat.Type, stream: GreyCat._Stream) -> object:
#                 width: c_int64 = stream.read_i64()
#                 sumType: c_byte = stream.read_i8()
#                 sum: c_double = stream.read_f64()
#                 sumSq: c_double = stream.read_f64()
#                 size: c_int32 = stream.read_i32()
#                 capacity: c_int32 = stream.read_i32()
#                 toHead: c_int64 = stream.read_i64()
#                 toTail: c_int64 = stream.read_i64()
#                 values: list[object] = [None] * capacity
#                 for offset in range(capacity):
#                     values[offset] = stream.read()
#                 sw: std_n.util.SlidingWindow = type.factory(type)
#                 sw.width = width
#                 sw.sumType = sumType
#                 sw.sum = sum
#                 sw.sumSq = sumSq
#                 sw.size = size
#                 sw.capacity = capacity
#                 sw.toHead = toHead
#                 sw.toTail = toTail
#                 sw.values = values

#         class TimeWindow(GreyCat.Object):
#             def __init__(self: std_n.util.TimeWindow, type: GreyCat.Type) -> None:
#                 super(type, None)
#                 self.width: c_int64
#                 self.sumType: c_byte
#                 self.sum: c_double
#                 self.sumSq: c_double
#                 self.size: c_int32
#                 self.capacity: c_int32
#                 self.toHead: c_int64
#                 self.toTail: c_int64
#                 self.values: list[Tuple[object, c_int64]]

#             def _save(self: std_n.util.TimeWindow, stream: GreyCat._Stream) -> None:
#                 stream.write_i8(PrimitiveType.OBJECT)
#                 stream.write_i32(self.type.offset)
#                 stream.write_i64(self.width)
#                 stream.write_i8(self.sumType)
#                 stream.write_f64(self.sum)
#                 stream.write_f64(self.sumSq)
#                 stream.write_i32(self.size)
#                 stream.write_i32(self.capacity)
#                 stream.write_i64(self.toHead)
#                 stream.write_i64(self.toTail)
#                 for offset in range(len(self.values)):
#                     valueTime = self.values[offset]
#                     stream.write_object(valueTime[0])
#                     stream.write_i64(valueTime[1])

#             @staticmethod
#             def load(type: GreyCat.Type, stream: GreyCat._Stream) -> object:
#                 width: c_int64 = stream.read_i64()
#                 sumType: c_byte = stream.read_i8()
#                 sum: c_double = stream.read_f64()
#                 sumSq: c_double = stream.read_f64()
#                 size: c_int32 = stream.read_i32()
#                 capacity: c_int32 = stream.read_i32()
#                 toHead: c_int64 = stream.read_i64()
#                 toTail: c_int64 = stream.read_i64()
#                 values: list[Tuple[object, c_int64]] = [
#                     None] * capacity
#                 for offset in range(capacity):
#                     values[offset] = (stream.read(), stream.read_i64())
#                 sw: std_n.util.TimeWindow = type.factory(type)
#                 sw.width = width
#                 sw.sumType = sumType
#                 sw.sum = sum
#                 sw.sumSq = sumSq
#                 sw.size = size
#                 sw.capacity = capacity
#                 sw.toHead = toHead
#                 sw.toTail = toTail
#                 sw.values = values

#     class io:
#         class Directory(GreyCat.Object):
#             def __init__(self: std_n.io.Directory, type: GreyCat.Type) -> None:
#                 super(type, None)
#                 raise NotImplementedError

#             @staticmethod
#             def load(type: GreyCat.Type, stream: GreyCat._Stream) -> object:
#                 raise NotImplementedError

#         class File(GreyCat.Object):
#             def __init__(self: std_n.io.File, type: GreyCat.Type) -> None:
#                 super(type, None)
#                 raise NotImplementedError

#             @staticmethod
#             def load(type: GreyCat.Type, stream: GreyCat._Stream) -> object:
#                 raise NotImplementedError

#         class FileWriter(GreyCat.Object):
#             def __init__(self: std_n.io.FileWriter, type: GreyCat.Type) -> None:
#                 super(type, None)
#                 raise NotImplementedError

#             @staticmethod
#             def load(type: GreyCat.Type, stream: GreyCat._Stream) -> object:
#                 raise NotImplementedError
