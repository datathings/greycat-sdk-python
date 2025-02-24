from __future__ import annotations

import base64
from ctypes import *
import hashlib
import http.client
from io import *
from itertools import repeat
import json
import os
import socket
from struct import pack, unpack
from typing import *
import greycat


class GreyCatServer:
    _exposed: dict[str, Callable[..., Any]]

    def __init__(self, abi_path: str, port: int):
        self.abi_path: str = abi_path
        self.port: int = port

    def run(self):
        gc = GreyCat(self.abi_path)
        srv_sock: socket.socket = socket.create_server(
            ("localhost", self.port))
        cli_sock: socket.socket
        stream: GreyCat._Stream
        endpoint: str
        type_name: str
        while True:
            cli_sock = srv_sock.accept()
            stream = GreyCat._Stream(gc, socket.SocketIO(cli_sock, "rwb"))
            stream.read_abi_header()
            endpoint = f"{gc.symbols[stream.read_vu32()]}::"  # module name
            type_name = gc.symbols[stream.read_vu32()]
            if type_name is not None:
                endpoint += f"{type_name}::"
            endpoint += gc.symbols[stream.read_vu32()]  # function name
            params: greycat.std.core.Array = stream.read()
            stream.write_abi_header()
            stream.write(GreyCatServer._exposed[endpoint](*params))


@final
class GreyCatNative:
    _gc: GreyCat | None = None

    def __init__(self):
        raise Exception("Static class")

    @staticmethod
    def _init():
        GreyCatNative._gc = GreyCat(os.getenv("GC_PY_PROJECT_HOME", "."))

    @staticmethod
    def _call(mvin: memoryview) -> memoryview:
        if GreyCatNative._gc is None:
            GreyCatNative._init()
        sin: GreyCat._Stream
        fqn: str
        type_name: str | None
        f: GreyCat.Function
        params: list
        with GreyCat._Stream(GreyCatNative._gc, BytesIO(mvin.obj)) as sin:
            fqn = GreyCatNative._gc.symbols[sin.read_vu32()]
            type_name = GreyCatNative._gc.symbols[sin.read_vu32()]
            if type_name is not None:
                fqn += f"::{type_name}"
            fqn += f"::{GreyCatNative._gc.symbols[sin.read_vu32()]}"
            f = GreyCatNative._gc.functions_by_name[fqn]
            params = list(repeat(None, sin.read_i64()))
            for offset in len(params):
                params[offset] = sin.read()
        out: BytesIO
        sout: GreyCat._Stream
        with BytesIO() as out:
            with GreyCat._Stream(GreyCatNative._gc, out) as sout:
                sout.write(f(*params))
                return out.getbuffer()


def expose(f_name: str) -> Callable[[Callable[..., Any]], None]:
    def decorator(f: Callable[..., Any]) -> None:
        # GreyCatServer
        GreyCatServer._exposed[f_name] = f
        # GreyCatNative
        if GreyCatNative._gc is None:
            GreyCatNative._init()
        gcf: GreyCat.Function = GreyCatNative._gc.functions_by_name[f_name]
        if gcf is None:
            raise Exception(f"Unknown function name: {f_name}")
        gcf.f = f
    return decorator


@final
class PrimitiveType:
    NULL: int = 0
    BOOL: int = 1
    CHAR: int = 2
    INT: int = 3
    FLOAT: int = 4
    NODE: int = 5
    NODE_TIME: int = 6
    NODE_INDEX: int = 7
    NODE_LIST: int = 8
    NODE_GEO: int = 9
    GEO: int = 10
    TIME: int = 11
    DURATION: int = 12
    CUBIC: int = 13
    STATIC_FIELD: int = 14
    OBJECT: int = 15
    T2: int = 16
    T3: int = 17
    T4: int = 18
    STR: int = 19
    T2F: int = 20
    T3F: int = 21
    T4F: int = 22
    BLOCK_REF: int = 23
    FUNCTION: int = 24
    UNDEFINED: int = 25
    TYPE: int = 26
    FIELD: int = 27
    STRING_LIT: int = 28
    SIZE: int = 29


class ByteArrayIO(BufferedIOBase):
    def __init__(self: ByteArrayIO, b: bytearray) -> None:
        self.__b = b

    def write(self: ByteArrayIO, __buffer: bytes) -> None:
        self.__b += bytearray(__buffer)


@final
class GreyCat:
    ABI_PROTO: Final[int] = 2

    @final
    class SocketServer:
        __ip: str = '127.0.0.1'

        def __init__(self: GreyCat.SocketServer, greycat: GreyCat, port_path: str = "gcdata/python-server") -> None:
            sock: socket.socket
            port: int
            for port in range(49_152, 65_536):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                if 0 != sock.connect_ex((GreyCat.SocketServer.__ip, port)):
                    sock.close()
                    break
                sock.close()
            self.__port: Final[int] = port
            self.__sock: Final[socket.socket] = socket.socket(
                socket.AF_INET, socket.SOCK_STREAM)
            self.__sock.bind((GreyCat.SocketServer.__ip, port))
            self.__greycat = greycat
            self.__endpoints: dict[str, Callable[[list[Any]], Any]] = {}
            self.__port_path = port_path

        def register(self, endpoint: str, callback: Callable[..., Any]) -> None:
            self.__endpoints[endpoint] = callback

        def serve(self) -> Never:
            conn: socket.socket
            stream: GreyCat._Stream
            endpoint: str
            parameters: List[Any]
            res: Any
            self.__sock.listen()  # TODO: set backlog?
            with open(self.__port_path, "w") as out:
                out.write(
                    f"{os.getpid()},{int.from_bytes(socket.inet_aton(socket.gethostbyname(GreyCat.SocketServer.__ip)))},{self.__port}")
            print(f"Serving at {GreyCat.SocketServer.__ip}:{self.__port}…")
            while True:
                conn, _ = self.__sock.accept()
                stream = GreyCat._Stream(
                    self.__greycat, socket.SocketIO(conn, "rwb"))
                endpoint = stream.read()
                parameters = stream.read()
                res = self.__endpoints[endpoint](*parameters)
                stream.write(res)
                stream.close()
                conn.close()

    @final
    class AbiReader:
        def __init__(self: GreyCat.AbiReader, stream: GreyCat._Stream) -> None:
            self.__stream: GreyCat._Stream = stream

        def read(self) -> Any:
            return self.__stream.read()

        def available(self) -> int:
            return len(self.__stream._io.peek())

    @final
    class AbiWriter:
        def __init__(self: GreyCat.AbiWriter, stream: GreyCat._Stream) -> None:
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
        ASCII_MAX: Final[int] = 127

        def __init__(
            self: GreyCat._Stream, greycat: GreyCat, io: BufferedReader | BufferedWriter | socket.SocketIO
        ) -> None:
            self.greycat: Final[GreyCat] = greycat
            self._io: BufferedReader | BufferedWriter | socket.SocketIO = io

        def close(self) -> None:
            self._io.close()

        def read_abi_header(self) -> None:
            abi_major: int = self.read_i16()
            if abi_major != GreyCat.ABI_PROTO:
                raise RuntimeError("wrong ABI protocol major version")
            abi_magic: int = self.read_i16()
            if abi_magic != self.greycat._abi_magic:
                raise RuntimeError(
                    f"wrong ABI magic: expected {self.greycat._abi_magic}, got {abi_magic}"
                )
            abi_version: int = self.read_i32()
            if abi_version > self.greycat._abi_version:
                raise RuntimeError(
                    "larger ABI version, please reload this handler")

        def read(self) -> Any:
            primitive_offset: int = self.read_i8()
            return GreyCat._Stream._PRIMITIVE_LOADERS[primitive_offset](self)

        def read_null(self) -> None:
            return None

        def read_bool(self) -> bool:
            return self.read_i8() != 0

        def read_char(self) -> c_char:
            return c_char(self.read_i8())

        def read_i8(self) -> int:
            return c_int8(self._io.read(1)[0]).value

        def read_i8_array(self, len_: int) -> bytes:
            tmp: bytes = self._io.read(len_)
            if len(tmp) < len_:
                raise Exception(f"{len(tmp)} < {len_}")
            return tmp

        def read_i16(self) -> int:
            tmp: bytes = self.read_i8_array(2)
            return c_int16((tmp[1] << 8) + ((tmp[0] << 8) >> 8)).value

        def read_i32(self) -> int:
            tmp: bytes = self.read_i8_array(4)
            return c_int32(
                (tmp[3] << 24)
                + ((tmp[2] << 24) >> 8)
                + ((tmp[1] << 24) >> 16)
                + ((tmp[0] << 24) >> 24)
            ).value

        def read_vu32(self) -> int:
            current: int
            value: int = 0

            current = self._io.read(1)[0]
            value |= current & 0x7F
            if 0 == (current & 0x80):
                return value

            current = self._io.read(1)[0]
            value |= (current & 0x7F) << 7
            if 0 == (current & 0x80):
                return value

            current = self._io.read(1)[0]
            value |= (current & 0x7F) << 14
            if 0 == (current & 0x80):
                return value

            current = self._io.read(1)[0]
            value |= (current & 0x7F) << 21
            if 0 == (current & 0x80):
                return value

            current = self._io.read(1)[0]
            value |= current << 28
            return value

        def read_i64(self) -> int:
            tmp: bytes = self.read_i8_array(8)
            return (
                (tmp[7] << 56)
                + ((tmp[6] << 56) >> 8)
                + ((tmp[5] << 56) >> 16)
                + ((tmp[4] << 56) >> 24)
                + ((tmp[3] << 56) >> 32)
                + ((tmp[2] << 56) >> 40)
                + ((tmp[1] << 56) >> 48)
                + ((tmp[0] << 56) >> 56)
            )

        def read_vi64(self) -> int:
            sign_swapped_value: int = self.read_vu64()
            return ((sign_swapped_value >> 1) ^ (-(-sign_swapped_value & 1)))

        def read_vu64(self) -> int:
            current: int
            value: int = 0

            current = self._io.read(1)[0]
            value |= current & 0x7F
            if 0 == (current & 0x80):
                return value

            current = self._io.read(1)[0]
            value |= (current & 0x7F) << 7
            if 0 == (current & 0x80):
                return value

            current = self._io.read(1)[0]
            value |= (current & 0x7F) << 14
            if 0 == (current & 0x80):
                return value

            current = self._io.read(1)[0]
            value |= (current & 0x7F) << 21
            if 0 == (current & 0x80):
                return value

            current = self._io.read(1)[0]
            value |= (current & 0x7F) << 28
            if 0 == (current & 0x80):
                return value

            current = self._io.read(1)[0]
            value |= (current & 0x7F) << 35
            if 0 == (current & 0x80):
                return value

            current = self._io.read(1)[0]
            value |= (current & 0x7F) << 42
            if 0 == (current & 0x80):
                return value

            current = self._io.read(1)[0]
            value |= (current & 0x7F) << 49
            if 0 == (current & 0x80):
                return value

            current = self._io.read(1)[0]
            value |= current << 56
            return value

        def read_f64(self) -> float:
            return unpack("d", pack("q", self.read_i64()))[0]

        def read_string(self, len_: int) -> str:
            return self.read_i8_array(len_).decode("utf-8")

        def read_string_lit(self) -> str:
            offset: int = self.read_vu32()
            if 0 == (offset & 1):
                raise IOError("wrong state")
            offset >>= 1
            if offset < len(self.greycat.symbols):
                return self.greycat.symbols[offset]
            raise ValueError("invalid primitive type")

        def read_object(self) -> Any:
            type_offset: int = self.read_vu32()
            type: Final[GreyCat.Type] = self.greycat.types[type_offset]
            return type.loader(type, self)

        def write_abi_header(self) -> None:
            self.write_i16(GreyCat.ABI_PROTO)
            self.write_i16(self.greycat._abi_magic)
            self.write_i32(self.greycat._abi_version)

        def write(self, value: Any, type_offset: int | None = None) -> None:
            if value is None:
                self.write_i8(PrimitiveType.NULL)
            elif type(value) is bool:
                self.write_i8(PrimitiveType.BOOL)
                self.write_bool(value)
            elif type(value) is c_char:
                c: c_char = value
                self.write_i8(PrimitiveType.CHAR)
                self.write_i8(c.value[0])
            elif type(value) is int:
                self.write_i8(PrimitiveType.INT)
                self.write_vi64(value)
            elif type(value) is c_int64:
                self.write_i8(PrimitiveType.INT)
                self.write_vi64(value.value)
            elif type(value) is float:
                self.write_i8(PrimitiveType.FLOAT)
                self.write_f64(value)
            elif type(value) is c_double:
                self.write_i8(PrimitiveType.FLOAT)
                self.write_f64(value.value)
            elif type(value) is str:
                self.write_string(value)
            elif issubclass(type(value), greycat.GreyCat.Object):
                o: GreyCat.Object = value
                o._save_type(self, type_offset)
                o._save(self)

        def write_string(self, s: str, skip_type: bool = False) -> None:
            if s in self.greycat._symbols_off_by_value:
                symbolOffset: int = self.greycat._symbols_off_by_value[s]
                if not skip_type:
                    self.write_i8(PrimitiveType.STRING_LIT)
                self.write_vu32(symbolOffset << 1 | 1)
            else:
                if not skip_type:
                    self.write_i8(PrimitiveType.OBJECT)
                    self.write_vu32(self.greycat.type_offset_core_string)
                data = s.encode("utf-8")
                self.write_vu32(len(data) << 1)
                self.write_i8_array(data, 0, len(data))

        def write_bool(self, b: bool) -> None:
            self._io.write(bytearray([1 if b else 0]))

        def write_i8(self, b: int) -> None:
            self._io.write(bytearray([b]))

        def write_i8_array(self, b: bytearray | bytes, offset: int, len_: int) -> None:
            self._io.write(b[slice(offset, offset + len_)])

        def write_i16(self, i: int) -> None:
            tmp: bytearray = bytearray(2)
            tmp[0] = i & 0xFF
            tmp[1] = (i >> 8) & 0xFF
            self._io.write(tmp)

        def write_i32(self, i: int) -> None:
            tmp: bytearray = bytearray(4)
            tmp[0] = i & 0xFF
            tmp[1] = (i >> 8) & 0xFF
            tmp[2] = (i >> 16) & 0xFF
            tmp[3] = (i >> 24) & 0xFF
            self._io.write(tmp)

        def write_vu32(self, value: int) -> None:
            packed_value: bytearray = bytearray(5)

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

        def write_i64(self, i: int) -> None:
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

        def write_vi64(self, i: int) -> None:
            self.write_vu64((i << 1) ^ (i >> 63))

        def write_vu64(self, value: int) -> None:
            packed_value: Final[bytearray] = bytearray(9)

            # TODO: check necessity of c_ubyte here (and below)
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

        def write_f64(self, d: float):
            self.write_i64(unpack("q", pack("d", d))[0])

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

        __t2_loader: Final[
            Callable[[GreyCat._Stream], object]
        ] = lambda stream: GreyCat._Stream.__type_loader(
            stream, stream.greycat.types[stream.greycat.type_offset_core_t2]
        )

        __t3_loader: Final[
            Callable[[GreyCat._Stream], object]
        ] = lambda stream: GreyCat._Stream.__type_loader(
            stream, stream.greycat.types[stream.greycat.type_offset_core_t3]
        )

        __t4_loader: Final[
            Callable[[GreyCat._Stream], object]
        ] = lambda stream: GreyCat._Stream.__type_loader(
            stream, stream.greycat.types[stream.greycat.type_offset_core_t4]
        )

        __str_loader: Final[
            Callable[[GreyCat._Stream], object]
        ] = lambda stream: GreyCat._Stream.__type_loader(
            stream, stream.greycat.types[stream.greycat.type_offset_core_str]
        )

        __t2f_loader: Final[
            Callable[[GreyCat._Stream], object]
        ] = lambda stream: GreyCat._Stream.__type_loader(
            stream, stream.greycat.types[stream.greycat.type_offset_core_t2f]
        )

        __t3f_loader: Final[
            Callable[[GreyCat._Stream], object]
        ] = lambda stream: GreyCat._Stream.__type_loader(
            stream, stream.greycat.types[stream.greycat.type_offset_core_t3f]
        )

        __t4f_loader: Final[
            Callable[[GreyCat._Stream], object]
        ] = lambda stream: GreyCat._Stream.__type_loader(
            stream, stream.greycat.types[stream.greycat.type_offset_core_t4f]
        )

        ___type_loader: Final[
            Callable[[GreyCat._Stream], object]
        ] = lambda stream: GreyCat._Stream.__type_loader(
            stream, stream.greycat.types[stream.greycat.type_offset_core_type]
        )

        __field_loader: Final[
            Callable[[GreyCat._Stream], object]
        ] = lambda stream: GreyCat._Stream.__type_loader(
            stream, stream.greycat.types[stream.greycat.type_offset_core_field]
        )

        @staticmethod
        @final
        def __error_loader(stream: GreyCat._Stream) -> object:
            raise ValueError("invalid primitive type")

        __string_lit_loader: Final[
            Callable[[GreyCat._Stream], object]
        ] = lambda stream: stream.read_string_lit()

        _PRIMITIVE_LOADERS: Final[List[__PrimitiveLoader]] = [
            None
        ] * PrimitiveType.SIZE
        _PRIMITIVE_LOADERS[PrimitiveType.NULL] = __null_loader
        _PRIMITIVE_LOADERS[PrimitiveType.BOOL] = __bool_loader
        _PRIMITIVE_LOADERS[PrimitiveType.CHAR] = __char_loader
        _PRIMITIVE_LOADERS[PrimitiveType.INT] = __i64_loader
        _PRIMITIVE_LOADERS[PrimitiveType.FLOAT] = __f64_loader
        _PRIMITIVE_LOADERS[PrimitiveType.NODE] = __node_loader
        _PRIMITIVE_LOADERS[PrimitiveType.NODE_TIME] = __node_time_loader
        _PRIMITIVE_LOADERS[PrimitiveType.NODE_INDEX] = __node_index_loader
        _PRIMITIVE_LOADERS[PrimitiveType.NODE_LIST] = __node_list_loader
        _PRIMITIVE_LOADERS[PrimitiveType.NODE_GEO] = __node_geo_loader
        _PRIMITIVE_LOADERS[PrimitiveType.GEO] = __geo_loader
        _PRIMITIVE_LOADERS[PrimitiveType.TIME] = __time_loader
        _PRIMITIVE_LOADERS[PrimitiveType.DURATION] = __duration_loader
        _PRIMITIVE_LOADERS[PrimitiveType.STATIC_FIELD] = __object_loader
        _PRIMITIVE_LOADERS[PrimitiveType.OBJECT] = __object_loader
        _PRIMITIVE_LOADERS[PrimitiveType.T2] = __t2_loader
        _PRIMITIVE_LOADERS[PrimitiveType.T3] = __t3_loader
        _PRIMITIVE_LOADERS[PrimitiveType.T4] = __t4_loader
        _PRIMITIVE_LOADERS[PrimitiveType.STR] = __str_loader
        _PRIMITIVE_LOADERS[PrimitiveType.T2F] = __t2f_loader
        _PRIMITIVE_LOADERS[PrimitiveType.T3F] = __t3f_loader
        _PRIMITIVE_LOADERS[PrimitiveType.T4F] = __t4f_loader
        _PRIMITIVE_LOADERS[PrimitiveType.TYPE] = ___type_loader
        _PRIMITIVE_LOADERS[PrimitiveType.FIELD] = __field_loader
        _PRIMITIVE_LOADERS[PrimitiveType.BLOCK_REF] = __error_loader
        # TODO?
        _PRIMITIVE_LOADERS[PrimitiveType.FUNCTION] = __error_loader
        _PRIMITIVE_LOADERS[PrimitiveType.UNDEFINED] = __error_loader
        _PRIMITIVE_LOADERS[PrimitiveType.STRING_LIT] = __string_lit_loader

    class Function:
        def __init__(self: GreyCat.Function, name: str, params: list[tuple[bool, int, int]], f: Callable[..., Any] | None = None) -> None:
            self.name: Final[str] = name
            self.params: list[tuple[bool, int, int]] = params
            self.f: Callable[..., Any] | None = f

    class Type:
        class Attribute:
            def __init__(
                self: GreyCat.Type.Attribute,
                name: str,
                abi_type: int,
                prog_type_offset: int,
                mapped_any_offset: int,
                mapped_att_offset: int,
                sbi_type: int,
                nullable: bool,
                mapped: bool,
            ):
                self.name: Final[str] = name
                self.abi_type: Final[int] = abi_type
                self.prog_type_offset: Final[int] = prog_type_offset
                self.mapped_any_offset: Final[int] = mapped_any_offset
                self.mapped_att_offset: Final[int] = mapped_att_offset
                self.sbi_type: Final[int] = sbi_type
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
            value_offset: Final[int] = stream.read_vu32()
            abi_type_att: Final[GreyCat.Type.Attribute] = type.attributes[value_offset]
            return program_type.enum_values[abi_type_att.mapped_att_offset]

        @staticmethod
        @final
        def __object_loader(type: GreyCat.Type, stream: GreyCat._Stream) -> Any:
            program_type: Final[GreyCat.Type] = type.greycat.types[type.mapped_type_off]
            attributes: Final[List[Any]] = [
                None] * len(program_type.attributes)
            nullable_bitset: bytes = stream.read_i8_array(
                type.nullable_nb_bytes)
            nullable_offset: int = -1
            att: GreyCat.Type.Attribute
            loaded_field: Any
            for att in type.attributes:
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
                load_type: int = att.sbi_type
                if load_type == PrimitiveType.UNDEFINED:
                    load_type = stream.read_i8()
                if load_type == PrimitiveType.STATIC_FIELD:
                    field_type: GreyCat.Type = type.greycat.types[att.abi_type]
                    if att.sbi_type == PrimitiveType.UNDEFINED:
                        loaded_field = GreyCat.Type.__enum_loader(
                            type.greycat.types[stream.read_vu32()], stream)
                    else:
                        loaded_field = GreyCat.Type.__enum_loader(
                            field_type, stream)
                elif load_type == PrimitiveType.OBJECT:
                    field_type: GreyCat.Type = type.greycat.types[att.abi_type]
                    # if (not field_type.is_native) and (
                    #     field_type.is_abstract
                    #     or att.sbi_type == PrimitiveType.UNDEFINED
                    # ):
                    if field_type.is_ambiguous or type.greycat.type_offset_core_any == field_type.offset or ((not field_type.is_native) and att.sbi_type == PrimitiveType.UNDEFINED):
                        field_type = type.greycat.types[stream.read_vu32()]
                    loaded_field = field_type.loader(field_type, stream)
                else:
                    loaded_field = GreyCat._Stream._PRIMITIVE_LOADERS[
                        load_type
                    ](stream)
                if att.mapped:
                    attributes[att.mapped_att_offset] = loaded_field
            if program_type.factory is None:
                return GreyCat.Object(program_type, attributes)
            else:
                return program_type.factory(program_type, attributes)

        @staticmethod
        @final
        def __monomorphic_factory(type: GreyCat.Type, parameters: list[Any]) -> Any:
            genericType: Final[GreyCat.Type] = type.greycat.types[type.genericAbiType]
            return genericType.factory(genericType, parameters)

        @staticmethod
        @final
        def __monomorphic_loader(type: GreyCat.Type, stream: GreyCat._Stream) -> Any:
            genericType: Final[GreyCat.Type] = type.greycat.types[type.genericAbiType]
            return genericType.loader(type, stream)

        def __init__(
            self: GreyCat.Type,
            offset: int,
            name: str,
            genericAbiType: int,
            g1AbiTypeDesc: int,
            g2AbiTypeDesc: int,
            mapped_type_off: int,
            masked_type_off: int,
            nullable_nb_bytes: int,
            is_masked: bool,
            is_abstract: bool,
            is_ambiguous: bool,
            is_enum: bool,
            is_native: bool,
            type_attributes: List[GreyCat.Type.Attribute],
            factory: GreyCat.Factory | None,
            loader: GreyCat.Loader | None,
            greycat: GreyCat,
        ) -> None:
            self.offset: Final[int] = offset
            self.name: Final[str] = name
            self.genericAbiType: Final[int] = genericAbiType
            self.g1AbiTypeDesc: Final[int] = g1AbiTypeDesc
            self.g2AbiTypeDesc: Final[int] = g2AbiTypeDesc
            self.mapped_type_off: Final[int] = mapped_type_off
            self.masked_type_off: Final[int] = masked_type_off
            self.nullable_nb_bytes: Final[int] = nullable_nb_bytes
            self.is_masked: Final[bool] = is_masked
            self.is_abstract: Final[bool] = is_abstract
            self.is_ambiguous: Final[bool] = is_ambiguous
            self.is_enum: Final[bool] = is_enum
            self.is_native: Final[bool] = is_native
            self.attributes: Final[List[GreyCat.Type.Attribute]
                                   ] = type_attributes
            self.attribute_off_by_name: Final[dict[str, int]] = {}
            att_offset: int
            for att_offset in range(len(type_attributes)):
                self.attribute_off_by_name[
                    type_attributes[att_offset].name
                ] = att_offset
            self.greycat: Final[GreyCat] = greycat
            self.factory: Final[GreyCat.Factory]
            if 0 == genericAbiType:
                self.factory = factory
            else:
                self.factory = GreyCat.Type.__monomorphic_factory
            self.enum_values: Final[List[GreyCat.Enum]] | None
            if offset == mapped_type_off:
                if self.is_enum:
                    self.enum_values = []
                    enum_offset: int
                    for enum_offset in range(len(type_attributes)):
                        attributes: List[Any] = [
                            enum_offset,
                            type_attributes[enum_offset].name,
                            None,
                        ]
                        if self.factory is None:
                            self.enum_values.append(
                                GreyCat.Enum(self, attributes))
                        else:
                            self.enum_values.append(
                                self.factory(self, attributes))
                else:
                    self.enum_values = None
            else:
                self.enum_values = None
            self.loader: Final[GreyCat.Loader]
            if 0 != genericAbiType:
                self.loader = GreyCat.Type.__monomorphic_loader
            elif loader is not None:
                self.loader = loader
            elif self.is_native:
                self.loader = GreyCat.Type.__error_loader
            elif self.is_enum:
                self.loader = GreyCat.Type.__enum_loader
            else:
                self.loader = GreyCat.Type.__object_loader
            self.static_values: List[Any] = []
            self.generated_offsets: List[int] | None = None

        def resolve_generated_offsets(self, *args: str) -> None:
            self.generated_offsets: List[int] = []
            for arg in args:
                resolved: int | None = self.attribute_off_by_name.get(arg)
                if resolved is None:
                    raise ValueError(
                        f"unmapped generated field, please re-generate this code!"
                    )
                self.generated_offsets.append(resolved)

        def resolve_generated_offset_with_values(self, *args: Any) -> None:
            self.generated_offsets: List[int] = []
            name_offset: int
            for name_offset in range(0, len(args), 2):
                resolved: int | None = self.attribute_off_by_name.get(
                    args[name_offset])
                if resolved is None:
                    raise ValueError(
                        "unmapped generated field, please re-generate this code!"
                    )
                self.generated_offsets.append(resolved)
                self.enum_values[resolved].value = args[name_offset + 1]

    class Object:
        def __init__(self: GreyCat.Object, type: GreyCat.Type, attributes: List[Any] | None) -> None:
            self.type_: Final[GreyCat.Type] = type
            self.attributes: List[Any] | None = attributes

        def get(self, attribute_name: str) -> Any | None:
            return self._get(self.type_.attribute_off_by_name[attribute_name])

        def set(self, attribute_name: str, value: Any | None) -> None:
            self._set(self.type_.attribute_off_by_name[attribute_name], value)

        def _get(self, offset: int) -> Any | None:
            return self.attributes[offset]

        def _set(self, offset: int, value: Any | None) -> None:
            self.attributes[offset] = value

        def _save_type(self, stream: GreyCat._Stream, type_offset: int | None = None) -> None:
            stream.write_i8(PrimitiveType.OBJECT)
            stream.write_vu32(
                self.type_.offset if type_offset is None else type_offset)

        def _save(self, stream: GreyCat._Stream) -> None:
            nullable_bitset: bytearray = bytearray(
                self.type_.nullable_nb_bytes)
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
                if field.sbi_type == PrimitiveType.NULL:
                    pass
                elif field.sbi_type == PrimitiveType.BOOL:
                    stream.write_bool(bool(value))
                elif field.sbi_type == PrimitiveType.CHAR:
                    c: int = c_ubyte(value).value
                    if c > GreyCat._Stream.ASCII_MAX:
                        raise ValueError(
                            f"Only ASCII characters are allowed: {c}")
                    stream.write_i8(c)
                elif field.sbi_type == PrimitiveType.INT:
                    if type(value) is c_int64:
                        stream.write_vi64(value.value)
                    else:
                        stream.write_vi64(value)
                elif field.sbi_type == PrimitiveType.FLOAT:
                    if type(value) is c_double:
                        stream.write_f64(value.value)
                    else:
                        stream.write_f64(value)
                elif field.sbi_type == PrimitiveType.NODE:
                    o._save(stream)
                elif field.sbi_type == PrimitiveType.NODE_TIME:
                    o = value
                    o._save(stream)
                elif field.sbi_type == PrimitiveType.NODE_INDEX:
                    o = value
                    o._save(stream)
                elif field.sbi_type == PrimitiveType.NODE_LIST:
                    o = value
                    o._save(stream)
                elif field.sbi_type == PrimitiveType.NODE_GEO:
                    o = value
                    o._save(stream)
                elif field.sbi_type == PrimitiveType.GEO:
                    o = value
                    o._save(stream)
                elif field.sbi_type == PrimitiveType.T2:
                    o = value
                    o._save(stream)
                elif field.sbi_type == PrimitiveType.T3:
                    o = value
                    o._save(stream)
                elif field.sbi_type == PrimitiveType.T4:
                    o = value
                    o._save(stream)
                elif field.sbi_type == PrimitiveType.TIME:
                    o = value
                    o._save(stream)
                elif field.sbi_type == PrimitiveType.DURATION:
                    o = value
                    o._save(stream)
                elif field.sbi_type == PrimitiveType.STATIC_FIELD:
                    o = value
                    o._save(stream)
                elif field.sbi_type == PrimitiveType.OBJECT:
                    if type(value) is str:
                        string: str = value
                        symbol_offset: int | None = (
                            self.type_.greycat._symbols_off_by_value[string]
                        )
                        if not (symbol_offset is None):
                            stream.write_vu32(
                                (symbol_offset << 1) | 1)
                        else:
                            data: bytes = string.encode("u%-8")
                            stream.write_vu32(len(data))
                            stream.write_i8_array(bytes, 0, len(data))
                    else:
                        o: GreyCat.Object = value
                        if field.abi_type != o.type_.offset and self.type_.greycat.types[field.abi_type].genericAbiType != o.type_.offset:
                            stream.write_vu32(o.type_.offset)
                        o._save(stream)
                # elif field.sbi_type == PrimitiveType.BLOCK_REF: # TODO
                # elif field.sbi_type == PrimitiveType.FUNCTION: # TODO
                elif field.sbi_type == PrimitiveType.UNDEFINED:
                    stream.write(value)
                else:
                    raise ValueError(f"wrong state: {field.sbi_type}")

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
        def __init__(self: GreyCat.Enum, type: GreyCat.Type, attributes: List[Any]) -> None:
            super().__init__(type, attributes)
            self.offset: Final[int] = attributes[0]
            self.key: Final[str] = attributes[1]
            self.value: Any = attributes[2]

        @final
        def _save_type(self, stream: GreyCat._Stream, _=None) -> None:
            stream.write_i8(PrimitiveType.STATIC_FIELD)
            stream.write_vu32(self.type_.offset)

        @final
        def _save(self, stream: GreyCat._Stream) -> None:
            stream.write_vu32(self.offset)

        def __str__(self) -> str:
            if self.value is None:
                return f"{self.type_.name}.{self.key}"
            return f"{self.type_.name}.{self.key}{{value={self.value}}}"

    Loader: Final[type[Callable[[Type, _Stream], Any]]
                  ] = Callable[[Type, _Stream], Any]

    Factory: Final[type[Callable[[Type, List[Any]], Any]]] = Callable[
        [Type, List[object]], Any
    ]

    class Library:
        def __init__(self: GreyCat.Library) -> None:
            self.mapped: List[GreyCat.Type] | None = None

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

    def __init__(self: GreyCat, url: str, libraries: List[GreyCat.Library] = [], username: str | None = None, password: str | None = None, use_cookie: bool = False, set_default: bool = True) -> None:
        GreyCat._DEFAULT: GreyCat | None = None

        self.__runtime_url: Final[str] = url
        self.__token: str | None = None
        if username is not None and password is not None:
            self.login(username, password, use_cookie)
        self.libs_by_name: Final[dict[str, GreyCat.Library]] = {}
        std_: greycat.std = greycat.std()
        self.libs_by_name[std_.name()] = std_
        self.__is_remote: bool = False
        library_offset: int
        # for declarations
        lib: GreyCat.Library
        for lib in libraries:
            self.libs_by_name[lib.name()] = lib
        loaders: Final[dict[str, GreyCat.Loader]] = {}
        factories: Final[dict[str, GreyCat.Factory]] = {}
        for lib in self.libs_by_name.values():
            lib.configure(loaders, factories)
        abi_stream: Final[GreyCat._Stream] = self.__get_abi(url)

        # step 0: verify abi version
        abi_major: int = abi_stream.read_i16()
        if abi_major != GreyCat.ABI_PROTO:
            raise Exception(
                f"wrong ABI proto: expected ${GreyCat.ABI_PROTO}, got {abi_major}"
            )
        self._abi_magic: Final[int] = abi_stream.read_i16()
        self._abi_version: Final[int] = abi_stream.read_i32()
        crc: int = abi_stream.read_i64()

        # step 1: create all symbols
        symbols_bytes: Final[int] = abi_stream.read_i64()
        symbols_count: Final[int] = abi_stream.read_i32()
        self.symbols: Final[List[str | None]] = [None]
        self._symbols_off_by_value: Final[dict[str, int]] = {}
        for offset in range(1, symbols_count + 1):
            symbol: str = abi_stream.read_string(abi_stream.read_vu32())
            self.symbols.append(symbol)
            self._symbols_off_by_value[symbol] = offset

        # step 2: create all types
        types_bytes: Final[int] = abi_stream.read_i64()
        types_size: Final[int] = abi_stream.read_i32()
        self.types: Final[List[GreyCat.Type]] = []
        attributes_size: Final[int] = abi_stream.read_i32()
        type_offset: int
        self.types_by_name: Final[dict[str, GreyCat.Type]] = {}
        for type_offset in range(types_size):
            module_name: str = self.symbols[abi_stream.read_vu32()]
            type_name: str = self.symbols[abi_stream.read_vu32()]
            lib_name: str = self.symbols[abi_stream.read_vu32()]
            fqn: str = f'{"" if module_name is None else f"{module_name}::"}{
                type_name}'
            generic_abi_type: Final[int] = abi_stream.read_vu32()
            g1_abi_type_desc: Final[int] = abi_stream.read_vu32()
            g2_abi_type_desc: Final[int] = abi_stream.read_vu32()
            # TODO: use?
            parent_type_id: Final[int] = abi_stream.read_vu32()
            attributes_len: int = abi_stream.read_vu32()
            abi_stream.read_vu32()  # unused field
            abi_stream.read_vu32()  # unused field
            mapped_abi_type_offset: int = abi_stream.read_vu32()
            masked_abi_type_offset: int = abi_stream.read_vu32()
            nullable_nb_bytes: int = abi_stream.read_vu32()
            flags: int = abi_stream.read_i8()
            is_native: bool = 0 != (flags & 1)
            is_abstract: bool = 0 != (flags & (1 << 1))
            is_enum: bool = 0 != (flags & (1 << 2))
            is_masked: bool = 0 != (flags & (1 << 3))
            is_ambiguous: bool = 0 != (flags & (1 << 4))
            is_volatile: bool = 0 != (flags & (1 << 5))
            type_attributes: Final[List[GreyCat.Type.Attribute]] = []
            for _ in repeat(None, attributes_len):
                name: Final[str] = self.symbols[abi_stream.read_vu32()]
                att_abi_type: Final[int] = abi_stream.read_vu32()
                prog_type_offset: Final[int] = abi_stream.read_vu32()
                mapped_any_offset: Final[int] = abi_stream.read_vu32()
                mapped_att_offset: Final[int] = abi_stream.read_vu32()
                sbi_type: Final[int] = abi_stream.read_i8()
                precision: Final[int] = abi_stream.read_i8()
                att_flags: Final[int] = abi_stream.read_i8()
                nullable: Final[bool] = 0 != (att_flags & 1)
                mapped: Final[bool] = 0 != (att_flags & (1 << 1))
                type_attributes.append(
                    GreyCat.Type.Attribute(
                        name,
                        att_abi_type,
                        prog_type_offset,
                        mapped_any_offset,
                        mapped_att_offset,
                        sbi_type,
                        nullable,
                        mapped,
                    )
                )
            if is_volatile:
                continue
            factory: GreyCat.Factory | None = None
            loader: GreyCat.Loader | None = None
            if 0 == generic_abi_type:
                if fqn in factories:
                    factory = factories[fqn]
                if fqn in loaders:
                    loader = loaders[fqn]
            else:
                super_fqn: str = self.types[generic_abi_type].name
                if super_fqn in factories:
                    factory = factories[super_fqn]
                if super_fqn in loaders:
                    loader = loaders[super_fqn]
            abi_type: GreyCat.Type = GreyCat.Type(
                type_offset,
                fqn,
                generic_abi_type,
                g1_abi_type_desc,
                g2_abi_type_desc,
                mapped_abi_type_offset,
                masked_abi_type_offset,
                nullable_nb_bytes,
                is_masked,
                is_abstract,
                is_ambiguous,
                is_enum,
                is_native,
                type_attributes,
                factory,
                loader,
                self,
            )
            if abi_type.mapped_type_off == type_offset and len(fqn) != 0:
                self.types_by_name[abi_type.name] = abi_type
            self.types.append(abi_type)
        # step 3: create all functions
        functions_bytes: Final[int] = abi_stream.read_i64()
        functions_size: Final[int] = abi_stream.read_i32()
        self.functions_by_name: Final[dict[str, GreyCat.Function]] = {}
        function_offset: int
        for function_offset in range(functions_size):
            module_name: str = self.symbols[abi_stream.read_vu32()]
            type_name: str = self.symbols[abi_stream.read_vu32()]
            function_name: str = self.symbols[abi_stream.read_vu32()]
            lib_name: str = self.symbols[abi_stream.read_vu32()]
            fqn: str = f'{"" if module_name is None else f"{module_name}::"}{
                "" if type_name is None else f"{type_name}::"}{function_name}'
            nb_params: int = abi_stream.read_vu32()
            params: list[tuple[bool, int, int]] = [None] * nb_params
            param_offset: int
            for param_offset in range(nb_params):
                nullable = abi_stream.read_bool()
                type_offset = abi_stream.read_vu32()
                symbol_offset = abi_stream.read_vu32()
                params[param_offset] = (nullable, type_offset, symbol_offset)
            abi_stream.read_vu32()
            abi_stream.read_i8()
            fn: GreyCat.Function = GreyCat.Function(fqn, params)
            self.functions_by_name[fqn] = fn
        # pre-resolve String type avoid runtime over-head
        tmp: GreyCat.Type = self.types_by_name["core::any"]
        if tmp is None:
            raise ValueError("wrong state")
        self.type_offset_core_any: Final[int] = tmp.offset

        tmp = self.types_by_name["core::String"]
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

        tmp = self.types_by_name["core::t2"]
        if tmp is None:
            raise ValueError("wrong state")
        self.type_offset_core_t2: Final[int] = tmp.offset

        tmp = self.types_by_name["core::t3"]
        if tmp is None:
            raise ValueError("wrong state")
        self.type_offset_core_t3: Final[int] = tmp.offset

        tmp = self.types_by_name["core::t4"]
        if tmp is None:
            raise ValueError("wrong state")
        self.type_offset_core_t4: Final[int] = tmp.offset

        tmp = self.types_by_name["core::str"]
        if tmp is None:
            raise ValueError("wrong state")
        self.type_offset_core_str: Final[int] = tmp.offset

        tmp = self.types_by_name["core::t2f"]
        if tmp is None:
            raise ValueError("wrong state")
        self.type_offset_core_t2f: Final[int] = tmp.offset

        tmp = self.types_by_name["core::t3f"]
        if tmp is None:
            raise ValueError("wrong state")
        self.type_offset_core_t3f: Final[int] = tmp.offset

        tmp = self.types_by_name["core::t4f"]
        if tmp is None:
            raise ValueError("wrong state")
        self.type_offset_core_t4f: Final[int] = tmp.offset

        tmp = self.types_by_name["core::type"]
        if tmp is None:
            raise ValueError("wrong state")
        self.type_offset_core_type: Final[int] = tmp.offset

        tmp = self.types_by_name["core::field"]
        if tmp is None:
            raise ValueError("wrong state")
        self.type_offset_core_field: Final[int] = tmp.offset

        abi_stream.close()
        for lib in self.libs_by_name.values():
            lib.init(self)

        if set_default:
            GreyCat._DEFAULT: GreyCat = self

    def call(self, fqn: str, parameters: List[object] = [], task: bool = False) -> object:
        if not (self.__is_remote):
            raise RuntimeError(
                "Remote calls are not available on local GreyCat handles"
            )
        url: str = f"{self.__runtime_url}"
        connection: http.client.HTTPConnection | http.client.HTTPSConnection
        if url.startswith("http://"):
            connection = http.client.HTTPConnection(url.replace("http://", ""))
        elif self.__runtime_url.startswith("https://"):
            connection = http.client.HTTPSConnection(
                url.replace("https://", ""))
        else:
            raise ValueError("wrong state")
        body: bytes | None = None
        stream: GreyCat._Stream
        fn: GreyCat.Function = self.functions_by_name[fqn]
        if len(parameters) > 0:
            b = bytearray()
            stream = GreyCat._Stream(self, ByteArrayIO(b))
            stream.write_abi_header()
            for index, parameter in enumerate(parameters):
                param_type = fn.params[index][1]
                stream.write(
                    parameter, None if param_type is self.type_offset_core_any else param_type)
            stream.close()
            body: bytes = bytes(b)
        headers: dict[str, str] = {
            "Content-Type": "application/octet-stream",
            "Accept": "application/octet-stream",
        }
        if self.__token is not None:
            headers["Authorization"] = self.__token
        if task:
            headers["task"] = ""
        connection.request(
            "POST",
            f"/{fqn}",
            body,
            headers,
        )
        response: http.client.HTTPResponse = connection.getresponse()
        status: int = response.status
        stream = GreyCat._Stream(self, response)
        stream.read_abi_header()
        res = stream.read()
        if 200 > status or 300 <= status:
            raise RuntimeError(f'HTTP {status}: {response.reason}\n\t{res}"')
        # if len(response.read(1)) > 0:
        #     raise IOError('Remaining unread bytes')
        stream.close()
        return res

    def fetch(self, path: str) -> object:
        connection: http.client.HTTPConnection | http.client.HTTPSConnection
        if self.__runtime_url.startswith("http://"):
            connection: http.client.HTTPConnection = http.client.HTTPConnection(
                self.__runtime_url.replace("http://", "")
            )
        elif self.__runtime_url.startswith("https://"):
            connection: http.client.HTTPSConnection = http.client.HTTPSConnection(
                self.__runtime_url.replace("https://", "")
            )
        else:
            raise ValueError
        headers: dict[str, str] = {
            "Accept": "application/octet-stream",
        }
        if self.__token is not None:
            headers["Authorization"] = self.__token
        connection.request(
            "GET",
            f"/{path}",
            None,
            headers
        )
        response: http.client.HTTPResponse = connection.getresponse()
        status: int = response.status
        stream = GreyCat._Stream(self, response)
        if 200 > status or 300 <= status:
            raise RuntimeError(f'HTTP {status}: {response.reason}"')
        stream.read_abi_header()
        res = stream.read()
        # if len(response.read(1)) > 0:
        #     raise IOError('Remaining unread bytes')
        stream.close()
        return res

    def login(self, username: str, password: str, use_cookie: bool = False) -> None:
        connection: http.client.HTTPConnection | http.client.HTTPSConnection
        if self.__runtime_url.startswith("http://"):
            connection: http.client.HTTPConnection = http.client.HTTPConnection(
                self.__runtime_url.replace("http://", "")
            )
        elif self.__runtime_url.startswith("https://"):
            connection: http.client.HTTPSConnection = http.client.HTTPSConnection(
                self.__runtime_url.replace("https://", "")
            )
        else:
            raise ValueError
        credentials = base64.b64encode(
            f"{username}:{hashlib.sha256(password.encode('utf-8')).hexdigest()}".encode("utf-8")).decode("utf-8")
        body = json.dumps([credentials, use_cookie])
        connection.request(
            "POST",
            "runtime::User::login",
            body,
            {
                "Content-Type": "application/json",
                "Accept": "application/json",
            },
        )
        response: http.client.HTTPResponse = connection.getresponse()
        status: int = response.status
        if 200 > status or 300 <= status:
            raise RuntimeError(f'HTTP {status}: {response.reason}"')
        self.__token = json.loads(response.read().decode("utf-8"))

    def load(self, path: str) -> object:
        with open(path, 'rb') as fin:
            stream: GreyCat._Stream = GreyCat._Stream(self, fin)
            stream.read_abi_header()
            return stream.read()

    def create(self, name: str, parameters: List[Any]) -> Any:
        type: Final[GreyCat.Type | None] = self.types_by_name[name]
        if type is None:
            return None
        return type.factory(type, parameters)

    def create_geo(self, lat: float, lng: float):
        type: GreyCat.Type = self.types[self.type_offset_core_geo]
        geo: greycat.std.core.geo = type.factory(type, [])
        geo.lat = lat
        geo.lng = lng
        return geo

    def create_time(self, epoch_us: int):
        type: GreyCat.Type = self.types[self.type_offset_core_time]
        t: greycat.std.core.time = type.factory(type, [])
        t.value = epoch_us
        return t

    def create_duration(self, duration_us: int):
        type: GreyCat.Type = self.types[self.type_offset_core_duration]
        dur: greycat.std.core.duration = type.factory(type, [])
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
        headers: dict[str, str] = {
            "Accept": "application/octet-stream",
        }
        if self.__token is not None:
            headers["Authorization"] = self.__token
        connection.request(
            "POST",
            "/runtime::Runtime::abi",
            None,
            headers,
        )
        response: http.client.HTTPResponse = connection.getresponse()
        status: int = response.status
        if 200 > status or 300 <= status:
            raise RuntimeError(f'HTTP {status}: {response.reason}"')
        self.__is_remote = True
        return GreyCat._Stream(self, response)

    def __get_local_abi(self, runtime_url: str) -> GreyCat._Stream:
        if runtime_url.startswith("file://"):
            runtime_url = runtime_url.replace("file://", "", 1)
        return GreyCat._Stream(
            self, open(os.path.join(
                runtime_url, "gcdata", "abi"), "rb")
        )

    def __get_abi(self, runtime_url: str) -> GreyCat._Stream:
        if runtime_url.startswith("http"):
            return self.__get_remote_abi(runtime_url)
        else:
            return self.__get_local_abi(runtime_url)
