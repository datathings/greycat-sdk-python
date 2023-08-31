from __future__ import annotations

from ctypes import *
import http.client
from io import *
import os
from struct import pack, unpack
from typing import *


@final
class PrimitiveType:
    NULL: c_ubyte = c_ubyte(0)
    BOOL: c_ubyte = c_ubyte(1)
    CHAR: c_ubyte = c_ubyte(2)
    INT: c_ubyte = c_ubyte(3)
    FLOAT: c_ubyte = c_ubyte(4)
    NODE: c_ubyte = c_ubyte(5)
    NODE_TIME: c_ubyte = c_ubyte(6)
    NODE_INDEX: c_ubyte = c_ubyte(7)
    NODE_LIST: c_ubyte = c_ubyte(8)
    NODE_GEO: c_ubyte = c_ubyte(9)
    GEO: c_ubyte = c_ubyte(10)
    TIME: c_ubyte = c_ubyte(11)
    DURATION: c_ubyte = c_ubyte(12)
    CUBIC: c_ubyte = c_ubyte(13)
    ENUM: c_ubyte = c_ubyte(14)
    OBJECT: c_ubyte = c_ubyte(15)
    TU2D: c_ubyte = c_ubyte(16)
    TU3D: c_ubyte = c_ubyte(17)
    TU4D: c_ubyte = c_ubyte(18)
    TU5D: c_ubyte = c_ubyte(19)
    TU6D: c_ubyte = c_ubyte(20)
    TU10D: c_ubyte = c_ubyte(21)
    TUF2D: c_ubyte = c_ubyte(22)
    TUF3D: c_ubyte = c_ubyte(23)
    TUF4D: c_ubyte = c_ubyte(24)
    BLOCK_REF: c_ubyte = c_ubyte(25)
    FUNCTION: c_ubyte = c_ubyte(26)
    UNDEFINED: c_ubyte = c_ubyte(27)
    STRING_LIT: c_ubyte = c_ubyte(28)
    SIZE: c_ubyte = c_ubyte(29)


class ByteArrayIO(BufferedIOBase):
    def __init__(self: ByteArrayIO, b: bytearray) -> None:
        self.__b = b

    def write(self: ByteArrayIO, __buffer: bytes) -> None:
        self.__b += bytearray(__buffer)


@final
class GreyCat:
    ABI_PROTO: Final[int] = 1

    @final
    class AbiReader:
        def __init__(self, stream: GreyCat._Stream) -> None:
            self.__stream: GreyCat._Stream = stream

        def read(self) -> Any:
            return self.__stream.read()

        def available(self) -> int:
            return len(self.__stream._io.peek())

    @final
    class AbiWriter:
        def __init__(self, stream: GreyCat._Stream) -> None:
            self.__stream: GreyCat._Stream = stream

        def write(self, object: Any) -> None:
            return self.__stream.write(object)

    def openAbiRead(self, path: str) -> GreyCat.AbiReader:
        s: GreyCat._Stream = GreyCat._Stream(self, open(path, "rb"))
        s.read_abi_header()
        return GreyCat.AbiReader(s)

    def openAbiWrite(self, path: str) -> GreyCat.AbiWriter:
        s: GreyCat._Stream = GreyCat._Stream(self, open(path, "wb"))
        s.write_abi_header()
        return GreyCat.AbiWriter(s)

    @final
    class _Stream:
        __ASCII_MAX: Final[c_ubyte] = c_ubyte(127)

        def __init__(self, greycat: GreyCat, io: BufferedReader | BufferedWriter) -> None:
            self.greycat: Final[GreyCat] = greycat
            self._io: BufferedReader | BufferedWriter = io

        def close(self) -> None:
            self._io.close()

        def read_abi_header(self) -> None:
            abi_major: int = self.read_i16().value
            if abi_major != GreyCat.ABI_PROTO:
                raise RuntimeError("wrong ABI protocol major version")
            abi_magic: c_int16 = self.read_i16()
            if abi_magic.value != self.greycat._abi_magic.value:
                raise RuntimeError(f"wrong ABI magic: expected {self.greycat._abi_magic.value}, got {abi_magic.value}")
            abi_version: c_int32 = self.read_i32()
            if abi_version.value > self.greycat._abi_version.value:
                raise RuntimeError("larger ABI version, please reload this handler")

        def read(self) -> Any:
            primitive_offset: c_ubyte = self.read_i8()
            return GreyCat._Stream._PRIMITIVE_LOADERS[primitive_offset.value](self)

        def read_null(self) -> type(None):
            return None

        def read_bool(self) -> bool:
            return self.read_i8().value != 0

        def read_char(self) -> c_char:
            return c_char(self.read_i8().value)

        def read_i8(self) -> c_ubyte:
            return c_ubyte(self._io.read(1)[0])

        def read_i8_array(self, len_: int) -> bytes:
            tmp: bytes = self._io.read(len_)
            if len(tmp) < len_:
                raise Exception(f"{len(tmp)} < {len_}")
            return tmp

        def read_i16(self) -> c_int16:
            tmp: bytes = self.read_i8_array(2)
            return c_int16((tmp[1] << 8) + ((tmp[0] << 8) >> 8))

        def read_i32(self) -> c_int32:
            tmp: bytes = self.read_i8_array(4)
            return c_int32(
                (tmp[3] << 24)
                + ((tmp[2] << 24) >> 8)
                + ((tmp[1] << 24) >> 16)
                + ((tmp[0] << 24) >> 24)
            )

        def read_vu32(self) -> c_uint32:
            current: int
            value: int = 0
            buf: bytes = self._io.peek(5)

            current = buf[0]
            value |= current & 0x7F
            if 0 == (current & 0x80):
                self._io.read(1)
                return c_uint32(value)

            current = buf[1]
            value |= (current & 0x7F) << 7
            if 0 == (current & 0x80):
                self._io.read(2)
                return c_uint32(value)

            current = buf[2]
            value |= (current & 0x7F) << 14
            if 0 == (current & 0x80):
                self._io.read(3)
                return c_uint32(value)

            current = buf[3]
            value |= (current & 0x7F) << 21
            if 0 == (current & 0x80):
                self._io.read(4)
                return c_uint32(value)

            current = buf[4]
            value |= current << 28
            self._io.read(5)
            return c_uint32(value)

        def read_i64(self) -> c_int64:
            tmp: bytes = self.read_i8_array(8)
            return c_int64(
                (tmp[7] << 56)
                + ((tmp[6] << 56) >> 8)
                + ((tmp[5] << 56) >> 16)
                + ((tmp[4] << 56) >> 24)
                + ((tmp[3] << 56) >> 32)
                + ((tmp[2] << 56) >> 40)
                + ((tmp[1] << 56) >> 48)
                + ((tmp[0] << 56) >> 56)
            )

        def read_vi64(self) -> c_int64:
            sign_swapped_value: int = self.read_vu64().value
            return c_int64((sign_swapped_value >> 1) ^ (-(-sign_swapped_value & 1)))

        def read_vu64(self) -> c_uint64:
            current: int
            value: int = 0
            buf: bytes = self._io.peek(9)

            current = buf[0]
            value |= current & 0x7F
            if 0 == (current & 0x80):
                self._io.read(1)
                return c_uint64(value)

            current = buf[1]
            value |= (current & 0x7F) << 7
            if 0 == (current & 0x80):
                self._io.read(2)
                return c_uint64(value)

            current = buf[2]
            value |= (current & 0x7F) << 14
            if 0 == (current & 0x80):
                self._io.read(3)
                return c_uint64(value)

            current = buf[3]
            value |= (current & 0x7F) << 21
            if 0 == (current & 0x80):
                self._io.read(4)
                return c_uint64(value)

            current = buf[4]
            value |= (current & 0x7F) << 28
            if 0 == (current & 0x80):
                self._io.read(5)
                return c_uint64(value)

            current = buf[5]
            value |= (current & 0x7F) << 35
            if 0 == (current & 0x80):
                self._io.read(6)
                return c_uint64(value)

            current = buf[6]
            value |= (current & 0x7F) << 42
            if 0 == (current & 0x80):
                self._io.read(7)
                return c_uint64(value)

            current = buf[7]
            value |= (current & 0x7F) << 49
            if 0 == (current & 0x80):
                self._io.read(8)
                return c_uint64(value)

            current = buf[8]
            value |= current << 56
            self._io.read(9)
            return c_uint64(value)

        def read_f64(self) -> c_double:
            return c_double(unpack("d", pack("q", self.read_i64().value))[0])

        def read_string(self, len_: int) -> str:
            return self.read_i8_array(len_).decode("utf-8")

        def read_string_lit(self) -> str:
            offset: int = self.read_vu32().value
            if 0 == (offset & 1):
                raise IOError("wrong state")
            offset >>= 1
            if offset < len(self.greycat.symbols):
                return self.greycat.symbols[offset]
            raise ValueError("invalid primitive type")

        def read_object(self) -> Any:
            type_offset: int = self.read_vu32().value
            type: Final[GreyCat.Type] = self.greycat.types[type_offset]
            return type.loader(type, self)

        def write_abi_header(self) -> None:
            self.write_i16(c_int16(GreyCat.ABI_PROTO))
            self.write_i16(self.greycat._abi_magic)
            self.write_i32(self.greycat._abi_version)

        def write(self, value: Any) -> None:
            if value is None:
                self.write_i8(PrimitiveType.NULL)
            elif type(value) is bool:
                self.write_i8(PrimitiveType.BOOL)
                self.write_bool(value)
            elif type(value) is c_char:
                c: c_char = value
                self.write_i8(PrimitiveType.CHAR)
                self.write_i8(c_ubyte(c.value[0]))
            elif type(value) is int:
                self.write_i8(PrimitiveType.INT)
                self.write_vi64(c_int64(value))
            elif type(value) is c_int64:
                self.write_i8(PrimitiveType.INT)
                self.write_vi64(value)
            elif type(value) is float:
                self.write_i8(PrimitiveType.FLOAT)
                self.write_f64(c_double(value))
            elif type(value) is c_double:
                self.write_i8(PrimitiveType.FLOAT)
                self.write_f64(value)
            elif type(value) is str:
                try:
                    symbolOffset: int = self.greycat._symbols_off_by_value[value]
                    self.write_i8(PrimitiveType.STRING_LIT)
                    self.write_vu32(c_uint32(symbolOffset << 1 | 1))
                except KeyError:
                    self.write_i8(PrimitiveType.OBJECT)
                    self.write_vu32(c_uint32(self.greycat.type_offset_core_string))
                    data = value.encode("utf-8")
                    self.write_vu32(c_uint32(len(data) << 1))
                    self.write_i8_array(data, 0, len(data))
            elif issubclass(type(value), GreyCat.Object) or type(value) is GreyCat.Object:
                value._save_type(self)
                value._save(self)

        def write_bool(self, b: bool) -> None:
            self._io.write(bytes(c_ubyte(1 if b else 0)))

        def write_i8(self, b: c_ubyte) -> None:
            self._io.write(bytes(b))

        def write_i8_array(self, b: bytearray | bytes, offset: int, len_: int) -> None:
            self._io.write(b[slice(offset, offset + len_)])

        def write_i16(self, i: c_int16) -> None:
            i = i.value
            tmp: bytearray = bytearray(2)
            tmp[0] = i & 0xFF
            tmp[1] = (i >> 8) & 0xFF
            self._io.write(tmp)

        def write_i32(self, i: c_int32) -> None:
            i = i.value
            tmp: bytearray = bytearray(4)
            tmp[0] = i & 0xFF
            tmp[1] = (i >> 8) & 0xFF
            tmp[2] = (i >> 16) & 0xFF
            tmp[3] = (i >> 24) & 0xFF
            self._io.write(tmp)

        def write_vu32(self, u: c_uint32) -> None:
            packed_value: bytearray = bytearray(5)
            value: int = u.value

            packed_value[0] = value & 0x7F
            if value < 0x80:
                self.write_i8_array(packed_value, 0, 1)
                return

            packed_value[0] |= 0x80
            value >>= 7
            packed_value[1] = value & 0x7F
            if value < 0x80:
                self.write_i8_array(packed_value, 0, 2)
                return

            packed_value[1] |= 0x80
            value >>= 7
            packed_value[2] = value & 0x7F
            if value < 0x80:
                self.write_i8_array(packed_value, 0, 3)
                return

            packed_value[2] |= 0x80
            value >>= 7
            packed_value[3] = value & 0x7F
            if value < 0x80:
                self.write_i8_array(packed_value, 0, 4)
                return

            packed_value[3] |= 0x80
            value >>= 7
            packed_value[4] = value & 0x7F
            self.write_i8_array(packed_value, 0, 5)

        def write_i64(self, i: c_int64) -> None:
            i = i.value
            tmp: bytearray = bytearray(8)
            tmp[0] = i & 0xFF
            tmp[1] = (i >> 8) & 0xFF
            tmp[2] = (i >> 16) & 0xFF
            tmp[3] = (i >> 24) & 0xFF
            tmp[4] = (i >> 32) & 0xFF
            tmp[5] = (i >> 40) & 0xFF
            tmp[6] = (i >> 48) & 0xFF
            tmp[7] = (i >> 56) & 0xFF
            self._io.write(tmp)

        def write_vi64(self, i: c_int64) -> None:
            self.write_vu64(c_uint64((i.value << 1) ^ (i.value >> 63)))

        def write_vu64(self, u: c_uint64) -> None:
            packed_value: Final[bytearray] = bytearray(9)
            value: int = u.value

            packed_value[0] = c_ubyte(value & 0x7F).value
            if value < 0x80:
                self.write_i8_array(packed_value, 0, 1)
                return

            packed_value[0] |= 0x80
            value >>= 7
            packed_value[1] = c_ubyte(value).value
            if value < 0x80:
                self.write_i8_array(packed_value, 0, 2)
                return

            packed_value[1] |= 0x80
            value >>= 7
            packed_value[2] = c_ubyte(value).value
            if value < 0x80:
                self.write_i8_array(packed_value, 0, 3)
                return

            packed_value[2] |= 0x80
            value >>= 7
            packed_value[3] = c_ubyte(value).value
            if value < 0x80:
                self.write_i8_array(packed_value, 0, 4)
                return

            packed_value[3] |= 0x80
            value >>= 7
            packed_value[4] = c_ubyte(value).value
            if value < 0x80:
                self.write_i8_array(packed_value, 0, 5)
                return

            packed_value[4] |= 0x80
            value >>= 7
            packed_value[5] = c_ubyte(value).value
            if value < 0x80:
                self.write_i8_array(packed_value, 0, 6)
                return

            packed_value[5] |= 0x80
            value >>= 7
            packed_value[6] = c_ubyte(value).value
            if value < 0x80:
                self.write_i8_array(packed_value, 0, 7)
                return

            packed_value[6] |= 0x80
            value >>= 7
            packed_value[7] = c_ubyte(value).value
            if value < 0x80:
                self.write_i8_array(packed_value, 0, 8)
                return

            packed_value[7] |= 0x80
            value >>= 7
            packed_value[8] = c_ubyte(value).value
            self.write_i8_array(packed_value, 0, 9)

        def write_f64(self, d: c_double):
            self.write_i64(c_int64(unpack("q", pack("d", d.value))[0]))

        __PrimitiveLoader: Final[type[Callable[[GreyCat._Stream], object]]] = Callable[
            [object], object
        ]

        __null_loader: Final[
            Callable[[GreyCat._Stream], object]
        ] = lambda stream: stream.read_null()
        __bool_loader: Final[
            Callable[[GreyCat._Stream], object]
        ] = lambda stream: stream.read_bool()
        __char_loader: Final[
            Callable[[GreyCat._Stream], object]
        ] = lambda stream: stream.read_char()
        __i64_loader: Final[
            Callable[[GreyCat._Stream], object]
        ] = lambda stream: stream.read_vi64()
        __f64_loader: Final[
            Callable[[GreyCat._Stream], object]
        ] = lambda stream: stream.read_f64()

        @staticmethod
        @final
        def __type_loader(stream: GreyCat._Stream, type: GreyCat.Type) -> object:
            return type.loader(type, stream)

        __node_loader: Final[
            Callable[[GreyCat._Stream], object]
        ] = lambda stream: GreyCat._Stream.__type_loader(
            stream, stream.greycat.types[stream.greycat.type_offset_core_node]
        )
        __node_time_loader: Final[
            Callable[[GreyCat._Stream], object]
        ] = lambda stream: GreyCat._Stream.__type_loader(
            stream, stream.greycat.types[stream.greycat.type_offset_core_node_time]
        )
        __node_index_loader: Final[
            Callable[[GreyCat._Stream], object]
        ] = lambda stream: GreyCat._Stream.__type_loader(
            stream, stream.greycat.types[stream.greycat.type_offset_core_node_index]
        )
        __node_list_loader: Final[
            Callable[[GreyCat._Stream], object]
        ] = lambda stream: GreyCat._Stream.__type_loader(
            stream, stream.greycat.types[stream.greycat.type_offset_core_node_list]
        )
        __node_geo_loader: Final[
            Callable[[GreyCat._Stream], object]
        ] = lambda stream: GreyCat._Stream.__type_loader(
            stream, stream.greycat.types[stream.greycat.type_offset_core_node_geo]
        )
        __geo_loader: Final[
            Callable[[GreyCat._Stream], object]
        ] = lambda stream: GreyCat._Stream.__type_loader(
            stream, stream.greycat.types[stream.greycat.type_offset_core_geo]
        )
        __time_loader: Final[
            Callable[[GreyCat._Stream], object]
        ] = lambda stream: GreyCat._Stream.__type_loader(
            stream, stream.greycat.types[stream.greycat.type_offset_core_time]
        )
        __duration_loader: Final[
            Callable[[GreyCat._Stream], object]
        ] = lambda stream: GreyCat._Stream.__type_loader(
            stream, stream.greycat.types[stream.greycat.type_offset_core_duration]
        )

        __object_loader: Final[
            Callable[[GreyCat._Stream], object]
        ] = lambda stream: stream.read_object()

        __tu2d_loader: Final[
            Callable[[GreyCat._Stream], object]
        ] = lambda stream: GreyCat._Stream.__type_loader(
            stream, stream.greycat.types[stream.greycat.type_offset_core_ti2d]
        )

        __tu3d_loader: Final[
            Callable[[GreyCat._Stream], object]
        ] = lambda stream: GreyCat._Stream.__type_loader(
            stream, stream.greycat.types[stream.greycat.type_offset_core_ti3d]
        )

        __tu4d_loader: Final[
            Callable[[GreyCat._Stream], object]
        ] = lambda stream: GreyCat._Stream.__type_loader(
            stream, stream.greycat.types[stream.greycat.type_offset_core_ti4d]
        )

        __tu5d_loader: Final[
            Callable[[GreyCat._Stream], object]
        ] = lambda stream: GreyCat._Stream.__type_loader(
            stream, stream.greycat.types[stream.greycat.type_offset_core_ti5d]
        )

        __tu6d_loader: Final[
            Callable[[GreyCat._Stream], object]
        ] = lambda stream: GreyCat._Stream.__type_loader(
            stream, stream.greycat.types[stream.greycat.type_offset_core_ti6d]
        )

        __tu10d_loader: Final[
            Callable[[GreyCat._Stream], object]
        ] = lambda stream: GreyCat._Stream.__type_loader(
            stream, stream.greycat.types[stream.greycat.type_offset_core_ti10d]
        )

        __tf2d_loader: Final[
            Callable[[GreyCat._Stream], object]
        ] = lambda stream: GreyCat._Stream.__type_loader(
            stream, stream.greycat.types[stream.greycat.type_offset_core_tf2d]
        )

        __tf3d_loader: Final[
            Callable[[GreyCat._Stream], object]
        ] = lambda stream: GreyCat._Stream.__type_loader(
            stream, stream.greycat.types[stream.greycat.type_offset_core_tf3d]
        )

        __tf4d_loader: Final[
            Callable[[GreyCat._Stream], object]
        ] = lambda stream: GreyCat._Stream.__type_loader(
            stream, stream.greycat.types[stream.greycat.type_offset_core_tf4d]
        )

        @staticmethod
        @final
        def __error_loader(stream: GreyCat._Stream) -> object:
            raise ValueError("invalid primitive type")

        __string_lit_loader: Final[
            Callable[[GreyCat._Stream], object]
        ] = lambda stream: stream.read_string_lit()

        _PRIMITIVE_LOADERS: Final[list[__PrimitiveLoader]] = [
            None
        ] * PrimitiveType.SIZE.value
        _PRIMITIVE_LOADERS[PrimitiveType.NULL.value] = __null_loader
        _PRIMITIVE_LOADERS[PrimitiveType.BOOL.value] = __bool_loader
        _PRIMITIVE_LOADERS[PrimitiveType.CHAR.value] = __char_loader
        _PRIMITIVE_LOADERS[PrimitiveType.INT.value] = __i64_loader
        _PRIMITIVE_LOADERS[PrimitiveType.FLOAT.value] = __f64_loader
        _PRIMITIVE_LOADERS[PrimitiveType.NODE.value] = __node_loader
        _PRIMITIVE_LOADERS[PrimitiveType.NODE_TIME.value] = __node_time_loader
        _PRIMITIVE_LOADERS[PrimitiveType.NODE_INDEX.value] = __node_index_loader
        _PRIMITIVE_LOADERS[PrimitiveType.NODE_LIST.value] = __node_list_loader
        _PRIMITIVE_LOADERS[PrimitiveType.NODE_GEO.value] = __node_geo_loader
        _PRIMITIVE_LOADERS[PrimitiveType.GEO.value] = __geo_loader
        _PRIMITIVE_LOADERS[PrimitiveType.TIME.value] = __time_loader
        _PRIMITIVE_LOADERS[PrimitiveType.DURATION.value] = __duration_loader
        _PRIMITIVE_LOADERS[PrimitiveType.ENUM.value] = __object_loader
        _PRIMITIVE_LOADERS[PrimitiveType.OBJECT.value] = __object_loader
        _PRIMITIVE_LOADERS[PrimitiveType.TU2D.value] = __tu2d_loader
        _PRIMITIVE_LOADERS[PrimitiveType.TU3D.value] = __tu3d_loader
        _PRIMITIVE_LOADERS[PrimitiveType.TU4D.value] = __tu4d_loader
        _PRIMITIVE_LOADERS[PrimitiveType.TU5D.value] = __tu5d_loader
        _PRIMITIVE_LOADERS[PrimitiveType.TU6D.value] = __tu6d_loader
        _PRIMITIVE_LOADERS[PrimitiveType.TU10D.value] = __tu10d_loader
        _PRIMITIVE_LOADERS[PrimitiveType.TUF2D.value] = __tf2d_loader
        _PRIMITIVE_LOADERS[PrimitiveType.TUF3D.value] = __tf3d_loader
        _PRIMITIVE_LOADERS[PrimitiveType.TUF4D.value] = __tf4d_loader
        _PRIMITIVE_LOADERS[PrimitiveType.BLOCK_REF.value] = __error_loader
        _PRIMITIVE_LOADERS[PrimitiveType.FUNCTION.value] = __error_loader  # TODO?
        _PRIMITIVE_LOADERS[PrimitiveType.UNDEFINED.value] = __error_loader
        _PRIMITIVE_LOADERS[PrimitiveType.STRING_LIT.value] = __string_lit_loader

    class Function:
        def __init__(self, name: str) -> None:
            self.name: Final[str] = name

    class Type:
        class Attribute:
            def __init__(
                self,
                name: str,
                abi_type: int,
                prog_type_offset: int,
                mapped_any_offset: int,
                mapped_att_offset: int,
                sbi_type: c_ubyte,
                nullable: bool,
                mapped: bool,
            ):
                self.name: Final[str] = name
                self.abi_type: Final[int] = abi_type
                self.prog_type_offset: Final[int] = prog_type_offset
                self.mapped_any_offset: Final[int] = mapped_any_offset
                self.mapped_att_offset: Final[int] = mapped_att_offset
                self.sbi_type: Final[c_ubyte] = sbi_type
                self.nullable: Final[bool] = nullable
                self.mapped: Final[bool] = mapped

        @staticmethod
        @final
        def __error_loader(type: GreyCat.Type, stream: GreyCat._Stream) -> Any:
            raise ValueError("wrong state")

        @staticmethod
        @final
        def __enum_loader(type: GreyCat.Type, stream: GreyCat._Stream) -> Any:
            program_type: Final[GreyCat.Type] = type.greycat.types[type.mapped_type_off]
            value_offset: Final[int] = stream.read_vu32().value
            abi_type_att: Final[GreyCat.Type.Attribute] = type.attributes[value_offset]
            return program_type.enum_values[abi_type_att.mapped_att_offset]

        @staticmethod
        @final
        def __object_loader(type: GreyCat.Type, stream: GreyCat._Stream) -> Any:
            program_type: Final[GreyCat.Type] = type.greycat.types[type.mapped_type_off]
            attributes: Final[list[Any]] = [None] * len(program_type.attributes)
            nullable_bitset: bytes = stream.read_i8_array(type.nullable_nb_bytes)
            nullable_offset: int = -1
            att_offset: int
            for att_offset in range(len(type.attributes)):
                att: GreyCat.Type.Attribute = type.attributes[att_offset]
                loaded_field: Any
                if att.nullable:
                    nullable_offset += 1
                    if 0 == (
                        (
                            (nullable_bitset[nullable_offset >> 3])
                            >> (nullable_offset & 7)
                        )
                        & 1
                    ):
                        continue
                load_type: c_ubyte = att.sbi_type.value
                if load_type == PrimitiveType.UNDEFINED.value:
                    load_type = stream.read_i8().value
                match load_type:
                    case PrimitiveType.ENUM.value:
                        field_type: GreyCat.Type = type.greycat.types[att.abi_type]
                        loaded_field = GreyCat.Type.__enum_loader(field_type, stream)
                    case PrimitiveType.OBJECT.value:
                        field_type: GreyCat.Type = type.greycat.types[att.abi_type]
                        if (not field_type.is_native) and (
                            field_type.is_abstract
                            or att.sbi_type.value == PrimitiveType.UNDEFINED.value
                        ):
                            field_type = type.greycat.types[stream.read_vu32().value]
                        loaded_field = field_type.loader(field_type, stream)
                    case _:
                        loaded_field = GreyCat._Stream._PRIMITIVE_LOADERS[
                            att.sbi_type.value
                        ](stream)
                if att.mapped:
                    attributes[att.mapped_att_offset] = loaded_field
            if program_type.factory is None:
                return GreyCat.Object(program_type, attributes)
            else:
                return program_type.factory(program_type, attributes)

        def __init__(
            self,
            offset: int,
            name: str,
            mapped_type_off: int,
            masked_type_off: int,
            nullable_nb_bytes: int,
            is_masked: bool,
            is_abstract: bool,
            is_enum: bool,
            is_native: bool,
            type_attributes: list[GreyCat.Type.Attribute],
            factory: GreyCat.Factory | None,
            loader: GreyCat.Loader | None,
            greycat: GreyCat,
        ) -> None:
            self.offset: Final[int] = offset
            self.name: Final[str] = name
            self.mapped_type_off: Final[int] = mapped_type_off
            self.masked_type_off: Final[int] = masked_type_off
            self.nullable_nb_bytes: Final[int] = nullable_nb_bytes
            self.is_masked: Final[bool] = is_masked
            self.is_abstract: Final[bool] = is_abstract
            self.is_enum: Final[bool] = is_enum
            self.is_native: Final[bool] = is_native
            self.attributes: Final[list[GreyCat.Type.Attribute]] = type_attributes
            self.attribute_off_by_name: Final[dict[str, int]] = {}
            att_offset: int
            for att_offset in range(len(type_attributes)):
                self.attribute_off_by_name[
                    type_attributes[att_offset].name
                ] = att_offset
            self.greycat: Final[GreyCat] = greycat
            self.factory: Final[GreyCat.Factory] = factory
            self.enum_values: Final[list[GreyCat.Enum]] | None
            if offset == mapped_type_off:
                if self.is_enum:
                    self.enum_values = [None] * len(type_attributes)
                    enum_offset: int
                    for enum_offset in range(len(type_attributes)):
                        attributes: list[Any] = [
                            enum_offset,
                            type_attributes[enum_offset].name,
                            None,
                        ]
                        if self.factory is None:
                            self.enum_values[enum_offset] = GreyCat.Enum(
                                self, attributes
                            )
                        else:
                            self.enum_values[enum_offset] = self.factory(
                                self, attributes
                            )
                else:
                    self.enum_values = None
            else:
                self.enum_values = None
            self.loader: Final[GreyCat.Loader]
            if not (loader is None):
                self.loader = loader
            elif self.is_native:
                self.loader = GreyCat.Type.__error_loader
            elif self.is_enum:
                self.loader = GreyCat.Type.__enum_loader
            else:
                self.loader = GreyCat.Type.__object_loader
            self.static_values: list[Any] = []
            self.generated_offsets: list[int] | None = None

        def resolve_generated_offsets(self, *args: str) -> None:
            self.generated_offsets: list[int] = [-1] * len(args)
            name_offset: int
            for name_offset in range(len(args)):
                resolved: int | None = self.attribute_off_by_name.get(args[name_offset])
                if resolved is None:
                    raise ValueError(
                        "unmapped generated field, please re-generate this code!"
                    )
                self.generated_offsets[name_offset] = resolved

        def resolve_generated_offset_with_values(self, *args: Any) -> None:
            self.generated_offsets: list[int] = [-1] * int(len(args) / 2)
            name_offset: int
            for name_offset in range(0, len(args), 2):
                resolved: int | None = self.attribute_off_by_name.get(args[name_offset])
                if resolved is None:
                    raise ValueError(
                        "unmapped generated field, please re-generate this code!"
                    )
                self.generated_offsets[int(name_offset / 2)] = resolved
                self.enum_values[resolved].value = args[name_offset + 1]

    class Object:
        def __init__(self, type: GreyCat.Type, attributes: list[Any] | None) -> None:
            self.type_: Final[GreyCat.Type] = type
            self.attributes: list[Any] | None = attributes

        def get(self, attribute_name: str) -> Any | None:
            return self._get(self.type_.attribute_off_by_name[attribute_name])

        def set(self, attribute_name: str, value: Any | None) -> None:
            self._set(self.type_.attribute_off_by_name[attribute_name], value)

        def _get(self, offset: int) -> Any | None:
            return self.attributes[offset]

        def _set(self, offset: int, value: Any | None) -> None:
            self.attributes[offset] = value

        def _save_type(self, stream: GreyCat._Stream) -> None:
            stream.write_i8(PrimitiveType.OBJECT)
            stream.write_vu32(c_uint32(self.type_.offset))

        def _save(self, stream: GreyCat._Stream) -> None:
            nullable_bitset: bytearray = bytearray(self.type_.nullable_nb_bytes)
            nullable_offset: int = 0
            field: GreyCat.Type.Attribute
            offset: int
            for offset in range(len(self.type_.attributes)):
                field = self.type_.attributes[offset]
                if field.nullable:
                    nullable_bitset[nullable_offset >> 3] |= (
                        0 if self._get(offset) is None else 1
                    ) << (nullable_offset & 7)
                    nullable_offset += 1
            stream.write_i8_array(nullable_bitset, 0, len(nullable_bitset))
            o: GreyCat.Object
            e: GreyCat.Enum
            for offset in range(len(self.type_.attributes)):
                field = self.type_.attributes[offset]
                value = self._get(offset)
                if field.nullable and (value is None):
                    continue
                match field.sbi_type.value:
                    case PrimitiveType.NULL.value:
                        pass
                    case PrimitiveType.BOOL.value:
                        stream.write_bool(bool(value))
                    case PrimitiveType.CHAR.value:
                        c: c_ubyte = c_ubyte(value)
                        if c > GreyCat._Stream.__ASCII_MAX:
                            raise ValueError(f"Only ASCII characters are allowed: {c}")
                        stream.write_i8(c)
                    case PrimitiveType.INT.value:
                        if type(value) is c_int64:
                            stream.write_vi64(value)
                        else:
                            stream.write_vi64(c_int64(value))
                    case PrimitiveType.FLOAT.value:
                        if type(value) is c_double:
                            stream.write_f64(value)
                        else:
                            stream.write_f64(c_double(value))
                    case PrimitiveType.NODE.value:
                        o._save(stream)
                    case PrimitiveType.NODE_TIME.value:
                        o = value
                        o._save(stream)
                    case PrimitiveType.NODE_INDEX.value:
                        o = value
                        o._save(stream)
                    case PrimitiveType.NODE_LIST.value:
                        o = value
                        o._save(stream)
                    case PrimitiveType.NODE_GEO.value:
                        o = value
                        o._save(stream)
                    case PrimitiveType.GEO.value:
                        o = value
                        o._save(stream)
                    case PrimitiveType.TU2D.value:
                        o = value
                        o._save(stream)
                    case PrimitiveType.TU3D.value:
                        o = value
                        o._save(stream)
                    case PrimitiveType.TU4D.value:
                        o = value
                        o._save(stream)
                    case PrimitiveType.TU5D.value:
                        o = value
                        o._save(stream)
                    case PrimitiveType.TU6D.value:
                        o = value
                        o._save(stream)
                    case PrimitiveType.TU10D.value:
                        o = value
                        o._save(stream)
                    case PrimitiveType.TUF2D.value:
                        o = value
                        o._save(stream)
                    case PrimitiveType.TUF3D.value:
                        o = value
                        o._save(stream)
                    case PrimitiveType.TUF4D.value:
                        o = value
                        o._save(stream)
                    case PrimitiveType.TIME.value:
                        o = value
                        o._save(stream)
                    case PrimitiveType.DURATION.value:
                        o = value
                        o._save(stream)
                    case PrimitiveType.ENUM.value:
                        o = value
                        o._save(stream)
                    case PrimitiveType.OBJECT.value:
                        if type(value) is str:
                            string: str = value
                            symbol_offset: int | None = (
                                self.type_.greycat._symbols_off_by_value[string]
                            )
                            if not (symbol_offset is None):
                                stream.write_vu32(c_uint32((symbol_offset << 1) | 1))
                            else:
                                data: bytes = string.encode("utf-8")
                                stream.write_vu32(c_uint32(len(data)))
                                stream.write_i8_array(bytes, 0, len(data))
                        else:
                            o: GreyCat.Object = value
                            if field.abi_type != o.type_.offset:
                                stream.write_vu32(o.type_.offset)
                            o._save(stream)
                    # case PrimitiveType.BLOCK_REF: # TODO
                    # case PrimitiveType.FUNCTION: # TODO
                    case PrimitiveType.UNDEFINED.value:
                        stream.write(value)
                    case _:
                        raise ValueError(f"wrong state: {field.sbi_type.value}")

        def __str__(self) -> str:
            res = f"{self.type_.name}{{"
            offset: int
            for offset in range(len(self.type_.attributes)):
                if offset > 0:
                    res = f"{res},"
                res = f"{res}{self.type_.attributes[offset].name}={self.attributes[offset]}"
            res = f"{res}}}"
            return res

    class Enum(Object):
        def __init__(self, type: GreyCat.Type, attributes: list[Any]) -> None:
            super().__init__(type, attributes)
            self.__offset: Final[int] = attributes[0]
            self.key: Final[str] = attributes[1]
            self.value: Any = attributes[2]

        @final
        def _save_type(self, stream: GreyCat._Stream) -> None:
            stream.write_i8(PrimitiveType.ENUM)
            stream.write_vu32(c_uint32(self.type_.offset))

        @final
        def _save(self, stream: GreyCat._Stream) -> None:
            stream.write_vu32(c_uint32(self.__offset))

        def __str__(self) -> str:
            if self.value is None:
                return f"{self.type_.name}.{self.key}"
            return f"{self.type_.name}.{self.key}{{value={self.value}}}"

    Loader: Final[type[Callable[[Type, _Stream], Any]]] = Callable[[Type, _Stream], Any]

    Factory: Final[type[Callable[[Type, list[Any]], Any]]] = Callable[
        [Type, list[object]], Any
    ]

    class Library:
        def __init__(self) -> None:
            self.mapped: list[GreyCat.Type] | None = None

        def name(self) -> str:
            raise NotImplementedError

        def configure(
            self,
            loaders: dict[str, GreyCat.Loader],
            factories: dict[str, GreyCat.Factory],
        ) -> None:
            raise NotImplementedError

        def init(self, greycat: GreyCat) -> None:
            raise NotImplementedError

    class Files:  # TODO?
        pass

    def __init__(self, url: str, libraries: list[GreyCat.Library] = []) -> None:
        self.libs_by_name: Final[dict[str, GreyCat.Library]] = {}
        std_: std = std()
        self.libs_by_name[std_.name()] = std_
        self.__is_remote: bool = False
        library_offset: int
        # for declarations
        lib: GreyCat.Library
        for library_offset in range(len(libraries)):
            lib = libraries[library_offset]
            self.libs_by_name[lib.name()] = lib
        loaders: Final[dict[str, GreyCat.Loader]] = {}
        factories: Final[dict[str, GreyCat.Factory]] = {}
        for lib in self.libs_by_name.values():
            lib.configure(loaders, factories)
        self.__runtime_url: Final[str] = url
        abi_stream: Final[GreyCat._Stream] = self.__get_abi(url)

        # step 0: verify abi version
        abi_major: int = abi_stream.read_i16().value
        if abi_major != GreyCat.ABI_PROTO:
            raise Exception(f"wrong ABI proto: expected ${GreyCat.ABI_PROTO}, got {abi_major}")
        self._abi_magic: Final[c_int16] = abi_stream.read_i16()
        self._abi_version: Final[c_int32] = abi_stream.read_i32()
        crc: c_int64 = abi_stream.read_i64()

        # step 1: create all symbols
        symbols_bytes: Final[c_int64] = abi_stream.read_i64()
        symbols_count: Final[int] = abi_stream.read_i32().value
        self.symbols: Final[list[str | None]] = [None] * (symbols_count + 1)
        self._symbols_off_by_value: Final[dict[str, int]] = {}
        offset: int
        for offset in range(1, symbols_count + 1):
            symbol: str = abi_stream.read_string(abi_stream.read_vu32().value)
            self.symbols[offset] = symbol
            self._symbols_off_by_value[symbol] = offset

        # step 2: create all types
        types_bytes: Final[c_int64] = abi_stream.read_i64()
        types_size: Final[int] = abi_stream.read_i32().value
        self.types: Final[list[GreyCat.Type]] = [None] * types_size
        attributes_size: Final[c_int32] = abi_stream.read_i32()
        type_offset: int
        self.types_by_name: Final[dict[str, GreyCat.Type]] = {}
        for type_offset in range(types_size):
            module_name: str = self.symbols[abi_stream.read_vu32().value]
            type_name: str = self.symbols[abi_stream.read_vu32().value]
            lib_name: str = self.symbols[abi_stream.read_vu32().value]
            fqn: str = f'{"" if module_name is None else f"{module_name}::"}{type_name}'
            attributes_len: int = abi_stream.read_vu32().value
            abi_stream.read_vu32()  # unused field
            abi_stream.read_vu32()  # unused field
            mapped_abi_type_offset: int = abi_stream.read_vu32().value
            masked_abi_type_offset: int = abi_stream.read_vu32().value
            nullable_nb_bytes: int = abi_stream.read_vu32().value
            flags: int = abi_stream.read_i8().value
            is_native: bool = 0 != (flags & 1)
            is_abstract: bool = 0 != (flags & (1 << 1))
            is_enum: bool = 0 != (flags & (1 << 2))
            is_masked: bool = 0 != (flags & (1 << 3))
            type_attributes: Final[list[GreyCat.Type.Attribute]] = [
                None
            ] * attributes_len
            enum_offset: int
            for enum_offset in range(attributes_len):
                name: Final[str] = self.symbols[abi_stream.read_vu32().value]
                att_abi_type: Final[int] = abi_stream.read_vu32().value
                prog_type_offset: Final[int] = abi_stream.read_vu32().value
                mapped_any_offset: Final[int] = abi_stream.read_vu32().value
                mapped_att_offset: Final[int] = abi_stream.read_vu32().value
                sbi_type: Final[c_ubyte] = abi_stream.read_i8()
                att_flags: Final[int] = abi_stream.read_i8().value
                nullable: Final[bool] = 0 != (att_flags & 1)
                mapped: Final[bool] = 0 != (att_flags & (1 << 1))
                type_attributes[enum_offset] = GreyCat.Type.Attribute(
                    name,
                    att_abi_type,
                    prog_type_offset,
                    mapped_any_offset,
                    mapped_att_offset,
                    sbi_type,
                    nullable,
                    mapped,
                )
            factory: GreyCat.Factory | None = None
            try:
                factory = factories[fqn]
            except KeyError:
                pass
            loader: GreyCat.Loader | None = None
            try:
                loader = loaders[fqn]
            except KeyError:
                pass
            abi_type: GreyCat.Type = GreyCat.Type(
                type_offset,
                fqn,
                mapped_abi_type_offset,
                masked_abi_type_offset,
                nullable_nb_bytes,
                is_masked,
                is_abstract,
                is_enum,
                is_native,
                type_attributes,
                factory,
                loader,
                self,
            )
            if abi_type.mapped_type_off == type_offset and len(fqn) != 0:
                self.types_by_name[abi_type.name] = abi_type
            self.types[type_offset] = abi_type
        # step 3: create all functions
        functions_bytes: Final[c_int64] = abi_stream.read_i64()
        functions_size: Final[int] = abi_stream.read_i32().value
        self.functions_by_name: Final[dict] = {}
        function_offset: int
        for function_offset in range(functions_size):
            module_name: str = self.symbols[abi_stream.read_vu32().value]
            type_name: str = self.symbols[abi_stream.read_vu32().value]
            function_name: str = self.symbols[abi_stream.read_vu32().value]
            lib_name: str = self.symbols[abi_stream.read_vu32().value]
            fqn: str = (
                f'{"" if module_name is None else f"{module_name}::"}{function_name}'
            )
            nb_params: int = abi_stream.read_vu32().value
            param_offset: int
            for param_offset in range(nb_params):
                abi_stream.read_i8()
                abi_stream.read_vu32()
                abi_stream.read_vu32()
            abi_stream.read_vu32()
            abi_stream.read_i8()
            fn: GreyCat.Function = GreyCat.Function(fqn)
            self.functions_by_name[fqn] = fn
        # pre-resolve String type avoid runtime over-head
        tmp: GreyCat.Type = self.types_by_name["core::String"]
        if tmp is None:
            raise ValueError("wrong state")
        self.type_offset_core_string: Final[int] = tmp.offset

        tmp = self.types_by_name["core::duration"]
        if tmp is None:
            raise ValueError("wrong state")
        self.type_offset_core_duration: Final[int] = tmp.offset

        tmp = self.types_by_name["core::time"]
        if tmp is None:
            raise ValueError("wrong state")
        self.type_offset_core_time: Final[int] = tmp.offset

        tmp = self.types_by_name["core::geo"]
        if tmp is None:
            raise ValueError("wrong state")
        self.type_offset_core_geo: Final[int] = tmp.offset

        tmp = self.types_by_name["core::nodeList"]
        if tmp is None:
            raise ValueError("wrong state")
        self.type_offset_core_node_list: Final[int] = tmp.offset

        tmp = self.types_by_name["core::nodeIndex"]
        if tmp is None:
            raise ValueError("wrong state")
        self.type_offset_core_node_index: Final[int] = tmp.offset

        tmp = self.types_by_name["core::nodeTime"]
        if tmp is None:
            raise ValueError("wrong state")
        self.type_offset_core_node_time: Final[int] = tmp.offset

        tmp = self.types_by_name["core::nodeGeo"]
        if tmp is None:
            raise ValueError("wrong state")
        self.type_offset_core_node_geo: Final[int] = tmp.offset

        tmp = self.types_by_name["core::node"]
        if tmp is None:
            raise ValueError("wrong state")
        self.type_offset_core_node: Final[int] = tmp.offset

        tmp = self.types_by_name["core::ti2d"]
        if tmp is None:
            raise ValueError("wrong state")
        self.type_offset_core_ti2d: Final[int] = tmp.offset

        tmp = self.types_by_name["core::ti3d"]
        if tmp is None:
            raise ValueError("wrong state")
        self.type_offset_core_ti3d: Final[int] = tmp.offset

        tmp = self.types_by_name["core::ti4d"]
        if tmp is None:
            raise ValueError("wrong state")
        self.type_offset_core_ti4d: Final[int] = tmp.offset

        tmp = self.types_by_name["core::ti5d"]
        if tmp is None:
            raise ValueError("wrong state")
        self.type_offset_core_ti5d: Final[int] = tmp.offset

        tmp = self.types_by_name["core::ti6d"]
        if tmp is None:
            raise ValueError("wrong state")
        self.type_offset_core_ti6d: Final[int] = tmp.offset

        tmp = self.types_by_name["core::ti10d"]
        if tmp is None:
            raise ValueError("wrong state")
        self.type_offset_core_ti10d: Final[int] = tmp.offset

        tmp = self.types_by_name["core::tf2d"]
        if tmp is None:
            raise ValueError("wrong state")
        self.type_offset_core_tf2d: Final[int] = tmp.offset

        tmp = self.types_by_name["core::tf3d"]
        if tmp is None:
            raise ValueError("wrong state")
        self.type_offset_core_tf3d: Final[int] = tmp.offset

        tmp = self.types_by_name["core::tf4d"]
        if tmp is None:
            raise ValueError("wrong state")
        self.type_offset_core_tf4d: Final[int] = tmp.offset

        abi_stream.close()
        for lib in self.libs_by_name.values():
            lib.init(self)

    @staticmethod
    def call(greycat: GreyCat, fqn: str, parameters: list[object]) -> object:
        if not (greycat.__is_remote):
            raise RuntimeError(
                "Remote calls are not available on local GreyCat handles"
            )
        fn: GreyCat.Function = greycat.functions_by_name[fqn]
        if fn is None:
            raise RuntimeError(f"Function not found with name {fqn}")
        url: str = f"{greycat.__runtime_url}/{fqn}"
        connection: http.client.HTTPConnection | http.client.HTTPSConnection
        if url.startswith("http://"):
            connection = http.client.HTTPConnection(url.replace("http://", ""))
        elif greycat.__runtime_url.startswith("https://"):
            connection = http.client.HTTPSConnection(url.replace("https://", ""))
        else:
            raise ValueError("wrong state")
        body: bytes | None = None
        stream: GreyCat._Stream
        if len(parameters > 0):
            b = bytearray()
            stream = GreyCat._Stream(greycat, ByteArrayIO(b))
            stream.write_abi_header()
            for offset in range(len(parameters)):
                stream.write(parameters[offset])
            stream.close()
            body = bytes(b)
        connection.request(
            "POST",
            fqn.replace(".", "/"),
            body,
            {
                "Accept": "application/octet-stream",
                "Content-Type": "application/octet-stream",
            },
        )
        response: http.client.HTTPResponse = connection.getresponse()
        status: int = response.status
        stream = GreyCat._Stream(greycat, response)
        if 200 > status or 300 <= status:
            raise RuntimeError(str(stream.read()))
        stream.read_abi_header()
        res = stream.read()
        # if len(response.read(1)) > 0:
        #     raise IOError('Remaining unread bytes')
        stream.close()
        return res

    def create(self, name: str, parameters: list[Any]) -> Any:
        type: Final[GreyCat.Type | None] = self.types_by_name[name]
        if type is None:
            return None
        return type.factory[type, parameters]

    def create_geo(self, lat: c_double, lng: c_double):
        type: GreyCat.Type = self.types[self.type_offset_core_geo]
        geo: std.core.geo = type.factory(type, [])
        geo.lat = c_double(lat)
        geo.lng = c_double(lng)
        return geo

    def create_time(self, epoch_us: c_int64):
        type: GreyCat.Type = self.types[self.type_offset_core_geo]
        t: std.core.time = type.factory(type, [])
        t.value = epoch_us
        return t

    def create_duration(self, duration_us: c_int64):
        type: GreyCat.Type = self.types[self.type_offset_core_geo]
        dur: std.core.duration = type.factory(type, [])
        dur.value = duration_us
        return dur

    def __get_remote_abi(self, runtime_url: str) -> GreyCat._Stream:
        connection: http.client.HTTPConnection | http.client.HTTPSConnection
        if runtime_url.startswith("http://"):
            connection: http.client.HTTPConnection = http.client.HTTPConnection(
                runtime_url.replace("http://", "")
            )
        elif runtime_url.startswith("https://"):
            connection: http.client.HTTPSConnection = http.client.HTTPSConnection(
                runtime_url.replace("https://", "")
            )
        else:
            raise ValueError
        connection.request(
            "POST", "runtime/Runtime/abi", None, {"Accept": "application/octet-stream"}
        )
        response: http.client.HTTPResponse = connection.getresponse()
        status: int = response.status
        if 200 > status or 300 <= status:
            msg = ""
            line: str = response.readline()
            while line is not None:
                msg = f"{msg}{line}\n"
                line = response.readline()
            raise RuntimeError(msg)
        self.__is_remote = True
        return GreyCat._Stream(self, response)

    def __get_local_abi(self, runtime_url: str) -> GreyCat._Stream:
        if runtime_url.startswith("file://"):
            runtime_url = runtime_url.replace("file://", "", 1)
        return GreyCat._Stream(
            self, open(os.path.join(runtime_url, "gcdata", "store", "abi"), "rb")
        )

    def __get_abi(self, runtime_url: str) -> GreyCat._Stream:
        if runtime_url.startswith("http"):
            return self.__get_remote_abi(runtime_url)
        else:
            return self.__get_local_abi(runtime_url)


from .std import std
