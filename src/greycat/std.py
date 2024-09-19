# AUTO-GENERATED FILE PLEASE DO NOT MODIFY MANUALLY
from __future__ import annotations
from ctypes import *
from typing import *
import struct
from greycat.greycat import GreyCat
from greycat.std_n import std_n


@final
class std(GreyCat.Library):
    name_: Final[str] = "std"

    def name(self) -> str:
        return self.name_

    @final
    class core:
        __T = TypeVar("__T")
        __K = TypeVar("__K")
        __V = TypeVar("__V")
        __U = TypeVar("__U")

        @final
        class GeoBox(GreyCat.Object):
            name_: Final[str] = "core::GeoBox"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def sw(self) -> std.core.geo:
                return self._get(self.type_.generated_offsets[0])

            def set_sw(self, v: std.core.geo) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def ne(self) -> std.core.geo:
                return self._get(self.type_.generated_offsets[1])

            def set_ne(self, v: std.core.geo) -> None:
                self._set(self.type_.generated_offsets[1], v)

            @staticmethod
            def create(sw: std.core.geo, ne: std.core.geo, greycat: Optional[GreyCat] = None) -> std.core.GeoBox:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                return std.core.GeoBox(greycat.libs_by_name[std.name_].mapped[0], [sw, ne])

        @final
        class Error(std_n.core._Error):
            name_: Final[str] = "core::Error"

            def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
                super().__init__(type)

            @staticmethod
            def create(greycat: Optional[GreyCat] = None) -> std_n.core._Error:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                return std.core.Error(greycat.libs_by_name[std.name_].mapped[1], [])

        @final
        class tf2d(std_n.core._tf2d):
            name_: Final[str] = "core::tf2d"

            def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
                super().__init__(type)

            @staticmethod
            def create(greycat: Optional[GreyCat] = None) -> std_n.core._tf2d:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                return std.core.tf2d(greycat.libs_by_name[std.name_].mapped[2], [])

        @final
        class Array(Generic[__T], std_n.core._Array[__T]):
            name_: Final[str] = "core::Array"

            def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
                super().__init__(type)

            @staticmethod
            def create(greycat: Optional[GreyCat] = None) -> std_n.core._Array:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                return std.core.Array(greycat.libs_by_name[std.name_].mapped[3], [])

        @final
        class String(std_n.core._String):
            name_: Final[str] = "core::String"

            def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
                super().__init__(type)

            @staticmethod
            def create(greycat: Optional[GreyCat] = None) -> std_n.core._String:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                return std.core.String(greycat.libs_by_name[std.name_].mapped[4], [])

        @final
        class Date(std_n.core._Date):
            name_: Final[str] = "core::Date"

            def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
                super().__init__(type)

            @staticmethod
            def create(greycat: Optional[GreyCat] = None) -> std_n.core._Date:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                return std.core.Date(greycat.libs_by_name[std.name_].mapped[5], [])

        @final
        class GeoPoly(GreyCat.Object):
            name_: Final[str] = "core::GeoPoly"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def points(self) -> std.core.Array:
                return self._get(self.type_.generated_offsets[0])

            def set_points(self, v: std.core.Array) -> None:
                self._set(self.type_.generated_offsets[0], v)

            @staticmethod
            def create(points: std.core.Array, greycat: Optional[GreyCat] = None) -> std.core.GeoPoly:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                return std.core.GeoPoly(greycat.libs_by_name[std.name_].mapped[6], [points])

        @final
        class ti5d(std_n.core._ti5d):
            name_: Final[str] = "core::ti5d"

            def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
                super().__init__(type)

            @staticmethod
            def create(greycat: Optional[GreyCat] = None) -> std_n.core._ti5d:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                return std.core.ti5d(greycat.libs_by_name[std.name_].mapped[7], [])

        @final
        class nodeTime(Generic[__T], std_n.core._nodeTime[__T]):
            name_: Final[str] = "core::nodeTime"

            def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
                super().__init__(type)

            @staticmethod
            def create(greycat: Optional[GreyCat] = None) -> std_n.core._nodeTime:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                return std.core.nodeTime(greycat.libs_by_name[std.name_].mapped[8], [])

        @final
        class TimeZone(GreyCat.Enum):
            name_: Final[str] = "core::TimeZone"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            @staticmethod
            def Africa_Accra(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[0]]

            @staticmethod
            def Africa_Bamako(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[1]]

            @staticmethod
            def Africa_Banjul(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[2]]

            @staticmethod
            def Africa_Conakry(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[3]]

            @staticmethod
            def Africa_Dakar(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[4]]

            @staticmethod
            def Africa_Freetown(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[5]]

            @staticmethod
            def Africa_Lome(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[6]]

            @staticmethod
            def Africa_Nouakchott(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[7]]

            @staticmethod
            def Africa_Ouagadougou(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[8]]

            @staticmethod
            def Africa_Timbuktu(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[9]]

            @staticmethod
            def Atlantic_Reykjavik(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[10]]

            @staticmethod
            def Atlantic_St_Helena(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[11]]

            @staticmethod
            def Iceland(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[12]]

            @staticmethod
            def Egypt(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[13]]

            @staticmethod
            def Africa_Maseru(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[14]]

            @staticmethod
            def Africa_Mbabane(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[15]]

            @staticmethod
            def Africa_Bangui(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[16]]

            @staticmethod
            def Africa_Brazzaville(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[17]]

            @staticmethod
            def Africa_Douala(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[18]]

            @staticmethod
            def Africa_Kinshasa(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[19]]

            @staticmethod
            def Africa_Libreville(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[20]]

            @staticmethod
            def Africa_Luanda(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[21]]

            @staticmethod
            def Africa_Malabo(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[22]]

            @staticmethod
            def Africa_Niamey(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[23]]

            @staticmethod
            def Africa_Porto_Novo(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[24]]

            @staticmethod
            def Africa_Blantyre(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[25]]

            @staticmethod
            def Africa_Bujumbura(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[26]]

            @staticmethod
            def Africa_Gaborone(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[27]]

            @staticmethod
            def Africa_Harare(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[28]]

            @staticmethod
            def Africa_Kigali(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[29]]

            @staticmethod
            def Africa_Lubumbashi(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[30]]

            @staticmethod
            def Africa_Lusaka(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[31]]

            @staticmethod
            def Africa_Addis_Ababa(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[32]]

            @staticmethod
            def Africa_Asmara(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[33]]

            @staticmethod
            def Africa_Asmera(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[34]]

            @staticmethod
            def Africa_Dar_es_Salaam(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[35]]

            @staticmethod
            def Africa_Djibouti(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[36]]

            @staticmethod
            def Africa_Kampala(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[37]]

            @staticmethod
            def Africa_Mogadishu(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[38]]

            @staticmethod
            def Indian_Antananarivo(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[39]]

            @staticmethod
            def Indian_Comoro(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[40]]

            @staticmethod
            def Indian_Mayotte(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[41]]

            @staticmethod
            def Libya(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[42]]

            @staticmethod
            def America_Atka(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[43]]

            @staticmethod
            def US_Aleutian(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[44]]

            @staticmethod
            def US_Alaska(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[45]]

            @staticmethod
            def America_Buenos_Aires(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[46]]

            @staticmethod
            def America_Argentina_ComodRivadavia(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[47]]

            @staticmethod
            def America_Catamarca(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[48]]

            @staticmethod
            def America_Cordoba(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[49]]

            @staticmethod
            def America_Rosario(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[50]]

            @staticmethod
            def America_Jujuy(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[51]]

            @staticmethod
            def America_Mendoza(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[52]]

            @staticmethod
            def US_Central(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[53]]

            @staticmethod
            def America_Shiprock(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[54]]

            @staticmethod
            def Navajo(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[55]]

            @staticmethod
            def US_Mountain(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[56]]

            @staticmethod
            def US_Michigan(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[57]]

            @staticmethod
            def America_Yellowknife(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[58]]

            @staticmethod
            def Canada_Mountain(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[59]]

            @staticmethod
            def Canada_Atlantic(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[60]]

            @staticmethod
            def Cuba(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[61]]

            @staticmethod
            def America_Fort_Wayne(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[62]]

            @staticmethod
            def America_Indianapolis(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[63]]

            @staticmethod
            def US_East_Indiana(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[64]]

            @staticmethod
            def America_Knox_IN(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[65]]

            @staticmethod
            def US_Indiana_Starke(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[66]]

            @staticmethod
            def America_Pangnirtung(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[67]]

            @staticmethod
            def Jamaica(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[68]]

            @staticmethod
            def America_Louisville(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[69]]

            @staticmethod
            def US_Pacific(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[70]]

            @staticmethod
            def Brazil_West(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[71]]

            @staticmethod
            def Mexico_BajaSur(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[72]]

            @staticmethod
            def Mexico_General(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[73]]

            @staticmethod
            def US_Eastern(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[74]]

            @staticmethod
            def Brazil_DeNoronha(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[75]]

            @staticmethod
            def America_Godthab(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[76]]

            @staticmethod
            def America_Atikokan(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[77]]

            @staticmethod
            def America_Cayman(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[78]]

            @staticmethod
            def America_Coral_Harbour(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[79]]

            @staticmethod
            def America_Creston(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[80]]

            @staticmethod
            def US_Arizona(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[81]]

            @staticmethod
            def America_Anguilla(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[82]]

            @staticmethod
            def America_Antigua(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[83]]

            @staticmethod
            def America_Aruba(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[84]]

            @staticmethod
            def America_Blanc_Sablon(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[85]]

            @staticmethod
            def America_Curacao(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[86]]

            @staticmethod
            def America_Dominica(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[87]]

            @staticmethod
            def America_Grenada(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[88]]

            @staticmethod
            def America_Guadeloupe(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[89]]

            @staticmethod
            def America_Kralendijk(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[90]]

            @staticmethod
            def America_Lower_Princes(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[91]]

            @staticmethod
            def America_Marigot(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[92]]

            @staticmethod
            def America_Montserrat(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[93]]

            @staticmethod
            def America_Port_of_Spain(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[94]]

            @staticmethod
            def America_St_Barthelemy(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[95]]

            @staticmethod
            def America_St_Kitts(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[96]]

            @staticmethod
            def America_St_Lucia(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[97]]

            @staticmethod
            def America_St_Thomas(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[98]]

            @staticmethod
            def America_St_Vincent(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[99]]

            @staticmethod
            def America_Tortola(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[100]]

            @staticmethod
            def America_Virgin(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[101]]

            @staticmethod
            def Canada_Saskatchewan(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[102]]

            @staticmethod
            def America_Porto_Acre(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[103]]

            @staticmethod
            def Brazil_Acre(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[104]]

            @staticmethod
            def Chile_Continental(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[105]]

            @staticmethod
            def Brazil_East(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[106]]

            @staticmethod
            def Canada_Newfoundland(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[107]]

            @staticmethod
            def America_Ensenada(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[108]]

            @staticmethod
            def America_Santa_Isabel(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[109]]

            @staticmethod
            def Mexico_BajaNorte(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[110]]

            @staticmethod
            def America_Montreal(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[111]]

            @staticmethod
            def America_Nassau(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[112]]

            @staticmethod
            def America_Nipigon(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[113]]

            @staticmethod
            def America_Thunder_Bay(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[114]]

            @staticmethod
            def Canada_Eastern(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[115]]

            @staticmethod
            def Canada_Pacific(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[116]]

            @staticmethod
            def Canada_Yukon(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[117]]

            @staticmethod
            def America_Rainy_River(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[118]]

            @staticmethod
            def Canada_Central(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[119]]

            @staticmethod
            def Asia_Ashkhabad(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[120]]

            @staticmethod
            def Asia_Phnom_Penh(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[121]]

            @staticmethod
            def Asia_Vientiane(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[122]]

            @staticmethod
            def Indian_Christmas(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[123]]

            @staticmethod
            def Asia_Dacca(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[124]]

            @staticmethod
            def Asia_Muscat(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[125]]

            @staticmethod
            def Indian_Mahe(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[126]]

            @staticmethod
            def Indian_Reunion(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[127]]

            @staticmethod
            def Asia_Saigon(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[128]]

            @staticmethod
            def Hongkong(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[129]]

            @staticmethod
            def Asia_Tel_Aviv(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[130]]

            @staticmethod
            def Israel(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[131]]

            @staticmethod
            def Asia_Katmandu(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[132]]

            @staticmethod
            def Asia_Calcutta(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[133]]

            @staticmethod
            def Asia_Brunei(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[134]]

            @staticmethod
            def Asia_Macao(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[135]]

            @staticmethod
            def Asia_Ujung_Pandang(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[136]]

            @staticmethod
            def Europe_Nicosia(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[137]]

            @staticmethod
            def Asia_Bahrain(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[138]]

            @staticmethod
            def Antarctica_Syowa(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[139]]

            @staticmethod
            def Asia_Aden(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[140]]

            @staticmethod
            def Asia_Kuwait(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[141]]

            @staticmethod
            def ROK(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[142]]

            @staticmethod
            def Asia_Chongqing(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[143]]

            @staticmethod
            def Asia_Chungking(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[144]]

            @staticmethod
            def Asia_Harbin(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[145]]

            @staticmethod
            def PRC(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[146]]

            @staticmethod
            def Asia_Kuala_Lumpur(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[147]]

            @staticmethod
            def Singapore(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[148]]

            @staticmethod
            def ROC(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[149]]

            @staticmethod
            def Iran(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[150]]

            @staticmethod
            def Asia_Thimbu(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[151]]

            @staticmethod
            def Japan(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[152]]

            @staticmethod
            def Asia_Ulan_Bator(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[153]]

            @staticmethod
            def Antarctica_Vostok(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[154]]

            @staticmethod
            def Asia_Kashgar(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[155]]

            @staticmethod
            def Asia_Rangoon(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[156]]

            @staticmethod
            def Indian_Cocos(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[157]]

            @staticmethod
            def Atlantic_Faeroe(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[158]]

            @staticmethod
            def Australia_South(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[159]]

            @staticmethod
            def Australia_Queensland(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[160]]

            @staticmethod
            def Australia_Yancowinna(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[161]]

            @staticmethod
            def Australia_North(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[162]]

            @staticmethod
            def Australia_Currie(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[163]]

            @staticmethod
            def Australia_Tasmania(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[164]]

            @staticmethod
            def Australia_LHI(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[165]]

            @staticmethod
            def Australia_Victoria(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[166]]

            @staticmethod
            def Australia_West(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[167]]

            @staticmethod
            def Australia_ACT(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[168]]

            @staticmethod
            def Australia_Canberra(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[169]]

            @staticmethod
            def Australia_NSW(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[170]]

            @staticmethod
            def GMT(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[171]]

            @staticmethod
            def GMTx0(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[172]]

            @staticmethod
            def GMT_0(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[173]]

            @staticmethod
            def GMT0(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[174]]

            @staticmethod
            def Greenwich(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[175]]

            @staticmethod
            def UCT(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[176]]

            @staticmethod
            def UTC(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[177]]

            @staticmethod
            def Universal(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[178]]

            @staticmethod
            def Zulu(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[179]]

            @staticmethod
            def Europe_Ljubljana(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[180]]

            @staticmethod
            def Europe_Podgorica(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[181]]

            @staticmethod
            def Europe_Sarajevo(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[182]]

            @staticmethod
            def Europe_Skopje(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[183]]

            @staticmethod
            def Europe_Zagreb(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[184]]

            @staticmethod
            def Arctic_Longyearbyen(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[185]]

            @staticmethod
            def Atlantic_Jan_Mayen(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[186]]

            @staticmethod
            def Europe_Copenhagen(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[187]]

            @staticmethod
            def Europe_Oslo(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[188]]

            @staticmethod
            def Europe_Stockholm(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[189]]

            @staticmethod
            def Europe_Amsterdam(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[190]]

            @staticmethod
            def Europe_Luxembourg(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[191]]

            @staticmethod
            def Europe_Tiraspol(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[192]]

            @staticmethod
            def Eire(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[193]]

            @staticmethod
            def Europe_Mariehamn(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[194]]

            @staticmethod
            def Asia_Istanbul(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[195]]

            @staticmethod
            def Turkey(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[196]]

            @staticmethod
            def Europe_Kiev(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[197]]

            @staticmethod
            def Europe_Uzhgorod(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[198]]

            @staticmethod
            def Europe_Zaporozhye(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[199]]

            @staticmethod
            def Portugal(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[200]]

            @staticmethod
            def Europe_Belfast(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[201]]

            @staticmethod
            def Europe_Guernsey(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[202]]

            @staticmethod
            def Europe_Isle_of_Man(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[203]]

            @staticmethod
            def Europe_Jersey(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[204]]

            @staticmethod
            def GB(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[205]]

            @staticmethod
            def GB_Eire(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[206]]

            @staticmethod
            def W_SU(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[207]]

            @staticmethod
            def Europe_Monaco(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[208]]

            @staticmethod
            def Europe_Bratislava(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[209]]

            @staticmethod
            def Europe_San_Marino(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[210]]

            @staticmethod
            def Europe_Vatican(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[211]]

            @staticmethod
            def Poland(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[212]]

            @staticmethod
            def Europe_Busingen(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[213]]

            @staticmethod
            def Europe_Vaduz(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[214]]

            @staticmethod
            def Indian_Kerguelen(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[215]]

            @staticmethod
            def Antarctica_McMurdo(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[216]]

            @staticmethod
            def Antarctica_South_Pole(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[217]]

            @staticmethod
            def NZ(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[218]]

            @staticmethod
            def NZ_CHAT(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[219]]

            @staticmethod
            def Chile_EasterIsland(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[220]]

            @staticmethod
            def Pacific_Pohnpei(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[221]]

            @staticmethod
            def Pacific_Ponape(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[222]]

            @staticmethod
            def Pacific_Saipan(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[223]]

            @staticmethod
            def Pacific_Johnston(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[224]]

            @staticmethod
            def US_Hawaii(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[225]]

            @staticmethod
            def Pacific_Enderbury(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[226]]

            @staticmethod
            def Kwajalein(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[227]]

            @staticmethod
            def Pacific_Midway(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[228]]

            @staticmethod
            def Pacific_Samoa(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[229]]

            @staticmethod
            def US_Samoa(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[230]]

            @staticmethod
            def Antarctica_DumontDUrville(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[231]]

            @staticmethod
            def Pacific_Chuuk(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[232]]

            @staticmethod
            def Pacific_Truk(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[233]]

            @staticmethod
            def Pacific_Yap(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[234]]

            @staticmethod
            def Pacific_Funafuti(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[235]]

            @staticmethod
            def Pacific_Majuro(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[236]]

            @staticmethod
            def Pacific_Wake(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[237]]

            @staticmethod
            def Pacific_Wallis(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[238]]

            @staticmethod
            def Africa_Abidjan(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[239]]

            @staticmethod
            def Africa_Algiers(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[240]]

            @staticmethod
            def Africa_Bissau(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[241]]

            @staticmethod
            def Africa_Cairo(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[242]]

            @staticmethod
            def Africa_Casablanca(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[243]]

            @staticmethod
            def Africa_Ceuta(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[244]]

            @staticmethod
            def Africa_El_Aaiun(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[245]]

            @staticmethod
            def Africa_Johannesburg(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[246]]

            @staticmethod
            def Africa_Juba(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[247]]

            @staticmethod
            def Africa_Khartoum(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[248]]

            @staticmethod
            def Africa_Lagos(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[249]]

            @staticmethod
            def Africa_Maputo(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[250]]

            @staticmethod
            def Africa_Monrovia(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[251]]

            @staticmethod
            def Africa_Nairobi(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[252]]

            @staticmethod
            def Africa_Ndjamena(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[253]]

            @staticmethod
            def Africa_Sao_Tome(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[254]]

            @staticmethod
            def Africa_Tripoli(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[255]]

            @staticmethod
            def Africa_Tunis(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[256]]

            @staticmethod
            def Africa_Windhoek(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[257]]

            @staticmethod
            def America_Adak(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[258]]

            @staticmethod
            def America_Anchorage(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[259]]

            @staticmethod
            def America_Araguaina(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[260]]

            @staticmethod
            def America_Argentina_Buenos_Aires(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[261]]

            @staticmethod
            def America_Argentina_Catamarca(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[262]]

            @staticmethod
            def America_Argentina_Cordoba(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[263]]

            @staticmethod
            def America_Argentina_Jujuy(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[264]]

            @staticmethod
            def America_Argentina_La_Rioja(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[265]]

            @staticmethod
            def America_Argentina_Mendoza(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[266]]

            @staticmethod
            def America_Argentina_Rio_Gallegos(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[267]]

            @staticmethod
            def America_Argentina_Salta(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[268]]

            @staticmethod
            def America_Argentina_San_Juan(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[269]]

            @staticmethod
            def America_Argentina_San_Luis(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[270]]

            @staticmethod
            def America_Argentina_Tucuman(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[271]]

            @staticmethod
            def America_Argentina_Ushuaia(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[272]]

            @staticmethod
            def America_Asuncion(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[273]]

            @staticmethod
            def America_Bahia(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[274]]

            @staticmethod
            def America_Bahia_Banderas(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[275]]

            @staticmethod
            def America_Barbados(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[276]]

            @staticmethod
            def America_Belem(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[277]]

            @staticmethod
            def America_Belize(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[278]]

            @staticmethod
            def America_Boa_Vista(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[279]]

            @staticmethod
            def America_Bogota(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[280]]

            @staticmethod
            def America_Boise(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[281]]

            @staticmethod
            def America_Cambridge_Bay(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[282]]

            @staticmethod
            def America_Campo_Grande(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[283]]

            @staticmethod
            def America_Cancun(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[284]]

            @staticmethod
            def America_Caracas(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[285]]

            @staticmethod
            def America_Cayenne(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[286]]

            @staticmethod
            def America_Chicago(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[287]]

            @staticmethod
            def America_Chihuahua(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[288]]

            @staticmethod
            def America_Ciudad_Juarez(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[289]]

            @staticmethod
            def America_Costa_Rica(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[290]]

            @staticmethod
            def America_Cuiaba(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[291]]

            @staticmethod
            def America_Danmarkshavn(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[292]]

            @staticmethod
            def America_Dawson(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[293]]

            @staticmethod
            def America_Dawson_Creek(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[294]]

            @staticmethod
            def America_Denver(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[295]]

            @staticmethod
            def America_Detroit(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[296]]

            @staticmethod
            def America_Edmonton(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[297]]

            @staticmethod
            def America_Eirunepe(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[298]]

            @staticmethod
            def America_El_Salvador(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[299]]

            @staticmethod
            def America_Fort_Nelson(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[300]]

            @staticmethod
            def America_Fortaleza(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[301]]

            @staticmethod
            def America_Glace_Bay(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[302]]

            @staticmethod
            def America_Goose_Bay(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[303]]

            @staticmethod
            def America_Grand_Turk(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[304]]

            @staticmethod
            def America_Guatemala(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[305]]

            @staticmethod
            def America_Guayaquil(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[306]]

            @staticmethod
            def America_Guyana(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[307]]

            @staticmethod
            def America_Halifax(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[308]]

            @staticmethod
            def America_Havana(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[309]]

            @staticmethod
            def America_Hermosillo(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[310]]

            @staticmethod
            def America_Indiana_Indianapolis(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[311]]

            @staticmethod
            def America_Indiana_Knox(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[312]]

            @staticmethod
            def America_Indiana_Marengo(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[313]]

            @staticmethod
            def America_Indiana_Petersburg(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[314]]

            @staticmethod
            def America_Indiana_Tell_City(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[315]]

            @staticmethod
            def America_Indiana_Vevay(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[316]]

            @staticmethod
            def America_Indiana_Vincennes(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[317]]

            @staticmethod
            def America_Indiana_Winamac(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[318]]

            @staticmethod
            def America_Inuvik(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[319]]

            @staticmethod
            def America_Iqaluit(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[320]]

            @staticmethod
            def America_Jamaica(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[321]]

            @staticmethod
            def America_Juneau(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[322]]

            @staticmethod
            def America_Kentucky_Louisville(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[323]]

            @staticmethod
            def America_Kentucky_Monticello(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[324]]

            @staticmethod
            def America_La_Paz(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[325]]

            @staticmethod
            def America_Lima(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[326]]

            @staticmethod
            def America_Los_Angeles(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[327]]

            @staticmethod
            def America_Maceio(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[328]]

            @staticmethod
            def America_Managua(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[329]]

            @staticmethod
            def America_Manaus(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[330]]

            @staticmethod
            def America_Martinique(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[331]]

            @staticmethod
            def America_Matamoros(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[332]]

            @staticmethod
            def America_Mazatlan(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[333]]

            @staticmethod
            def America_Menominee(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[334]]

            @staticmethod
            def America_Merida(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[335]]

            @staticmethod
            def America_Metlakatla(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[336]]

            @staticmethod
            def America_Mexico_City(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[337]]

            @staticmethod
            def America_Miquelon(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[338]]

            @staticmethod
            def America_Moncton(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[339]]

            @staticmethod
            def America_Monterrey(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[340]]

            @staticmethod
            def America_Montevideo(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[341]]

            @staticmethod
            def America_New_York(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[342]]

            @staticmethod
            def America_Nome(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[343]]

            @staticmethod
            def America_Noronha(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[344]]

            @staticmethod
            def America_North_Dakota_Beulah(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[345]]

            @staticmethod
            def America_North_Dakota_Center(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[346]]

            @staticmethod
            def America_North_Dakota_New_Salem(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[347]]

            @staticmethod
            def America_Nuuk(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[348]]

            @staticmethod
            def America_Ojinaga(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[349]]

            @staticmethod
            def America_Panama(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[350]]

            @staticmethod
            def America_Paramaribo(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[351]]

            @staticmethod
            def America_Phoenix(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[352]]

            @staticmethod
            def America_Port_au_Prince(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[353]]

            @staticmethod
            def America_Porto_Velho(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[354]]

            @staticmethod
            def America_Puerto_Rico(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[355]]

            @staticmethod
            def America_Punta_Arenas(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[356]]

            @staticmethod
            def America_Rankin_Inlet(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[357]]

            @staticmethod
            def America_Recife(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[358]]

            @staticmethod
            def America_Regina(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[359]]

            @staticmethod
            def America_Resolute(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[360]]

            @staticmethod
            def America_Rio_Branco(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[361]]

            @staticmethod
            def America_Santarem(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[362]]

            @staticmethod
            def America_Santiago(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[363]]

            @staticmethod
            def America_Santo_Domingo(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[364]]

            @staticmethod
            def America_Sao_Paulo(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[365]]

            @staticmethod
            def America_Scoresbysund(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[366]]

            @staticmethod
            def America_Sitka(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[367]]

            @staticmethod
            def America_St_Johns(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[368]]

            @staticmethod
            def America_Swift_Current(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[369]]

            @staticmethod
            def America_Tegucigalpa(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[370]]

            @staticmethod
            def America_Thule(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[371]]

            @staticmethod
            def America_Tijuana(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[372]]

            @staticmethod
            def America_Toronto(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[373]]

            @staticmethod
            def America_Vancouver(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[374]]

            @staticmethod
            def America_Whitehorse(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[375]]

            @staticmethod
            def America_Winnipeg(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[376]]

            @staticmethod
            def America_Yakutat(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[377]]

            @staticmethod
            def Antarctica_Casey(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[378]]

            @staticmethod
            def Antarctica_Davis(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[379]]

            @staticmethod
            def Antarctica_Macquarie(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[380]]

            @staticmethod
            def Antarctica_Mawson(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[381]]

            @staticmethod
            def Antarctica_Palmer(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[382]]

            @staticmethod
            def Antarctica_Rothera(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[383]]

            @staticmethod
            def Antarctica_Troll(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[384]]

            @staticmethod
            def Asia_Almaty(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[385]]

            @staticmethod
            def Asia_Amman(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[386]]

            @staticmethod
            def Asia_Anadyr(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[387]]

            @staticmethod
            def Asia_Aqtau(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[388]]

            @staticmethod
            def Asia_Aqtobe(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[389]]

            @staticmethod
            def Asia_Ashgabat(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[390]]

            @staticmethod
            def Asia_Atyrau(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[391]]

            @staticmethod
            def Asia_Baghdad(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[392]]

            @staticmethod
            def Asia_Baku(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[393]]

            @staticmethod
            def Asia_Bangkok(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[394]]

            @staticmethod
            def Asia_Barnaul(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[395]]

            @staticmethod
            def Asia_Beirut(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[396]]

            @staticmethod
            def Asia_Bishkek(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[397]]

            @staticmethod
            def Asia_Chita(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[398]]

            @staticmethod
            def Asia_Choibalsan(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[399]]

            @staticmethod
            def Asia_Colombo(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[400]]

            @staticmethod
            def Asia_Damascus(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[401]]

            @staticmethod
            def Asia_Dhaka(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[402]]

            @staticmethod
            def Asia_Dili(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[403]]

            @staticmethod
            def Asia_Dubai(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[404]]

            @staticmethod
            def Asia_Dushanbe(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[405]]

            @staticmethod
            def Asia_Famagusta(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[406]]

            @staticmethod
            def Asia_Gaza(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[407]]

            @staticmethod
            def Asia_Hebron(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[408]]

            @staticmethod
            def Asia_Ho_Chi_Minh(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[409]]

            @staticmethod
            def Asia_Hong_Kong(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[410]]

            @staticmethod
            def Asia_Hovd(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[411]]

            @staticmethod
            def Asia_Irkutsk(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[412]]

            @staticmethod
            def Asia_Jakarta(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[413]]

            @staticmethod
            def Asia_Jayapura(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[414]]

            @staticmethod
            def Asia_Jerusalem(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[415]]

            @staticmethod
            def Asia_Kabul(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[416]]

            @staticmethod
            def Asia_Kamchatka(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[417]]

            @staticmethod
            def Asia_Karachi(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[418]]

            @staticmethod
            def Asia_Kathmandu(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[419]]

            @staticmethod
            def Asia_Khandyga(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[420]]

            @staticmethod
            def Asia_Kolkata(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[421]]

            @staticmethod
            def Asia_Krasnoyarsk(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[422]]

            @staticmethod
            def Asia_Kuching(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[423]]

            @staticmethod
            def Asia_Macau(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[424]]

            @staticmethod
            def Asia_Magadan(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[425]]

            @staticmethod
            def Asia_Makassar(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[426]]

            @staticmethod
            def Asia_Manila(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[427]]

            @staticmethod
            def Asia_Nicosia(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[428]]

            @staticmethod
            def Asia_Novokuznetsk(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[429]]

            @staticmethod
            def Asia_Novosibirsk(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[430]]

            @staticmethod
            def Asia_Omsk(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[431]]

            @staticmethod
            def Asia_Oral(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[432]]

            @staticmethod
            def Asia_Pontianak(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[433]]

            @staticmethod
            def Asia_Pyongyang(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[434]]

            @staticmethod
            def Asia_Qatar(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[435]]

            @staticmethod
            def Asia_Qostanay(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[436]]

            @staticmethod
            def Asia_Qyzylorda(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[437]]

            @staticmethod
            def Asia_Riyadh(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[438]]

            @staticmethod
            def Asia_Sakhalin(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[439]]

            @staticmethod
            def Asia_Samarkand(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[440]]

            @staticmethod
            def Asia_Seoul(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[441]]

            @staticmethod
            def Asia_Shanghai(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[442]]

            @staticmethod
            def Asia_Singapore(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[443]]

            @staticmethod
            def Asia_Srednekolymsk(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[444]]

            @staticmethod
            def Asia_Taipei(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[445]]

            @staticmethod
            def Asia_Tashkent(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[446]]

            @staticmethod
            def Asia_Tbilisi(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[447]]

            @staticmethod
            def Asia_Tehran(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[448]]

            @staticmethod
            def Asia_Thimphu(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[449]]

            @staticmethod
            def Asia_Tokyo(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[450]]

            @staticmethod
            def Asia_Tomsk(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[451]]

            @staticmethod
            def Asia_Ulaanbaatar(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[452]]

            @staticmethod
            def Asia_Urumqi(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[453]]

            @staticmethod
            def Asia_Ust_Nera(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[454]]

            @staticmethod
            def Asia_Vladivostok(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[455]]

            @staticmethod
            def Asia_Yakutsk(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[456]]

            @staticmethod
            def Asia_Yangon(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[457]]

            @staticmethod
            def Asia_Yekaterinburg(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[458]]

            @staticmethod
            def Asia_Yerevan(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[459]]

            @staticmethod
            def Atlantic_Azores(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[460]]

            @staticmethod
            def Atlantic_Bermuda(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[461]]

            @staticmethod
            def Atlantic_Canary(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[462]]

            @staticmethod
            def Atlantic_Cape_Verde(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[463]]

            @staticmethod
            def Atlantic_Faroe(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[464]]

            @staticmethod
            def Atlantic_Madeira(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[465]]

            @staticmethod
            def Atlantic_South_Georgia(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[466]]

            @staticmethod
            def Atlantic_Stanley(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[467]]

            @staticmethod
            def Australia_Adelaide(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[468]]

            @staticmethod
            def Australia_Brisbane(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[469]]

            @staticmethod
            def Australia_Broken_Hill(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[470]]

            @staticmethod
            def Australia_Darwin(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[471]]

            @staticmethod
            def Australia_Eucla(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[472]]

            @staticmethod
            def Australia_Hobart(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[473]]

            @staticmethod
            def Australia_Lindeman(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[474]]

            @staticmethod
            def Australia_Lord_Howe(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[475]]

            @staticmethod
            def Australia_Melbourne(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[476]]

            @staticmethod
            def Australia_Perth(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[477]]

            @staticmethod
            def Australia_Sydney(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[478]]

            @staticmethod
            def CET(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[479]]

            @staticmethod
            def CST6CDT(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[480]]

            @staticmethod
            def EET(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[481]]

            @staticmethod
            def EST(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[482]]

            @staticmethod
            def EST5EDT(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[483]]

            @staticmethod
            def Europe_Andorra(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[484]]

            @staticmethod
            def Europe_Astrakhan(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[485]]

            @staticmethod
            def Europe_Athens(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[486]]

            @staticmethod
            def Europe_Belgrade(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[487]]

            @staticmethod
            def Europe_Berlin(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[488]]

            @staticmethod
            def Europe_Brussels(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[489]]

            @staticmethod
            def Europe_Bucharest(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[490]]

            @staticmethod
            def Europe_Budapest(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[491]]

            @staticmethod
            def Europe_Chisinau(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[492]]

            @staticmethod
            def Europe_Dublin(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[493]]

            @staticmethod
            def Europe_Gibraltar(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[494]]

            @staticmethod
            def Europe_Helsinki(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[495]]

            @staticmethod
            def Europe_Istanbul(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[496]]

            @staticmethod
            def Europe_Kaliningrad(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[497]]

            @staticmethod
            def Europe_Kirov(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[498]]

            @staticmethod
            def Europe_Kyiv(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[499]]

            @staticmethod
            def Europe_Lisbon(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[500]]

            @staticmethod
            def Europe_London(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[501]]

            @staticmethod
            def Europe_Madrid(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[502]]

            @staticmethod
            def Europe_Malta(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[503]]

            @staticmethod
            def Europe_Minsk(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[504]]

            @staticmethod
            def Europe_Moscow(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[505]]

            @staticmethod
            def Europe_Paris(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[506]]

            @staticmethod
            def Europe_Prague(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[507]]

            @staticmethod
            def Europe_Riga(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[508]]

            @staticmethod
            def Europe_Rome(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[509]]

            @staticmethod
            def Europe_Samara(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[510]]

            @staticmethod
            def Europe_Saratov(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[511]]

            @staticmethod
            def Europe_Simferopol(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[512]]

            @staticmethod
            def Europe_Sofia(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[513]]

            @staticmethod
            def Europe_Tallinn(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[514]]

            @staticmethod
            def Europe_Tirane(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[515]]

            @staticmethod
            def Europe_Ulyanovsk(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[516]]

            @staticmethod
            def Europe_Vienna(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[517]]

            @staticmethod
            def Europe_Vilnius(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[518]]

            @staticmethod
            def Europe_Volgograd(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[519]]

            @staticmethod
            def Europe_Warsaw(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[520]]

            @staticmethod
            def Europe_Zurich(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[521]]

            @staticmethod
            def Factory(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[522]]

            @staticmethod
            def HST(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[523]]

            @staticmethod
            def Indian_Chagos(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[524]]

            @staticmethod
            def Indian_Maldives(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[525]]

            @staticmethod
            def Indian_Mauritius(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[526]]

            @staticmethod
            def MET(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[527]]

            @staticmethod
            def MST(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[528]]

            @staticmethod
            def MST7MDT(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[529]]

            @staticmethod
            def PST8PDT(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[530]]

            @staticmethod
            def Pacific_Apia(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[531]]

            @staticmethod
            def Pacific_Auckland(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[532]]

            @staticmethod
            def Pacific_Bougainville(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[533]]

            @staticmethod
            def Pacific_Chatham(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[534]]

            @staticmethod
            def Pacific_Easter(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[535]]

            @staticmethod
            def Pacific_Efate(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[536]]

            @staticmethod
            def Pacific_Fakaofo(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[537]]

            @staticmethod
            def Pacific_Fiji(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[538]]

            @staticmethod
            def Pacific_Galapagos(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[539]]

            @staticmethod
            def Pacific_Gambier(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[540]]

            @staticmethod
            def Pacific_Guadalcanal(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[541]]

            @staticmethod
            def Pacific_Guam(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[542]]

            @staticmethod
            def Pacific_Honolulu(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[543]]

            @staticmethod
            def Pacific_Kanton(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[544]]

            @staticmethod
            def Pacific_Kiritimati(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[545]]

            @staticmethod
            def Pacific_Kosrae(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[546]]

            @staticmethod
            def Pacific_Kwajalein(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[547]]

            @staticmethod
            def Pacific_Marquesas(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[548]]

            @staticmethod
            def Pacific_Nauru(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[549]]

            @staticmethod
            def Pacific_Niue(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[550]]

            @staticmethod
            def Pacific_Norfolk(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[551]]

            @staticmethod
            def Pacific_Noumea(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[552]]

            @staticmethod
            def Pacific_Pago_Pago(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[553]]

            @staticmethod
            def Pacific_Palau(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[554]]

            @staticmethod
            def Pacific_Pitcairn(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[555]]

            @staticmethod
            def Pacific_Port_Moresby(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[556]]

            @staticmethod
            def Pacific_Rarotonga(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[557]]

            @staticmethod
            def Pacific_Tahiti(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[558]]

            @staticmethod
            def Pacific_Tarawa(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[559]]

            @staticmethod
            def Pacific_Tongatapu(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[560]]

            @staticmethod
            def WET(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[9]
                return t.enum_values[t.generated_offsets[561]]

            @staticmethod
            def create(greycat: Optional[GreyCat] = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                return std.core.TimeZone(greycat.libs_by_name[std.name_].mapped[9], [])

        @final
        class Table(Generic[__T], std_n.core._Table[__T]):
            name_: Final[str] = "core::Table"

            def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
                super().__init__(type)

            @staticmethod
            def create(greycat: Optional[GreyCat] = None) -> std_n.core._Table:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                return std.core.Table(greycat.libs_by_name[std.name_].mapped[10], [])

        @final
        class ti10d(std_n.core._ti10d):
            name_: Final[str] = "core::ti10d"

            def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
                super().__init__(type)

            @staticmethod
            def create(greycat: Optional[GreyCat] = None) -> std_n.core._ti10d:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                return std.core.ti10d(greycat.libs_by_name[std.name_].mapped[11], [])

        @final
        class duration(std_n.core._duration):
            name_: Final[str] = "core::duration"

            def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
                super().__init__(type)

            @staticmethod
            def create(greycat: Optional[GreyCat] = None) -> std_n.core._duration:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                return std.core.duration(greycat.libs_by_name[std.name_].mapped[12], [])

        @final
        class DurationUnit(GreyCat.Enum):
            name_: Final[str] = "core::DurationUnit"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            @staticmethod
            def microseconds(greycat: Optional[GreyCat] = None) -> std.core.DurationUnit:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[13]
                return t.enum_values[t.generated_offsets[0]]

            @staticmethod
            def milliseconds(greycat: Optional[GreyCat] = None) -> std.core.DurationUnit:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[13]
                return t.enum_values[t.generated_offsets[1]]

            @staticmethod
            def seconds(greycat: Optional[GreyCat] = None) -> std.core.DurationUnit:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[13]
                return t.enum_values[t.generated_offsets[2]]

            @staticmethod
            def minutes(greycat: Optional[GreyCat] = None) -> std.core.DurationUnit:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[13]
                return t.enum_values[t.generated_offsets[3]]

            @staticmethod
            def hours(greycat: Optional[GreyCat] = None) -> std.core.DurationUnit:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[13]
                return t.enum_values[t.generated_offsets[4]]

            @staticmethod
            def days(greycat: Optional[GreyCat] = None) -> std.core.DurationUnit:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[13]
                return t.enum_values[t.generated_offsets[5]]

            @staticmethod
            def weeks(greycat: Optional[GreyCat] = None) -> std.core.DurationUnit:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[13]
                return t.enum_values[t.generated_offsets[6]]

            @staticmethod
            def months(greycat: Optional[GreyCat] = None) -> std.core.DurationUnit:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[13]
                return t.enum_values[t.generated_offsets[7]]

            @staticmethod
            def years(greycat: Optional[GreyCat] = None) -> std.core.DurationUnit:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[13]
                return t.enum_values[t.generated_offsets[8]]

            @staticmethod
            def create(greycat: Optional[GreyCat] = None) -> std.core.DurationUnit:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                return std.core.DurationUnit(greycat.libs_by_name[std.name_].mapped[13], [])

        @final
        class Tensor(std_n.core._Tensor):
            name_: Final[str] = "core::Tensor"

            def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
                super().__init__(type)

            @staticmethod
            def create(greycat: Optional[GreyCat] = None) -> std_n.core._Tensor:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                return std.core.Tensor(greycat.libs_by_name[std.name_].mapped[14], [])

        @final
        class nodeIndex(Generic[__K, __V], std_n.core._nodeIndex[__K, __V]):
            name_: Final[str] = "core::nodeIndex"

            def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
                super().__init__(type)

            @staticmethod
            def create(greycat: Optional[GreyCat] = None) -> std_n.core._nodeIndex:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                return std.core.nodeIndex(greycat.libs_by_name[std.name_].mapped[15], [])

        @final
        class TableColumnMapping(GreyCat.Object):
            name_: Final[str] = "core::TableColumnMapping"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def column(self) -> int:
                return self._get(self.type_.generated_offsets[0])

            def set_column(self, v: int) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def extractors(self) -> std.core.Array:
                return self._get(self.type_.generated_offsets[1])

            def set_extractors(self, v: std.core.Array) -> None:
                self._set(self.type_.generated_offsets[1], v)

            @staticmethod
            def create(column: int, extractors: std.core.Array, greycat: Optional[GreyCat] = None) -> std.core.TableColumnMapping:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                return std.core.TableColumnMapping(greycat.libs_by_name[std.name_].mapped[16], [column, extractors])

        @final
        class nodeList(Generic[__T], std_n.core._nodeList[__T]):
            name_: Final[str] = "core::nodeList"

            def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
                super().__init__(type)

            @staticmethod
            def create(greycat: Optional[GreyCat] = None) -> std_n.core._nodeList:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                return std.core.nodeList(greycat.libs_by_name[std.name_].mapped[17], [])

        @final
        class TensorType(GreyCat.Enum):
            name_: Final[str] = "core::TensorType"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            @staticmethod
            def i32(greycat: Optional[GreyCat] = None) -> std.core.TensorType:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[18]
                return t.enum_values[t.generated_offsets[0]]

            @staticmethod
            def i64(greycat: Optional[GreyCat] = None) -> std.core.TensorType:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[18]
                return t.enum_values[t.generated_offsets[1]]

            @staticmethod
            def f32(greycat: Optional[GreyCat] = None) -> std.core.TensorType:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[18]
                return t.enum_values[t.generated_offsets[2]]

            @staticmethod
            def f64(greycat: Optional[GreyCat] = None) -> std.core.TensorType:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[18]
                return t.enum_values[t.generated_offsets[3]]

            @staticmethod
            def c64(greycat: Optional[GreyCat] = None) -> std.core.TensorType:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[18]
                return t.enum_values[t.generated_offsets[4]]

            @staticmethod
            def c128(greycat: Optional[GreyCat] = None) -> std.core.TensorType:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[18]
                return t.enum_values[t.generated_offsets[5]]

            @staticmethod
            def create(greycat: Optional[GreyCat] = None) -> std.core.TensorType:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                return std.core.TensorType(greycat.libs_by_name[std.name_].mapped[18], [])

        @final
        class Tuple(Generic[__T, __U], GreyCat.Object):
            name_: Final[str] = "core::Tuple"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def x(self) -> std.core.__T:
                return self._get(self.type_.generated_offsets[0])

            def set_x(self, v: std.core.__T) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def y(self) -> std.core.__U:
                return self._get(self.type_.generated_offsets[1])

            def set_y(self, v: std.core.__U) -> None:
                self._set(self.type_.generated_offsets[1], v)

            @staticmethod
            def create(x: std.core.__T, y: std.core.__U, greycat: Optional[GreyCat] = None) -> std.core.Tuple[TypeVar("T"), TypeVar("U")]:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                return std.core.Tuple(greycat.libs_by_name[std.name_].mapped[19], [x, y])

        @final
        class ti2d(std_n.core._ti2d):
            name_: Final[str] = "core::ti2d"

            def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
                super().__init__(type)

            @staticmethod
            def create(greycat: Optional[GreyCat] = None) -> std_n.core._ti2d:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                return std.core.ti2d(greycat.libs_by_name[std.name_].mapped[20], [])

        @final
        class tf4d(std_n.core._tf4d):
            name_: Final[str] = "core::tf4d"

            def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
                super().__init__(type)

            @staticmethod
            def create(greycat: Optional[GreyCat] = None) -> std_n.core._tf4d:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                return std.core.tf4d(greycat.libs_by_name[std.name_].mapped[21], [])

        @final
        class DatePart(GreyCat.Enum):
            name_: Final[str] = "core::DatePart"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            @staticmethod
            def years(greycat: Optional[GreyCat] = None) -> std.core.DatePart:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[22]
                return t.enum_values[t.generated_offsets[0]]

            @staticmethod
            def months(greycat: Optional[GreyCat] = None) -> std.core.DatePart:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[22]
                return t.enum_values[t.generated_offsets[1]]

            @staticmethod
            def days(greycat: Optional[GreyCat] = None) -> std.core.DatePart:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[22]
                return t.enum_values[t.generated_offsets[2]]

            @staticmethod
            def hours(greycat: Optional[GreyCat] = None) -> std.core.DatePart:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[22]
                return t.enum_values[t.generated_offsets[3]]

            @staticmethod
            def minutes(greycat: Optional[GreyCat] = None) -> std.core.DatePart:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[22]
                return t.enum_values[t.generated_offsets[4]]

            @staticmethod
            def seconds(greycat: Optional[GreyCat] = None) -> std.core.DatePart:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[22]
                return t.enum_values[t.generated_offsets[5]]

            @staticmethod
            def microseconds(greycat: Optional[GreyCat] = None) -> std.core.DatePart:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[22]
                return t.enum_values[t.generated_offsets[6]]

            @staticmethod
            def create(greycat: Optional[GreyCat] = None) -> std.core.DatePart:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                return std.core.DatePart(greycat.libs_by_name[std.name_].mapped[22], [])

        @final
        class function(std_n.core._function):
            name_: Final[str] = "core::function"

            def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
                super().__init__(type)

            @staticmethod
            def create(greycat: Optional[GreyCat] = None) -> std_n.core._function:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                return std.core.function(greycat.libs_by_name[std.name_].mapped[23], [])

        @final
        class ti3d(std_n.core._ti3d):
            name_: Final[str] = "core::ti3d"

            def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
                super().__init__(type)

            @staticmethod
            def create(greycat: Optional[GreyCat] = None) -> std_n.core._ti3d:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                return std.core.ti3d(greycat.libs_by_name[std.name_].mapped[24], [])

        @final
        class TableColumnMeta(GreyCat.Object):
            name_: Final[str] = "core::TableColumnMeta"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def type(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_type(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def size(self) -> int:
                return self._get(self.type_.generated_offsets[1])

            def set_size(self, v: int) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def index(self) -> bool:
                return self._get(self.type_.generated_offsets[2])

            def set_index(self, v: bool) -> None:
                self._set(self.type_.generated_offsets[2], v)

            def header(self) -> str:
                return self._get(self.type_.generated_offsets[3])

            def set_header(self, v: str) -> None:
                self._set(self.type_.generated_offsets[3], v)

            def min(self) -> Any:
                return self._get(self.type_.generated_offsets[4])

            def set_min(self, v: Any) -> None:
                self._set(self.type_.generated_offsets[4], v)

            def max(self) -> Any:
                return self._get(self.type_.generated_offsets[5])

            def set_max(self, v: Any) -> None:
                self._set(self.type_.generated_offsets[5], v)

            def avg(self) -> Any:
                return self._get(self.type_.generated_offsets[6])

            def set_avg(self, v: Any) -> None:
                self._set(self.type_.generated_offsets[6], v)

            def std(self) -> Any:
                return self._get(self.type_.generated_offsets[7])

            def set_std(self, v: Any) -> None:
                self._set(self.type_.generated_offsets[7], v)

            @staticmethod
            def create(type: str, size: int, index: bool, header: str, min: Any, max: Any, avg: Any, std: Any, greycat: Optional[GreyCat] = None) -> std.core.TableColumnMeta:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                return std.core.TableColumnMeta(greycat.libs_by_name[std.name_].mapped[25], [type, size, index, header, min, max, avg, std])

        @final
        class nodeGeo(Generic[__T], std_n.core._nodeGeo[__T]):
            name_: Final[str] = "core::nodeGeo"

            def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
                super().__init__(type)

            @staticmethod
            def create(greycat: Optional[GreyCat] = None) -> std_n.core._nodeGeo:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                return std.core.nodeGeo(greycat.libs_by_name[std.name_].mapped[26], [])

        @final
        class node(Generic[__T], std_n.core._node[__T]):
            name_: Final[str] = "core::node"

            def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
                super().__init__(type)

            @staticmethod
            def create(greycat: Optional[GreyCat] = None) -> std_n.core._node:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                return std.core.node(greycat.libs_by_name[std.name_].mapped[27], [])

        @final
        class tf3d(std_n.core._tf3d):
            name_: Final[str] = "core::tf3d"

            def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
                super().__init__(type)

            @staticmethod
            def create(greycat: Optional[GreyCat] = None) -> std_n.core._tf3d:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                return std.core.tf3d(greycat.libs_by_name[std.name_].mapped[28], [])

        @final
        class nodeIndexBucket(std_n.core._nodeIndexBucket):
            name_: Final[str] = "core::nodeIndexBucket"

            def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
                super().__init__(type)

            @staticmethod
            def create(greycat: Optional[GreyCat] = None) -> std_n.core._nodeIndexBucket:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                return std.core.nodeIndexBucket(greycat.libs_by_name[std.name_].mapped[29], [])

        @final
        class time(std_n.core._time):
            name_: Final[str] = "core::time"

            def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
                super().__init__(type)

            @staticmethod
            def create(greycat: Optional[GreyCat] = None) -> std_n.core._time:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                return std.core.time(greycat.libs_by_name[std.name_].mapped[30], [])

        @final
        class SamplingMode(GreyCat.Enum):
            name_: Final[str] = "core::SamplingMode"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            @staticmethod
            def fixed(greycat: Optional[GreyCat] = None) -> std.core.SamplingMode:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[31]
                return t.enum_values[t.generated_offsets[0]]

            @staticmethod
            def fixed_reg(greycat: Optional[GreyCat] = None) -> std.core.SamplingMode:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[31]
                return t.enum_values[t.generated_offsets[1]]

            @staticmethod
            def adaptative(greycat: Optional[GreyCat] = None) -> std.core.SamplingMode:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[31]
                return t.enum_values[t.generated_offsets[2]]

            @staticmethod
            def dense(greycat: Optional[GreyCat] = None) -> std.core.SamplingMode:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[31]
                return t.enum_values[t.generated_offsets[3]]

            @staticmethod
            def create(greycat: Optional[GreyCat] = None) -> std.core.SamplingMode:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                return std.core.SamplingMode(greycat.libs_by_name[std.name_].mapped[31], [])

        @final
        class ti6d(std_n.core._ti6d):
            name_: Final[str] = "core::ti6d"

            def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
                super().__init__(type)

            @staticmethod
            def create(greycat: Optional[GreyCat] = None) -> std_n.core._ti6d:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                return std.core.ti6d(greycat.libs_by_name[std.name_].mapped[32], [])

        @final
        class GeoCircle(GreyCat.Object):
            name_: Final[str] = "core::GeoCircle"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def center(self) -> std.core.geo:
                return self._get(self.type_.generated_offsets[0])

            def set_center(self, v: std.core.geo) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def radius(self) -> float:
                return self._get(self.type_.generated_offsets[1])

            def set_radius(self, v: float) -> None:
                self._set(self.type_.generated_offsets[1], v)

            @staticmethod
            def create(center: std.core.geo, radius: float, greycat: Optional[GreyCat] = None) -> std.core.GeoCircle:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                return std.core.GeoCircle(greycat.libs_by_name[std.name_].mapped[33], [center, radius])

        @final
        class Map(Generic[__K, __V], std_n.core._Map[__K, __V]):
            name_: Final[str] = "core::Map"

            def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
                super().__init__(type)

            @staticmethod
            def create(greycat: Optional[GreyCat] = None) -> std_n.core._Map:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                return std.core.Map(greycat.libs_by_name[std.name_].mapped[34], [])

        @final
        class ErrorCode(GreyCat.Enum):
            name_: Final[str] = "core::ErrorCode"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            @staticmethod
            def none(greycat: Optional[GreyCat] = None) -> std.core.ErrorCode:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[35]
                return t.enum_values[t.generated_offsets[0]]

            @staticmethod
            def too_deep_workspace(greycat: Optional[GreyCat] = None) -> std.core.ErrorCode:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[35]
                return t.enum_values[t.generated_offsets[1]]

            @staticmethod
            def too_deep_iterator(greycat: Optional[GreyCat] = None) -> std.core.ErrorCode:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[35]
                return t.enum_values[t.generated_offsets[2]]

            @staticmethod
            def wrong_operand(greycat: Optional[GreyCat] = None) -> std.core.ErrorCode:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[35]
                return t.enum_values[t.generated_offsets[3]]

            @staticmethod
            def wrong_params(greycat: Optional[GreyCat] = None) -> std.core.ErrorCode:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[35]
                return t.enum_values[t.generated_offsets[4]]

            @staticmethod
            def wrong_param_type(greycat: Optional[GreyCat] = None) -> std.core.ErrorCode:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[35]
                return t.enum_values[t.generated_offsets[5]]

            @staticmethod
            def wrong_numeric(greycat: Optional[GreyCat] = None) -> std.core.ErrorCode:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[35]
                return t.enum_values[t.generated_offsets[6]]

            @staticmethod
            def wrong_state(greycat: Optional[GreyCat] = None) -> std.core.ErrorCode:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[35]
                return t.enum_values[t.generated_offsets[7]]

            @staticmethod
            def wrong_null(greycat: Optional[GreyCat] = None) -> std.core.ErrorCode:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[35]
                return t.enum_values[t.generated_offsets[8]]

            @staticmethod
            def unresolved_ref(greycat: Optional[GreyCat] = None) -> std.core.ErrorCode:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[35]
                return t.enum_values[t.generated_offsets[9]]

            @staticmethod
            def assign_error(greycat: Optional[GreyCat] = None) -> std.core.ErrorCode:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[35]
                return t.enum_values[t.generated_offsets[10]]

            @staticmethod
            def interrupted(greycat: Optional[GreyCat] = None) -> std.core.ErrorCode:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[35]
                return t.enum_values[t.generated_offsets[11]]

            @staticmethod
            def throw(greycat: Optional[GreyCat] = None) -> std.core.ErrorCode:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[35]
                return t.enum_values[t.generated_offsets[12]]

            @staticmethod
            def wrong_type(greycat: Optional[GreyCat] = None) -> std.core.ErrorCode:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[35]
                return t.enum_values[t.generated_offsets[13]]

            @staticmethod
            def wrong_dimension(greycat: Optional[GreyCat] = None) -> std.core.ErrorCode:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[35]
                return t.enum_values[t.generated_offsets[14]]

            @staticmethod
            def unsupported_operation(greycat: Optional[GreyCat] = None) -> std.core.ErrorCode:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[35]
                return t.enum_values[t.generated_offsets[15]]

            @staticmethod
            def unsupported_type(greycat: Optional[GreyCat] = None) -> std.core.ErrorCode:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[35]
                return t.enum_values[t.generated_offsets[16]]

            @staticmethod
            def dimensions_mismatch(greycat: Optional[GreyCat] = None) -> std.core.ErrorCode:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[35]
                return t.enum_values[t.generated_offsets[17]]

            @staticmethod
            def timeout(greycat: Optional[GreyCat] = None) -> std.core.ErrorCode:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[35]
                return t.enum_values[t.generated_offsets[18]]

            @staticmethod
            def forbidden(greycat: Optional[GreyCat] = None) -> std.core.ErrorCode:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[35]
                return t.enum_values[t.generated_offsets[19]]

            @staticmethod
            def runtime_error(greycat: Optional[GreyCat] = None) -> std.core.ErrorCode:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[35]
                return t.enum_values[t.generated_offsets[20]]

            @staticmethod
            def create(greycat: Optional[GreyCat] = None) -> std.core.ErrorCode:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                return std.core.ErrorCode(greycat.libs_by_name[std.name_].mapped[35], [])

        @final
        class ti4d(std_n.core._ti4d):
            name_: Final[str] = "core::ti4d"

            def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
                super().__init__(type)

            @staticmethod
            def create(greycat: Optional[GreyCat] = None) -> std_n.core._ti4d:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                return std.core.ti4d(greycat.libs_by_name[std.name_].mapped[36], [])

        @final
        class geo(std_n.core._geo):
            name_: Final[str] = "core::geo"

            def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
                super().__init__(type)

            @staticmethod
            def create(greycat: Optional[GreyCat] = None) -> std_n.core._geo:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                return std.core.geo(greycat.libs_by_name[std.name_].mapped[37], [])

        @final
        class nodeTimeSingleton(GreyCat.Object):
            name_: Final[str] = "core::nodeTimeSingleton"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def t(self) -> std.core.time:
                return self._get(self.type_.generated_offsets[0])

            def set_t(self, v: std.core.time) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def v(self) -> Any:
                return self._get(self.type_.generated_offsets[1])

            def set_v(self, v: Any) -> None:
                self._set(self.type_.generated_offsets[1], v)

            @staticmethod
            def create(t: std.core.time, v: Any, greycat: Optional[GreyCat] = None) -> std.core.nodeTimeSingleton:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                return std.core.nodeTimeSingleton(greycat.libs_by_name[std.name_].mapped[38], [t, v])

        @final
        class NodeInfo(Generic[__T], GreyCat.Object):
            name_: Final[str] = "core::NodeInfo"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def size(self) -> int:
                return self._get(self.type_.generated_offsets[0])

            def set_size(self, v: int) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def from_(self) -> std.core.__T:
                return self._get(self.type_.generated_offsets[1])

            def set_from(self, v: std.core.__T) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def to(self) -> std.core.__T:
                return self._get(self.type_.generated_offsets[2])

            def set_to(self, v: std.core.__T) -> None:
                self._set(self.type_.generated_offsets[2], v)

            @staticmethod
            def create(size: int, from_: std.core.__T, to: std.core.__T, greycat: Optional[GreyCat] = None) -> std.core.NodeInfo[TypeVar("T")]:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                return std.core.NodeInfo(greycat.libs_by_name[std.name_].mapped[39], [size, from_, to])

    @final
    class runtime:

        @final
        class RuntimeInfo(GreyCat.Object):
            name_: Final[str] = "runtime::RuntimeInfo"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def version(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_version(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def program_version(self) -> str:
                return self._get(self.type_.generated_offsets[1])

            def set_program_version(self, v: str) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def arch(self) -> str:
                return self._get(self.type_.generated_offsets[2])

            def set_arch(self, v: str) -> None:
                self._set(self.type_.generated_offsets[2], v)

            def timezone(self) -> std.core.TimeZone:
                return self._get(self.type_.generated_offsets[3])

            def set_timezone(self, v: std.core.TimeZone) -> None:
                self._set(self.type_.generated_offsets[3], v)

            def license(self) -> std.runtime.License:
                return self._get(self.type_.generated_offsets[4])

            def set_license(self, v: std.runtime.License) -> None:
                self._set(self.type_.generated_offsets[4], v)

            def io_threads(self) -> int:
                return self._get(self.type_.generated_offsets[5])

            def set_io_threads(self, v: int) -> None:
                self._set(self.type_.generated_offsets[5], v)

            def bg_threads(self) -> int:
                return self._get(self.type_.generated_offsets[6])

            def set_bg_threads(self, v: int) -> None:
                self._set(self.type_.generated_offsets[6], v)

            def fg_threads(self) -> int:
                return self._get(self.type_.generated_offsets[7])

            def set_fg_threads(self, v: int) -> None:
                self._set(self.type_.generated_offsets[7], v)

            def mem_total(self) -> int:
                return self._get(self.type_.generated_offsets[8])

            def set_mem_total(self, v: int) -> None:
                self._set(self.type_.generated_offsets[8], v)

            def mem_worker(self) -> int:
                return self._get(self.type_.generated_offsets[9])

            def set_mem_worker(self, v: int) -> None:
                self._set(self.type_.generated_offsets[9], v)

            def nb_ctx(self) -> int:
                return self._get(self.type_.generated_offsets[10])

            def set_nb_ctx(self, v: int) -> None:
                self._set(self.type_.generated_offsets[10], v)

            def store_stats(self) -> std.runtime.StoreStat:
                return self._get(self.type_.generated_offsets[11])

            def set_store_stats(self, v: std.runtime.StoreStat) -> None:
                self._set(self.type_.generated_offsets[11], v)

            @staticmethod
            def create(version: str, program_version: str, arch: str, timezone: std.core.TimeZone, license: std.runtime.License, io_threads: int, bg_threads: int, fg_threads: int, mem_total: int, mem_worker: int, nb_ctx: int, store_stats: std.runtime.StoreStat, greycat: Optional[GreyCat] = None) -> std.runtime.RuntimeInfo:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                return std.runtime.RuntimeInfo(greycat.libs_by_name[std.name_].mapped[40], [version, program_version, arch, timezone, license, io_threads, bg_threads, fg_threads, mem_total, mem_worker, nb_ctx, store_stats])

        @final
        class PeriodicTask(GreyCat.Object):
            name_: Final[str] = "runtime::PeriodicTask"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def function(self) -> std.core.function:
                return self._get(self.type_.generated_offsets[0])

            def set_function(self, v: std.core.function) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def user_id(self) -> int:
                return self._get(self.type_.generated_offsets[1])

            def set_user_id(self, v: int) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def arguments(self) -> std.core.Array:
                return self._get(self.type_.generated_offsets[2])

            def set_arguments(self, v: std.core.Array) -> None:
                self._set(self.type_.generated_offsets[2], v)

            def start(self) -> std.core.time:
                return self._get(self.type_.generated_offsets[3])

            def set_start(self, v: std.core.time) -> None:
                self._set(self.type_.generated_offsets[3], v)

            def every(self) -> std.core.duration:
                return self._get(self.type_.generated_offsets[4])

            def set_every(self, v: std.core.duration) -> None:
                self._set(self.type_.generated_offsets[4], v)

            @staticmethod
            def all(__greycat: Optional[GreyCat] = None) -> std.core.Array:
                if __greycat is None:
                    __greycat = GreyCat.DEFAULT
                return __greycat.call("runtime::PeriodicTask::all")

            @staticmethod
            def set(tasks: std.core.Array, __greycat: Optional[GreyCat] = None) -> None:
                if __greycat is None:
                    __greycat = GreyCat.DEFAULT
                return __greycat.call("runtime::PeriodicTask::set", [tasks, ])

            @staticmethod
            def create(function: std.core.function, user_id: int, arguments: std.core.Array, start: std.core.time, every: std.core.duration, greycat: Optional[GreyCat] = None) -> std.runtime.PeriodicTask:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                return std.runtime.PeriodicTask(greycat.libs_by_name[std.name_].mapped[41], [function, user_id, arguments, start, every])

        @final
        class SecurityFields(GreyCat.Object):
            name_: Final[str] = "runtime::SecurityFields"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def email(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_email(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def name(self) -> str:
                return self._get(self.type_.generated_offsets[1])

            def set_name(self, v: str) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def first_name(self) -> str:
                return self._get(self.type_.generated_offsets[2])

            def set_first_name(self, v: str) -> None:
                self._set(self.type_.generated_offsets[2], v)

            def last_name(self) -> str:
                return self._get(self.type_.generated_offsets[3])

            def set_last_name(self, v: str) -> None:
                self._set(self.type_.generated_offsets[3], v)

            def roles(self) -> std.core.Map:
                return self._get(self.type_.generated_offsets[4])

            def set_roles(self, v: std.core.Map) -> None:
                self._set(self.type_.generated_offsets[4], v)

            def groups(self) -> std.core.Map:
                return self._get(self.type_.generated_offsets[5])

            def set_groups(self, v: std.core.Map) -> None:
                self._set(self.type_.generated_offsets[5], v)

            @staticmethod
            def set(f: std.runtime.SecurityFields, __greycat: Optional[GreyCat] = None) -> None:
                if __greycat is None:
                    __greycat = GreyCat.DEFAULT
                return __greycat.call("runtime::SecurityFields::set", [f, ])

            @staticmethod
            def get(__greycat: Optional[GreyCat] = None) -> std.runtime.SecurityFields:
                if __greycat is None:
                    __greycat = GreyCat.DEFAULT
                return __greycat.call("runtime::SecurityFields::get")

            @staticmethod
            def create(email: str, name: str, first_name: str, last_name: str, roles: std.core.Map, groups: std.core.Map, greycat: Optional[GreyCat] = None) -> std.runtime.SecurityFields:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                return std.runtime.SecurityFields(greycat.libs_by_name[std.name_].mapped[42], [email, name, first_name, last_name, roles, groups])

        @final
        class LicenseType(GreyCat.Enum):
            name_: Final[str] = "runtime::LicenseType"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            @staticmethod
            def community(greycat: Optional[GreyCat] = None) -> std.runtime.LicenseType:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[43]
                return t.enum_values[t.generated_offsets[0]]

            @staticmethod
            def enterprise(greycat: Optional[GreyCat] = None) -> std.runtime.LicenseType:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[43]
                return t.enum_values[t.generated_offsets[1]]

            @staticmethod
            def testing(greycat: Optional[GreyCat] = None) -> std.runtime.LicenseType:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[43]
                return t.enum_values[t.generated_offsets[2]]

            @staticmethod
            def create(greycat: Optional[GreyCat] = None) -> std.runtime.LicenseType:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                return std.runtime.LicenseType(greycat.libs_by_name[std.name_].mapped[43], [])

        @final
        class UserGroup(GreyCat.Object):
            name_: Final[str] = "runtime::UserGroup"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def id(self) -> int:
                return self._get(self.type_.generated_offsets[0])

            def set_id(self, v: int) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def name(self) -> str:
                return self._get(self.type_.generated_offsets[1])

            def set_name(self, v: str) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def activated(self) -> bool:
                return self._get(self.type_.generated_offsets[2])

            def set_activated(self, v: bool) -> None:
                self._set(self.type_.generated_offsets[2], v)

            @staticmethod
            def all(__greycat: Optional[GreyCat] = None) -> std.core.Array:
                if __greycat is None:
                    __greycat = GreyCat.DEFAULT
                return __greycat.call("runtime::SecurityEntity::all")

            @staticmethod
            def set(entity: std.runtime.SecurityEntity, __greycat: Optional[GreyCat] = None) -> int:
                if __greycat is None:
                    __greycat = GreyCat.DEFAULT
                return __greycat.call("runtime::SecurityEntity::set", [entity, ])

            @staticmethod
            def create(id: int, name: str, activated: bool, greycat: Optional[GreyCat] = None) -> std.runtime.UserGroup:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                return std.runtime.UserGroup(greycat.libs_by_name[std.name_].mapped[44], [id, name, activated])

        @final
        class UserGroupPolicyType(GreyCat.Enum):
            name_: Final[str] = "runtime::UserGroupPolicyType"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            @staticmethod
            def read(greycat: Optional[GreyCat] = None) -> std.runtime.UserGroupPolicyType:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[45]
                return t.enum_values[t.generated_offsets[0]]

            @staticmethod
            def write(greycat: Optional[GreyCat] = None) -> std.runtime.UserGroupPolicyType:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[45]
                return t.enum_values[t.generated_offsets[1]]

            @staticmethod
            def execute(greycat: Optional[GreyCat] = None) -> std.runtime.UserGroupPolicyType:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[45]
                return t.enum_values[t.generated_offsets[2]]

            @staticmethod
            def create(greycat: Optional[GreyCat] = None) -> std.runtime.UserGroupPolicyType:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                return std.runtime.UserGroupPolicyType(greycat.libs_by_name[std.name_].mapped[45], [])

        @final
        class UserGroupPolicy(GreyCat.Object):
            name_: Final[str] = "runtime::UserGroupPolicy"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def group_id(self) -> int:
                return self._get(self.type_.generated_offsets[0])

            def set_group_id(self, v: int) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def type(self) -> std.runtime.UserGroupPolicyType:
                return self._get(self.type_.generated_offsets[1])

            def set_type(self, v: std.runtime.UserGroupPolicyType) -> None:
                self._set(self.type_.generated_offsets[1], v)

            @staticmethod
            def create(group_id: int, type: std.runtime.UserGroupPolicyType, greycat: Optional[GreyCat] = None) -> std.runtime.UserGroupPolicy:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                return std.runtime.UserGroupPolicy(greycat.libs_by_name[std.name_].mapped[46], [group_id, type])

        @final
        class User(GreyCat.Object):
            name_: Final[str] = "runtime::User"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def id(self) -> int:
                return self._get(self.type_.generated_offsets[0])

            def set_id(self, v: int) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def name(self) -> str:
                return self._get(self.type_.generated_offsets[1])

            def set_name(self, v: str) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def activated(self) -> bool:
                return self._get(self.type_.generated_offsets[2])

            def set_activated(self, v: bool) -> None:
                self._set(self.type_.generated_offsets[2], v)

            def full_name(self) -> str:
                return self._get(self.type_.generated_offsets[3])

            def set_full_name(self, v: str) -> None:
                self._set(self.type_.generated_offsets[3], v)

            def email(self) -> str:
                return self._get(self.type_.generated_offsets[4])

            def set_email(self, v: str) -> None:
                self._set(self.type_.generated_offsets[4], v)

            def role(self) -> str:
                return self._get(self.type_.generated_offsets[5])

            def set_role(self, v: str) -> None:
                self._set(self.type_.generated_offsets[5], v)

            def permissions_flags(self) -> int:
                return self._get(self.type_.generated_offsets[6])

            def set_permissions_flags(self, v: int) -> None:
                self._set(self.type_.generated_offsets[6], v)

            def groups(self) -> std.core.Array:
                return self._get(self.type_.generated_offsets[7])

            def set_groups(self, v: std.core.Array) -> None:
                self._set(self.type_.generated_offsets[7], v)

            def groups_flags(self) -> int:
                return self._get(self.type_.generated_offsets[8])

            def set_groups_flags(self, v: int) -> None:
                self._set(self.type_.generated_offsets[8], v)

            def external(self) -> bool:
                return self._get(self.type_.generated_offsets[9])

            def set_external(self, v: bool) -> None:
                self._set(self.type_.generated_offsets[9], v)

            @staticmethod
            def all(__greycat: Optional[GreyCat] = None) -> std.core.Array:
                if __greycat is None:
                    __greycat = GreyCat.DEFAULT
                return __greycat.call("runtime::SecurityEntity::all")

            @staticmethod
            def set(entity: std.runtime.SecurityEntity, __greycat: Optional[GreyCat] = None) -> int:
                if __greycat is None:
                    __greycat = GreyCat.DEFAULT
                return __greycat.call("runtime::SecurityEntity::set", [entity, ])

            @staticmethod
            def login(credentials: str, use_cookie: bool, __greycat: Optional[GreyCat] = None) -> str:
                if __greycat is None:
                    __greycat = GreyCat.DEFAULT
                return __greycat.call("runtime::User::login", [credentials, use_cookie, ])

            @staticmethod
            def tokenLogin(token: str, use_cookie: bool, __greycat: Optional[GreyCat] = None) -> str:
                if __greycat is None:
                    __greycat = GreyCat.DEFAULT
                return __greycat.call("runtime::User::tokenLogin", [token, use_cookie, ])

            @staticmethod
            def logout(__greycat: Optional[GreyCat] = None) -> None:
                if __greycat is None:
                    __greycat = GreyCat.DEFAULT
                return __greycat.call("runtime::User::logout")

            @staticmethod
            def renew(use_cookie: bool, __greycat: Optional[GreyCat] = None) -> str:
                if __greycat is None:
                    __greycat = GreyCat.DEFAULT
                return __greycat.call("runtime::User::renew", [use_cookie, ])

            @staticmethod
            def current(__greycat: Optional[GreyCat] = None) -> int:
                if __greycat is None:
                    __greycat = GreyCat.DEFAULT
                return __greycat.call("runtime::User::current")

            @staticmethod
            def me(__greycat: Optional[GreyCat] = None) -> std.runtime.User:
                if __greycat is None:
                    __greycat = GreyCat.DEFAULT
                return __greycat.call("runtime::User::me")

            @staticmethod
            def permissions(__greycat: Optional[GreyCat] = None) -> std.core.Array:
                if __greycat is None:
                    __greycat = GreyCat.DEFAULT
                return __greycat.call("runtime::User::permissions")

            @staticmethod
            def setPassword(name: str, pass_: str, __greycat: Optional[GreyCat] = None) -> bool:
                if __greycat is None:
                    __greycat = GreyCat.DEFAULT
                return __greycat.call("runtime::User::setPassword", [name, pass_, ])

            @staticmethod
            def getToken(id: int, __greycat: Optional[GreyCat] = None) -> str:
                if __greycat is None:
                    __greycat = GreyCat.DEFAULT
                return __greycat.call("runtime::User::getToken", [id, ])

            @staticmethod
            def create(id: int, name: str, activated: bool, full_name: str, email: str, role: str, permissions_flags: int, groups: std.core.Array, groups_flags: int, external: bool, greycat: Optional[GreyCat] = None) -> std.runtime.User:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                return std.runtime.User(greycat.libs_by_name[std.name_].mapped[47], [id, name, activated, full_name, email, role, permissions_flags, groups, groups_flags, external])

        @final
        class UserCredential(GreyCat.Object):
            name_: Final[str] = "runtime::UserCredential"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def offset(self) -> int:
                return self._get(self.type_.generated_offsets[0])

            def set_offset(self, v: int) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def pass_(self) -> str:
                return self._get(self.type_.generated_offsets[1])

            def set_pass(self, v: str) -> None:
                self._set(self.type_.generated_offsets[1], v)

            @staticmethod
            def create(offset: int, pass_: str, greycat: Optional[GreyCat] = None) -> std.runtime.UserCredential:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                return std.runtime.UserCredential(greycat.libs_by_name[std.name_].mapped[48], [offset, pass_])

        @final
        class StoreStat(GreyCat.Object):
            name_: Final[str] = "runtime::StoreStat"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def capacity_bytes(self) -> int:
                return self._get(self.type_.generated_offsets[0])

            def set_capacity_bytes(self, v: int) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def allocated_bytes(self) -> int:
                return self._get(self.type_.generated_offsets[1])

            def set_allocated_bytes(self, v: int) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def allocated_ratio(self) -> float:
                return self._get(self.type_.generated_offsets[2])

            def set_allocated_ratio(self, v: float) -> None:
                self._set(self.type_.generated_offsets[2], v)

            def remained_bytes(self) -> int:
                return self._get(self.type_.generated_offsets[3])

            def set_remained_bytes(self, v: int) -> None:
                self._set(self.type_.generated_offsets[3], v)

            def remained_ratio(self) -> float:
                return self._get(self.type_.generated_offsets[4])

            def set_remained_ratio(self, v: float) -> None:
                self._set(self.type_.generated_offsets[4], v)

            def used_bytes(self) -> int:
                return self._get(self.type_.generated_offsets[5])

            def set_used_bytes(self, v: int) -> None:
                self._set(self.type_.generated_offsets[5], v)

            def used_ratio(self) -> float:
                return self._get(self.type_.generated_offsets[6])

            def set_used_ratio(self, v: float) -> None:
                self._set(self.type_.generated_offsets[6], v)

            def available_bytes(self) -> int:
                return self._get(self.type_.generated_offsets[7])

            def set_available_bytes(self, v: int) -> None:
                self._set(self.type_.generated_offsets[7], v)

            def available_ratio(self) -> float:
                return self._get(self.type_.generated_offsets[8])

            def set_available_ratio(self, v: float) -> None:
                self._set(self.type_.generated_offsets[8], v)

            @staticmethod
            def create(capacity_bytes: int, allocated_bytes: int, allocated_ratio: float, remained_bytes: int, remained_ratio: float, used_bytes: int, used_ratio: float, available_bytes: int, available_ratio: float, greycat: Optional[GreyCat] = None) -> std.runtime.StoreStat:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                return std.runtime.StoreStat(greycat.libs_by_name[std.name_].mapped[49], [capacity_bytes, allocated_bytes, allocated_ratio, remained_bytes, remained_ratio, used_bytes, used_ratio, available_bytes, available_ratio])

        @final
        class UserRole(GreyCat.Object):
            name_: Final[str] = "runtime::UserRole"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def name(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_name(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def permissions(self) -> std.core.Array:
                return self._get(self.type_.generated_offsets[1])

            def set_permissions(self, v: std.core.Array) -> None:
                self._set(self.type_.generated_offsets[1], v)

            @staticmethod
            def all(__greycat: Optional[GreyCat] = None) -> std.core.Array:
                if __greycat is None:
                    __greycat = GreyCat.DEFAULT
                return __greycat.call("runtime::UserRole::all")

            @staticmethod
            def remove(name: str, __greycat: Optional[GreyCat] = None) -> None:
                if __greycat is None:
                    __greycat = GreyCat.DEFAULT
                return __greycat.call("runtime::UserRole::remove", [name, ])

            @staticmethod
            def set(value: std.runtime.UserRole, __greycat: Optional[GreyCat] = None) -> None:
                if __greycat is None:
                    __greycat = GreyCat.DEFAULT
                return __greycat.call("runtime::UserRole::set", [value, ])

            @staticmethod
            def create(name: str, permissions: std.core.Array, greycat: Optional[GreyCat] = None) -> std.runtime.UserRole:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                return std.runtime.UserRole(greycat.libs_by_name[std.name_].mapped[50], [name, permissions])

        @final
        class OpenIDConnect(GreyCat.Object):
            name_: Final[str] = "runtime::OpenIDConnect"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def url(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_url(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def clientId(self) -> str:
                return self._get(self.type_.generated_offsets[1])

            def set_clientId(self, v: str) -> None:
                self._set(self.type_.generated_offsets[1], v)

            @staticmethod
            def config(__greycat: Optional[GreyCat] = None) -> std.runtime.OpenIDConnect:
                if __greycat is None:
                    __greycat = GreyCat.DEFAULT
                return __greycat.call("runtime::OpenIDConnect::config")

            @staticmethod
            def create(url: str, clientId: str, greycat: Optional[GreyCat] = None) -> std.runtime.OpenIDConnect:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                return std.runtime.OpenIDConnect(greycat.libs_by_name[std.name_].mapped[51], [url, clientId])

        @final
        class Task(GreyCat.Object):
            name_: Final[str] = "runtime::Task"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def user_id(self) -> int:
                return self._get(self.type_.generated_offsets[0])

            def set_user_id(self, v: int) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def task_id(self) -> int:
                return self._get(self.type_.generated_offsets[1])

            def set_task_id(self, v: int) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def mod(self) -> str:
                return self._get(self.type_.generated_offsets[2])

            def set_mod(self, v: str) -> None:
                self._set(self.type_.generated_offsets[2], v)

            def type(self) -> str:
                return self._get(self.type_.generated_offsets[3])

            def set_type(self, v: str) -> None:
                self._set(self.type_.generated_offsets[3], v)

            def fun(self) -> str:
                return self._get(self.type_.generated_offsets[4])

            def set_fun(self, v: str) -> None:
                self._set(self.type_.generated_offsets[4], v)

            def creation(self) -> std.core.time:
                return self._get(self.type_.generated_offsets[5])

            def set_creation(self, v: std.core.time) -> None:
                self._set(self.type_.generated_offsets[5], v)

            def status(self) -> std.runtime.TaskStatus:
                return self._get(self.type_.generated_offsets[6])

            def set_status(self, v: std.runtime.TaskStatus) -> None:
                self._set(self.type_.generated_offsets[6], v)

            @staticmethod
            def running(__greycat: Optional[GreyCat] = None) -> std.core.Array:
                if __greycat is None:
                    __greycat = GreyCat.DEFAULT
                return __greycat.call("runtime::Task::running")

            @staticmethod
            def history(offset: int, max: int, __greycat: Optional[GreyCat] = None) -> std.core.Array:
                if __greycat is None:
                    __greycat = GreyCat.DEFAULT
                return __greycat.call("runtime::Task::history", [offset, max, ])

            @staticmethod
            def cancel(task_id: int, __greycat: Optional[GreyCat] = None) -> bool:
                if __greycat is None:
                    __greycat = GreyCat.DEFAULT
                return __greycat.call("runtime::Task::cancel", [task_id, ])

            @staticmethod
            def info(user_id: int, task_id: int, __greycat: Optional[GreyCat] = None) -> std.runtime.TaskInfo:
                if __greycat is None:
                    __greycat = GreyCat.DEFAULT
                return __greycat.call("runtime::Task::info", [user_id, task_id, ])

            @staticmethod
            def create(user_id: int, task_id: int, mod: str, type: str, fun: str, creation: std.core.time, status: std.runtime.TaskStatus, greycat: Optional[GreyCat] = None) -> std.runtime.Task:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                return std.runtime.Task(greycat.libs_by_name[std.name_].mapped[52], [user_id, task_id, mod, type, fun, creation, status])

        @final
        class SecurityPolicy(GreyCat.Object):
            name_: Final[str] = "runtime::SecurityPolicy"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def entities(self) -> std.core.Array:
                return self._get(self.type_.generated_offsets[0])

            def set_entities(self, v: std.core.Array) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def credentials(self) -> std.core.Map:
                return self._get(self.type_.generated_offsets[1])

            def set_credentials(self, v: std.core.Map) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def roles(self) -> std.core.Map:
                return self._get(self.type_.generated_offsets[2])

            def set_roles(self, v: std.core.Map) -> None:
                self._set(self.type_.generated_offsets[2], v)

            def fields(self) -> std.runtime.SecurityFields:
                return self._get(self.type_.generated_offsets[3])

            def set_fields(self, v: std.runtime.SecurityFields) -> None:
                self._set(self.type_.generated_offsets[3], v)

            def keys(self) -> std.core.Map:
                return self._get(self.type_.generated_offsets[4])

            def set_keys(self, v: std.core.Map) -> None:
                self._set(self.type_.generated_offsets[4], v)

            def keys_last_refresh(self) -> std.core.time:
                return self._get(self.type_.generated_offsets[5])

            def set_keys_last_refresh(self, v: std.core.time) -> None:
                self._set(self.type_.generated_offsets[5], v)

            @staticmethod
            def permissions(__greycat: Optional[GreyCat] = None) -> std.core.Array:
                if __greycat is None:
                    __greycat = GreyCat.DEFAULT
                return __greycat.call("runtime::SecurityPolicy::permissions")

            @staticmethod
            def create(entities: std.core.Array, credentials: std.core.Map, roles: std.core.Map, fields: std.runtime.SecurityFields, keys: std.core.Map, keys_last_refresh: std.core.time, greycat: Optional[GreyCat] = None) -> std.runtime.SecurityPolicy:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                return std.runtime.SecurityPolicy(greycat.libs_by_name[std.name_].mapped[53], [entities, credentials, roles, fields, keys, keys_last_refresh])

        @final
        class License(GreyCat.Object):
            name_: Final[str] = "runtime::License"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def name(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_name(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def start(self) -> std.core.time:
                return self._get(self.type_.generated_offsets[1])

            def set_start(self, v: std.core.time) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def end(self) -> std.core.time:
                return self._get(self.type_.generated_offsets[2])

            def set_end(self, v: std.core.time) -> None:
                self._set(self.type_.generated_offsets[2], v)

            def company(self) -> str:
                return self._get(self.type_.generated_offsets[3])

            def set_company(self, v: str) -> None:
                self._set(self.type_.generated_offsets[3], v)

            def max_memory(self) -> int:
                return self._get(self.type_.generated_offsets[4])

            def set_max_memory(self, v: int) -> None:
                self._set(self.type_.generated_offsets[4], v)

            def extra_1(self) -> int:
                return self._get(self.type_.generated_offsets[5])

            def set_extra_1(self, v: int) -> None:
                self._set(self.type_.generated_offsets[5], v)

            def extra_2(self) -> int:
                return self._get(self.type_.generated_offsets[6])

            def set_extra_2(self, v: int) -> None:
                self._set(self.type_.generated_offsets[6], v)

            def type(self) -> std.runtime.LicenseType:
                return self._get(self.type_.generated_offsets[7])

            def set_type(self, v: std.runtime.LicenseType) -> None:
                self._set(self.type_.generated_offsets[7], v)

            @staticmethod
            def create(name: str, start: std.core.time, end: std.core.time, company: str, max_memory: int, extra_1: int, extra_2: int, type: std.runtime.LicenseType, greycat: Optional[GreyCat] = None) -> std.runtime.License:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                return std.runtime.License(greycat.libs_by_name[std.name_].mapped[54], [name, start, end, company, max_memory, extra_1, extra_2, type])

        @final
        class Runtime(GreyCat.Object):
            name_: Final[str] = "runtime::Runtime"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            @staticmethod
            def info(__greycat: Optional[GreyCat] = None) -> std.runtime.RuntimeInfo:
                if __greycat is None:
                    __greycat = GreyCat.DEFAULT
                return __greycat.call("runtime::Runtime::info")

            @staticmethod
            def abi(__greycat: Optional[GreyCat] = None) -> None:
                if __greycat is None:
                    __greycat = GreyCat.DEFAULT
                return __greycat.call("runtime::Runtime::abi")

            @staticmethod
            def readModVar(mod_var: str, __greycat: Optional[GreyCat] = None) -> Any:
                if __greycat is None:
                    __greycat = GreyCat.DEFAULT
                return __greycat.call("runtime::Runtime::readModVar", [mod_var, ])

            @staticmethod
            def create(greycat: Optional[GreyCat] = None) -> std.runtime.Runtime:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                return std.runtime.Runtime(greycat.libs_by_name[std.name_].mapped[55], [])

        @final
        class TaskStatus(GreyCat.Enum):
            name_: Final[str] = "runtime::TaskStatus"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            @staticmethod
            def empty(greycat: Optional[GreyCat] = None) -> std.runtime.TaskStatus:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[56]
                return t.enum_values[t.generated_offsets[0]]

            @staticmethod
            def waiting(greycat: Optional[GreyCat] = None) -> std.runtime.TaskStatus:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[56]
                return t.enum_values[t.generated_offsets[1]]

            @staticmethod
            def running(greycat: Optional[GreyCat] = None) -> std.runtime.TaskStatus:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[56]
                return t.enum_values[t.generated_offsets[2]]

            @staticmethod
            def cancelled(greycat: Optional[GreyCat] = None) -> std.runtime.TaskStatus:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[56]
                return t.enum_values[t.generated_offsets[3]]

            @staticmethod
            def error(greycat: Optional[GreyCat] = None) -> std.runtime.TaskStatus:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[56]
                return t.enum_values[t.generated_offsets[4]]

            @staticmethod
            def ended(greycat: Optional[GreyCat] = None) -> std.runtime.TaskStatus:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[56]
                return t.enum_values[t.generated_offsets[5]]

            @staticmethod
            def create(greycat: Optional[GreyCat] = None) -> std.runtime.TaskStatus:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                return std.runtime.TaskStatus(greycat.libs_by_name[std.name_].mapped[56], [])

        @final
        class TaskInfo(GreyCat.Object):
            name_: Final[str] = "runtime::TaskInfo"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def user_id(self) -> int:
                return self._get(self.type_.generated_offsets[0])

            def set_user_id(self, v: int) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def task_id(self) -> int:
                return self._get(self.type_.generated_offsets[1])

            def set_task_id(self, v: int) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def mod(self) -> str:
                return self._get(self.type_.generated_offsets[2])

            def set_mod(self, v: str) -> None:
                self._set(self.type_.generated_offsets[2], v)

            def type(self) -> str:
                return self._get(self.type_.generated_offsets[3])

            def set_type(self, v: str) -> None:
                self._set(self.type_.generated_offsets[3], v)

            def fun(self) -> str:
                return self._get(self.type_.generated_offsets[4])

            def set_fun(self, v: str) -> None:
                self._set(self.type_.generated_offsets[4], v)

            def creation(self) -> std.core.time:
                return self._get(self.type_.generated_offsets[5])

            def set_creation(self, v: std.core.time) -> None:
                self._set(self.type_.generated_offsets[5], v)

            def status(self) -> std.runtime.TaskStatus:
                return self._get(self.type_.generated_offsets[6])

            def set_status(self, v: std.runtime.TaskStatus) -> None:
                self._set(self.type_.generated_offsets[6], v)

            def start(self) -> std.core.time:
                return self._get(self.type_.generated_offsets[7])

            def set_start(self, v: std.core.time) -> None:
                self._set(self.type_.generated_offsets[7], v)

            def progress(self) -> float:
                return self._get(self.type_.generated_offsets[8])

            def set_progress(self, v: float) -> None:
                self._set(self.type_.generated_offsets[8], v)

            def remaining(self) -> std.core.duration:
                return self._get(self.type_.generated_offsets[9])

            def set_remaining(self, v: std.core.duration) -> None:
                self._set(self.type_.generated_offsets[9], v)

            def duration(self) -> std.core.duration:
                return self._get(self.type_.generated_offsets[10])

            def set_duration(self, v: std.core.duration) -> None:
                self._set(self.type_.generated_offsets[10], v)

            def sub_waiting(self) -> int:
                return self._get(self.type_.generated_offsets[11])

            def set_sub_waiting(self, v: int) -> None:
                self._set(self.type_.generated_offsets[11], v)

            def sub_tasks_all(self) -> int:
                return self._get(self.type_.generated_offsets[12])

            def set_sub_tasks_all(self, v: int) -> None:
                self._set(self.type_.generated_offsets[12], v)

            @staticmethod
            def create(user_id: int, task_id: int, mod: str, type: str, fun: str, creation: std.core.time, status: std.runtime.TaskStatus, start: std.core.time, progress: float, remaining: std.core.duration, duration: std.core.duration, sub_waiting: int, sub_tasks_all: int, greycat: Optional[GreyCat] = None) -> std.runtime.TaskInfo:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                return std.runtime.TaskInfo(greycat.libs_by_name[std.name_].mapped[57], [user_id, task_id, mod, type, fun, creation, status, start, progress, remaining, duration, sub_waiting, sub_tasks_all])

        @final
        class System(GreyCat.Object):
            name_: Final[str] = "runtime::System"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            @staticmethod
            def create(greycat: Optional[GreyCat] = None) -> std.runtime.System:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                return std.runtime.System(greycat.libs_by_name[std.name_].mapped[58], [])

        @final
        class SecurityEntity(GreyCat.Object):
            name_: Final[str] = "runtime::SecurityEntity"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def id(self) -> int:
                return self._get(self.type_.generated_offsets[0])

            def set_id(self, v: int) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def name(self) -> str:
                return self._get(self.type_.generated_offsets[1])

            def set_name(self, v: str) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def activated(self) -> bool:
                return self._get(self.type_.generated_offsets[2])

            def set_activated(self, v: bool) -> None:
                self._set(self.type_.generated_offsets[2], v)

            @staticmethod
            def all(__greycat: Optional[GreyCat] = None) -> std.core.Array:
                if __greycat is None:
                    __greycat = GreyCat.DEFAULT
                return __greycat.call("runtime::SecurityEntity::all")

            @staticmethod
            def set(entity: std.runtime.SecurityEntity, __greycat: Optional[GreyCat] = None) -> int:
                if __greycat is None:
                    __greycat = GreyCat.DEFAULT
                return __greycat.call("runtime::SecurityEntity::set", [entity, ])

            @staticmethod
            def create(id: int, name: str, activated: bool, greycat: Optional[GreyCat] = None) -> std.runtime.SecurityEntity:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                return std.runtime.SecurityEntity(greycat.libs_by_name[std.name_].mapped[59], [id, name, activated])

    @final
    class io:

        @final
        class CsvColumnDate(GreyCat.Object):
            name_: Final[str] = "io::CsvColumnDate"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def name(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_name(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def mandatory(self) -> bool:
                return self._get(self.type_.generated_offsets[1])

            def set_mandatory(self, v: bool) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def offset(self) -> int:
                return self._get(self.type_.generated_offsets[2])

            def set_offset(self, v: int) -> None:
                self._set(self.type_.generated_offsets[2], v)

            def format(self) -> str:
                return self._get(self.type_.generated_offsets[3])

            def set_format(self, v: str) -> None:
                self._set(self.type_.generated_offsets[3], v)

            def tz(self) -> std.core.TimeZone:
                return self._get(self.type_.generated_offsets[4])

            def set_tz(self, v: std.core.TimeZone) -> None:
                self._set(self.type_.generated_offsets[4], v)

            def as_time(self) -> bool:
                return self._get(self.type_.generated_offsets[5])

            def set_as_time(self, v: bool) -> None:
                self._set(self.type_.generated_offsets[5], v)

            @staticmethod
            def create(name: str, mandatory: bool, offset: int, format: str, tz: std.core.TimeZone, as_time: bool, greycat: Optional[GreyCat] = None) -> std.io.CsvColumnDate:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                return std.io.CsvColumnDate(greycat.libs_by_name[std.name_].mapped[60], [name, mandatory, offset, format, tz, as_time])

        @final
        class CsvColumnInteger(GreyCat.Object):
            name_: Final[str] = "io::CsvColumnInteger"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def name(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_name(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def mandatory(self) -> bool:
                return self._get(self.type_.generated_offsets[1])

            def set_mandatory(self, v: bool) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def offset(self) -> int:
                return self._get(self.type_.generated_offsets[2])

            def set_offset(self, v: int) -> None:
                self._set(self.type_.generated_offsets[2], v)

            @staticmethod
            def create(name: str, mandatory: bool, offset: int, greycat: Optional[GreyCat] = None) -> std.io.CsvColumnInteger:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                return std.io.CsvColumnInteger(greycat.libs_by_name[std.name_].mapped[61], [name, mandatory, offset])

        @final
        class File(GreyCat.Object):
            name_: Final[str] = "io::File"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def path(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_path(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def size(self) -> int:
                return self._get(self.type_.generated_offsets[1])

            def set_size(self, v: int) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def last_modification(self) -> std.core.time:
                return self._get(self.type_.generated_offsets[2])

            def set_last_modification(self, v: std.core.time) -> None:
                self._set(self.type_.generated_offsets[2], v)

            @staticmethod
            def create(path: str, size: int, last_modification: std.core.time, greycat: Optional[GreyCat] = None) -> std.io.File:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                return std.io.File(greycat.libs_by_name[std.name_].mapped[62], [path, size, last_modification])

        @final
        class CsvColumnString(GreyCat.Object):
            name_: Final[str] = "io::CsvColumnString"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def name(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_name(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def mandatory(self) -> bool:
                return self._get(self.type_.generated_offsets[1])

            def set_mandatory(self, v: bool) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def offset(self) -> int:
                return self._get(self.type_.generated_offsets[2])

            def set_offset(self, v: int) -> None:
                self._set(self.type_.generated_offsets[2], v)

            def trim(self) -> bool:
                return self._get(self.type_.generated_offsets[3])

            def set_trim(self, v: bool) -> None:
                self._set(self.type_.generated_offsets[3], v)

            def try_number(self) -> bool:
                return self._get(self.type_.generated_offsets[4])

            def set_try_number(self, v: bool) -> None:
                self._set(self.type_.generated_offsets[4], v)

            def try_json(self) -> bool:
                return self._get(self.type_.generated_offsets[5])

            def set_try_json(self, v: bool) -> None:
                self._set(self.type_.generated_offsets[5], v)

            def values(self) -> std.core.Array:
                return self._get(self.type_.generated_offsets[6])

            def set_values(self, v: std.core.Array) -> None:
                self._set(self.type_.generated_offsets[6], v)

            def encoder(self) -> std.io.TextEncoder:
                return self._get(self.type_.generated_offsets[7])

            def set_encoder(self, v: std.io.TextEncoder) -> None:
                self._set(self.type_.generated_offsets[7], v)

            @staticmethod
            def create(name: str, mandatory: bool, offset: int, trim: bool, try_number: bool, try_json: bool, values: std.core.Array, encoder: std.io.TextEncoder, greycat: Optional[GreyCat] = None) -> std.io.CsvColumnString:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                return std.io.CsvColumnString(greycat.libs_by_name[std.name_].mapped[63], [name, mandatory, offset, trim, try_number, try_json, values, encoder])

        @final
        class CsvStatistics(GreyCat.Object):
            name_: Final[str] = "io::CsvStatistics"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def header_lines(self) -> int:
                return self._get(self.type_.generated_offsets[0])

            def set_header_lines(self, v: int) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def separator(self) -> c_char:
                return self._get(self.type_.generated_offsets[1])

            def set_separator(self, v: c_char) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def string_delimiter(self) -> c_char:
                return self._get(self.type_.generated_offsets[2])

            def set_string_delimiter(self, v: c_char) -> None:
                self._set(self.type_.generated_offsets[2], v)

            def decimal_separator(self) -> c_char:
                return self._get(self.type_.generated_offsets[3])

            def set_decimal_separator(self, v: c_char) -> None:
                self._set(self.type_.generated_offsets[3], v)

            def thousands_separator(self) -> c_char:
                return self._get(self.type_.generated_offsets[4])

            def set_thousands_separator(self, v: c_char) -> None:
                self._set(self.type_.generated_offsets[4], v)

            def columns(self) -> std.core.Array:
                return self._get(self.type_.generated_offsets[5])

            def set_columns(self, v: std.core.Array) -> None:
                self._set(self.type_.generated_offsets[5], v)

            def line_count(self) -> int:
                return self._get(self.type_.generated_offsets[6])

            def set_line_count(self, v: int) -> None:
                self._set(self.type_.generated_offsets[6], v)

            def fail_count(self) -> int:
                return self._get(self.type_.generated_offsets[7])

            def set_fail_count(self, v: int) -> None:
                self._set(self.type_.generated_offsets[7], v)

            def file_count(self) -> int:
                return self._get(self.type_.generated_offsets[8])

            def set_file_count(self, v: int) -> None:
                self._set(self.type_.generated_offsets[8], v)

            @staticmethod
            def create(header_lines: int, separator: c_char, string_delimiter: c_char, decimal_separator: c_char, thousands_separator: c_char, columns: std.core.Array, line_count: int, fail_count: int, file_count: int, greycat: Optional[GreyCat] = None) -> std.io.CsvStatistics:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                return std.io.CsvStatistics(greycat.libs_by_name[std.name_].mapped[64], [header_lines, separator, string_delimiter, decimal_separator, thousands_separator, columns, line_count, fail_count, file_count])

        @final
        class CsvColumnFloat(GreyCat.Object):
            name_: Final[str] = "io::CsvColumnFloat"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def name(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_name(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def mandatory(self) -> bool:
                return self._get(self.type_.generated_offsets[1])

            def set_mandatory(self, v: bool) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def offset(self) -> int:
                return self._get(self.type_.generated_offsets[2])

            def set_offset(self, v: int) -> None:
                self._set(self.type_.generated_offsets[2], v)

            @staticmethod
            def create(name: str, mandatory: bool, offset: int, greycat: Optional[GreyCat] = None) -> std.io.CsvColumnFloat:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                return std.io.CsvColumnFloat(greycat.libs_by_name[std.name_].mapped[65], [name, mandatory, offset])

        @final
        class HttpHeader(GreyCat.Object):
            name_: Final[str] = "io::HttpHeader"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def name(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_name(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def value(self) -> str:
                return self._get(self.type_.generated_offsets[1])

            def set_value(self, v: str) -> None:
                self._set(self.type_.generated_offsets[1], v)

            @staticmethod
            def create(name: str, value: str, greycat: Optional[GreyCat] = None) -> std.io.HttpHeader:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                return std.io.HttpHeader(greycat.libs_by_name[std.name_].mapped[66], [name, value])

        @final
        class CsvFormat(GreyCat.Object):
            name_: Final[str] = "io::CsvFormat"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def header_lines(self) -> int:
                return self._get(self.type_.generated_offsets[0])

            def set_header_lines(self, v: int) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def separator(self) -> c_char:
                return self._get(self.type_.generated_offsets[1])

            def set_separator(self, v: c_char) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def string_delimiter(self) -> c_char:
                return self._get(self.type_.generated_offsets[2])

            def set_string_delimiter(self, v: c_char) -> None:
                self._set(self.type_.generated_offsets[2], v)

            def decimal_separator(self) -> c_char:
                return self._get(self.type_.generated_offsets[3])

            def set_decimal_separator(self, v: c_char) -> None:
                self._set(self.type_.generated_offsets[3], v)

            def thousands_separator(self) -> c_char:
                return self._get(self.type_.generated_offsets[4])

            def set_thousands_separator(self, v: c_char) -> None:
                self._set(self.type_.generated_offsets[4], v)

            def columns_size(self) -> int:
                return self._get(self.type_.generated_offsets[5])

            def set_columns_size(self, v: int) -> None:
                self._set(self.type_.generated_offsets[5], v)

            def columns(self) -> std.core.Array:
                return self._get(self.type_.generated_offsets[6])

            def set_columns(self, v: std.core.Array) -> None:
                self._set(self.type_.generated_offsets[6], v)

            @staticmethod
            def generate(format: std.io.CsvFormat, ident_col: int, time_col: int, __greycat: Optional[GreyCat] = None) -> str:
                if __greycat is None:
                    __greycat = GreyCat.DEFAULT
                return __greycat.call("io::CsvFormat::generate", [format, ident_col, time_col, ])

            @staticmethod
            def validate(path: str, format: std.io.CsvFormat, max_rows: int, max_invalid: int, invalid_path: str, __greycat: Optional[GreyCat] = None) -> std.runtime.Task:
                if __greycat is None:
                    __greycat = GreyCat.DEFAULT
                return __greycat.call("io::CsvFormat::validate", [path, format, max_rows, max_invalid, invalid_path, ])

            @staticmethod
            def sample(path: str, format: std.io.CsvFormat, offset: int, max: int, __greycat: Optional[GreyCat] = None) -> std.core.Table:
                if __greycat is None:
                    __greycat = GreyCat.DEFAULT
                return __greycat.call("io::CsvFormat::sample", [path, format, offset, max, ])

            @staticmethod
            def infer(analysis: std.io.CsvStatistics, __greycat: Optional[GreyCat] = None) -> std.io.CsvFormat:
                if __greycat is None:
                    __greycat = GreyCat.DEFAULT
                return __greycat.call("io::CsvFormat::infer", [analysis, ])

            @staticmethod
            def create(header_lines: int, separator: c_char, string_delimiter: c_char, decimal_separator: c_char, thousands_separator: c_char, columns_size: int, columns: std.core.Array, greycat: Optional[GreyCat] = None) -> std.io.CsvFormat:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                return std.io.CsvFormat(greycat.libs_by_name[std.name_].mapped[67], [header_lines, separator, string_delimiter, decimal_separator, thousands_separator, columns_size, columns])

        @final
        class CsvColumnDuration(GreyCat.Object):
            name_: Final[str] = "io::CsvColumnDuration"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def name(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_name(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def mandatory(self) -> bool:
                return self._get(self.type_.generated_offsets[1])

            def set_mandatory(self, v: bool) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def offset(self) -> int:
                return self._get(self.type_.generated_offsets[2])

            def set_offset(self, v: int) -> None:
                self._set(self.type_.generated_offsets[2], v)

            def unit(self) -> std.core.DurationUnit:
                return self._get(self.type_.generated_offsets[3])

            def set_unit(self, v: std.core.DurationUnit) -> None:
                self._set(self.type_.generated_offsets[3], v)

            @staticmethod
            def create(name: str, mandatory: bool, offset: int, unit: std.core.DurationUnit, greycat: Optional[GreyCat] = None) -> std.io.CsvColumnDuration:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                return std.io.CsvColumnDuration(greycat.libs_by_name[std.name_].mapped[68], [name, mandatory, offset, unit])

        @final
        class CsvAnalysis(GreyCat.Object):
            name_: Final[str] = "io::CsvAnalysis"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def config(self) -> std.io.CsvAnalysisConfig:
                return self._get(self.type_.generated_offsets[0])

            def set_config(self, v: std.io.CsvAnalysisConfig) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def statistics(self) -> std.io.CsvStatistics:
                return self._get(self.type_.generated_offsets[1])

            def set_statistics(self, v: std.io.CsvStatistics) -> None:
                self._set(self.type_.generated_offsets[1], v)

            @staticmethod
            def analyze(file_path: str, config: std.io.CsvAnalysisConfig, __greycat: Optional[GreyCat] = None) -> std.runtime.Task:
                if __greycat is None:
                    __greycat = GreyCat.DEFAULT
                return __greycat.call("io::CsvAnalysis::analyze", [file_path, config, ])

            @staticmethod
            def create(config: std.io.CsvAnalysisConfig, statistics: std.io.CsvStatistics, greycat: Optional[GreyCat] = None) -> std.io.CsvAnalysis:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                return std.io.CsvAnalysis(greycat.libs_by_name[std.name_].mapped[69], [config, statistics])

        @final
        class CsvAnalysisConfig(GreyCat.Object):
            name_: Final[str] = "io::CsvAnalysisConfig"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def header_lines(self) -> int:
                return self._get(self.type_.generated_offsets[0])

            def set_header_lines(self, v: int) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def separator(self) -> c_char:
                return self._get(self.type_.generated_offsets[1])

            def set_separator(self, v: c_char) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def string_delimiter(self) -> c_char:
                return self._get(self.type_.generated_offsets[2])

            def set_string_delimiter(self, v: c_char) -> None:
                self._set(self.type_.generated_offsets[2], v)

            def decimal_separator(self) -> c_char:
                return self._get(self.type_.generated_offsets[3])

            def set_decimal_separator(self, v: c_char) -> None:
                self._set(self.type_.generated_offsets[3], v)

            def thousands_separator(self) -> c_char:
                return self._get(self.type_.generated_offsets[4])

            def set_thousands_separator(self, v: c_char) -> None:
                self._set(self.type_.generated_offsets[4], v)

            def row_limit(self) -> int:
                return self._get(self.type_.generated_offsets[5])

            def set_row_limit(self, v: int) -> None:
                self._set(self.type_.generated_offsets[5], v)

            def enumerable_limit(self) -> int:
                return self._get(self.type_.generated_offsets[6])

            def set_enumerable_limit(self, v: int) -> None:
                self._set(self.type_.generated_offsets[6], v)

            def date_check_limit(self) -> int:
                return self._get(self.type_.generated_offsets[7])

            def set_date_check_limit(self, v: int) -> None:
                self._set(self.type_.generated_offsets[7], v)

            def date_formats(self) -> std.core.Array:
                return self._get(self.type_.generated_offsets[8])

            def set_date_formats(self, v: std.core.Array) -> None:
                self._set(self.type_.generated_offsets[8], v)

            @staticmethod
            def enumerable_limit_default(greycat: Optional[GreyCat] = None) -> int:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[70]
                return t.static_values[0]

            @staticmethod
            def date_check_limit_default(greycat: Optional[GreyCat] = None) -> int:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[70]
                return t.static_values[1]

            @staticmethod
            def create(header_lines: int, separator: c_char, string_delimiter: c_char, decimal_separator: c_char, thousands_separator: c_char, row_limit: int, enumerable_limit: int, date_check_limit: int, date_formats: std.core.Array, greycat: Optional[GreyCat] = None) -> std.io.CsvAnalysisConfig:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                return std.io.CsvAnalysisConfig(greycat.libs_by_name[std.name_].mapped[70], [header_lines, separator, string_delimiter, decimal_separator, thousands_separator, row_limit, enumerable_limit, date_check_limit, date_formats])

        @final
        class SmtpAuth(GreyCat.Enum):
            name_: Final[str] = "io::SmtpAuth"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            @staticmethod
            def none(greycat: Optional[GreyCat] = None) -> std.io.SmtpAuth:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[71]
                return t.enum_values[t.generated_offsets[0]]

            @staticmethod
            def plain(greycat: Optional[GreyCat] = None) -> std.io.SmtpAuth:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[71]
                return t.enum_values[t.generated_offsets[1]]

            @staticmethod
            def login(greycat: Optional[GreyCat] = None) -> std.io.SmtpAuth:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[71]
                return t.enum_values[t.generated_offsets[2]]

            @staticmethod
            def create(greycat: Optional[GreyCat] = None) -> std.io.SmtpAuth:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                return std.io.SmtpAuth(greycat.libs_by_name[std.name_].mapped[71], [])

        @final
        class Http(GreyCat.Object):
            name_: Final[str] = "io::Http"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            @staticmethod
            def create(greycat: Optional[GreyCat] = None) -> std.io.Http:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                return std.io.Http(greycat.libs_by_name[std.name_].mapped[72], [])

        @final
        class Smtp(GreyCat.Object):
            name_: Final[str] = "io::Smtp"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def host(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_host(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def port(self) -> int:
                return self._get(self.type_.generated_offsets[1])

            def set_port(self, v: int) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def mode(self) -> std.io.SmtpMode:
                return self._get(self.type_.generated_offsets[2])

            def set_mode(self, v: std.io.SmtpMode) -> None:
                self._set(self.type_.generated_offsets[2], v)

            def authenticate(self) -> std.io.SmtpAuth:
                return self._get(self.type_.generated_offsets[3])

            def set_authenticate(self, v: std.io.SmtpAuth) -> None:
                self._set(self.type_.generated_offsets[3], v)

            def user(self) -> str:
                return self._get(self.type_.generated_offsets[4])

            def set_user(self, v: str) -> None:
                self._set(self.type_.generated_offsets[4], v)

            def pass_(self) -> str:
                return self._get(self.type_.generated_offsets[5])

            def set_pass(self, v: str) -> None:
                self._set(self.type_.generated_offsets[5], v)

            @staticmethod
            def create(host: str, port: int, mode: std.io.SmtpMode, authenticate: std.io.SmtpAuth, user: str, pass_: str, greycat: Optional[GreyCat] = None) -> std.io.Smtp:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                return std.io.Smtp(greycat.libs_by_name[std.name_].mapped[73], [host, port, mode, authenticate, user, pass_])

        @final
        class Mqtt(GreyCat.Object):
            name_: Final[str] = "io::Mqtt"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            @staticmethod
            def create(greycat: Optional[GreyCat] = None) -> std.io.Mqtt:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                return std.io.Mqtt(greycat.libs_by_name[std.name_].mapped[74], [])

        @final
        class TextEncoder(GreyCat.Enum):
            name_: Final[str] = "io::TextEncoder"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            @staticmethod
            def plain(greycat: Optional[GreyCat] = None) -> std.io.TextEncoder:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[75]
                return t.enum_values[t.generated_offsets[0]]

            @staticmethod
            def base64(greycat: Optional[GreyCat] = None) -> std.io.TextEncoder:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[75]
                return t.enum_values[t.generated_offsets[1]]

            @staticmethod
            def base64url(greycat: Optional[GreyCat] = None) -> std.io.TextEncoder:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[75]
                return t.enum_values[t.generated_offsets[2]]

            @staticmethod
            def hexadecimal(greycat: Optional[GreyCat] = None) -> std.io.TextEncoder:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[75]
                return t.enum_values[t.generated_offsets[3]]

            @staticmethod
            def create(greycat: Optional[GreyCat] = None) -> std.io.TextEncoder:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                return std.io.TextEncoder(greycat.libs_by_name[std.name_].mapped[75], [])

        @final
        class CsvColumnStatistics(GreyCat.Object):
            name_: Final[str] = "io::CsvColumnStatistics"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def name(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_name(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def example(self) -> Any:
                return self._get(self.type_.generated_offsets[1])

            def set_example(self, v: Any) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def null_count(self) -> int:
                return self._get(self.type_.generated_offsets[2])

            def set_null_count(self, v: int) -> None:
                self._set(self.type_.generated_offsets[2], v)

            def bool_count(self) -> int:
                return self._get(self.type_.generated_offsets[3])

            def set_bool_count(self, v: int) -> None:
                self._set(self.type_.generated_offsets[3], v)

            def int_count(self) -> int:
                return self._get(self.type_.generated_offsets[4])

            def set_int_count(self, v: int) -> None:
                self._set(self.type_.generated_offsets[4], v)

            def float_count(self) -> int:
                return self._get(self.type_.generated_offsets[5])

            def set_float_count(self, v: int) -> None:
                self._set(self.type_.generated_offsets[5], v)

            def string_count(self) -> int:
                return self._get(self.type_.generated_offsets[6])

            def set_string_count(self, v: int) -> None:
                self._set(self.type_.generated_offsets[6], v)

            def date_count(self) -> int:
                return self._get(self.type_.generated_offsets[7])

            def set_date_count(self, v: int) -> None:
                self._set(self.type_.generated_offsets[7], v)

            def date_format_count(self) -> std.core.Map:
                return self._get(self.type_.generated_offsets[8])

            def set_date_format_count(self, v: std.core.Map) -> None:
                self._set(self.type_.generated_offsets[8], v)

            def enumerable_count(self) -> std.core.Map:
                return self._get(self.type_.generated_offsets[9])

            def set_enumerable_count(self, v: std.core.Map) -> None:
                self._set(self.type_.generated_offsets[9], v)

            def profile(self) -> std.util.Gaussian:
                return self._get(self.type_.generated_offsets[10])

            def set_profile(self, v: std.util.Gaussian) -> None:
                self._set(self.type_.generated_offsets[10], v)

            @staticmethod
            def create(name: str, example: Any, null_count: int, bool_count: int, int_count: int, float_count: int, string_count: int, date_count: int, date_format_count: std.core.Map, enumerable_count: std.core.Map, profile: std.util.Gaussian, greycat: Optional[GreyCat] = None) -> std.io.CsvColumnStatistics:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                return std.io.CsvColumnStatistics(greycat.libs_by_name[std.name_].mapped[76], [name, example, null_count, bool_count, int_count, float_count, string_count, date_count, date_format_count, enumerable_count, profile])

        @final
        class CsvColumnIgnored(GreyCat.Object):
            name_: Final[str] = "io::CsvColumnIgnored"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def name(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_name(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def mandatory(self) -> bool:
                return self._get(self.type_.generated_offsets[1])

            def set_mandatory(self, v: bool) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def offset(self) -> int:
                return self._get(self.type_.generated_offsets[2])

            def set_offset(self, v: int) -> None:
                self._set(self.type_.generated_offsets[2], v)

            @staticmethod
            def create(name: str, mandatory: bool, offset: int, greycat: Optional[GreyCat] = None) -> std.io.CsvColumnIgnored:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                return std.io.CsvColumnIgnored(greycat.libs_by_name[std.name_].mapped[77], [name, mandatory, offset])

        @final
        class CsvColumnTime(GreyCat.Object):
            name_: Final[str] = "io::CsvColumnTime"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def name(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_name(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def mandatory(self) -> bool:
                return self._get(self.type_.generated_offsets[1])

            def set_mandatory(self, v: bool) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def offset(self) -> int:
                return self._get(self.type_.generated_offsets[2])

            def set_offset(self, v: int) -> None:
                self._set(self.type_.generated_offsets[2], v)

            def unit(self) -> std.core.DurationUnit:
                return self._get(self.type_.generated_offsets[3])

            def set_unit(self, v: std.core.DurationUnit) -> None:
                self._set(self.type_.generated_offsets[3], v)

            @staticmethod
            def create(name: str, mandatory: bool, offset: int, unit: std.core.DurationUnit, greycat: Optional[GreyCat] = None) -> std.io.CsvColumnTime:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                return std.io.CsvColumnTime(greycat.libs_by_name[std.name_].mapped[78], [name, mandatory, offset, unit])

        @final
        class Url(GreyCat.Object):
            name_: Final[str] = "io::Url"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def protocol(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_protocol(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def host(self) -> str:
                return self._get(self.type_.generated_offsets[1])

            def set_host(self, v: str) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def port(self) -> int:
                return self._get(self.type_.generated_offsets[2])

            def set_port(self, v: int) -> None:
                self._set(self.type_.generated_offsets[2], v)

            def path(self) -> str:
                return self._get(self.type_.generated_offsets[3])

            def set_path(self, v: str) -> None:
                self._set(self.type_.generated_offsets[3], v)

            def params(self) -> std.core.Map:
                return self._get(self.type_.generated_offsets[4])

            def set_params(self, v: std.core.Map) -> None:
                self._set(self.type_.generated_offsets[4], v)

            def hash(self) -> str:
                return self._get(self.type_.generated_offsets[5])

            def set_hash(self, v: str) -> None:
                self._set(self.type_.generated_offsets[5], v)

            @staticmethod
            def create(protocol: str, host: str, port: int, path: str, params: std.core.Map, hash: str, greycat: Optional[GreyCat] = None) -> std.io.Url:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                return std.io.Url(greycat.libs_by_name[std.name_].mapped[79], [protocol, host, port, path, params, hash])

        @final
        class Email(GreyCat.Object):
            name_: Final[str] = "io::Email"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def from_(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_from(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def subject(self) -> str:
                return self._get(self.type_.generated_offsets[1])

            def set_subject(self, v: str) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def body(self) -> str:
                return self._get(self.type_.generated_offsets[2])

            def set_body(self, v: str) -> None:
                self._set(self.type_.generated_offsets[2], v)

            def body_is_html(self) -> bool:
                return self._get(self.type_.generated_offsets[3])

            def set_body_is_html(self, v: bool) -> None:
                self._set(self.type_.generated_offsets[3], v)

            def to(self) -> std.core.Array:
                return self._get(self.type_.generated_offsets[4])

            def set_to(self, v: std.core.Array) -> None:
                self._set(self.type_.generated_offsets[4], v)

            def cc(self) -> std.core.Array:
                return self._get(self.type_.generated_offsets[5])

            def set_cc(self, v: std.core.Array) -> None:
                self._set(self.type_.generated_offsets[5], v)

            def bcc(self) -> std.core.Array:
                return self._get(self.type_.generated_offsets[6])

            def set_bcc(self, v: std.core.Array) -> None:
                self._set(self.type_.generated_offsets[6], v)

            @staticmethod
            def create(from_: str, subject: str, body: str, body_is_html: bool, to: std.core.Array, cc: std.core.Array, bcc: std.core.Array, greycat: Optional[GreyCat] = None) -> std.io.Email:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                return std.io.Email(greycat.libs_by_name[std.name_].mapped[80], [from_, subject, body, body_is_html, to, cc, bcc])

        @final
        class CsvValidateResult(GreyCat.Object):
            name_: Final[str] = "io::CsvValidateResult"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def line_count(self) -> int:
                return self._get(self.type_.generated_offsets[0])

            def set_line_count(self, v: int) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def fail_count(self) -> int:
                return self._get(self.type_.generated_offsets[1])

            def set_fail_count(self, v: int) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def invalid_count(self) -> std.core.Array:
                return self._get(self.type_.generated_offsets[2])

            def set_invalid_count(self, v: std.core.Array) -> None:
                self._set(self.type_.generated_offsets[2], v)

            @staticmethod
            def create(line_count: int, fail_count: int, invalid_count: std.core.Array, greycat: Optional[GreyCat] = None) -> std.io.CsvValidateResult:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                return std.io.CsvValidateResult(greycat.libs_by_name[std.name_].mapped[81], [line_count, fail_count, invalid_count])

        @final
        class CsvColumnBoolean(GreyCat.Object):
            name_: Final[str] = "io::CsvColumnBoolean"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def name(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_name(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def mandatory(self) -> bool:
                return self._get(self.type_.generated_offsets[1])

            def set_mandatory(self, v: bool) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def offset(self) -> int:
                return self._get(self.type_.generated_offsets[2])

            def set_offset(self, v: int) -> None:
                self._set(self.type_.generated_offsets[2], v)

            @staticmethod
            def create(name: str, mandatory: bool, offset: int, greycat: Optional[GreyCat] = None) -> std.io.CsvColumnBoolean:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                return std.io.CsvColumnBoolean(greycat.libs_by_name[std.name_].mapped[82], [name, mandatory, offset])

        @final
        class CsvColumn(GreyCat.Object):
            name_: Final[str] = "io::CsvColumn"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def name(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_name(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def mandatory(self) -> bool:
                return self._get(self.type_.generated_offsets[1])

            def set_mandatory(self, v: bool) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def offset(self) -> int:
                return self._get(self.type_.generated_offsets[2])

            def set_offset(self, v: int) -> None:
                self._set(self.type_.generated_offsets[2], v)

            @staticmethod
            def create(name: str, mandatory: bool, offset: int, greycat: Optional[GreyCat] = None) -> std.io.CsvColumn:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                return std.io.CsvColumn(greycat.libs_by_name[std.name_].mapped[83], [name, mandatory, offset])

        @final
        class SmtpMode(GreyCat.Enum):
            name_: Final[str] = "io::SmtpMode"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            @staticmethod
            def plain(greycat: Optional[GreyCat] = None) -> std.io.SmtpMode:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[84]
                return t.enum_values[t.generated_offsets[0]]

            @staticmethod
            def ssl_tls(greycat: Optional[GreyCat] = None) -> std.io.SmtpMode:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[84]
                return t.enum_values[t.generated_offsets[1]]

            @staticmethod
            def starttls(greycat: Optional[GreyCat] = None) -> std.io.SmtpMode:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[84]
                return t.enum_values[t.generated_offsets[2]]

            @staticmethod
            def create(greycat: Optional[GreyCat] = None) -> std.io.SmtpMode:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                return std.io.SmtpMode(greycat.libs_by_name[std.name_].mapped[84], [])

    @final
    class math:

        @final
        class MathConstants(GreyCat.Object):
            name_: Final[str] = "math::MathConstants"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            @staticmethod
            def e(greycat: Optional[GreyCat] = None) -> float:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[85]
                return t.static_values[0]

            @staticmethod
            def log_2e(greycat: Optional[GreyCat] = None) -> float:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[85]
                return t.static_values[1]

            @staticmethod
            def log_10e(greycat: Optional[GreyCat] = None) -> float:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[85]
                return t.static_values[2]

            @staticmethod
            def ln2(greycat: Optional[GreyCat] = None) -> float:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[85]
                return t.static_values[3]

            @staticmethod
            def ln10(greycat: Optional[GreyCat] = None) -> float:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[85]
                return t.static_values[4]

            @staticmethod
            def pi(greycat: Optional[GreyCat] = None) -> float:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[85]
                return t.static_values[5]

            @staticmethod
            def pi_2(greycat: Optional[GreyCat] = None) -> float:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[85]
                return t.static_values[6]

            @staticmethod
            def pi_4(greycat: Optional[GreyCat] = None) -> float:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[85]
                return t.static_values[7]

            @staticmethod
            def m1_pi(greycat: Optional[GreyCat] = None) -> float:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[85]
                return t.static_values[8]

            @staticmethod
            def m2_pi(greycat: Optional[GreyCat] = None) -> float:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[85]
                return t.static_values[9]

            @staticmethod
            def m2_sqrt_pi(greycat: Optional[GreyCat] = None) -> float:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[85]
                return t.static_values[10]

            @staticmethod
            def sqrt2(greycat: Optional[GreyCat] = None) -> float:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[85]
                return t.static_values[11]

            @staticmethod
            def sqrt1_2(greycat: Optional[GreyCat] = None) -> float:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[85]
                return t.static_values[12]

            @staticmethod
            def create(greycat: Optional[GreyCat] = None) -> std.math.MathConstants:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                return std.math.MathConstants(greycat.libs_by_name[std.name_].mapped[85], [])

    @final
    class util:
        __T = TypeVar("__T")

        @final
        class Random(GreyCat.Object):
            name_: Final[str] = "util::Random"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def seed(self) -> int:
                return self._get(self.type_.generated_offsets[0])

            def set_seed(self, v: int) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def v(self) -> float:
                return self._get(self.type_.generated_offsets[1])

            def set_v(self, v: float) -> None:
                self._set(self.type_.generated_offsets[1], v)

            @staticmethod
            def create(seed: int, v: float, greycat: Optional[GreyCat] = None) -> std.util.Random:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                return std.util.Random(greycat.libs_by_name[std.name_].mapped[86], [seed, v])

        @final
        class Iban(std_n.util._Iban):
            name_: Final[str] = "util::Iban"

            def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
                super().__init__(type)

            @staticmethod
            def create(greycat: Optional[GreyCat] = None) -> std_n.util._Iban:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                return std.util.Iban(greycat.libs_by_name[std.name_].mapped[87], [])

        @final
        class Gaussian(GreyCat.Object):
            name_: Final[str] = "util::Gaussian"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def sum(self) -> float:
                return self._get(self.type_.generated_offsets[0])

            def set_sum(self, v: float) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def sum_sq(self) -> float:
                return self._get(self.type_.generated_offsets[1])

            def set_sum_sq(self, v: float) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def count(self) -> int:
                return self._get(self.type_.generated_offsets[2])

            def set_count(self, v: int) -> None:
                self._set(self.type_.generated_offsets[2], v)

            def min(self) -> float:
                return self._get(self.type_.generated_offsets[3])

            def set_min(self, v: float) -> None:
                self._set(self.type_.generated_offsets[3], v)

            def max(self) -> float:
                return self._get(self.type_.generated_offsets[4])

            def set_max(self, v: float) -> None:
                self._set(self.type_.generated_offsets[4], v)

            @staticmethod
            def create(sum: float, sum_sq: float, count: int, min: float, max: float, greycat: Optional[GreyCat] = None) -> std.util.Gaussian:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                return std.util.Gaussian(greycat.libs_by_name[std.name_].mapped[88], [sum, sum_sq, count, min, max])

        @final
        class HistogramFloat(std_n.util._HistogramFloat):
            name_: Final[str] = "util::HistogramFloat"

            def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
                super().__init__(type)

            @staticmethod
            def create(greycat: Optional[GreyCat] = None) -> std_n.util._HistogramFloat:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                return std.util.HistogramFloat(greycat.libs_by_name[std.name_].mapped[89], [])

        @final
        class BoxPlotInt(GreyCat.Object):
            name_: Final[str] = "util::BoxPlotInt"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def min(self) -> int:
                return self._get(self.type_.generated_offsets[0])

            def set_min(self, v: int) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def max(self) -> int:
                return self._get(self.type_.generated_offsets[1])

            def set_max(self, v: int) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def whiskerLow(self) -> int:
                return self._get(self.type_.generated_offsets[2])

            def set_whiskerLow(self, v: int) -> None:
                self._set(self.type_.generated_offsets[2], v)

            def whiskerHigh(self) -> int:
                return self._get(self.type_.generated_offsets[3])

            def set_whiskerHigh(self, v: int) -> None:
                self._set(self.type_.generated_offsets[3], v)

            def percentile1(self) -> int:
                return self._get(self.type_.generated_offsets[4])

            def set_percentile1(self, v: int) -> None:
                self._set(self.type_.generated_offsets[4], v)

            def percentile5(self) -> int:
                return self._get(self.type_.generated_offsets[5])

            def set_percentile5(self, v: int) -> None:
                self._set(self.type_.generated_offsets[5], v)

            def percentile25(self) -> int:
                return self._get(self.type_.generated_offsets[6])

            def set_percentile25(self, v: int) -> None:
                self._set(self.type_.generated_offsets[6], v)

            def percentile50(self) -> int:
                return self._get(self.type_.generated_offsets[7])

            def set_percentile50(self, v: int) -> None:
                self._set(self.type_.generated_offsets[7], v)

            def percentile75(self) -> int:
                return self._get(self.type_.generated_offsets[8])

            def set_percentile75(self, v: int) -> None:
                self._set(self.type_.generated_offsets[8], v)

            def percentile95(self) -> int:
                return self._get(self.type_.generated_offsets[9])

            def set_percentile95(self, v: int) -> None:
                self._set(self.type_.generated_offsets[9], v)

            def percentile99(self) -> int:
                return self._get(self.type_.generated_offsets[10])

            def set_percentile99(self, v: int) -> None:
                self._set(self.type_.generated_offsets[10], v)

            def countOutliersLow(self) -> int:
                return self._get(self.type_.generated_offsets[11])

            def set_countOutliersLow(self, v: int) -> None:
                self._set(self.type_.generated_offsets[11], v)

            def countOutliersHigh(self) -> int:
                return self._get(self.type_.generated_offsets[12])

            def set_countOutliersHigh(self, v: int) -> None:
                self._set(self.type_.generated_offsets[12], v)

            def percentageOutliersLow(self) -> float:
                return self._get(self.type_.generated_offsets[13])

            def set_percentageOutliersLow(self, v: float) -> None:
                self._set(self.type_.generated_offsets[13], v)

            def percentageOutliersHigh(self) -> float:
                return self._get(self.type_.generated_offsets[14])

            def set_percentageOutliersHigh(self, v: float) -> None:
                self._set(self.type_.generated_offsets[14], v)

            def sum(self) -> float:
                return self._get(self.type_.generated_offsets[15])

            def set_sum(self, v: float) -> None:
                self._set(self.type_.generated_offsets[15], v)

            def avg(self) -> float:
                return self._get(self.type_.generated_offsets[16])

            def set_avg(self, v: float) -> None:
                self._set(self.type_.generated_offsets[16], v)

            def std(self) -> float:
                return self._get(self.type_.generated_offsets[17])

            def set_std(self, v: float) -> None:
                self._set(self.type_.generated_offsets[17], v)

            def size(self) -> int:
                return self._get(self.type_.generated_offsets[18])

            def set_size(self, v: int) -> None:
                self._set(self.type_.generated_offsets[18], v)

            @staticmethod
            def create(min: int, max: int, whiskerLow: int, whiskerHigh: int, percentile1: int, percentile5: int, percentile25: int, percentile50: int, percentile75: int, percentile95: int, percentile99: int, countOutliersLow: int, countOutliersHigh: int, percentageOutliersLow: float, percentageOutliersHigh: float, sum: float, avg: float, std: float, size: int, greycat: Optional[GreyCat] = None) -> std.util.BoxPlotInt:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                return std.util.BoxPlotInt(greycat.libs_by_name[std.name_].mapped[90], [min, max, whiskerLow, whiskerHigh, percentile1, percentile5, percentile25, percentile50, percentile75, percentile95, percentile99, countOutliersLow, countOutliersHigh, percentageOutliersLow, percentageOutliersHigh, sum, avg, std, size])

        @final
        class BoxPlotFloat(GreyCat.Object):
            name_: Final[str] = "util::BoxPlotFloat"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def min(self) -> float:
                return self._get(self.type_.generated_offsets[0])

            def set_min(self, v: float) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def max(self) -> float:
                return self._get(self.type_.generated_offsets[1])

            def set_max(self, v: float) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def whiskerLow(self) -> float:
                return self._get(self.type_.generated_offsets[2])

            def set_whiskerLow(self, v: float) -> None:
                self._set(self.type_.generated_offsets[2], v)

            def whiskerHigh(self) -> float:
                return self._get(self.type_.generated_offsets[3])

            def set_whiskerHigh(self, v: float) -> None:
                self._set(self.type_.generated_offsets[3], v)

            def percentile1(self) -> float:
                return self._get(self.type_.generated_offsets[4])

            def set_percentile1(self, v: float) -> None:
                self._set(self.type_.generated_offsets[4], v)

            def percentile5(self) -> float:
                return self._get(self.type_.generated_offsets[5])

            def set_percentile5(self, v: float) -> None:
                self._set(self.type_.generated_offsets[5], v)

            def percentile25(self) -> float:
                return self._get(self.type_.generated_offsets[6])

            def set_percentile25(self, v: float) -> None:
                self._set(self.type_.generated_offsets[6], v)

            def percentile50(self) -> float:
                return self._get(self.type_.generated_offsets[7])

            def set_percentile50(self, v: float) -> None:
                self._set(self.type_.generated_offsets[7], v)

            def percentile75(self) -> float:
                return self._get(self.type_.generated_offsets[8])

            def set_percentile75(self, v: float) -> None:
                self._set(self.type_.generated_offsets[8], v)

            def percentile95(self) -> float:
                return self._get(self.type_.generated_offsets[9])

            def set_percentile95(self, v: float) -> None:
                self._set(self.type_.generated_offsets[9], v)

            def percentile99(self) -> float:
                return self._get(self.type_.generated_offsets[10])

            def set_percentile99(self, v: float) -> None:
                self._set(self.type_.generated_offsets[10], v)

            def countOutliersLow(self) -> int:
                return self._get(self.type_.generated_offsets[11])

            def set_countOutliersLow(self, v: int) -> None:
                self._set(self.type_.generated_offsets[11], v)

            def countOutliersHigh(self) -> int:
                return self._get(self.type_.generated_offsets[12])

            def set_countOutliersHigh(self, v: int) -> None:
                self._set(self.type_.generated_offsets[12], v)

            def percentageOutliersLow(self) -> float:
                return self._get(self.type_.generated_offsets[13])

            def set_percentageOutliersLow(self, v: float) -> None:
                self._set(self.type_.generated_offsets[13], v)

            def percentageOutliersHigh(self) -> float:
                return self._get(self.type_.generated_offsets[14])

            def set_percentageOutliersHigh(self, v: float) -> None:
                self._set(self.type_.generated_offsets[14], v)

            def sum(self) -> float:
                return self._get(self.type_.generated_offsets[15])

            def set_sum(self, v: float) -> None:
                self._set(self.type_.generated_offsets[15], v)

            def avg(self) -> float:
                return self._get(self.type_.generated_offsets[16])

            def set_avg(self, v: float) -> None:
                self._set(self.type_.generated_offsets[16], v)

            def std(self) -> float:
                return self._get(self.type_.generated_offsets[17])

            def set_std(self, v: float) -> None:
                self._set(self.type_.generated_offsets[17], v)

            def size(self) -> int:
                return self._get(self.type_.generated_offsets[18])

            def set_size(self, v: int) -> None:
                self._set(self.type_.generated_offsets[18], v)

            @staticmethod
            def create(min: float, max: float, whiskerLow: float, whiskerHigh: float, percentile1: float, percentile5: float, percentile25: float, percentile50: float, percentile75: float, percentile95: float, percentile99: float, countOutliersLow: int, countOutliersHigh: int, percentageOutliersLow: float, percentageOutliersHigh: float, sum: float, avg: float, std: float, size: int, greycat: Optional[GreyCat] = None) -> std.util.BoxPlotFloat:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                return std.util.BoxPlotFloat(greycat.libs_by_name[std.name_].mapped[91], [min, max, whiskerLow, whiskerHigh, percentile1, percentile5, percentile25, percentile50, percentile75, percentile95, percentile99, countOutliersLow, countOutliersHigh, percentageOutliersLow, percentageOutliersHigh, sum, avg, std, size])

        @final
        class GaussianProfile(std_n.util._GaussianProfile):
            name_: Final[str] = "util::GaussianProfile"

            def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
                super().__init__(type)

            @staticmethod
            def create(greycat: Optional[GreyCat] = None) -> std_n.util._GaussianProfile:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                return std.util.GaussianProfile(greycat.libs_by_name[std.name_].mapped[92], [])

        @final
        class ProgressTracker(GreyCat.Object):
            name_: Final[str] = "util::ProgressTracker"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def start(self) -> std.core.time:
                return self._get(self.type_.generated_offsets[0])

            def set_start(self, v: std.core.time) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def total(self) -> int:
                return self._get(self.type_.generated_offsets[1])

            def set_total(self, v: int) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def counter(self) -> int:
                return self._get(self.type_.generated_offsets[2])

            def set_counter(self, v: int) -> None:
                self._set(self.type_.generated_offsets[2], v)

            def duration(self) -> std.core.duration:
                return self._get(self.type_.generated_offsets[3])

            def set_duration(self, v: std.core.duration) -> None:
                self._set(self.type_.generated_offsets[3], v)

            def progress(self) -> float:
                return self._get(self.type_.generated_offsets[4])

            def set_progress(self, v: float) -> None:
                self._set(self.type_.generated_offsets[4], v)

            def speed(self) -> float:
                return self._get(self.type_.generated_offsets[5])

            def set_speed(self, v: float) -> None:
                self._set(self.type_.generated_offsets[5], v)

            def remaining(self) -> std.core.duration:
                return self._get(self.type_.generated_offsets[6])

            def set_remaining(self, v: std.core.duration) -> None:
                self._set(self.type_.generated_offsets[6], v)

            @staticmethod
            def create(start: std.core.time, total: int, counter: int, duration: std.core.duration, progress: float, speed: float, remaining: std.core.duration, greycat: Optional[GreyCat] = None) -> std.util.ProgressTracker:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                return std.util.ProgressTracker(greycat.libs_by_name[std.name_].mapped[93], [start, total, counter, duration, progress, speed, remaining])

        @final
        class Buffer(std_n.util._Buffer):
            name_: Final[str] = "util::Buffer"

            def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
                super().__init__(type)

            @staticmethod
            def create(greycat: Optional[GreyCat] = None) -> std_n.util._Buffer:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                return std.util.Buffer(greycat.libs_by_name[std.name_].mapped[94], [])

        @final
        class DenseDim(GreyCat.Object):
            name_: Final[str] = "util::DenseDim"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def min(self) -> int:
                return self._get(self.type_.generated_offsets[0])

            def set_min(self, v: int) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def max(self) -> int:
                return self._get(self.type_.generated_offsets[1])

            def set_max(self, v: int) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def step(self) -> int:
                return self._get(self.type_.generated_offsets[2])

            def set_step(self, v: int) -> None:
                self._set(self.type_.generated_offsets[2], v)

            @staticmethod
            def create(min: int, max: int, step: int, greycat: Optional[GreyCat] = None) -> std.util.DenseDim:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                return std.util.DenseDim(greycat.libs_by_name[std.name_].mapped[95], [min, max, step])

        @final
        class HistogramInt(std_n.util._HistogramInt):
            name_: Final[str] = "util::HistogramInt"

            def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
                super().__init__(type)

            @staticmethod
            def create(greycat: Optional[GreyCat] = None) -> std_n.util._HistogramInt:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                return std.util.HistogramInt(greycat.libs_by_name[std.name_].mapped[96], [])

        @final
        class SlidingWindow(std_n.util._SlidingWindow):
            name_: Final[str] = "util::SlidingWindow"

            def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
                super().__init__(type)

            @staticmethod
            def create(greycat: Optional[GreyCat] = None) -> std_n.util._SlidingWindow:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                return std.util.SlidingWindow(greycat.libs_by_name[std.name_].mapped[97], [])

        @final
        class Queue(Generic[__T], std_n.util._Queue[__T]):
            name_: Final[str] = "util::Queue"

            def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
                super().__init__(type)

            @staticmethod
            def create(greycat: Optional[GreyCat] = None) -> std_n.util._Queue:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                return std.util.Queue(greycat.libs_by_name[std.name_].mapped[98], [])

        @final
        class Plot(GreyCat.Object):
            name_: Final[str] = "util::Plot"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            @staticmethod
            def create(greycat: Optional[GreyCat] = None) -> std.util.Plot:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                return std.util.Plot(greycat.libs_by_name[std.name_].mapped[99], [])

        @final
        class TimeWindow(std_n.util._TimeWindow):
            name_: Final[str] = "util::TimeWindow"

            def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
                super().__init__(type)

            @staticmethod
            def create(greycat: Optional[GreyCat] = None) -> std_n.util._TimeWindow:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                return std.util.TimeWindow(greycat.libs_by_name[std.name_].mapped[100], [])

        @final
        class Assert(GreyCat.Object):
            name_: Final[str] = "util::Assert"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            @staticmethod
            def create(greycat: Optional[GreyCat] = None) -> std.util.Assert:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                return std.util.Assert(greycat.libs_by_name[std.name_].mapped[101], [])

        @final
        class Crypto(GreyCat.Object):
            name_: Final[str] = "util::Crypto"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            @staticmethod
            def create(greycat: Optional[GreyCat] = None) -> std.util.Crypto:
                if greycat is None:
                    greycat = GreyCat.DEFAULT
                return std.util.Crypto(greycat.libs_by_name[std.name_].mapped[102], [])

    def configure(self, loaders: dict[str, GreyCat.Loader], factories: dict[str, GreyCat.Factory]) -> None:
        factories[std.core.GeoBox.name_] = lambda type, attributes: std.core.GeoBox(type, attributes)
        factories[std.core.Error.name_] = lambda type, attributes: std.core.Error(type, attributes)
        loaders[std.core.Error.name_] = lambda type, stream: std_n.core._Error.load(type, stream)
        factories[std.core.tf2d.name_] = lambda type, attributes: std.core.tf2d(type, attributes)
        loaders[std.core.tf2d.name_] = lambda type, stream: std_n.core._tf2d.load(type, stream)
        factories[std.core.Array.name_] = lambda type, attributes: std.core.Array(type, attributes)
        loaders[std.core.Array.name_] = lambda type, stream: std_n.core._Array.load(type, stream)
        factories[std.core.String.name_] = lambda type, attributes: std.core.String(type, attributes)
        loaders[std.core.String.name_] = lambda type, stream: std_n.core._String.load(type, stream)
        factories[std.core.Date.name_] = lambda type, attributes: std.core.Date(type, attributes)
        loaders[std.core.Date.name_] = lambda type, stream: std_n.core._Date.load(type, stream)
        factories[std.core.GeoPoly.name_] = lambda type, attributes: std.core.GeoPoly(type, attributes)
        factories[std.core.ti5d.name_] = lambda type, attributes: std.core.ti5d(type, attributes)
        loaders[std.core.ti5d.name_] = lambda type, stream: std_n.core._ti5d.load(type, stream)
        factories[std.core.nodeTime.name_] = lambda type, attributes: std.core.nodeTime(type, attributes)
        loaders[std.core.nodeTime.name_] = lambda type, stream: std_n.core._nodeTime.load(type, stream)
        factories[std.core.TimeZone.name_] = lambda type, attributes: std.core.TimeZone(type, attributes)
        factories[std.core.Table.name_] = lambda type, attributes: std.core.Table(type, attributes)
        loaders[std.core.Table.name_] = lambda type, stream: std_n.core._Table.load(type, stream)
        factories[std.core.ti10d.name_] = lambda type, attributes: std.core.ti10d(type, attributes)
        loaders[std.core.ti10d.name_] = lambda type, stream: std_n.core._ti10d.load(type, stream)
        factories[std.core.duration.name_] = lambda type, attributes: std.core.duration(type, attributes)
        loaders[std.core.duration.name_] = lambda type, stream: std_n.core._duration.load(type, stream)
        factories[std.core.DurationUnit.name_] = lambda type, attributes: std.core.DurationUnit(type, attributes)
        factories[std.core.Tensor.name_] = lambda type, attributes: std.core.Tensor(type, attributes)
        loaders[std.core.Tensor.name_] = lambda type, stream: std_n.core._Tensor.load(type, stream)
        factories[std.core.nodeIndex.name_] = lambda type, attributes: std.core.nodeIndex(type, attributes)
        loaders[std.core.nodeIndex.name_] = lambda type, stream: std_n.core._nodeIndex.load(type, stream)
        factories[std.core.TableColumnMapping.name_] = lambda type, attributes: std.core.TableColumnMapping(type, attributes)
        factories[std.core.nodeList.name_] = lambda type, attributes: std.core.nodeList(type, attributes)
        loaders[std.core.nodeList.name_] = lambda type, stream: std_n.core._nodeList.load(type, stream)
        factories[std.core.TensorType.name_] = lambda type, attributes: std.core.TensorType(type, attributes)
        factories[std.core.Tuple.name_] = lambda type, attributes: std.core.Tuple(type, attributes)
        factories[std.core.ti2d.name_] = lambda type, attributes: std.core.ti2d(type, attributes)
        loaders[std.core.ti2d.name_] = lambda type, stream: std_n.core._ti2d.load(type, stream)
        factories[std.core.tf4d.name_] = lambda type, attributes: std.core.tf4d(type, attributes)
        loaders[std.core.tf4d.name_] = lambda type, stream: std_n.core._tf4d.load(type, stream)
        factories[std.core.DatePart.name_] = lambda type, attributes: std.core.DatePart(type, attributes)
        factories[std.core.function.name_] = lambda type, attributes: std.core.function(type, attributes)
        loaders[std.core.function.name_] = lambda type, stream: std_n.core._function.load(type, stream)
        factories[std.core.ti3d.name_] = lambda type, attributes: std.core.ti3d(type, attributes)
        loaders[std.core.ti3d.name_] = lambda type, stream: std_n.core._ti3d.load(type, stream)
        factories[std.core.TableColumnMeta.name_] = lambda type, attributes: std.core.TableColumnMeta(type, attributes)
        factories[std.core.nodeGeo.name_] = lambda type, attributes: std.core.nodeGeo(type, attributes)
        loaders[std.core.nodeGeo.name_] = lambda type, stream: std_n.core._nodeGeo.load(type, stream)
        factories[std.core.node.name_] = lambda type, attributes: std.core.node(type, attributes)
        loaders[std.core.node.name_] = lambda type, stream: std_n.core._node.load(type, stream)
        factories[std.core.tf3d.name_] = lambda type, attributes: std.core.tf3d(type, attributes)
        loaders[std.core.tf3d.name_] = lambda type, stream: std_n.core._tf3d.load(type, stream)
        factories[std.core.nodeIndexBucket.name_] = lambda type, attributes: std.core.nodeIndexBucket(type, attributes)
        loaders[std.core.nodeIndexBucket.name_] = lambda type, stream: std_n.core._nodeIndexBucket.load(type, stream)
        factories[std.core.time.name_] = lambda type, attributes: std.core.time(type, attributes)
        loaders[std.core.time.name_] = lambda type, stream: std_n.core._time.load(type, stream)
        factories[std.core.SamplingMode.name_] = lambda type, attributes: std.core.SamplingMode(type, attributes)
        factories[std.core.ti6d.name_] = lambda type, attributes: std.core.ti6d(type, attributes)
        loaders[std.core.ti6d.name_] = lambda type, stream: std_n.core._ti6d.load(type, stream)
        factories[std.core.GeoCircle.name_] = lambda type, attributes: std.core.GeoCircle(type, attributes)
        factories[std.core.Map.name_] = lambda type, attributes: std.core.Map(type, attributes)
        loaders[std.core.Map.name_] = lambda type, stream: std_n.core._Map.load(type, stream)
        factories[std.core.ErrorCode.name_] = lambda type, attributes: std.core.ErrorCode(type, attributes)
        factories[std.core.ti4d.name_] = lambda type, attributes: std.core.ti4d(type, attributes)
        loaders[std.core.ti4d.name_] = lambda type, stream: std_n.core._ti4d.load(type, stream)
        factories[std.core.geo.name_] = lambda type, attributes: std.core.geo(type, attributes)
        loaders[std.core.geo.name_] = lambda type, stream: std_n.core._geo.load(type, stream)
        factories[std.core.nodeTimeSingleton.name_] = lambda type, attributes: std.core.nodeTimeSingleton(type, attributes)
        factories[std.core.NodeInfo.name_] = lambda type, attributes: std.core.NodeInfo(type, attributes)
        factories[std.runtime.RuntimeInfo.name_] = lambda type, attributes: std.runtime.RuntimeInfo(type, attributes)
        factories[std.runtime.PeriodicTask.name_] = lambda type, attributes: std.runtime.PeriodicTask(type, attributes)
        factories[std.runtime.SecurityFields.name_] = lambda type, attributes: std.runtime.SecurityFields(type, attributes)
        factories[std.runtime.LicenseType.name_] = lambda type, attributes: std.runtime.LicenseType(type, attributes)
        factories[std.runtime.UserGroup.name_] = lambda type, attributes: std.runtime.UserGroup(type, attributes)
        factories[std.runtime.UserGroupPolicyType.name_] = lambda type, attributes: std.runtime.UserGroupPolicyType(type, attributes)
        factories[std.runtime.UserGroupPolicy.name_] = lambda type, attributes: std.runtime.UserGroupPolicy(type, attributes)
        factories[std.runtime.User.name_] = lambda type, attributes: std.runtime.User(type, attributes)
        factories[std.runtime.UserCredential.name_] = lambda type, attributes: std.runtime.UserCredential(type, attributes)
        factories[std.runtime.StoreStat.name_] = lambda type, attributes: std.runtime.StoreStat(type, attributes)
        factories[std.runtime.UserRole.name_] = lambda type, attributes: std.runtime.UserRole(type, attributes)
        factories[std.runtime.OpenIDConnect.name_] = lambda type, attributes: std.runtime.OpenIDConnect(type, attributes)
        factories[std.runtime.Task.name_] = lambda type, attributes: std.runtime.Task(type, attributes)
        factories[std.runtime.SecurityPolicy.name_] = lambda type, attributes: std.runtime.SecurityPolicy(type, attributes)
        factories[std.runtime.License.name_] = lambda type, attributes: std.runtime.License(type, attributes)
        factories[std.runtime.Runtime.name_] = lambda type, attributes: std.runtime.Runtime(type, attributes)
        factories[std.runtime.TaskStatus.name_] = lambda type, attributes: std.runtime.TaskStatus(type, attributes)
        factories[std.runtime.TaskInfo.name_] = lambda type, attributes: std.runtime.TaskInfo(type, attributes)
        factories[std.runtime.System.name_] = lambda type, attributes: std.runtime.System(type, attributes)
        factories[std.runtime.SecurityEntity.name_] = lambda type, attributes: std.runtime.SecurityEntity(type, attributes)
        factories[std.io.CsvColumnDate.name_] = lambda type, attributes: std.io.CsvColumnDate(type, attributes)
        factories[std.io.CsvColumnInteger.name_] = lambda type, attributes: std.io.CsvColumnInteger(type, attributes)
        factories[std.io.File.name_] = lambda type, attributes: std.io.File(type, attributes)
        factories[std.io.CsvColumnString.name_] = lambda type, attributes: std.io.CsvColumnString(type, attributes)
        factories[std.io.CsvStatistics.name_] = lambda type, attributes: std.io.CsvStatistics(type, attributes)
        factories[std.io.CsvColumnFloat.name_] = lambda type, attributes: std.io.CsvColumnFloat(type, attributes)
        factories[std.io.HttpHeader.name_] = lambda type, attributes: std.io.HttpHeader(type, attributes)
        factories[std.io.CsvFormat.name_] = lambda type, attributes: std.io.CsvFormat(type, attributes)
        factories[std.io.CsvColumnDuration.name_] = lambda type, attributes: std.io.CsvColumnDuration(type, attributes)
        factories[std.io.CsvAnalysis.name_] = lambda type, attributes: std.io.CsvAnalysis(type, attributes)
        factories[std.io.CsvAnalysisConfig.name_] = lambda type, attributes: std.io.CsvAnalysisConfig(type, attributes)
        factories[std.io.SmtpAuth.name_] = lambda type, attributes: std.io.SmtpAuth(type, attributes)
        factories[std.io.Http.name_] = lambda type, attributes: std.io.Http(type, attributes)
        factories[std.io.Smtp.name_] = lambda type, attributes: std.io.Smtp(type, attributes)
        factories[std.io.Mqtt.name_] = lambda type, attributes: std.io.Mqtt(type, attributes)
        factories[std.io.TextEncoder.name_] = lambda type, attributes: std.io.TextEncoder(type, attributes)
        factories[std.io.CsvColumnStatistics.name_] = lambda type, attributes: std.io.CsvColumnStatistics(type, attributes)
        factories[std.io.CsvColumnIgnored.name_] = lambda type, attributes: std.io.CsvColumnIgnored(type, attributes)
        factories[std.io.CsvColumnTime.name_] = lambda type, attributes: std.io.CsvColumnTime(type, attributes)
        factories[std.io.Url.name_] = lambda type, attributes: std.io.Url(type, attributes)
        factories[std.io.Email.name_] = lambda type, attributes: std.io.Email(type, attributes)
        factories[std.io.CsvValidateResult.name_] = lambda type, attributes: std.io.CsvValidateResult(type, attributes)
        factories[std.io.CsvColumnBoolean.name_] = lambda type, attributes: std.io.CsvColumnBoolean(type, attributes)
        factories[std.io.CsvColumn.name_] = lambda type, attributes: std.io.CsvColumn(type, attributes)
        factories[std.io.SmtpMode.name_] = lambda type, attributes: std.io.SmtpMode(type, attributes)
        factories[std.math.MathConstants.name_] = lambda type, attributes: std.math.MathConstants(type, attributes)
        factories[std.util.Random.name_] = lambda type, attributes: std.util.Random(type, attributes)
        factories[std.util.Iban.name_] = lambda type, attributes: std.util.Iban(type, attributes)
        loaders[std.util.Iban.name_] = lambda type, stream: std_n.util._Iban.load(type, stream)
        factories[std.util.Gaussian.name_] = lambda type, attributes: std.util.Gaussian(type, attributes)
        factories[std.util.HistogramFloat.name_] = lambda type, attributes: std.util.HistogramFloat(type, attributes)
        loaders[std.util.HistogramFloat.name_] = lambda type, stream: std_n.util._HistogramFloat.load(type, stream)
        factories[std.util.BoxPlotInt.name_] = lambda type, attributes: std.util.BoxPlotInt(type, attributes)
        factories[std.util.BoxPlotFloat.name_] = lambda type, attributes: std.util.BoxPlotFloat(type, attributes)
        factories[std.util.GaussianProfile.name_] = lambda type, attributes: std.util.GaussianProfile(type, attributes)
        loaders[std.util.GaussianProfile.name_] = lambda type, stream: std_n.util._GaussianProfile.load(type, stream)
        factories[std.util.ProgressTracker.name_] = lambda type, attributes: std.util.ProgressTracker(type, attributes)
        factories[std.util.Buffer.name_] = lambda type, attributes: std.util.Buffer(type, attributes)
        loaders[std.util.Buffer.name_] = lambda type, stream: std_n.util._Buffer.load(type, stream)
        factories[std.util.DenseDim.name_] = lambda type, attributes: std.util.DenseDim(type, attributes)
        factories[std.util.HistogramInt.name_] = lambda type, attributes: std.util.HistogramInt(type, attributes)
        loaders[std.util.HistogramInt.name_] = lambda type, stream: std_n.util._HistogramInt.load(type, stream)
        factories[std.util.SlidingWindow.name_] = lambda type, attributes: std.util.SlidingWindow(type, attributes)
        loaders[std.util.SlidingWindow.name_] = lambda type, stream: std_n.util._SlidingWindow.load(type, stream)
        factories[std.util.Queue.name_] = lambda type, attributes: std.util.Queue(type, attributes)
        loaders[std.util.Queue.name_] = lambda type, stream: std_n.util._Queue.load(type, stream)
        factories[std.util.Plot.name_] = lambda type, attributes: std.util.Plot(type, attributes)
        factories[std.util.TimeWindow.name_] = lambda type, attributes: std.util.TimeWindow(type, attributes)
        loaders[std.util.TimeWindow.name_] = lambda type, stream: std_n.util._TimeWindow.load(type, stream)
        factories[std.util.Assert.name_] = lambda type, attributes: std.util.Assert(type, attributes)
        factories[std.util.Crypto.name_] = lambda type, attributes: std.util.Crypto(type, attributes)

    def init(self, greycat: GreyCat) -> None:
        self.mapped: list[GreyCat.Type] = [
            greycat.types_by_name[std.core.GeoBox.name_],
            greycat.types_by_name[std.core.Error.name_],
            greycat.types_by_name[std.core.tf2d.name_],
            greycat.types_by_name[std.core.Array.name_],
            greycat.types_by_name[std.core.String.name_],
            greycat.types_by_name[std.core.Date.name_],
            greycat.types_by_name[std.core.GeoPoly.name_],
            greycat.types_by_name[std.core.ti5d.name_],
            greycat.types_by_name[std.core.nodeTime.name_],
            greycat.types_by_name[std.core.TimeZone.name_],
            greycat.types_by_name[std.core.Table.name_],
            greycat.types_by_name[std.core.ti10d.name_],
            greycat.types_by_name[std.core.duration.name_],
            greycat.types_by_name[std.core.DurationUnit.name_],
            greycat.types_by_name[std.core.Tensor.name_],
            greycat.types_by_name[std.core.nodeIndex.name_],
            greycat.types_by_name[std.core.TableColumnMapping.name_],
            greycat.types_by_name[std.core.nodeList.name_],
            greycat.types_by_name[std.core.TensorType.name_],
            greycat.types_by_name[std.core.Tuple.name_],
            greycat.types_by_name[std.core.ti2d.name_],
            greycat.types_by_name[std.core.tf4d.name_],
            greycat.types_by_name[std.core.DatePart.name_],
            greycat.types_by_name[std.core.function.name_],
            greycat.types_by_name[std.core.ti3d.name_],
            greycat.types_by_name[std.core.TableColumnMeta.name_],
            greycat.types_by_name[std.core.nodeGeo.name_],
            greycat.types_by_name[std.core.node.name_],
            greycat.types_by_name[std.core.tf3d.name_],
            greycat.types_by_name[std.core.nodeIndexBucket.name_],
            greycat.types_by_name[std.core.time.name_],
            greycat.types_by_name[std.core.SamplingMode.name_],
            greycat.types_by_name[std.core.ti6d.name_],
            greycat.types_by_name[std.core.GeoCircle.name_],
            greycat.types_by_name[std.core.Map.name_],
            greycat.types_by_name[std.core.ErrorCode.name_],
            greycat.types_by_name[std.core.ti4d.name_],
            greycat.types_by_name[std.core.geo.name_],
            greycat.types_by_name[std.core.nodeTimeSingleton.name_],
            greycat.types_by_name[std.core.NodeInfo.name_],
            greycat.types_by_name[std.runtime.RuntimeInfo.name_],
            greycat.types_by_name[std.runtime.PeriodicTask.name_],
            greycat.types_by_name[std.runtime.SecurityFields.name_],
            greycat.types_by_name[std.runtime.LicenseType.name_],
            greycat.types_by_name[std.runtime.UserGroup.name_],
            greycat.types_by_name[std.runtime.UserGroupPolicyType.name_],
            greycat.types_by_name[std.runtime.UserGroupPolicy.name_],
            greycat.types_by_name[std.runtime.User.name_],
            greycat.types_by_name[std.runtime.UserCredential.name_],
            greycat.types_by_name[std.runtime.StoreStat.name_],
            greycat.types_by_name[std.runtime.UserRole.name_],
            greycat.types_by_name[std.runtime.OpenIDConnect.name_],
            greycat.types_by_name[std.runtime.Task.name_],
            greycat.types_by_name[std.runtime.SecurityPolicy.name_],
            greycat.types_by_name[std.runtime.License.name_],
            greycat.types_by_name[std.runtime.Runtime.name_],
            greycat.types_by_name[std.runtime.TaskStatus.name_],
            greycat.types_by_name[std.runtime.TaskInfo.name_],
            greycat.types_by_name[std.runtime.System.name_],
            greycat.types_by_name[std.runtime.SecurityEntity.name_],
            greycat.types_by_name[std.io.CsvColumnDate.name_],
            greycat.types_by_name[std.io.CsvColumnInteger.name_],
            greycat.types_by_name[std.io.File.name_],
            greycat.types_by_name[std.io.CsvColumnString.name_],
            greycat.types_by_name[std.io.CsvStatistics.name_],
            greycat.types_by_name[std.io.CsvColumnFloat.name_],
            greycat.types_by_name[std.io.HttpHeader.name_],
            greycat.types_by_name[std.io.CsvFormat.name_],
            greycat.types_by_name[std.io.CsvColumnDuration.name_],
            greycat.types_by_name[std.io.CsvAnalysis.name_],
            greycat.types_by_name[std.io.CsvAnalysisConfig.name_],
            greycat.types_by_name[std.io.SmtpAuth.name_],
            greycat.types_by_name[std.io.Http.name_],
            greycat.types_by_name[std.io.Smtp.name_],
            greycat.types_by_name[std.io.Mqtt.name_],
            greycat.types_by_name[std.io.TextEncoder.name_],
            greycat.types_by_name[std.io.CsvColumnStatistics.name_],
            greycat.types_by_name[std.io.CsvColumnIgnored.name_],
            greycat.types_by_name[std.io.CsvColumnTime.name_],
            greycat.types_by_name[std.io.Url.name_],
            greycat.types_by_name[std.io.Email.name_],
            greycat.types_by_name[std.io.CsvValidateResult.name_],
            greycat.types_by_name[std.io.CsvColumnBoolean.name_],
            greycat.types_by_name[std.io.CsvColumn.name_],
            greycat.types_by_name[std.io.SmtpMode.name_],
            greycat.types_by_name[std.math.MathConstants.name_],
            greycat.types_by_name[std.util.Random.name_],
            greycat.types_by_name[std.util.Iban.name_],
            greycat.types_by_name[std.util.Gaussian.name_],
            greycat.types_by_name[std.util.HistogramFloat.name_],
            greycat.types_by_name[std.util.BoxPlotInt.name_],
            greycat.types_by_name[std.util.BoxPlotFloat.name_],
            greycat.types_by_name[std.util.GaussianProfile.name_],
            greycat.types_by_name[std.util.ProgressTracker.name_],
            greycat.types_by_name[std.util.Buffer.name_],
            greycat.types_by_name[std.util.DenseDim.name_],
            greycat.types_by_name[std.util.HistogramInt.name_],
            greycat.types_by_name[std.util.SlidingWindow.name_],
            greycat.types_by_name[std.util.Queue.name_],
            greycat.types_by_name[std.util.Plot.name_],
            greycat.types_by_name[std.util.TimeWindow.name_],
            greycat.types_by_name[std.util.Assert.name_],
            greycat.types_by_name[std.util.Crypto.name_],
        ]
        self.mapped[0].resolve_generated_offsets("sw", "ne")
        self.mapped[6].resolve_generated_offsets("points")
        self.mapped[9].resolve_generated_offset_with_values("Africa_Accra", "Africa/Accra", "Africa_Bamako", "Africa/Bamako", "Africa_Banjul", "Africa/Banjul", "Africa_Conakry", "Africa/Conakry", "Africa_Dakar", "Africa/Dakar", "Africa_Freetown", "Africa/Freetown", "Africa_Lome", "Africa/Lome", "Africa_Nouakchott", "Africa/Nouakchott", "Africa_Ouagadougou", "Africa/Ouagadougou", "Africa_Timbuktu", "Africa/Timbuktu", "Atlantic_Reykjavik", "Atlantic/Reykjavik", "Atlantic_St_Helena", "Atlantic/St_Helena", "Iceland", "Iceland", "Egypt", "Egypt", "Africa_Maseru", "Africa/Maseru", "Africa_Mbabane", "Africa/Mbabane", "Africa_Bangui", "Africa/Bangui", "Africa_Brazzaville", "Africa/Brazzaville", "Africa_Douala", "Africa/Douala", "Africa_Kinshasa", "Africa/Kinshasa", "Africa_Libreville", "Africa/Libreville", "Africa_Luanda", "Africa/Luanda", "Africa_Malabo", "Africa/Malabo", "Africa_Niamey", "Africa/Niamey", "Africa_Porto_Novo", "Africa/Porto-Novo", "Africa_Blantyre", "Africa/Blantyre", "Africa_Bujumbura", "Africa/Bujumbura", "Africa_Gaborone", "Africa/Gaborone", "Africa_Harare", "Africa/Harare", "Africa_Kigali", "Africa/Kigali", "Africa_Lubumbashi", "Africa/Lubumbashi", "Africa_Lusaka", "Africa/Lusaka", "Africa_Addis_Ababa", "Africa/Addis_Ababa", "Africa_Asmara", "Africa/Asmara", "Africa_Asmera", "Africa/Asmera", "Africa_Dar_es_Salaam", "Africa/Dar_es_Salaam", "Africa_Djibouti", "Africa/Djibouti", "Africa_Kampala", "Africa/Kampala", "Africa_Mogadishu", "Africa/Mogadishu", "Indian_Antananarivo", "Indian/Antananarivo", "Indian_Comoro", "Indian/Comoro", "Indian_Mayotte", "Indian/Mayotte", "Libya", "Libya", "America_Atka", "America/Atka", "US_Aleutian", "US/Aleutian", "US_Alaska", "US/Alaska", "America_Buenos_Aires", "America/Buenos_Aires", "America_Argentina_ComodRivadavia", "America/Argentina/ComodRivadavia", "America_Catamarca", "America/Catamarca", "America_Cordoba", "America/Cordoba", "America_Rosario", "America/Rosario", "America_Jujuy", "America/Jujuy", "America_Mendoza", "America/Mendoza", "US_Central", "US/Central", "America_Shiprock", "America/Shiprock", "Navajo", "Navajo", "US_Mountain", "US/Mountain", "US_Michigan", "US/Michigan", "America_Yellowknife", "America/Yellowknife", "Canada_Mountain", "Canada/Mountain", "Canada_Atlantic", "Canada/Atlantic", "Cuba", "Cuba", "America_Fort_Wayne", "America/Fort_Wayne", "America_Indianapolis", "America/Indianapolis", "US_East_Indiana", "US/East-Indiana", "America_Knox_IN", "America/Knox_IN", "US_Indiana_Starke", "US/Indiana-Starke", "America_Pangnirtung", "America/Pangnirtung", "Jamaica", "Jamaica", "America_Louisville", "America/Louisville", "US_Pacific", "US/Pacific", "Brazil_West", "Brazil/West", "Mexico_BajaSur", "Mexico/BajaSur", "Mexico_General", "Mexico/General", "US_Eastern", "US/Eastern", "Brazil_DeNoronha", "Brazil/DeNoronha", "America_Godthab", "America/Godthab", "America_Atikokan", "America/Atikokan", "America_Cayman", "America/Cayman", "America_Coral_Harbour", "America/Coral_Harbour", "America_Creston", "America/Creston", "US_Arizona", "US/Arizona", "America_Anguilla", "America/Anguilla", "America_Antigua", "America/Antigua", "America_Aruba", "America/Aruba", "America_Blanc_Sablon", "America/Blanc-Sablon", "America_Curacao", "America/Curacao", "America_Dominica", "America/Dominica", "America_Grenada", "America/Grenada", "America_Guadeloupe", "America/Guadeloupe", "America_Kralendijk", "America/Kralendijk", "America_Lower_Princes", "America/Lower_Princes", "America_Marigot", "America/Marigot", "America_Montserrat", "America/Montserrat", "America_Port_of_Spain", "America/Port_of_Spain", "America_St_Barthelemy", "America/St_Barthelemy", "America_St_Kitts", "America/St_Kitts", "America_St_Lucia", "America/St_Lucia", "America_St_Thomas", "America/St_Thomas", "America_St_Vincent", "America/St_Vincent", "America_Tortola", "America/Tortola", "America_Virgin", "America/Virgin", "Canada_Saskatchewan", "Canada/Saskatchewan", "America_Porto_Acre", "America/Porto_Acre", "Brazil_Acre", "Brazil/Acre", "Chile_Continental", "Chile/Continental", "Brazil_East", "Brazil/East", "Canada_Newfoundland", "Canada/Newfoundland", "America_Ensenada", "America/Ensenada", "America_Santa_Isabel", "America/Santa_Isabel", "Mexico_BajaNorte", "Mexico/BajaNorte", "America_Montreal", "America/Montreal", "America_Nassau", "America/Nassau", "America_Nipigon", "America/Nipigon", "America_Thunder_Bay", "America/Thunder_Bay", "Canada_Eastern", "Canada/Eastern", "Canada_Pacific", "Canada/Pacific", "Canada_Yukon", "Canada/Yukon", "America_Rainy_River", "America/Rainy_River", "Canada_Central", "Canada/Central", "Asia_Ashkhabad", "Asia/Ashkhabad", "Asia_Phnom_Penh", "Asia/Phnom_Penh", "Asia_Vientiane", "Asia/Vientiane", "Indian_Christmas", "Indian/Christmas", "Asia_Dacca", "Asia/Dacca", "Asia_Muscat", "Asia/Muscat", "Indian_Mahe", "Indian/Mahe", "Indian_Reunion", "Indian/Reunion", "Asia_Saigon", "Asia/Saigon", "Hongkong", "Hongkong", "Asia_Tel_Aviv", "Asia/Tel_Aviv", "Israel", "Israel", "Asia_Katmandu", "Asia/Katmandu", "Asia_Calcutta", "Asia/Calcutta", "Asia_Brunei", "Asia/Brunei", "Asia_Macao", "Asia/Macao", "Asia_Ujung_Pandang", "Asia/Ujung_Pandang", "Europe_Nicosia", "Europe/Nicosia", "Asia_Bahrain", "Asia/Bahrain", "Antarctica_Syowa", "Antarctica/Syowa", "Asia_Aden", "Asia/Aden", "Asia_Kuwait", "Asia/Kuwait", "ROK", "ROK", "Asia_Chongqing", "Asia/Chongqing", "Asia_Chungking", "Asia/Chungking", "Asia_Harbin", "Asia/Harbin", "PRC", "PRC", "Asia_Kuala_Lumpur", "Asia/Kuala_Lumpur", "Singapore", "Singapore", "ROC", "ROC", "Iran", "Iran", "Asia_Thimbu", "Asia/Thimbu", "Japan", "Japan", "Asia_Ulan_Bator", "Asia/Ulan_Bator", "Antarctica_Vostok", "Antarctica/Vostok", "Asia_Kashgar", "Asia/Kashgar", "Asia_Rangoon", "Asia/Rangoon", "Indian_Cocos", "Indian/Cocos", "Atlantic_Faeroe", "Atlantic/Faeroe", "Australia_South", "Australia/South", "Australia_Queensland", "Australia/Queensland", "Australia_Yancowinna", "Australia/Yancowinna", "Australia_North", "Australia/North", "Australia_Currie", "Australia/Currie", "Australia_Tasmania", "Australia/Tasmania", "Australia_LHI", "Australia/LHI", "Australia_Victoria", "Australia/Victoria", "Australia_West", "Australia/West", "Australia_ACT", "Australia/ACT", "Australia_Canberra", "Australia/Canberra", "Australia_NSW", "Australia/NSW", "GMT", "GMT", "GMTx0", "GMT+0", "GMT_0", "GMT-0", "GMT0", "GMT0", "Greenwich", "Greenwich", "UCT", "UCT", "UTC", "UTC", "Universal", "Universal", "Zulu", "Zulu", "Europe_Ljubljana", "Europe/Ljubljana", "Europe_Podgorica", "Europe/Podgorica", "Europe_Sarajevo", "Europe/Sarajevo", "Europe_Skopje", "Europe/Skopje", "Europe_Zagreb", "Europe/Zagreb", "Arctic_Longyearbyen", "Arctic/Longyearbyen", "Atlantic_Jan_Mayen", "Atlantic/Jan_Mayen", "Europe_Copenhagen", "Europe/Copenhagen", "Europe_Oslo", "Europe/Oslo", "Europe_Stockholm", "Europe/Stockholm", "Europe_Amsterdam", "Europe/Amsterdam", "Europe_Luxembourg", "Europe/Luxembourg", "Europe_Tiraspol", "Europe/Tiraspol", "Eire", "Eire", "Europe_Mariehamn", "Europe/Mariehamn", "Asia_Istanbul", "Asia/Istanbul", "Turkey", "Turkey", "Europe_Kiev", "Europe/Kiev", "Europe_Uzhgorod", "Europe/Uzhgorod", "Europe_Zaporozhye", "Europe/Zaporozhye", "Portugal", "Portugal", "Europe_Belfast", "Europe/Belfast", "Europe_Guernsey", "Europe/Guernsey", "Europe_Isle_of_Man", "Europe/Isle_of_Man", "Europe_Jersey", "Europe/Jersey", "GB", "GB", "GB_Eire", "GB-Eire", "W_SU", "W-SU", "Europe_Monaco", "Europe/Monaco", "Europe_Bratislava", "Europe/Bratislava", "Europe_San_Marino", "Europe/San_Marino", "Europe_Vatican", "Europe/Vatican", "Poland", "Poland", "Europe_Busingen", "Europe/Busingen", "Europe_Vaduz", "Europe/Vaduz", "Indian_Kerguelen", "Indian/Kerguelen", "Antarctica_McMurdo", "Antarctica/McMurdo", "Antarctica_South_Pole", "Antarctica/South_Pole", "NZ", "NZ", "NZ_CHAT", "NZ-CHAT", "Chile_EasterIsland", "Chile/EasterIsland", "Pacific_Pohnpei", "Pacific/Pohnpei", "Pacific_Ponape", "Pacific/Ponape", "Pacific_Saipan", "Pacific/Saipan", "Pacific_Johnston", "Pacific/Johnston", "US_Hawaii", "US/Hawaii", "Pacific_Enderbury", "Pacific/Enderbury", "Kwajalein", "Kwajalein", "Pacific_Midway", "Pacific/Midway", "Pacific_Samoa", "Pacific/Samoa", "US_Samoa", "US/Samoa", "Antarctica_DumontDUrville", "Antarctica/DumontDUrville", "Pacific_Chuuk", "Pacific/Chuuk", "Pacific_Truk", "Pacific/Truk", "Pacific_Yap", "Pacific/Yap", "Pacific_Funafuti", "Pacific/Funafuti", "Pacific_Majuro", "Pacific/Majuro", "Pacific_Wake", "Pacific/Wake", "Pacific_Wallis", "Pacific/Wallis", "Africa_Abidjan", "Africa/Abidjan", "Africa_Algiers", "Africa/Algiers", "Africa_Bissau", "Africa/Bissau", "Africa_Cairo", "Africa/Cairo", "Africa_Casablanca", "Africa/Casablanca", "Africa_Ceuta", "Africa/Ceuta", "Africa_El_Aaiun", "Africa/El_Aaiun", "Africa_Johannesburg", "Africa/Johannesburg", "Africa_Juba", "Africa/Juba", "Africa_Khartoum", "Africa/Khartoum", "Africa_Lagos", "Africa/Lagos", "Africa_Maputo", "Africa/Maputo", "Africa_Monrovia", "Africa/Monrovia", "Africa_Nairobi", "Africa/Nairobi", "Africa_Ndjamena", "Africa/Ndjamena", "Africa_Sao_Tome", "Africa/Sao_Tome", "Africa_Tripoli", "Africa/Tripoli", "Africa_Tunis", "Africa/Tunis", "Africa_Windhoek", "Africa/Windhoek", "America_Adak", "America/Adak", "America_Anchorage", "America/Anchorage", "America_Araguaina", "America/Araguaina", "America_Argentina_Buenos_Aires", "America/Argentina/Buenos_Aires", "America_Argentina_Catamarca", "America/Argentina/Catamarca", "America_Argentina_Cordoba", "America/Argentina/Cordoba", "America_Argentina_Jujuy", "America/Argentina/Jujuy", "America_Argentina_La_Rioja", "America/Argentina/La_Rioja", "America_Argentina_Mendoza", "America/Argentina/Mendoza", "America_Argentina_Rio_Gallegos", "America/Argentina/Rio_Gallegos", "America_Argentina_Salta", "America/Argentina/Salta", "America_Argentina_San_Juan", "America/Argentina/San_Juan", "America_Argentina_San_Luis", "America/Argentina/San_Luis", "America_Argentina_Tucuman", "America/Argentina/Tucuman", "America_Argentina_Ushuaia", "America/Argentina/Ushuaia", "America_Asuncion", "America/Asuncion", "America_Bahia", "America/Bahia", "America_Bahia_Banderas", "America/Bahia_Banderas", "America_Barbados", "America/Barbados", "America_Belem", "America/Belem", "America_Belize", "America/Belize", "America_Boa_Vista", "America/Boa_Vista", "America_Bogota", "America/Bogota", "America_Boise", "America/Boise", "America_Cambridge_Bay", "America/Cambridge_Bay", "America_Campo_Grande", "America/Campo_Grande", "America_Cancun", "America/Cancun", "America_Caracas", "America/Caracas", "America_Cayenne", "America/Cayenne", "America_Chicago", "America/Chicago", "America_Chihuahua", "America/Chihuahua", "America_Ciudad_Juarez", "America/Ciudad_Juarez", "America_Costa_Rica", "America/Costa_Rica", "America_Cuiaba", "America/Cuiaba", "America_Danmarkshavn", "America/Danmarkshavn", "America_Dawson", "America/Dawson", "America_Dawson_Creek", "America/Dawson_Creek", "America_Denver", "America/Denver", "America_Detroit", "America/Detroit", "America_Edmonton", "America/Edmonton", "America_Eirunepe", "America/Eirunepe", "America_El_Salvador", "America/El_Salvador", "America_Fort_Nelson", "America/Fort_Nelson", "America_Fortaleza", "America/Fortaleza", "America_Glace_Bay", "America/Glace_Bay", "America_Goose_Bay", "America/Goose_Bay", "America_Grand_Turk", "America/Grand_Turk", "America_Guatemala", "America/Guatemala", "America_Guayaquil", "America/Guayaquil", "America_Guyana", "America/Guyana", "America_Halifax", "America/Halifax", "America_Havana", "America/Havana", "America_Hermosillo", "America/Hermosillo", "America_Indiana_Indianapolis", "America/Indiana/Indianapolis", "America_Indiana_Knox", "America/Indiana/Knox", "America_Indiana_Marengo", "America/Indiana/Marengo", "America_Indiana_Petersburg", "America/Indiana/Petersburg", "America_Indiana_Tell_City", "America/Indiana/Tell_City", "America_Indiana_Vevay", "America/Indiana/Vevay", "America_Indiana_Vincennes", "America/Indiana/Vincennes", "America_Indiana_Winamac", "America/Indiana/Winamac", "America_Inuvik", "America/Inuvik", "America_Iqaluit", "America/Iqaluit", "America_Jamaica", "America/Jamaica", "America_Juneau", "America/Juneau", "America_Kentucky_Louisville", "America/Kentucky/Louisville", "America_Kentucky_Monticello", "America/Kentucky/Monticello", "America_La_Paz", "America/La_Paz", "America_Lima", "America/Lima", "America_Los_Angeles", "America/Los_Angeles", "America_Maceio", "America/Maceio", "America_Managua", "America/Managua", "America_Manaus", "America/Manaus", "America_Martinique", "America/Martinique", "America_Matamoros", "America/Matamoros", "America_Mazatlan", "America/Mazatlan", "America_Menominee", "America/Menominee", "America_Merida", "America/Merida", "America_Metlakatla", "America/Metlakatla", "America_Mexico_City", "America/Mexico_City", "America_Miquelon", "America/Miquelon", "America_Moncton", "America/Moncton", "America_Monterrey", "America/Monterrey", "America_Montevideo", "America/Montevideo", "America_New_York", "America/New_York", "America_Nome", "America/Nome", "America_Noronha", "America/Noronha", "America_North_Dakota_Beulah", "America/North_Dakota/Beulah", "America_North_Dakota_Center", "America/North_Dakota/Center", "America_North_Dakota_New_Salem", "America/North_Dakota/New_Salem", "America_Nuuk", "America/Nuuk", "America_Ojinaga", "America/Ojinaga", "America_Panama", "America/Panama", "America_Paramaribo", "America/Paramaribo", "America_Phoenix", "America/Phoenix", "America_Port_au_Prince", "America/Port-au-Prince", "America_Porto_Velho", "America/Porto_Velho", "America_Puerto_Rico", "America/Puerto_Rico", "America_Punta_Arenas", "America/Punta_Arenas", "America_Rankin_Inlet", "America/Rankin_Inlet", "America_Recife", "America/Recife", "America_Regina", "America/Regina", "America_Resolute", "America/Resolute", "America_Rio_Branco", "America/Rio_Branco", "America_Santarem", "America/Santarem", "America_Santiago", "America/Santiago", "America_Santo_Domingo", "America/Santo_Domingo", "America_Sao_Paulo", "America/Sao_Paulo", "America_Scoresbysund", "America/Scoresbysund", "America_Sitka", "America/Sitka", "America_St_Johns", "America/St_Johns", "America_Swift_Current", "America/Swift_Current", "America_Tegucigalpa", "America/Tegucigalpa", "America_Thule", "America/Thule", "America_Tijuana", "America/Tijuana", "America_Toronto", "America/Toronto", "America_Vancouver", "America/Vancouver", "America_Whitehorse", "America/Whitehorse", "America_Winnipeg", "America/Winnipeg", "America_Yakutat", "America/Yakutat", "Antarctica_Casey", "Antarctica/Casey", "Antarctica_Davis", "Antarctica/Davis", "Antarctica_Macquarie", "Antarctica/Macquarie", "Antarctica_Mawson", "Antarctica/Mawson", "Antarctica_Palmer", "Antarctica/Palmer", "Antarctica_Rothera", "Antarctica/Rothera", "Antarctica_Troll", "Antarctica/Troll", "Asia_Almaty", "Asia/Almaty", "Asia_Amman", "Asia/Amman", "Asia_Anadyr", "Asia/Anadyr", "Asia_Aqtau", "Asia/Aqtau", "Asia_Aqtobe", "Asia/Aqtobe", "Asia_Ashgabat", "Asia/Ashgabat", "Asia_Atyrau", "Asia/Atyrau", "Asia_Baghdad", "Asia/Baghdad", "Asia_Baku", "Asia/Baku", "Asia_Bangkok", "Asia/Bangkok", "Asia_Barnaul", "Asia/Barnaul", "Asia_Beirut", "Asia/Beirut", "Asia_Bishkek", "Asia/Bishkek", "Asia_Chita", "Asia/Chita", "Asia_Choibalsan", "Asia/Choibalsan", "Asia_Colombo", "Asia/Colombo", "Asia_Damascus", "Asia/Damascus", "Asia_Dhaka", "Asia/Dhaka", "Asia_Dili", "Asia/Dili", "Asia_Dubai", "Asia/Dubai", "Asia_Dushanbe", "Asia/Dushanbe", "Asia_Famagusta", "Asia/Famagusta", "Asia_Gaza", "Asia/Gaza", "Asia_Hebron", "Asia/Hebron", "Asia_Ho_Chi_Minh", "Asia/Ho_Chi_Minh", "Asia_Hong_Kong", "Asia/Hong_Kong", "Asia_Hovd", "Asia/Hovd", "Asia_Irkutsk", "Asia/Irkutsk", "Asia_Jakarta", "Asia/Jakarta", "Asia_Jayapura", "Asia/Jayapura", "Asia_Jerusalem", "Asia/Jerusalem", "Asia_Kabul", "Asia/Kabul", "Asia_Kamchatka", "Asia/Kamchatka", "Asia_Karachi", "Asia/Karachi", "Asia_Kathmandu", "Asia/Kathmandu", "Asia_Khandyga", "Asia/Khandyga", "Asia_Kolkata", "Asia/Kolkata", "Asia_Krasnoyarsk", "Asia/Krasnoyarsk", "Asia_Kuching", "Asia/Kuching", "Asia_Macau", "Asia/Macau", "Asia_Magadan", "Asia/Magadan", "Asia_Makassar", "Asia/Makassar", "Asia_Manila", "Asia/Manila", "Asia_Nicosia", "Asia/Nicosia", "Asia_Novokuznetsk", "Asia/Novokuznetsk", "Asia_Novosibirsk", "Asia/Novosibirsk", "Asia_Omsk", "Asia/Omsk", "Asia_Oral", "Asia/Oral", "Asia_Pontianak", "Asia/Pontianak", "Asia_Pyongyang", "Asia/Pyongyang", "Asia_Qatar", "Asia/Qatar", "Asia_Qostanay", "Asia/Qostanay", "Asia_Qyzylorda", "Asia/Qyzylorda", "Asia_Riyadh", "Asia/Riyadh", "Asia_Sakhalin", "Asia/Sakhalin", "Asia_Samarkand", "Asia/Samarkand", "Asia_Seoul", "Asia/Seoul", "Asia_Shanghai", "Asia/Shanghai", "Asia_Singapore", "Asia/Singapore", "Asia_Srednekolymsk", "Asia/Srednekolymsk", "Asia_Taipei", "Asia/Taipei", "Asia_Tashkent", "Asia/Tashkent", "Asia_Tbilisi", "Asia/Tbilisi", "Asia_Tehran", "Asia/Tehran", "Asia_Thimphu", "Asia/Thimphu", "Asia_Tokyo", "Asia/Tokyo", "Asia_Tomsk", "Asia/Tomsk", "Asia_Ulaanbaatar", "Asia/Ulaanbaatar", "Asia_Urumqi", "Asia/Urumqi", "Asia_Ust_Nera", "Asia/Ust-Nera", "Asia_Vladivostok", "Asia/Vladivostok", "Asia_Yakutsk", "Asia/Yakutsk", "Asia_Yangon", "Asia/Yangon", "Asia_Yekaterinburg", "Asia/Yekaterinburg", "Asia_Yerevan", "Asia/Yerevan", "Atlantic_Azores", "Atlantic/Azores", "Atlantic_Bermuda", "Atlantic/Bermuda", "Atlantic_Canary", "Atlantic/Canary", "Atlantic_Cape_Verde", "Atlantic/Cape_Verde", "Atlantic_Faroe", "Atlantic/Faroe", "Atlantic_Madeira", "Atlantic/Madeira", "Atlantic_South_Georgia", "Atlantic/South_Georgia", "Atlantic_Stanley", "Atlantic/Stanley", "Australia_Adelaide", "Australia/Adelaide", "Australia_Brisbane", "Australia/Brisbane", "Australia_Broken_Hill", "Australia/Broken_Hill", "Australia_Darwin", "Australia/Darwin", "Australia_Eucla", "Australia/Eucla", "Australia_Hobart", "Australia/Hobart", "Australia_Lindeman", "Australia/Lindeman", "Australia_Lord_Howe", "Australia/Lord_Howe", "Australia_Melbourne", "Australia/Melbourne", "Australia_Perth", "Australia/Perth", "Australia_Sydney", "Australia/Sydney", "CET", "CET", "CST6CDT", "CST6CDT", "EET", "EET", "EST", "EST", "EST5EDT", "EST5EDT", "Europe_Andorra", "Europe/Andorra", "Europe_Astrakhan", "Europe/Astrakhan", "Europe_Athens", "Europe/Athens", "Europe_Belgrade", "Europe/Belgrade", "Europe_Berlin", "Europe/Berlin", "Europe_Brussels", "Europe/Brussels", "Europe_Bucharest", "Europe/Bucharest", "Europe_Budapest", "Europe/Budapest", "Europe_Chisinau", "Europe/Chisinau", "Europe_Dublin", "Europe/Dublin", "Europe_Gibraltar", "Europe/Gibraltar", "Europe_Helsinki", "Europe/Helsinki", "Europe_Istanbul", "Europe/Istanbul", "Europe_Kaliningrad", "Europe/Kaliningrad", "Europe_Kirov", "Europe/Kirov", "Europe_Kyiv", "Europe/Kyiv", "Europe_Lisbon", "Europe/Lisbon", "Europe_London", "Europe/London", "Europe_Madrid", "Europe/Madrid", "Europe_Malta", "Europe/Malta", "Europe_Minsk", "Europe/Minsk", "Europe_Moscow", "Europe/Moscow", "Europe_Paris", "Europe/Paris", "Europe_Prague", "Europe/Prague", "Europe_Riga", "Europe/Riga", "Europe_Rome", "Europe/Rome", "Europe_Samara", "Europe/Samara", "Europe_Saratov", "Europe/Saratov", "Europe_Simferopol", "Europe/Simferopol", "Europe_Sofia", "Europe/Sofia", "Europe_Tallinn", "Europe/Tallinn", "Europe_Tirane", "Europe/Tirane", "Europe_Ulyanovsk", "Europe/Ulyanovsk", "Europe_Vienna", "Europe/Vienna", "Europe_Vilnius", "Europe/Vilnius", "Europe_Volgograd", "Europe/Volgograd", "Europe_Warsaw", "Europe/Warsaw", "Europe_Zurich", "Europe/Zurich", "Factory", "Factory", "HST", "HST", "Indian_Chagos", "Indian/Chagos", "Indian_Maldives", "Indian/Maldives", "Indian_Mauritius", "Indian/Mauritius", "MET", "MET", "MST", "MST", "MST7MDT", "MST7MDT", "PST8PDT", "PST8PDT", "Pacific_Apia", "Pacific/Apia", "Pacific_Auckland", "Pacific/Auckland", "Pacific_Bougainville", "Pacific/Bougainville", "Pacific_Chatham", "Pacific/Chatham", "Pacific_Easter", "Pacific/Easter", "Pacific_Efate", "Pacific/Efate", "Pacific_Fakaofo", "Pacific/Fakaofo", "Pacific_Fiji", "Pacific/Fiji", "Pacific_Galapagos", "Pacific/Galapagos", "Pacific_Gambier", "Pacific/Gambier", "Pacific_Guadalcanal", "Pacific/Guadalcanal", "Pacific_Guam", "Pacific/Guam", "Pacific_Honolulu", "Pacific/Honolulu", "Pacific_Kanton", "Pacific/Kanton", "Pacific_Kiritimati", "Pacific/Kiritimati", "Pacific_Kosrae", "Pacific/Kosrae", "Pacific_Kwajalein", "Pacific/Kwajalein", "Pacific_Marquesas", "Pacific/Marquesas", "Pacific_Nauru", "Pacific/Nauru", "Pacific_Niue", "Pacific/Niue", "Pacific_Norfolk", "Pacific/Norfolk", "Pacific_Noumea", "Pacific/Noumea", "Pacific_Pago_Pago", "Pacific/Pago_Pago", "Pacific_Palau", "Pacific/Palau", "Pacific_Pitcairn", "Pacific/Pitcairn", "Pacific_Port_Moresby", "Pacific/Port_Moresby", "Pacific_Rarotonga", "Pacific/Rarotonga", "Pacific_Tahiti", "Pacific/Tahiti", "Pacific_Tarawa", "Pacific/Tarawa", "Pacific_Tongatapu", "Pacific/Tongatapu", "WET", "WET")
        self.mapped[13].resolve_generated_offset_with_values("microseconds", 1, "milliseconds", 1000, "seconds", 1000000, "minutes", 60000000, "hours", 3600000000, "days", 86400000000, "weeks", 604800000000, "months", 2628000000000, "years", 31536000000000)
        self.mapped[16].resolve_generated_offsets("column", "extractors")
        self.mapped[18].resolve_generated_offset_with_values("i32", 4, "i64", 8, "f32", 4, "f64", 8, "c64", 8, "c128", 16)
        self.mapped[19].resolve_generated_offsets("x", "y")
        self.mapped[22].resolve_generated_offset_with_values("years", 0, "months", 1, "days", 2, "hours", 3, "minutes", 4, "seconds", 5, "microseconds", 6)
        self.mapped[25].resolve_generated_offsets("type", "size", "index", "header", "min", "max", "avg", "std")
        self.mapped[30].static_values = [greycat.create_time(-9223372036854775808), greycat.create_time(9223372036854775807)]
        self.mapped[31].resolve_generated_offset_with_values("fixed", 0, "fixed_reg", 1, "adaptative", 2, "dense", 3)
        self.mapped[33].resolve_generated_offsets("center", "radius")
        self.mapped[35].resolve_generated_offset_with_values("none", 0, "too_deep_workspace", 1, "too_deep_iterator", 2, "wrong_operand", 3, "wrong_params", 4, "wrong_param_type", 5, "wrong_numeric", 6, "wrong_state", 7, "wrong_null", 8, "unresolved_ref", 9, "assign_error", 10, "interrupted", 11, "throw", 12, "wrong_type", 13, "wrong_dimension", 14, "unsupported_operation", 15, "unsupported_type", 16, "dimensions_mismatch", 17, "timeout", 18, "forbidden", 19, "runtime_error", 20)
        self.mapped[37].static_values = [greycat.create_geo(struct.unpack("=d", struct.pack("=q", -4587686678796158022))[0], struct.unpack("=d", struct.pack("=q", -4582834833316020224))[0]), greycat.create_geo(struct.unpack("=d", struct.pack("=q", 4635685358058617786))[0], struct.unpack("=d", struct.pack("=q", 4640537203538755584))[0])]
        self.mapped[38].resolve_generated_offsets("t", "v")
        self.mapped[39].resolve_generated_offsets("size", "from", "to")
        self.mapped[40].resolve_generated_offsets("version", "program_version", "arch", "timezone", "license", "io_threads", "bg_threads", "fg_threads", "mem_total", "mem_worker", "nb_ctx", "store_stats")
        self.mapped[41].resolve_generated_offsets("function", "user_id", "arguments", "start", "every")
        self.mapped[42].resolve_generated_offsets("email", "name", "first_name", "last_name", "roles", "groups")
        self.mapped[43].resolve_generated_offset_with_values("community", 0, "enterprise", 1, "testing", 2)
        self.mapped[44].resolve_generated_offsets("id", "name", "activated")
        self.mapped[45].resolve_generated_offset_with_values("read", 0, "write", 1, "execute", 2)
        self.mapped[46].resolve_generated_offsets("group_id", "type")
        self.mapped[47].resolve_generated_offsets("id", "name", "activated", "full_name", "email", "role", "permissions_flags", "groups", "groups_flags", "external")
        self.mapped[48].resolve_generated_offsets("offset", "pass")
        self.mapped[49].resolve_generated_offsets("capacity_bytes", "allocated_bytes", "allocated_ratio", "remained_bytes", "remained_ratio", "used_bytes", "used_ratio", "available_bytes", "available_ratio")
        self.mapped[50].resolve_generated_offsets("name", "permissions")
        self.mapped[51].resolve_generated_offsets("url", "clientId")
        self.mapped[52].resolve_generated_offsets("user_id", "task_id", "mod", "type", "fun", "creation", "status")
        self.mapped[53].resolve_generated_offsets("entities", "credentials", "roles", "fields", "keys", "keys_last_refresh")
        self.mapped[54].resolve_generated_offsets("name", "start", "end", "company", "max_memory", "extra_1", "extra_2", "type")
        self.mapped[56].resolve_generated_offset_with_values("empty", 0, "waiting", 1, "running", 2, "cancelled", 3, "error", 4, "ended", 5)
        self.mapped[57].resolve_generated_offsets("user_id", "task_id", "mod", "type", "fun", "creation", "status", "start", "progress", "remaining", "duration", "sub_waiting", "sub_tasks_all")
        self.mapped[59].resolve_generated_offsets("id", "name", "activated")
        self.mapped[60].resolve_generated_offsets("name", "mandatory", "offset", "format", "tz", "as_time")
        self.mapped[61].resolve_generated_offsets("name", "mandatory", "offset")
        self.mapped[62].resolve_generated_offsets("path", "size", "last_modification")
        self.mapped[63].resolve_generated_offsets("name", "mandatory", "offset", "trim", "try_number", "try_json", "values", "encoder")
        self.mapped[64].resolve_generated_offsets("header_lines", "separator", "string_delimiter", "decimal_separator", "thousands_separator", "columns", "line_count", "fail_count", "file_count")
        self.mapped[65].resolve_generated_offsets("name", "mandatory", "offset")
        self.mapped[66].resolve_generated_offsets("name", "value")
        self.mapped[67].resolve_generated_offsets("header_lines", "separator", "string_delimiter", "decimal_separator", "thousands_separator", "columns_size", "columns")
        self.mapped[68].resolve_generated_offsets("name", "mandatory", "offset", "unit")
        self.mapped[69].resolve_generated_offsets("config", "statistics")
        self.mapped[70].resolve_generated_offsets("header_lines", "separator", "string_delimiter", "decimal_separator", "thousands_separator", "row_limit", "enumerable_limit", "date_check_limit", "date_formats")
        self.mapped[70].static_values = [100, 100]
        self.mapped[71].resolve_generated_offset_with_values("none", 0, "plain", 1, "login", 2)
        self.mapped[73].resolve_generated_offsets("host", "port", "mode", "authenticate", "user", "pass")
        self.mapped[75].resolve_generated_offset_with_values("plain", None, "base64", None, "base64url", None, "hexadecimal", None)
        self.mapped[76].resolve_generated_offsets("name", "example", "null_count", "bool_count", "int_count", "float_count", "string_count", "date_count", "date_format_count", "enumerable_count", "profile")
        self.mapped[77].resolve_generated_offsets("name", "mandatory", "offset")
        self.mapped[78].resolve_generated_offsets("name", "mandatory", "offset", "unit")
        self.mapped[79].resolve_generated_offsets("protocol", "host", "port", "path", "params", "hash")
        self.mapped[80].resolve_generated_offsets("from", "subject", "body", "body_is_html", "to", "cc", "bcc")
        self.mapped[81].resolve_generated_offsets("line_count", "fail_count", "invalid_count")
        self.mapped[82].resolve_generated_offsets("name", "mandatory", "offset")
        self.mapped[83].resolve_generated_offsets("name", "mandatory", "offset")
        self.mapped[84].resolve_generated_offset_with_values("plain", 0, "ssl_tls", 1, "starttls", 2)
        self.mapped[85].static_values = [struct.unpack("=d", struct.pack("=q", 4613303445314885481))[0], struct.unpack("=d", struct.pack("=q", 4609176140021203710))[0], struct.unpack("=d", struct.pack("=q", 4601495173785380110))[0], struct.unpack("=d", struct.pack("=q", 4604418534313441775))[0], struct.unpack("=d", struct.pack("=q", 4612367379483415830))[0], struct.unpack("=d", struct.pack("=q", 4614256656552045848))[0], struct.unpack("=d", struct.pack("=q", 4609753056924675352))[0], struct.unpack("=d", struct.pack("=q", 4605249457297304856))[0], struct.unpack("=d", struct.pack("=q", 4599405781057128579))[0], struct.unpack("=d", struct.pack("=q", 4603909380684499075))[0], struct.unpack("=d", struct.pack("=q", 4607760587169110893))[0], struct.unpack("=d", struct.pack("=q", 4609047870845172685))[0], struct.unpack("=d", struct.pack("=q", 4604544271217802189))[0]]
        self.mapped[86].resolve_generated_offsets("seed", "v")
        self.mapped[88].resolve_generated_offsets("sum", "sum_sq", "count", "min", "max")
        self.mapped[89].static_values = [0, 1, 2, 3]
        self.mapped[90].resolve_generated_offsets("min", "max", "whiskerLow", "whiskerHigh", "percentile1", "percentile5", "percentile25", "percentile50", "percentile75", "percentile95", "percentile99", "countOutliersLow", "countOutliersHigh", "percentageOutliersLow", "percentageOutliersHigh", "sum", "avg", "std", "size")
        self.mapped[91].resolve_generated_offsets("min", "max", "whiskerLow", "whiskerHigh", "percentile1", "percentile5", "percentile25", "percentile50", "percentile75", "percentile95", "percentile99", "countOutliersLow", "countOutliersHigh", "percentageOutliersLow", "percentageOutliersHigh", "sum", "avg", "std", "size")
        self.mapped[92].static_values = [0, 1, 2, 3, 4, 5, 6]
        self.mapped[93].resolve_generated_offsets("start", "total", "counter", "duration", "progress", "speed", "remaining")
        self.mapped[95].resolve_generated_offsets("min", "max", "step")
        self.mapped[96].static_values = [0, 1, 2, 3]
