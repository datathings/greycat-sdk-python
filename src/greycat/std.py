# AUTO-GENERATED FILE PLEASE DO NOT MODIFY MANUALLY
from __future__ import annotations
from ctypes import *
from typing import *
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
        __U = TypeVar("__U")
        __K = TypeVar("__K")
        __V = TypeVar("__V")

        @final
        class t4(std_n.core._t4):
            name_: Final[str] = "core::t4"

            def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
                super().__init__(type)

            @staticmethod
            def create(greycat: GreyCat) -> std_n.core._t4:
                return std.core.t4(greycat.libs_by_name[std.name_].mapped[0], [])

        @final
        class Date(GreyCat.Object):
            name_: Final[str] = "core::Date"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def year(self) -> int:
                return self._get(self.type_.generated_offsets[0])

            def set_year(self, v: int) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def month(self) -> int:
                return self._get(self.type_.generated_offsets[1])

            def set_month(self, v: int) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def day(self) -> int:
                return self._get(self.type_.generated_offsets[2])

            def set_day(self, v: int) -> None:
                self._set(self.type_.generated_offsets[2], v)

            def hour(self) -> int:
                return self._get(self.type_.generated_offsets[3])

            def set_hour(self, v: int) -> None:
                self._set(self.type_.generated_offsets[3], v)

            def minute(self) -> int:
                return self._get(self.type_.generated_offsets[4])

            def set_minute(self, v: int) -> None:
                self._set(self.type_.generated_offsets[4], v)

            def second(self) -> int:
                return self._get(self.type_.generated_offsets[5])

            def set_second(self, v: int) -> None:
                self._set(self.type_.generated_offsets[5], v)

            def microsecond(self) -> int:
                return self._get(self.type_.generated_offsets[6])

            def set_microsecond(self, v: int) -> None:
                self._set(self.type_.generated_offsets[6], v)

            @staticmethod
            def fromTime(time: std.core.time, tz: std.core.TimeZone, __greycat: Optional[GreyCat] = None) -> std.core.Date:
                if __greycat is None:
                    __greycat  = GreyCat.DEFAULT
                return __greycat.call("core::Date::fromTime", [time, tz, ])

            @staticmethod
            def create(greycat: GreyCat, year: int, month: int, day: int, hour: int, minute: int, second: int, microsecond: int) -> std.core.Date:
                return std.core.Date(greycat.libs_by_name[std.name_].mapped[1], [year, month, day, hour, minute, second, microsecond])

        @final
        class nodeTimeCursor(Generic[__T], GreyCat.Object):
            name_: Final[str] = "core::nodeTimeCursor"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def n(self) -> std.core.nodeTime:
                return self._get(self.type_.generated_offsets[0])

            def set_n(self, v: std.core.nodeTime) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def req_time(self) -> std.core.time:
                return self._get(self.type_.generated_offsets[1])

            def set_req_time(self, v: std.core.time) -> None:
                self._set(self.type_.generated_offsets[1], v)

            @staticmethod
            def create(greycat: GreyCat, n: std.core.nodeTime, req_time: std.core.time) -> std.core.nodeTimeCursor[TypeVar("T")]:
                return std.core.nodeTimeCursor(greycat.libs_by_name[std.name_].mapped[2], [n, req_time])

        @final
        class TimeZone(GreyCat.Enum):
            name_: Final[str] = "core::TimeZone"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def __class_getitem__(cls, key) -> std.core.TimeZone:
                if isinstance(key, tuple):
                    key, greycat = key
                else:
                    greycat = GreyCat._DEFAULT
                if "Africa/Abidjan" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[0]]
                if "Africa/Accra" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[1]]
                if "Africa/Addis_Ababa" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[2]]
                if "Africa/Algiers" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[3]]
                if "Africa/Asmara" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[4]]
                if "Africa/Asmera" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[5]]
                if "Africa/Bamako" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[6]]
                if "Africa/Bangui" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[7]]
                if "Africa/Banjul" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[8]]
                if "Africa/Bissau" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[9]]
                if "Africa/Blantyre" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[10]]
                if "Africa/Brazzaville" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[11]]
                if "Africa/Bujumbura" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[12]]
                if "Africa/Cairo" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[13]]
                if "Africa/Casablanca" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[14]]
                if "Africa/Ceuta" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[15]]
                if "Africa/Conakry" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[16]]
                if "Africa/Dakar" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[17]]
                if "Africa/Dar_es_Salaam" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[18]]
                if "Africa/Djibouti" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[19]]
                if "Africa/Douala" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[20]]
                if "Africa/El_Aaiun" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[21]]
                if "Africa/Freetown" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[22]]
                if "Africa/Gaborone" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[23]]
                if "Africa/Harare" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[24]]
                if "Africa/Johannesburg" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[25]]
                if "Africa/Juba" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[26]]
                if "Africa/Kampala" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[27]]
                if "Africa/Khartoum" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[28]]
                if "Africa/Kigali" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[29]]
                if "Africa/Kinshasa" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[30]]
                if "Africa/Lagos" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[31]]
                if "Africa/Libreville" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[32]]
                if "Africa/Lome" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[33]]
                if "Africa/Luanda" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[34]]
                if "Africa/Lubumbashi" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[35]]
                if "Africa/Lusaka" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[36]]
                if "Africa/Malabo" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[37]]
                if "Africa/Maputo" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[38]]
                if "Africa/Maseru" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[39]]
                if "Africa/Mbabane" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[40]]
                if "Africa/Mogadishu" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[41]]
                if "Africa/Monrovia" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[42]]
                if "Africa/Nairobi" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[43]]
                if "Africa/Ndjamena" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[44]]
                if "Africa/Niamey" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[45]]
                if "Africa/Nouakchott" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[46]]
                if "Africa/Ouagadougou" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[47]]
                if "Africa/Porto-Novo" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[48]]
                if "Africa/Sao_Tome" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[49]]
                if "Africa/Timbuktu" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[50]]
                if "Africa/Tripoli" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[51]]
                if "Africa/Tunis" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[52]]
                if "Africa/Windhoek" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[53]]
                if "America/Adak" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[54]]
                if "America/Anchorage" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[55]]
                if "America/Anguilla" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[56]]
                if "America/Antigua" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[57]]
                if "America/Araguaina" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[58]]
                if "America/Argentina/Buenos_Aires" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[59]]
                if "America/Argentina/Catamarca" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[60]]
                if "America/Argentina/ComodRivadavia" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[61]]
                if "America/Argentina/Cordoba" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[62]]
                if "America/Argentina/Jujuy" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[63]]
                if "America/Argentina/La_Rioja" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[64]]
                if "America/Argentina/Mendoza" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[65]]
                if "America/Argentina/Rio_Gallegos" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[66]]
                if "America/Argentina/Salta" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[67]]
                if "America/Argentina/San_Juan" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[68]]
                if "America/Argentina/San_Luis" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[69]]
                if "America/Argentina/Tucuman" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[70]]
                if "America/Argentina/Ushuaia" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[71]]
                if "America/Aruba" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[72]]
                if "America/Asuncion" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[73]]
                if "America/Atikokan" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[74]]
                if "America/Atka" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[75]]
                if "America/Bahia" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[76]]
                if "America/Bahia_Banderas" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[77]]
                if "America/Barbados" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[78]]
                if "America/Belem" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[79]]
                if "America/Belize" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[80]]
                if "America/Blanc-Sablon" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[81]]
                if "America/Boa_Vista" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[82]]
                if "America/Bogota" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[83]]
                if "America/Boise" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[84]]
                if "America/Buenos_Aires" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[85]]
                if "America/Cambridge_Bay" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[86]]
                if "America/Campo_Grande" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[87]]
                if "America/Cancun" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[88]]
                if "America/Caracas" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[89]]
                if "America/Catamarca" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[90]]
                if "America/Cayenne" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[91]]
                if "America/Cayman" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[92]]
                if "America/Chicago" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[93]]
                if "America/Chihuahua" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[94]]
                if "America/Ciudad_Juarez" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[95]]
                if "America/Coral_Harbour" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[96]]
                if "America/Cordoba" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[97]]
                if "America/Costa_Rica" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[98]]
                if "America/Creston" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[99]]
                if "America/Cuiaba" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[100]]
                if "America/Curacao" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[101]]
                if "America/Danmarkshavn" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[102]]
                if "America/Dawson" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[103]]
                if "America/Dawson_Creek" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[104]]
                if "America/Denver" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[105]]
                if "America/Detroit" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[106]]
                if "America/Dominica" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[107]]
                if "America/Edmonton" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[108]]
                if "America/Eirunepe" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[109]]
                if "America/El_Salvador" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[110]]
                if "America/Ensenada" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[111]]
                if "America/Fort_Nelson" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[112]]
                if "America/Fort_Wayne" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[113]]
                if "America/Fortaleza" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[114]]
                if "America/Glace_Bay" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[115]]
                if "America/Godthab" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[116]]
                if "America/Goose_Bay" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[117]]
                if "America/Grand_Turk" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[118]]
                if "America/Grenada" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[119]]
                if "America/Guadeloupe" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[120]]
                if "America/Guatemala" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[121]]
                if "America/Guayaquil" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[122]]
                if "America/Guyana" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[123]]
                if "America/Halifax" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[124]]
                if "America/Havana" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[125]]
                if "America/Hermosillo" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[126]]
                if "America/Indiana/Indianapolis" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[127]]
                if "America/Indiana/Knox" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[128]]
                if "America/Indiana/Marengo" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[129]]
                if "America/Indiana/Petersburg" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[130]]
                if "America/Indiana/Tell_City" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[131]]
                if "America/Indiana/Vevay" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[132]]
                if "America/Indiana/Vincennes" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[133]]
                if "America/Indiana/Winamac" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[134]]
                if "America/Indianapolis" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[135]]
                if "America/Inuvik" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[136]]
                if "America/Iqaluit" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[137]]
                if "America/Jamaica" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[138]]
                if "America/Jujuy" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[139]]
                if "America/Juneau" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[140]]
                if "America/Kentucky/Louisville" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[141]]
                if "America/Kentucky/Monticello" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[142]]
                if "America/Knox_IN" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[143]]
                if "America/Kralendijk" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[144]]
                if "America/La_Paz" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[145]]
                if "America/Lima" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[146]]
                if "America/Los_Angeles" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[147]]
                if "America/Louisville" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[148]]
                if "America/Lower_Princes" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[149]]
                if "America/Maceio" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[150]]
                if "America/Managua" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[151]]
                if "America/Manaus" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[152]]
                if "America/Marigot" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[153]]
                if "America/Martinique" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[154]]
                if "America/Matamoros" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[155]]
                if "America/Mazatlan" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[156]]
                if "America/Mendoza" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[157]]
                if "America/Menominee" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[158]]
                if "America/Merida" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[159]]
                if "America/Metlakatla" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[160]]
                if "America/Mexico_City" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[161]]
                if "America/Miquelon" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[162]]
                if "America/Moncton" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[163]]
                if "America/Monterrey" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[164]]
                if "America/Montevideo" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[165]]
                if "America/Montreal" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[166]]
                if "America/Montserrat" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[167]]
                if "America/Nassau" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[168]]
                if "America/New_York" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[169]]
                if "America/Nipigon" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[170]]
                if "America/Nome" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[171]]
                if "America/Noronha" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[172]]
                if "America/North_Dakota/Beulah" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[173]]
                if "America/North_Dakota/Center" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[174]]
                if "America/North_Dakota/New_Salem" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[175]]
                if "America/Nuuk" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[176]]
                if "America/Ojinaga" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[177]]
                if "America/Panama" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[178]]
                if "America/Pangnirtung" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[179]]
                if "America/Paramaribo" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[180]]
                if "America/Phoenix" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[181]]
                if "America/Port-au-Prince" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[182]]
                if "America/Port_of_Spain" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[183]]
                if "America/Porto_Acre" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[184]]
                if "America/Porto_Velho" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[185]]
                if "America/Puerto_Rico" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[186]]
                if "America/Punta_Arenas" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[187]]
                if "America/Rainy_River" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[188]]
                if "America/Rankin_Inlet" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[189]]
                if "America/Recife" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[190]]
                if "America/Regina" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[191]]
                if "America/Resolute" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[192]]
                if "America/Rio_Branco" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[193]]
                if "America/Rosario" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[194]]
                if "America/Santa_Isabel" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[195]]
                if "America/Santarem" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[196]]
                if "America/Santiago" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[197]]
                if "America/Santo_Domingo" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[198]]
                if "America/Sao_Paulo" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[199]]
                if "America/Scoresbysund" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[200]]
                if "America/Shiprock" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[201]]
                if "America/Sitka" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[202]]
                if "America/St_Barthelemy" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[203]]
                if "America/St_Johns" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[204]]
                if "America/St_Kitts" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[205]]
                if "America/St_Lucia" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[206]]
                if "America/St_Thomas" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[207]]
                if "America/St_Vincent" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[208]]
                if "America/Swift_Current" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[209]]
                if "America/Tegucigalpa" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[210]]
                if "America/Thule" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[211]]
                if "America/Thunder_Bay" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[212]]
                if "America/Tijuana" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[213]]
                if "America/Toronto" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[214]]
                if "America/Tortola" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[215]]
                if "America/Vancouver" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[216]]
                if "America/Virgin" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[217]]
                if "America/Whitehorse" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[218]]
                if "America/Winnipeg" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[219]]
                if "America/Yakutat" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[220]]
                if "America/Yellowknife" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[221]]
                if "Antarctica/Casey" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[222]]
                if "Antarctica/Davis" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[223]]
                if "Antarctica/DumontDUrville" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[224]]
                if "Antarctica/Macquarie" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[225]]
                if "Antarctica/Mawson" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[226]]
                if "Antarctica/McMurdo" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[227]]
                if "Antarctica/Palmer" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[228]]
                if "Antarctica/Rothera" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[229]]
                if "Antarctica/South_Pole" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[230]]
                if "Antarctica/Syowa" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[231]]
                if "Antarctica/Troll" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[232]]
                if "Antarctica/Vostok" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[233]]
                if "Arctic/Longyearbyen" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[234]]
                if "Asia/Aden" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[235]]
                if "Asia/Almaty" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[236]]
                if "Asia/Amman" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[237]]
                if "Asia/Anadyr" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[238]]
                if "Asia/Aqtau" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[239]]
                if "Asia/Aqtobe" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[240]]
                if "Asia/Ashgabat" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[241]]
                if "Asia/Ashkhabad" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[242]]
                if "Asia/Atyrau" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[243]]
                if "Asia/Baghdad" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[244]]
                if "Asia/Bahrain" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[245]]
                if "Asia/Baku" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[246]]
                if "Asia/Bangkok" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[247]]
                if "Asia/Barnaul" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[248]]
                if "Asia/Beirut" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[249]]
                if "Asia/Bishkek" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[250]]
                if "Asia/Brunei" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[251]]
                if "Asia/Calcutta" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[252]]
                if "Asia/Chita" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[253]]
                if "Asia/Choibalsan" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[254]]
                if "Asia/Chongqing" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[255]]
                if "Asia/Chungking" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[256]]
                if "Asia/Colombo" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[257]]
                if "Asia/Dacca" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[258]]
                if "Asia/Damascus" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[259]]
                if "Asia/Dhaka" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[260]]
                if "Asia/Dili" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[261]]
                if "Asia/Dubai" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[262]]
                if "Asia/Dushanbe" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[263]]
                if "Asia/Famagusta" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[264]]
                if "Asia/Gaza" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[265]]
                if "Asia/Harbin" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[266]]
                if "Asia/Hebron" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[267]]
                if "Asia/Ho_Chi_Minh" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[268]]
                if "Asia/Hong_Kong" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[269]]
                if "Asia/Hovd" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[270]]
                if "Asia/Irkutsk" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[271]]
                if "Asia/Istanbul" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[272]]
                if "Asia/Jakarta" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[273]]
                if "Asia/Jayapura" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[274]]
                if "Asia/Jerusalem" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[275]]
                if "Asia/Kabul" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[276]]
                if "Asia/Kamchatka" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[277]]
                if "Asia/Karachi" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[278]]
                if "Asia/Kashgar" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[279]]
                if "Asia/Kathmandu" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[280]]
                if "Asia/Katmandu" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[281]]
                if "Asia/Khandyga" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[282]]
                if "Asia/Kolkata" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[283]]
                if "Asia/Krasnoyarsk" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[284]]
                if "Asia/Kuala_Lumpur" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[285]]
                if "Asia/Kuching" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[286]]
                if "Asia/Kuwait" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[287]]
                if "Asia/Macao" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[288]]
                if "Asia/Macau" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[289]]
                if "Asia/Magadan" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[290]]
                if "Asia/Makassar" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[291]]
                if "Asia/Manila" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[292]]
                if "Asia/Muscat" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[293]]
                if "Asia/Nicosia" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[294]]
                if "Asia/Novokuznetsk" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[295]]
                if "Asia/Novosibirsk" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[296]]
                if "Asia/Omsk" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[297]]
                if "Asia/Oral" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[298]]
                if "Asia/Phnom_Penh" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[299]]
                if "Asia/Pontianak" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[300]]
                if "Asia/Pyongyang" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[301]]
                if "Asia/Qatar" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[302]]
                if "Asia/Qostanay" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[303]]
                if "Asia/Qyzylorda" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[304]]
                if "Asia/Rangoon" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[305]]
                if "Asia/Riyadh" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[306]]
                if "Asia/Saigon" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[307]]
                if "Asia/Sakhalin" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[308]]
                if "Asia/Samarkand" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[309]]
                if "Asia/Seoul" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[310]]
                if "Asia/Shanghai" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[311]]
                if "Asia/Singapore" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[312]]
                if "Asia/Srednekolymsk" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[313]]
                if "Asia/Taipei" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[314]]
                if "Asia/Tashkent" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[315]]
                if "Asia/Tbilisi" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[316]]
                if "Asia/Tehran" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[317]]
                if "Asia/Tel_Aviv" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[318]]
                if "Asia/Thimbu" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[319]]
                if "Asia/Thimphu" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[320]]
                if "Asia/Tokyo" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[321]]
                if "Asia/Tomsk" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[322]]
                if "Asia/Ujung_Pandang" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[323]]
                if "Asia/Ulaanbaatar" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[324]]
                if "Asia/Ulan_Bator" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[325]]
                if "Asia/Urumqi" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[326]]
                if "Asia/Ust-Nera" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[327]]
                if "Asia/Vientiane" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[328]]
                if "Asia/Vladivostok" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[329]]
                if "Asia/Yakutsk" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[330]]
                if "Asia/Yangon" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[331]]
                if "Asia/Yekaterinburg" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[332]]
                if "Asia/Yerevan" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[333]]
                if "Atlantic/Azores" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[334]]
                if "Atlantic/Bermuda" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[335]]
                if "Atlantic/Canary" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[336]]
                if "Atlantic/Cape_Verde" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[337]]
                if "Atlantic/Faeroe" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[338]]
                if "Atlantic/Faroe" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[339]]
                if "Atlantic/Jan_Mayen" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[340]]
                if "Atlantic/Madeira" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[341]]
                if "Atlantic/Reykjavik" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[342]]
                if "Atlantic/South_Georgia" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[343]]
                if "Atlantic/St_Helena" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[344]]
                if "Atlantic/Stanley" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[345]]
                if "Australia/ACT" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[346]]
                if "Australia/Adelaide" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[347]]
                if "Australia/Brisbane" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[348]]
                if "Australia/Broken_Hill" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[349]]
                if "Australia/Canberra" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[350]]
                if "Australia/Currie" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[351]]
                if "Australia/Darwin" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[352]]
                if "Australia/Eucla" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[353]]
                if "Australia/Hobart" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[354]]
                if "Australia/LHI" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[355]]
                if "Australia/Lindeman" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[356]]
                if "Australia/Lord_Howe" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[357]]
                if "Australia/Melbourne" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[358]]
                if "Australia/NSW" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[359]]
                if "Australia/North" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[360]]
                if "Australia/Perth" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[361]]
                if "Australia/Queensland" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[362]]
                if "Australia/South" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[363]]
                if "Australia/Sydney" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[364]]
                if "Australia/Tasmania" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[365]]
                if "Australia/Victoria" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[366]]
                if "Australia/West" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[367]]
                if "Australia/Yancowinna" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[368]]
                if "Brazil/Acre" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[369]]
                if "Brazil/DeNoronha" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[370]]
                if "Brazil/East" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[371]]
                if "Brazil/West" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[372]]
                if "CET" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[373]]
                if "CST6CDT" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[374]]
                if "Canada/Atlantic" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[375]]
                if "Canada/Central" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[376]]
                if "Canada/Eastern" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[377]]
                if "Canada/Mountain" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[378]]
                if "Canada/Newfoundland" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[379]]
                if "Canada/Pacific" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[380]]
                if "Canada/Saskatchewan" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[381]]
                if "Canada/Yukon" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[382]]
                if "Chile/Continental" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[383]]
                if "Chile/EasterIsland" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[384]]
                if "Cuba" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[385]]
                if "EET" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[386]]
                if "EST" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[387]]
                if "EST5EDT" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[388]]
                if "Egypt" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[389]]
                if "Eire" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[390]]
                if "Etc/GMT" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[391]]
                if "Etc/GMT+0" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[392]]
                if "Etc/GMT+1" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[393]]
                if "Etc/GMT+10" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[394]]
                if "Etc/GMT+11" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[395]]
                if "Etc/GMT+12" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[396]]
                if "Etc/GMT+2" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[397]]
                if "Etc/GMT+3" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[398]]
                if "Etc/GMT+4" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[399]]
                if "Etc/GMT+5" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[400]]
                if "Etc/GMT+6" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[401]]
                if "Etc/GMT+7" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[402]]
                if "Etc/GMT+8" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[403]]
                if "Etc/GMT+9" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[404]]
                if "Etc/GMT-0" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[405]]
                if "Etc/GMT-1" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[406]]
                if "Etc/GMT-10" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[407]]
                if "Etc/GMT-11" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[408]]
                if "Etc/GMT-12" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[409]]
                if "Etc/GMT-13" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[410]]
                if "Etc/GMT-14" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[411]]
                if "Etc/GMT-2" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[412]]
                if "Etc/GMT-3" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[413]]
                if "Etc/GMT-4" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[414]]
                if "Etc/GMT-5" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[415]]
                if "Etc/GMT-6" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[416]]
                if "Etc/GMT-7" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[417]]
                if "Etc/GMT-8" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[418]]
                if "Etc/GMT-9" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[419]]
                if "Etc/GMT0" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[420]]
                if "Etc/Greenwich" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[421]]
                if "Etc/UCT" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[422]]
                if "Etc/UTC" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[423]]
                if "Etc/Universal" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[424]]
                if "Etc/Zulu" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[425]]
                if "Europe/Amsterdam" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[426]]
                if "Europe/Andorra" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[427]]
                if "Europe/Astrakhan" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[428]]
                if "Europe/Athens" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[429]]
                if "Europe/Belfast" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[430]]
                if "Europe/Belgrade" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[431]]
                if "Europe/Berlin" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[432]]
                if "Europe/Bratislava" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[433]]
                if "Europe/Brussels" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[434]]
                if "Europe/Bucharest" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[435]]
                if "Europe/Budapest" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[436]]
                if "Europe/Busingen" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[437]]
                if "Europe/Chisinau" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[438]]
                if "Europe/Copenhagen" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[439]]
                if "Europe/Dublin" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[440]]
                if "Europe/Gibraltar" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[441]]
                if "Europe/Guernsey" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[442]]
                if "Europe/Helsinki" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[443]]
                if "Europe/Isle_of_Man" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[444]]
                if "Europe/Istanbul" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[445]]
                if "Europe/Jersey" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[446]]
                if "Europe/Kaliningrad" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[447]]
                if "Europe/Kiev" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[448]]
                if "Europe/Kirov" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[449]]
                if "Europe/Kyiv" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[450]]
                if "Europe/Lisbon" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[451]]
                if "Europe/Ljubljana" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[452]]
                if "Europe/London" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[453]]
                if "Europe/Luxembourg" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[454]]
                if "Europe/Madrid" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[455]]
                if "Europe/Malta" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[456]]
                if "Europe/Mariehamn" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[457]]
                if "Europe/Minsk" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[458]]
                if "Europe/Monaco" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[459]]
                if "Europe/Moscow" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[460]]
                if "Europe/Nicosia" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[461]]
                if "Europe/Oslo" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[462]]
                if "Europe/Paris" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[463]]
                if "Europe/Podgorica" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[464]]
                if "Europe/Prague" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[465]]
                if "Europe/Riga" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[466]]
                if "Europe/Rome" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[467]]
                if "Europe/Samara" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[468]]
                if "Europe/San_Marino" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[469]]
                if "Europe/Sarajevo" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[470]]
                if "Europe/Saratov" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[471]]
                if "Europe/Simferopol" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[472]]
                if "Europe/Skopje" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[473]]
                if "Europe/Sofia" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[474]]
                if "Europe/Stockholm" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[475]]
                if "Europe/Tallinn" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[476]]
                if "Europe/Tirane" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[477]]
                if "Europe/Tiraspol" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[478]]
                if "Europe/Ulyanovsk" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[479]]
                if "Europe/Uzhgorod" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[480]]
                if "Europe/Vaduz" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[481]]
                if "Europe/Vatican" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[482]]
                if "Europe/Vienna" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[483]]
                if "Europe/Vilnius" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[484]]
                if "Europe/Volgograd" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[485]]
                if "Europe/Warsaw" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[486]]
                if "Europe/Zagreb" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[487]]
                if "Europe/Zaporozhye" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[488]]
                if "Europe/Zurich" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[489]]
                if "Factory" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[490]]
                if "GB" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[491]]
                if "GB-Eire" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[492]]
                if "GMT" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[493]]
                if "GMT+0" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[494]]
                if "GMT-0" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[495]]
                if "GMT0" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[496]]
                if "Greenwich" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[497]]
                if "HST" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[498]]
                if "Hongkong" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[499]]
                if "Iceland" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[500]]
                if "Indian/Antananarivo" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[501]]
                if "Indian/Chagos" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[502]]
                if "Indian/Christmas" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[503]]
                if "Indian/Cocos" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[504]]
                if "Indian/Comoro" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[505]]
                if "Indian/Kerguelen" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[506]]
                if "Indian/Mahe" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[507]]
                if "Indian/Maldives" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[508]]
                if "Indian/Mauritius" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[509]]
                if "Indian/Mayotte" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[510]]
                if "Indian/Reunion" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[511]]
                if "Iran" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[512]]
                if "Israel" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[513]]
                if "Jamaica" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[514]]
                if "Japan" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[515]]
                if "Kwajalein" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[516]]
                if "Libya" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[517]]
                if "MET" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[518]]
                if "MST" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[519]]
                if "MST7MDT" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[520]]
                if "Mexico/BajaNorte" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[521]]
                if "Mexico/BajaSur" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[522]]
                if "Mexico/General" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[523]]
                if "NZ" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[524]]
                if "NZ-CHAT" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[525]]
                if "Navajo" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[526]]
                if "PRC" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[527]]
                if "PST8PDT" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[528]]
                if "Pacific/Apia" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[529]]
                if "Pacific/Auckland" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[530]]
                if "Pacific/Bougainville" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[531]]
                if "Pacific/Chatham" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[532]]
                if "Pacific/Chuuk" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[533]]
                if "Pacific/Easter" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[534]]
                if "Pacific/Efate" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[535]]
                if "Pacific/Enderbury" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[536]]
                if "Pacific/Fakaofo" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[537]]
                if "Pacific/Fiji" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[538]]
                if "Pacific/Funafuti" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[539]]
                if "Pacific/Galapagos" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[540]]
                if "Pacific/Gambier" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[541]]
                if "Pacific/Guadalcanal" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[542]]
                if "Pacific/Guam" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[543]]
                if "Pacific/Honolulu" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[544]]
                if "Pacific/Johnston" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[545]]
                if "Pacific/Kanton" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[546]]
                if "Pacific/Kiritimati" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[547]]
                if "Pacific/Kosrae" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[548]]
                if "Pacific/Kwajalein" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[549]]
                if "Pacific/Majuro" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[550]]
                if "Pacific/Marquesas" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[551]]
                if "Pacific/Midway" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[552]]
                if "Pacific/Nauru" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[553]]
                if "Pacific/Niue" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[554]]
                if "Pacific/Norfolk" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[555]]
                if "Pacific/Noumea" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[556]]
                if "Pacific/Pago_Pago" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[557]]
                if "Pacific/Palau" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[558]]
                if "Pacific/Pitcairn" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[559]]
                if "Pacific/Pohnpei" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[560]]
                if "Pacific/Ponape" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[561]]
                if "Pacific/Port_Moresby" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[562]]
                if "Pacific/Rarotonga" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[563]]
                if "Pacific/Saipan" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[564]]
                if "Pacific/Samoa" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[565]]
                if "Pacific/Tahiti" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[566]]
                if "Pacific/Tarawa" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[567]]
                if "Pacific/Tongatapu" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[568]]
                if "Pacific/Truk" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[569]]
                if "Pacific/Wake" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[570]]
                if "Pacific/Wallis" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[571]]
                if "Pacific/Yap" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[572]]
                if "Poland" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[573]]
                if "Portugal" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[574]]
                if "ROC" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[575]]
                if "ROK" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[576]]
                if "Singapore" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[577]]
                if "Turkey" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[578]]
                if "UCT" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[579]]
                if "US/Alaska" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[580]]
                if "US/Aleutian" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[581]]
                if "US/Arizona" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[582]]
                if "US/Central" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[583]]
                if "US/East-Indiana" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[584]]
                if "US/Eastern" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[585]]
                if "US/Hawaii" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[586]]
                if "US/Indiana-Starke" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[587]]
                if "US/Michigan" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[588]]
                if "US/Mountain" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[589]]
                if "US/Pacific" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[590]]
                if "US/Samoa" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[591]]
                if "UTC" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[592]]
                if "Universal" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[593]]
                if "W-SU" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[594]]
                if "WET" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[595]]
                if "Zulu" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                    return t.enum_values[t.generated_offsets[596]]
                raise Error("wrong state")

            @staticmethod
            def create(greycat: GreyCat) -> std.core.TimeZone:
                return std.core.TimeZone(greycat.libs_by_name[std.name_].mapped[3], [])

        @final
        class t3(std_n.core._t3):
            name_: Final[str] = "core::t3"

            def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
                super().__init__(type)

            @staticmethod
            def create(greycat: GreyCat) -> std_n.core._t3:
                return std.core.t3(greycat.libs_by_name[std.name_].mapped[4], [])

        @final
        class SortOrder(GreyCat.Enum):
            name_: Final[str] = "core::SortOrder"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def __class_getitem__(cls, key) -> std.core.SortOrder:
                if isinstance(key, tuple):
                    key, greycat = key
                else:
                    greycat = GreyCat._DEFAULT
                if "asc" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[5]
                    return t.enum_values[t.generated_offsets[0]]
                if "desc" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[5]
                    return t.enum_values[t.generated_offsets[1]]
                raise Error("wrong state")

            @staticmethod
            def create(greycat: GreyCat) -> std.core.SortOrder:
                return std.core.SortOrder(greycat.libs_by_name[std.name_].mapped[5], [])

        @final
        class FloatPrecision(GreyCat.Enum):
            name_: Final[str] = "core::FloatPrecision"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def __class_getitem__(cls, key) -> std.core.FloatPrecision:
                if isinstance(key, tuple):
                    key, greycat = key
                else:
                    greycat = GreyCat._DEFAULT
                if "p1" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[6]
                    return t.enum_values[t.generated_offsets[0]]
                if "p10" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[6]
                    return t.enum_values[t.generated_offsets[1]]
                if "p100" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[6]
                    return t.enum_values[t.generated_offsets[2]]
                if "p1000" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[6]
                    return t.enum_values[t.generated_offsets[3]]
                if "p10000" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[6]
                    return t.enum_values[t.generated_offsets[4]]
                if "p100000" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[6]
                    return t.enum_values[t.generated_offsets[5]]
                if "p1000000" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[6]
                    return t.enum_values[t.generated_offsets[6]]
                if "p10000000" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[6]
                    return t.enum_values[t.generated_offsets[7]]
                if "p100000000" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[6]
                    return t.enum_values[t.generated_offsets[8]]
                if "p1000000000" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[6]
                    return t.enum_values[t.generated_offsets[9]]
                if "p10000000000" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[6]
                    return t.enum_values[t.generated_offsets[10]]
                raise Error("wrong state")

            @staticmethod
            def create(greycat: GreyCat) -> std.core.FloatPrecision:
                return std.core.FloatPrecision(greycat.libs_by_name[std.name_].mapped[6], [])

        @final
        class t2(std_n.core._t2):
            name_: Final[str] = "core::t2"

            def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
                super().__init__(type)

            @staticmethod
            def create(greycat: GreyCat) -> std_n.core._t2:
                return std.core.t2(greycat.libs_by_name[std.name_].mapped[7], [])

        @final
        class t4f(std_n.core._t4f):
            name_: Final[str] = "core::t4f"

            def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
                super().__init__(type)

            @staticmethod
            def create(greycat: GreyCat) -> std_n.core._t4f:
                return std.core.t4f(greycat.libs_by_name[std.name_].mapped[8], [])

        @final
        class Array(Generic[__T], std_n.core._Array[__T]):
            name_: Final[str] = "core::Array"

            def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
                super().__init__(type)

            @staticmethod
            def create(greycat: GreyCat) -> std_n.core._Array:
                return std.core.Array(greycat.libs_by_name[std.name_].mapped[9], [])

        @final
        class Tuple(Generic[__T, __U], GreyCat.Object):
            name_: Final[str] = "core::Tuple"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def x(self) -> std.core.__:
                return self._get(self.type_.generated_offsets[0])

            def set_x(self, v: std.core.__) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def y(self) -> std.core.__:
                return self._get(self.type_.generated_offsets[1])

            def set_y(self, v: std.core.__) -> None:
                self._set(self.type_.generated_offsets[1], v)

            @staticmethod
            def create(greycat: GreyCat, x: std.core.__, y: std.core.__) -> std.core.Tuple[TypeVar("T"), TypeVar("U")]:
                return std.core.Tuple(greycat.libs_by_name[std.name_].mapped[10], [x, y])

        @final
        class Map(Generic[__K, __V], std_n.core._Map[__K, __V]):
            name_: Final[str] = "core::Map"

            def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
                super().__init__(type)

            @staticmethod
            def create(greycat: GreyCat) -> std_n.core._Map:
                return std.core.Map(greycat.libs_by_name[std.name_].mapped[11], [])

        @final
        class String(std_n.core._String):
            name_: Final[str] = "core::String"

            def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
                super().__init__(type)

            @staticmethod
            def create(greycat: GreyCat) -> std_n.core._String:
                return std.core.String(greycat.libs_by_name[std.name_].mapped[12], [])

        @final
        class field(std_n.core._field):
            name_: Final[str] = "core::field"

            def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
                super().__init__(type)

            @staticmethod
            def create(greycat: GreyCat) -> std_n.core._field:
                return std.core.field(greycat.libs_by_name[std.name_].mapped[13], [])

        @final
        class Tensor(std_n.core._Tensor):
            name_: Final[str] = "core::Tensor"

            def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
                super().__init__(type)

            @staticmethod
            def create(greycat: GreyCat) -> std_n.core._Tensor:
                return std.core.Tensor(greycat.libs_by_name[std.name_].mapped[14], [])

        @final
        class NodeInfo(Generic[__T], GreyCat.Object):
            name_: Final[str] = "core::NodeInfo"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def size(self) -> int:
                return self._get(self.type_.generated_offsets[0])

            def set_size(self, v: int) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def from_(self) -> std.core.__:
                return self._get(self.type_.generated_offsets[1])

            def set_from(self, v: std.core.__) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def to(self) -> std.core.__:
                return self._get(self.type_.generated_offsets[2])

            def set_to(self, v: std.core.__) -> None:
                self._set(self.type_.generated_offsets[2], v)

            @staticmethod
            def create(greycat: GreyCat, size: int, from_: std.core.__, to: std.core.__) -> std.core.NodeInfo[TypeVar("T")]:
                return std.core.NodeInfo(greycat.libs_by_name[std.name_].mapped[15], [size, from_, to])

        @final
        class MathConstants(GreyCat.Object):
            name_: Final[str] = "core::MathConstants"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            @staticmethod
            def e(greycat: GreyCat) -> float:
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[16]
                return t.static_values[0]

            @staticmethod
            def log_2e(greycat: GreyCat) -> float:
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[16]
                return t.static_values[1]

            @staticmethod
            def log_10e(greycat: GreyCat) -> float:
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[16]
                return t.static_values[2]

            @staticmethod
            def ln2(greycat: GreyCat) -> float:
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[16]
                return t.static_values[3]

            @staticmethod
            def ln10(greycat: GreyCat) -> float:
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[16]
                return t.static_values[4]

            @staticmethod
            def pi(greycat: GreyCat) -> float:
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[16]
                return t.static_values[5]

            @staticmethod
            def pi_2(greycat: GreyCat) -> float:
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[16]
                return t.static_values[6]

            @staticmethod
            def pi_4(greycat: GreyCat) -> float:
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[16]
                return t.static_values[7]

            @staticmethod
            def m1_pi(greycat: GreyCat) -> float:
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[16]
                return t.static_values[8]

            @staticmethod
            def m2_pi(greycat: GreyCat) -> float:
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[16]
                return t.static_values[9]

            @staticmethod
            def m2_sqrt_pi(greycat: GreyCat) -> float:
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[16]
                return t.static_values[10]

            @staticmethod
            def sqrt2(greycat: GreyCat) -> float:
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[16]
                return t.static_values[11]

            @staticmethod
            def sqrt1_2(greycat: GreyCat) -> float:
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[16]
                return t.static_values[12]

            @staticmethod
            def create(greycat: GreyCat) -> std.core.MathConstants:
                return std.core.MathConstants(greycat.libs_by_name[std.name_].mapped[16], [])

        @final
        class t3f(std_n.core._t3f):
            name_: Final[str] = "core::t3f"

            def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
                super().__init__(type)

            @staticmethod
            def create(greycat: GreyCat) -> std_n.core._t3f:
                return std.core.t3f(greycat.libs_by_name[std.name_].mapped[17], [])

        @final
        class type(std_n.core._type):
            name_: Final[str] = "core::type"

            def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
                super().__init__(type)

            @staticmethod
            def create(greycat: GreyCat) -> std_n.core._type:
                return std.core.type(greycat.libs_by_name[std.name_].mapped[18], [])

        @final
        class Table(Generic[__T], std_n.core._Table[__T]):
            name_: Final[str] = "core::Table"

            def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
                super().__init__(type)

            @staticmethod
            def create(greycat: GreyCat) -> std_n.core._Table:
                return std.core.Table(greycat.libs_by_name[std.name_].mapped[19], [])

        @final
        class nodeIndex(Generic[__K, __V], std_n.core._nodeIndex[__K, __V]):
            name_: Final[str] = "core::nodeIndex"

            def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
                super().__init__(type)

            @staticmethod
            def create(greycat: GreyCat) -> std_n.core._nodeIndex:
                return std.core.nodeIndex(greycat.libs_by_name[std.name_].mapped[20], [])

        @final
        class Buffer(std_n.core._Buffer):
            name_: Final[str] = "core::Buffer"

            def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
                super().__init__(type)

            @staticmethod
            def create(greycat: GreyCat) -> std_n.core._Buffer:
                return std.core.Buffer(greycat.libs_by_name[std.name_].mapped[21], [])

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
            def create(greycat: GreyCat, sw: std.core.geo, ne: std.core.geo) -> std.core.GeoBox:
                return std.core.GeoBox(greycat.libs_by_name[std.name_].mapped[22], [sw, ne])

        @final
        class DurationUnit(GreyCat.Enum):
            name_: Final[str] = "core::DurationUnit"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def __class_getitem__(cls, key) -> std.core.DurationUnit:
                if isinstance(key, tuple):
                    key, greycat = key
                else:
                    greycat = GreyCat._DEFAULT
                if "microseconds" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[23]
                    return t.enum_values[t.generated_offsets[0]]
                if "milliseconds" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[23]
                    return t.enum_values[t.generated_offsets[1]]
                if "seconds" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[23]
                    return t.enum_values[t.generated_offsets[2]]
                if "minutes" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[23]
                    return t.enum_values[t.generated_offsets[3]]
                if "hours" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[23]
                    return t.enum_values[t.generated_offsets[4]]
                if "days" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[23]
                    return t.enum_values[t.generated_offsets[5]]
                raise Error("wrong state")

            @staticmethod
            def create(greycat: GreyCat) -> std.core.DurationUnit:
                return std.core.DurationUnit(greycat.libs_by_name[std.name_].mapped[23], [])

        @final
        class nodeTime(Generic[__T], std_n.core._nodeTime[__T]):
            name_: Final[str] = "core::nodeTime"

            def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
                super().__init__(type)

            @staticmethod
            def create(greycat: GreyCat) -> std_n.core._nodeTime:
                return std.core.nodeTime(greycat.libs_by_name[std.name_].mapped[24], [])

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
            def create(greycat: GreyCat, t: std.core.time, v: Any) -> std.core.nodeTimeSingleton:
                return std.core.nodeTimeSingleton(greycat.libs_by_name[std.name_].mapped[25], [t, v])

        @final
        class nodeList(Generic[__T], std_n.core._nodeList[__T]):
            name_: Final[str] = "core::nodeList"

            def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
                super().__init__(type)

            @staticmethod
            def create(greycat: GreyCat) -> std_n.core._nodeList:
                return std.core.nodeList(greycat.libs_by_name[std.name_].mapped[26], [])

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
            def create(greycat: GreyCat, center: std.core.geo, radius: float) -> std.core.GeoCircle:
                return std.core.GeoCircle(greycat.libs_by_name[std.name_].mapped[27], [center, radius])

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
            def create(greycat: GreyCat, points: std.core.Array) -> std.core.GeoPoly:
                return std.core.GeoPoly(greycat.libs_by_name[std.name_].mapped[28], [points])

        @final
        class Error(GreyCat.Object):
            name_: Final[str] = "core::Error"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def message(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_message(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def stack(self) -> std.core.Array:
                return self._get(self.type_.generated_offsets[1])

            def set_stack(self, v: std.core.Array) -> None:
                self._set(self.type_.generated_offsets[1], v)

            @staticmethod
            def create(greycat: GreyCat, message: str, stack: std.core.Array) -> std.core.Error:
                return std.core.Error(greycat.libs_by_name[std.name_].mapped[29], [message, stack])

        @final
        class ErrorFrame(GreyCat.Object):
            name_: Final[str] = "core::ErrorFrame"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def module(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_module(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def function(self) -> str:
                return self._get(self.type_.generated_offsets[1])

            def set_function(self, v: str) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def line(self) -> int:
                return self._get(self.type_.generated_offsets[2])

            def set_line(self, v: int) -> None:
                self._set(self.type_.generated_offsets[2], v)

            def column(self) -> int:
                return self._get(self.type_.generated_offsets[3])

            def set_column(self, v: int) -> None:
                self._set(self.type_.generated_offsets[3], v)

            @staticmethod
            def create(greycat: GreyCat, module: str, function: str, line: int, column: int) -> std.core.ErrorFrame:
                return std.core.ErrorFrame(greycat.libs_by_name[std.name_].mapped[30], [module, function, line, column])

        @final
        class duration(std_n.core._duration):
            name_: Final[str] = "core::duration"

            def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
                super().__init__(type)

            @staticmethod
            def create(greycat: GreyCat) -> std_n.core._duration:
                return std.core.duration(greycat.libs_by_name[std.name_].mapped[31], [])

        @final
        class geo(std_n.core._geo):
            name_: Final[str] = "core::geo"

            def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
                super().__init__(type)

            @staticmethod
            def create(greycat: GreyCat) -> std_n.core._geo:
                return std.core.geo(greycat.libs_by_name[std.name_].mapped[32], [])

        @final
        class function(std_n.core._function):
            name_: Final[str] = "core::function"

            def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
                super().__init__(type)

            @staticmethod
            def create(greycat: GreyCat) -> std_n.core._function:
                return std.core.function(greycat.libs_by_name[std.name_].mapped[33], [])

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
            def create(greycat: GreyCat, column: int, extractors: std.core.Array) -> std.core.TableColumnMapping:
                return std.core.TableColumnMapping(greycat.libs_by_name[std.name_].mapped[34], [column, extractors])

        @final
        class time(std_n.core._time):
            name_: Final[str] = "core::time"

            def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
                super().__init__(type)

            @staticmethod
            def create(greycat: GreyCat) -> std_n.core._time:
                return std.core.time(greycat.libs_by_name[std.name_].mapped[35], [])

        @final
        class t2f(std_n.core._t2f):
            name_: Final[str] = "core::t2f"

            def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
                super().__init__(type)

            @staticmethod
            def create(greycat: GreyCat) -> std_n.core._t2f:
                return std.core.t2f(greycat.libs_by_name[std.name_].mapped[36], [])

        @final
        class TensorType(GreyCat.Enum):
            name_: Final[str] = "core::TensorType"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def __class_getitem__(cls, key) -> std.core.TensorType:
                if isinstance(key, tuple):
                    key, greycat = key
                else:
                    greycat = GreyCat._DEFAULT
                if "i32" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[37]
                    return t.enum_values[t.generated_offsets[0]]
                if "i64" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[37]
                    return t.enum_values[t.generated_offsets[1]]
                if "f32" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[37]
                    return t.enum_values[t.generated_offsets[2]]
                if "f64" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[37]
                    return t.enum_values[t.generated_offsets[3]]
                if "c64" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[37]
                    return t.enum_values[t.generated_offsets[4]]
                if "c128" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[37]
                    return t.enum_values[t.generated_offsets[5]]
                raise Error("wrong state")

            @staticmethod
            def create(greycat: GreyCat) -> std.core.TensorType:
                return std.core.TensorType(greycat.libs_by_name[std.name_].mapped[37], [])

        @final
        class SamplingMode(GreyCat.Enum):
            name_: Final[str] = "core::SamplingMode"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def __class_getitem__(cls, key) -> std.core.SamplingMode:
                if isinstance(key, tuple):
                    key, greycat = key
                else:
                    greycat = GreyCat._DEFAULT
                if "fixed" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[38]
                    return t.enum_values[t.generated_offsets[0]]
                if "fixed_reg" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[38]
                    return t.enum_values[t.generated_offsets[1]]
                if "adaptative" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[38]
                    return t.enum_values[t.generated_offsets[2]]
                if "dense" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[38]
                    return t.enum_values[t.generated_offsets[3]]
                raise Error("wrong state")

            @staticmethod
            def create(greycat: GreyCat) -> std.core.SamplingMode:
                return std.core.SamplingMode(greycat.libs_by_name[std.name_].mapped[38], [])

        @final
        class CalendarUnit(GreyCat.Enum):
            name_: Final[str] = "core::CalendarUnit"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def __class_getitem__(cls, key) -> std.core.CalendarUnit:
                if isinstance(key, tuple):
                    key, greycat = key
                else:
                    greycat = GreyCat._DEFAULT
                if "year" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[39]
                    return t.enum_values[t.generated_offsets[0]]
                if "month" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[39]
                    return t.enum_values[t.generated_offsets[1]]
                if "day" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[39]
                    return t.enum_values[t.generated_offsets[2]]
                if "hour" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[39]
                    return t.enum_values[t.generated_offsets[3]]
                if "minute" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[39]
                    return t.enum_values[t.generated_offsets[4]]
                if "second" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[39]
                    return t.enum_values[t.generated_offsets[5]]
                if "microsecond" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[39]
                    return t.enum_values[t.generated_offsets[6]]
                raise Error("wrong state")

            @staticmethod
            def create(greycat: GreyCat) -> std.core.CalendarUnit:
                return std.core.CalendarUnit(greycat.libs_by_name[std.name_].mapped[39], [])

        @final
        class node(Generic[__T], std_n.core._node[__T]):
            name_: Final[str] = "core::node"

            def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
                super().__init__(type)

            @staticmethod
            def create(greycat: GreyCat) -> std_n.core._node:
                return std.core.node(greycat.libs_by_name[std.name_].mapped[40], [])

        @final
        class str(std_n.core._str):
            name_: Final[str] = "core::str"

            def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
                super().__init__(type)

            @staticmethod
            def create(greycat: GreyCat) -> std_n.core._str:
                return std.core.str(greycat.libs_by_name[std.name_].mapped[41], [])

        @final
        class nodeGeo(Generic[__T], std_n.core._nodeGeo[__T]):
            name_: Final[str] = "core::nodeGeo"

            def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
                super().__init__(type)

            @staticmethod
            def create(greycat: GreyCat) -> std_n.core._nodeGeo:
                return std.core.nodeGeo(greycat.libs_by_name[std.name_].mapped[42], [])

        @final
        class ErrorCode(GreyCat.Enum):
            name_: Final[str] = "core::ErrorCode"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def __class_getitem__(cls, key) -> std.core.ErrorCode:
                if isinstance(key, tuple):
                    key, greycat = key
                else:
                    greycat = GreyCat._DEFAULT
                if "none" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[43]
                    return t.enum_values[t.generated_offsets[0]]
                if "interrupted" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[43]
                    return t.enum_values[t.generated_offsets[1]]
                if "await_" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[43]
                    return t.enum_values[t.generated_offsets[2]]
                if "timeout" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[43]
                    return t.enum_values[t.generated_offsets[3]]
                if "forbidden" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[43]
                    return t.enum_values[t.generated_offsets[4]]
                if "runtime_error" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[43]
                    return t.enum_values[t.generated_offsets[5]]
                raise Error("wrong state")

            @staticmethod
            def create(greycat: GreyCat) -> std.core.ErrorCode:
                return std.core.ErrorCode(greycat.libs_by_name[std.name_].mapped[43], [])

    @final
    class runtime:
        __T = TypeVar("__T")

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
            def get(__greycat: Optional[GreyCat] = None) -> std.runtime.SecurityFields:
                if __greycat is None:
                    __greycat  = GreyCat.DEFAULT
                return __greycat.call("runtime::SecurityFields::get")

            @staticmethod
            def set(f: std.runtime.SecurityFields, __greycat: Optional[GreyCat] = None) -> None:
                if __greycat is None:
                    __greycat  = GreyCat.DEFAULT
                return __greycat.call("runtime::SecurityFields::set", [f, ])

            @staticmethod
            def create(greycat: GreyCat, email: str, name: str, first_name: str, last_name: str, roles: std.core.Map, groups: std.core.Map) -> std.runtime.SecurityFields:
                return std.runtime.SecurityFields(greycat.libs_by_name[std.name_].mapped[44], [email, name, first_name, last_name, roles, groups])

        @final
        class DebugVariable(GreyCat.Object):
            name_: Final[str] = "runtime::DebugVariable"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def name(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_name(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def value(self) -> Any:
                return self._get(self.type_.generated_offsets[1])

            def set_value(self, v: Any) -> None:
                self._set(self.type_.generated_offsets[1], v)

            @staticmethod
            def create(greycat: GreyCat, name: str, value: Any) -> std.runtime.DebugVariable:
                return std.runtime.DebugVariable(greycat.libs_by_name[std.name_].mapped[45], [name, value])

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
            def create(greycat: GreyCat, version: str, program_version: str, arch: str, timezone: std.core.TimeZone, license: std.runtime.License, io_threads: int, bg_threads: int, fg_threads: int, mem_total: int, mem_worker: int, nb_ctx: int, store_stats: std.runtime.StoreStat) -> std.runtime.RuntimeInfo:
                return std.runtime.RuntimeInfo(greycat.libs_by_name[std.name_].mapped[46], [version, program_version, arch, timezone, license, io_threads, bg_threads, fg_threads, mem_total, mem_worker, nb_ctx, store_stats])

        @final
        class UserGroupPolicyType(GreyCat.Enum):
            name_: Final[str] = "runtime::UserGroupPolicyType"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def __class_getitem__(cls, key) -> std.runtime.UserGroupPolicyType:
                if isinstance(key, tuple):
                    key, greycat = key
                else:
                    greycat = GreyCat._DEFAULT
                if "read" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[47]
                    return t.enum_values[t.generated_offsets[0]]
                if "write" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[47]
                    return t.enum_values[t.generated_offsets[1]]
                if "execute" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[47]
                    return t.enum_values[t.generated_offsets[2]]
                raise Error("wrong state")

            @staticmethod
            def create(greycat: GreyCat) -> std.runtime.UserGroupPolicyType:
                return std.runtime.UserGroupPolicyType(greycat.libs_by_name[std.name_].mapped[47], [])

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
            def create(greycat: GreyCat, offset: int, pass_: str) -> std.runtime.UserCredential:
                return std.runtime.UserCredential(greycat.libs_by_name[std.name_].mapped[48], [offset, pass_])

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
            def create(greycat: GreyCat, id: int, name: str, activated: bool) -> std.runtime.UserGroup:
                return std.runtime.UserGroup(greycat.libs_by_name[std.name_].mapped[49], [id, name, activated])

        @final
        class DebugInfo(GreyCat.Object):
            name_: Final[str] = "runtime::DebugInfo"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def scopes(self) -> std.core.Array:
                return self._get(self.type_.generated_offsets[0])

            def set_scopes(self, v: std.core.Array) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def root(self) -> Any:
                return self._get(self.type_.generated_offsets[1])

            def set_root(self, v: Any) -> None:
                self._set(self.type_.generated_offsets[1], v)

            @staticmethod
            def create(greycat: GreyCat, scopes: std.core.Array, root: Any) -> std.runtime.DebugInfo:
                return std.runtime.DebugInfo(greycat.libs_by_name[std.name_].mapped[50], [scopes, root])

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
                    __greycat  = GreyCat.DEFAULT
                return __greycat.call("runtime::SecurityPolicy::permissions")

            @staticmethod
            def create(greycat: GreyCat, entities: std.core.Array, credentials: std.core.Map, roles: std.core.Map, fields: std.runtime.SecurityFields, keys: std.core.Map, keys_last_refresh: std.core.time) -> std.runtime.SecurityPolicy:
                return std.runtime.SecurityPolicy(greycat.libs_by_name[std.name_].mapped[51], [entities, credentials, roles, fields, keys, keys_last_refresh])

        @final
        class DebugBreakpoint(GreyCat.Object):
            name_: Final[str] = "runtime::DebugBreakpoint"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def module(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_module(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def line(self) -> int:
                return self._get(self.type_.generated_offsets[1])

            def set_line(self, v: int) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def column(self) -> int:
                return self._get(self.type_.generated_offsets[2])

            def set_column(self, v: int) -> None:
                self._set(self.type_.generated_offsets[2], v)

            @staticmethod
            def create(greycat: GreyCat, module: str, line: int, column: int) -> std.runtime.DebugBreakpoint:
                return std.runtime.DebugBreakpoint(greycat.libs_by_name[std.name_].mapped[52], [module, line, column])

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
            def set(entity: std.runtime.SecurityEntity, __greycat: Optional[GreyCat] = None) -> int:
                if __greycat is None:
                    __greycat  = GreyCat.DEFAULT
                return __greycat.call("runtime::SecurityEntity::set", [entity, ])

            @staticmethod
            def all(__greycat: Optional[GreyCat] = None) -> std.core.Array:
                if __greycat is None:
                    __greycat  = GreyCat.DEFAULT
                return __greycat.call("runtime::SecurityEntity::all")

            @staticmethod
            def create(greycat: GreyCat, id: int, name: str, activated: bool) -> std.runtime.SecurityEntity:
                return std.runtime.SecurityEntity(greycat.libs_by_name[std.name_].mapped[53], [id, name, activated])

        @final
        class Log(GreyCat.Object):
            name_: Final[str] = "runtime::Log"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def level(self) -> std.runtime.LogLevel:
                return self._get(self.type_.generated_offsets[0])

            def set_level(self, v: std.runtime.LogLevel) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def time(self) -> std.core.time:
                return self._get(self.type_.generated_offsets[1])

            def set_time(self, v: std.core.time) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def user_id(self) -> int:
                return self._get(self.type_.generated_offsets[2])

            def set_user_id(self, v: int) -> None:
                self._set(self.type_.generated_offsets[2], v)

            def id(self) -> int:
                return self._get(self.type_.generated_offsets[3])

            def set_id(self, v: int) -> None:
                self._set(self.type_.generated_offsets[3], v)

            def id2(self) -> int:
                return self._get(self.type_.generated_offsets[4])

            def set_id2(self, v: int) -> None:
                self._set(self.type_.generated_offsets[4], v)

            def src(self) -> str:
                return self._get(self.type_.generated_offsets[5])

            def set_src(self, v: str) -> None:
                self._set(self.type_.generated_offsets[5], v)

            def tag(self) -> str:
                return self._get(self.type_.generated_offsets[6])

            def set_tag(self, v: str) -> None:
                self._set(self.type_.generated_offsets[6], v)

            def data(self) -> Any:
                return self._get(self.type_.generated_offsets[7])

            def set_data(self, v: Any) -> None:
                self._set(self.type_.generated_offsets[7], v)

            @staticmethod
            def create(greycat: GreyCat, level: std.runtime.LogLevel, time: std.core.time, user_id: int, id: int, id2: int, src: str, tag: str, data: Any) -> std.runtime.Log:
                return std.runtime.Log(greycat.libs_by_name[std.name_].mapped[54], [level, time, user_id, id, id2, src, tag, data])

        @final
        class System(GreyCat.Object):
            name_: Final[str] = "runtime::System"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            @staticmethod
            def create(greycat: GreyCat) -> std.runtime.System:
                return std.runtime.System(greycat.libs_by_name[std.name_].mapped[55], [])

        @final
        class Runtime(GreyCat.Object):
            name_: Final[str] = "runtime::Runtime"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            @staticmethod
            def root(__greycat: Optional[GreyCat] = None) -> Any:
                if __greycat is None:
                    __greycat  = GreyCat.DEFAULT
                return __greycat.call("runtime::Runtime::root")

            @staticmethod
            def abi(__greycat: Optional[GreyCat] = None) -> None:
                if __greycat is None:
                    __greycat  = GreyCat.DEFAULT
                return __greycat.call("runtime::Runtime::abi")

            @staticmethod
            def info(__greycat: Optional[GreyCat] = None) -> std.runtime.RuntimeInfo:
                if __greycat is None:
                    __greycat  = GreyCat.DEFAULT
                return __greycat.call("runtime::Runtime::info")

            @staticmethod
            def create(greycat: GreyCat) -> std.runtime.Runtime:
                return std.runtime.Runtime(greycat.libs_by_name[std.name_].mapped[56], [])

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
            def set(value: std.runtime.UserRole, __greycat: Optional[GreyCat] = None) -> None:
                if __greycat is None:
                    __greycat  = GreyCat.DEFAULT
                return __greycat.call("runtime::UserRole::set", [value, ])

            @staticmethod
            def remove(name: str, __greycat: Optional[GreyCat] = None) -> None:
                if __greycat is None:
                    __greycat  = GreyCat.DEFAULT
                return __greycat.call("runtime::UserRole::remove", [name, ])

            @staticmethod
            def all(__greycat: Optional[GreyCat] = None) -> std.core.Array:
                if __greycat is None:
                    __greycat  = GreyCat.DEFAULT
                return __greycat.call("runtime::UserRole::all")

            @staticmethod
            def create(greycat: GreyCat, name: str, permissions: std.core.Array) -> std.runtime.UserRole:
                return std.runtime.UserRole(greycat.libs_by_name[std.name_].mapped[57], [name, permissions])

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
            def create(greycat: GreyCat, group_id: int, type: std.runtime.UserGroupPolicyType) -> std.runtime.UserGroupPolicy:
                return std.runtime.UserGroupPolicy(greycat.libs_by_name[std.name_].mapped[58], [group_id, type])

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
            def getToken(id: int, __greycat: Optional[GreyCat] = None) -> str:
                if __greycat is None:
                    __greycat  = GreyCat.DEFAULT
                return __greycat.call("runtime::User::getToken", [id, ])

            @staticmethod
            def setPassword(name: str, pass_: str, __greycat: Optional[GreyCat] = None) -> bool:
                if __greycat is None:
                    __greycat  = GreyCat.DEFAULT
                return __greycat.call("runtime::User::setPassword", [name, pass_, ])

            @staticmethod
            def permissions(__greycat: Optional[GreyCat] = None) -> std.core.Array:
                if __greycat is None:
                    __greycat  = GreyCat.DEFAULT
                return __greycat.call("runtime::User::permissions")

            @staticmethod
            def me(__greycat: Optional[GreyCat] = None) -> std.runtime.User:
                if __greycat is None:
                    __greycat  = GreyCat.DEFAULT
                return __greycat.call("runtime::User::me")

            @staticmethod
            def current(__greycat: Optional[GreyCat] = None) -> int:
                if __greycat is None:
                    __greycat  = GreyCat.DEFAULT
                return __greycat.call("runtime::User::current")

            @staticmethod
            def renew(use_cookie: bool, __greycat: Optional[GreyCat] = None) -> str:
                if __greycat is None:
                    __greycat  = GreyCat.DEFAULT
                return __greycat.call("runtime::User::renew", [use_cookie, ])

            @staticmethod
            def logout(__greycat: Optional[GreyCat] = None) -> None:
                if __greycat is None:
                    __greycat  = GreyCat.DEFAULT
                return __greycat.call("runtime::User::logout")

            @staticmethod
            def tokenLogin(token: str, use_cookie: bool, __greycat: Optional[GreyCat] = None) -> str:
                if __greycat is None:
                    __greycat  = GreyCat.DEFAULT
                return __greycat.call("runtime::User::tokenLogin", [token, use_cookie, ])

            @staticmethod
            def login(credentials: str, use_cookie: bool, __greycat: Optional[GreyCat] = None) -> str:
                if __greycat is None:
                    __greycat  = GreyCat.DEFAULT
                return __greycat.call("runtime::User::login", [credentials, use_cookie, ])

            @staticmethod
            def create(greycat: GreyCat, id: int, name: str, activated: bool, full_name: str, email: str, role: str, permissions_flags: int, groups: std.core.Array, groups_flags: int, external: bool) -> std.runtime.User:
                return std.runtime.User(greycat.libs_by_name[std.name_].mapped[59], [id, name, activated, full_name, email, role, permissions_flags, groups, groups_flags, external])

        @final
        class Job(Generic[__T], GreyCat.Object):
            name_: Final[str] = "runtime::Job"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def function(self) -> std.core.function:
                return self._get(self.type_.generated_offsets[0])

            def set_function(self, v: std.core.function) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def arguments(self) -> std.core.Array:
                return self._get(self.type_.generated_offsets[1])

            def set_arguments(self, v: std.core.Array) -> None:
                self._set(self.type_.generated_offsets[1], v)

            @staticmethod
            def create(greycat: GreyCat, function: std.core.function, arguments: std.core.Array) -> std.runtime.Job[TypeVar("T")]:
                return std.runtime.Job(greycat.libs_by_name[std.name_].mapped[60], [function, arguments])

        @final
        class CallPerf(GreyCat.Object):
            name_: Final[str] = "runtime::CallPerf"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def duration(self) -> std.core.duration:
                return self._get(self.type_.generated_offsets[0])

            def set_duration(self, v: std.core.duration) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def bytes_write_disk(self) -> int:
                return self._get(self.type_.generated_offsets[1])

            def set_bytes_write_disk(self, v: int) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def bytes_write_disk_raw(self) -> int:
                return self._get(self.type_.generated_offsets[2])

            def set_bytes_write_disk_raw(self, v: int) -> None:
                self._set(self.type_.generated_offsets[2], v)

            def bytes_read_disk(self) -> int:
                return self._get(self.type_.generated_offsets[3])

            def set_bytes_read_disk(self, v: int) -> None:
                self._set(self.type_.generated_offsets[3], v)

            def bytes_read_disk_raw(self) -> int:
                return self._get(self.type_.generated_offsets[4])

            def set_bytes_read_disk_raw(self, v: int) -> None:
                self._set(self.type_.generated_offsets[4], v)

            def bytes_read_cache(self) -> int:
                return self._get(self.type_.generated_offsets[5])

            def set_bytes_read_cache(self, v: int) -> None:
                self._set(self.type_.generated_offsets[5], v)

            @staticmethod
            def create(greycat: GreyCat, duration: std.core.duration, bytes_write_disk: int, bytes_write_disk_raw: int, bytes_read_disk: int, bytes_read_disk_raw: int, bytes_read_cache: int) -> std.runtime.CallPerf:
                return std.runtime.CallPerf(greycat.libs_by_name[std.name_].mapped[61], [duration, bytes_write_disk, bytes_write_disk_raw, bytes_read_disk, bytes_read_disk_raw, bytes_read_cache])

        @final
        class Debug(GreyCat.Object):
            name_: Final[str] = "runtime::Debug"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            @staticmethod
            def info(worker: int, __greycat: Optional[GreyCat] = None) -> std.runtime.DebugInfo:
                if __greycat is None:
                    __greycat  = GreyCat.DEFAULT
                return __greycat.call("runtime::Debug::info", [worker, ])

            @staticmethod
            def resume(worker: int, __greycat: Optional[GreyCat] = None) -> None:
                if __greycat is None:
                    __greycat  = GreyCat.DEFAULT
                return __greycat.call("runtime::Debug::resume", [worker, ])

            @staticmethod
            def pause(worker: int, __greycat: Optional[GreyCat] = None) -> None:
                if __greycat is None:
                    __greycat  = GreyCat.DEFAULT
                return __greycat.call("runtime::Debug::pause", [worker, ])

            @staticmethod
            def workers(__greycat: Optional[GreyCat] = None) -> std.core.Array:
                if __greycat is None:
                    __greycat  = GreyCat.DEFAULT
                return __greycat.call("runtime::Debug::workers")

            @staticmethod
            def remove(bps: std.core.Array, __greycat: Optional[GreyCat] = None) -> None:
                if __greycat is None:
                    __greycat  = GreyCat.DEFAULT
                return __greycat.call("runtime::Debug::remove", [bps, ])

            @staticmethod
            def add(bps: std.core.Array, __greycat: Optional[GreyCat] = None) -> None:
                if __greycat is None:
                    __greycat  = GreyCat.DEFAULT
                return __greycat.call("runtime::Debug::add", [bps, ])

            @staticmethod
            def create(greycat: GreyCat) -> std.runtime.Debug:
                return std.runtime.Debug(greycat.libs_by_name[std.name_].mapped[62], [])

        @final
        class DebugFrame(GreyCat.Object):
            name_: Final[str] = "runtime::DebugFrame"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def module(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_module(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def function(self) -> std.core.function:
                return self._get(self.type_.generated_offsets[1])

            def set_function(self, v: std.core.function) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def line(self) -> int:
                return self._get(self.type_.generated_offsets[2])

            def set_line(self, v: int) -> None:
                self._set(self.type_.generated_offsets[2], v)

            def column(self) -> int:
                return self._get(self.type_.generated_offsets[3])

            def set_column(self, v: int) -> None:
                self._set(self.type_.generated_offsets[3], v)

            def scope(self) -> std.core.Array:
                return self._get(self.type_.generated_offsets[4])

            def set_scope(self, v: std.core.Array) -> None:
                self._set(self.type_.generated_offsets[4], v)

            @staticmethod
            def create(greycat: GreyCat, module: str, function: std.core.function, line: int, column: int, scope: std.core.Array) -> std.runtime.DebugFrame:
                return std.runtime.DebugFrame(greycat.libs_by_name[std.name_].mapped[63], [module, function, line, column, scope])

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
            def set(tasks: std.core.Array, __greycat: Optional[GreyCat] = None) -> None:
                if __greycat is None:
                    __greycat  = GreyCat.DEFAULT
                return __greycat.call("runtime::PeriodicTask::set", [tasks, ])

            @staticmethod
            def all(__greycat: Optional[GreyCat] = None) -> std.core.Array:
                if __greycat is None:
                    __greycat  = GreyCat.DEFAULT
                return __greycat.call("runtime::PeriodicTask::all")

            @staticmethod
            def create(greycat: GreyCat, function: std.core.function, user_id: int, arguments: std.core.Array, start: std.core.time, every: std.core.duration) -> std.runtime.PeriodicTask:
                return std.runtime.PeriodicTask(greycat.libs_by_name[std.name_].mapped[64], [function, user_id, arguments, start, every])

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
            def create(greycat: GreyCat, name: str, start: std.core.time, end: std.core.time, company: str, max_memory: int, extra_1: int, extra_2: int, type: std.runtime.LicenseType) -> std.runtime.License:
                return std.runtime.License(greycat.libs_by_name[std.name_].mapped[65], [name, start, end, company, max_memory, extra_1, extra_2, type])

        @final
        class LogLevel(GreyCat.Enum):
            name_: Final[str] = "runtime::LogLevel"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def __class_getitem__(cls, key) -> std.runtime.LogLevel:
                if isinstance(key, tuple):
                    key, greycat = key
                else:
                    greycat = GreyCat._DEFAULT
                if "error" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[66]
                    return t.enum_values[t.generated_offsets[0]]
                if "warn" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[66]
                    return t.enum_values[t.generated_offsets[1]]
                if "info" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[66]
                    return t.enum_values[t.generated_offsets[2]]
                if "perf" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[66]
                    return t.enum_values[t.generated_offsets[3]]
                if "trace" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[66]
                    return t.enum_values[t.generated_offsets[4]]
                raise Error("wrong state")

            @staticmethod
            def create(greycat: GreyCat) -> std.runtime.LogLevel:
                return std.runtime.LogLevel(greycat.libs_by_name[std.name_].mapped[66], [])

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
                    __greycat  = GreyCat.DEFAULT
                return __greycat.call("runtime::OpenIDConnect::config")

            @staticmethod
            def create(greycat: GreyCat, url: str, clientId: str) -> std.runtime.OpenIDConnect:
                return std.runtime.OpenIDConnect(greycat.libs_by_name[std.name_].mapped[67], [url, clientId])

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
            def create(greycat: GreyCat, capacity_bytes: int, allocated_bytes: int, allocated_ratio: float, remained_bytes: int, remained_ratio: float, used_bytes: int, used_ratio: float, available_bytes: int, available_ratio: float) -> std.runtime.StoreStat:
                return std.runtime.StoreStat(greycat.libs_by_name[std.name_].mapped[68], [capacity_bytes, allocated_bytes, allocated_ratio, remained_bytes, remained_ratio, used_bytes, used_ratio, available_bytes, available_ratio])

        @final
        class LicenseType(GreyCat.Enum):
            name_: Final[str] = "runtime::LicenseType"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def __class_getitem__(cls, key) -> std.runtime.LicenseType:
                if isinstance(key, tuple):
                    key, greycat = key
                else:
                    greycat = GreyCat._DEFAULT
                if "community" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[69]
                    return t.enum_values[t.generated_offsets[0]]
                if "enterprise" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[69]
                    return t.enum_values[t.generated_offsets[1]]
                if "testing" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[69]
                    return t.enum_values[t.generated_offsets[2]]
                raise Error("wrong state")

            @staticmethod
            def create(greycat: GreyCat) -> std.runtime.LicenseType:
                return std.runtime.LicenseType(greycat.libs_by_name[std.name_].mapped[69], [])

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

            def start(self) -> std.core.time:
                return self._get(self.type_.generated_offsets[6])

            def set_start(self, v: std.core.time) -> None:
                self._set(self.type_.generated_offsets[6], v)

            def duration(self) -> std.core.duration:
                return self._get(self.type_.generated_offsets[7])

            def set_duration(self, v: std.core.duration) -> None:
                self._set(self.type_.generated_offsets[7], v)

            def status(self) -> std.runtime.TaskStatus:
                return self._get(self.type_.generated_offsets[8])

            def set_status(self, v: std.runtime.TaskStatus) -> None:
                self._set(self.type_.generated_offsets[8], v)

            def progress(self) -> float:
                return self._get(self.type_.generated_offsets[9])

            def set_progress(self, v: float) -> None:
                self._set(self.type_.generated_offsets[9], v)

            @staticmethod
            def is_running(task_id: int, __greycat: Optional[GreyCat] = None) -> bool:
                if __greycat is None:
                    __greycat  = GreyCat.DEFAULT
                return __greycat.call("runtime::Task::is_running", [task_id, ])

            @staticmethod
            def cancel(task_id: int, __greycat: Optional[GreyCat] = None) -> bool:
                if __greycat is None:
                    __greycat  = GreyCat.DEFAULT
                return __greycat.call("runtime::Task::cancel", [task_id, ])

            @staticmethod
            def history(offset: int, max: int, __greycat: Optional[GreyCat] = None) -> std.core.Array:
                if __greycat is None:
                    __greycat  = GreyCat.DEFAULT
                return __greycat.call("runtime::Task::history", [offset, max, ])

            @staticmethod
            def running(__greycat: Optional[GreyCat] = None) -> std.core.Array:
                if __greycat is None:
                    __greycat  = GreyCat.DEFAULT
                return __greycat.call("runtime::Task::running")

            @staticmethod
            def create(greycat: GreyCat, user_id: int, task_id: int, mod: str, type: str, fun: str, creation: std.core.time, start: std.core.time, duration: std.core.duration, status: std.runtime.TaskStatus, progress: float) -> std.runtime.Task:
                return std.runtime.Task(greycat.libs_by_name[std.name_].mapped[70], [user_id, task_id, mod, type, fun, creation, start, duration, status, progress])

        @final
        class TaskStatus(GreyCat.Enum):
            name_: Final[str] = "runtime::TaskStatus"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def __class_getitem__(cls, key) -> std.runtime.TaskStatus:
                if isinstance(key, tuple):
                    key, greycat = key
                else:
                    greycat = GreyCat._DEFAULT
                if "empty" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[71]
                    return t.enum_values[t.generated_offsets[0]]
                if "waiting" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[71]
                    return t.enum_values[t.generated_offsets[1]]
                if "running" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[71]
                    return t.enum_values[t.generated_offsets[2]]
                if "await_" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[71]
                    return t.enum_values[t.generated_offsets[3]]
                if "cancelled" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[71]
                    return t.enum_values[t.generated_offsets[4]]
                if "error" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[71]
                    return t.enum_values[t.generated_offsets[5]]
                if "ended" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[71]
                    return t.enum_values[t.generated_offsets[6]]
                if "ended_with_errors" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[71]
                    return t.enum_values[t.generated_offsets[7]]
                raise Error("wrong state")

            @staticmethod
            def create(greycat: GreyCat) -> std.runtime.TaskStatus:
                return std.runtime.TaskStatus(greycat.libs_by_name[std.name_].mapped[71], [])

    @final
    class io:
        __T = TypeVar("__T")

        @final
        class FileWalker(GreyCat.Object):
            name_: Final[str] = "io::FileWalker"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def path(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_path(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            @staticmethod
            def create(greycat: GreyCat, path: str) -> std.io.FileWalker:
                return std.io.FileWalker(greycat.libs_by_name[std.name_].mapped[72], [path])

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
            def create(greycat: GreyCat, header_lines: int, separator: c_char, string_delimiter: c_char, decimal_separator: c_char, thousands_separator: c_char, columns: std.core.Array, line_count: int, fail_count: int, file_count: int) -> std.io.CsvStatistics:
                return std.io.CsvStatistics(greycat.libs_by_name[std.name_].mapped[73], [header_lines, separator, string_delimiter, decimal_separator, thousands_separator, columns, line_count, fail_count, file_count])

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
            def create(greycat: GreyCat, name: str, example: Any, null_count: int, bool_count: int, int_count: int, float_count: int, string_count: int, date_count: int, date_format_count: std.core.Map, enumerable_count: std.core.Map, profile: std.util.Gaussian) -> std.io.CsvColumnStatistics:
                return std.io.CsvColumnStatistics(greycat.libs_by_name[std.name_].mapped[74], [name, example, null_count, bool_count, int_count, float_count, string_count, date_count, date_format_count, enumerable_count, profile])

        @final
        class Http(GreyCat.Object):
            name_: Final[str] = "io::Http"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            @staticmethod
            def create(greycat: GreyCat) -> std.io.Http:
                return std.io.Http(greycat.libs_by_name[std.name_].mapped[75], [])

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
            def create(greycat: GreyCat, name: str, value: str) -> std.io.HttpHeader:
                return std.io.HttpHeader(greycat.libs_by_name[std.name_].mapped[76], [name, value])

        @final
        class GcbWriter(Generic[__T], GreyCat.Object):
            name_: Final[str] = "io::GcbWriter"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def path(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_path(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def append(self) -> bool:
                return self._get(self.type_.generated_offsets[1])

            def set_append(self, v: bool) -> None:
                self._set(self.type_.generated_offsets[1], v)

            @staticmethod
            def create(greycat: GreyCat, path: str, append: bool) -> std.io.GcbWriter[TypeVar("T")]:
                return std.io.GcbWriter(greycat.libs_by_name[std.name_].mapped[77], [path, append])

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
            def create(greycat: GreyCat, protocol: str, host: str, port: int, path: str, params: std.core.Map, hash: str) -> std.io.Url:
                return std.io.Url(greycat.libs_by_name[std.name_].mapped[78], [protocol, host, port, path, params, hash])

        @final
        class Json(Generic[__T], GreyCat.Object):
            name_: Final[str] = "io::Json"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            @staticmethod
            def create(greycat: GreyCat) -> std.io.Json[TypeVar("T")]:
                return std.io.Json(greycat.libs_by_name[std.name_].mapped[79], [])

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
            def create(greycat: GreyCat, name: str, mandatory: bool, offset: int, trim: bool, try_number: bool, try_json: bool, values: std.core.Array, encoder: std.io.TextEncoder) -> std.io.CsvColumnString:
                return std.io.CsvColumnString(greycat.libs_by_name[std.name_].mapped[80], [name, mandatory, offset, trim, try_number, try_json, values, encoder])

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
            def create(greycat: GreyCat, name: str, mandatory: bool, offset: int, format: str, tz: std.core.TimeZone, as_time: bool) -> std.io.CsvColumnDate:
                return std.io.CsvColumnDate(greycat.libs_by_name[std.name_].mapped[81], [name, mandatory, offset, format, tz, as_time])

        @final
        class JsonWriter(Generic[__T], GreyCat.Object):
            name_: Final[str] = "io::JsonWriter"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def path(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_path(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def append(self) -> bool:
                return self._get(self.type_.generated_offsets[1])

            def set_append(self, v: bool) -> None:
                self._set(self.type_.generated_offsets[1], v)

            @staticmethod
            def create(greycat: GreyCat, path: str, append: bool) -> std.io.JsonWriter[TypeVar("T")]:
                return std.io.JsonWriter(greycat.libs_by_name[std.name_].mapped[82], [path, append])

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
            def create(greycat: GreyCat, from_: str, subject: str, body: str, body_is_html: bool, to: std.core.Array, cc: std.core.Array, bcc: std.core.Array) -> std.io.Email:
                return std.io.Email(greycat.libs_by_name[std.name_].mapped[83], [from_, subject, body, body_is_html, to, cc, bcc])

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
            def create(greycat: GreyCat, name: str, mandatory: bool, offset: int) -> std.io.CsvColumnIgnored:
                return std.io.CsvColumnIgnored(greycat.libs_by_name[std.name_].mapped[84], [name, mandatory, offset])

        @final
        class Writer(Generic[__T], GreyCat.Object):
            name_: Final[str] = "io::Writer"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def path(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_path(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def append(self) -> bool:
                return self._get(self.type_.generated_offsets[1])

            def set_append(self, v: bool) -> None:
                self._set(self.type_.generated_offsets[1], v)

            @staticmethod
            def create(greycat: GreyCat, path: str, append: bool) -> std.io.Writer[TypeVar("T")]:
                return std.io.Writer(greycat.libs_by_name[std.name_].mapped[85], [path, append])

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
            def create(greycat: GreyCat, path: str, size: int, last_modification: std.core.time) -> std.io.File:
                return std.io.File(greycat.libs_by_name[std.name_].mapped[86], [path, size, last_modification])

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
            def create(greycat: GreyCat, name: str, mandatory: bool, offset: int) -> std.io.CsvColumnFloat:
                return std.io.CsvColumnFloat(greycat.libs_by_name[std.name_].mapped[87], [name, mandatory, offset])

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
            def create(greycat: GreyCat, name: str, mandatory: bool, offset: int, unit: std.core.DurationUnit) -> std.io.CsvColumnTime:
                return std.io.CsvColumnTime(greycat.libs_by_name[std.name_].mapped[88], [name, mandatory, offset, unit])

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
            def create(greycat: GreyCat, name: str, mandatory: bool, offset: int) -> std.io.CsvColumn:
                return std.io.CsvColumn(greycat.libs_by_name[std.name_].mapped[89], [name, mandatory, offset])

        @final
        class SmtpMode(GreyCat.Enum):
            name_: Final[str] = "io::SmtpMode"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def __class_getitem__(cls, key) -> std.io.SmtpMode:
                if isinstance(key, tuple):
                    key, greycat = key
                else:
                    greycat = GreyCat._DEFAULT
                if "plain" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[90]
                    return t.enum_values[t.generated_offsets[0]]
                if "ssl_tls" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[90]
                    return t.enum_values[t.generated_offsets[1]]
                if "starttls" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[90]
                    return t.enum_values[t.generated_offsets[2]]
                raise Error("wrong state")

            @staticmethod
            def create(greycat: GreyCat) -> std.io.SmtpMode:
                return std.io.SmtpMode(greycat.libs_by_name[std.name_].mapped[90], [])

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
            def enumerable_limit_default(greycat: GreyCat) -> int:
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[91]
                return t.static_values[0]

            @staticmethod
            def date_check_limit_default(greycat: GreyCat) -> int:
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[91]
                return t.static_values[1]

            @staticmethod
            def create(greycat: GreyCat, header_lines: int, separator: c_char, string_delimiter: c_char, decimal_separator: c_char, thousands_separator: c_char, row_limit: int, enumerable_limit: int, date_check_limit: int, date_formats: std.core.Array) -> std.io.CsvAnalysisConfig:
                return std.io.CsvAnalysisConfig(greycat.libs_by_name[std.name_].mapped[91], [header_lines, separator, string_delimiter, decimal_separator, thousands_separator, row_limit, enumerable_limit, date_check_limit, date_formats])

        @final
        class JsonReader(Generic[__T], GreyCat.Object):
            name_: Final[str] = "io::JsonReader"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def path(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_path(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def pos(self) -> int:
                return self._get(self.type_.generated_offsets[1])

            def set_pos(self, v: int) -> None:
                self._set(self.type_.generated_offsets[1], v)

            @staticmethod
            def create(greycat: GreyCat, path: str, pos: int) -> std.io.JsonReader[TypeVar("T")]:
                return std.io.JsonReader(greycat.libs_by_name[std.name_].mapped[92], [path, pos])

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
            def analyze(file_path: str, config: std.io.CsvAnalysisConfig, __greycat: Optional[GreyCat] = None) -> std.io.CsvStatistics:
                if __greycat is None:
                    __greycat  = GreyCat.DEFAULT
                return __greycat.call("io::CsvAnalysis::analyze", [file_path, config, ])

            @staticmethod
            def create(greycat: GreyCat, config: std.io.CsvAnalysisConfig, statistics: std.io.CsvStatistics) -> std.io.CsvAnalysis:
                return std.io.CsvAnalysis(greycat.libs_by_name[std.name_].mapped[93], [config, statistics])

        @final
        class CsvWriter(Generic[__T], GreyCat.Object):
            name_: Final[str] = "io::CsvWriter"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def path(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_path(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def append(self) -> bool:
                return self._get(self.type_.generated_offsets[1])

            def set_append(self, v: bool) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def format(self) -> std.io.CsvFormat:
                return self._get(self.type_.generated_offsets[2])

            def set_format(self, v: std.io.CsvFormat) -> None:
                self._set(self.type_.generated_offsets[2], v)

            @staticmethod
            def create(greycat: GreyCat, path: str, append: bool, format: std.io.CsvFormat) -> std.io.CsvWriter[TypeVar("T")]:
                return std.io.CsvWriter(greycat.libs_by_name[std.name_].mapped[94], [path, append, format])

        @final
        class TextEncoder(GreyCat.Enum):
            name_: Final[str] = "io::TextEncoder"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def __class_getitem__(cls, key) -> std.io.TextEncoder:
                if isinstance(key, tuple):
                    key, greycat = key
                else:
                    greycat = GreyCat._DEFAULT
                if "plain" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[95]
                    return t.enum_values[t.generated_offsets[0]]
                if "base64" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[95]
                    return t.enum_values[t.generated_offsets[1]]
                if "base64url" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[95]
                    return t.enum_values[t.generated_offsets[2]]
                if "hexadecimal" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[95]
                    return t.enum_values[t.generated_offsets[3]]
                raise Error("wrong state")

            @staticmethod
            def create(greycat: GreyCat) -> std.io.TextEncoder:
                return std.io.TextEncoder(greycat.libs_by_name[std.name_].mapped[95], [])

        @final
        class CsvReader(Generic[__T], GreyCat.Object):
            name_: Final[str] = "io::CsvReader"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def path(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_path(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def pos(self) -> int:
                return self._get(self.type_.generated_offsets[1])

            def set_pos(self, v: int) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def format(self) -> std.io.CsvFormat:
                return self._get(self.type_.generated_offsets[2])

            def set_format(self, v: std.io.CsvFormat) -> None:
                self._set(self.type_.generated_offsets[2], v)

            def sharding(self) -> std.io.CsvSharding:
                return self._get(self.type_.generated_offsets[3])

            def set_sharding(self, v: std.io.CsvSharding) -> None:
                self._set(self.type_.generated_offsets[3], v)

            @staticmethod
            def create(greycat: GreyCat, path: str, pos: int, format: std.io.CsvFormat, sharding: std.io.CsvSharding) -> std.io.CsvReader[TypeVar("T")]:
                return std.io.CsvReader(greycat.libs_by_name[std.name_].mapped[96], [path, pos, format, sharding])

        @final
        class TextReader(GreyCat.Object):
            name_: Final[str] = "io::TextReader"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def path(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_path(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def pos(self) -> int:
                return self._get(self.type_.generated_offsets[1])

            def set_pos(self, v: int) -> None:
                self._set(self.type_.generated_offsets[1], v)

            @staticmethod
            def create(greycat: GreyCat, path: str, pos: int) -> std.io.TextReader:
                return std.io.TextReader(greycat.libs_by_name[std.name_].mapped[97], [path, pos])

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
            def create(greycat: GreyCat, name: str, mandatory: bool, offset: int) -> std.io.CsvColumnInteger:
                return std.io.CsvColumnInteger(greycat.libs_by_name[std.name_].mapped[98], [name, mandatory, offset])

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
            def create(greycat: GreyCat, name: str, mandatory: bool, offset: int) -> std.io.CsvColumnBoolean:
                return std.io.CsvColumnBoolean(greycat.libs_by_name[std.name_].mapped[99], [name, mandatory, offset])

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
            def create(greycat: GreyCat, name: str, mandatory: bool, offset: int, unit: std.core.DurationUnit) -> std.io.CsvColumnDuration:
                return std.io.CsvColumnDuration(greycat.libs_by_name[std.name_].mapped[100], [name, mandatory, offset, unit])

        @final
        class GcbReader(Generic[__T], GreyCat.Object):
            name_: Final[str] = "io::GcbReader"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def path(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_path(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def pos(self) -> int:
                return self._get(self.type_.generated_offsets[1])

            def set_pos(self, v: int) -> None:
                self._set(self.type_.generated_offsets[1], v)

            @staticmethod
            def create(greycat: GreyCat, path: str, pos: int) -> std.io.GcbReader[TypeVar("T")]:
                return std.io.GcbReader(greycat.libs_by_name[std.name_].mapped[101], [path, pos])

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
            def create(greycat: GreyCat, host: str, port: int, mode: std.io.SmtpMode, authenticate: std.io.SmtpAuth, user: str, pass_: str) -> std.io.Smtp:
                return std.io.Smtp(greycat.libs_by_name[std.name_].mapped[102], [host, port, mode, authenticate, user, pass_])

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
            def create(greycat: GreyCat, line_count: int, fail_count: int, invalid_count: std.core.Array) -> std.io.CsvValidateResult:
                return std.io.CsvValidateResult(greycat.libs_by_name[std.name_].mapped[103], [line_count, fail_count, invalid_count])

        @final
        class Reader(Generic[__T], GreyCat.Object):
            name_: Final[str] = "io::Reader"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def path(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_path(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def pos(self) -> int:
                return self._get(self.type_.generated_offsets[1])

            def set_pos(self, v: int) -> None:
                self._set(self.type_.generated_offsets[1], v)

            @staticmethod
            def create(greycat: GreyCat, path: str, pos: int) -> std.io.Reader[TypeVar("T")]:
                return std.io.Reader(greycat.libs_by_name[std.name_].mapped[104], [path, pos])

        @final
        class TextWriter(Generic[__T], GreyCat.Object):
            name_: Final[str] = "io::TextWriter"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def path(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_path(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def append(self) -> bool:
                return self._get(self.type_.generated_offsets[1])

            def set_append(self, v: bool) -> None:
                self._set(self.type_.generated_offsets[1], v)

            @staticmethod
            def create(greycat: GreyCat, path: str, append: bool) -> std.io.TextWriter[TypeVar("T")]:
                return std.io.TextWriter(greycat.libs_by_name[std.name_].mapped[105], [path, append])

        @final
        class SmtpAuth(GreyCat.Enum):
            name_: Final[str] = "io::SmtpAuth"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def __class_getitem__(cls, key) -> std.io.SmtpAuth:
                if isinstance(key, tuple):
                    key, greycat = key
                else:
                    greycat = GreyCat._DEFAULT
                if "none" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[106]
                    return t.enum_values[t.generated_offsets[0]]
                if "plain" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[106]
                    return t.enum_values[t.generated_offsets[1]]
                if "login" == key:
                    t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[106]
                    return t.enum_values[t.generated_offsets[2]]
                raise Error("wrong state")

            @staticmethod
            def create(greycat: GreyCat) -> std.io.SmtpAuth:
                return std.io.SmtpAuth(greycat.libs_by_name[std.name_].mapped[106], [])

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
            def infer(analysis: std.io.CsvStatistics, __greycat: Optional[GreyCat] = None) -> std.io.CsvFormat:
                if __greycat is None:
                    __greycat  = GreyCat.DEFAULT
                return __greycat.call("io::CsvFormat::infer", [analysis, ])

            @staticmethod
            def sample(path: str, format: std.io.CsvFormat, offset: int, max: int, __greycat: Optional[GreyCat] = None) -> std.core.Table:
                if __greycat is None:
                    __greycat  = GreyCat.DEFAULT
                return __greycat.call("io::CsvFormat::sample", [path, format, offset, max, ])

            @staticmethod
            def validate(path: str, format: std.io.CsvFormat, max_rows: int, max_invalid: int, invalid_path: str, __greycat: Optional[GreyCat] = None) -> std.io.CsvValidateResult:
                if __greycat is None:
                    __greycat  = GreyCat.DEFAULT
                return __greycat.call("io::CsvFormat::validate", [path, format, max_rows, max_invalid, invalid_path, ])

            @staticmethod
            def generate(format: std.io.CsvFormat, ident_col: int, time_col: int, __greycat: Optional[GreyCat] = None) -> str:
                if __greycat is None:
                    __greycat  = GreyCat.DEFAULT
                return __greycat.call("io::CsvFormat::generate", [format, ident_col, time_col, ])

            @staticmethod
            def create(greycat: GreyCat, header_lines: int, separator: c_char, string_delimiter: c_char, decimal_separator: c_char, thousands_separator: c_char, columns_size: int, columns: std.core.Array) -> std.io.CsvFormat:
                return std.io.CsvFormat(greycat.libs_by_name[std.name_].mapped[107], [header_lines, separator, string_delimiter, decimal_separator, thousands_separator, columns_size, columns])

        @final
        class CsvSharding(GreyCat.Object):
            name_: Final[str] = "io::CsvSharding"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def id(self) -> int:
                return self._get(self.type_.generated_offsets[0])

            def set_id(self, v: int) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def column(self) -> int:
                return self._get(self.type_.generated_offsets[1])

            def set_column(self, v: int) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def modulo(self) -> int:
                return self._get(self.type_.generated_offsets[2])

            def set_modulo(self, v: int) -> None:
                self._set(self.type_.generated_offsets[2], v)

            @staticmethod
            def create(greycat: GreyCat, id: int, column: int, modulo: int) -> std.io.CsvSharding:
                return std.io.CsvSharding(greycat.libs_by_name[std.name_].mapped[108], [id, column, modulo])

    @final
    class util:
        __T = TypeVar("__T")

        @final
        class Quantizer(Generic[__T], GreyCat.Object):
            name_: Final[str] = "util::Quantizer"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            @staticmethod
            def create(greycat: GreyCat) -> std.util.Quantizer[TypeVar("T")]:
                return std.util.Quantizer(greycat.libs_by_name[std.name_].mapped[109], [])

        @final
        class LogQuantizer(Generic[__T], GreyCat.Object):
            name_: Final[str] = "util::LogQuantizer"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def min(self) -> std.util.__:
                return self._get(self.type_.generated_offsets[0])

            def set_min(self, v: std.util.__) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def max(self) -> std.util.__:
                return self._get(self.type_.generated_offsets[1])

            def set_max(self, v: std.util.__) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def bins(self) -> int:
                return self._get(self.type_.generated_offsets[2])

            def set_bins(self, v: int) -> None:
                self._set(self.type_.generated_offsets[2], v)

            def open(self) -> bool:
                return self._get(self.type_.generated_offsets[3])

            def set_open(self, v: bool) -> None:
                self._set(self.type_.generated_offsets[3], v)

            @staticmethod
            def create(greycat: GreyCat, min: std.util.__, max: std.util.__, bins: int, open: bool) -> std.util.LogQuantizer[TypeVar("T")]:
                return std.util.LogQuantizer(greycat.libs_by_name[std.name_].mapped[110], [min, max, bins, open])

        @final
        class LinearQuantizer(Generic[__T], GreyCat.Object):
            name_: Final[str] = "util::LinearQuantizer"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def min(self) -> std.util.__:
                return self._get(self.type_.generated_offsets[0])

            def set_min(self, v: std.util.__) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def max(self) -> std.util.__:
                return self._get(self.type_.generated_offsets[1])

            def set_max(self, v: std.util.__) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def bins(self) -> int:
                return self._get(self.type_.generated_offsets[2])

            def set_bins(self, v: int) -> None:
                self._set(self.type_.generated_offsets[2], v)

            def open(self) -> bool:
                return self._get(self.type_.generated_offsets[3])

            def set_open(self, v: bool) -> None:
                self._set(self.type_.generated_offsets[3], v)

            @staticmethod
            def create(greycat: GreyCat, min: std.util.__, max: std.util.__, bins: int, open: bool) -> std.util.LinearQuantizer[TypeVar("T")]:
                return std.util.LinearQuantizer(greycat.libs_by_name[std.name_].mapped[111], [min, max, bins, open])

        @final
        class GaussianProfileSlot(GreyCat.Object):
            name_: Final[str] = "util::GaussianProfileSlot"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def sum(self) -> int:
                return self._get(self.type_.generated_offsets[0])

            def set_sum(self, v: int) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def sumsq(self) -> int:
                return self._get(self.type_.generated_offsets[1])

            def set_sumsq(self, v: int) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def count(self) -> int:
                return self._get(self.type_.generated_offsets[2])

            def set_count(self, v: int) -> None:
                self._set(self.type_.generated_offsets[2], v)

            @staticmethod
            def create(greycat: GreyCat, sum: int, sumsq: int, count: int) -> std.util.GaussianProfileSlot:
                return std.util.GaussianProfileSlot(greycat.libs_by_name[std.name_].mapped[112], [sum, sumsq, count])

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
            def create(greycat: GreyCat, start: std.core.time, total: int, counter: int, duration: std.core.duration, progress: float, speed: float, remaining: std.core.duration) -> std.util.ProgressTracker:
                return std.util.ProgressTracker(greycat.libs_by_name[std.name_].mapped[113], [start, total, counter, duration, progress, speed, remaining])

        @final
        class HistogramStats(GreyCat.Object):
            name_: Final[str] = "util::HistogramStats"

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

            def whisker_low(self) -> float:
                return self._get(self.type_.generated_offsets[2])

            def set_whisker_low(self, v: float) -> None:
                self._set(self.type_.generated_offsets[2], v)

            def whisker_high(self) -> float:
                return self._get(self.type_.generated_offsets[3])

            def set_whisker_high(self, v: float) -> None:
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

            def count_outliers_low(self) -> int:
                return self._get(self.type_.generated_offsets[11])

            def set_count_outliers_low(self, v: int) -> None:
                self._set(self.type_.generated_offsets[11], v)

            def count_outliers_high(self) -> int:
                return self._get(self.type_.generated_offsets[12])

            def set_count_outliers_high(self, v: int) -> None:
                self._set(self.type_.generated_offsets[12], v)

            def percentage_outliers_low(self) -> float:
                return self._get(self.type_.generated_offsets[13])

            def set_percentage_outliers_low(self, v: float) -> None:
                self._set(self.type_.generated_offsets[13], v)

            def percentage_outliers_high(self) -> float:
                return self._get(self.type_.generated_offsets[14])

            def set_percentage_outliers_high(self, v: float) -> None:
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
            def create(greycat: GreyCat, min: float, max: float, whisker_low: float, whisker_high: float, percentile1: float, percentile5: float, percentile25: float, percentile50: float, percentile75: float, percentile95: float, percentile99: float, count_outliers_low: int, count_outliers_high: int, percentage_outliers_low: float, percentage_outliers_high: float, sum: float, avg: float, std: float, size: int) -> std.util.HistogramStats:
                return std.util.HistogramStats(greycat.libs_by_name[std.name_].mapped[114], [min, max, whisker_low, whisker_high, percentile1, percentile5, percentile25, percentile50, percentile75, percentile95, percentile99, count_outliers_low, count_outliers_high, percentage_outliers_low, percentage_outliers_high, sum, avg, std, size])

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
            def create(greycat: GreyCat, seed: int, v: float) -> std.util.Random:
                return std.util.Random(greycat.libs_by_name[std.name_].mapped[115], [seed, v])

        @final
        class MultiQuantizer(Generic[__T], GreyCat.Object):
            name_: Final[str] = "util::MultiQuantizer"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def quantizers(self) -> std.core.Array:
                return self._get(self.type_.generated_offsets[0])

            def set_quantizers(self, v: std.core.Array) -> None:
                self._set(self.type_.generated_offsets[0], v)

            @staticmethod
            def create(greycat: GreyCat, quantizers: std.core.Array) -> std.util.MultiQuantizer[TypeVar("T")]:
                return std.util.MultiQuantizer(greycat.libs_by_name[std.name_].mapped[116], [quantizers])

        @final
        class Crypto(GreyCat.Object):
            name_: Final[str] = "util::Crypto"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            @staticmethod
            def create(greycat: GreyCat) -> std.util.Crypto:
                return std.util.Crypto(greycat.libs_by_name[std.name_].mapped[117], [])

        @final
        class QuantizerSlotBound(Generic[__T], GreyCat.Object):
            name_: Final[str] = "util::QuantizerSlotBound"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def min(self) -> std.util.__:
                return self._get(self.type_.generated_offsets[0])

            def set_min(self, v: std.util.__) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def max(self) -> std.util.__:
                return self._get(self.type_.generated_offsets[1])

            def set_max(self, v: std.util.__) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def center(self) -> std.util.__:
                return self._get(self.type_.generated_offsets[2])

            def set_center(self, v: std.util.__) -> None:
                self._set(self.type_.generated_offsets[2], v)

            @staticmethod
            def create(greycat: GreyCat, min: std.util.__, max: std.util.__, center: std.util.__) -> std.util.QuantizerSlotBound[TypeVar("T")]:
                return std.util.QuantizerSlotBound(greycat.libs_by_name[std.name_].mapped[118], [min, max, center])

        @final
        class Gaussian(GreyCat.Object):
            name_: Final[str] = "util::Gaussian"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def sum(self) -> float:
                return self._get(self.type_.generated_offsets[0])

            def set_sum(self, v: float) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def sumsq(self) -> float:
                return self._get(self.type_.generated_offsets[1])

            def set_sumsq(self, v: float) -> None:
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
            def create(greycat: GreyCat, sum: float, sumsq: float, count: int, min: float, max: float) -> std.util.Gaussian:
                return std.util.Gaussian(greycat.libs_by_name[std.name_].mapped[119], [sum, sumsq, count, min, max])

        @final
        class Stack(Generic[__T], GreyCat.Object):
            name_: Final[str] = "util::Stack"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def values(self) -> std.core.Array:
                return self._get(self.type_.generated_offsets[0])

            def set_values(self, v: std.core.Array) -> None:
                self._set(self.type_.generated_offsets[0], v)

            @staticmethod
            def create(greycat: GreyCat, values: std.core.Array) -> std.util.Stack[TypeVar("T")]:
                return std.util.Stack(greycat.libs_by_name[std.name_].mapped[120], [values])

        @final
        class Histogram(Generic[__T], GreyCat.Object):
            name_: Final[str] = "util::Histogram"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def quantizer(self) -> std.util.Quantizer:
                return self._get(self.type_.generated_offsets[0])

            def set_quantizer(self, v: std.util.Quantizer) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def bins(self) -> std.core.Array:
                return self._get(self.type_.generated_offsets[1])

            def set_bins(self, v: std.core.Array) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def nb_rejected(self) -> int:
                return self._get(self.type_.generated_offsets[2])

            def set_nb_rejected(self, v: int) -> None:
                self._set(self.type_.generated_offsets[2], v)

            def nb_accepted(self) -> int:
                return self._get(self.type_.generated_offsets[3])

            def set_nb_accepted(self, v: int) -> None:
                self._set(self.type_.generated_offsets[3], v)

            @staticmethod
            def create(greycat: GreyCat, quantizer: std.util.Quantizer, bins: std.core.Array, nb_rejected: int, nb_accepted: int) -> std.util.Histogram[TypeVar("T")]:
                return std.util.Histogram(greycat.libs_by_name[std.name_].mapped[121], [quantizer, bins, nb_rejected, nb_accepted])

        @final
        class SlidingWindow(Generic[__T], GreyCat.Object):
            name_: Final[str] = "util::SlidingWindow"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def values(self) -> std.core.Array:
                return self._get(self.type_.generated_offsets[0])

            def set_values(self, v: std.core.Array) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def span(self) -> int:
                return self._get(self.type_.generated_offsets[1])

            def set_span(self, v: int) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def sum(self) -> float:
                return self._get(self.type_.generated_offsets[2])

            def set_sum(self, v: float) -> None:
                self._set(self.type_.generated_offsets[2], v)

            def sumsq(self) -> float:
                return self._get(self.type_.generated_offsets[3])

            def set_sumsq(self, v: float) -> None:
                self._set(self.type_.generated_offsets[3], v)

            def field(self) -> std.core.field:
                return self._get(self.type_.generated_offsets[4])

            def set_field(self, v: std.core.field) -> None:
                self._set(self.type_.generated_offsets[4], v)

            @staticmethod
            def create(greycat: GreyCat, values: std.core.Array, span: int, sum: float, sumsq: float, field: std.core.field) -> std.util.SlidingWindow[TypeVar("T")]:
                return std.util.SlidingWindow(greycat.libs_by_name[std.name_].mapped[122], [values, span, sum, sumsq, field])

        @final
        class CustomQuantizer(Generic[__T], GreyCat.Object):
            name_: Final[str] = "util::CustomQuantizer"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def min(self) -> std.util.__:
                return self._get(self.type_.generated_offsets[0])

            def set_min(self, v: std.util.__) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def max(self) -> std.util.__:
                return self._get(self.type_.generated_offsets[1])

            def set_max(self, v: std.util.__) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def step_starts(self) -> std.core.Array:
                return self._get(self.type_.generated_offsets[2])

            def set_step_starts(self, v: std.core.Array) -> None:
                self._set(self.type_.generated_offsets[2], v)

            def open(self) -> bool:
                return self._get(self.type_.generated_offsets[3])

            def set_open(self, v: bool) -> None:
                self._set(self.type_.generated_offsets[3], v)

            @staticmethod
            def create(greycat: GreyCat, min: std.util.__, max: std.util.__, step_starts: std.core.Array, open: bool) -> std.util.CustomQuantizer[TypeVar("T")]:
                return std.util.CustomQuantizer(greycat.libs_by_name[std.name_].mapped[123], [min, max, step_starts, open])

        @final
        class Assert(GreyCat.Object):
            name_: Final[str] = "util::Assert"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            @staticmethod
            def create(greycat: GreyCat) -> std.util.Assert:
                return std.util.Assert(greycat.libs_by_name[std.name_].mapped[124], [])

        @final
        class Queue(Generic[__T], GreyCat.Object):
            name_: Final[str] = "util::Queue"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def values(self) -> std.core.Array:
                return self._get(self.type_.generated_offsets[0])

            def set_values(self, v: std.core.Array) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def capacity(self) -> int:
                return self._get(self.type_.generated_offsets[1])

            def set_capacity(self, v: int) -> None:
                self._set(self.type_.generated_offsets[1], v)

            @staticmethod
            def create(greycat: GreyCat, values: std.core.Array, capacity: int) -> std.util.Queue[TypeVar("T")]:
                return std.util.Queue(greycat.libs_by_name[std.name_].mapped[125], [values, capacity])

        @final
        class GaussianProfile(Generic[__T], GreyCat.Object):
            name_: Final[str] = "util::GaussianProfile"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def quantizer(self) -> std.util.Quantizer:
                return self._get(self.type_.generated_offsets[0])

            def set_quantizer(self, v: std.util.Quantizer) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def precision(self) -> std.core.FloatPrecision:
                return self._get(self.type_.generated_offsets[1])

            def set_precision(self, v: std.core.FloatPrecision) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def bins(self) -> std.core.Table:
                return self._get(self.type_.generated_offsets[2])

            def set_bins(self, v: std.core.Table) -> None:
                self._set(self.type_.generated_offsets[2], v)

            def value_min(self) -> float:
                return self._get(self.type_.generated_offsets[3])

            def set_value_min(self, v: float) -> None:
                self._set(self.type_.generated_offsets[3], v)

            def nb_rejected(self) -> int:
                return self._get(self.type_.generated_offsets[4])

            def set_nb_rejected(self, v: int) -> None:
                self._set(self.type_.generated_offsets[4], v)

            @staticmethod
            def create(greycat: GreyCat, quantizer: std.util.Quantizer, precision: std.core.FloatPrecision, bins: std.core.Table, value_min: float, nb_rejected: int) -> std.util.GaussianProfile[TypeVar("T")]:
                return std.util.GaussianProfile(greycat.libs_by_name[std.name_].mapped[126], [quantizer, precision, bins, value_min, nb_rejected])

        @final
        class TimeWindow(Generic[__T], GreyCat.Object):
            name_: Final[str] = "util::TimeWindow"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def values(self) -> std.core.Table:
                return self._get(self.type_.generated_offsets[0])

            def set_values(self, v: std.core.Table) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def span(self) -> std.core.duration:
                return self._get(self.type_.generated_offsets[1])

            def set_span(self, v: std.core.duration) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def sum(self) -> float:
                return self._get(self.type_.generated_offsets[2])

            def set_sum(self, v: float) -> None:
                self._set(self.type_.generated_offsets[2], v)

            def sumsq(self) -> float:
                return self._get(self.type_.generated_offsets[3])

            def set_sumsq(self, v: float) -> None:
                self._set(self.type_.generated_offsets[3], v)

            def field(self) -> std.core.field:
                return self._get(self.type_.generated_offsets[4])

            def set_field(self, v: std.core.field) -> None:
                self._set(self.type_.generated_offsets[4], v)

            @staticmethod
            def create(greycat: GreyCat, values: std.core.Table, span: std.core.duration, sum: float, sumsq: float, field: std.core.field) -> std.util.TimeWindow[TypeVar("T")]:
                return std.util.TimeWindow(greycat.libs_by_name[std.name_].mapped[127], [values, span, sum, sumsq, field])

        @final
        class Plot(GreyCat.Object):
            name_: Final[str] = "util::Plot"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            @staticmethod
            def create(greycat: GreyCat) -> std.util.Plot:
                return std.util.Plot(greycat.libs_by_name[std.name_].mapped[128], [])

    def configure(self, loaders: dict[str, GreyCat.Loader], factories: dict[str, GreyCat.Factory]) -> None:
        factories[std.core.t4.name_] = lambda type, attributes: std.core.t4(type, attributes)
        loaders[std.core.t4.name_] = lambda type, stream: std_n.core._t4.load(type, stream)
        factories[std.core.Date.name_] = lambda type, attributes: std.core.Date(type, attributes)
        factories[std.core.nodeTimeCursor.name_] = lambda type, attributes: std.core.nodeTimeCursor(type, attributes)
        factories[std.core.TimeZone.name_] = lambda type, attributes: std.core.TimeZone(type, attributes)
        factories[std.core.t3.name_] = lambda type, attributes: std.core.t3(type, attributes)
        loaders[std.core.t3.name_] = lambda type, stream: std_n.core._t3.load(type, stream)
        factories[std.core.SortOrder.name_] = lambda type, attributes: std.core.SortOrder(type, attributes)
        factories[std.core.FloatPrecision.name_] = lambda type, attributes: std.core.FloatPrecision(type, attributes)
        factories[std.core.t2.name_] = lambda type, attributes: std.core.t2(type, attributes)
        loaders[std.core.t2.name_] = lambda type, stream: std_n.core._t2.load(type, stream)
        factories[std.core.t4f.name_] = lambda type, attributes: std.core.t4f(type, attributes)
        loaders[std.core.t4f.name_] = lambda type, stream: std_n.core._t4f.load(type, stream)
        factories[std.core.Array.name_] = lambda type, attributes: std.core.Array(type, attributes)
        loaders[std.core.Array.name_] = lambda type, stream: std_n.core._Array.load(type, stream)
        factories[std.core.Tuple.name_] = lambda type, attributes: std.core.Tuple(type, attributes)
        factories[std.core.Map.name_] = lambda type, attributes: std.core.Map(type, attributes)
        loaders[std.core.Map.name_] = lambda type, stream: std_n.core._Map.load(type, stream)
        factories[std.core.String.name_] = lambda type, attributes: std.core.String(type, attributes)
        loaders[std.core.String.name_] = lambda type, stream: std_n.core._String.load(type, stream)
        factories[std.core.field.name_] = lambda type, attributes: std.core.field(type, attributes)
        loaders[std.core.field.name_] = lambda type, stream: std_n.core._field.load(type, stream)
        factories[std.core.Tensor.name_] = lambda type, attributes: std.core.Tensor(type, attributes)
        loaders[std.core.Tensor.name_] = lambda type, stream: std_n.core._Tensor.load(type, stream)
        factories[std.core.NodeInfo.name_] = lambda type, attributes: std.core.NodeInfo(type, attributes)
        factories[std.core.MathConstants.name_] = lambda type, attributes: std.core.MathConstants(type, attributes)
        factories[std.core.t3f.name_] = lambda type, attributes: std.core.t3f(type, attributes)
        loaders[std.core.t3f.name_] = lambda type, stream: std_n.core._t3f.load(type, stream)
        factories[std.core.type.name_] = lambda type, attributes: std.core.type(type, attributes)
        loaders[std.core.type.name_] = lambda type, stream: std_n.core._type.load(type, stream)
        factories[std.core.Table.name_] = lambda type, attributes: std.core.Table(type, attributes)
        loaders[std.core.Table.name_] = lambda type, stream: std_n.core._Table.load(type, stream)
        factories[std.core.nodeIndex.name_] = lambda type, attributes: std.core.nodeIndex(type, attributes)
        loaders[std.core.nodeIndex.name_] = lambda type, stream: std_n.core._nodeIndex.load(type, stream)
        factories[std.core.Buffer.name_] = lambda type, attributes: std.core.Buffer(type, attributes)
        loaders[std.core.Buffer.name_] = lambda type, stream: std_n.core._Buffer.load(type, stream)
        factories[std.core.GeoBox.name_] = lambda type, attributes: std.core.GeoBox(type, attributes)
        factories[std.core.DurationUnit.name_] = lambda type, attributes: std.core.DurationUnit(type, attributes)
        factories[std.core.nodeTime.name_] = lambda type, attributes: std.core.nodeTime(type, attributes)
        loaders[std.core.nodeTime.name_] = lambda type, stream: std_n.core._nodeTime.load(type, stream)
        factories[std.core.nodeTimeSingleton.name_] = lambda type, attributes: std.core.nodeTimeSingleton(type, attributes)
        factories[std.core.nodeList.name_] = lambda type, attributes: std.core.nodeList(type, attributes)
        loaders[std.core.nodeList.name_] = lambda type, stream: std_n.core._nodeList.load(type, stream)
        factories[std.core.GeoCircle.name_] = lambda type, attributes: std.core.GeoCircle(type, attributes)
        factories[std.core.GeoPoly.name_] = lambda type, attributes: std.core.GeoPoly(type, attributes)
        factories[std.core.Error.name_] = lambda type, attributes: std.core.Error(type, attributes)
        factories[std.core.ErrorFrame.name_] = lambda type, attributes: std.core.ErrorFrame(type, attributes)
        factories[std.core.duration.name_] = lambda type, attributes: std.core.duration(type, attributes)
        loaders[std.core.duration.name_] = lambda type, stream: std_n.core._duration.load(type, stream)
        factories[std.core.geo.name_] = lambda type, attributes: std.core.geo(type, attributes)
        loaders[std.core.geo.name_] = lambda type, stream: std_n.core._geo.load(type, stream)
        factories[std.core.function.name_] = lambda type, attributes: std.core.function(type, attributes)
        loaders[std.core.function.name_] = lambda type, stream: std_n.core._function.load(type, stream)
        factories[std.core.TableColumnMapping.name_] = lambda type, attributes: std.core.TableColumnMapping(type, attributes)
        factories[std.core.time.name_] = lambda type, attributes: std.core.time(type, attributes)
        loaders[std.core.time.name_] = lambda type, stream: std_n.core._time.load(type, stream)
        factories[std.core.t2f.name_] = lambda type, attributes: std.core.t2f(type, attributes)
        loaders[std.core.t2f.name_] = lambda type, stream: std_n.core._t2f.load(type, stream)
        factories[std.core.TensorType.name_] = lambda type, attributes: std.core.TensorType(type, attributes)
        factories[std.core.SamplingMode.name_] = lambda type, attributes: std.core.SamplingMode(type, attributes)
        factories[std.core.CalendarUnit.name_] = lambda type, attributes: std.core.CalendarUnit(type, attributes)
        factories[std.core.node.name_] = lambda type, attributes: std.core.node(type, attributes)
        loaders[std.core.node.name_] = lambda type, stream: std_n.core._node.load(type, stream)
        factories[std.core.str.name_] = lambda type, attributes: std.core.str(type, attributes)
        loaders[std.core.str.name_] = lambda type, stream: std_n.core._str.load(type, stream)
        factories[std.core.nodeGeo.name_] = lambda type, attributes: std.core.nodeGeo(type, attributes)
        loaders[std.core.nodeGeo.name_] = lambda type, stream: std_n.core._nodeGeo.load(type, stream)
        factories[std.core.ErrorCode.name_] = lambda type, attributes: std.core.ErrorCode(type, attributes)
        factories[std.runtime.SecurityFields.name_] = lambda type, attributes: std.runtime.SecurityFields(type, attributes)
        factories[std.runtime.DebugVariable.name_] = lambda type, attributes: std.runtime.DebugVariable(type, attributes)
        factories[std.runtime.RuntimeInfo.name_] = lambda type, attributes: std.runtime.RuntimeInfo(type, attributes)
        factories[std.runtime.UserGroupPolicyType.name_] = lambda type, attributes: std.runtime.UserGroupPolicyType(type, attributes)
        factories[std.runtime.UserCredential.name_] = lambda type, attributes: std.runtime.UserCredential(type, attributes)
        factories[std.runtime.UserGroup.name_] = lambda type, attributes: std.runtime.UserGroup(type, attributes)
        factories[std.runtime.DebugInfo.name_] = lambda type, attributes: std.runtime.DebugInfo(type, attributes)
        factories[std.runtime.SecurityPolicy.name_] = lambda type, attributes: std.runtime.SecurityPolicy(type, attributes)
        factories[std.runtime.DebugBreakpoint.name_] = lambda type, attributes: std.runtime.DebugBreakpoint(type, attributes)
        factories[std.runtime.SecurityEntity.name_] = lambda type, attributes: std.runtime.SecurityEntity(type, attributes)
        factories[std.runtime.Log.name_] = lambda type, attributes: std.runtime.Log(type, attributes)
        factories[std.runtime.System.name_] = lambda type, attributes: std.runtime.System(type, attributes)
        factories[std.runtime.Runtime.name_] = lambda type, attributes: std.runtime.Runtime(type, attributes)
        factories[std.runtime.UserRole.name_] = lambda type, attributes: std.runtime.UserRole(type, attributes)
        factories[std.runtime.UserGroupPolicy.name_] = lambda type, attributes: std.runtime.UserGroupPolicy(type, attributes)
        factories[std.runtime.User.name_] = lambda type, attributes: std.runtime.User(type, attributes)
        factories[std.runtime.Job.name_] = lambda type, attributes: std.runtime.Job(type, attributes)
        factories[std.runtime.CallPerf.name_] = lambda type, attributes: std.runtime.CallPerf(type, attributes)
        factories[std.runtime.Debug.name_] = lambda type, attributes: std.runtime.Debug(type, attributes)
        factories[std.runtime.DebugFrame.name_] = lambda type, attributes: std.runtime.DebugFrame(type, attributes)
        factories[std.runtime.PeriodicTask.name_] = lambda type, attributes: std.runtime.PeriodicTask(type, attributes)
        factories[std.runtime.License.name_] = lambda type, attributes: std.runtime.License(type, attributes)
        factories[std.runtime.LogLevel.name_] = lambda type, attributes: std.runtime.LogLevel(type, attributes)
        factories[std.runtime.OpenIDConnect.name_] = lambda type, attributes: std.runtime.OpenIDConnect(type, attributes)
        factories[std.runtime.StoreStat.name_] = lambda type, attributes: std.runtime.StoreStat(type, attributes)
        factories[std.runtime.LicenseType.name_] = lambda type, attributes: std.runtime.LicenseType(type, attributes)
        factories[std.runtime.Task.name_] = lambda type, attributes: std.runtime.Task(type, attributes)
        factories[std.runtime.TaskStatus.name_] = lambda type, attributes: std.runtime.TaskStatus(type, attributes)
        factories[std.io.FileWalker.name_] = lambda type, attributes: std.io.FileWalker(type, attributes)
        factories[std.io.CsvStatistics.name_] = lambda type, attributes: std.io.CsvStatistics(type, attributes)
        factories[std.io.CsvColumnStatistics.name_] = lambda type, attributes: std.io.CsvColumnStatistics(type, attributes)
        factories[std.io.Http.name_] = lambda type, attributes: std.io.Http(type, attributes)
        factories[std.io.HttpHeader.name_] = lambda type, attributes: std.io.HttpHeader(type, attributes)
        factories[std.io.GcbWriter.name_] = lambda type, attributes: std.io.GcbWriter(type, attributes)
        factories[std.io.Url.name_] = lambda type, attributes: std.io.Url(type, attributes)
        factories[std.io.Json.name_] = lambda type, attributes: std.io.Json(type, attributes)
        factories[std.io.CsvColumnString.name_] = lambda type, attributes: std.io.CsvColumnString(type, attributes)
        factories[std.io.CsvColumnDate.name_] = lambda type, attributes: std.io.CsvColumnDate(type, attributes)
        factories[std.io.JsonWriter.name_] = lambda type, attributes: std.io.JsonWriter(type, attributes)
        factories[std.io.Email.name_] = lambda type, attributes: std.io.Email(type, attributes)
        factories[std.io.CsvColumnIgnored.name_] = lambda type, attributes: std.io.CsvColumnIgnored(type, attributes)
        factories[std.io.Writer.name_] = lambda type, attributes: std.io.Writer(type, attributes)
        factories[std.io.File.name_] = lambda type, attributes: std.io.File(type, attributes)
        factories[std.io.CsvColumnFloat.name_] = lambda type, attributes: std.io.CsvColumnFloat(type, attributes)
        factories[std.io.CsvColumnTime.name_] = lambda type, attributes: std.io.CsvColumnTime(type, attributes)
        factories[std.io.CsvColumn.name_] = lambda type, attributes: std.io.CsvColumn(type, attributes)
        factories[std.io.SmtpMode.name_] = lambda type, attributes: std.io.SmtpMode(type, attributes)
        factories[std.io.CsvAnalysisConfig.name_] = lambda type, attributes: std.io.CsvAnalysisConfig(type, attributes)
        factories[std.io.JsonReader.name_] = lambda type, attributes: std.io.JsonReader(type, attributes)
        factories[std.io.CsvAnalysis.name_] = lambda type, attributes: std.io.CsvAnalysis(type, attributes)
        factories[std.io.CsvWriter.name_] = lambda type, attributes: std.io.CsvWriter(type, attributes)
        factories[std.io.TextEncoder.name_] = lambda type, attributes: std.io.TextEncoder(type, attributes)
        factories[std.io.CsvReader.name_] = lambda type, attributes: std.io.CsvReader(type, attributes)
        factories[std.io.TextReader.name_] = lambda type, attributes: std.io.TextReader(type, attributes)
        factories[std.io.CsvColumnInteger.name_] = lambda type, attributes: std.io.CsvColumnInteger(type, attributes)
        factories[std.io.CsvColumnBoolean.name_] = lambda type, attributes: std.io.CsvColumnBoolean(type, attributes)
        factories[std.io.CsvColumnDuration.name_] = lambda type, attributes: std.io.CsvColumnDuration(type, attributes)
        factories[std.io.GcbReader.name_] = lambda type, attributes: std.io.GcbReader(type, attributes)
        factories[std.io.Smtp.name_] = lambda type, attributes: std.io.Smtp(type, attributes)
        factories[std.io.CsvValidateResult.name_] = lambda type, attributes: std.io.CsvValidateResult(type, attributes)
        factories[std.io.Reader.name_] = lambda type, attributes: std.io.Reader(type, attributes)
        factories[std.io.TextWriter.name_] = lambda type, attributes: std.io.TextWriter(type, attributes)
        factories[std.io.SmtpAuth.name_] = lambda type, attributes: std.io.SmtpAuth(type, attributes)
        factories[std.io.CsvFormat.name_] = lambda type, attributes: std.io.CsvFormat(type, attributes)
        factories[std.io.CsvSharding.name_] = lambda type, attributes: std.io.CsvSharding(type, attributes)
        factories[std.util.Quantizer.name_] = lambda type, attributes: std.util.Quantizer(type, attributes)
        factories[std.util.LogQuantizer.name_] = lambda type, attributes: std.util.LogQuantizer(type, attributes)
        factories[std.util.LinearQuantizer.name_] = lambda type, attributes: std.util.LinearQuantizer(type, attributes)
        factories[std.util.GaussianProfileSlot.name_] = lambda type, attributes: std.util.GaussianProfileSlot(type, attributes)
        factories[std.util.ProgressTracker.name_] = lambda type, attributes: std.util.ProgressTracker(type, attributes)
        factories[std.util.HistogramStats.name_] = lambda type, attributes: std.util.HistogramStats(type, attributes)
        factories[std.util.Random.name_] = lambda type, attributes: std.util.Random(type, attributes)
        factories[std.util.MultiQuantizer.name_] = lambda type, attributes: std.util.MultiQuantizer(type, attributes)
        factories[std.util.Crypto.name_] = lambda type, attributes: std.util.Crypto(type, attributes)
        factories[std.util.QuantizerSlotBound.name_] = lambda type, attributes: std.util.QuantizerSlotBound(type, attributes)
        factories[std.util.Gaussian.name_] = lambda type, attributes: std.util.Gaussian(type, attributes)
        factories[std.util.Stack.name_] = lambda type, attributes: std.util.Stack(type, attributes)
        factories[std.util.Histogram.name_] = lambda type, attributes: std.util.Histogram(type, attributes)
        factories[std.util.SlidingWindow.name_] = lambda type, attributes: std.util.SlidingWindow(type, attributes)
        factories[std.util.CustomQuantizer.name_] = lambda type, attributes: std.util.CustomQuantizer(type, attributes)
        factories[std.util.Assert.name_] = lambda type, attributes: std.util.Assert(type, attributes)
        factories[std.util.Queue.name_] = lambda type, attributes: std.util.Queue(type, attributes)
        factories[std.util.GaussianProfile.name_] = lambda type, attributes: std.util.GaussianProfile(type, attributes)
        factories[std.util.TimeWindow.name_] = lambda type, attributes: std.util.TimeWindow(type, attributes)
        factories[std.util.Plot.name_] = lambda type, attributes: std.util.Plot(type, attributes)

    def init(self, greycat: GreyCat) -> None:
        self.mapped: list[GreyCat.Type] = [
            greycat.types_by_name[std.core.t4.name_],
            greycat.types_by_name[std.core.Date.name_],
            greycat.types_by_name[std.core.nodeTimeCursor.name_],
            greycat.types_by_name[std.core.TimeZone.name_],
            greycat.types_by_name[std.core.t3.name_],
            greycat.types_by_name[std.core.SortOrder.name_],
            greycat.types_by_name[std.core.FloatPrecision.name_],
            greycat.types_by_name[std.core.t2.name_],
            greycat.types_by_name[std.core.t4f.name_],
            greycat.types_by_name[std.core.Array.name_],
            greycat.types_by_name[std.core.Tuple.name_],
            greycat.types_by_name[std.core.Map.name_],
            greycat.types_by_name[std.core.String.name_],
            greycat.types_by_name[std.core.field.name_],
            greycat.types_by_name[std.core.Tensor.name_],
            greycat.types_by_name[std.core.NodeInfo.name_],
            greycat.types_by_name[std.core.MathConstants.name_],
            greycat.types_by_name[std.core.t3f.name_],
            greycat.types_by_name[std.core.type.name_],
            greycat.types_by_name[std.core.Table.name_],
            greycat.types_by_name[std.core.nodeIndex.name_],
            greycat.types_by_name[std.core.Buffer.name_],
            greycat.types_by_name[std.core.GeoBox.name_],
            greycat.types_by_name[std.core.DurationUnit.name_],
            greycat.types_by_name[std.core.nodeTime.name_],
            greycat.types_by_name[std.core.nodeTimeSingleton.name_],
            greycat.types_by_name[std.core.nodeList.name_],
            greycat.types_by_name[std.core.GeoCircle.name_],
            greycat.types_by_name[std.core.GeoPoly.name_],
            greycat.types_by_name[std.core.Error.name_],
            greycat.types_by_name[std.core.ErrorFrame.name_],
            greycat.types_by_name[std.core.duration.name_],
            greycat.types_by_name[std.core.geo.name_],
            greycat.types_by_name[std.core.function.name_],
            greycat.types_by_name[std.core.TableColumnMapping.name_],
            greycat.types_by_name[std.core.time.name_],
            greycat.types_by_name[std.core.t2f.name_],
            greycat.types_by_name[std.core.TensorType.name_],
            greycat.types_by_name[std.core.SamplingMode.name_],
            greycat.types_by_name[std.core.CalendarUnit.name_],
            greycat.types_by_name[std.core.node.name_],
            greycat.types_by_name[std.core.str.name_],
            greycat.types_by_name[std.core.nodeGeo.name_],
            greycat.types_by_name[std.core.ErrorCode.name_],
            greycat.types_by_name[std.runtime.SecurityFields.name_],
            greycat.types_by_name[std.runtime.DebugVariable.name_],
            greycat.types_by_name[std.runtime.RuntimeInfo.name_],
            greycat.types_by_name[std.runtime.UserGroupPolicyType.name_],
            greycat.types_by_name[std.runtime.UserCredential.name_],
            greycat.types_by_name[std.runtime.UserGroup.name_],
            greycat.types_by_name[std.runtime.DebugInfo.name_],
            greycat.types_by_name[std.runtime.SecurityPolicy.name_],
            greycat.types_by_name[std.runtime.DebugBreakpoint.name_],
            greycat.types_by_name[std.runtime.SecurityEntity.name_],
            greycat.types_by_name[std.runtime.Log.name_],
            greycat.types_by_name[std.runtime.System.name_],
            greycat.types_by_name[std.runtime.Runtime.name_],
            greycat.types_by_name[std.runtime.UserRole.name_],
            greycat.types_by_name[std.runtime.UserGroupPolicy.name_],
            greycat.types_by_name[std.runtime.User.name_],
            greycat.types_by_name[std.runtime.Job.name_],
            greycat.types_by_name[std.runtime.CallPerf.name_],
            greycat.types_by_name[std.runtime.Debug.name_],
            greycat.types_by_name[std.runtime.DebugFrame.name_],
            greycat.types_by_name[std.runtime.PeriodicTask.name_],
            greycat.types_by_name[std.runtime.License.name_],
            greycat.types_by_name[std.runtime.LogLevel.name_],
            greycat.types_by_name[std.runtime.OpenIDConnect.name_],
            greycat.types_by_name[std.runtime.StoreStat.name_],
            greycat.types_by_name[std.runtime.LicenseType.name_],
            greycat.types_by_name[std.runtime.Task.name_],
            greycat.types_by_name[std.runtime.TaskStatus.name_],
            greycat.types_by_name[std.io.FileWalker.name_],
            greycat.types_by_name[std.io.CsvStatistics.name_],
            greycat.types_by_name[std.io.CsvColumnStatistics.name_],
            greycat.types_by_name[std.io.Http.name_],
            greycat.types_by_name[std.io.HttpHeader.name_],
            greycat.types_by_name[std.io.GcbWriter.name_],
            greycat.types_by_name[std.io.Url.name_],
            greycat.types_by_name[std.io.Json.name_],
            greycat.types_by_name[std.io.CsvColumnString.name_],
            greycat.types_by_name[std.io.CsvColumnDate.name_],
            greycat.types_by_name[std.io.JsonWriter.name_],
            greycat.types_by_name[std.io.Email.name_],
            greycat.types_by_name[std.io.CsvColumnIgnored.name_],
            greycat.types_by_name[std.io.Writer.name_],
            greycat.types_by_name[std.io.File.name_],
            greycat.types_by_name[std.io.CsvColumnFloat.name_],
            greycat.types_by_name[std.io.CsvColumnTime.name_],
            greycat.types_by_name[std.io.CsvColumn.name_],
            greycat.types_by_name[std.io.SmtpMode.name_],
            greycat.types_by_name[std.io.CsvAnalysisConfig.name_],
            greycat.types_by_name[std.io.JsonReader.name_],
            greycat.types_by_name[std.io.CsvAnalysis.name_],
            greycat.types_by_name[std.io.CsvWriter.name_],
            greycat.types_by_name[std.io.TextEncoder.name_],
            greycat.types_by_name[std.io.CsvReader.name_],
            greycat.types_by_name[std.io.TextReader.name_],
            greycat.types_by_name[std.io.CsvColumnInteger.name_],
            greycat.types_by_name[std.io.CsvColumnBoolean.name_],
            greycat.types_by_name[std.io.CsvColumnDuration.name_],
            greycat.types_by_name[std.io.GcbReader.name_],
            greycat.types_by_name[std.io.Smtp.name_],
            greycat.types_by_name[std.io.CsvValidateResult.name_],
            greycat.types_by_name[std.io.Reader.name_],
            greycat.types_by_name[std.io.TextWriter.name_],
            greycat.types_by_name[std.io.SmtpAuth.name_],
            greycat.types_by_name[std.io.CsvFormat.name_],
            greycat.types_by_name[std.io.CsvSharding.name_],
            greycat.types_by_name[std.util.Quantizer.name_],
            greycat.types_by_name[std.util.LogQuantizer.name_],
            greycat.types_by_name[std.util.LinearQuantizer.name_],
            greycat.types_by_name[std.util.GaussianProfileSlot.name_],
            greycat.types_by_name[std.util.ProgressTracker.name_],
            greycat.types_by_name[std.util.HistogramStats.name_],
            greycat.types_by_name[std.util.Random.name_],
            greycat.types_by_name[std.util.MultiQuantizer.name_],
            greycat.types_by_name[std.util.Crypto.name_],
            greycat.types_by_name[std.util.QuantizerSlotBound.name_],
            greycat.types_by_name[std.util.Gaussian.name_],
            greycat.types_by_name[std.util.Stack.name_],
            greycat.types_by_name[std.util.Histogram.name_],
            greycat.types_by_name[std.util.SlidingWindow.name_],
            greycat.types_by_name[std.util.CustomQuantizer.name_],
            greycat.types_by_name[std.util.Assert.name_],
            greycat.types_by_name[std.util.Queue.name_],
            greycat.types_by_name[std.util.GaussianProfile.name_],
            greycat.types_by_name[std.util.TimeWindow.name_],
            greycat.types_by_name[std.util.Plot.name_],
        ]
        self.mapped[1].resolve_generated_offsets("refs", "from", "maxRows", "mode")
        self.mapped[3].resolve_generated_offsets("year", "month", "day", "hour", "minute", "second", "microsecond")
        self.mapped[4].resolve_generated_offsets("n", "req_time")
        self.mapped[5].resolve_generated_offset_with_values("Africa/Abidjan", None, "Africa/Accra", None, "Africa/Addis_Ababa", None, "Africa/Algiers", None, "Africa/Asmara", None, "Africa/Asmera", None, "Africa/Bamako", None, "Africa/Bangui", None, "Africa/Banjul", None, "Africa/Bissau", None, "Africa/Blantyre", None, "Africa/Brazzaville", None, "Africa/Bujumbura", None, "Africa/Cairo", None, "Africa/Casablanca", None, "Africa/Ceuta", None, "Africa/Conakry", None, "Africa/Dakar", None, "Africa/Dar_es_Salaam", None, "Africa/Djibouti", None, "Africa/Douala", None, "Africa/El_Aaiun", None, "Africa/Freetown", None, "Africa/Gaborone", None, "Africa/Harare", None, "Africa/Johannesburg", None, "Africa/Juba", None, "Africa/Kampala", None, "Africa/Khartoum", None, "Africa/Kigali", None, "Africa/Kinshasa", None, "Africa/Lagos", None, "Africa/Libreville", None, "Africa/Lome", None, "Africa/Luanda", None, "Africa/Lubumbashi", None, "Africa/Lusaka", None, "Africa/Malabo", None, "Africa/Maputo", None, "Africa/Maseru", None, "Africa/Mbabane", None, "Africa/Mogadishu", None, "Africa/Monrovia", None, "Africa/Nairobi", None, "Africa/Ndjamena", None, "Africa/Niamey", None, "Africa/Nouakchott", None, "Africa/Ouagadougou", None, "Africa/Porto-Novo", None, "Africa/Sao_Tome", None, "Africa/Timbuktu", None, "Africa/Tripoli", None, "Africa/Tunis", None, "Africa/Windhoek", None, "America/Adak", None, "America/Anchorage", None, "America/Anguilla", None, "America/Antigua", None, "America/Araguaina", None, "America/Argentina/Buenos_Aires", None, "America/Argentina/Catamarca", None, "America/Argentina/ComodRivadavia", None, "America/Argentina/Cordoba", None, "America/Argentina/Jujuy", None, "America/Argentina/La_Rioja", None, "America/Argentina/Mendoza", None, "America/Argentina/Rio_Gallegos", None, "America/Argentina/Salta", None, "America/Argentina/San_Juan", None, "America/Argentina/San_Luis", None, "America/Argentina/Tucuman", None, "America/Argentina/Ushuaia", None, "America/Aruba", None, "America/Asuncion", None, "America/Atikokan", None, "America/Atka", None, "America/Bahia", None, "America/Bahia_Banderas", None, "America/Barbados", None, "America/Belem", None, "America/Belize", None, "America/Blanc-Sablon", None, "America/Boa_Vista", None, "America/Bogota", None, "America/Boise", None, "America/Buenos_Aires", None, "America/Cambridge_Bay", None, "America/Campo_Grande", None, "America/Cancun", None, "America/Caracas", None, "America/Catamarca", None, "America/Cayenne", None, "America/Cayman", None, "America/Chicago", None, "America/Chihuahua", None, "America/Ciudad_Juarez", None, "America/Coral_Harbour", None, "America/Cordoba", None, "America/Costa_Rica", None, "America/Creston", None, "America/Cuiaba", None, "America/Curacao", None, "America/Danmarkshavn", None, "America/Dawson", None, "America/Dawson_Creek", None, "America/Denver", None, "America/Detroit", None, "America/Dominica", None, "America/Edmonton", None, "America/Eirunepe", None, "America/El_Salvador", None, "America/Ensenada", None, "America/Fort_Nelson", None, "America/Fort_Wayne", None, "America/Fortaleza", None, "America/Glace_Bay", None, "America/Godthab", None, "America/Goose_Bay", None, "America/Grand_Turk", None, "America/Grenada", None, "America/Guadeloupe", None, "America/Guatemala", None, "America/Guayaquil", None, "America/Guyana", None, "America/Halifax", None, "America/Havana", None, "America/Hermosillo", None, "America/Indiana/Indianapolis", None, "America/Indiana/Knox", None, "America/Indiana/Marengo", None, "America/Indiana/Petersburg", None, "America/Indiana/Tell_City", None, "America/Indiana/Vevay", None, "America/Indiana/Vincennes", None, "America/Indiana/Winamac", None, "America/Indianapolis", None, "America/Inuvik", None, "America/Iqaluit", None, "America/Jamaica", None, "America/Jujuy", None, "America/Juneau", None, "America/Kentucky/Louisville", None, "America/Kentucky/Monticello", None, "America/Knox_IN", None, "America/Kralendijk", None, "America/La_Paz", None, "America/Lima", None, "America/Los_Angeles", None, "America/Louisville", None, "America/Lower_Princes", None, "America/Maceio", None, "America/Managua", None, "America/Manaus", None, "America/Marigot", None, "America/Martinique", None, "America/Matamoros", None, "America/Mazatlan", None, "America/Mendoza", None, "America/Menominee", None, "America/Merida", None, "America/Metlakatla", None, "America/Mexico_City", None, "America/Miquelon", None, "America/Moncton", None, "America/Monterrey", None, "America/Montevideo", None, "America/Montreal", None, "America/Montserrat", None, "America/Nassau", None, "America/New_York", None, "America/Nipigon", None, "America/Nome", None, "America/Noronha", None, "America/North_Dakota/Beulah", None, "America/North_Dakota/Center", None, "America/North_Dakota/New_Salem", None, "America/Nuuk", None, "America/Ojinaga", None, "America/Panama", None, "America/Pangnirtung", None, "America/Paramaribo", None, "America/Phoenix", None, "America/Port-au-Prince", None, "America/Port_of_Spain", None, "America/Porto_Acre", None, "America/Porto_Velho", None, "America/Puerto_Rico", None, "America/Punta_Arenas", None, "America/Rainy_River", None, "America/Rankin_Inlet", None, "America/Recife", None, "America/Regina", None, "America/Resolute", None, "America/Rio_Branco", None, "America/Rosario", None, "America/Santa_Isabel", None, "America/Santarem", None, "America/Santiago", None, "America/Santo_Domingo", None, "America/Sao_Paulo", None, "America/Scoresbysund", None, "America/Shiprock", None, "America/Sitka", None, "America/St_Barthelemy", None, "America/St_Johns", None, "America/St_Kitts", None, "America/St_Lucia", None, "America/St_Thomas", None, "America/St_Vincent", None, "America/Swift_Current", None, "America/Tegucigalpa", None, "America/Thule", None, "America/Thunder_Bay", None, "America/Tijuana", None, "America/Toronto", None, "America/Tortola", None, "America/Vancouver", None, "America/Virgin", None, "America/Whitehorse", None, "America/Winnipeg", None, "America/Yakutat", None, "America/Yellowknife", None, "Antarctica/Casey", None, "Antarctica/Davis", None, "Antarctica/DumontDUrville", None, "Antarctica/Macquarie", None, "Antarctica/Mawson", None, "Antarctica/McMurdo", None, "Antarctica/Palmer", None, "Antarctica/Rothera", None, "Antarctica/South_Pole", None, "Antarctica/Syowa", None, "Antarctica/Troll", None, "Antarctica/Vostok", None, "Arctic/Longyearbyen", None, "Asia/Aden", None, "Asia/Almaty", None, "Asia/Amman", None, "Asia/Anadyr", None, "Asia/Aqtau", None, "Asia/Aqtobe", None, "Asia/Ashgabat", None, "Asia/Ashkhabad", None, "Asia/Atyrau", None, "Asia/Baghdad", None, "Asia/Bahrain", None, "Asia/Baku", None, "Asia/Bangkok", None, "Asia/Barnaul", None, "Asia/Beirut", None, "Asia/Bishkek", None, "Asia/Brunei", None, "Asia/Calcutta", None, "Asia/Chita", None, "Asia/Choibalsan", None, "Asia/Chongqing", None, "Asia/Chungking", None, "Asia/Colombo", None, "Asia/Dacca", None, "Asia/Damascus", None, "Asia/Dhaka", None, "Asia/Dili", None, "Asia/Dubai", None, "Asia/Dushanbe", None, "Asia/Famagusta", None, "Asia/Gaza", None, "Asia/Harbin", None, "Asia/Hebron", None, "Asia/Ho_Chi_Minh", None, "Asia/Hong_Kong", None, "Asia/Hovd", None, "Asia/Irkutsk", None, "Asia/Istanbul", None, "Asia/Jakarta", None, "Asia/Jayapura", None, "Asia/Jerusalem", None, "Asia/Kabul", None, "Asia/Kamchatka", None, "Asia/Karachi", None, "Asia/Kashgar", None, "Asia/Kathmandu", None, "Asia/Katmandu", None, "Asia/Khandyga", None, "Asia/Kolkata", None, "Asia/Krasnoyarsk", None, "Asia/Kuala_Lumpur", None, "Asia/Kuching", None, "Asia/Kuwait", None, "Asia/Macao", None, "Asia/Macau", None, "Asia/Magadan", None, "Asia/Makassar", None, "Asia/Manila", None, "Asia/Muscat", None, "Asia/Nicosia", None, "Asia/Novokuznetsk", None, "Asia/Novosibirsk", None, "Asia/Omsk", None, "Asia/Oral", None, "Asia/Phnom_Penh", None, "Asia/Pontianak", None, "Asia/Pyongyang", None, "Asia/Qatar", None, "Asia/Qostanay", None, "Asia/Qyzylorda", None, "Asia/Rangoon", None, "Asia/Riyadh", None, "Asia/Saigon", None, "Asia/Sakhalin", None, "Asia/Samarkand", None, "Asia/Seoul", None, "Asia/Shanghai", None, "Asia/Singapore", None, "Asia/Srednekolymsk", None, "Asia/Taipei", None, "Asia/Tashkent", None, "Asia/Tbilisi", None, "Asia/Tehran", None, "Asia/Tel_Aviv", None, "Asia/Thimbu", None, "Asia/Thimphu", None, "Asia/Tokyo", None, "Asia/Tomsk", None, "Asia/Ujung_Pandang", None, "Asia/Ulaanbaatar", None, "Asia/Ulan_Bator", None, "Asia/Urumqi", None, "Asia/Ust-Nera", None, "Asia/Vientiane", None, "Asia/Vladivostok", None, "Asia/Yakutsk", None, "Asia/Yangon", None, "Asia/Yekaterinburg", None, "Asia/Yerevan", None, "Atlantic/Azores", None, "Atlantic/Bermuda", None, "Atlantic/Canary", None, "Atlantic/Cape_Verde", None, "Atlantic/Faeroe", None, "Atlantic/Faroe", None, "Atlantic/Jan_Mayen", None, "Atlantic/Madeira", None, "Atlantic/Reykjavik", None, "Atlantic/South_Georgia", None, "Atlantic/St_Helena", None, "Atlantic/Stanley", None, "Australia/ACT", None, "Australia/Adelaide", None, "Australia/Brisbane", None, "Australia/Broken_Hill", None, "Australia/Canberra", None, "Australia/Currie", None, "Australia/Darwin", None, "Australia/Eucla", None, "Australia/Hobart", None, "Australia/LHI", None, "Australia/Lindeman", None, "Australia/Lord_Howe", None, "Australia/Melbourne", None, "Australia/NSW", None, "Australia/North", None, "Australia/Perth", None, "Australia/Queensland", None, "Australia/South", None, "Australia/Sydney", None, "Australia/Tasmania", None, "Australia/Victoria", None, "Australia/West", None, "Australia/Yancowinna", None, "Brazil/Acre", None, "Brazil/DeNoronha", None, "Brazil/East", None, "Brazil/West", None, "CET", None, "CST6CDT", None, "Canada/Atlantic", None, "Canada/Central", None, "Canada/Eastern", None, "Canada/Mountain", None, "Canada/Newfoundland", None, "Canada/Pacific", None, "Canada/Saskatchewan", None, "Canada/Yukon", None, "Chile/Continental", None, "Chile/EasterIsland", None, "Cuba", None, "EET", None, "EST", None, "EST5EDT", None, "Egypt", None, "Eire", None, "Etc/GMT", None, "Etc/GMT+0", None, "Etc/GMT+1", None, "Etc/GMT+10", None, "Etc/GMT+11", None, "Etc/GMT+12", None, "Etc/GMT+2", None, "Etc/GMT+3", None, "Etc/GMT+4", None, "Etc/GMT+5", None, "Etc/GMT+6", None, "Etc/GMT+7", None, "Etc/GMT+8", None, "Etc/GMT+9", None, "Etc/GMT-0", None, "Etc/GMT-1", None, "Etc/GMT-10", None, "Etc/GMT-11", None, "Etc/GMT-12", None, "Etc/GMT-13", None, "Etc/GMT-14", None, "Etc/GMT-2", None, "Etc/GMT-3", None, "Etc/GMT-4", None, "Etc/GMT-5", None, "Etc/GMT-6", None, "Etc/GMT-7", None, "Etc/GMT-8", None, "Etc/GMT-9", None, "Etc/GMT0", None, "Etc/Greenwich", None, "Etc/UCT", None, "Etc/UTC", None, "Etc/Universal", None, "Etc/Zulu", None, "Europe/Amsterdam", None, "Europe/Andorra", None, "Europe/Astrakhan", None, "Europe/Athens", None, "Europe/Belfast", None, "Europe/Belgrade", None, "Europe/Berlin", None, "Europe/Bratislava", None, "Europe/Brussels", None, "Europe/Bucharest", None, "Europe/Budapest", None, "Europe/Busingen", None, "Europe/Chisinau", None, "Europe/Copenhagen", None, "Europe/Dublin", None, "Europe/Gibraltar", None, "Europe/Guernsey", None, "Europe/Helsinki", None, "Europe/Isle_of_Man", None, "Europe/Istanbul", None, "Europe/Jersey", None, "Europe/Kaliningrad", None, "Europe/Kiev", None, "Europe/Kirov", None, "Europe/Kyiv", None, "Europe/Lisbon", None, "Europe/Ljubljana", None, "Europe/London", None, "Europe/Luxembourg", None, "Europe/Madrid", None, "Europe/Malta", None, "Europe/Mariehamn", None, "Europe/Minsk", None, "Europe/Monaco", None, "Europe/Moscow", None, "Europe/Nicosia", None, "Europe/Oslo", None, "Europe/Paris", None, "Europe/Podgorica", None, "Europe/Prague", None, "Europe/Riga", None, "Europe/Rome", None, "Europe/Samara", None, "Europe/San_Marino", None, "Europe/Sarajevo", None, "Europe/Saratov", None, "Europe/Simferopol", None, "Europe/Skopje", None, "Europe/Sofia", None, "Europe/Stockholm", None, "Europe/Tallinn", None, "Europe/Tirane", None, "Europe/Tiraspol", None, "Europe/Ulyanovsk", None, "Europe/Uzhgorod", None, "Europe/Vaduz", None, "Europe/Vatican", None, "Europe/Vienna", None, "Europe/Vilnius", None, "Europe/Volgograd", None, "Europe/Warsaw", None, "Europe/Zagreb", None, "Europe/Zaporozhye", None, "Europe/Zurich", None, "Factory", None, "GB", None, "GB-Eire", None, "GMT", None, "GMT+0", None, "GMT-0", None, "GMT0", None, "Greenwich", None, "HST", None, "Hongkong", None, "Iceland", None, "Indian/Antananarivo", None, "Indian/Chagos", None, "Indian/Christmas", None, "Indian/Cocos", None, "Indian/Comoro", None, "Indian/Kerguelen", None, "Indian/Mahe", None, "Indian/Maldives", None, "Indian/Mauritius", None, "Indian/Mayotte", None, "Indian/Reunion", None, "Iran", None, "Israel", None, "Jamaica", None, "Japan", None, "Kwajalein", None, "Libya", None, "MET", None, "MST", None, "MST7MDT", None, "Mexico/BajaNorte", None, "Mexico/BajaSur", None, "Mexico/General", None, "NZ", None, "NZ-CHAT", None, "Navajo", None, "PRC", None, "PST8PDT", None, "Pacific/Apia", None, "Pacific/Auckland", None, "Pacific/Bougainville", None, "Pacific/Chatham", None, "Pacific/Chuuk", None, "Pacific/Easter", None, "Pacific/Efate", None, "Pacific/Enderbury", None, "Pacific/Fakaofo", None, "Pacific/Fiji", None, "Pacific/Funafuti", None, "Pacific/Galapagos", None, "Pacific/Gambier", None, "Pacific/Guadalcanal", None, "Pacific/Guam", None, "Pacific/Honolulu", None, "Pacific/Johnston", None, "Pacific/Kanton", None, "Pacific/Kiritimati", None, "Pacific/Kosrae", None, "Pacific/Kwajalein", None, "Pacific/Majuro", None, "Pacific/Marquesas", None, "Pacific/Midway", None, "Pacific/Nauru", None, "Pacific/Niue", None, "Pacific/Norfolk", None, "Pacific/Noumea", None, "Pacific/Pago_Pago", None, "Pacific/Palau", None, "Pacific/Pitcairn", None, "Pacific/Pohnpei", None, "Pacific/Ponape", None, "Pacific/Port_Moresby", None, "Pacific/Rarotonga", None, "Pacific/Saipan", None, "Pacific/Samoa", None, "Pacific/Tahiti", None, "Pacific/Tarawa", None, "Pacific/Tongatapu", None, "Pacific/Truk", None, "Pacific/Wake", None, "Pacific/Wallis", None, "Pacific/Yap", None, "Poland", None, "Portugal", None, "ROC", None, "ROK", None, "Singapore", None, "Turkey", None, "UCT", None, "US/Alaska", None, "US/Aleutian", None, "US/Arizona", None, "US/Central", None, "US/East-Indiana", None, "US/Eastern", None, "US/Hawaii", None, "US/Indiana-Starke", None, "US/Michigan", None, "US/Mountain", None, "US/Pacific", None, "US/Samoa", None, "UTC", None, "Universal", None, "W-SU", None, "WET", None, "Zulu", None)
        self.mapped[8].resolve_generated_offset_with_values("asc", None, "desc", None)
        self.mapped[9].resolve_generated_offsets("x", "y")
        self.mapped[10].resolve_generated_offset_with_values("p1", float.fromhex("0x1p+0"), "p10", float.fromhex("0x1.999999999999ap-4"), "p100", float.fromhex("0x1.47ae147ae147bp-7"), "p1000", float.fromhex("0x1.0624dd2f1a9fcp-10"), "p10000", float.fromhex("0x1.a36e2eb1c432dp-14"), "p100000", float.fromhex("0x1.4f8b588e368f1p-17"), "p1000000", float.fromhex("0x1.0c6f7a0b5ed8dp-20"), "p10000000", float.fromhex("0x1.ad7f29abcaf48p-24"), "p100000000", float.fromhex("0x1.5798ee2308c3ap-27"), "p1000000000", float.fromhex("0x1.12e0be826d695p-30"), "p10000000000", float.fromhex("0x1.b7cdfd9d7bdbbp-34"))
        self.mapped[11].resolve_generated_offsets("nodes")
        self.mapped[15].resolve_generated_offsets("nodes")
        self.mapped[16].resolve_generated_offsets("table", "mappings")
        self.mapped[20].resolve_generated_offsets("refs", "from", "to", "maxRows", "mode", "maxDephasing")
        self.mapped[22].resolve_generated_offsets("nodes")
        self.mapped[26].resolve_generated_offsets("refs", "from", "to", "maxRows", "mode", "maxDephasing", "tz")
        self.mapped[29].resolve_generated_offsets("x", "y")
        self.mapped[43].resolve_generated_offsets("refs", "from", "to", "maxRows", "mode")
        self.mapped[44].resolve_generated_offsets("nodes")
        self.mapped[45].resolve_generated_offsets("size", "from", "to")
        self.mapped[47].resolve_generated_offsets("x", "y")
        self.mapped[50].static_values = [float.fromhex("0x1.5bf0a8b145769p+1"), float.fromhex("0x1.71547652b82fep+0"), float.fromhex("0x1.bcb7b1526e50ep-2"), float.fromhex("0x1.62e42fefa39efp-1"), float.fromhex("0x1.26bb1bbb55516p+1"), float.fromhex("0x1.921fb54442d18p+1"), float.fromhex("0x1.921fb54442d18p+0"), float.fromhex("0x1.921fb54442d18p-1"), float.fromhex("0x1.45f306dc9c883p-2"), float.fromhex("0x1.45f306dc9c883p-1"), float.fromhex("0x1.20dd750429b6dp+0"), float.fromhex("0x1.6a09e667f3bcdp+0"), float.fromhex("0x1.6a09e667f3bcdp-1")]
        self.mapped[65].resolve_generated_offsets("sw", "ne")
        self.mapped[66].resolve_generated_offsets("time", "tz")
        self.mapped[71].resolve_generated_offset_with_values("microseconds", 1, "milliseconds", 1000, "seconds", 1000000, "minutes", 60000000, "hours", 3600000000, "days", 86400000000)
        self.mapped[74].resolve_generated_offsets("t", "v")
        self.mapped[78].resolve_generated_offsets("center", "radius")
        self.mapped[80].resolve_generated_offsets("points")
        self.mapped[81].resolve_generated_offsets("message", "stack")
        self.mapped[83].resolve_generated_offsets("n")
        self.mapped[86].resolve_generated_offsets("module", "function", "line", "column")
        self.mapped[88].resolve_generated_offsets("size", "from", "to")
        self.mapped[89].static_values = [greycat.create_geo(float.fromhex("-0x1.54345b1903bbap+6"), float.fromhex("-0x1.67fffffe98p+7")), greycat.create_geo(float.fromhex("0x1.54345b1903bbap+6"), float.fromhex("0x1.67fffffe98p+7"))]
        self.mapped[91].resolve_generated_offsets("size", "from", "to")
        self.mapped[92].resolve_generated_offsets("size", "from", "to")
        self.mapped[96].resolve_generated_offsets("column", "extractors")
        self.mapped[97].static_values = [greycat.create_time(-9223372036854775808), greycat.create_time(9223372036854775807)]
        self.mapped[100].resolve_generated_offset_with_values("i32", 4, "i64", 8, "f32", 4, "f64", 8, "c64", 8, "c128", 16)
        self.mapped[102].resolve_generated_offset_with_values("fixed", 0, "fixed_reg", 1, "adaptative", 2, "dense", 3)
        self.mapped[105].resolve_generated_offset_with_values("year", 0, "month", 1, "day", 2, "hour", 3, "minute", 4, "second", 5, "microsecond", 6)
        self.mapped[112].resolve_generated_offsets("x", "y")
        self.mapped[113].resolve_generated_offset_with_values("none", 0, "interrupted", 1, "await", 2, "timeout", 6, "forbidden", 7, "runtime_error", 8)
        self.mapped[115].resolve_generated_offsets("email", "name", "first_name", "last_name", "roles", "groups")
        self.mapped[116].resolve_generated_offsets("name", "value")
        self.mapped[117].resolve_generated_offsets("version", "program_version", "arch", "timezone", "license", "io_threads", "bg_threads", "fg_threads", "mem_total", "mem_worker", "nb_ctx", "store_stats")
        self.mapped[118].resolve_generated_offsets("id")
        self.mapped[120].resolve_generated_offsets("token", "use_cookie")
        self.mapped[121].resolve_generated_offset_with_values("read", 0, "write", 1, "execute", 2)
        self.mapped[122].resolve_generated_offsets("offset", "pass")
        self.mapped[123].resolve_generated_offsets("id", "name", "activated")
        self.mapped[124].resolve_generated_offsets("scopes", "root")
        self.mapped[126].resolve_generated_offsets("entities", "credentials", "roles", "fields", "keys", "keys_last_refresh")
        self.mapped[127].resolve_generated_offsets("name", "pass")
        self.mapped[129].resolve_generated_offsets("module", "line", "column")
        self.mapped[130].resolve_generated_offsets("id", "name", "activated")
        self.mapped[131].resolve_generated_offsets("level", "time", "user_id", "id", "id2", "src", "tag", "data")
        self.mapped[132].resolve_generated_offsets("entity")
        self.mapped[137].resolve_generated_offsets("name", "permissions")
        self.mapped[138].resolve_generated_offsets("value")
        self.mapped[140].resolve_generated_offsets("group_id", "type")
        self.mapped[141].resolve_generated_offsets("worker")
        self.mapped[143].resolve_generated_offsets("worker")
        self.mapped[145].resolve_generated_offsets("credentials", "use_cookie")
        self.mapped[146].resolve_generated_offsets("id", "name", "activated", "full_name", "email", "role", "permissions_flags", "groups", "groups_flags", "external")
        self.mapped[147].resolve_generated_offsets("worker")
        self.mapped[148].resolve_generated_offsets("bps")
        self.mapped[151].resolve_generated_offsets("function", "arguments")
        self.mapped[154].resolve_generated_offsets("duration", "bytes_write_disk", "bytes_write_disk_raw", "bytes_read_disk", "bytes_read_disk_raw", "bytes_read_cache")
        self.mapped[157].resolve_generated_offsets("module", "function", "line", "column", "scope")
        self.mapped[158].resolve_generated_offsets("function", "user_id", "arguments", "start", "every")
        self.mapped[159].resolve_generated_offsets("task_id")
        self.mapped[160].resolve_generated_offsets("f")
        self.mapped[161].resolve_generated_offsets("name", "start", "end", "company", "max_memory", "extra_1", "extra_2", "type")
        self.mapped[162].resolve_generated_offset_with_values("error", None, "warn", None, "info", None, "perf", None, "trace", None)
        self.mapped[164].resolve_generated_offsets("bps")
        self.mapped[165].resolve_generated_offsets("name")
        self.mapped[166].resolve_generated_offsets("url", "clientId")
        self.mapped[167].resolve_generated_offsets("capacity_bytes", "allocated_bytes", "allocated_ratio", "remained_bytes", "remained_ratio", "used_bytes", "used_ratio", "available_bytes", "available_ratio")
        self.mapped[168].resolve_generated_offset_with_values("community", 0, "enterprise", 1, "testing", 2)
        self.mapped[169].resolve_generated_offsets("use_cookie")
        self.mapped[170].resolve_generated_offsets("offset", "max")
        self.mapped[172].resolve_generated_offsets("task_id")
        self.mapped[173].resolve_generated_offsets("user_id", "task_id", "mod", "type", "fun", "creation", "start", "duration", "status", "progress")
        self.mapped[174].resolve_generated_offsets("tasks")
        self.mapped[175].resolve_generated_offset_with_values("empty", 0, "waiting", 1, "running", 2, "await", 3, "cancelled", 4, "error", 5, "ended", 6, "ended_with_errors", 7)
        self.mapped[176].resolve_generated_offsets("path")
        self.mapped[177].resolve_generated_offsets("header_lines", "separator", "string_delimiter", "decimal_separator", "thousands_separator", "columns", "line_count", "fail_count", "file_count")
        self.mapped[178].resolve_generated_offsets("name", "example", "null_count", "bool_count", "int_count", "float_count", "string_count", "date_count", "date_format_count", "enumerable_count", "profile")
        self.mapped[180].resolve_generated_offsets("name", "value")
        self.mapped[181].resolve_generated_offsets("path", "append")
        self.mapped[182].resolve_generated_offsets("protocol", "host", "port", "path", "params", "hash")
        self.mapped[184].resolve_generated_offsets("name", "mandatory", "offset", "trim", "try_number", "try_json", "values", "encoder")
        self.mapped[185].resolve_generated_offsets("name", "mandatory", "offset", "format", "tz", "as_time")
        self.mapped[186].resolve_generated_offsets("analysis")
        self.mapped[187].resolve_generated_offsets("path", "append")
        self.mapped[188].resolve_generated_offsets("from", "subject", "body", "body_is_html", "to", "cc", "bcc")
        self.mapped[189].resolve_generated_offsets("name", "mandatory", "offset")
        self.mapped[190].resolve_generated_offsets("path", "append")
        self.mapped[191].resolve_generated_offsets("path", "format", "max_rows", "max_invalid", "invalid_path")
        self.mapped[192].resolve_generated_offsets("path", "format", "offset", "max")
        self.mapped[193].resolve_generated_offsets("path", "size", "last_modification")
        self.mapped[194].resolve_generated_offsets("file_path", "config")
        self.mapped[195].resolve_generated_offsets("name", "mandatory", "offset")
        self.mapped[196].resolve_generated_offsets("name", "mandatory", "offset", "unit")
        self.mapped[197].resolve_generated_offsets("name", "mandatory", "offset")
        self.mapped[198].resolve_generated_offset_with_values("plain", 0, "ssl_tls", 1, "starttls", 2)
        self.mapped[199].resolve_generated_offsets("header_lines", "separator", "string_delimiter", "decimal_separator", "thousands_separator", "row_limit", "enumerable_limit", "date_check_limit", "date_formats")
        self.mapped[199].static_values = [100, 100]
        self.mapped[200].resolve_generated_offsets("path", "pos")
        self.mapped[201].resolve_generated_offsets("path", "pos")
        self.mapped[202].resolve_generated_offsets("config", "statistics")
        self.mapped[203].resolve_generated_offsets("path", "append", "format")
        self.mapped[204].resolve_generated_offset_with_values("plain", None, "base64", None, "base64url", None, "hexadecimal", None)
        self.mapped[205].resolve_generated_offsets("path", "pos", "format", "sharding")
        self.mapped[206].resolve_generated_offsets("path", "pos")
        self.mapped[207].resolve_generated_offsets("name", "mandatory", "offset")
        self.mapped[208].resolve_generated_offsets("name", "mandatory", "offset")
        self.mapped[209].resolve_generated_offsets("name", "mandatory", "offset", "unit")
        self.mapped[210].resolve_generated_offsets("path", "pos")
        self.mapped[211].resolve_generated_offsets("host", "port", "mode", "authenticate", "user", "pass")
        self.mapped[212].resolve_generated_offsets("format", "ident_col", "time_col")
        self.mapped[213].resolve_generated_offsets("line_count", "fail_count", "invalid_count")
        self.mapped[214].resolve_generated_offsets("path", "pos")
        self.mapped[215].resolve_generated_offsets("path", "append")
        self.mapped[216].resolve_generated_offset_with_values("none", 0, "plain", 1, "login", 2)
        self.mapped[217].resolve_generated_offsets("header_lines", "separator", "string_delimiter", "decimal_separator", "thousands_separator", "columns_size", "columns")
        self.mapped[218].resolve_generated_offsets("id", "column", "modulo")
        self.mapped[220].resolve_generated_offsets("min", "max", "bins", "open")
        self.mapped[221].resolve_generated_offsets("min", "max", "bins", "open")
        self.mapped[222].resolve_generated_offsets("sum", "sumsq", "count")
        self.mapped[223].resolve_generated_offsets("start", "total", "counter", "duration", "progress", "speed", "remaining")
        self.mapped[224].resolve_generated_offsets("min", "max", "whisker_low", "whisker_high", "percentile1", "percentile5", "percentile25", "percentile50", "percentile75", "percentile95", "percentile99", "count_outliers_low", "count_outliers_high", "percentage_outliers_low", "percentage_outliers_high", "sum", "avg", "std", "size")
        self.mapped[225].resolve_generated_offsets("seed", "v")
        self.mapped[226].resolve_generated_offsets("quantizers")
        self.mapped[228].resolve_generated_offsets("min", "max", "center")
        self.mapped[230].resolve_generated_offsets("sum", "sumsq", "count", "min", "max")
        self.mapped[231].resolve_generated_offsets("values")
        self.mapped[232].resolve_generated_offsets("quantizer", "bins", "nb_rejected", "nb_accepted")
        self.mapped[233].resolve_generated_offsets("values", "span", "sum", "sumsq", "field")
        self.mapped[234].resolve_generated_offsets("min", "max", "step_starts", "open")
        self.mapped[236].resolve_generated_offsets("min", "max", "center")
        self.mapped[237].resolve_generated_offsets("values", "capacity")
        self.mapped[238].resolve_generated_offsets("quantizer", "precision", "bins", "value_min", "nb_rejected")
        self.mapped[239].resolve_generated_offsets("values", "span", "sum", "sumsq", "field")
