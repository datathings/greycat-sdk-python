from __future__ import annotations

from ctypes import *
from io import *
from struct import pack, unpack
from typing import *


class GreyCat:
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
        ENUM: c_byte = c_byte(13)
        OBJECT: c_byte = c_byte(14)
        BLOCK: c_byte = c_byte(15)
        BLOCK_REF: c_byte = c_byte(16)
        FUNCTION_REF: c_byte = c_byte(17)
        UNDEFINED: c_byte = c_byte(18)
        STRING_LIT: c_byte = c_byte(19)
        SIZE: c_byte = c_byte(20)

    class Stream:
        def __init__(self, greycat: GreyCat, io: BufferedIOBase):
            self.__io: BufferedIOBase = io
            self.greycat: GreyCat = greycat

        def read_i8(self) -> c_byte:
            return c_byte(self.__io.read(1))

        def read_char(self) -> c_char:
            return c_char(self.__io.read(1))

        def read_bool(self) -> bool:
            return self.read_i8() != c_byte(0)

        def read_null(self) -> None:  # TODO: check return type
            return None

        def read_i32(self) -> c_int32:
            tmp: bytes = self.__io.read(4)
            if len(tmp) < 4:
                raise Exception
            return c_int32((tmp[3] << 24) + ((tmp[2] << 24) >> 8) + ((tmp[1] << 24) >> 16) + ((tmp[0] << 24) >> 24))

        def read_i64(self) -> c_int64:
            tmp: bytes = self.__io.read(8)
            if len(tmp) < 8:
                raise Exception
            return c_int64((tmp[7] << 56) + ((tmp[6] << 56) >> 8) + ((tmp[5] << 56) >> 16) + ((tmp[4] << 56) >> 24) + ((tmp[3] << 56) >> 32) + ((tmp[2] << 56) >> 40) + ((tmp[1] << 56) >> 48) + ((tmp[0] << 56) >> 56))

        def read_i8_array(self, len_: int) -> bytes:
            tmp: bytes = self.__io.read(len_)
            if len(tmp) < len_:
                raise Exception
            return tmp

        def read_f64(self) -> c_double:
            return c_double(unpack('d', pack('q', self.read_i64().value)))

        def read_string(self, len_: int) -> str:
            return self.read_i8_array(len_).decode('utf-8')

        def write_i8(self, b: c_byte) -> None:
            self.__io.write(bytes(b))

        def write_bool(self, b: bool) -> None:
            self.__io.write(bytes(c_byte(1 if b else 0)))

        def write_i8_array(self, b: bytes, offset: int, len_: int) -> None:
            self.__io.write(b[slice(offset, offset + len_)])

        def write_i32(self, i: c_int32) -> None:
            i = i.value
            tmp: bytearray = bytearray(4)
            tmp[0] = i & 0xFF
            tmp[1] = (i >> 8) & 0xFF
            tmp[2] = (i >> 16) & 0xFF
            tmp[3] = (i >> 24) & 0xFF
            self.__io.write(tmp)

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

        def write_f64(self, f: c_double) -> None:
            self.write_i64(c_int64(unpack('q', pack('d', c_double.value))))

        def close(self) -> None:
            self.__io.close()

        def read(self) -> object:
            return GreyCat.Stream.__PRIMITIVE_LOADERS[self.read_i8().value](self)

        def read_object(self) -> object:
            type: GreyCat.Type = self.greycat.types[self.read_i32().value]
            return type.loader(type, self)

        def read_string_lit(self) -> str:
            offset: int = self.read_i32().value
            if (offset < len(self.greycat.__symbols)):
                return self.greycat.__symbols[offset]
            raise ValueError('invalid primitive type')

        PrimitiveLoader: type[Callable[[GreyCat.Stream],
                                       object]] = Callable[[object], object]

        __null_loader: Callable[[GreyCat.Stream],
                                object] = lambda stream: stream.read_null()
        __bool_loader: Callable[[GreyCat.Stream],
                                object] = lambda stream: stream.read_bool()
        __char_loader: Callable[[GreyCat.Stream],
                                object] = lambda stream: stream.read_char()
        __i64_loader: Callable[[GreyCat.Stream],
                               object] = lambda stream: stream.read_i64()
        __f64_loader: Callable[[GreyCat.Stream],
                               object] = lambda stream: stream.read_f64()

        @staticmethod
        def __type_loader(stream: GreyCat.Stream, type: GreyCat.Type) -> object:
            return type.loader(type, stream)

        __node_loader: Callable[[GreyCat.Stream], object] = lambda stream: GreyCat.Stream.__type_loader(
            stream, stream.greycat.type_offset_core_node)
        __node_time_loader: Callable[[GreyCat.Stream], object] = lambda stream: GreyCat. Stream.__type_loader(
            stream, stream.greycat.type_offset_core_node_time)
        __node_index_loader: Callable[[GreyCat.Stream], object] = lambda stream: GreyCat.Stream.__type_loader(
            stream, stream.greycat.type_offset_core_node_index)
        __node_list_loader: Callable[[GreyCat.Stream], object] = lambda stream: GreyCat.Stream.__type_loader(
            stream, stream.greycat.type_offset_core_node_list)
        __node_geo_loader: Callable[[GreyCat.Stream], object] = lambda stream: GreyCat.Stream.__type_loader(
            stream, stream.greycat.type_offset_core_node_geo)
        __geo_loader: Callable[[GreyCat.Stream], object] = lambda stream: GreyCat.Stream.__type_loader(
            stream, stream.greycat.type_offset_core_geo)
        __time_loader: Callable[[GreyCat.Stream], object] = lambda stream: GreyCat.Stream.__type_loader(
            stream, stream.greycat.type_offset_core_time)
        __duration_loader: Callable[[GreyCat.Stream], object] = lambda stream: GreyCat.Stream.__type_loader(
            stream, stream.greycat.type_offset_core_duration)

        __object_loader: Callable[[GreyCat.Stream],
                                  object] = lambda stream: stream.read_object()

        @staticmethod
        def __error_loader(stream: GreyCat.Stream) -> object:
            raise ValueError('invalid primitive type')

        __string_lit_loader: Callable[[GreyCat.Stream],
                                      object] = lambda stream: stream.read_string_lit()

        __PRIMITIVE_LOADERS: list[PrimitiveLoader] = []
        __PrimitiveType: type[GreyCat.PrimitiveType] = object
        __PRIMITIVE_LOADERS[__PrimitiveType.NULL] = __null_loader
        __PRIMITIVE_LOADERS[__PrimitiveType.BOOL] = __bool_loader
        __PRIMITIVE_LOADERS[__PrimitiveType.CHAR] = __char_loader
        __PRIMITIVE_LOADERS[__PrimitiveType.INT] = __i64_loader
        __PRIMITIVE_LOADERS[__PrimitiveType.FLOAT] = __f64_loader
        __PRIMITIVE_LOADERS[__PrimitiveType.NODE] = __node_loader
        __PRIMITIVE_LOADERS[__PrimitiveType.NODE_TIME] = __node_time_loader
        __PRIMITIVE_LOADERS[__PrimitiveType.NODE_INDEX] = __node_index_loader
        __PRIMITIVE_LOADERS[__PrimitiveType.NODE_LIST] = __node_list_loader
        __PRIMITIVE_LOADERS[__PrimitiveType.NODE_GEO] = __node_geo_loader
        __PRIMITIVE_LOADERS[__PrimitiveType.GEO] = __geo_loader
        __PRIMITIVE_LOADERS[__PrimitiveType.TIME] = __time_loader
        __PRIMITIVE_LOADERS[__PrimitiveType.DURATION] = __duration_loader
        __PRIMITIVE_LOADERS[__PrimitiveType.ENUM] = __object_loader
        __PRIMITIVE_LOADERS[__PrimitiveType.OBJECT] = __object_loader
        __PRIMITIVE_LOADERS[__PrimitiveType.BLOCK] = __error_loader
        __PRIMITIVE_LOADERS[__PrimitiveType.BLOCK_REF] = __error_loader
        __PRIMITIVE_LOADERS[__PrimitiveType.FUNCTION_REF] = __error_loader
        __PRIMITIVE_LOADERS[__PrimitiveType.UNDEFINED] = __error_loader
        __PRIMITIVE_LOADERS[__PrimitiveType.STRING_LIT] = __string_lit_loader

    Loader = Callable[[Type, Stream], object]

    Factory = Callable[[Type, list[object]], object]

    class Type:
        class Attribute:
            def __init__(self, name: str, typeModuleName: str, typeName: str, progTypeOffset: c_int32, mappedAnyOffset: c_int32, mappedAttOffset: c_int32, sbiType: c_byte, nullable: bool, mapped: bool):
                self.name = name
                self.typeModulName = typeModuleName
                self.typeName = typeName
                self.progTypeOffset = progTypeOffset
                self.mappedAnyOffset = mappedAnyOffset
                self.mappedAttOffset = mappedAttOffset
                self.sbiType = sbiType
                self.nullable = nullable
                self.mapped = mapped

        @staticmethod
        def error_loader(type: GreyCat.Type, stream: GreyCat.Stream) -> object:
            raise ValueError('wrong state')

        @staticmethod
        def enum_loader(type: GreyCat.Type, stream: GreyCat.Stream) -> object:
            programType: GreyCat.Type = type.greycat.types[type.mapped_type_off]
            valueOffset: c_int32 = stream.read_i32()
            abiTypeAtt: GreyCat.Type.Attribute = type.attributes[valueOffset]
            return programType.enum_values[abiTypeAtt.mappedAttOffset]

        @staticmethod
        def object_loader(type: GreyCat.Type, stream: GreyCat.Stream) -> object:
            programType: GreyCat.Type = type.greycat.types[type.mapped_type_off]
            attributes: list[object] = []
            for attOffset in range(len(type.attributes)):
                att: GreyCat.Type.Attribute = type.attributes[attOffset]
                loadedField: object = stream.read()
                if att.mapped:
                    attributes[att.mappedAttOffset] = loadedField
            if programType.factory is None:
                return GreyCat.Object(programType, attributes)
            else:
                return programType.factory(programType, attributes)

        def __init__(self, offset: c_int32, name: str, mapped_type_off: c_int32, masked_type_off: c_int32, is_masked: bool, is_enum: bool, is_native: bool, typeAttributes: list[Attribute], loader: GreyCat.Loader, factory: GreyCat.Factory, greycat: GreyCat):
            self.offset = offset
            self.name = name
            self.mapped_type_off = mapped_type_off
            self.masked_type_off = masked_type_off
            self.is_masked = is_masked
            self.is_enum = is_enum
            self.is_native = is_native
            self.attributes = typeAttributes
            self.attribute_off_by_name = dict()
            for off in range(len(self.attributes)):
                self.attribute_off_by_name[self.attributes[off].name, off]
            self.greycat = greycat
            self.factory = factory
            if self.offset == self.mapped_type_off:
                if self.is_enum:
                    self.enum_values: list[GreyCat.Enum] = []
                    for enumOffset in range(len(self.attributes)):
                        attributes: list[object] = list(
                            enumOffset, self.attributes[enumOffset, None])
                        if self.factory is None:
                            self.enum_values[enumOffset] = GreyCat.Enum(
                                self, attributes)
                        else:
                            self.enum_values[enumOffset] = self.factory(
                                self, attributes)
                else:
                    self.enum_values = None
            else:
                self.enum_values = None
            if loader is not None:
                self.loader = loader
            elif self.is_native:
                self.loader = GreyCat.Type.error_loader
            elif self.is_enum:
                self.loader = GreyCat.Type.enum_loader
            else:
                self.loader = GreyCat.Type.object_loader

    class Object:
        def __init__(self, type: GreyCat.Type, attributes: list[object]):
            self.type = type
            self.attributes = attributes

        def get(self, attributeName: str) -> object:
            return self.attributes[self.type.attribute_off_by_name[attributeName]]

        def set(self, attributeName: str, value: object) -> None:
            self.attributes[self.type.attribute_off_by_name[attributeName]] = value

        # TODO

    class Enum(Object):
        def __init__(self, type: GreyCat.Type, attributes: list[object]):
            super(type, None)
            self.__offset: int = attributes[0]
            self.key: str = attributes[1]
            self.value: object = attributes[2]

        def save(self, stream: GreyCat.Stream) -> None:
            stream.write_i8(GreyCat.PrimitiveType.ENUM)
            stream.write_i32(self.type.offset)
            stream.write_i32(self.__offset)

        # TODO

    class Library:
        def __init__(self):
            self.mapped: list[GreyCat.Type] = []

        def name(self) -> str:
            raise NotImplementedError

        def configure(self, loaders: dict[str, GreyCat.Loader], factories: dict[str, GreyCat.Factory]) -> None:
            raise NotImplementedError

        def init(self, greycat: GreyCat) -> None:
            raise NotImplementedError

    def __init__(self, url: str, *libraries: GreyCat.Library):
        loaders = dict()
        factories = dict()
        if 0 == len(libraries):
            libraries = (std_n())
        self.libs_by_name: dict[str, GreyCat.Library] = dict()
        for lib in libraries:
            lib.configure(loaders, factories)
            self.libs_by_name[lib.name()] = lib
        self.__runtime_url = url
        abiStream: GreyCat.Stream = GreyCat.getRemoteAbi()
        symbolsCount: c_int32 = abiStream.read_i32()
        self.__symbols: str = []
        self.__symbols_off_by_value = dict()
        self.__symbols[0] = None
        for offset in range(1, 1 + symbolsCount.value):
            symbol: str = abiStream.read_string(abiStream.read_i32().value)
            self.__symbols[offset] = symbol
            self.__symbols_off_by_value[symbol] = offset
        typeSize: c_int32 = abiStream.read_i32()
        self.types: list[GreyCat.Type] = []
        self.types_by_name: dict[str, GreyCat.Type] = dict()
        for i in range(typeSize.value):
            moduleName: str = self.__symbols[abiStream.read_i32().value]
            typeName: str = self.__symbols[abiStream.read_i32().value]
            if moduleName is None:
                fqn = ''
            else:
                fqn = f'{moduleName}.{typeName}'
            attributesLen: c_int32 = abiStream.read_i32()
            abiStream.read_i32()  # unused field
            abiStream.read_i32()  # unused field
            mappedAbiTypeOffset: c_int32 = abiStream.read_i32()
            maskedAbiTypeOffset: c_int32 = abiStream.read_i32()
            isNative: bool = abiStream.read_bool()
            isEnum: bool = abiStream.read_bool()
            isMasked: bool = abiStream.read_bool()
            typeAttributes: list[GreyCat.Type.Attribute] = []
            for enumOffset in range(attributesLen):
                name: str = self.__symbols[abiStream.read_i32().value]
                typeModuleName: str = self.__symbols[abiStream.read_i32(
                ).value]
                attributeTypeName: str = self.__symbols[abiStream.read_i32(
                ).value]
                progTypeOffset: c_int32 = abiStream.read_i32()
                mappedAnyOffset: c_int32 = abiStream.read_i32()
                mappedAttOffset: c_int32 = abiStream.read_i32()
                sbiType: c_byte = abiStream.read_i8()
                nullable: bool = abiStream.read_bool()
                mapped: bool = abiStream.read_bool()
                typeAttributes[enumOffset] = GreyCat.Type.Attribute(name, typeModuleName, attributeTypeName, progTypeOffset, mappedAnyOffset, mappedAttOffset,
                                                                    sbiType, nullable, mapped)
            abiType = GreyCat.Type(i, fqn, mappedAbiTypeOffset, maskedAbiTypeOffset, isMasked, isEnum, isNative, typeAttributes, factories[fqn], loaders[fqn],
                                   self)
            # only the program-related ABI type (last version) is mapped to itself
            if abiType.mapped_type_off == i and len(fqn) != 0:
                self.types_by_name[abiType.name, abiType]
            self.types[i] = abiType
        type_core_string = self.types_by_name['core.String']
        type_core_duration = self.types_by_name['core.duration']
        type_core_time = self.types_by_name['core.time']
        type_core_geo = self.types_by_name['core.geo']
        type_core_node_list = self.types_by_name['core.nodeList']
        type_core_node_index = self.types_by_name['core.nodeIndex']
        type_core_node_time = self.types_by_name['core.nodeTime']
        type_core_node_geo = self.types_by_name['core.nodeGeo']
        type_core_node = self.types_by_name['core.node']
        if None in [
            type_core_string,
            type_core_duration,
            type_core_time,
            type_core_geo,
            type_core_node_list,
            type_core_node_index,
            type_core_node_time,
            type_core_node_geo,
            type_core_node,
        ]:
            raise ValueError('wrong state')
        self.type_offset_core_string = type_core_string.offset
        self.type_offset_core_duration = type_core_duration.offset
        self.type_offset_core_time = type_core_time.offset
        self.type_offset_core_geo = type_core_geo.offset
        self.type_offset_core_node_list = type_core_node_list.offset
        self.type_offset_core_node_index = type_core_node_index.offset
        self.type_offset_core_node_time = type_core_node_time.offset
        self.type_offset_core_node_geo = type_core_node_geo.offset
        self.type_offset_core_node = type_core_node.offset
        abiStream.close()
        for i in range(len(libraries)):
            libraries[i].init(self)

    def getRemoteAbi(self) -> GreyCat.Stream:
        pass  # TODO
