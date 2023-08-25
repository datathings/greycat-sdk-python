from __future__ import annotations

from ctypes import *
import http.client
from io import *
from struct import pack, unpack
from typing import *


@final
class PrimitiveType:
    NULL: c_byte = c_byte(0)
    BOOL: c_byte = c_byte(1)
    CHAR: c_byte = c_byte(2)
    INT: c_byte = c_byte(3)
    FLOAT: c_byte = c_byte(4)
    NODE: c_byte = c_byte(5)
    NODE_TIME: c_byte = c_byte(6)
    NODE_INDEX: c_byte = c_byte(7)
    NODE_LIST: c_byte = c_byte(8)
    NODE_GEO: c_byte = c_byte(9)
    GEO: c_byte = c_byte(10)
    TIME: c_byte = c_byte(11)
    DURATION: c_byte = c_byte(12)
    CUBIC: c_byte = c_byte(13)
    ENUM: c_byte = c_byte(14)
    OBJECT: c_byte = c_byte(15)
    TU2D: c_byte = c_byte(16)
    TU3D: c_byte = c_byte(17)
    TU4D: c_byte = c_byte(18)
    TU5D: c_byte = c_byte(19)
    TU6D: c_byte = c_byte(20)
    TU10D: c_byte = c_byte(21)
    TF2D: c_byte = c_byte(22)
    TF3D: c_byte = c_byte(23)
    TF4D: c_byte = c_byte(24)
    BLOCK_REF: c_byte = c_byte(25)
    FUNCTION: c_byte = c_byte(26)
    UNDEFINED: c_byte = c_byte(27)
    STRING_LIT: c_byte = c_byte(28)
    SIZE: c_byte = c_byte(29)


@final
class GreyCat:
    ABI_PROTO: Final[int] = 1

    @final
    class AbiReader:
        def __init__(self, stream: GreyCat.Stream) -> None:
            self.__stream: GreyCat.Stream = stream

        def read(self) -> Any:
            return self.__stream.read()

        def available(self) -> int:
            try:
                pass  # TODO
            except:  # TODO: specific exception
                return 0

    @final
    class AbiWriter:
        def __init__(self, stream: GreyCat.Stream) -> None:
            self.__stream: GreyCat.Stream = stream

        def write(self, object: Any) -> None:
            return self.__stream.write(object)

    def openAbiRead(self, path: str) -> GreyCat.AbiReader:
        pass  # TODO

    def openAbiWrite(self, path: str) -> GreyCat.AbiWriter:
        pass  # TODO

    @final
    class Stream:
        __ASCII_MAX: Final[c_byte] = c_byte(127)

        def __init__(self, greycat: GreyCat, io: BufferedIOBase) -> None:
            self.__tmp = Final[list[c_byte]] = [c_byte(0)] * 8
            self.__io: BufferedIOBase = io
            self.greycat: Final[GreyCat] = greycat

        def read(self) -> Any:
            primitive_offset: c_byte = self.read_i8()
            return GreyCat.Stream.PRIMITIVE_LOADERS[primitive_offset.value](self)

        def read_i8(self) -> c_byte:
            return c_byte(self.__io.read(1)[0])

        def read_i8_array(self, len_: int) -> bytes:
            tmp: bytes = self.__io.read(len_)
            if len(tmp) < len_:
                raise Exception
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

        def read_vu32(self) -> c_uint32:
            pass  # TODO

        def write(self, value: Any) -> None:
            if value is None:
                self.write_i8(PrimitiveType.NULL)
            elif type(value) is bool:
                self.write_i8(PrimitiveType.BOOL)
                self.write_bool(value)
            elif type(value) is c_char:
                c: c_char = value
                self.write_i8(PrimitiveType.CHAR)
                self.write_i8(c_byte(c.value[0]))
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
                symbolOffset: int = self.greycat.__symbols_off_by_value[value]
                if symbolOffset is not None:
                    self.write_i8(PrimitiveType.STRING_LIT)
                    self.write_vu32(c_uint32(symbolOffset << 1 | 1))
                else:
                    self.write_i8(PrimitiveType.OBJECT)
                    self.write_vu32(c_uint32(self.greycat.type_offset_core_string))
                    data = value.encode("utf-8")
                    self.write_vu32(c_uint32(len(data) << 1))
                    self.write_i8_array(data, 0, len(data))
            elif type(value) is GreyCat.Object:
                value.saveType(self)
                value.save(self)

        def write_bool(self, b: bool) -> None:
            self.__io.write(bytes(c_byte(1 if b else 0)))

        def write_i8(self, b: c_byte) -> None:
            self.__io.write(bytes(b))

        def write_i8_array(self, b: bytearray | bytes, offset: int, len_: int) -> None:
            self.__io.write(b[slice(offset, offset + len_)])

        def write_vu32(self, u: c_uint32):
            pass  # TODO

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
            self.__io.write(tmp)

        def write_vi64(self, i: c_int64) -> None:
            self.write_vu64(c_uint64((i.value << 1) ^ (i.value >> 63)))

        def write_vu64(self, u: c_uint64) -> None:
            packed_value: Final[bytearray] = bytearray(9)
            value: int = u.value

            packed_value[0] = c_byte(value & 0x7F).value
            if value < 0x80:
                self.write_i8_array(packed_value, 0, 1)
                return

            packed_value[0] |= 0x80
            value >>= 7
            packed_value[1] = c_byte(value).value
            if value < 0x80:
                self.write_i8_array(packed_value, 0, 2)
                return

            packed_value[1] |= 0x80
            value >>= 7
            packed_value[2] = c_byte(value).value
            if value < 0x80:
                self.write_i8_array(packed_value, 0, 3)
                return

            packed_value[2] |= 0x80
            value >>= 7
            packed_value[3] = c_byte(value).value
            if value < 0x80:
                self.write_i8_array(packed_value, 0, 4)
                return

            packed_value[3] |= 0x80
            value >>= 7
            packed_value[4] = c_byte(value).value
            if value < 0x80:
                self.write_i8_array(packed_value, 0, 5)
                return

            packed_value[4] |= 0x80
            value >>= 7
            packed_value[5] = c_byte(value).value
            if value < 0x80:
                self.write_i8_array(packed_value, 0, 6)
                return

            packed_value[5] |= 0x80
            value >>= 7
            packed_value[6] = c_byte(value).value
            if value < 0x80:
                self.write_i8_array(packed_value, 0, 7)
                return

            packed_value[6] |= 0x80
            value >>= 7
            packed_value[7] = c_byte(value).value
            if value < 0x80:
                self.write_i8_array(packed_value, 0, 8)
                return

            packed_value[7] |= 0x80
            value >>= 7
            packed_value[8] = c_byte(value).value
            self.write_i8_array(packed_value, 0, 9)

        def write_f64(self, d: c_double):
            self.write_i64(c_int64(unpack("q", pack("d", d.value))[0]))

        PrimitiveLoader: Final[type[Callable[[GreyCat.Stream], object]]] = Callable[
            [object], object
        ]

        __null_loader: Final[
            Callable[[GreyCat.Stream], object]
        ] = lambda stream: stream.read_null()
        __bool_loader: Final[
            Callable[[GreyCat.Stream], object]
        ] = lambda stream: stream.read_bool()
        __char_loader: Final[
            Callable[[GreyCat.Stream], object]
        ] = lambda stream: stream.read_char()
        __i64_loader: Final[
            Callable[[GreyCat.Stream], object]
        ] = lambda stream: stream.read_i64()
        __f64_loader: Final[
            Callable[[GreyCat.Stream], object]
        ] = lambda stream: stream.read_f64()

        @staticmethod
        @final
        def __type_loader(stream: GreyCat.Stream, type: GreyCat.Type) -> object:
            return type.loader(type, stream)

        __node_loader: Final[
            Callable[[GreyCat.Stream], object]
        ] = lambda stream: GreyCat.Stream.__type_loader(
            stream, stream.greycat.type_offset_core_node
        )
        __node_time_loader: Final[
            Callable[[GreyCat.Stream], object]
        ] = lambda stream: GreyCat.Stream.__type_loader(
            stream, stream.greycat.type_offset_core_node_time
        )
        __node_index_loader: Final[
            Callable[[GreyCat.Stream], object]
        ] = lambda stream: GreyCat.Stream.__type_loader(
            stream, stream.greycat.type_offset_core_node_index
        )
        __node_list_loader: Final[
            Callable[[GreyCat.Stream], object]
        ] = lambda stream: GreyCat.Stream.__type_loader(
            stream, stream.greycat.type_offset_core_node_list
        )
        __node_geo_loader: Final[
            Callable[[GreyCat.Stream], object]
        ] = lambda stream: GreyCat.Stream.__type_loader(
            stream, stream.greycat.type_offset_core_node_geo
        )
        __geo_loader: Final[
            Callable[[GreyCat.Stream], object]
        ] = lambda stream: GreyCat.Stream.__type_loader(
            stream, stream.greycat.type_offset_core_geo
        )
        __time_loader: Final[
            Callable[[GreyCat.Stream], object]
        ] = lambda stream: GreyCat.Stream.__type_loader(
            stream, stream.greycat.type_offset_core_time
        )
        __duration_loader: Final[
            Callable[[GreyCat.Stream], object]
        ] = lambda stream: GreyCat.Stream.__type_loader(
            stream, stream.greycat.type_offset_core_duration
        )

        __object_loader: Final[
            Callable[[GreyCat.Stream], object]
        ] = lambda stream: stream.read_object()

        __tu2d_loader: Final[
            Callable[[GreyCat.Stream], object]
        ] = lambda stream: GreyCat.Stream.__type_loader(
            stream, stream.greycat.type_offset_core_ti2d
        )

        __tu3d_loader: Final[
            Callable[[GreyCat.Stream], object]
        ] = lambda stream: GreyCat.Stream.__type_loader(
            stream, stream.greycat.type_offset_core_ti3d
        )

        __tu4d_loader: Final[
            Callable[[GreyCat.Stream], object]
        ] = lambda stream: GreyCat.Stream.__type_loader(
            stream, stream.greycat.type_offset_core_ti4d
        )

        __tu5d_loader: Final[
            Callable[[GreyCat.Stream], object]
        ] = lambda stream: GreyCat.Stream.__type_loader(
            stream, stream.greycat.type_offset_core_ti5d
        )

        __tu6d_loader: Final[
            Callable[[GreyCat.Stream], object]
        ] = lambda stream: GreyCat.Stream.__type_loader(
            stream, stream.greycat.type_offset_core_ti6d
        )

        __tu10d_loader: Final[
            Callable[[GreyCat.Stream], object]
        ] = lambda stream: GreyCat.Stream.__type_loader(
            stream, stream.greycat.type_offset_core_ti10d
        )

        __tf2d_loader: Final[
            Callable[[GreyCat.Stream], object]
        ] = lambda stream: GreyCat.Stream.__type_loader(
            stream, stream.greycat.type_offset_core_tf2d
        )

        __tf3d_loader: Final[
            Callable[[GreyCat.Stream], object]
        ] = lambda stream: GreyCat.Stream.__type_loader(
            stream, stream.greycat.type_offset_core_tf3d
        )

        __tf4d_loader: Final[
            Callable[[GreyCat.Stream], object]
        ] = lambda stream: GreyCat.Stream.__type_loader(
            stream, stream.greycat.type_offset_core_tf4d
        )

        @staticmethod
        @final
        def __error_loader(stream: GreyCat.Stream) -> object:
            raise ValueError("invalid primitive type")

        __string_lit_loader: Final[
            Callable[[GreyCat.Stream], object]
        ] = lambda stream: stream.read_string_lit()

        PRIMITIVE_LOADERS: Final[list[PrimitiveLoader]] = [
            None
        ] * PrimitiveType.SIZE.value
        PRIMITIVE_LOADERS[PrimitiveType.NULL.value] = __null_loader
        PRIMITIVE_LOADERS[PrimitiveType.BOOL.value] = __bool_loader
        PRIMITIVE_LOADERS[PrimitiveType.CHAR.value] = __char_loader
        PRIMITIVE_LOADERS[PrimitiveType.INT.value] = __i64_loader
        PRIMITIVE_LOADERS[PrimitiveType.FLOAT.value] = __f64_loader
        PRIMITIVE_LOADERS[PrimitiveType.NODE.value] = __node_loader
        PRIMITIVE_LOADERS[PrimitiveType.NODE_TIME.value] = __node_time_loader
        PRIMITIVE_LOADERS[PrimitiveType.NODE_INDEX.value] = __node_index_loader
        PRIMITIVE_LOADERS[PrimitiveType.NODE_LIST.value] = __node_list_loader
        PRIMITIVE_LOADERS[PrimitiveType.NODE_GEO.value] = __node_geo_loader
        PRIMITIVE_LOADERS[PrimitiveType.GEO.value] = __geo_loader
        PRIMITIVE_LOADERS[PrimitiveType.TIME.value] = __time_loader
        PRIMITIVE_LOADERS[PrimitiveType.DURATION.value] = __duration_loader
        PRIMITIVE_LOADERS[PrimitiveType.ENUM.value] = __object_loader
        PRIMITIVE_LOADERS[PrimitiveType.OBJECT.value] = __object_loader
        PRIMITIVE_LOADERS[PrimitiveType.TU2D.value] = __tu2d_loader
        PRIMITIVE_LOADERS[PrimitiveType.TU3D.value] = __tu3d_loader
        PRIMITIVE_LOADERS[PrimitiveType.TU4D.value] = __tu4d_loader
        PRIMITIVE_LOADERS[PrimitiveType.TU5D.value] = __tu5d_loader
        PRIMITIVE_LOADERS[PrimitiveType.TU6D.value] = __tu6d_loader
        PRIMITIVE_LOADERS[PrimitiveType.TU10D.value] = __tu10d_loader
        PRIMITIVE_LOADERS[PrimitiveType.TF2D.value] = __tf2d_loader
        PRIMITIVE_LOADERS[PrimitiveType.TF3D.value] = __tf3d_loader
        PRIMITIVE_LOADERS[PrimitiveType.TF4D.value] = __tf4d_loader
        PRIMITIVE_LOADERS[PrimitiveType.BLOCK_REF.value] = __error_loader
        PRIMITIVE_LOADERS[PrimitiveType.FUNCTION] = __error_loader  # TODO?
        PRIMITIVE_LOADERS[PrimitiveType.UNDEFINED.value] = __error_loader
        PRIMITIVE_LOADERS[PrimitiveType.STRING_LIT.value] = __string_lit_loader

    Loader: Final[type[Callable[[Type, Stream], Any]]] = Callable[[Type, Stream], Any]

    Factory: Final[type[Callable[[Type, list[Any]], Any]]] = Callable[
        [Type, list[object]], Any
    ]

    class Type:
        class Attribute:
            def __init__(
                self,
                name: str,
                abi_type: int,
                prog_type_offset: int,
                mapped_any_offset: int,
                mapped_att_offset: int,
                sbi_type: c_byte,
                nullable: bool,
                mapped: bool,
            ):
                self.name: Final[str] = name
                self.abi_type: Final[int] = abi_type
                self.prog_type_offset: Final[int] = prog_type_offset
                self.mapped_any_offset: Final[int] = mapped_any_offset
                self.mapped_att_offset: Final[int] = mapped_att_offset
                self.sbi_type: Final[c_byte] = sbi_type
                self.nullable: Final[bool] = nullable
                self.mapped: Final[bool] = mapped

        @staticmethod
        @final
        def __error_loader(type: GreyCat.Type, stream: GreyCat.Stream) -> Any:
            raise ValueError("wrong state")

        @staticmethod
        @final
        def __enum_loader(type: GreyCat.Type, stream: GreyCat.Stream) -> Any:
            program_type: Final[GreyCat.Type] = type.greycat.types[type.mapped_type_off]
            value_offset: Final[int] = stream.read_vu32().value
            abi_type_att: Final[GreyCat.Type.Attribute] = type.attributes[value_offset]
            return program_type.enum_values[abi_type_att.mapped_att_offset]

        @staticmethod
        @final
        def __object_loader(type: GreyCat.Type, stream: GreyCat.Stream) -> Any:
            program_type: Final[GreyCat.Type] = type.greycat.types[type.mapped_type_off]
            attributes: Final[list[Any]] = [None] * len(program_type.attributes)
            nullable_bitset: bytes = stream.read_i8_array(type.nullable_nb_bytes)
            nullable_offset: int = -1
            for att_offset in range(type.attributes):
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
                load_type: c_byte = att.sbi_type
                if load_type == PrimitiveType.UNDEFINED:
                    load_type = stream.read_i8()
                match load_type:
                    case PrimitiveType.ENUM:
                        field_type: GreyCat.Type = type.greycat.types[att.abi_type]
                        loaded_field = GreyCat.Type.__enum_loader(field_type, stream)
                    case PrimitiveType.OBJECT:
                        field_type: GreyCat.Type = type.greycat.types[att.abi_type]
                        if (not field_type.is_native) and (
                            field_type.is_abstract
                            or att.sbi_type == PrimitiveType.UNDEFINED
                        ):
                            field_type = type.greycat.types[stream.read_vu32()]
                        loaded_field = field_type.loader(field_type, stream)
                    case _:
                        loaded_field = GreyCat.Stream.PRIMITIVE_LOADERS[att.sbi_type](
                            stream
                        )
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
            factory: GreyCat.Factory,
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

    class Object:
        def __init__(self, type: GreyCat.Type, attributes: list[Any]) -> None:
            self.type: Final[GreyCat.Type] = type
            self.attributes: list[Any] = attributes

        def saveType(self, stream: GreyCat.Stream) -> None:
            stream.write_i8(PrimitiveType.OBJECT)
            stream.write_vu32(self.type.offset)

        def save(self, stream: GreyCat.Stream) -> None:
            pass  # TODO

    class Enum(Object):
        def __init__(self, type: GreyCat.Type, attributes: list[Any]) -> None:
            super(type, attributes)

    class Library:
        def __init__(self: GreyCat.Library) -> None:
            self.mapped: list[GreyCat.Type] | None = None

        def name(self: GreyCat.Library) -> str:
            raise NotImplementedError

        def configure(
            self: GreyCat.Library,
            loaders: dict[str, GreyCat.Loader],
            factories: dict[str, GreyCat.Factory],
        ) -> None:
            raise NotImplementedError

        def init(self: GreyCat.Library, greycat: GreyCat) -> None:
            raise NotImplementedError

    def __init__(self, *args: GreyCat.Library, url: str) -> None:
        self.libs_by_name: Final[dict[str, GreyCat.Library]] = {}
        std_: std = std()
        self.libs_by_name[std_.name()] = std
        for i in range(len(*args)):
            lib: GreyCat.Library = args[i]
            self.libs_by_name[lib.name()] = lib
        loaders: Final[dict[str, GreyCat.Loader]] = {}
        factories: Final[dict[str, GreyCat.Factory]] = {}
        for _, lib in self.libs_by_name:
            lib.configure(loaders, factories)
        self.runtime_url: Final[str] = url
        abi_stream: Final[GreyCat.Stream] = self.__get_abi(url)

        # step 0: verify abi version
        abi_major: int = abi_stream.read_i16()
        if abi_major != GreyCat.ABI_PROTO:
            raise Exception("wrong ABI proto")
        self.abi_magic: Final[c_int16] = abi_stream.read_i16()
        self.abi_version: Final[c_int32] = abi_stream.read_i32()
        crc: c_int64 = abi_stream.read_i64()

        # step 1: create all symbols
        symbols_bytes: Final[c_int64] = abi_stream.read_i64()
        symbols_count: Final[int] = abi_stream.read_i32().value
        self.symbols: Final[list[str | None]] = [None] * (symbols_count + 1)
        self.symbols_off_by_value: Final[dict[str, int]] = {}
        for offset in range(1, symbols_count + 1):
            symbol: str = abi_stream.read_string(abi_stream.read_vu32())
            self.symbols[offset] = symbol
            self.symbols_off_by_value[symbol] = offset

        # step 2: create all types
        types_bytes: Final[c_int64] = abi_stream.read_i64()
        types_size: Final[int] = abi_stream.read_i32().value
        self.types: Final[list[GreyCat.Type]] = [None] * types_size
        attributes_size: Final[c_int32] = abi_stream.read_i32()
        for i in range(types_size):
            module_name: Final[str] = self.symbols[abi_stream.read_vu32().value]
            type_name: Final[str] = self.symbols[abi_stream.read_vu32().value]
            lib_name: Final[str] = self.symbols[abi_stream.read_vu32().value]
            fqn: Final[
                str
            ] = f'{"" if module_name is None else f"{module_name}::"}{type_name}'
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
            for enum_offset in range(attributes_len):
                name: Final[str] = self.symbols[abi_stream.read_vu32().value]
                att_abi_type: Final[int] = abi_stream.read_vu32().value
                prog_type_offset: Final[int] = abi_stream.read_vu32().value
                mapped_any_offset: Final[int] = abi_stream.read_vu32().value
                mapped_att_offset: Final[int] = abi_stream.read_vu32().value
                sbi_type: Final[c_byte] = abi_stream.read_i8()
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
            abi_type: GreyCat.Type = Type(
                i,
                fqn,
                mapped_abi_type_offset,
                masked_abi_type_offset,
                nullable_nb_bytes,
                is_masked,
                is_abstract,
                is_enum,
                is_native,
                type_attributes,
                factories[fqn],
                loaders[fqn],
                self,
            )
            self.types_by_name: Final[dict[str, GreyCat.Type]] = {}
            if abi_type.mapped_type_off == i and len(fqn) != 0:
                self.types_by_name[abi_type.name, abi_type]
            self.types[i] = abi_type
        # step 3: create all functions
        # TODO

    def __get_abi(self, runtime_url: str) -> GreyCat.Stream:
        if runtime_url.startswith("http"):
            return self.__get_remote_abi(runtime_url)
        else:
            return self.__get_local_abi(runtime_url)

    def __get_remote_abi(self, runtime_url: str) -> GreyCat.Stream:
        pass  # TODO

    def __get_local_abi(self, runtime_url: str) -> GreyCat.Stream:
        pass  # TODO


# class PrimitiveType:
#     NULL: c_byte = c_byte(0)
#     BOOL: c_byte = c_byte(1)
#     CHAR: c_byte = c_byte(2)
#     INT: c_byte = c_byte(3)
#     FLOAT: c_byte = c_byte(4)
#     NODE: c_byte = c_byte(5)
#     NODE_TIME: c_byte = c_byte(6)
#     NODE_INDEX: c_byte = c_byte(7)
#     NODE_LIST: c_byte = c_byte(8)
#     NODE_GEO: c_byte = c_byte(9)
#     GEO: c_byte = c_byte(10)
#     TIME: c_byte = c_byte(11)
#     DURATION: c_byte = c_byte(12)
#     ENUM: c_byte = c_byte(13)
#     OBJECT: c_byte = c_byte(14)
#     BLOCK: c_byte = c_byte(15)
#     BLOCK_REF: c_byte = c_byte(16)
#     FUNCTION_REF: c_byte = c_byte(17)
#     UNDEFINED: c_byte = c_byte(18)
#     STRING_LIT: c_byte = c_byte(19)
#     SIZE: c_byte = c_byte(20)


# class ByteArrayIO(BufferedIOBase):
#     def __init__(self: ByteArrayIO, b: bytearray) -> None:
#         self.__b = b

#     def write(self: ByteArrayIO, __buffer: bytes) -> None:
#         self.__b += bytearray(__buffer)


# class GreyCat:

#     class Stream:
#         def __init__(self: GreyCat.Stream, greycat: GreyCat, io: BufferedIOBase) -> None:
#             self.__io: BufferedIOBase = io
#             self.greycat: GreyCat = greycat

#         def read_i8(self: GreyCat.Stream) -> c_byte:
#             return c_byte(self.__io.read(1)[0])

#         def read_char(self: GreyCat.Stream) -> c_char:
#             return c_char(self.__io.read(1)[0])

#         def read_bool(self: GreyCat.Stream) -> bool:
#             return self.read_i8().value != 0

#         def read_null(self: GreyCat.Stream) -> None:
#             return None

#         def read_i32(self: GreyCat.Stream) -> c_int32:
#             tmp: bytes = self.__io.read(4)
#             if len(tmp) < 4:
#                 raise Exception
#             return c_int32((tmp[3] << 24) + ((tmp[2] << 24) >> 8) + ((tmp[1] << 24) >> 16) + ((tmp[0] << 24) >> 24))

#         def read_i64(self: GreyCat.Stream) -> c_int64:
#             tmp: bytes = self.__io.read(8)
#             if len(tmp) < 8:
#                 raise Exception
#             return c_int64((tmp[7] << 56) + ((tmp[6] << 56) >> 8) + ((tmp[5] << 56) >> 16) + ((tmp[4] << 56) >> 24) + ((tmp[3] << 56) >> 32) + ((tmp[2] << 56) >> 40) + ((tmp[1] << 56) >> 48) + ((tmp[0] << 56) >> 56))

#         def read_i8_array(self: GreyCat.Stream, len_: int) -> bytes:
#             tmp: bytes = self.__io.read(len_)
#             if len(tmp) < len_:
#                 raise Exception
#             return tmp

#         def read_f64(self: GreyCat.Stream) -> c_double:
#             return c_double(unpack('d', pack('q', self.read_i64().value))[0])

#         def read_string(self: GreyCat.Stream, len_: int) -> str:
#             return self.read_i8_array(len_).decode('utf-8')

#         def write_i8(self: GreyCat.Stream, b: c_byte) -> None:
#             self.__io.write(bytes(b))

#         def write_bool(self: GreyCat.Stream, b: bool) -> None:
#             self.__io.write(bytes(c_byte(1 if b else 0)))

#         def write_i8_array(self: GreyCat.Stream, b: bytes, offset: int, len_: int) -> None:
#             self.__io.write(b[slice(offset, offset + len_)])

#         def write_i32(self: GreyCat.Stream, i: c_int32) -> None:
#             i = i.value
#             tmp: bytearray = bytearray(4)
#             tmp[0] = i & 0xFF
#             tmp[1] = (i >> 8) & 0xFF
#             tmp[2] = (i >> 16) & 0xFF
#             tmp[3] = (i >> 24) & 0xFF
#             self.__io.write(tmp)

#         def write_i64(self: GreyCat.Stream, i: c_int64) -> None:
#             i = i.value
#             tmp: bytearray = bytearray(8)
#             tmp[0] = i & 0xFF
#             tmp[1] = (i >> 8) & 0xFF
#             tmp[2] = (i >> 16) & 0xFF
#             tmp[3] = (i >> 24) & 0xFF
#             tmp[4] = (i >> 32) & 0xFF
#             tmp[5] = (i >> 40) & 0xFF
#             tmp[6] = (i >> 48) & 0xFF
#             tmp[7] = (i >> 56) & 0xFF
#             self.__io.write(tmp)

#         def write_f64(self: GreyCat.Stream, f: c_double) -> None:
#             self.write_i64(c_int64(unpack('q', pack('d', f.value))[0]))

#         def write_object(self: GreyCat.Stream, o: object) -> None:
#             if o is None:
#                 self.write_i8(PrimitiveType.NULL)
#             elif type(o) is bool:
#                 self.write_i8(PrimitiveType.BOOL)
#                 self.write_bool(o)
#             elif type(o) is c_char:
#                 c: c_char = o
#                 self.write_i8(PrimitiveType.CHAR)
#                 self.write_i8(c_byte(c.value[0]))
#             elif type(o) is int:
#                 self.write_i8(PrimitiveType.INT)
#                 self.write_i64(c_int64(o))
#             elif type(o) is c_int64:
#                 self.write_i8(PrimitiveType.INT)
#                 self.write_i64(o)
#             elif type(o) is float:
#                 self.write_i8(PrimitiveType.FLOAT)
#                 self.write_f64(c_double(o))
#             elif type(o) is c_double:
#                 self.write_i8(PrimitiveType.FLOAT)
#                 self.write_f64(o)
#             elif type(o) is str:
#                 symbolOffset: int = self.greycat.__symbols_off_by_value[o]
#                 if symbolOffset is not None:
#                     self.write_i8(PrimitiveType.STRING_LIT)
#                     self.write_i32(c_int32(symbolOffset))
#                 else:
#                     self.write_i8(PrimitiveType.OBJECT)
#                     self.write_i32(
#                         c_int32(self.greycat.type_offset_core_string))
#                     self.write_i32(c_int32(len(o)))
#                     data = o.encode('utf-8')
#                     self.write_i8_array(data, 0, len(data))
#             elif type(o) is GreyCat.Object:
#                 o.save(self)
#             else:
#                 raise ValueError('wrong state')

#         def close(self: GreyCat.Stream) -> None:
#             self.__io.close()

#         def read(self: GreyCat.Stream) -> object:
#             return GreyCat.Stream.__PRIMITIVE_LOADERS[self.read_i8().value](self)

#         def read_object(self: GreyCat.Stream) -> object:
#             type: GreyCat.Type = self.greycat.types[self.read_i32().value]
#             return type.loader(type, self)

#         def read_string_lit(self: GreyCat.Stream) -> str:
#             offset: int = self.read_i32().value
#             if (offset < len(self.greycat.__symbols)):
#                 return self.greycat.__symbols[offset]
#             raise ValueError('invalid primitive type')

#         PrimitiveLoader: type[Callable[[GreyCat.Stream],
#                                        object]] = Callable[[object], object]

#         __null_loader: Callable[[GreyCat.Stream],
#                                 object] = lambda stream: stream.read_null()
#         __bool_loader: Callable[[GreyCat.Stream],
#                                 object] = lambda stream: stream.read_bool()
#         __char_loader: Callable[[GreyCat.Stream],
#                                 object] = lambda stream: stream.read_char()
#         __i64_loader: Callable[[GreyCat.Stream],
#                                object] = lambda stream: stream.read_i64()
#         __f64_loader: Callable[[GreyCat.Stream],
#                                object] = lambda stream: stream.read_f64()

#         @staticmethod
#         def __type_loader(stream: GreyCat.Stream, type: GreyCat.Type) -> object:
#             return type.loader(type, stream)

#         __node_loader: Callable[[GreyCat.Stream], object] = lambda stream: GreyCat.Stream.__type_loader(
#             stream, stream.greycat.type_offset_core_node)
#         __node_time_loader: Callable[[GreyCat.Stream], object] = lambda stream: GreyCat. Stream.__type_loader(
#             stream, stream.greycat.type_offset_core_node_time)
#         __node_index_loader: Callable[[GreyCat.Stream], object] = lambda stream: GreyCat.Stream.__type_loader(
#             stream, stream.greycat.type_offset_core_node_index)
#         __node_list_loader: Callable[[GreyCat.Stream], object] = lambda stream: GreyCat.Stream.__type_loader(
#             stream, stream.greycat.type_offset_core_node_list)
#         __node_geo_loader: Callable[[GreyCat.Stream], object] = lambda stream: GreyCat.Stream.__type_loader(
#             stream, stream.greycat.type_offset_core_node_geo)
#         __geo_loader: Callable[[GreyCat.Stream], object] = lambda stream: GreyCat.Stream.__type_loader(
#             stream, stream.greycat.type_offset_core_geo)
#         __time_loader: Callable[[GreyCat.Stream], object] = lambda stream: GreyCat.Stream.__type_loader(
#             stream, stream.greycat.type_offset_core_time)
#         __duration_loader: Callable[[GreyCat.Stream], object] = lambda stream: GreyCat.Stream.__type_loader(
#             stream, stream.greycat.type_offset_core_duration)

#         __object_loader: Callable[[GreyCat.Stream],
#                                   object] = lambda stream: stream.read_object()

#         @staticmethod
#         def __error_loader(stream: GreyCat.Stream) -> object:
#             raise ValueError('invalid primitive type')

#         __string_lit_loader: Callable[[GreyCat.Stream],
#                                       object] = lambda stream: stream.read_string_lit()

#         __PRIMITIVE_LOADERS: list[PrimitiveLoader] = [
#             None] * PrimitiveType.SIZE.value
#         __PRIMITIVE_LOADERS[PrimitiveType.NULL.value] = __null_loader
#         __PRIMITIVE_LOADERS[PrimitiveType.BOOL.value] = __bool_loader
#         __PRIMITIVE_LOADERS[PrimitiveType.CHAR.value] = __char_loader
#         __PRIMITIVE_LOADERS[PrimitiveType.INT.value] = __i64_loader
#         __PRIMITIVE_LOADERS[PrimitiveType.FLOAT.value] = __f64_loader
#         __PRIMITIVE_LOADERS[PrimitiveType.NODE.value] = __node_loader
#         __PRIMITIVE_LOADERS[PrimitiveType.NODE_TIME.value] = __node_time_loader
#         __PRIMITIVE_LOADERS[PrimitiveType.NODE_INDEX.value] = __node_index_loader
#         __PRIMITIVE_LOADERS[PrimitiveType.NODE_LIST.value] = __node_list_loader
#         __PRIMITIVE_LOADERS[PrimitiveType.NODE_GEO.value] = __node_geo_loader
#         __PRIMITIVE_LOADERS[PrimitiveType.GEO.value] = __geo_loader
#         __PRIMITIVE_LOADERS[PrimitiveType.TIME.value] = __time_loader
#         __PRIMITIVE_LOADERS[PrimitiveType.DURATION.value] = __duration_loader
#         __PRIMITIVE_LOADERS[PrimitiveType.ENUM.value] = __object_loader
#         __PRIMITIVE_LOADERS[PrimitiveType.OBJECT.value] = __object_loader
#         __PRIMITIVE_LOADERS[PrimitiveType.BLOCK.value] = __error_loader
#         __PRIMITIVE_LOADERS[PrimitiveType.BLOCK_REF.value] = __error_loader
#         __PRIMITIVE_LOADERS[PrimitiveType.FUNCTION_REF.value] = __error_loader
#         __PRIMITIVE_LOADERS[PrimitiveType.UNDEFINED.value] = __error_loader
#         __PRIMITIVE_LOADERS[PrimitiveType.STRING_LIT.value] = __string_lit_loader

#     Loader = Callable[[Type, Stream], object]

#     Factory = Callable[[Type, list[object]], object]

#     class Type:
#         class Attribute:
#             def __init__(self: GreyCat.Type.Attribute, name: str, typeModuleName: str, typeName: str, progTypeOffset: c_int32, mappedAnyOffset: c_int32, mappedAttOffset: c_int32, sbiType: c_byte, nullable: bool, mapped: bool) -> None:
#                 self.name = name
#                 self.typeModulName = typeModuleName
#                 self.typeName = typeName
#                 self.progTypeOffset = progTypeOffset
#                 self.mappedAnyOffset = mappedAnyOffset
#                 self.mappedAttOffset = mappedAttOffset
#                 self.sbiType = sbiType
#                 self.nullable = nullable
#                 self.mapped = mapped

#         @staticmethod
#         def error_loader(type: GreyCat.Type, stream: GreyCat.Stream) -> object:
#             raise ValueError('wrong state')

#         @staticmethod
#         def enum_loader(type: GreyCat.Type, stream: GreyCat.Stream) -> object:
#             programType: GreyCat.Type = type.greycat.types[type.mapped_type_off.value]
#             valueOffset: c_int32 = stream.read_i32()
#             abiTypeAtt: GreyCat.Type.Attribute = type.attributes[valueOffset.value]
#             return programType.enum_values[abiTypeAtt.mappedAttOffset.value]

#         @staticmethod
#         def object_loader(type: GreyCat.Type, stream: GreyCat.Stream) -> object:
#             programType: GreyCat.Type = type.greycat.types[type.mapped_type_off.value]
#             attributes: list[object] = [None] * len(type.attributes)
#             for attOffset in range(len(type.attributes)):
#                 att: GreyCat.Type.Attribute = type.attributes[attOffset]
#                 loadedField: object = stream.read()
#                 if att.mapped:
#                     attributes[att.mappedAttOffset.value] = loadedField
#             if programType.factory is None:
#                 return GreyCat.Object(programType, attributes)
#             else:
#                 return programType.factory(programType, attributes)

#         def __init__(self: GreyCat.Type, offset: c_int32, name: str, mapped_type_off: c_int32, masked_type_off: c_int32, is_masked: bool, is_enum: bool, is_native: bool, typeAttributes: list[Attribute], loader: GreyCat.Loader, factory: GreyCat.Factory, greycat: GreyCat) -> None:
#             self.offset = offset
#             self.name = name
#             self.mapped_type_off = mapped_type_off
#             self.masked_type_off = masked_type_off
#             self.is_masked = is_masked
#             self.is_enum = is_enum
#             self.is_native = is_native
#             self.attributes = typeAttributes
#             self.attribute_off_by_name = dict()
#             for off in range(len(self.attributes)):
#                 self.attribute_off_by_name[self.attributes[off].name] = off
#             self.greycat = greycat
#             self.factory = factory
#             if self.offset == self.mapped_type_off:
#                 if self.is_enum:
#                     self.enum_values: list[GreyCat.Enum] = []
#                     for enumOffset in range(len(self.attributes)):
#                         attributes: list[object] = list(
#                             enumOffset, self.attributes[enumOffset, None])
#                         if self.factory is None:
#                             self.enum_values[enumOffset] = GreyCat.Enum(
#                                 self, attributes)
#                         else:
#                             self.enum_values[enumOffset] = self.factory(
#                                 self, attributes)
#                 else:
#                     self.enum_values = None
#             else:
#                 self.enum_values = None
#             if loader is not None:
#                 self.loader = loader
#             elif self.is_native:
#                 self.loader = GreyCat.Type.error_loader
#             elif self.is_enum:
#                 self.loader = GreyCat.Type.enum_loader
#             else:
#                 self.loader = GreyCat.Type.object_loader

#     class Object:
#         def __init__(self: GreyCat.Object, type: GreyCat.Type, attributes: list[object] | None) -> None:
#             self.type = type
#             self.attributes = attributes

#         def get(self: GreyCat.Object, attributeName: str) -> object:
#             return self.attributes[self.type.attribute_off_by_name[attributeName]]

#         def set(self: GreyCat.Object, attributeName: str, value: object) -> None:
#             self.attributes[self.type.attribute_off_by_name[attributeName]] = value

#         def save(self: GreyCat.Object, stream: GreyCat.Stream) -> None:
#             stream.write_i8(PrimitiveType.OBJECT)
#             stream.write_i32(self.type.offset)
#             if self.attributes is not None:
#                 for offset in range(len(self.attributes)):
#                     stream.write_object(self.attributes[offset])

#         def __str__(self: GreyCat.Object) -> str:
#             res = f'{self.type.name}{{'
#             for offset in range(len(self.type.attributes)):
#                 if offset > 0:
#                     res = f'{res},'
#                 res = f'{res}{self.type.attributes[offset].name}={self.attributes[offset]}'
#             res = f'{res}}}'
#             return res

#     class Enum(Object):
#         def __init__(self: GreyCat.Enum, type: GreyCat.Type, attributes: list[object]) -> None:
#             super(type, None)
#             self.__offset: int = attributes[0]
#             self.key: str = attributes[1]
#             self.value: object = attributes[2]

#         def save(self: GreyCat.Enum, stream: GreyCat.Stream) -> None:
#             stream.write_i8(PrimitiveType.ENUM)
#             stream.write_i32(self.type.offset)
#             stream.write_i32(self.__offset)

#     class Library:
#         def __init__(self: GreyCat.Library) -> None:
#             self.mapped: list[GreyCat.Type] = []

#         def name(self: GreyCat.Library) -> str:
#             raise NotImplementedError

#         def configure(self: GreyCat.Library, loaders: dict[str, GreyCat.Loader], factories: dict[str, GreyCat.Factory]) -> None:
#             raise NotImplementedError

#         def init(self: GreyCat.Library, greycat: GreyCat) -> None:
#             raise NotImplementedError

#     def __init__(self: GreyCat, url: str, *libraries: GreyCat.Library) -> None:
#         loaders = dict()
#         factories = dict()
#         if 0 == len(libraries):
#             pass
#             # libraries = (std_n()) # TODO
#         self.libs_by_name: dict[str, GreyCat.Library] = dict()
#         for lib in libraries:
#             lib.configure(loaders, factories)
#             self.libs_by_name[lib.name()] = lib
#         self.__runtime_url = url
#         abiStream: GreyCat.Stream = self.getRemoteAbi()
#         symbolsCount: int = abiStream.read_i32().value
#         self.__symbols: str = [None] * (1 + symbolsCount)
#         self.__symbols_off_by_value = dict()
#         self.__symbols[0] = None
#         for offset in range(1, 1 + symbolsCount):
#             symbol: str = abiStream.read_string(abiStream.read_i32().value)
#             self.__symbols[offset] = symbol
#             self.__symbols_off_by_value[symbol] = offset
#         typeSize: c_int32 = abiStream.read_i32()
#         self.types: list[GreyCat.Type] = [None] * typeSize.value
#         self.types_by_name: dict[str, GreyCat.Type] = dict()
#         for i in range(typeSize.value):
#             moduleName: str = self.__symbols[abiStream.read_i32().value]
#             typeName: str = self.__symbols[abiStream.read_i32().value]
#             if moduleName is None:
#                 fqn = ''
#             else:
#                 fqn = f'{moduleName}.{typeName}'
#             attributesLen: int = abiStream.read_i32().value
#             abiStream.read_i32()  # unused field
#             abiStream.read_i32()  # unused field
#             mappedAbiTypeOffset: c_int32 = abiStream.read_i32()
#             maskedAbiTypeOffset: c_int32 = abiStream.read_i32()
#             isNative: bool = abiStream.read_bool()
#             isEnum: bool = abiStream.read_bool()
#             isMasked: bool = abiStream.read_bool()
#             typeAttributes: list[GreyCat.Type.Attribute] = [
#                 None] * attributesLen
#             for enumOffset in range(attributesLen):
#                 name: str = self.__symbols[abiStream.read_i32().value]
#                 typeModuleName: str = self.__symbols[abiStream.read_i32(
#                 ).value]
#                 attributeTypeName: str = self.__symbols[abiStream.read_i32(
#                 ).value]
#                 progTypeOffset: c_int32 = abiStream.read_i32()
#                 mappedAnyOffset: c_int32 = abiStream.read_i32()
#                 mappedAttOffset: c_int32 = abiStream.read_i32()
#                 sbiType: c_byte = abiStream.read_i8()
#                 nullable: bool = abiStream.read_bool()
#                 mapped: bool = abiStream.read_bool()
#                 typeAttributes[enumOffset] = GreyCat.Type.Attribute(name, typeModuleName, attributeTypeName, progTypeOffset, mappedAnyOffset, mappedAttOffset,
#                                                                     sbiType, nullable, mapped)
#             abiType = GreyCat.Type(c_int32(i), fqn, mappedAbiTypeOffset, maskedAbiTypeOffset, isMasked, isEnum, isNative, typeAttributes, factories.get(fqn, None), loaders.get(fqn, None),
#                                    self)
#             # only the program-related ABI type (last version) is mapped to itself
#             if abiType.mapped_type_off.value == i and len(fqn) != 0:
#                 self.types_by_name[abiType.name] = abiType
#             self.types[i] = abiType
#         type_core_string = self.types_by_name.get('core.String', None)
#         type_core_duration = self.types_by_name.get('core.duration', None)
#         type_core_time = self.types_by_name.get('core.time', None)
#         type_core_geo = self.types_by_name.get('core.geo', None)
#         type_core_node_list = self.types_by_name.get('core.nodeList', None)
#         type_core_node_index = self.types_by_name.get('core.nodeIndex', None)
#         type_core_node_time = self.types_by_name.get('core.nodeTime', None)
#         type_core_node_geo = self.types_by_name.get('core.nodeGeo', None)
#         type_core_node = self.types_by_name.get('core.node', None)
#         if None in [
#             type_core_string,
#             type_core_duration,
#             type_core_time,
#             type_core_geo,
#             type_core_node_list,
#             type_core_node_index,
#             type_core_node_time,
#             type_core_node_geo,
#             type_core_node,
#         ]:
#             raise ValueError('wrong state')
#         self.type_offset_core_string = type_core_string.offset
#         self.type_offset_core_duration = type_core_duration.offset
#         self.type_offset_core_time = type_core_time.offset
#         self.type_offset_core_geo = type_core_geo.offset
#         self.type_offset_core_node_list = type_core_node_list.offset
#         self.type_offset_core_node_index = type_core_node_index.offset
#         self.type_offset_core_node_time = type_core_node_time.offset
#         self.type_offset_core_node_geo = type_core_node_geo.offset
#         self.type_offset_core_node = type_core_node.offset
#         abiStream.close()
#         for i in range(len(libraries)):
#             libraries[i].init(self)

#     @staticmethod
#     def call(greycat: GreyCat, fqn: str, parameters: list[object]) -> object:
#         connection: http.client.HTTPConnection | http.client.HTTPSConnection
#         if greycat.__runtime_url.startswith('http://'):
#             connection = http.client.HTTPConnection(
#                 greycat.__runtime_url.replace('http://', ''))
#         elif greycat.__runtime_url.startswith('https://'):
#             connection = http.client.HTTPSConnection(
#                 greycat.__runtime_url.replace('https://', ''))
#         else:
#             raise ValueError
#         body: bytes | None = None
#         if len(parameters) > 0:
#             b = bytearray()
#             stream = GreyCat.Stream(greycat, ByteArrayIO(b))
#             for offset in range(len(parameters)):
#                 stream.write_object(parameters[offset])
#             stream.close()
#             body = bytes(b)
#         connection.request('POST', fqn.replace(
#             '.', '/'), body, {'Accept': 'application/octet-stream', 'Content-Type': 'application/octet-stream'})
#         response: http.client.HTTPResponse = connection.getresponse()
#         status: int = response.status
#         stream = GreyCat.Stream(greycat, response)
#         if 200 > status or 300 <= status:
#             raise RuntimeError(str(stream.read()))
#         res = stream.read()
#         if len(response.read(1)) > 0:
#             raise IOError('Remaining unread bytes')
#         stream.close()
#         return res

#     def getRemoteAbi(self: GreyCat) -> GreyCat.Stream:
#         connection: http.client.HTTPConnection | http.client.HTTPSConnection
#         if self.__runtime_url.startswith('http://'):
#             connection: http.client.HTTPConnection = http.client.HTTPConnection(
#                 self.__runtime_url.replace('http://', ''))
#         elif self.__runtime_url.startswith('https://'):
#             connection: http.client.HTTPSConnection = http.client.HTTPSConnection(
#                 self.__runtime_url.replace('https://', ''))
#         else:
#             raise ValueError
#         connection.request('POST', 'runtime/Runtime/abi',
#                            None, {'Accept': 'application/octet-stream'})
#         response: http.client.HTTPResponse = connection.getresponse()
#         status: int = response.status
#         if 200 > status or 300 <= status:
#             msg = ''
#             line: str = response.readline()
#             while line is not None:
#                 msg = f'{msg}{line}\n'
#                 line = response.readline()
#             raise RuntimeError(msg)
#         return GreyCat.Stream(self, response)
