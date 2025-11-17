# AUTO-GENERATED FILE PLEASE DO NOT MODIFY MANUALLY
from __future__ import annotations
from ctypes import *
from typing import *
from .greycat import *
from .std_n import std_n

@final
class core:
    __T = TypeVar("__T")
    __K = TypeVar("__K")
    __V = TypeVar("__V")
    __U = TypeVar("__U")

    @final
    class VectorIndex(Generic[__T], GreyCat.Object):
        name_: Final[str] = "core::VectorIndex"

        def __init__(self, vectors: core.nodeList, values: core.nodeList, count: int, max_level: int, entry_index: int, vertices: core.nodeList, rng: util.Random, distance: core.TensorDistance, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[0]
            attributes: list = [vectors, values, count, max_level, entry_index, vertices, rng, distance]
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

        def vectors(self) -> core.nodeList:
            return self._get(self.type_.generated_offsets[0])

        def set_vectors(self, v: core.nodeList) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def values(self) -> core.nodeList:
            return self._get(self.type_.generated_offsets[1])

        def set_values(self, v: core.nodeList) -> None:
            self._set(self.type_.generated_offsets[1], v)

        def count(self) -> int:
            return self._get(self.type_.generated_offsets[2])

        def set_count(self, v: int) -> None:
            self._set(self.type_.generated_offsets[2], v)

        def max_level(self) -> int:
            return self._get(self.type_.generated_offsets[3])

        def set_max_level(self, v: int) -> None:
            self._set(self.type_.generated_offsets[3], v)

        def entry_index(self) -> int:
            return self._get(self.type_.generated_offsets[4])

        def set_entry_index(self, v: int) -> None:
            self._set(self.type_.generated_offsets[4], v)

        def vertices(self) -> core.nodeList:
            return self._get(self.type_.generated_offsets[5])

        def set_vertices(self, v: core.nodeList) -> None:
            self._set(self.type_.generated_offsets[5], v)

        def rng(self) -> util.Random:
            return self._get(self.type_.generated_offsets[6])

        def set_rng(self, v: util.Random) -> None:
            self._set(self.type_.generated_offsets[6], v)

        def distance(self) -> core.TensorDistance:
            return self._get(self.type_.generated_offsets[7])

        def set_distance(self, v: core.TensorDistance) -> None:
            self._set(self.type_.generated_offsets[7], v)

    @final
    class t3f(std_n.core._t3f):
        name_: Final[str] = "core::t3f"

        def __init__(self, _type: Optional[GreyCat.Type] = None, *_):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[1]
            super().__init__(_type)

    @final
    class TensorType(GreyCat.Enum):
        name_: Final[str] = "core::TensorType"
        __indices_by_values: dict[str, int] = {
            "i32": 0,
            "i64": 1,
            "f32": 2,
            "f64": 3,
            "c64": 4,
            "c128": 5,
        }

        def __init__(self, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[2]
            attributes: list = []
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

        def __class_getitem__(cls, key) -> core.TensorType:
            greycat: GreyCat
            if isinstance(key, tuple):
                key, greycat = key
            else:
                greycat = GreyCat._DEFAULT
            t: Final[GreyCat.Type] = greycat.libs_by_name[_std._name].mapped[2]
            return t.enum_values[t.generated_offsets[core.TensorType.__indices_by_values[key]]]

    @final
    class nodeGeo(Generic[__T], std_n.core._nodeGeo[__T]):
        name_: Final[str] = "core::nodeGeo"

        def __init__(self, _type: Optional[GreyCat.Type] = None, *_):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[3]
            super().__init__(_type)

    @final
    class nodeTime(Generic[__T], std_n.core._nodeTime[__T]):
        name_: Final[str] = "core::nodeTime"

        def __init__(self, _type: Optional[GreyCat.Type] = None, *_):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[4]
            super().__init__(_type)

    @final
    class nodeIndexBucket(Generic[__K, __V], GreyCat.Object):
        name_: Final[str] = "core::nodeIndexBucket"

        def __init__(self, key: core.__K, value: core.__V, next: core.nodeIndexBucket, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[5]
            attributes: list = [key, value, next]
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

        def key(self) -> core.__K:
            return self._get(self.type_.generated_offsets[0])

        def set_key(self, v: core.__K) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def value(self) -> core.__V:
            return self._get(self.type_.generated_offsets[1])

        def set_value(self, v: core.__V) -> None:
            self._set(self.type_.generated_offsets[1], v)

        def next(self) -> core.nodeIndexBucket:
            return self._get(self.type_.generated_offsets[2])

        def set_next(self, v: core.nodeIndexBucket) -> None:
            self._set(self.type_.generated_offsets[2], v)

    @final
    class String(std_n.core._String):
        name_: Final[str] = "core::String"

        def __init__(self, _type: Optional[GreyCat.Type] = None, *_):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[6]
            super().__init__(_type)

    @final
    class FloatPrecision(GreyCat.Enum):
        name_: Final[str] = "core::FloatPrecision"
        __indices_by_values: dict[str, int] = {
            "p1": 0,
            "p10": 1,
            "p100": 2,
            "p1000": 3,
            "p10000": 4,
            "p100000": 5,
            "p1000000": 6,
            "p10000000": 7,
            "p100000000": 8,
            "p1000000000": 9,
            "p10000000000": 10,
        }

        def __init__(self, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[7]
            attributes: list = []
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

        def __class_getitem__(cls, key) -> core.FloatPrecision:
            greycat: GreyCat
            if isinstance(key, tuple):
                key, greycat = key
            else:
                greycat = GreyCat._DEFAULT
            t: Final[GreyCat.Type] = greycat.libs_by_name[_std._name].mapped[7]
            return t.enum_values[t.generated_offsets[core.FloatPrecision.__indices_by_values[key]]]

    @final
    class field(std_n.core._field):
        name_: Final[str] = "core::field"

        def __init__(self, _type: Optional[GreyCat.Type] = None, *_):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[8]
            super().__init__(_type)

    @final
    class nodeList(Generic[__T], std_n.core._nodeList[__T]):
        name_: Final[str] = "core::nodeList"

        def __init__(self, _type: Optional[GreyCat.Type] = None, *_):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[9]
            super().__init__(_type)

    @final
    class Buffer(std_n.core._Buffer):
        name_: Final[str] = "core::Buffer"

        def __init__(self, _type: Optional[GreyCat.Type] = None, *_):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[10]
            super().__init__(_type)

    @final
    class t2(std_n.core._t2):
        name_: Final[str] = "core::t2"

        def __init__(self, _type: Optional[GreyCat.Type] = None, *_):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[11]
            super().__init__(_type)

    @final
    class time(std_n.core._time):
        name_: Final[str] = "core::time"

        def __init__(self, _type: Optional[GreyCat.Type] = None, *_):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[12]
            super().__init__(_type)

    @final
    class CalendarUnit(GreyCat.Enum):
        name_: Final[str] = "core::CalendarUnit"
        __indices_by_values: dict[str, int] = {
            "year": 0,
            "month": 1,
            "day": 2,
            "hour": 3,
            "minute": 4,
            "second": 5,
            "microsecond": 6,
        }

        def __init__(self, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[13]
            attributes: list = []
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

        def __class_getitem__(cls, key) -> core.CalendarUnit:
            greycat: GreyCat
            if isinstance(key, tuple):
                key, greycat = key
            else:
                greycat = GreyCat._DEFAULT
            t: Final[GreyCat.Type] = greycat.libs_by_name[_std._name].mapped[13]
            return t.enum_values[t.generated_offsets[core.CalendarUnit.__indices_by_values[key]]]

    @final
    class Map(Generic[__K, __V], std_n.core._Map[__K, __V]):
        name_: Final[str] = "core::Map"

        def __init__(self, _type: Optional[GreyCat.Type] = None, *_):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[14]
            super().__init__(_type)

    @final
    class TensorDistance(GreyCat.Enum):
        name_: Final[str] = "core::TensorDistance"
        __indices_by_values: dict[str, int] = {
            "euclidean": 0,
            "cosine": 1,
        }

        def __init__(self, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[15]
            attributes: list = []
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

        def __class_getitem__(cls, key) -> core.TensorDistance:
            greycat: GreyCat
            if isinstance(key, tuple):
                key, greycat = key
            else:
                greycat = GreyCat._DEFAULT
            t: Final[GreyCat.Type] = greycat.libs_by_name[_std._name].mapped[15]
            return t.enum_values[t.generated_offsets[core.TensorDistance.__indices_by_values[key]]]

    @final
    class MathConstants(GreyCat.Object):
        name_: Final[str] = "core::MathConstants"

        def __init__(self, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[16]
            attributes: list = []
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

    @final
    class TimeZone(GreyCat.Enum):
        name_: Final[str] = "core::TimeZone"
        __indices_by_values: dict[str, int] = {
            "UTC": 0,
            "Africa/Abidjan": 1,
            "Africa/Accra": 2,
            "Africa/Addis_Ababa": 3,
            "Africa/Algiers": 4,
            "Africa/Asmara": 5,
            "Africa/Asmera": 6,
            "Africa/Bamako": 7,
            "Africa/Bangui": 8,
            "Africa/Banjul": 9,
            "Africa/Bissau": 10,
            "Africa/Blantyre": 11,
            "Africa/Brazzaville": 12,
            "Africa/Bujumbura": 13,
            "Africa/Cairo": 14,
            "Africa/Casablanca": 15,
            "Africa/Ceuta": 16,
            "Africa/Conakry": 17,
            "Africa/Dakar": 18,
            "Africa/Dar_es_Salaam": 19,
            "Africa/Djibouti": 20,
            "Africa/Douala": 21,
            "Africa/El_Aaiun": 22,
            "Africa/Freetown": 23,
            "Africa/Gaborone": 24,
            "Africa/Harare": 25,
            "Africa/Johannesburg": 26,
            "Africa/Juba": 27,
            "Africa/Kampala": 28,
            "Africa/Khartoum": 29,
            "Africa/Kigali": 30,
            "Africa/Kinshasa": 31,
            "Africa/Lagos": 32,
            "Africa/Libreville": 33,
            "Africa/Lome": 34,
            "Africa/Luanda": 35,
            "Africa/Lubumbashi": 36,
            "Africa/Lusaka": 37,
            "Africa/Malabo": 38,
            "Africa/Maputo": 39,
            "Africa/Maseru": 40,
            "Africa/Mbabane": 41,
            "Africa/Mogadishu": 42,
            "Africa/Monrovia": 43,
            "Africa/Nairobi": 44,
            "Africa/Ndjamena": 45,
            "Africa/Niamey": 46,
            "Africa/Nouakchott": 47,
            "Africa/Ouagadougou": 48,
            "Africa/Porto-Novo": 49,
            "Africa/Sao_Tome": 50,
            "Africa/Timbuktu": 51,
            "Africa/Tripoli": 52,
            "Africa/Tunis": 53,
            "Africa/Windhoek": 54,
            "America/Adak": 55,
            "America/Anchorage": 56,
            "America/Anguilla": 57,
            "America/Antigua": 58,
            "America/Araguaina": 59,
            "America/Argentina/Buenos_Aires": 60,
            "America/Argentina/Catamarca": 61,
            "America/Argentina/ComodRivadavia": 62,
            "America/Argentina/Cordoba": 63,
            "America/Argentina/Jujuy": 64,
            "America/Argentina/La_Rioja": 65,
            "America/Argentina/Mendoza": 66,
            "America/Argentina/Rio_Gallegos": 67,
            "America/Argentina/Salta": 68,
            "America/Argentina/San_Juan": 69,
            "America/Argentina/San_Luis": 70,
            "America/Argentina/Tucuman": 71,
            "America/Argentina/Ushuaia": 72,
            "America/Aruba": 73,
            "America/Asuncion": 74,
            "America/Atikokan": 75,
            "America/Atka": 76,
            "America/Bahia": 77,
            "America/Bahia_Banderas": 78,
            "America/Barbados": 79,
            "America/Belem": 80,
            "America/Belize": 81,
            "America/Blanc-Sablon": 82,
            "America/Boa_Vista": 83,
            "America/Bogota": 84,
            "America/Boise": 85,
            "America/Buenos_Aires": 86,
            "America/Cambridge_Bay": 87,
            "America/Campo_Grande": 88,
            "America/Cancun": 89,
            "America/Caracas": 90,
            "America/Catamarca": 91,
            "America/Cayenne": 92,
            "America/Cayman": 93,
            "America/Chicago": 94,
            "America/Chihuahua": 95,
            "America/Ciudad_Juarez": 96,
            "America/Coral_Harbour": 97,
            "America/Cordoba": 98,
            "America/Costa_Rica": 99,
            "America/Coyhaique": 100,
            "America/Creston": 101,
            "America/Cuiaba": 102,
            "America/Curacao": 103,
            "America/Danmarkshavn": 104,
            "America/Dawson": 105,
            "America/Dawson_Creek": 106,
            "America/Denver": 107,
            "America/Detroit": 108,
            "America/Dominica": 109,
            "America/Edmonton": 110,
            "America/Eirunepe": 111,
            "America/El_Salvador": 112,
            "America/Ensenada": 113,
            "America/Fort_Nelson": 114,
            "America/Fort_Wayne": 115,
            "America/Fortaleza": 116,
            "America/Glace_Bay": 117,
            "America/Godthab": 118,
            "America/Goose_Bay": 119,
            "America/Grand_Turk": 120,
            "America/Grenada": 121,
            "America/Guadeloupe": 122,
            "America/Guatemala": 123,
            "America/Guayaquil": 124,
            "America/Guyana": 125,
            "America/Halifax": 126,
            "America/Havana": 127,
            "America/Hermosillo": 128,
            "America/Indiana/Indianapolis": 129,
            "America/Indiana/Knox": 130,
            "America/Indiana/Marengo": 131,
            "America/Indiana/Petersburg": 132,
            "America/Indiana/Tell_City": 133,
            "America/Indiana/Vevay": 134,
            "America/Indiana/Vincennes": 135,
            "America/Indiana/Winamac": 136,
            "America/Indianapolis": 137,
            "America/Inuvik": 138,
            "America/Iqaluit": 139,
            "America/Jamaica": 140,
            "America/Jujuy": 141,
            "America/Juneau": 142,
            "America/Kentucky/Louisville": 143,
            "America/Kentucky/Monticello": 144,
            "America/Knox_IN": 145,
            "America/Kralendijk": 146,
            "America/La_Paz": 147,
            "America/Lima": 148,
            "America/Los_Angeles": 149,
            "America/Louisville": 150,
            "America/Lower_Princes": 151,
            "America/Maceio": 152,
            "America/Managua": 153,
            "America/Manaus": 154,
            "America/Marigot": 155,
            "America/Martinique": 156,
            "America/Matamoros": 157,
            "America/Mazatlan": 158,
            "America/Mendoza": 159,
            "America/Menominee": 160,
            "America/Merida": 161,
            "America/Metlakatla": 162,
            "America/Mexico_City": 163,
            "America/Miquelon": 164,
            "America/Moncton": 165,
            "America/Monterrey": 166,
            "America/Montevideo": 167,
            "America/Montreal": 168,
            "America/Montserrat": 169,
            "America/Nassau": 170,
            "America/New_York": 171,
            "America/Nipigon": 172,
            "America/Nome": 173,
            "America/Noronha": 174,
            "America/North_Dakota/Beulah": 175,
            "America/North_Dakota/Center": 176,
            "America/North_Dakota/New_Salem": 177,
            "America/Nuuk": 178,
            "America/Ojinaga": 179,
            "America/Panama": 180,
            "America/Pangnirtung": 181,
            "America/Paramaribo": 182,
            "America/Phoenix": 183,
            "America/Port-au-Prince": 184,
            "America/Port_of_Spain": 185,
            "America/Porto_Acre": 186,
            "America/Porto_Velho": 187,
            "America/Puerto_Rico": 188,
            "America/Punta_Arenas": 189,
            "America/Rainy_River": 190,
            "America/Rankin_Inlet": 191,
            "America/Recife": 192,
            "America/Regina": 193,
            "America/Resolute": 194,
            "America/Rio_Branco": 195,
            "America/Rosario": 196,
            "America/Santa_Isabel": 197,
            "America/Santarem": 198,
            "America/Santiago": 199,
            "America/Santo_Domingo": 200,
            "America/Sao_Paulo": 201,
            "America/Scoresbysund": 202,
            "America/Shiprock": 203,
            "America/Sitka": 204,
            "America/St_Barthelemy": 205,
            "America/St_Johns": 206,
            "America/St_Kitts": 207,
            "America/St_Lucia": 208,
            "America/St_Thomas": 209,
            "America/St_Vincent": 210,
            "America/Swift_Current": 211,
            "America/Tegucigalpa": 212,
            "America/Thule": 213,
            "America/Thunder_Bay": 214,
            "America/Tijuana": 215,
            "America/Toronto": 216,
            "America/Tortola": 217,
            "America/Vancouver": 218,
            "America/Virgin": 219,
            "America/Whitehorse": 220,
            "America/Winnipeg": 221,
            "America/Yakutat": 222,
            "America/Yellowknife": 223,
            "Antarctica/Casey": 224,
            "Antarctica/Davis": 225,
            "Antarctica/DumontDUrville": 226,
            "Antarctica/Macquarie": 227,
            "Antarctica/Mawson": 228,
            "Antarctica/McMurdo": 229,
            "Antarctica/Palmer": 230,
            "Antarctica/Rothera": 231,
            "Antarctica/South_Pole": 232,
            "Antarctica/Syowa": 233,
            "Antarctica/Troll": 234,
            "Antarctica/Vostok": 235,
            "Arctic/Longyearbyen": 236,
            "Asia/Aden": 237,
            "Asia/Almaty": 238,
            "Asia/Amman": 239,
            "Asia/Anadyr": 240,
            "Asia/Aqtau": 241,
            "Asia/Aqtobe": 242,
            "Asia/Ashgabat": 243,
            "Asia/Ashkhabad": 244,
            "Asia/Atyrau": 245,
            "Asia/Baghdad": 246,
            "Asia/Bahrain": 247,
            "Asia/Baku": 248,
            "Asia/Bangkok": 249,
            "Asia/Barnaul": 250,
            "Asia/Beirut": 251,
            "Asia/Bishkek": 252,
            "Asia/Brunei": 253,
            "Asia/Calcutta": 254,
            "Asia/Chita": 255,
            "Asia/Choibalsan": 256,
            "Asia/Chongqing": 257,
            "Asia/Chungking": 258,
            "Asia/Colombo": 259,
            "Asia/Dacca": 260,
            "Asia/Damascus": 261,
            "Asia/Dhaka": 262,
            "Asia/Dili": 263,
            "Asia/Dubai": 264,
            "Asia/Dushanbe": 265,
            "Asia/Famagusta": 266,
            "Asia/Gaza": 267,
            "Asia/Harbin": 268,
            "Asia/Hebron": 269,
            "Asia/Ho_Chi_Minh": 270,
            "Asia/Hong_Kong": 271,
            "Asia/Hovd": 272,
            "Asia/Irkutsk": 273,
            "Asia/Istanbul": 274,
            "Asia/Jakarta": 275,
            "Asia/Jayapura": 276,
            "Asia/Jerusalem": 277,
            "Asia/Kabul": 278,
            "Asia/Kamchatka": 279,
            "Asia/Karachi": 280,
            "Asia/Kashgar": 281,
            "Asia/Kathmandu": 282,
            "Asia/Katmandu": 283,
            "Asia/Khandyga": 284,
            "Asia/Kolkata": 285,
            "Asia/Krasnoyarsk": 286,
            "Asia/Kuala_Lumpur": 287,
            "Asia/Kuching": 288,
            "Asia/Kuwait": 289,
            "Asia/Macao": 290,
            "Asia/Macau": 291,
            "Asia/Magadan": 292,
            "Asia/Makassar": 293,
            "Asia/Manila": 294,
            "Asia/Muscat": 295,
            "Asia/Nicosia": 296,
            "Asia/Novokuznetsk": 297,
            "Asia/Novosibirsk": 298,
            "Asia/Omsk": 299,
            "Asia/Oral": 300,
            "Asia/Phnom_Penh": 301,
            "Asia/Pontianak": 302,
            "Asia/Pyongyang": 303,
            "Asia/Qatar": 304,
            "Asia/Qostanay": 305,
            "Asia/Qyzylorda": 306,
            "Asia/Rangoon": 307,
            "Asia/Riyadh": 308,
            "Asia/Saigon": 309,
            "Asia/Sakhalin": 310,
            "Asia/Samarkand": 311,
            "Asia/Seoul": 312,
            "Asia/Shanghai": 313,
            "Asia/Singapore": 314,
            "Asia/Srednekolymsk": 315,
            "Asia/Taipei": 316,
            "Asia/Tashkent": 317,
            "Asia/Tbilisi": 318,
            "Asia/Tehran": 319,
            "Asia/Tel_Aviv": 320,
            "Asia/Thimbu": 321,
            "Asia/Thimphu": 322,
            "Asia/Tokyo": 323,
            "Asia/Tomsk": 324,
            "Asia/Ujung_Pandang": 325,
            "Asia/Ulaanbaatar": 326,
            "Asia/Ulan_Bator": 327,
            "Asia/Urumqi": 328,
            "Asia/Ust-Nera": 329,
            "Asia/Vientiane": 330,
            "Asia/Vladivostok": 331,
            "Asia/Yakutsk": 332,
            "Asia/Yangon": 333,
            "Asia/Yekaterinburg": 334,
            "Asia/Yerevan": 335,
            "Atlantic/Azores": 336,
            "Atlantic/Bermuda": 337,
            "Atlantic/Canary": 338,
            "Atlantic/Cape_Verde": 339,
            "Atlantic/Faeroe": 340,
            "Atlantic/Faroe": 341,
            "Atlantic/Jan_Mayen": 342,
            "Atlantic/Madeira": 343,
            "Atlantic/Reykjavik": 344,
            "Atlantic/South_Georgia": 345,
            "Atlantic/St_Helena": 346,
            "Atlantic/Stanley": 347,
            "Australia/ACT": 348,
            "Australia/Adelaide": 349,
            "Australia/Brisbane": 350,
            "Australia/Broken_Hill": 351,
            "Australia/Canberra": 352,
            "Australia/Currie": 353,
            "Australia/Darwin": 354,
            "Australia/Eucla": 355,
            "Australia/Hobart": 356,
            "Australia/LHI": 357,
            "Australia/Lindeman": 358,
            "Australia/Lord_Howe": 359,
            "Australia/Melbourne": 360,
            "Australia/NSW": 361,
            "Australia/North": 362,
            "Australia/Perth": 363,
            "Australia/Queensland": 364,
            "Australia/South": 365,
            "Australia/Sydney": 366,
            "Australia/Tasmania": 367,
            "Australia/Victoria": 368,
            "Australia/West": 369,
            "Australia/Yancowinna": 370,
            "Brazil/Acre": 371,
            "Brazil/DeNoronha": 372,
            "Brazil/East": 373,
            "Brazil/West": 374,
            "CET": 375,
            "CST6CDT": 376,
            "Canada/Atlantic": 377,
            "Canada/Central": 378,
            "Canada/Eastern": 379,
            "Canada/Mountain": 380,
            "Canada/Newfoundland": 381,
            "Canada/Pacific": 382,
            "Canada/Saskatchewan": 383,
            "Canada/Yukon": 384,
            "Chile/Continental": 385,
            "Chile/EasterIsland": 386,
            "Cuba": 387,
            "EET": 388,
            "EST": 389,
            "EST5EDT": 390,
            "Egypt": 391,
            "Eire": 392,
            "Etc/GMT": 393,
            "Etc/GMT+0": 394,
            "Etc/GMT+1": 395,
            "Etc/GMT+10": 396,
            "Etc/GMT+11": 397,
            "Etc/GMT+12": 398,
            "Etc/GMT+2": 399,
            "Etc/GMT+3": 400,
            "Etc/GMT+4": 401,
            "Etc/GMT+5": 402,
            "Etc/GMT+6": 403,
            "Etc/GMT+7": 404,
            "Etc/GMT+8": 405,
            "Etc/GMT+9": 406,
            "Etc/GMT-0": 407,
            "Etc/GMT-1": 408,
            "Etc/GMT-10": 409,
            "Etc/GMT-11": 410,
            "Etc/GMT-12": 411,
            "Etc/GMT-13": 412,
            "Etc/GMT-14": 413,
            "Etc/GMT-2": 414,
            "Etc/GMT-3": 415,
            "Etc/GMT-4": 416,
            "Etc/GMT-5": 417,
            "Etc/GMT-6": 418,
            "Etc/GMT-7": 419,
            "Etc/GMT-8": 420,
            "Etc/GMT-9": 421,
            "Etc/GMT0": 422,
            "Etc/Greenwich": 423,
            "Etc/UCT": 424,
            "Etc/UTC": 425,
            "Etc/Universal": 426,
            "Etc/Zulu": 427,
            "Europe/Amsterdam": 428,
            "Europe/Andorra": 429,
            "Europe/Astrakhan": 430,
            "Europe/Athens": 431,
            "Europe/Belfast": 432,
            "Europe/Belgrade": 433,
            "Europe/Berlin": 434,
            "Europe/Bratislava": 435,
            "Europe/Brussels": 436,
            "Europe/Bucharest": 437,
            "Europe/Budapest": 438,
            "Europe/Busingen": 439,
            "Europe/Chisinau": 440,
            "Europe/Copenhagen": 441,
            "Europe/Dublin": 442,
            "Europe/Gibraltar": 443,
            "Europe/Guernsey": 444,
            "Europe/Helsinki": 445,
            "Europe/Isle_of_Man": 446,
            "Europe/Istanbul": 447,
            "Europe/Jersey": 448,
            "Europe/Kaliningrad": 449,
            "Europe/Kiev": 450,
            "Europe/Kirov": 451,
            "Europe/Kyiv": 452,
            "Europe/Lisbon": 453,
            "Europe/Ljubljana": 454,
            "Europe/London": 455,
            "Europe/Luxembourg": 456,
            "Europe/Madrid": 457,
            "Europe/Malta": 458,
            "Europe/Mariehamn": 459,
            "Europe/Minsk": 460,
            "Europe/Monaco": 461,
            "Europe/Moscow": 462,
            "Europe/Nicosia": 463,
            "Europe/Oslo": 464,
            "Europe/Paris": 465,
            "Europe/Podgorica": 466,
            "Europe/Prague": 467,
            "Europe/Riga": 468,
            "Europe/Rome": 469,
            "Europe/Samara": 470,
            "Europe/San_Marino": 471,
            "Europe/Sarajevo": 472,
            "Europe/Saratov": 473,
            "Europe/Simferopol": 474,
            "Europe/Skopje": 475,
            "Europe/Sofia": 476,
            "Europe/Stockholm": 477,
            "Europe/Tallinn": 478,
            "Europe/Tirane": 479,
            "Europe/Tiraspol": 480,
            "Europe/Ulyanovsk": 481,
            "Europe/Uzhgorod": 482,
            "Europe/Vaduz": 483,
            "Europe/Vatican": 484,
            "Europe/Vienna": 485,
            "Europe/Vilnius": 486,
            "Europe/Volgograd": 487,
            "Europe/Warsaw": 488,
            "Europe/Zagreb": 489,
            "Europe/Zaporozhye": 490,
            "Europe/Zurich": 491,
            "Factory": 492,
            "GB": 493,
            "GB-Eire": 494,
            "GMT": 495,
            "GMT+0": 496,
            "GMT-0": 497,
            "GMT0": 498,
            "Greenwich": 499,
            "HST": 500,
            "Hongkong": 501,
            "Iceland": 502,
            "Indian/Antananarivo": 503,
            "Indian/Chagos": 504,
            "Indian/Christmas": 505,
            "Indian/Cocos": 506,
            "Indian/Comoro": 507,
            "Indian/Kerguelen": 508,
            "Indian/Mahe": 509,
            "Indian/Maldives": 510,
            "Indian/Mauritius": 511,
            "Indian/Mayotte": 512,
            "Indian/Reunion": 513,
            "Iran": 514,
            "Israel": 515,
            "Jamaica": 516,
            "Japan": 517,
            "Kwajalein": 518,
            "Libya": 519,
            "MET": 520,
            "MST": 521,
            "MST7MDT": 522,
            "Mexico/BajaNorte": 523,
            "Mexico/BajaSur": 524,
            "Mexico/General": 525,
            "NZ": 526,
            "NZ-CHAT": 527,
            "Navajo": 528,
            "PRC": 529,
            "PST8PDT": 530,
            "Pacific/Apia": 531,
            "Pacific/Auckland": 532,
            "Pacific/Bougainville": 533,
            "Pacific/Chatham": 534,
            "Pacific/Chuuk": 535,
            "Pacific/Easter": 536,
            "Pacific/Efate": 537,
            "Pacific/Enderbury": 538,
            "Pacific/Fakaofo": 539,
            "Pacific/Fiji": 540,
            "Pacific/Funafuti": 541,
            "Pacific/Galapagos": 542,
            "Pacific/Gambier": 543,
            "Pacific/Guadalcanal": 544,
            "Pacific/Guam": 545,
            "Pacific/Honolulu": 546,
            "Pacific/Johnston": 547,
            "Pacific/Kanton": 548,
            "Pacific/Kiritimati": 549,
            "Pacific/Kosrae": 550,
            "Pacific/Kwajalein": 551,
            "Pacific/Majuro": 552,
            "Pacific/Marquesas": 553,
            "Pacific/Midway": 554,
            "Pacific/Nauru": 555,
            "Pacific/Niue": 556,
            "Pacific/Norfolk": 557,
            "Pacific/Noumea": 558,
            "Pacific/Pago_Pago": 559,
            "Pacific/Palau": 560,
            "Pacific/Pitcairn": 561,
            "Pacific/Pohnpei": 562,
            "Pacific/Ponape": 563,
            "Pacific/Port_Moresby": 564,
            "Pacific/Rarotonga": 565,
            "Pacific/Saipan": 566,
            "Pacific/Samoa": 567,
            "Pacific/Tahiti": 568,
            "Pacific/Tarawa": 569,
            "Pacific/Tongatapu": 570,
            "Pacific/Truk": 571,
            "Pacific/Wake": 572,
            "Pacific/Wallis": 573,
            "Pacific/Yap": 574,
            "Poland": 575,
            "Portugal": 576,
            "ROC": 577,
            "ROK": 578,
            "Singapore": 579,
            "Turkey": 580,
            "UCT": 581,
            "US/Alaska": 582,
            "US/Aleutian": 583,
            "US/Arizona": 584,
            "US/Central": 585,
            "US/East-Indiana": 586,
            "US/Eastern": 587,
            "US/Hawaii": 588,
            "US/Indiana-Starke": 589,
            "US/Michigan": 590,
            "US/Mountain": 591,
            "US/Pacific": 592,
            "US/Samoa": 593,
            "Universal": 594,
            "W-SU": 595,
            "WET": 596,
            "Zulu": 597,
        }

        def __init__(self, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[17]
            attributes: list = []
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

        def __class_getitem__(cls, key) -> core.TimeZone:
            greycat: GreyCat
            if isinstance(key, tuple):
                key, greycat = key
            else:
                greycat = GreyCat._DEFAULT
            t: Final[GreyCat.Type] = greycat.libs_by_name[_std._name].mapped[17]
            return t.enum_values[t.generated_offsets[core.TimeZone.__indices_by_values[key]]]

    @final
    class t3(std_n.core._t3):
        name_: Final[str] = "core::t3"

        def __init__(self, _type: Optional[GreyCat.Type] = None, *_):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[18]
            super().__init__(_type)

    @final
    class type(std_n.core._type):
        name_: Final[str] = "core::type"

        def __init__(self, _type: Optional[GreyCat.Type] = None, *_):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[19]
            super().__init__(_type)

    @final
    class str(std_n.core._str):
        name_: Final[str] = "core::str"

        def __init__(self, _type: Optional[GreyCat.Type] = None, *_):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[20]
            super().__init__(_type)

    @final
    class SamplingMode(GreyCat.Enum):
        name_: Final[str] = "core::SamplingMode"
        __indices_by_values: dict[str, int] = {
            "fixed": 0,
            "fixed_reg": 1,
            "adaptative": 2,
            "dense": 3,
        }

        def __init__(self, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[21]
            attributes: list = []
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

        def __class_getitem__(cls, key) -> core.SamplingMode:
            greycat: GreyCat
            if isinstance(key, tuple):
                key, greycat = key
            else:
                greycat = GreyCat._DEFAULT
            t: Final[GreyCat.Type] = greycat.libs_by_name[_std._name].mapped[21]
            return t.enum_values[t.generated_offsets[core.SamplingMode.__indices_by_values[key]]]

    @final
    class node(Generic[__T], std_n.core._node[__T]):
        name_: Final[str] = "core::node"

        def __init__(self, _type: Optional[GreyCat.Type] = None, *_):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[22]
            super().__init__(_type)

    @final
    class VectorVertex(GreyCat.Object):
        name_: Final[str] = "core::VectorVertex"

        def __init__(self, level: int, neighbours: core.Array, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[23]
            attributes: list = [level, neighbours]
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

        def level(self) -> int:
            return self._get(self.type_.generated_offsets[0])

        def set_level(self, v: int) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def neighbours(self) -> core.Array:
            return self._get(self.type_.generated_offsets[1])

        def set_neighbours(self, v: core.Array) -> None:
            self._set(self.type_.generated_offsets[1], v)

    @final
    class TableColumnMapping(GreyCat.Object):
        name_: Final[str] = "core::TableColumnMapping"

        def __init__(self, column: int, extractors: core.Array, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[24]
            attributes: list = [column, extractors]
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

        def column(self) -> int:
            return self._get(self.type_.generated_offsets[0])

        def set_column(self, v: int) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def extractors(self) -> core.Array:
            return self._get(self.type_.generated_offsets[1])

        def set_extractors(self, v: core.Array) -> None:
            self._set(self.type_.generated_offsets[1], v)

    @final
    class ErrorFrame(GreyCat.Object):
        name_: Final[str] = "core::ErrorFrame"

        def __init__(self, module: str, function: str, line: int, column: int, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[25]
            attributes: list = [module, function, line, column]
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

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

    @final
    class nodeIndex(Generic[__K, __V], std_n.core._nodeIndex[__K, __V]):
        name_: Final[str] = "core::nodeIndex"

        def __init__(self, _type: Optional[GreyCat.Type] = None, *_):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[26]
            super().__init__(_type)

    @final
    class GeoBox(GreyCat.Object):
        name_: Final[str] = "core::GeoBox"

        def __init__(self, sw: core.geo, ne: core.geo, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[27]
            attributes: list = [sw, ne]
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

        def sw(self) -> core.geo:
            return self._get(self.type_.generated_offsets[0])

        def set_sw(self, v: core.geo) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def ne(self) -> core.geo:
            return self._get(self.type_.generated_offsets[1])

        def set_ne(self, v: core.geo) -> None:
            self._set(self.type_.generated_offsets[1], v)

    @final
    class Table(Generic[__T], std_n.core._Table[__T]):
        name_: Final[str] = "core::Table"

        def __init__(self, _type: Optional[GreyCat.Type] = None, *_):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[28]
            super().__init__(_type)

    @final
    class t2f(std_n.core._t2f):
        name_: Final[str] = "core::t2f"

        def __init__(self, _type: Optional[GreyCat.Type] = None, *_):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[29]
            super().__init__(_type)

    @final
    class duration(std_n.core._duration):
        name_: Final[str] = "core::duration"

        def __init__(self, _type: Optional[GreyCat.Type] = None, *_):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[30]
            super().__init__(_type)

    @final
    class geo(std_n.core._geo):
        name_: Final[str] = "core::geo"

        def __init__(self, _type: Optional[GreyCat.Type] = None, *_):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[31]
            super().__init__(_type)

    @final
    class Array(Generic[__T], std_n.core._Array[__T]):
        name_: Final[str] = "core::Array"

        def __init__(self, _type: Optional[GreyCat.Type] = None, *_):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[32]
            super().__init__(_type)

    @final
    class Tuple(Generic[__T, __U], GreyCat.Object):
        name_: Final[str] = "core::Tuple"

        def __init__(self, x: core.__T, y: core.__U, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[33]
            attributes: list = [x, y]
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

        def x(self) -> core.__T:
            return self._get(self.type_.generated_offsets[0])

        def set_x(self, v: core.__T) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def y(self) -> core.__U:
            return self._get(self.type_.generated_offsets[1])

        def set_y(self, v: core.__U) -> None:
            self._set(self.type_.generated_offsets[1], v)

    @final
    class GeoPoly(GreyCat.Object):
        name_: Final[str] = "core::GeoPoly"

        def __init__(self, points: core.Array, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[34]
            attributes: list = [points]
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

        def points(self) -> core.Array:
            return self._get(self.type_.generated_offsets[0])

        def set_points(self, v: core.Array) -> None:
            self._set(self.type_.generated_offsets[0], v)

    @final
    class SortOrder(GreyCat.Enum):
        name_: Final[str] = "core::SortOrder"
        __indices_by_values: dict[str, int] = {
            "asc": 0,
            "desc": 1,
        }

        def __init__(self, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[35]
            attributes: list = []
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

        def __class_getitem__(cls, key) -> core.SortOrder:
            greycat: GreyCat
            if isinstance(key, tuple):
                key, greycat = key
            else:
                greycat = GreyCat._DEFAULT
            t: Final[GreyCat.Type] = greycat.libs_by_name[_std._name].mapped[35]
            return t.enum_values[t.generated_offsets[core.SortOrder.__indices_by_values[key]]]

    @final
    class nodeTimeCursor(Generic[__T], GreyCat.Object):
        name_: Final[str] = "core::nodeTimeCursor"

        def __init__(self, n: core.nodeTime, req_time: core.time, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[36]
            attributes: list = [n, req_time]
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

        def n(self) -> core.nodeTime:
            return self._get(self.type_.generated_offsets[0])

        def set_n(self, v: core.nodeTime) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def req_time(self) -> core.time:
            return self._get(self.type_.generated_offsets[1])

        def set_req_time(self, v: core.time) -> None:
            self._set(self.type_.generated_offsets[1], v)

    @final
    class t4f(std_n.core._t4f):
        name_: Final[str] = "core::t4f"

        def __init__(self, _type: Optional[GreyCat.Type] = None, *_):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[37]
            super().__init__(_type)

    @final
    class GeoCircle(GreyCat.Object):
        name_: Final[str] = "core::GeoCircle"

        def __init__(self, center: core.geo, radius: float, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[38]
            attributes: list = [center, radius]
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

        def center(self) -> core.geo:
            return self._get(self.type_.generated_offsets[0])

        def set_center(self, v: core.geo) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def radius(self) -> float:
            return self._get(self.type_.generated_offsets[1])

        def set_radius(self, v: float) -> None:
            self._set(self.type_.generated_offsets[1], v)

    @final
    class t4(std_n.core._t4):
        name_: Final[str] = "core::t4"

        def __init__(self, _type: Optional[GreyCat.Type] = None, *_):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[39]
            super().__init__(_type)

    @final
    class Date(GreyCat.Object):
        name_: Final[str] = "core::Date"

        def __init__(self, year: int, month: int, day: int, hour: int, minute: int, second: int, microsecond: int, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[40]
            attributes: list = [year, month, day, hour, minute, second, microsecond]
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

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

    @final
    class SearchResult(Generic[__K, __V], GreyCat.Object):
        name_: Final[str] = "core::SearchResult"

        def __init__(self, key: core.__K, value: core.__V, distance: float, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[41]
            attributes: list = [key, value, distance]
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

        def key(self) -> core.__K:
            return self._get(self.type_.generated_offsets[0])

        def set_key(self, v: core.__K) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def value(self) -> core.__V:
            return self._get(self.type_.generated_offsets[1])

        def set_value(self, v: core.__V) -> None:
            self._set(self.type_.generated_offsets[1], v)

        def distance(self) -> float:
            return self._get(self.type_.generated_offsets[2])

        def set_distance(self, v: float) -> None:
            self._set(self.type_.generated_offsets[2], v)

    @final
    class DurationUnit(GreyCat.Enum):
        name_: Final[str] = "core::DurationUnit"
        __indices_by_values: dict[str, int] = {
            "microseconds": 0,
            "milliseconds": 1,
            "seconds": 2,
            "minutes": 3,
            "hours": 4,
            "days": 5,
        }

        def __init__(self, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[42]
            attributes: list = []
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

        def __class_getitem__(cls, key) -> core.DurationUnit:
            greycat: GreyCat
            if isinstance(key, tuple):
                key, greycat = key
            else:
                greycat = GreyCat._DEFAULT
            t: Final[GreyCat.Type] = greycat.libs_by_name[_std._name].mapped[42]
            return t.enum_values[t.generated_offsets[core.DurationUnit.__indices_by_values[key]]]

    @final
    class function(std_n.core._function):
        name_: Final[str] = "core::function"

        def __init__(self, _type: Optional[GreyCat.Type] = None, *_):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[43]
            super().__init__(_type)

    @final
    class Tensor(std_n.core._Tensor):
        name_: Final[str] = "core::Tensor"

        def __init__(self, _type: Optional[GreyCat.Type] = None, *_):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[44]
            super().__init__(_type)

    @final
    class ErrorCode(GreyCat.Enum):
        name_: Final[str] = "core::ErrorCode"
        __indices_by_values: dict[str, int] = {
            "none": 0,
            "interrupted": 1,
            "await_": 2,
            "timeout": 3,
            "forbidden": 4,
            "runtime_error": 5,
        }

        def __init__(self, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[45]
            attributes: list = []
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

        def __class_getitem__(cls, key) -> core.ErrorCode:
            greycat: GreyCat
            if isinstance(key, tuple):
                key, greycat = key
            else:
                greycat = GreyCat._DEFAULT
            t: Final[GreyCat.Type] = greycat.libs_by_name[_std._name].mapped[45]
            return t.enum_values[t.generated_offsets[core.ErrorCode.__indices_by_values[key]]]

    @final
    class NodeInfo(Generic[__T], GreyCat.Object):
        name_: Final[str] = "core::NodeInfo"

        def __init__(self, size: int, from_: core.__T, to: core.__T, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[46]
            attributes: list = [size, from_, to]
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

        def size(self) -> int:
            return self._get(self.type_.generated_offsets[0])

        def set_size(self, v: int) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def from_(self) -> core.__T:
            return self._get(self.type_.generated_offsets[1])

        def set_from_(self, v: core.__T) -> None:
            self._set(self.type_.generated_offsets[1], v)

        def to(self) -> core.__T:
            return self._get(self.type_.generated_offsets[2])

        def set_to(self, v: core.__T) -> None:
            self._set(self.type_.generated_offsets[2], v)

    @final
    class Error(GreyCat.Object):
        name_: Final[str] = "core::Error"

        def __init__(self, message: str, stack: core.Array, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[47]
            attributes: list = [message, stack]
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

        def message(self) -> str:
            return self._get(self.type_.generated_offsets[0])

        def set_message(self, v: str) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def stack(self) -> core.Array:
            return self._get(self.type_.generated_offsets[1])

        def set_stack(self, v: core.Array) -> None:
            self._set(self.type_.generated_offsets[1], v)


@final
class io:
    __T = TypeVar("__T")

    @final
    class TextReader(GreyCat.Object):
        name_: Final[str] = "io::TextReader"

        def __init__(self, path: str, pos: int, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[48]
            attributes: list = [path, pos]
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

        def path(self) -> str:
            return self._get(self.type_.generated_offsets[0])

        def set_path(self, v: str) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def pos(self) -> int:
            return self._get(self.type_.generated_offsets[1])

        def set_pos(self, v: int) -> None:
            self._set(self.type_.generated_offsets[1], v)

    @final
    class SmtpMode(GreyCat.Enum):
        name_: Final[str] = "io::SmtpMode"
        __indices_by_values: dict[str, int] = {
            "plain": 0,
            "ssl_tls": 1,
            "starttls": 2,
        }

        def __init__(self, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[49]
            attributes: list = []
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

        def __class_getitem__(cls, key) -> io.SmtpMode:
            greycat: GreyCat
            if isinstance(key, tuple):
                key, greycat = key
            else:
                greycat = GreyCat._DEFAULT
            t: Final[GreyCat.Type] = greycat.libs_by_name[_std._name].mapped[49]
            return t.enum_values[t.generated_offsets[io.SmtpMode.__indices_by_values[key]]]

    @final
    class GcbReader(Generic[__T], GreyCat.Object):
        name_: Final[str] = "io::GcbReader"

        def __init__(self, path: str, pos: int, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[50]
            attributes: list = [path, pos]
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

        def path(self) -> str:
            return self._get(self.type_.generated_offsets[0])

        def set_path(self, v: str) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def pos(self) -> int:
            return self._get(self.type_.generated_offsets[1])

        def set_pos(self, v: int) -> None:
            self._set(self.type_.generated_offsets[1], v)

    @final
    class CsvStatistics(GreyCat.Object):
        name_: Final[str] = "io::CsvStatistics"

        def __init__(self, header_lines: int, separator: c_char, string_delimiter: c_char, decimal_separator: c_char, thousands_separator: c_char, columns: core.Array, line_count: int, fail_count: int, file_count: int, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[51]
            attributes: list = [header_lines, separator, string_delimiter, decimal_separator, thousands_separator, columns, line_count, fail_count, file_count]
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

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

        def columns(self) -> core.Array:
            return self._get(self.type_.generated_offsets[5])

        def set_columns(self, v: core.Array) -> None:
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

    @final
    class CsvAnalysisConfig(GreyCat.Object):
        name_: Final[str] = "io::CsvAnalysisConfig"

        def __init__(self, header_lines: int, separator: c_char, string_delimiter: c_char, decimal_separator: c_char, thousands_separator: c_char, row_limit: int, enumerable_limit: int, date_check_limit: int, date_formats: core.Array, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[52]
            attributes: list = [header_lines, separator, string_delimiter, decimal_separator, thousands_separator, row_limit, enumerable_limit, date_check_limit, date_formats]
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

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

        def date_formats(self) -> core.Array:
            return self._get(self.type_.generated_offsets[8])

        def set_date_formats(self, v: core.Array) -> None:
            self._set(self.type_.generated_offsets[8], v)

    @final
    class TextWriter(Generic[__T], GreyCat.Object):
        name_: Final[str] = "io::TextWriter"

        def __init__(self, path: str, append: bool, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[53]
            attributes: list = [path, append]
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

        def path(self) -> str:
            return self._get(self.type_.generated_offsets[0])

        def set_path(self, v: str) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def append(self) -> bool:
            return self._get(self.type_.generated_offsets[1])

        def set_append(self, v: bool) -> None:
            self._set(self.type_.generated_offsets[1], v)

    @final
    class CsvWriter(Generic[__T], GreyCat.Object):
        name_: Final[str] = "io::CsvWriter"

        def __init__(self, path: str, append: bool, format: io.CsvFormat, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[54]
            attributes: list = [path, append, format]
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

        def path(self) -> str:
            return self._get(self.type_.generated_offsets[0])

        def set_path(self, v: str) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def append(self) -> bool:
            return self._get(self.type_.generated_offsets[1])

        def set_append(self, v: bool) -> None:
            self._set(self.type_.generated_offsets[1], v)

        def format(self) -> io.CsvFormat:
            return self._get(self.type_.generated_offsets[2])

        def set_format(self, v: io.CsvFormat) -> None:
            self._set(self.type_.generated_offsets[2], v)

    @final
    class HttpMethod(GreyCat.Enum):
        name_: Final[str] = "io::HttpMethod"
        __indices_by_values: dict[str, int] = {
            "GET": 0,
            "HEAD": 1,
            "POST": 2,
            "PUT": 3,
            "DELETE": 4,
            "CONNECT": 5,
            "OPTIONS": 6,
            "TRACE": 7,
            "PATCH": 8,
        }

        def __init__(self, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[55]
            attributes: list = []
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

        def __class_getitem__(cls, key) -> io.HttpMethod:
            greycat: GreyCat
            if isinstance(key, tuple):
                key, greycat = key
            else:
                greycat = GreyCat._DEFAULT
            t: Final[GreyCat.Type] = greycat.libs_by_name[_std._name].mapped[55]
            return t.enum_values[t.generated_offsets[io.HttpMethod.__indices_by_values[key]]]

    @final
    class SmtpAuth(GreyCat.Enum):
        name_: Final[str] = "io::SmtpAuth"
        __indices_by_values: dict[str, int] = {
            "none": 0,
            "plain": 1,
            "login": 2,
        }

        def __init__(self, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[56]
            attributes: list = []
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

        def __class_getitem__(cls, key) -> io.SmtpAuth:
            greycat: GreyCat
            if isinstance(key, tuple):
                key, greycat = key
            else:
                greycat = GreyCat._DEFAULT
            t: Final[GreyCat.Type] = greycat.libs_by_name[_std._name].mapped[56]
            return t.enum_values[t.generated_offsets[io.SmtpAuth.__indices_by_values[key]]]

    @final
    class Email(GreyCat.Object):
        name_: Final[str] = "io::Email"

        def __init__(self, from_: str, subject: str, body: str, body_is_html: bool, to: core.Array, cc: core.Array, bcc: core.Array, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[57]
            attributes: list = [from_, subject, body, body_is_html, to, cc, bcc]
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

        def from_(self) -> str:
            return self._get(self.type_.generated_offsets[0])

        def set_from_(self, v: str) -> None:
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

        def to(self) -> core.Array:
            return self._get(self.type_.generated_offsets[4])

        def set_to(self, v: core.Array) -> None:
            self._set(self.type_.generated_offsets[4], v)

        def cc(self) -> core.Array:
            return self._get(self.type_.generated_offsets[5])

        def set_cc(self, v: core.Array) -> None:
            self._set(self.type_.generated_offsets[5], v)

        def bcc(self) -> core.Array:
            return self._get(self.type_.generated_offsets[6])

        def set_bcc(self, v: core.Array) -> None:
            self._set(self.type_.generated_offsets[6], v)

    @final
    class Url(GreyCat.Object):
        name_: Final[str] = "io::Url"

        def __init__(self, protocol: str, host: str, port: int, path: str, params: core.Map, hash: str, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[58]
            attributes: list = [protocol, host, port, path, params, hash]
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

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

        def params(self) -> core.Map:
            return self._get(self.type_.generated_offsets[4])

        def set_params(self, v: core.Map) -> None:
            self._set(self.type_.generated_offsets[4], v)

        def hash(self) -> str:
            return self._get(self.type_.generated_offsets[5])

        def set_hash(self, v: str) -> None:
            self._set(self.type_.generated_offsets[5], v)

    @final
    class Smtp(GreyCat.Object):
        name_: Final[str] = "io::Smtp"

        def __init__(self, host: str, port: int, mode: io.SmtpMode, authenticate: io.SmtpAuth, user: str, pass_: str, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[59]
            attributes: list = [host, port, mode, authenticate, user, pass_]
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

        def host(self) -> str:
            return self._get(self.type_.generated_offsets[0])

        def set_host(self, v: str) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def port(self) -> int:
            return self._get(self.type_.generated_offsets[1])

        def set_port(self, v: int) -> None:
            self._set(self.type_.generated_offsets[1], v)

        def mode(self) -> io.SmtpMode:
            return self._get(self.type_.generated_offsets[2])

        def set_mode(self, v: io.SmtpMode) -> None:
            self._set(self.type_.generated_offsets[2], v)

        def authenticate(self) -> io.SmtpAuth:
            return self._get(self.type_.generated_offsets[3])

        def set_authenticate(self, v: io.SmtpAuth) -> None:
            self._set(self.type_.generated_offsets[3], v)

        def user(self) -> str:
            return self._get(self.type_.generated_offsets[4])

        def set_user(self, v: str) -> None:
            self._set(self.type_.generated_offsets[4], v)

        def pass_(self) -> str:
            return self._get(self.type_.generated_offsets[5])

        def set_pass_(self, v: str) -> None:
            self._set(self.type_.generated_offsets[5], v)

    @final
    class Reader(Generic[__T], GreyCat.Object):
        name_: Final[str] = "io::Reader"

        def __init__(self, path: str, pos: int, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[60]
            attributes: list = [path, pos]
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

        def path(self) -> str:
            return self._get(self.type_.generated_offsets[0])

        def set_path(self, v: str) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def pos(self) -> int:
            return self._get(self.type_.generated_offsets[1])

        def set_pos(self, v: int) -> None:
            self._set(self.type_.generated_offsets[1], v)

    @final
    class CsvColumnStatistics(GreyCat.Object):
        name_: Final[str] = "io::CsvColumnStatistics"

        def __init__(self, name: str, example: Any, null_count: int, bool_count: int, int_count: int, float_count: int, string_count: int, date_count: int, date_format_count: core.Map, enumerable_count: core.Map, profile: util.Gaussian, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[61]
            attributes: list = [name, example, null_count, bool_count, int_count, float_count, string_count, date_count, date_format_count, enumerable_count, profile]
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

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

        def date_format_count(self) -> core.Map:
            return self._get(self.type_.generated_offsets[8])

        def set_date_format_count(self, v: core.Map) -> None:
            self._set(self.type_.generated_offsets[8], v)

        def enumerable_count(self) -> core.Map:
            return self._get(self.type_.generated_offsets[9])

        def set_enumerable_count(self, v: core.Map) -> None:
            self._set(self.type_.generated_offsets[9], v)

        def profile(self) -> util.Gaussian:
            return self._get(self.type_.generated_offsets[10])

        def set_profile(self, v: util.Gaussian) -> None:
            self._set(self.type_.generated_offsets[10], v)

    @final
    class FileWalker(GreyCat.Object):
        name_: Final[str] = "io::FileWalker"

        def __init__(self, path: str, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[62]
            attributes: list = [path]
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

        def path(self) -> str:
            return self._get(self.type_.generated_offsets[0])

        def set_path(self, v: str) -> None:
            self._set(self.type_.generated_offsets[0], v)

    @final
    class HttpResponse(Generic[__T], GreyCat.Object):
        name_: Final[str] = "io::HttpResponse"

        def __init__(self, status_code: int, headers: core.Map, content: io.__T, error_msg: str, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[63]
            attributes: list = [status_code, headers, content, error_msg]
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

        def status_code(self) -> int:
            return self._get(self.type_.generated_offsets[0])

        def set_status_code(self, v: int) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def headers(self) -> core.Map:
            return self._get(self.type_.generated_offsets[1])

        def set_headers(self, v: core.Map) -> None:
            self._set(self.type_.generated_offsets[1], v)

        def content(self) -> io.__T:
            return self._get(self.type_.generated_offsets[2])

        def set_content(self, v: io.__T) -> None:
            self._set(self.type_.generated_offsets[2], v)

        def error_msg(self) -> str:
            return self._get(self.type_.generated_offsets[3])

        def set_error_msg(self, v: str) -> None:
            self._set(self.type_.generated_offsets[3], v)

    @final
    class JsonWriter(Generic[__T], GreyCat.Object):
        name_: Final[str] = "io::JsonWriter"

        def __init__(self, path: str, append: bool, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[64]
            attributes: list = [path, append]
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

        def path(self) -> str:
            return self._get(self.type_.generated_offsets[0])

        def set_path(self, v: str) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def append(self) -> bool:
            return self._get(self.type_.generated_offsets[1])

        def set_append(self, v: bool) -> None:
            self._set(self.type_.generated_offsets[1], v)

    @final
    class Json(Generic[__T], GreyCat.Object):
        name_: Final[str] = "io::Json"

        def __init__(self, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[65]
            attributes: list = []
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

    @final
    class CsvSharding(GreyCat.Object):
        name_: Final[str] = "io::CsvSharding"

        def __init__(self, id: int, column: int, modulo: int, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[66]
            attributes: list = [id, column, modulo]
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

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

    @final
    class Csv(GreyCat.Object):
        name_: Final[str] = "io::Csv"

        def __init__(self, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[67]
            attributes: list = []
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

        @staticmethod
        def sample(reader: io.CsvReader, max_lines: int, __greycat: Optional[GreyCat] = None) -> core.Table:
            if __greycat is None:
                __greycat  = GreyCat._DEFAULT
            return __greycat.call("io::Csv::sample", [reader, max_lines, ])

        @staticmethod
        def analyze(files: core.Array, config: io.CsvAnalysisConfig, __greycat: Optional[GreyCat] = None) -> io.CsvStatistics:
            if __greycat is None:
                __greycat  = GreyCat._DEFAULT
            return __greycat.call("io::Csv::analyze", [files, config, ])

        @staticmethod
        def generate(stats: io.CsvStatistics, __greycat: Optional[GreyCat] = None) -> str:
            if __greycat is None:
                __greycat  = GreyCat._DEFAULT
            return __greycat.call("io::Csv::generate", [stats, ])

    @final
    class Writer(Generic[__T], GreyCat.Object):
        name_: Final[str] = "io::Writer"

        def __init__(self, path: str, append: bool, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[68]
            attributes: list = [path, append]
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

        def path(self) -> str:
            return self._get(self.type_.generated_offsets[0])

        def set_path(self, v: str) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def append(self) -> bool:
            return self._get(self.type_.generated_offsets[1])

        def set_append(self, v: bool) -> None:
            self._set(self.type_.generated_offsets[1], v)

    @final
    class JsonReader(Generic[__T], GreyCat.Object):
        name_: Final[str] = "io::JsonReader"

        def __init__(self, path: str, pos: int, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[69]
            attributes: list = [path, pos]
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

        def path(self) -> str:
            return self._get(self.type_.generated_offsets[0])

        def set_path(self, v: str) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def pos(self) -> int:
            return self._get(self.type_.generated_offsets[1])

        def set_pos(self, v: int) -> None:
            self._set(self.type_.generated_offsets[1], v)

    @final
    class CsvReader(Generic[__T], GreyCat.Object):
        name_: Final[str] = "io::CsvReader"

        def __init__(self, path: str, pos: int, format: io.CsvFormat, sharding: io.CsvSharding, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[70]
            attributes: list = [path, pos, format, sharding]
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

        def path(self) -> str:
            return self._get(self.type_.generated_offsets[0])

        def set_path(self, v: str) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def pos(self) -> int:
            return self._get(self.type_.generated_offsets[1])

        def set_pos(self, v: int) -> None:
            self._set(self.type_.generated_offsets[1], v)

        def format(self) -> io.CsvFormat:
            return self._get(self.type_.generated_offsets[2])

        def set_format(self, v: io.CsvFormat) -> None:
            self._set(self.type_.generated_offsets[2], v)

        def sharding(self) -> io.CsvSharding:
            return self._get(self.type_.generated_offsets[3])

        def set_sharding(self, v: io.CsvSharding) -> None:
            self._set(self.type_.generated_offsets[3], v)

    @final
    class XmlReader(Generic[__T], GreyCat.Object):
        name_: Final[str] = "io::XmlReader"

        def __init__(self, path: str, pos: int, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[71]
            attributes: list = [path, pos]
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

        def path(self) -> str:
            return self._get(self.type_.generated_offsets[0])

        def set_path(self, v: str) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def pos(self) -> int:
            return self._get(self.type_.generated_offsets[1])

        def set_pos(self, v: int) -> None:
            self._set(self.type_.generated_offsets[1], v)

    @final
    class Http(Generic[__T], GreyCat.Object):
        name_: Final[str] = "io::Http"

        def __init__(self, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[72]
            attributes: list = []
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

    @final
    class GcbWriter(Generic[__T], GreyCat.Object):
        name_: Final[str] = "io::GcbWriter"

        def __init__(self, path: str, append: bool, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[73]
            attributes: list = [path, append]
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

        def path(self) -> str:
            return self._get(self.type_.generated_offsets[0])

        def set_path(self, v: str) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def append(self) -> bool:
            return self._get(self.type_.generated_offsets[1])

        def set_append(self, v: bool) -> None:
            self._set(self.type_.generated_offsets[1], v)

    @final
    class HttpRequest(GreyCat.Object):
        name_: Final[str] = "io::HttpRequest"

        def __init__(self, method: io.HttpMethod, url: str, headers: core.Map, body: str, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[74]
            attributes: list = [method, url, headers, body]
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

        def method(self) -> io.HttpMethod:
            return self._get(self.type_.generated_offsets[0])

        def set_method(self, v: io.HttpMethod) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def url(self) -> str:
            return self._get(self.type_.generated_offsets[1])

        def set_url(self, v: str) -> None:
            self._set(self.type_.generated_offsets[1], v)

        def headers(self) -> core.Map:
            return self._get(self.type_.generated_offsets[2])

        def set_headers(self, v: core.Map) -> None:
            self._set(self.type_.generated_offsets[2], v)

        def body(self) -> str:
            return self._get(self.type_.generated_offsets[3])

        def set_body(self, v: str) -> None:
            self._set(self.type_.generated_offsets[3], v)

    @final
    class CsvFormat(GreyCat.Object):
        name_: Final[str] = "io::CsvFormat"

        def __init__(self, header_lines: int, separator: c_char, string_delimiter: c_char, decimal_separator: c_char, thousands_separator: c_char, trim: bool, format: str, tz: core.TimeZone, strict: bool, nearest_time: bool, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[75]
            attributes: list = [header_lines, separator, string_delimiter, decimal_separator, thousands_separator, trim, format, tz, strict, nearest_time]
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

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

        def trim(self) -> bool:
            return self._get(self.type_.generated_offsets[5])

        def set_trim(self, v: bool) -> None:
            self._set(self.type_.generated_offsets[5], v)

        def format(self) -> str:
            return self._get(self.type_.generated_offsets[6])

        def set_format(self, v: str) -> None:
            self._set(self.type_.generated_offsets[6], v)

        def tz(self) -> core.TimeZone:
            return self._get(self.type_.generated_offsets[7])

        def set_tz(self, v: core.TimeZone) -> None:
            self._set(self.type_.generated_offsets[7], v)

        def strict(self) -> bool:
            return self._get(self.type_.generated_offsets[8])

        def set_strict(self, v: bool) -> None:
            self._set(self.type_.generated_offsets[8], v)

        def nearest_time(self) -> bool:
            return self._get(self.type_.generated_offsets[9])

        def set_nearest_time(self, v: bool) -> None:
            self._set(self.type_.generated_offsets[9], v)

    @final
    class File(GreyCat.Object):
        name_: Final[str] = "io::File"

        def __init__(self, path: str, size: int, last_modification: core.time, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[76]
            attributes: list = [path, size, last_modification]
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

        def path(self) -> str:
            return self._get(self.type_.generated_offsets[0])

        def set_path(self, v: str) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def size(self) -> int:
            return self._get(self.type_.generated_offsets[1])

        def set_size(self, v: int) -> None:
            self._set(self.type_.generated_offsets[1], v)

        def last_modification(self) -> core.time:
            return self._get(self.type_.generated_offsets[2])

        def set_last_modification(self, v: core.time) -> None:
            self._set(self.type_.generated_offsets[2], v)


@final
class runtime:
    __T = TypeVar("__T")

    @final
    class Role(GreyCat.Object):
        name_: Final[str] = "runtime::Role"

        def __init__(self, name: str, permissions: core.Array, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[77]
            attributes: list = [name, permissions]
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

        def name(self) -> str:
            return self._get(self.type_.generated_offsets[0])

        def set_name(self, v: str) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def permissions(self) -> core.Array:
            return self._get(self.type_.generated_offsets[1])

        def set_permissions(self, v: core.Array) -> None:
            self._set(self.type_.generated_offsets[1], v)

        @staticmethod
        def all(__greycat: Optional[GreyCat] = None) -> core.Array:
            if __greycat is None:
                __greycat  = GreyCat._DEFAULT
            return __greycat.call("runtime::Role::all")

    @final
    class Month(GreyCat.Enum):
        name_: Final[str] = "runtime::Month"
        __indices_by_values: dict[str, int] = {
            "Jan": 0,
            "Feb": 1,
            "Mar": 2,
            "Apr": 3,
            "May": 4,
            "Jun": 5,
            "Jul": 6,
            "Aug": 7,
            "Sep": 8,
            "Oct": 9,
            "Nov": 10,
            "Dec": 11,
        }

        def __init__(self, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[78]
            attributes: list = []
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

        def __class_getitem__(cls, key) -> runtime.Month:
            greycat: GreyCat
            if isinstance(key, tuple):
                key, greycat = key
            else:
                greycat = GreyCat._DEFAULT
            t: Final[GreyCat.Type] = greycat.libs_by_name[_std._name].mapped[78]
            return t.enum_values[t.generated_offsets[runtime.Month.__indices_by_values[key]]]

    @final
    class Runtime(GreyCat.Object):
        name_: Final[str] = "runtime::Runtime"

        def __init__(self, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[79]
            attributes: list = []
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

        @staticmethod
        def root(__greycat: Optional[GreyCat] = None) -> Any:
            if __greycat is None:
                __greycat  = GreyCat._DEFAULT
            return __greycat.call("runtime::Runtime::root")

        @staticmethod
        def abi(__greycat: Optional[GreyCat] = None) -> None:
            if __greycat is None:
                __greycat  = GreyCat._DEFAULT
            return __greycat.call("runtime::Runtime::abi")

        @staticmethod
        def info(__greycat: Optional[GreyCat] = None) -> runtime.RuntimeInfo:
            if __greycat is None:
                __greycat  = GreyCat._DEFAULT
            return __greycat.call("runtime::Runtime::info")

    @final
    class FixedPeriodicity(GreyCat.Object):
        name_: Final[str] = "runtime::FixedPeriodicity"

        def __init__(self, every: core.duration, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[80]
            attributes: list = [every]
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

        def every(self) -> core.duration:
            return self._get(self.type_.generated_offsets[0])

        def set_every(self, v: core.duration) -> None:
            self._set(self.type_.generated_offsets[0], v)

    @final
    class DateTuple(GreyCat.Object):
        name_: Final[str] = "runtime::DateTuple"

        def __init__(self, day: int, month: runtime.Month, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[81]
            attributes: list = [day, month]
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

        def day(self) -> int:
            return self._get(self.type_.generated_offsets[0])

        def set_day(self, v: int) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def month(self) -> runtime.Month:
            return self._get(self.type_.generated_offsets[1])

        def set_month(self, v: runtime.Month) -> None:
            self._set(self.type_.generated_offsets[1], v)

    @final
    class Frame(GreyCat.Object):
        name_: Final[str] = "runtime::Frame"

        def __init__(self, module: str, type: str, function: str, src: str, line: int, column: int, scope: core.Array, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[82]
            attributes: list = [module, type, function, src, line, column, scope]
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

        def module(self) -> str:
            return self._get(self.type_.generated_offsets[0])

        def set_module(self, v: str) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def type(self) -> str:
            return self._get(self.type_.generated_offsets[1])

        def set_type(self, v: str) -> None:
            self._set(self.type_.generated_offsets[1], v)

        def function(self) -> str:
            return self._get(self.type_.generated_offsets[2])

        def set_function(self, v: str) -> None:
            self._set(self.type_.generated_offsets[2], v)

        def src(self) -> str:
            return self._get(self.type_.generated_offsets[3])

        def set_src(self, v: str) -> None:
            self._set(self.type_.generated_offsets[3], v)

        def line(self) -> int:
            return self._get(self.type_.generated_offsets[4])

        def set_line(self, v: int) -> None:
            self._set(self.type_.generated_offsets[4], v)

        def column(self) -> int:
            return self._get(self.type_.generated_offsets[5])

        def set_column(self, v: int) -> None:
            self._set(self.type_.generated_offsets[5], v)

        def scope(self) -> core.Array:
            return self._get(self.type_.generated_offsets[6])

        def set_scope(self, v: core.Array) -> None:
            self._set(self.type_.generated_offsets[6], v)

    @final
    class Log(GreyCat.Object):
        name_: Final[str] = "runtime::Log"

        def __init__(self, level: runtime.LogLevel, time: core.time, user_id: int, id: int, id2: int, src: core.function, data: Any, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[83]
            attributes: list = [level, time, user_id, id, id2, src, data]
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

        def level(self) -> runtime.LogLevel:
            return self._get(self.type_.generated_offsets[0])

        def set_level(self, v: runtime.LogLevel) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def time(self) -> core.time:
            return self._get(self.type_.generated_offsets[1])

        def set_time(self, v: core.time) -> None:
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

        def src(self) -> core.function:
            return self._get(self.type_.generated_offsets[5])

        def set_src(self, v: core.function) -> None:
            self._set(self.type_.generated_offsets[5], v)

        def data(self) -> Any:
            return self._get(self.type_.generated_offsets[6])

        def set_data(self, v: Any) -> None:
            self._set(self.type_.generated_offsets[6], v)

    @final
    class MediaTypeObject(GreyCat.Object):
        name_: Final[str] = "runtime::MediaTypeObject"

        def __init__(self, schema: runtime.SchemaObject, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[84]
            attributes: list = [schema]
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

        def schema(self) -> runtime.SchemaObject:
            return self._get(self.type_.generated_offsets[0])

        def set_schema(self, v: runtime.SchemaObject) -> None:
            self._set(self.type_.generated_offsets[0], v)

    @final
    class UserGroupPolicyType(GreyCat.Enum):
        name_: Final[str] = "runtime::UserGroupPolicyType"
        __indices_by_values: dict[str, int] = {
            "read": 0,
            "write": 1,
            "execute": 2,
        }

        def __init__(self, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[85]
            attributes: list = []
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

        def __class_getitem__(cls, key) -> runtime.UserGroupPolicyType:
            greycat: GreyCat
            if isinstance(key, tuple):
                key, greycat = key
            else:
                greycat = GreyCat._DEFAULT
            t: Final[GreyCat.Type] = greycat.libs_by_name[_std._name].mapped[85]
            return t.enum_values[t.generated_offsets[runtime.UserGroupPolicyType.__indices_by_values[key]]]

    @final
    class SecurityEntity(GreyCat.Object):
        name_: Final[str] = "runtime::SecurityEntity"

        def __init__(self, id: int, name: str, activated: bool, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[86]
            attributes: list = [id, name, activated]
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

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
        def set(entity: runtime.SecurityEntity, __greycat: Optional[GreyCat] = None) -> int:
            if __greycat is None:
                __greycat  = GreyCat._DEFAULT
            return __greycat.call("runtime::SecurityEntity::set", [entity, ])

        @staticmethod
        def all(__greycat: Optional[GreyCat] = None) -> core.Array:
            if __greycat is None:
                __greycat  = GreyCat._DEFAULT
            return __greycat.call("runtime::SecurityEntity::all")

    @final
    class RequestBodyObject(GreyCat.Object):
        name_: Final[str] = "runtime::RequestBodyObject"

        def __init__(self, content: core.Map, required: bool, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[87]
            attributes: list = [content, required]
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

        def content(self) -> core.Map:
            return self._get(self.type_.generated_offsets[0])

        def set_content(self, v: core.Map) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def required(self) -> bool:
            return self._get(self.type_.generated_offsets[1])

        def set_required(self, v: bool) -> None:
            self._set(self.type_.generated_offsets[1], v)

    @final
    class OperationObject(GreyCat.Object):
        name_: Final[str] = "runtime::OperationObject"

        def __init__(self, requestBody: runtime.RequestBodyObject, responses: core.Map, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[88]
            attributes: list = [requestBody, responses]
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

        def requestBody(self) -> runtime.RequestBodyObject:
            return self._get(self.type_.generated_offsets[0])

        def set_requestBody(self, v: runtime.RequestBodyObject) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def responses(self) -> core.Map:
            return self._get(self.type_.generated_offsets[1])

        def set_responses(self, v: core.Map) -> None:
            self._set(self.type_.generated_offsets[1], v)

    @final
    class ResponseObject(GreyCat.Object):
        name_: Final[str] = "runtime::ResponseObject"

        def __init__(self, description: str, headers: core.Map, content: core.Map, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[89]
            attributes: list = [description, headers, content]
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

        def description(self) -> str:
            return self._get(self.type_.generated_offsets[0])

        def set_description(self, v: str) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def headers(self) -> core.Map:
            return self._get(self.type_.generated_offsets[1])

        def set_headers(self, v: core.Map) -> None:
            self._set(self.type_.generated_offsets[1], v)

        def content(self) -> core.Map:
            return self._get(self.type_.generated_offsets[2])

        def set_content(self, v: core.Map) -> None:
            self._set(self.type_.generated_offsets[2], v)

    @final
    class UserCredential(GreyCat.Object):
        name_: Final[str] = "runtime::UserCredential"

        def __init__(self, offset: int, pass_: str, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[90]
            attributes: list = [offset, pass_]
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

        def offset(self) -> int:
            return self._get(self.type_.generated_offsets[0])

        def set_offset(self, v: int) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def pass_(self) -> str:
            return self._get(self.type_.generated_offsets[1])

        def set_pass_(self, v: str) -> None:
            self._set(self.type_.generated_offsets[1], v)

    @final
    class TaskStatus(GreyCat.Enum):
        name_: Final[str] = "runtime::TaskStatus"
        __indices_by_values: dict[str, int] = {
            "empty": 0,
            "waiting": 1,
            "running": 2,
            "await_": 3,
            "cancelled": 4,
            "error": 5,
            "ended": 6,
            "ended_with_errors": 7,
            "breakpoint": 8,
        }

        def __init__(self, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[91]
            attributes: list = []
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

        def __class_getitem__(cls, key) -> runtime.TaskStatus:
            greycat: GreyCat
            if isinstance(key, tuple):
                key, greycat = key
            else:
                greycat = GreyCat._DEFAULT
            t: Final[GreyCat.Type] = greycat.libs_by_name[_std._name].mapped[91]
            return t.enum_values[t.generated_offsets[runtime.TaskStatus.__indices_by_values[key]]]

    @final
    class DayOfWeek(GreyCat.Enum):
        name_: Final[str] = "runtime::DayOfWeek"
        __indices_by_values: dict[str, int] = {
            "Mon": 0,
            "Tue": 1,
            "Wed": 2,
            "Thu": 3,
            "Fri": 4,
            "Sat": 5,
            "Sun": 6,
        }

        def __init__(self, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[92]
            attributes: list = []
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

        def __class_getitem__(cls, key) -> runtime.DayOfWeek:
            greycat: GreyCat
            if isinstance(key, tuple):
                key, greycat = key
            else:
                greycat = GreyCat._DEFAULT
            t: Final[GreyCat.Type] = greycat.libs_by_name[_std._name].mapped[92]
            return t.enum_values[t.generated_offsets[runtime.DayOfWeek.__indices_by_values[key]]]

    @final
    class UserGroup(GreyCat.Object):
        name_: Final[str] = "runtime::UserGroup"

        def __init__(self, id: int, name: str, activated: bool, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[93]
            attributes: list = [id, name, activated]
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

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

    @final
    class PathItemObject(GreyCat.Object):
        name_: Final[str] = "runtime::PathItemObject"

        def __init__(self, description: str, post: runtime.OperationObject, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[94]
            attributes: list = [description, post]
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

        def description(self) -> str:
            return self._get(self.type_.generated_offsets[0])

        def set_description(self, v: str) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def post(self) -> runtime.OperationObject:
            return self._get(self.type_.generated_offsets[1])

        def set_post(self, v: runtime.OperationObject) -> None:
            self._set(self.type_.generated_offsets[1], v)

    @final
    class SecurityPolicy(GreyCat.Object):
        name_: Final[str] = "runtime::SecurityPolicy"

        def __init__(self, entities: core.Array, credentials: core.Map, fields: runtime.SecurityFields, keys: core.Map, keys_last_refresh: core.time, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[95]
            attributes: list = [entities, credentials, fields, keys, keys_last_refresh]
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

        def entities(self) -> core.Array:
            return self._get(self.type_.generated_offsets[0])

        def set_entities(self, v: core.Array) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def credentials(self) -> core.Map:
            return self._get(self.type_.generated_offsets[1])

        def set_credentials(self, v: core.Map) -> None:
            self._set(self.type_.generated_offsets[1], v)

        def fields(self) -> runtime.SecurityFields:
            return self._get(self.type_.generated_offsets[2])

        def set_fields(self, v: runtime.SecurityFields) -> None:
            self._set(self.type_.generated_offsets[2], v)

        def keys(self) -> core.Map:
            return self._get(self.type_.generated_offsets[3])

        def set_keys(self, v: core.Map) -> None:
            self._set(self.type_.generated_offsets[3], v)

        def keys_last_refresh(self) -> core.time:
            return self._get(self.type_.generated_offsets[4])

        def set_keys_last_refresh(self, v: core.time) -> None:
            self._set(self.type_.generated_offsets[4], v)

    @final
    class OpenIDConnect(GreyCat.Object):
        name_: Final[str] = "runtime::OpenIDConnect"

        def __init__(self, url: str, clientId: str, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[96]
            attributes: list = [url, clientId]
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

        def url(self) -> str:
            return self._get(self.type_.generated_offsets[0])

        def set_url(self, v: str) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def clientId(self) -> str:
            return self._get(self.type_.generated_offsets[1])

        def set_clientId(self, v: str) -> None:
            self._set(self.type_.generated_offsets[1], v)

        @staticmethod
        def config(__greycat: Optional[GreyCat] = None) -> runtime.OpenIDConnect:
            if __greycat is None:
                __greycat  = GreyCat._DEFAULT
            return __greycat.call("runtime::OpenIDConnect::config")

    @final
    class Debug(GreyCat.Object):
        name_: Final[str] = "runtime::Debug"

        def __init__(self, id: int, frames: core.Array, root: Any, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[97]
            attributes: list = [id, frames, root]
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

        def id(self) -> int:
            return self._get(self.type_.generated_offsets[0])

        def set_id(self, v: int) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def frames(self) -> core.Array:
            return self._get(self.type_.generated_offsets[1])

        def set_frames(self, v: core.Array) -> None:
            self._set(self.type_.generated_offsets[1], v)

        def root(self) -> Any:
            return self._get(self.type_.generated_offsets[2])

        def set_root(self, v: Any) -> None:
            self._set(self.type_.generated_offsets[2], v)

        @staticmethod
        def resume(id: int, __greycat: Optional[GreyCat] = None) -> None:
            if __greycat is None:
                __greycat  = GreyCat._DEFAULT
            return __greycat.call("runtime::Debug::resume", [id, ])

        @staticmethod
        def get(id: int, __greycat: Optional[GreyCat] = None) -> runtime.Debug:
            if __greycat is None:
                __greycat  = GreyCat._DEFAULT
            return __greycat.call("runtime::Debug::get", [id, ])

        @staticmethod
        def all(__greycat: Optional[GreyCat] = None) -> core.Array:
            if __greycat is None:
                __greycat  = GreyCat._DEFAULT
            return __greycat.call("runtime::Debug::all")

    @final
    class YearlyPeriodicity(GreyCat.Object):
        name_: Final[str] = "runtime::YearlyPeriodicity"

        def __init__(self, dates: core.Array, timezone: core.TimeZone, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[98]
            attributes: list = [dates, timezone]
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

        def dates(self) -> core.Array:
            return self._get(self.type_.generated_offsets[0])

        def set_dates(self, v: core.Array) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def timezone(self) -> core.TimeZone:
            return self._get(self.type_.generated_offsets[1])

        def set_timezone(self, v: core.TimeZone) -> None:
            self._set(self.type_.generated_offsets[1], v)

    @final
    class OpenApi(GreyCat.Object):
        name_: Final[str] = "runtime::OpenApi"

        def __init__(self, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[99]
            attributes: list = []
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

        @staticmethod
        def v3(__greycat: Optional[GreyCat] = None) -> runtime.OpenApiV3:
            if __greycat is None:
                __greycat  = GreyCat._DEFAULT
            return __greycat.call("runtime::OpenApi::v3")

    @final
    class License(GreyCat.Object):
        name_: Final[str] = "runtime::License"

        def __init__(self, name: str, start: core.time, end: core.time, company: str, max_memory: int, extra_1: int, extra_2: int, type: runtime.LicenseType, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[100]
            attributes: list = [name, start, end, company, max_memory, extra_1, extra_2, type]
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

        def name(self) -> str:
            return self._get(self.type_.generated_offsets[0])

        def set_name(self, v: str) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def start(self) -> core.time:
            return self._get(self.type_.generated_offsets[1])

        def set_start(self, v: core.time) -> None:
            self._set(self.type_.generated_offsets[1], v)

        def end(self) -> core.time:
            return self._get(self.type_.generated_offsets[2])

        def set_end(self, v: core.time) -> None:
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

        def type(self) -> runtime.LicenseType:
            return self._get(self.type_.generated_offsets[7])

        def set_type(self, v: runtime.LicenseType) -> None:
            self._set(self.type_.generated_offsets[7], v)

    @final
    class ComponentsObject(GreyCat.Object):
        name_: Final[str] = "runtime::ComponentsObject"

        def __init__(self, schemas: core.Map, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[101]
            attributes: list = [schemas]
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

        def schemas(self) -> core.Map:
            return self._get(self.type_.generated_offsets[0])

        def set_schemas(self, v: core.Map) -> None:
            self._set(self.type_.generated_offsets[0], v)

    @final
    class UserGroupPolicy(GreyCat.Object):
        name_: Final[str] = "runtime::UserGroupPolicy"

        def __init__(self, group_id: int, type: runtime.UserGroupPolicyType, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[102]
            attributes: list = [group_id, type]
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

        def group_id(self) -> int:
            return self._get(self.type_.generated_offsets[0])

        def set_group_id(self, v: int) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def type(self) -> runtime.UserGroupPolicyType:
            return self._get(self.type_.generated_offsets[1])

        def set_type(self, v: runtime.UserGroupPolicyType) -> None:
            self._set(self.type_.generated_offsets[1], v)

    @final
    class MonthlyPeriodicity(GreyCat.Object):
        name_: Final[str] = "runtime::MonthlyPeriodicity"

        def __init__(self, days: core.Array, daily: runtime.DailyPeriodicity, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[103]
            attributes: list = [days, daily]
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

        def days(self) -> core.Array:
            return self._get(self.type_.generated_offsets[0])

        def set_days(self, v: core.Array) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def daily(self) -> runtime.DailyPeriodicity:
            return self._get(self.type_.generated_offsets[1])

        def set_daily(self, v: runtime.DailyPeriodicity) -> None:
            self._set(self.type_.generated_offsets[1], v)

    @final
    class ResponseCode(GreyCat.Enum):
        name_: Final[str] = "runtime::ResponseCode"
        __indices_by_values: dict[str, int] = {
            "200": 0,
            "400": 1,
            "404": 2,
        }

        def __init__(self, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[104]
            attributes: list = []
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

        def __class_getitem__(cls, key) -> runtime.ResponseCode:
            greycat: GreyCat
            if isinstance(key, tuple):
                key, greycat = key
            else:
                greycat = GreyCat._DEFAULT
            t: Final[GreyCat.Type] = greycat.libs_by_name[_std._name].mapped[104]
            return t.enum_values[t.generated_offsets[runtime.ResponseCode.__indices_by_values[key]]]

    @final
    class OpenApiVersion(GreyCat.Enum):
        name_: Final[str] = "runtime::OpenApiVersion"
        __indices_by_values: dict[str, int] = {
            "3.0.4": 0,
        }

        def __init__(self, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[105]
            attributes: list = []
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

        def __class_getitem__(cls, key) -> runtime.OpenApiVersion:
            greycat: GreyCat
            if isinstance(key, tuple):
                key, greycat = key
            else:
                greycat = GreyCat._DEFAULT
            t: Final[GreyCat.Type] = greycat.libs_by_name[_std._name].mapped[105]
            return t.enum_values[t.generated_offsets[runtime.OpenApiVersion.__indices_by_values[key]]]

    @final
    class Variable(GreyCat.Object):
        name_: Final[str] = "runtime::Variable"

        def __init__(self, name: str, value: Any, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[106]
            attributes: list = [name, value]
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

        def name(self) -> str:
            return self._get(self.type_.generated_offsets[0])

        def set_name(self, v: str) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def value(self) -> Any:
            return self._get(self.type_.generated_offsets[1])

        def set_value(self, v: Any) -> None:
            self._set(self.type_.generated_offsets[1], v)

    @final
    class MergeStrategy(GreyCat.Enum):
        name_: Final[str] = "runtime::MergeStrategy"
        __indices_by_values: dict[str, int] = {
            "strict": 0,
            "first_wins": 1,
            "last_wins": 2,
        }

        def __init__(self, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[107]
            attributes: list = []
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

        def __class_getitem__(cls, key) -> runtime.MergeStrategy:
            greycat: GreyCat
            if isinstance(key, tuple):
                key, greycat = key
            else:
                greycat = GreyCat._DEFAULT
            t: Final[GreyCat.Type] = greycat.libs_by_name[_std._name].mapped[107]
            return t.enum_values[t.generated_offsets[runtime.MergeStrategy.__indices_by_values[key]]]

    @final
    class InfoObject(GreyCat.Object):
        name_: Final[str] = "runtime::InfoObject"

        def __init__(self, title: str, version: str, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[108]
            attributes: list = [title, version]
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

        def title(self) -> str:
            return self._get(self.type_.generated_offsets[0])

        def set_title(self, v: str) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def version(self) -> str:
            return self._get(self.type_.generated_offsets[1])

        def set_version(self, v: str) -> None:
            self._set(self.type_.generated_offsets[1], v)

    @final
    class DailyPeriodicity(GreyCat.Object):
        name_: Final[str] = "runtime::DailyPeriodicity"

        def __init__(self, hour: int, minute: int, second: int, timezone: core.TimeZone, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[109]
            attributes: list = [hour, minute, second, timezone]
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

        def hour(self) -> int:
            return self._get(self.type_.generated_offsets[0])

        def set_hour(self, v: int) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def minute(self) -> int:
            return self._get(self.type_.generated_offsets[1])

        def set_minute(self, v: int) -> None:
            self._set(self.type_.generated_offsets[1], v)

        def second(self) -> int:
            return self._get(self.type_.generated_offsets[2])

        def set_second(self, v: int) -> None:
            self._set(self.type_.generated_offsets[2], v)

        def timezone(self) -> core.TimeZone:
            return self._get(self.type_.generated_offsets[3])

        def set_timezone(self, v: core.TimeZone) -> None:
            self._set(self.type_.generated_offsets[3], v)

    @final
    class LicenseType(GreyCat.Enum):
        name_: Final[str] = "runtime::LicenseType"
        __indices_by_values: dict[str, int] = {
            "community": 0,
            "enterprise": 1,
            "testing": 2,
        }

        def __init__(self, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[110]
            attributes: list = []
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

        def __class_getitem__(cls, key) -> runtime.LicenseType:
            greycat: GreyCat
            if isinstance(key, tuple):
                key, greycat = key
            else:
                greycat = GreyCat._DEFAULT
            t: Final[GreyCat.Type] = greycat.libs_by_name[_std._name].mapped[110]
            return t.enum_values[t.generated_offsets[runtime.LicenseType.__indices_by_values[key]]]

    @final
    class Scheduler(GreyCat.Object):
        name_: Final[str] = "runtime::Scheduler"

        def __init__(self, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[111]
            attributes: list = []
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

        @staticmethod
        def deactivate(function: core.function, __greycat: Optional[GreyCat] = None) -> bool:
            if __greycat is None:
                __greycat  = GreyCat._DEFAULT
            return __greycat.call("runtime::Scheduler::deactivate", [function, ])

        @staticmethod
        def activate(function: core.function, __greycat: Optional[GreyCat] = None) -> bool:
            if __greycat is None:
                __greycat  = GreyCat._DEFAULT
            return __greycat.call("runtime::Scheduler::activate", [function, ])

        @staticmethod
        def find(function: core.function, __greycat: Optional[GreyCat] = None) -> runtime.PeriodicTask:
            if __greycat is None:
                __greycat  = GreyCat._DEFAULT
            return __greycat.call("runtime::Scheduler::find", [function, ])

        @staticmethod
        def list(__greycat: Optional[GreyCat] = None) -> core.Array:
            if __greycat is None:
                __greycat  = GreyCat._DEFAULT
            return __greycat.call("runtime::Scheduler::list")

        @staticmethod
        def add(function: core.function, periodicity: runtime.Periodicity, options: runtime.PeriodicOptions, __greycat: Optional[GreyCat] = None) -> None:
            if __greycat is None:
                __greycat  = GreyCat._DEFAULT
            return __greycat.call("runtime::Scheduler::add", [function, periodicity, options, ])

    @final
    class PeriodicOptions(GreyCat.Object):
        name_: Final[str] = "runtime::PeriodicOptions"

        def __init__(self, activated: bool, start: core.time, max_duration: core.duration, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[112]
            attributes: list = [activated, start, max_duration]
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

        def activated(self) -> bool:
            return self._get(self.type_.generated_offsets[0])

        def set_activated(self, v: bool) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def start(self) -> core.time:
            return self._get(self.type_.generated_offsets[1])

        def set_start(self, v: core.time) -> None:
            self._set(self.type_.generated_offsets[1], v)

        def max_duration(self) -> core.duration:
            return self._get(self.type_.generated_offsets[2])

        def set_max_duration(self, v: core.duration) -> None:
            self._set(self.type_.generated_offsets[2], v)

    @final
    class HeaderObject(GreyCat.Object):
        name_: Final[str] = "runtime::HeaderObject"

        def __init__(self, description: str, required: bool, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[113]
            attributes: list = [description, required]
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

        def description(self) -> str:
            return self._get(self.type_.generated_offsets[0])

        def set_description(self, v: str) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def required(self) -> bool:
            return self._get(self.type_.generated_offsets[1])

        def set_required(self, v: bool) -> None:
            self._set(self.type_.generated_offsets[1], v)

    @final
    class ChildProcess(GreyCat.Object):
        name_: Final[str] = "runtime::ChildProcess"

        def __init__(self, pid: int, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[114]
            attributes: list = [pid]
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

        def pid(self) -> int:
            return self._get(self.type_.generated_offsets[0])

        def set_pid(self, v: int) -> None:
            self._set(self.type_.generated_offsets[0], v)

    @final
    class SchemaObject(GreyCat.Object):
        name_: Final[str] = "runtime::SchemaObject"

        def __init__(self, __ref: str, type: runtime.SchemaType, format: runtime.SchemaFormat, nullable: bool, properties: core.Map, required: core.Array, items: runtime.SchemaObject, oneOf: core.Array, allOf: core.Array, minItems: int, maxItems: int, enum: core.Array, additionalProperties: runtime.SchemaObject, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[115]
            attributes: list = [__ref, type, format, nullable, properties, required, items, oneOf, allOf, minItems, maxItems, enum, additionalProperties]
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

        def __ref(self) -> str:
            return self._get(self.type_.generated_offsets[0])

        def set___ref(self, v: str) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def type(self) -> runtime.SchemaType:
            return self._get(self.type_.generated_offsets[1])

        def set_type(self, v: runtime.SchemaType) -> None:
            self._set(self.type_.generated_offsets[1], v)

        def format(self) -> runtime.SchemaFormat:
            return self._get(self.type_.generated_offsets[2])

        def set_format(self, v: runtime.SchemaFormat) -> None:
            self._set(self.type_.generated_offsets[2], v)

        def nullable(self) -> bool:
            return self._get(self.type_.generated_offsets[3])

        def set_nullable(self, v: bool) -> None:
            self._set(self.type_.generated_offsets[3], v)

        def properties(self) -> core.Map:
            return self._get(self.type_.generated_offsets[4])

        def set_properties(self, v: core.Map) -> None:
            self._set(self.type_.generated_offsets[4], v)

        def required(self) -> core.Array:
            return self._get(self.type_.generated_offsets[5])

        def set_required(self, v: core.Array) -> None:
            self._set(self.type_.generated_offsets[5], v)

        def items(self) -> runtime.SchemaObject:
            return self._get(self.type_.generated_offsets[6])

        def set_items(self, v: runtime.SchemaObject) -> None:
            self._set(self.type_.generated_offsets[6], v)

        def oneOf(self) -> core.Array:
            return self._get(self.type_.generated_offsets[7])

        def set_oneOf(self, v: core.Array) -> None:
            self._set(self.type_.generated_offsets[7], v)

        def allOf(self) -> core.Array:
            return self._get(self.type_.generated_offsets[8])

        def set_allOf(self, v: core.Array) -> None:
            self._set(self.type_.generated_offsets[8], v)

        def minItems(self) -> int:
            return self._get(self.type_.generated_offsets[9])

        def set_minItems(self, v: int) -> None:
            self._set(self.type_.generated_offsets[9], v)

        def maxItems(self) -> int:
            return self._get(self.type_.generated_offsets[10])

        def set_maxItems(self, v: int) -> None:
            self._set(self.type_.generated_offsets[10], v)

        def enum(self) -> core.Array:
            return self._get(self.type_.generated_offsets[11])

        def set_enum(self, v: core.Array) -> None:
            self._set(self.type_.generated_offsets[11], v)

        def additionalProperties(self) -> runtime.SchemaObject:
            return self._get(self.type_.generated_offsets[12])

        def set_additionalProperties(self, v: runtime.SchemaObject) -> None:
            self._set(self.type_.generated_offsets[12], v)

    @final
    class Permission(GreyCat.Object):
        name_: Final[str] = "runtime::Permission"

        def __init__(self, name: str, description: str, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[116]
            attributes: list = [name, description]
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

        def name(self) -> str:
            return self._get(self.type_.generated_offsets[0])

        def set_name(self, v: str) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def description(self) -> str:
            return self._get(self.type_.generated_offsets[1])

        def set_description(self, v: str) -> None:
            self._set(self.type_.generated_offsets[1], v)

        @staticmethod
        def all(__greycat: Optional[GreyCat] = None) -> core.Array:
            if __greycat is None:
                __greycat  = GreyCat._DEFAULT
            return __greycat.call("runtime::Permission::all")

    @final
    class Task(GreyCat.Object):
        name_: Final[str] = "runtime::Task"

        def __init__(self, user_id: int, task_id: int, mod: str, type: str, fun: str, creation: core.time, start: core.time, duration: core.duration, status: runtime.TaskStatus, progress: float, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[117]
            attributes: list = [user_id, task_id, mod, type, fun, creation, start, duration, status, progress]
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

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

        def creation(self) -> core.time:
            return self._get(self.type_.generated_offsets[5])

        def set_creation(self, v: core.time) -> None:
            self._set(self.type_.generated_offsets[5], v)

        def start(self) -> core.time:
            return self._get(self.type_.generated_offsets[6])

        def set_start(self, v: core.time) -> None:
            self._set(self.type_.generated_offsets[6], v)

        def duration(self) -> core.duration:
            return self._get(self.type_.generated_offsets[7])

        def set_duration(self, v: core.duration) -> None:
            self._set(self.type_.generated_offsets[7], v)

        def status(self) -> runtime.TaskStatus:
            return self._get(self.type_.generated_offsets[8])

        def set_status(self, v: runtime.TaskStatus) -> None:
            self._set(self.type_.generated_offsets[8], v)

        def progress(self) -> float:
            return self._get(self.type_.generated_offsets[9])

        def set_progress(self, v: float) -> None:
            self._set(self.type_.generated_offsets[9], v)

        @staticmethod
        def is_running(task_id: int, __greycat: Optional[GreyCat] = None) -> bool:
            if __greycat is None:
                __greycat  = GreyCat._DEFAULT
            return __greycat.call("runtime::Task::is_running", [task_id, ])

        @staticmethod
        def cancel(task_id: int, __greycat: Optional[GreyCat] = None) -> bool:
            if __greycat is None:
                __greycat  = GreyCat._DEFAULT
            return __greycat.call("runtime::Task::cancel", [task_id, ])

        @staticmethod
        def history(offset: int, max: int, __greycat: Optional[GreyCat] = None) -> core.Array:
            if __greycat is None:
                __greycat  = GreyCat._DEFAULT
            return __greycat.call("runtime::Task::history", [offset, max, ])

        @staticmethod
        def running(__greycat: Optional[GreyCat] = None) -> core.Array:
            if __greycat is None:
                __greycat  = GreyCat._DEFAULT
            return __greycat.call("runtime::Task::running")

    @final
    class System(GreyCat.Object):
        name_: Final[str] = "runtime::System"

        def __init__(self, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[118]
            attributes: list = []
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

    @final
    class SecurityFields(GreyCat.Object):
        name_: Final[str] = "runtime::SecurityFields"

        def __init__(self, email: str, name: str, first_name: str, last_name: str, roles: core.Map, groups: core.Map, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[119]
            attributes: list = [email, name, first_name, last_name, roles, groups]
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

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

        def roles(self) -> core.Map:
            return self._get(self.type_.generated_offsets[4])

        def set_roles(self, v: core.Map) -> None:
            self._set(self.type_.generated_offsets[4], v)

        def groups(self) -> core.Map:
            return self._get(self.type_.generated_offsets[5])

        def set_groups(self, v: core.Map) -> None:
            self._set(self.type_.generated_offsets[5], v)

        @staticmethod
        def get(__greycat: Optional[GreyCat] = None) -> runtime.SecurityFields:
            if __greycat is None:
                __greycat  = GreyCat._DEFAULT
            return __greycat.call("runtime::SecurityFields::get")

        @staticmethod
        def set(f: runtime.SecurityFields, __greycat: Optional[GreyCat] = None) -> None:
            if __greycat is None:
                __greycat  = GreyCat._DEFAULT
            return __greycat.call("runtime::SecurityFields::set", [f, ])

    @final
    class LogDataUsage(GreyCat.Object):
        name_: Final[str] = "runtime::LogDataUsage"

        def __init__(self, read_bytes: int, read_hits: int, read_wasted: int, write_bytes: int, write_hits: int, cache_bytes: int, cache_hits: int, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[120]
            attributes: list = [read_bytes, read_hits, read_wasted, write_bytes, write_hits, cache_bytes, cache_hits]
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

        def read_bytes(self) -> int:
            return self._get(self.type_.generated_offsets[0])

        def set_read_bytes(self, v: int) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def read_hits(self) -> int:
            return self._get(self.type_.generated_offsets[1])

        def set_read_hits(self, v: int) -> None:
            self._set(self.type_.generated_offsets[1], v)

        def read_wasted(self) -> int:
            return self._get(self.type_.generated_offsets[2])

        def set_read_wasted(self, v: int) -> None:
            self._set(self.type_.generated_offsets[2], v)

        def write_bytes(self) -> int:
            return self._get(self.type_.generated_offsets[3])

        def set_write_bytes(self, v: int) -> None:
            self._set(self.type_.generated_offsets[3], v)

        def write_hits(self) -> int:
            return self._get(self.type_.generated_offsets[4])

        def set_write_hits(self, v: int) -> None:
            self._set(self.type_.generated_offsets[4], v)

        def cache_bytes(self) -> int:
            return self._get(self.type_.generated_offsets[5])

        def set_cache_bytes(self, v: int) -> None:
            self._set(self.type_.generated_offsets[5], v)

        def cache_hits(self) -> int:
            return self._get(self.type_.generated_offsets[6])

        def set_cache_hits(self, v: int) -> None:
            self._set(self.type_.generated_offsets[6], v)

    @final
    class LogLevel(GreyCat.Enum):
        name_: Final[str] = "runtime::LogLevel"
        __indices_by_values: dict[str, int] = {
            "error": 0,
            "warn": 1,
            "info": 2,
            "perf": 3,
            "trace": 4,
        }

        def __init__(self, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[121]
            attributes: list = []
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

        def __class_getitem__(cls, key) -> runtime.LogLevel:
            greycat: GreyCat
            if isinstance(key, tuple):
                key, greycat = key
            else:
                greycat = GreyCat._DEFAULT
            t: Final[GreyCat.Type] = greycat.libs_by_name[_std._name].mapped[121]
            return t.enum_values[t.generated_offsets[runtime.LogLevel.__indices_by_values[key]]]

    @final
    class PeriodicTask(GreyCat.Object):
        name_: Final[str] = "runtime::PeriodicTask"

        def __init__(self, function: core.function, periodicity: runtime.Periodicity, options: runtime.PeriodicOptions, is_active: bool, next_execution: core.time, execution_count: int, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[122]
            attributes: list = [function, periodicity, options, is_active, next_execution, execution_count]
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

        def function(self) -> core.function:
            return self._get(self.type_.generated_offsets[0])

        def set_function(self, v: core.function) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def periodicity(self) -> runtime.Periodicity:
            return self._get(self.type_.generated_offsets[1])

        def set_periodicity(self, v: runtime.Periodicity) -> None:
            self._set(self.type_.generated_offsets[1], v)

        def options(self) -> runtime.PeriodicOptions:
            return self._get(self.type_.generated_offsets[2])

        def set_options(self, v: runtime.PeriodicOptions) -> None:
            self._set(self.type_.generated_offsets[2], v)

        def is_active(self) -> bool:
            return self._get(self.type_.generated_offsets[3])

        def set_is_active(self, v: bool) -> None:
            self._set(self.type_.generated_offsets[3], v)

        def next_execution(self) -> core.time:
            return self._get(self.type_.generated_offsets[4])

        def set_next_execution(self, v: core.time) -> None:
            self._set(self.type_.generated_offsets[4], v)

        def execution_count(self) -> int:
            return self._get(self.type_.generated_offsets[5])

        def set_execution_count(self, v: int) -> None:
            self._set(self.type_.generated_offsets[5], v)

    @final
    class User(GreyCat.Object):
        name_: Final[str] = "runtime::User"

        def __init__(self, id: int, name: str, activated: bool, full_name: str, email: str, role: str, groups: core.Array, groups_flags: int, external: bool, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[123]
            attributes: list = [id, name, activated, full_name, email, role, groups, groups_flags, external]
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

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

        def groups(self) -> core.Array:
            return self._get(self.type_.generated_offsets[6])

        def set_groups(self, v: core.Array) -> None:
            self._set(self.type_.generated_offsets[6], v)

        def groups_flags(self) -> int:
            return self._get(self.type_.generated_offsets[7])

        def set_groups_flags(self, v: int) -> None:
            self._set(self.type_.generated_offsets[7], v)

        def external(self) -> bool:
            return self._get(self.type_.generated_offsets[8])

        def set_external(self, v: bool) -> None:
            self._set(self.type_.generated_offsets[8], v)

        @staticmethod
        def setPassword(name: str, pass_: str, __greycat: Optional[GreyCat] = None) -> bool:
            if __greycat is None:
                __greycat  = GreyCat._DEFAULT
            return __greycat.call("runtime::User::setPassword", [name, pass_, ])

        @staticmethod
        def permissions(__greycat: Optional[GreyCat] = None) -> core.Array:
            if __greycat is None:
                __greycat  = GreyCat._DEFAULT
            return __greycat.call("runtime::User::permissions")

        @staticmethod
        def me(__greycat: Optional[GreyCat] = None) -> runtime.User:
            if __greycat is None:
                __greycat  = GreyCat._DEFAULT
            return __greycat.call("runtime::User::me")

        @staticmethod
        def current(__greycat: Optional[GreyCat] = None) -> int:
            if __greycat is None:
                __greycat  = GreyCat._DEFAULT
            return __greycat.call("runtime::User::current")

        @staticmethod
        def renew(use_cookie: bool, __greycat: Optional[GreyCat] = None) -> str:
            if __greycat is None:
                __greycat  = GreyCat._DEFAULT
            return __greycat.call("runtime::User::renew", [use_cookie, ])

        @staticmethod
        def logout(__greycat: Optional[GreyCat] = None) -> None:
            if __greycat is None:
                __greycat  = GreyCat._DEFAULT
            return __greycat.call("runtime::User::logout")

        @staticmethod
        def tokenLogin(token: str, use_cookie: bool, __greycat: Optional[GreyCat] = None) -> str:
            if __greycat is None:
                __greycat  = GreyCat._DEFAULT
            return __greycat.call("runtime::User::tokenLogin", [token, use_cookie, ])

        @staticmethod
        def login(credentials: str, use_cookie: bool, __greycat: Optional[GreyCat] = None) -> str:
            if __greycat is None:
                __greycat  = GreyCat._DEFAULT
            return __greycat.call("runtime::User::login", [credentials, use_cookie, ])

    @final
    class OpenApiV3(GreyCat.Object):
        name_: Final[str] = "runtime::OpenApiV3"

        def __init__(self, openapi: runtime.OpenApiVersion, info: runtime.InfoObject, paths: core.Map, components: runtime.ComponentsObject, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[124]
            attributes: list = [openapi, info, paths, components]
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

        def openapi(self) -> runtime.OpenApiVersion:
            return self._get(self.type_.generated_offsets[0])

        def set_openapi(self, v: runtime.OpenApiVersion) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def info(self) -> runtime.InfoObject:
            return self._get(self.type_.generated_offsets[1])

        def set_info(self, v: runtime.InfoObject) -> None:
            self._set(self.type_.generated_offsets[1], v)

        def paths(self) -> core.Map:
            return self._get(self.type_.generated_offsets[2])

        def set_paths(self, v: core.Map) -> None:
            self._set(self.type_.generated_offsets[2], v)

        def components(self) -> runtime.ComponentsObject:
            return self._get(self.type_.generated_offsets[3])

        def set_components(self, v: runtime.ComponentsObject) -> None:
            self._set(self.type_.generated_offsets[3], v)

    @final
    class SchemaFormat(GreyCat.Enum):
        name_: Final[str] = "runtime::SchemaFormat"
        __indices_by_values: dict[str, int] = {
            "int32": 0,
            "int64": 1,
            "float": 2,
            "double": 3,
            "byte": 4,
            "binary": 5,
            "date": 6,
            "date-time": 7,
            "password": 8,
        }

        def __init__(self, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[125]
            attributes: list = []
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

        def __class_getitem__(cls, key) -> runtime.SchemaFormat:
            greycat: GreyCat
            if isinstance(key, tuple):
                key, greycat = key
            else:
                greycat = GreyCat._DEFAULT
            t: Final[GreyCat.Type] = greycat.libs_by_name[_std._name].mapped[125]
            return t.enum_values[t.generated_offsets[runtime.SchemaFormat.__indices_by_values[key]]]

    @final
    class SchemaType(GreyCat.Enum):
        name_: Final[str] = "runtime::SchemaType"
        __indices_by_values: dict[str, int] = {
            "string": 0,
            "number": 1,
            "integer": 2,
            "boolean": 3,
            "object": 4,
            "array": 5,
        }

        def __init__(self, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[126]
            attributes: list = []
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

        def __class_getitem__(cls, key) -> runtime.SchemaType:
            greycat: GreyCat
            if isinstance(key, tuple):
                key, greycat = key
            else:
                greycat = GreyCat._DEFAULT
            t: Final[GreyCat.Type] = greycat.libs_by_name[_std._name].mapped[126]
            return t.enum_values[t.generated_offsets[runtime.SchemaType.__indices_by_values[key]]]

    @final
    class Periodicity(GreyCat.Object):
        name_: Final[str] = "runtime::Periodicity"

        def __init__(self, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[127]
            attributes: list = []
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

    @final
    class ChildProcessResult(GreyCat.Object):
        name_: Final[str] = "runtime::ChildProcessResult"

        def __init__(self, code: int, stdout: str, stderr: str, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[128]
            attributes: list = [code, stdout, stderr]
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

        def code(self) -> int:
            return self._get(self.type_.generated_offsets[0])

        def set_code(self, v: int) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def stdout(self) -> str:
            return self._get(self.type_.generated_offsets[1])

        def set_stdout(self, v: str) -> None:
            self._set(self.type_.generated_offsets[1], v)

        def stderr(self) -> str:
            return self._get(self.type_.generated_offsets[2])

        def set_stderr(self, v: str) -> None:
            self._set(self.type_.generated_offsets[2], v)

    @final
    class RuntimeInfo(GreyCat.Object):
        name_: Final[str] = "runtime::RuntimeInfo"

        def __init__(self, version: str, program_version: str, arch: str, timezone: core.TimeZone, license: runtime.License, io_threads: int, bg_threads: int, fg_threads: int, mem_total: int, mem_worker: int, disk_data_bytes: int, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[129]
            attributes: list = [version, program_version, arch, timezone, license, io_threads, bg_threads, fg_threads, mem_total, mem_worker, disk_data_bytes]
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

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

        def timezone(self) -> core.TimeZone:
            return self._get(self.type_.generated_offsets[3])

        def set_timezone(self, v: core.TimeZone) -> None:
            self._set(self.type_.generated_offsets[3], v)

        def license(self) -> runtime.License:
            return self._get(self.type_.generated_offsets[4])

        def set_license(self, v: runtime.License) -> None:
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

        def disk_data_bytes(self) -> int:
            return self._get(self.type_.generated_offsets[10])

        def set_disk_data_bytes(self, v: int) -> None:
            self._set(self.type_.generated_offsets[10], v)

    @final
    class Job(Generic[__T], GreyCat.Object):
        name_: Final[str] = "runtime::Job"

        def __init__(self, function: core.function, arguments: core.Array, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[130]
            attributes: list = [function, arguments]
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

        def function(self) -> core.function:
            return self._get(self.type_.generated_offsets[0])

        def set_function(self, v: core.function) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def arguments(self) -> core.Array:
            return self._get(self.type_.generated_offsets[1])

        def set_arguments(self, v: core.Array) -> None:
            self._set(self.type_.generated_offsets[1], v)

    @final
    class WeeklyPeriodicity(GreyCat.Object):
        name_: Final[str] = "runtime::WeeklyPeriodicity"

        def __init__(self, days: core.Array, daily: runtime.DailyPeriodicity, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[131]
            attributes: list = [days, daily]
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

        def days(self) -> core.Array:
            return self._get(self.type_.generated_offsets[0])

        def set_days(self, v: core.Array) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def daily(self) -> runtime.DailyPeriodicity:
            return self._get(self.type_.generated_offsets[1])

        def set_daily(self, v: runtime.DailyPeriodicity) -> None:
            self._set(self.type_.generated_offsets[1], v)


@final
class util:
    __T = TypeVar("__T")

    @final
    class QuantizerSlotBound(Generic[__T], GreyCat.Object):
        name_: Final[str] = "util::QuantizerSlotBound"

        def __init__(self, min: util.__T, max: util.__T, center: util.__T, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[132]
            attributes: list = [min, max, center]
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

        def min(self) -> util.__T:
            return self._get(self.type_.generated_offsets[0])

        def set_min(self, v: util.__T) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def max(self) -> util.__T:
            return self._get(self.type_.generated_offsets[1])

        def set_max(self, v: util.__T) -> None:
            self._set(self.type_.generated_offsets[1], v)

        def center(self) -> util.__T:
            return self._get(self.type_.generated_offsets[2])

        def set_center(self, v: util.__T) -> None:
            self._set(self.type_.generated_offsets[2], v)

    @final
    class Histogram(Generic[__T], GreyCat.Object):
        name_: Final[str] = "util::Histogram"

        def __init__(self, quantizer: util.Quantizer, bins: core.Array, nb_rejected: int, nb_accepted: int, min: util.__T, max: util.__T, sum: float, sumsq: float, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[133]
            attributes: list = [quantizer, bins, nb_rejected, nb_accepted, min, max, sum, sumsq]
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

        def quantizer(self) -> util.Quantizer:
            return self._get(self.type_.generated_offsets[0])

        def set_quantizer(self, v: util.Quantizer) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def bins(self) -> core.Array:
            return self._get(self.type_.generated_offsets[1])

        def set_bins(self, v: core.Array) -> None:
            self._set(self.type_.generated_offsets[1], v)

        def nb_rejected(self) -> int:
            return self._get(self.type_.generated_offsets[2])

        def set_nb_rejected(self, v: int) -> None:
            self._set(self.type_.generated_offsets[2], v)

        def nb_accepted(self) -> int:
            return self._get(self.type_.generated_offsets[3])

        def set_nb_accepted(self, v: int) -> None:
            self._set(self.type_.generated_offsets[3], v)

        def min(self) -> util.__T:
            return self._get(self.type_.generated_offsets[4])

        def set_min(self, v: util.__T) -> None:
            self._set(self.type_.generated_offsets[4], v)

        def max(self) -> util.__T:
            return self._get(self.type_.generated_offsets[5])

        def set_max(self, v: util.__T) -> None:
            self._set(self.type_.generated_offsets[5], v)

        def sum(self) -> float:
            return self._get(self.type_.generated_offsets[6])

        def set_sum(self, v: float) -> None:
            self._set(self.type_.generated_offsets[6], v)

        def sumsq(self) -> float:
            return self._get(self.type_.generated_offsets[7])

        def set_sumsq(self, v: float) -> None:
            self._set(self.type_.generated_offsets[7], v)

    @final
    class Quantizer(Generic[__T], GreyCat.Object):
        name_: Final[str] = "util::Quantizer"

        def __init__(self, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[134]
            attributes: list = []
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

    @final
    class SlidingWindow(Generic[__T], GreyCat.Object):
        name_: Final[str] = "util::SlidingWindow"

        def __init__(self, values: core.Array, span: int, sum: float, sumsq: float, field: core.field, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[135]
            attributes: list = [values, span, sum, sumsq, field]
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

        def values(self) -> core.Array:
            return self._get(self.type_.generated_offsets[0])

        def set_values(self, v: core.Array) -> None:
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

        def field(self) -> core.field:
            return self._get(self.type_.generated_offsets[4])

        def set_field(self, v: core.field) -> None:
            self._set(self.type_.generated_offsets[4], v)

    @final
    class LinearQuantizer(Generic[__T], GreyCat.Object):
        name_: Final[str] = "util::LinearQuantizer"

        def __init__(self, min: util.__T, max: util.__T, bins: int, open: bool, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[136]
            attributes: list = [min, max, bins, open]
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

        def min(self) -> util.__T:
            return self._get(self.type_.generated_offsets[0])

        def set_min(self, v: util.__T) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def max(self) -> util.__T:
            return self._get(self.type_.generated_offsets[1])

        def set_max(self, v: util.__T) -> None:
            self._set(self.type_.generated_offsets[1], v)

        def bins(self) -> int:
            return self._get(self.type_.generated_offsets[2])

        def set_bins(self, v: int) -> None:
            self._set(self.type_.generated_offsets[2], v)

        def open(self) -> bool:
            return self._get(self.type_.generated_offsets[3])

        def set_open(self, v: bool) -> None:
            self._set(self.type_.generated_offsets[3], v)

    @final
    class Stack(Generic[__T], GreyCat.Object):
        name_: Final[str] = "util::Stack"

        def __init__(self, values: core.Array, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[137]
            attributes: list = [values]
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

        def values(self) -> core.Array:
            return self._get(self.type_.generated_offsets[0])

        def set_values(self, v: core.Array) -> None:
            self._set(self.type_.generated_offsets[0], v)

    @final
    class Random(GreyCat.Object):
        name_: Final[str] = "util::Random"

        def __init__(self, seed: int, v: float, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[138]
            attributes: list = [seed, v]
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

        def seed(self) -> int:
            return self._get(self.type_.generated_offsets[0])

        def set_seed(self, v: int) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def v(self) -> float:
            return self._get(self.type_.generated_offsets[1])

        def set_v(self, v: float) -> None:
            self._set(self.type_.generated_offsets[1], v)

    @final
    class MultiQuantizer(Generic[__T], GreyCat.Object):
        name_: Final[str] = "util::MultiQuantizer"

        def __init__(self, quantizers: core.Array, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[139]
            attributes: list = [quantizers]
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

        def quantizers(self) -> core.Array:
            return self._get(self.type_.generated_offsets[0])

        def set_quantizers(self, v: core.Array) -> None:
            self._set(self.type_.generated_offsets[0], v)

    @final
    class Assert(GreyCat.Object):
        name_: Final[str] = "util::Assert"

        def __init__(self, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[140]
            attributes: list = []
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

    @final
    class Plot(GreyCat.Object):
        name_: Final[str] = "util::Plot"

        def __init__(self, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[141]
            attributes: list = []
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

    @final
    class CustomQuantizer(Generic[__T], GreyCat.Object):
        name_: Final[str] = "util::CustomQuantizer"

        def __init__(self, min: util.__T, max: util.__T, step_starts: core.Array, open: bool, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[142]
            attributes: list = [min, max, step_starts, open]
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

        def min(self) -> util.__T:
            return self._get(self.type_.generated_offsets[0])

        def set_min(self, v: util.__T) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def max(self) -> util.__T:
            return self._get(self.type_.generated_offsets[1])

        def set_max(self, v: util.__T) -> None:
            self._set(self.type_.generated_offsets[1], v)

        def step_starts(self) -> core.Array:
            return self._get(self.type_.generated_offsets[2])

        def set_step_starts(self, v: core.Array) -> None:
            self._set(self.type_.generated_offsets[2], v)

        def open(self) -> bool:
            return self._get(self.type_.generated_offsets[3])

        def set_open(self, v: bool) -> None:
            self._set(self.type_.generated_offsets[3], v)

    @final
    class TimeWindow(Generic[__T], GreyCat.Object):
        name_: Final[str] = "util::TimeWindow"

        def __init__(self, values: core.Table, span: core.duration, sum: float, sumsq: float, field: core.field, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[143]
            attributes: list = [values, span, sum, sumsq, field]
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

        def values(self) -> core.Table:
            return self._get(self.type_.generated_offsets[0])

        def set_values(self, v: core.Table) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def span(self) -> core.duration:
            return self._get(self.type_.generated_offsets[1])

        def set_span(self, v: core.duration) -> None:
            self._set(self.type_.generated_offsets[1], v)

        def sum(self) -> float:
            return self._get(self.type_.generated_offsets[2])

        def set_sum(self, v: float) -> None:
            self._set(self.type_.generated_offsets[2], v)

        def sumsq(self) -> float:
            return self._get(self.type_.generated_offsets[3])

        def set_sumsq(self, v: float) -> None:
            self._set(self.type_.generated_offsets[3], v)

        def field(self) -> core.field:
            return self._get(self.type_.generated_offsets[4])

        def set_field(self, v: core.field) -> None:
            self._set(self.type_.generated_offsets[4], v)

    @final
    class Queue(Generic[__T], GreyCat.Object):
        name_: Final[str] = "util::Queue"

        def __init__(self, values: core.Array, capacity: int, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[144]
            attributes: list = [values, capacity]
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

        def values(self) -> core.Array:
            return self._get(self.type_.generated_offsets[0])

        def set_values(self, v: core.Array) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def capacity(self) -> int:
            return self._get(self.type_.generated_offsets[1])

        def set_capacity(self, v: int) -> None:
            self._set(self.type_.generated_offsets[1], v)

    @final
    class Gaussian(Generic[__T], GreyCat.Object):
        name_: Final[str] = "util::Gaussian"

        def __init__(self, sum: float, sumsq: float, count: int, min: util.__T, max: util.__T, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[145]
            attributes: list = [sum, sumsq, count, min, max]
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

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

        def min(self) -> util.__T:
            return self._get(self.type_.generated_offsets[3])

        def set_min(self, v: util.__T) -> None:
            self._set(self.type_.generated_offsets[3], v)

        def max(self) -> util.__T:
            return self._get(self.type_.generated_offsets[4])

        def set_max(self, v: util.__T) -> None:
            self._set(self.type_.generated_offsets[4], v)

    @final
    class GaussianProfile(Generic[__T], GreyCat.Object):
        name_: Final[str] = "util::GaussianProfile"

        def __init__(self, quantizer: util.Quantizer, precision: core.FloatPrecision, bins: core.Table, value_min: float, nb_rejected: int, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[146]
            attributes: list = [quantizer, precision, bins, value_min, nb_rejected]
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

        def quantizer(self) -> util.Quantizer:
            return self._get(self.type_.generated_offsets[0])

        def set_quantizer(self, v: util.Quantizer) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def precision(self) -> core.FloatPrecision:
            return self._get(self.type_.generated_offsets[1])

        def set_precision(self, v: core.FloatPrecision) -> None:
            self._set(self.type_.generated_offsets[1], v)

        def bins(self) -> core.Table:
            return self._get(self.type_.generated_offsets[2])

        def set_bins(self, v: core.Table) -> None:
            self._set(self.type_.generated_offsets[2], v)

        def value_min(self) -> float:
            return self._get(self.type_.generated_offsets[3])

        def set_value_min(self, v: float) -> None:
            self._set(self.type_.generated_offsets[3], v)

        def nb_rejected(self) -> int:
            return self._get(self.type_.generated_offsets[4])

        def set_nb_rejected(self, v: int) -> None:
            self._set(self.type_.generated_offsets[4], v)

    @final
    class Crypto(GreyCat.Object):
        name_: Final[str] = "util::Crypto"

        def __init__(self, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[147]
            attributes: list = []
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

    @final
    class HistogramBin(Generic[__T], GreyCat.Object):
        name_: Final[str] = "util::HistogramBin"

        def __init__(self, bin: util.QuantizerSlotBound, count: int, ratio: float, cumulative_count: int, cumulative_ratio: float, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[148]
            attributes: list = [bin, count, ratio, cumulative_count, cumulative_ratio]
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

        def bin(self) -> util.QuantizerSlotBound:
            return self._get(self.type_.generated_offsets[0])

        def set_bin(self, v: util.QuantizerSlotBound) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def count(self) -> int:
            return self._get(self.type_.generated_offsets[1])

        def set_count(self, v: int) -> None:
            self._set(self.type_.generated_offsets[1], v)

        def ratio(self) -> float:
            return self._get(self.type_.generated_offsets[2])

        def set_ratio(self, v: float) -> None:
            self._set(self.type_.generated_offsets[2], v)

        def cumulative_count(self) -> int:
            return self._get(self.type_.generated_offsets[3])

        def set_cumulative_count(self, v: int) -> None:
            self._set(self.type_.generated_offsets[3], v)

        def cumulative_ratio(self) -> float:
            return self._get(self.type_.generated_offsets[4])

        def set_cumulative_ratio(self, v: float) -> None:
            self._set(self.type_.generated_offsets[4], v)

    @final
    class HistogramStats(Generic[__T], GreyCat.Object):
        name_: Final[str] = "util::HistogramStats"

        def __init__(self, min: util.__T, max: util.__T, whisker_low: util.__T, whisker_high: util.__T, percentile1: util.__T, percentile5: util.__T, percentile10: util.__T, percentile20: util.__T, percentile25: util.__T, percentile50: util.__T, percentile75: util.__T, percentile80: util.__T, percentile90: util.__T, percentile95: util.__T, percentile99: util.__T, sum: float, avg: util.__T, std: util.__T, size: int, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[149]
            attributes: list = [min, max, whisker_low, whisker_high, percentile1, percentile5, percentile10, percentile20, percentile25, percentile50, percentile75, percentile80, percentile90, percentile95, percentile99, sum, avg, std, size]
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

        def min(self) -> util.__T:
            return self._get(self.type_.generated_offsets[0])

        def set_min(self, v: util.__T) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def max(self) -> util.__T:
            return self._get(self.type_.generated_offsets[1])

        def set_max(self, v: util.__T) -> None:
            self._set(self.type_.generated_offsets[1], v)

        def whisker_low(self) -> util.__T:
            return self._get(self.type_.generated_offsets[2])

        def set_whisker_low(self, v: util.__T) -> None:
            self._set(self.type_.generated_offsets[2], v)

        def whisker_high(self) -> util.__T:
            return self._get(self.type_.generated_offsets[3])

        def set_whisker_high(self, v: util.__T) -> None:
            self._set(self.type_.generated_offsets[3], v)

        def percentile1(self) -> util.__T:
            return self._get(self.type_.generated_offsets[4])

        def set_percentile1(self, v: util.__T) -> None:
            self._set(self.type_.generated_offsets[4], v)

        def percentile5(self) -> util.__T:
            return self._get(self.type_.generated_offsets[5])

        def set_percentile5(self, v: util.__T) -> None:
            self._set(self.type_.generated_offsets[5], v)

        def percentile10(self) -> util.__T:
            return self._get(self.type_.generated_offsets[6])

        def set_percentile10(self, v: util.__T) -> None:
            self._set(self.type_.generated_offsets[6], v)

        def percentile20(self) -> util.__T:
            return self._get(self.type_.generated_offsets[7])

        def set_percentile20(self, v: util.__T) -> None:
            self._set(self.type_.generated_offsets[7], v)

        def percentile25(self) -> util.__T:
            return self._get(self.type_.generated_offsets[8])

        def set_percentile25(self, v: util.__T) -> None:
            self._set(self.type_.generated_offsets[8], v)

        def percentile50(self) -> util.__T:
            return self._get(self.type_.generated_offsets[9])

        def set_percentile50(self, v: util.__T) -> None:
            self._set(self.type_.generated_offsets[9], v)

        def percentile75(self) -> util.__T:
            return self._get(self.type_.generated_offsets[10])

        def set_percentile75(self, v: util.__T) -> None:
            self._set(self.type_.generated_offsets[10], v)

        def percentile80(self) -> util.__T:
            return self._get(self.type_.generated_offsets[11])

        def set_percentile80(self, v: util.__T) -> None:
            self._set(self.type_.generated_offsets[11], v)

        def percentile90(self) -> util.__T:
            return self._get(self.type_.generated_offsets[12])

        def set_percentile90(self, v: util.__T) -> None:
            self._set(self.type_.generated_offsets[12], v)

        def percentile95(self) -> util.__T:
            return self._get(self.type_.generated_offsets[13])

        def set_percentile95(self, v: util.__T) -> None:
            self._set(self.type_.generated_offsets[13], v)

        def percentile99(self) -> util.__T:
            return self._get(self.type_.generated_offsets[14])

        def set_percentile99(self, v: util.__T) -> None:
            self._set(self.type_.generated_offsets[14], v)

        def sum(self) -> float:
            return self._get(self.type_.generated_offsets[15])

        def set_sum(self, v: float) -> None:
            self._set(self.type_.generated_offsets[15], v)

        def avg(self) -> util.__T:
            return self._get(self.type_.generated_offsets[16])

        def set_avg(self, v: util.__T) -> None:
            self._set(self.type_.generated_offsets[16], v)

        def std(self) -> util.__T:
            return self._get(self.type_.generated_offsets[17])

        def set_std(self, v: util.__T) -> None:
            self._set(self.type_.generated_offsets[17], v)

        def size(self) -> int:
            return self._get(self.type_.generated_offsets[18])

        def set_size(self, v: int) -> None:
            self._set(self.type_.generated_offsets[18], v)

    @final
    class ProgressTracker(GreyCat.Object):
        name_: Final[str] = "util::ProgressTracker"

        def __init__(self, start: core.time, total: int, counter: int, duration: core.duration, progress: float, speed: float, remaining: core.duration, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[150]
            attributes: list = [start, total, counter, duration, progress, speed, remaining]
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

        def start(self) -> core.time:
            return self._get(self.type_.generated_offsets[0])

        def set_start(self, v: core.time) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def total(self) -> int:
            return self._get(self.type_.generated_offsets[1])

        def set_total(self, v: int) -> None:
            self._set(self.type_.generated_offsets[1], v)

        def counter(self) -> int:
            return self._get(self.type_.generated_offsets[2])

        def set_counter(self, v: int) -> None:
            self._set(self.type_.generated_offsets[2], v)

        def duration(self) -> core.duration:
            return self._get(self.type_.generated_offsets[3])

        def set_duration(self, v: core.duration) -> None:
            self._set(self.type_.generated_offsets[3], v)

        def progress(self) -> float:
            return self._get(self.type_.generated_offsets[4])

        def set_progress(self, v: float) -> None:
            self._set(self.type_.generated_offsets[4], v)

        def speed(self) -> float:
            return self._get(self.type_.generated_offsets[5])

        def set_speed(self, v: float) -> None:
            self._set(self.type_.generated_offsets[5], v)

        def remaining(self) -> core.duration:
            return self._get(self.type_.generated_offsets[6])

        def set_remaining(self, v: core.duration) -> None:
            self._set(self.type_.generated_offsets[6], v)

    @final
    class GaussianProfileSlot(GreyCat.Object):
        name_: Final[str] = "util::GaussianProfileSlot"

        def __init__(self, sum: int, sumsq: int, count: int, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[151]
            attributes: list = [sum, sumsq, count]
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

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

    @final
    class LogQuantizer(Generic[__T], GreyCat.Object):
        name_: Final[str] = "util::LogQuantizer"

        def __init__(self, min: util.__T, max: util.__T, bins: int, open: bool, *, _type: Optional[GreyCat.Type] = None):
            if _type is None:
                _type = GreyCat._DEFAULT.libs_by_name[_std._name].mapped[152]
            attributes: list = [min, max, bins, open]
            super().__init__(_type, [attributes[offset] for offset in _type.generated_offsets])

        def min(self) -> util.__T:
            return self._get(self.type_.generated_offsets[0])

        def set_min(self, v: util.__T) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def max(self) -> util.__T:
            return self._get(self.type_.generated_offsets[1])

        def set_max(self, v: util.__T) -> None:
            self._set(self.type_.generated_offsets[1], v)

        def bins(self) -> int:
            return self._get(self.type_.generated_offsets[2])

        def set_bins(self, v: int) -> None:
            self._set(self.type_.generated_offsets[2], v)

        def open(self) -> bool:
            return self._get(self.type_.generated_offsets[3])

        def set_open(self, v: bool) -> None:
            self._set(self.type_.generated_offsets[3], v)


@final
class _std(GreyCat.Library):
    _name = "std"

    def name(self) -> str:
        return _std._name

    def configure(self, loaders: dict[str, GreyCat.Loader], factories: dict[str, GreyCat.Factory]) -> None:
        factories[core.VectorIndex.name_] = lambda _type, attributes: core.VectorIndex(*attributes, _type=_type)
        factories[core.t3f.name_] = lambda _type, attributes: core.t3f(*attributes, _type=_type)
        loaders[core.t3f.name_] = lambda type, stream: std_n.core._t3f.load(type, stream)

        factories[core.TensorType.name_] = lambda _type, attributes: GreyCat.Enum(_type, attributes)
        factories[core.nodeGeo.name_] = lambda _type, attributes: core.nodeGeo(*attributes, _type=_type)
        loaders[core.nodeGeo.name_] = lambda type, stream: std_n.core._nodeGeo.load(type, stream)

        factories[core.nodeTime.name_] = lambda _type, attributes: core.nodeTime(*attributes, _type=_type)
        loaders[core.nodeTime.name_] = lambda type, stream: std_n.core._nodeTime.load(type, stream)

        factories[core.nodeIndexBucket.name_] = lambda _type, attributes: core.nodeIndexBucket(*attributes, _type=_type)
        factories[core.String.name_] = lambda _type, attributes: core.String(*attributes, _type=_type)
        loaders[core.String.name_] = lambda type, stream: std_n.core._String.load(type, stream)

        factories[core.FloatPrecision.name_] = lambda _type, attributes: GreyCat.Enum(_type, attributes)
        factories[core.field.name_] = lambda _type, attributes: core.field(*attributes, _type=_type)
        loaders[core.field.name_] = lambda type, stream: std_n.core._field.load(type, stream)

        factories[core.nodeList.name_] = lambda _type, attributes: core.nodeList(*attributes, _type=_type)
        loaders[core.nodeList.name_] = lambda type, stream: std_n.core._nodeList.load(type, stream)

        factories[core.Buffer.name_] = lambda _type, attributes: core.Buffer(*attributes, _type=_type)
        loaders[core.Buffer.name_] = lambda type, stream: std_n.core._Buffer.load(type, stream)

        factories[core.t2.name_] = lambda _type, attributes: core.t2(*attributes, _type=_type)
        loaders[core.t2.name_] = lambda type, stream: std_n.core._t2.load(type, stream)

        factories[core.time.name_] = lambda _type, attributes: core.time(*attributes, _type=_type)
        loaders[core.time.name_] = lambda type, stream: std_n.core._time.load(type, stream)

        factories[core.CalendarUnit.name_] = lambda _type, attributes: GreyCat.Enum(_type, attributes)
        factories[core.Map.name_] = lambda _type, attributes: core.Map(*attributes, _type=_type)
        loaders[core.Map.name_] = lambda type, stream: std_n.core._Map.load(type, stream)

        factories[core.TensorDistance.name_] = lambda _type, attributes: GreyCat.Enum(_type, attributes)
        factories[core.MathConstants.name_] = lambda _type, attributes: core.MathConstants(*attributes, _type=_type)
        factories[core.TimeZone.name_] = lambda _type, attributes: GreyCat.Enum(_type, attributes)
        factories[core.t3.name_] = lambda _type, attributes: core.t3(*attributes, _type=_type)
        loaders[core.t3.name_] = lambda type, stream: std_n.core._t3.load(type, stream)

        factories[core.type.name_] = lambda _type, attributes: core.type(*attributes, _type=_type)
        loaders[core.type.name_] = lambda type, stream: std_n.core._type.load(type, stream)

        factories[core.str.name_] = lambda _type, attributes: core.str(*attributes, _type=_type)
        loaders[core.str.name_] = lambda type, stream: std_n.core._str.load(type, stream)

        factories[core.SamplingMode.name_] = lambda _type, attributes: GreyCat.Enum(_type, attributes)
        factories[core.node.name_] = lambda _type, attributes: core.node(*attributes, _type=_type)
        loaders[core.node.name_] = lambda type, stream: std_n.core._node.load(type, stream)

        factories[core.VectorVertex.name_] = lambda _type, attributes: core.VectorVertex(*attributes, _type=_type)
        factories[core.TableColumnMapping.name_] = lambda _type, attributes: core.TableColumnMapping(*attributes, _type=_type)
        factories[core.ErrorFrame.name_] = lambda _type, attributes: core.ErrorFrame(*attributes, _type=_type)
        factories[core.nodeIndex.name_] = lambda _type, attributes: core.nodeIndex(*attributes, _type=_type)
        loaders[core.nodeIndex.name_] = lambda type, stream: std_n.core._nodeIndex.load(type, stream)

        factories[core.GeoBox.name_] = lambda _type, attributes: core.GeoBox(*attributes, _type=_type)
        factories[core.Table.name_] = lambda _type, attributes: core.Table(*attributes, _type=_type)
        loaders[core.Table.name_] = lambda type, stream: std_n.core._Table.load(type, stream)

        factories[core.t2f.name_] = lambda _type, attributes: core.t2f(*attributes, _type=_type)
        loaders[core.t2f.name_] = lambda type, stream: std_n.core._t2f.load(type, stream)

        factories[core.duration.name_] = lambda _type, attributes: core.duration(*attributes, _type=_type)
        loaders[core.duration.name_] = lambda type, stream: std_n.core._duration.load(type, stream)

        factories[core.geo.name_] = lambda _type, attributes: core.geo(*attributes, _type=_type)
        loaders[core.geo.name_] = lambda type, stream: std_n.core._geo.load(type, stream)

        factories[core.Array.name_] = lambda _type, attributes: core.Array(*attributes, _type=_type)
        loaders[core.Array.name_] = lambda type, stream: std_n.core._Array.load(type, stream)

        factories[core.Tuple.name_] = lambda _type, attributes: core.Tuple(*attributes, _type=_type)
        factories[core.GeoPoly.name_] = lambda _type, attributes: core.GeoPoly(*attributes, _type=_type)
        factories[core.SortOrder.name_] = lambda _type, attributes: GreyCat.Enum(_type, attributes)
        factories[core.nodeTimeCursor.name_] = lambda _type, attributes: core.nodeTimeCursor(*attributes, _type=_type)
        factories[core.t4f.name_] = lambda _type, attributes: core.t4f(*attributes, _type=_type)
        loaders[core.t4f.name_] = lambda type, stream: std_n.core._t4f.load(type, stream)

        factories[core.GeoCircle.name_] = lambda _type, attributes: core.GeoCircle(*attributes, _type=_type)
        factories[core.t4.name_] = lambda _type, attributes: core.t4(*attributes, _type=_type)
        loaders[core.t4.name_] = lambda type, stream: std_n.core._t4.load(type, stream)

        factories[core.Date.name_] = lambda _type, attributes: core.Date(*attributes, _type=_type)
        factories[core.SearchResult.name_] = lambda _type, attributes: core.SearchResult(*attributes, _type=_type)
        factories[core.DurationUnit.name_] = lambda _type, attributes: GreyCat.Enum(_type, attributes)
        factories[core.function.name_] = lambda _type, attributes: core.function(*attributes, _type=_type)
        loaders[core.function.name_] = lambda type, stream: std_n.core._function.load(type, stream)

        factories[core.Tensor.name_] = lambda _type, attributes: core.Tensor(*attributes, _type=_type)
        loaders[core.Tensor.name_] = lambda type, stream: std_n.core._Tensor.load(type, stream)

        factories[core.ErrorCode.name_] = lambda _type, attributes: GreyCat.Enum(_type, attributes)
        factories[core.NodeInfo.name_] = lambda _type, attributes: core.NodeInfo(*attributes, _type=_type)
        factories[core.Error.name_] = lambda _type, attributes: core.Error(*attributes, _type=_type)
        factories[io.TextReader.name_] = lambda _type, attributes: io.TextReader(*attributes, _type=_type)
        factories[io.SmtpMode.name_] = lambda _type, attributes: GreyCat.Enum(_type, attributes)
        factories[io.GcbReader.name_] = lambda _type, attributes: io.GcbReader(*attributes, _type=_type)
        factories[io.CsvStatistics.name_] = lambda _type, attributes: io.CsvStatistics(*attributes, _type=_type)
        factories[io.CsvAnalysisConfig.name_] = lambda _type, attributes: io.CsvAnalysisConfig(*attributes, _type=_type)
        factories[io.TextWriter.name_] = lambda _type, attributes: io.TextWriter(*attributes, _type=_type)
        factories[io.CsvWriter.name_] = lambda _type, attributes: io.CsvWriter(*attributes, _type=_type)
        factories[io.HttpMethod.name_] = lambda _type, attributes: GreyCat.Enum(_type, attributes)
        factories[io.SmtpAuth.name_] = lambda _type, attributes: GreyCat.Enum(_type, attributes)
        factories[io.Email.name_] = lambda _type, attributes: io.Email(*attributes, _type=_type)
        factories[io.Url.name_] = lambda _type, attributes: io.Url(*attributes, _type=_type)
        factories[io.Smtp.name_] = lambda _type, attributes: io.Smtp(*attributes, _type=_type)
        factories[io.Reader.name_] = lambda _type, attributes: io.Reader(*attributes, _type=_type)
        factories[io.CsvColumnStatistics.name_] = lambda _type, attributes: io.CsvColumnStatistics(*attributes, _type=_type)
        factories[io.FileWalker.name_] = lambda _type, attributes: io.FileWalker(*attributes, _type=_type)
        factories[io.HttpResponse.name_] = lambda _type, attributes: io.HttpResponse(*attributes, _type=_type)
        factories[io.JsonWriter.name_] = lambda _type, attributes: io.JsonWriter(*attributes, _type=_type)
        factories[io.Json.name_] = lambda _type, attributes: io.Json(*attributes, _type=_type)
        factories[io.CsvSharding.name_] = lambda _type, attributes: io.CsvSharding(*attributes, _type=_type)
        factories[io.Csv.name_] = lambda _type, attributes: io.Csv(*attributes, _type=_type)
        factories[io.Writer.name_] = lambda _type, attributes: io.Writer(*attributes, _type=_type)
        factories[io.JsonReader.name_] = lambda _type, attributes: io.JsonReader(*attributes, _type=_type)
        factories[io.CsvReader.name_] = lambda _type, attributes: io.CsvReader(*attributes, _type=_type)
        factories[io.XmlReader.name_] = lambda _type, attributes: io.XmlReader(*attributes, _type=_type)
        factories[io.Http.name_] = lambda _type, attributes: io.Http(*attributes, _type=_type)
        factories[io.GcbWriter.name_] = lambda _type, attributes: io.GcbWriter(*attributes, _type=_type)
        factories[io.HttpRequest.name_] = lambda _type, attributes: io.HttpRequest(*attributes, _type=_type)
        factories[io.CsvFormat.name_] = lambda _type, attributes: io.CsvFormat(*attributes, _type=_type)
        factories[io.File.name_] = lambda _type, attributes: io.File(*attributes, _type=_type)
        factories[runtime.Role.name_] = lambda _type, attributes: runtime.Role(*attributes, _type=_type)
        factories[runtime.Month.name_] = lambda _type, attributes: GreyCat.Enum(_type, attributes)
        factories[runtime.Runtime.name_] = lambda _type, attributes: runtime.Runtime(*attributes, _type=_type)
        factories[runtime.FixedPeriodicity.name_] = lambda _type, attributes: runtime.FixedPeriodicity(*attributes, _type=_type)
        factories[runtime.DateTuple.name_] = lambda _type, attributes: runtime.DateTuple(*attributes, _type=_type)
        factories[runtime.Frame.name_] = lambda _type, attributes: runtime.Frame(*attributes, _type=_type)
        factories[runtime.Log.name_] = lambda _type, attributes: runtime.Log(*attributes, _type=_type)
        factories[runtime.MediaTypeObject.name_] = lambda _type, attributes: runtime.MediaTypeObject(*attributes, _type=_type)
        factories[runtime.UserGroupPolicyType.name_] = lambda _type, attributes: GreyCat.Enum(_type, attributes)
        factories[runtime.SecurityEntity.name_] = lambda _type, attributes: runtime.SecurityEntity(*attributes, _type=_type)
        factories[runtime.RequestBodyObject.name_] = lambda _type, attributes: runtime.RequestBodyObject(*attributes, _type=_type)
        factories[runtime.OperationObject.name_] = lambda _type, attributes: runtime.OperationObject(*attributes, _type=_type)
        factories[runtime.ResponseObject.name_] = lambda _type, attributes: runtime.ResponseObject(*attributes, _type=_type)
        factories[runtime.UserCredential.name_] = lambda _type, attributes: runtime.UserCredential(*attributes, _type=_type)
        factories[runtime.TaskStatus.name_] = lambda _type, attributes: GreyCat.Enum(_type, attributes)
        factories[runtime.DayOfWeek.name_] = lambda _type, attributes: GreyCat.Enum(_type, attributes)
        factories[runtime.UserGroup.name_] = lambda _type, attributes: runtime.UserGroup(*attributes, _type=_type)
        factories[runtime.PathItemObject.name_] = lambda _type, attributes: runtime.PathItemObject(*attributes, _type=_type)
        factories[runtime.SecurityPolicy.name_] = lambda _type, attributes: runtime.SecurityPolicy(*attributes, _type=_type)
        factories[runtime.OpenIDConnect.name_] = lambda _type, attributes: runtime.OpenIDConnect(*attributes, _type=_type)
        factories[runtime.Debug.name_] = lambda _type, attributes: runtime.Debug(*attributes, _type=_type)
        factories[runtime.YearlyPeriodicity.name_] = lambda _type, attributes: runtime.YearlyPeriodicity(*attributes, _type=_type)
        factories[runtime.OpenApi.name_] = lambda _type, attributes: runtime.OpenApi(*attributes, _type=_type)
        factories[runtime.License.name_] = lambda _type, attributes: runtime.License(*attributes, _type=_type)
        factories[runtime.ComponentsObject.name_] = lambda _type, attributes: runtime.ComponentsObject(*attributes, _type=_type)
        factories[runtime.UserGroupPolicy.name_] = lambda _type, attributes: runtime.UserGroupPolicy(*attributes, _type=_type)
        factories[runtime.MonthlyPeriodicity.name_] = lambda _type, attributes: runtime.MonthlyPeriodicity(*attributes, _type=_type)
        factories[runtime.ResponseCode.name_] = lambda _type, attributes: GreyCat.Enum(_type, attributes)
        factories[runtime.OpenApiVersion.name_] = lambda _type, attributes: GreyCat.Enum(_type, attributes)
        factories[runtime.Variable.name_] = lambda _type, attributes: runtime.Variable(*attributes, _type=_type)
        factories[runtime.MergeStrategy.name_] = lambda _type, attributes: GreyCat.Enum(_type, attributes)
        factories[runtime.InfoObject.name_] = lambda _type, attributes: runtime.InfoObject(*attributes, _type=_type)
        factories[runtime.DailyPeriodicity.name_] = lambda _type, attributes: runtime.DailyPeriodicity(*attributes, _type=_type)
        factories[runtime.LicenseType.name_] = lambda _type, attributes: GreyCat.Enum(_type, attributes)
        factories[runtime.Scheduler.name_] = lambda _type, attributes: runtime.Scheduler(*attributes, _type=_type)
        factories[runtime.PeriodicOptions.name_] = lambda _type, attributes: runtime.PeriodicOptions(*attributes, _type=_type)
        factories[runtime.HeaderObject.name_] = lambda _type, attributes: runtime.HeaderObject(*attributes, _type=_type)
        factories[runtime.ChildProcess.name_] = lambda _type, attributes: runtime.ChildProcess(*attributes, _type=_type)
        factories[runtime.SchemaObject.name_] = lambda _type, attributes: runtime.SchemaObject(*attributes, _type=_type)
        factories[runtime.Permission.name_] = lambda _type, attributes: runtime.Permission(*attributes, _type=_type)
        factories[runtime.Task.name_] = lambda _type, attributes: runtime.Task(*attributes, _type=_type)
        factories[runtime.System.name_] = lambda _type, attributes: runtime.System(*attributes, _type=_type)
        factories[runtime.SecurityFields.name_] = lambda _type, attributes: runtime.SecurityFields(*attributes, _type=_type)
        factories[runtime.LogDataUsage.name_] = lambda _type, attributes: runtime.LogDataUsage(*attributes, _type=_type)
        factories[runtime.LogLevel.name_] = lambda _type, attributes: GreyCat.Enum(_type, attributes)
        factories[runtime.PeriodicTask.name_] = lambda _type, attributes: runtime.PeriodicTask(*attributes, _type=_type)
        factories[runtime.User.name_] = lambda _type, attributes: runtime.User(*attributes, _type=_type)
        factories[runtime.OpenApiV3.name_] = lambda _type, attributes: runtime.OpenApiV3(*attributes, _type=_type)
        factories[runtime.SchemaFormat.name_] = lambda _type, attributes: GreyCat.Enum(_type, attributes)
        factories[runtime.SchemaType.name_] = lambda _type, attributes: GreyCat.Enum(_type, attributes)
        factories[runtime.Periodicity.name_] = lambda _type, attributes: runtime.Periodicity(*attributes, _type=_type)
        factories[runtime.ChildProcessResult.name_] = lambda _type, attributes: runtime.ChildProcessResult(*attributes, _type=_type)
        factories[runtime.RuntimeInfo.name_] = lambda _type, attributes: runtime.RuntimeInfo(*attributes, _type=_type)
        factories[runtime.Job.name_] = lambda _type, attributes: runtime.Job(*attributes, _type=_type)
        factories[runtime.WeeklyPeriodicity.name_] = lambda _type, attributes: runtime.WeeklyPeriodicity(*attributes, _type=_type)
        factories[util.QuantizerSlotBound.name_] = lambda _type, attributes: util.QuantizerSlotBound(*attributes, _type=_type)
        factories[util.Histogram.name_] = lambda _type, attributes: util.Histogram(*attributes, _type=_type)
        factories[util.Quantizer.name_] = lambda _type, attributes: util.Quantizer(*attributes, _type=_type)
        factories[util.SlidingWindow.name_] = lambda _type, attributes: util.SlidingWindow(*attributes, _type=_type)
        factories[util.LinearQuantizer.name_] = lambda _type, attributes: util.LinearQuantizer(*attributes, _type=_type)
        factories[util.Stack.name_] = lambda _type, attributes: util.Stack(*attributes, _type=_type)
        factories[util.Random.name_] = lambda _type, attributes: util.Random(*attributes, _type=_type)
        factories[util.MultiQuantizer.name_] = lambda _type, attributes: util.MultiQuantizer(*attributes, _type=_type)
        factories[util.Assert.name_] = lambda _type, attributes: util.Assert(*attributes, _type=_type)
        factories[util.Plot.name_] = lambda _type, attributes: util.Plot(*attributes, _type=_type)
        factories[util.CustomQuantizer.name_] = lambda _type, attributes: util.CustomQuantizer(*attributes, _type=_type)
        factories[util.TimeWindow.name_] = lambda _type, attributes: util.TimeWindow(*attributes, _type=_type)
        factories[util.Queue.name_] = lambda _type, attributes: util.Queue(*attributes, _type=_type)
        factories[util.Gaussian.name_] = lambda _type, attributes: util.Gaussian(*attributes, _type=_type)
        factories[util.GaussianProfile.name_] = lambda _type, attributes: util.GaussianProfile(*attributes, _type=_type)
        factories[util.Crypto.name_] = lambda _type, attributes: util.Crypto(*attributes, _type=_type)
        factories[util.HistogramBin.name_] = lambda _type, attributes: util.HistogramBin(*attributes, _type=_type)
        factories[util.HistogramStats.name_] = lambda _type, attributes: util.HistogramStats(*attributes, _type=_type)
        factories[util.ProgressTracker.name_] = lambda _type, attributes: util.ProgressTracker(*attributes, _type=_type)
        factories[util.GaussianProfileSlot.name_] = lambda _type, attributes: util.GaussianProfileSlot(*attributes, _type=_type)
        factories[util.LogQuantizer.name_] = lambda _type, attributes: util.LogQuantizer(*attributes, _type=_type)

    def init(self, greycat: GreyCat) -> None:
        self.mapped: list[GreyCat.Type] = [
            greycat.types_by_name[core.VectorIndex.name_],
            greycat.types_by_name[core.t3f.name_],
            greycat.types_by_name[core.TensorType.name_],
            greycat.types_by_name[core.nodeGeo.name_],
            greycat.types_by_name[core.nodeTime.name_],
            greycat.types_by_name[core.nodeIndexBucket.name_],
            greycat.types_by_name[core.String.name_],
            greycat.types_by_name[core.FloatPrecision.name_],
            greycat.types_by_name[core.field.name_],
            greycat.types_by_name[core.nodeList.name_],
            greycat.types_by_name[core.Buffer.name_],
            greycat.types_by_name[core.t2.name_],
            greycat.types_by_name[core.time.name_],
            greycat.types_by_name[core.CalendarUnit.name_],
            greycat.types_by_name[core.Map.name_],
            greycat.types_by_name[core.TensorDistance.name_],
            greycat.types_by_name[core.MathConstants.name_],
            greycat.types_by_name[core.TimeZone.name_],
            greycat.types_by_name[core.t3.name_],
            greycat.types_by_name[core.type.name_],
            greycat.types_by_name[core.str.name_],
            greycat.types_by_name[core.SamplingMode.name_],
            greycat.types_by_name[core.node.name_],
            greycat.types_by_name[core.VectorVertex.name_],
            greycat.types_by_name[core.TableColumnMapping.name_],
            greycat.types_by_name[core.ErrorFrame.name_],
            greycat.types_by_name[core.nodeIndex.name_],
            greycat.types_by_name[core.GeoBox.name_],
            greycat.types_by_name[core.Table.name_],
            greycat.types_by_name[core.t2f.name_],
            greycat.types_by_name[core.duration.name_],
            greycat.types_by_name[core.geo.name_],
            greycat.types_by_name[core.Array.name_],
            greycat.types_by_name[core.Tuple.name_],
            greycat.types_by_name[core.GeoPoly.name_],
            greycat.types_by_name[core.SortOrder.name_],
            greycat.types_by_name[core.nodeTimeCursor.name_],
            greycat.types_by_name[core.t4f.name_],
            greycat.types_by_name[core.GeoCircle.name_],
            greycat.types_by_name[core.t4.name_],
            greycat.types_by_name[core.Date.name_],
            greycat.types_by_name[core.SearchResult.name_],
            greycat.types_by_name[core.DurationUnit.name_],
            greycat.types_by_name[core.function.name_],
            greycat.types_by_name[core.Tensor.name_],
            greycat.types_by_name[core.ErrorCode.name_],
            greycat.types_by_name[core.NodeInfo.name_],
            greycat.types_by_name[core.Error.name_],
            greycat.types_by_name[io.TextReader.name_],
            greycat.types_by_name[io.SmtpMode.name_],
            greycat.types_by_name[io.GcbReader.name_],
            greycat.types_by_name[io.CsvStatistics.name_],
            greycat.types_by_name[io.CsvAnalysisConfig.name_],
            greycat.types_by_name[io.TextWriter.name_],
            greycat.types_by_name[io.CsvWriter.name_],
            greycat.types_by_name[io.HttpMethod.name_],
            greycat.types_by_name[io.SmtpAuth.name_],
            greycat.types_by_name[io.Email.name_],
            greycat.types_by_name[io.Url.name_],
            greycat.types_by_name[io.Smtp.name_],
            greycat.types_by_name[io.Reader.name_],
            greycat.types_by_name[io.CsvColumnStatistics.name_],
            greycat.types_by_name[io.FileWalker.name_],
            greycat.types_by_name[io.HttpResponse.name_],
            greycat.types_by_name[io.JsonWriter.name_],
            greycat.types_by_name[io.Json.name_],
            greycat.types_by_name[io.CsvSharding.name_],
            greycat.types_by_name[io.Csv.name_],
            greycat.types_by_name[io.Writer.name_],
            greycat.types_by_name[io.JsonReader.name_],
            greycat.types_by_name[io.CsvReader.name_],
            greycat.types_by_name[io.XmlReader.name_],
            greycat.types_by_name[io.Http.name_],
            greycat.types_by_name[io.GcbWriter.name_],
            greycat.types_by_name[io.HttpRequest.name_],
            greycat.types_by_name[io.CsvFormat.name_],
            greycat.types_by_name[io.File.name_],
            greycat.types_by_name[runtime.Role.name_],
            greycat.types_by_name[runtime.Month.name_],
            greycat.types_by_name[runtime.Runtime.name_],
            greycat.types_by_name[runtime.FixedPeriodicity.name_],
            greycat.types_by_name[runtime.DateTuple.name_],
            greycat.types_by_name[runtime.Frame.name_],
            greycat.types_by_name[runtime.Log.name_],
            greycat.types_by_name[runtime.MediaTypeObject.name_],
            greycat.types_by_name[runtime.UserGroupPolicyType.name_],
            greycat.types_by_name[runtime.SecurityEntity.name_],
            greycat.types_by_name[runtime.RequestBodyObject.name_],
            greycat.types_by_name[runtime.OperationObject.name_],
            greycat.types_by_name[runtime.ResponseObject.name_],
            greycat.types_by_name[runtime.UserCredential.name_],
            greycat.types_by_name[runtime.TaskStatus.name_],
            greycat.types_by_name[runtime.DayOfWeek.name_],
            greycat.types_by_name[runtime.UserGroup.name_],
            greycat.types_by_name[runtime.PathItemObject.name_],
            greycat.types_by_name[runtime.SecurityPolicy.name_],
            greycat.types_by_name[runtime.OpenIDConnect.name_],
            greycat.types_by_name[runtime.Debug.name_],
            greycat.types_by_name[runtime.YearlyPeriodicity.name_],
            greycat.types_by_name[runtime.OpenApi.name_],
            greycat.types_by_name[runtime.License.name_],
            greycat.types_by_name[runtime.ComponentsObject.name_],
            greycat.types_by_name[runtime.UserGroupPolicy.name_],
            greycat.types_by_name[runtime.MonthlyPeriodicity.name_],
            greycat.types_by_name[runtime.ResponseCode.name_],
            greycat.types_by_name[runtime.OpenApiVersion.name_],
            greycat.types_by_name[runtime.Variable.name_],
            greycat.types_by_name[runtime.MergeStrategy.name_],
            greycat.types_by_name[runtime.InfoObject.name_],
            greycat.types_by_name[runtime.DailyPeriodicity.name_],
            greycat.types_by_name[runtime.LicenseType.name_],
            greycat.types_by_name[runtime.Scheduler.name_],
            greycat.types_by_name[runtime.PeriodicOptions.name_],
            greycat.types_by_name[runtime.HeaderObject.name_],
            greycat.types_by_name[runtime.ChildProcess.name_],
            greycat.types_by_name[runtime.SchemaObject.name_],
            greycat.types_by_name[runtime.Permission.name_],
            greycat.types_by_name[runtime.Task.name_],
            greycat.types_by_name[runtime.System.name_],
            greycat.types_by_name[runtime.SecurityFields.name_],
            greycat.types_by_name[runtime.LogDataUsage.name_],
            greycat.types_by_name[runtime.LogLevel.name_],
            greycat.types_by_name[runtime.PeriodicTask.name_],
            greycat.types_by_name[runtime.User.name_],
            greycat.types_by_name[runtime.OpenApiV3.name_],
            greycat.types_by_name[runtime.SchemaFormat.name_],
            greycat.types_by_name[runtime.SchemaType.name_],
            greycat.types_by_name[runtime.Periodicity.name_],
            greycat.types_by_name[runtime.ChildProcessResult.name_],
            greycat.types_by_name[runtime.RuntimeInfo.name_],
            greycat.types_by_name[runtime.Job.name_],
            greycat.types_by_name[runtime.WeeklyPeriodicity.name_],
            greycat.types_by_name[util.QuantizerSlotBound.name_],
            greycat.types_by_name[util.Histogram.name_],
            greycat.types_by_name[util.Quantizer.name_],
            greycat.types_by_name[util.SlidingWindow.name_],
            greycat.types_by_name[util.LinearQuantizer.name_],
            greycat.types_by_name[util.Stack.name_],
            greycat.types_by_name[util.Random.name_],
            greycat.types_by_name[util.MultiQuantizer.name_],
            greycat.types_by_name[util.Assert.name_],
            greycat.types_by_name[util.Plot.name_],
            greycat.types_by_name[util.CustomQuantizer.name_],
            greycat.types_by_name[util.TimeWindow.name_],
            greycat.types_by_name[util.Queue.name_],
            greycat.types_by_name[util.Gaussian.name_],
            greycat.types_by_name[util.GaussianProfile.name_],
            greycat.types_by_name[util.Crypto.name_],
            greycat.types_by_name[util.HistogramBin.name_],
            greycat.types_by_name[util.HistogramStats.name_],
            greycat.types_by_name[util.ProgressTracker.name_],
            greycat.types_by_name[util.GaussianProfileSlot.name_],
            greycat.types_by_name[util.LogQuantizer.name_],
        ]
        self.mapped[0].resolve_generated_offsets("vectors", "values", "count", "max_level", "entry_index", "vertices", "rng", "distance")
        self.mapped[2].resolve_generated_offset_with_values("i32", 4, "i64", 8, "f32", 4, "f64", 8, "c64", 8, "c128", 16)
        self.mapped[5].resolve_generated_offsets("key", "value", "next")
        self.mapped[7].resolve_generated_offset_with_values("p1", float.fromhex("0x1p+0"), "p10", float.fromhex("0x1.999999999999ap-4"), "p100", float.fromhex("0x1.47ae147ae147bp-7"), "p1000", float.fromhex("0x1.0624dd2f1a9fcp-10"), "p10000", float.fromhex("0x1.a36e2eb1c432dp-14"), "p100000", float.fromhex("0x1.4f8b588e368f1p-17"), "p1000000", float.fromhex("0x1.0c6f7a0b5ed8dp-20"), "p10000000", float.fromhex("0x1.ad7f29abcaf48p-24"), "p100000000", float.fromhex("0x1.5798ee2308c3ap-27"), "p1000000000", float.fromhex("0x1.12e0be826d695p-30"), "p10000000000", float.fromhex("0x1.b7cdfd9d7bdbbp-34"))
        self.mapped[13].resolve_generated_offset_with_values("year", 0, "month", 1, "day", 2, "hour", 3, "minute", 4, "second", 5, "microsecond", 6)
        self.mapped[15].resolve_generated_offset_with_values("euclidean", None, "cosine", None)
        self.mapped[17].resolve_generated_offset_with_values("UTC", None, "Africa/Abidjan", None, "Africa/Accra", None, "Africa/Addis_Ababa", None, "Africa/Algiers", None, "Africa/Asmara", None, "Africa/Asmera", None, "Africa/Bamako", None, "Africa/Bangui", None, "Africa/Banjul", None, "Africa/Bissau", None, "Africa/Blantyre", None, "Africa/Brazzaville", None, "Africa/Bujumbura", None, "Africa/Cairo", None, "Africa/Casablanca", None, "Africa/Ceuta", None, "Africa/Conakry", None, "Africa/Dakar", None, "Africa/Dar_es_Salaam", None, "Africa/Djibouti", None, "Africa/Douala", None, "Africa/El_Aaiun", None, "Africa/Freetown", None, "Africa/Gaborone", None, "Africa/Harare", None, "Africa/Johannesburg", None, "Africa/Juba", None, "Africa/Kampala", None, "Africa/Khartoum", None, "Africa/Kigali", None, "Africa/Kinshasa", None, "Africa/Lagos", None, "Africa/Libreville", None, "Africa/Lome", None, "Africa/Luanda", None, "Africa/Lubumbashi", None, "Africa/Lusaka", None, "Africa/Malabo", None, "Africa/Maputo", None, "Africa/Maseru", None, "Africa/Mbabane", None, "Africa/Mogadishu", None, "Africa/Monrovia", None, "Africa/Nairobi", None, "Africa/Ndjamena", None, "Africa/Niamey", None, "Africa/Nouakchott", None, "Africa/Ouagadougou", None, "Africa/Porto-Novo", None, "Africa/Sao_Tome", None, "Africa/Timbuktu", None, "Africa/Tripoli", None, "Africa/Tunis", None, "Africa/Windhoek", None, "America/Adak", None, "America/Anchorage", None, "America/Anguilla", None, "America/Antigua", None, "America/Araguaina", None, "America/Argentina/Buenos_Aires", None, "America/Argentina/Catamarca", None, "America/Argentina/ComodRivadavia", None, "America/Argentina/Cordoba", None, "America/Argentina/Jujuy", None, "America/Argentina/La_Rioja", None, "America/Argentina/Mendoza", None, "America/Argentina/Rio_Gallegos", None, "America/Argentina/Salta", None, "America/Argentina/San_Juan", None, "America/Argentina/San_Luis", None, "America/Argentina/Tucuman", None, "America/Argentina/Ushuaia", None, "America/Aruba", None, "America/Asuncion", None, "America/Atikokan", None, "America/Atka", None, "America/Bahia", None, "America/Bahia_Banderas", None, "America/Barbados", None, "America/Belem", None, "America/Belize", None, "America/Blanc-Sablon", None, "America/Boa_Vista", None, "America/Bogota", None, "America/Boise", None, "America/Buenos_Aires", None, "America/Cambridge_Bay", None, "America/Campo_Grande", None, "America/Cancun", None, "America/Caracas", None, "America/Catamarca", None, "America/Cayenne", None, "America/Cayman", None, "America/Chicago", None, "America/Chihuahua", None, "America/Ciudad_Juarez", None, "America/Coral_Harbour", None, "America/Cordoba", None, "America/Costa_Rica", None, "America/Coyhaique", None, "America/Creston", None, "America/Cuiaba", None, "America/Curacao", None, "America/Danmarkshavn", None, "America/Dawson", None, "America/Dawson_Creek", None, "America/Denver", None, "America/Detroit", None, "America/Dominica", None, "America/Edmonton", None, "America/Eirunepe", None, "America/El_Salvador", None, "America/Ensenada", None, "America/Fort_Nelson", None, "America/Fort_Wayne", None, "America/Fortaleza", None, "America/Glace_Bay", None, "America/Godthab", None, "America/Goose_Bay", None, "America/Grand_Turk", None, "America/Grenada", None, "America/Guadeloupe", None, "America/Guatemala", None, "America/Guayaquil", None, "America/Guyana", None, "America/Halifax", None, "America/Havana", None, "America/Hermosillo", None, "America/Indiana/Indianapolis", None, "America/Indiana/Knox", None, "America/Indiana/Marengo", None, "America/Indiana/Petersburg", None, "America/Indiana/Tell_City", None, "America/Indiana/Vevay", None, "America/Indiana/Vincennes", None, "America/Indiana/Winamac", None, "America/Indianapolis", None, "America/Inuvik", None, "America/Iqaluit", None, "America/Jamaica", None, "America/Jujuy", None, "America/Juneau", None, "America/Kentucky/Louisville", None, "America/Kentucky/Monticello", None, "America/Knox_IN", None, "America/Kralendijk", None, "America/La_Paz", None, "America/Lima", None, "America/Los_Angeles", None, "America/Louisville", None, "America/Lower_Princes", None, "America/Maceio", None, "America/Managua", None, "America/Manaus", None, "America/Marigot", None, "America/Martinique", None, "America/Matamoros", None, "America/Mazatlan", None, "America/Mendoza", None, "America/Menominee", None, "America/Merida", None, "America/Metlakatla", None, "America/Mexico_City", None, "America/Miquelon", None, "America/Moncton", None, "America/Monterrey", None, "America/Montevideo", None, "America/Montreal", None, "America/Montserrat", None, "America/Nassau", None, "America/New_York", None, "America/Nipigon", None, "America/Nome", None, "America/Noronha", None, "America/North_Dakota/Beulah", None, "America/North_Dakota/Center", None, "America/North_Dakota/New_Salem", None, "America/Nuuk", None, "America/Ojinaga", None, "America/Panama", None, "America/Pangnirtung", None, "America/Paramaribo", None, "America/Phoenix", None, "America/Port-au-Prince", None, "America/Port_of_Spain", None, "America/Porto_Acre", None, "America/Porto_Velho", None, "America/Puerto_Rico", None, "America/Punta_Arenas", None, "America/Rainy_River", None, "America/Rankin_Inlet", None, "America/Recife", None, "America/Regina", None, "America/Resolute", None, "America/Rio_Branco", None, "America/Rosario", None, "America/Santa_Isabel", None, "America/Santarem", None, "America/Santiago", None, "America/Santo_Domingo", None, "America/Sao_Paulo", None, "America/Scoresbysund", None, "America/Shiprock", None, "America/Sitka", None, "America/St_Barthelemy", None, "America/St_Johns", None, "America/St_Kitts", None, "America/St_Lucia", None, "America/St_Thomas", None, "America/St_Vincent", None, "America/Swift_Current", None, "America/Tegucigalpa", None, "America/Thule", None, "America/Thunder_Bay", None, "America/Tijuana", None, "America/Toronto", None, "America/Tortola", None, "America/Vancouver", None, "America/Virgin", None, "America/Whitehorse", None, "America/Winnipeg", None, "America/Yakutat", None, "America/Yellowknife", None, "Antarctica/Casey", None, "Antarctica/Davis", None, "Antarctica/DumontDUrville", None, "Antarctica/Macquarie", None, "Antarctica/Mawson", None, "Antarctica/McMurdo", None, "Antarctica/Palmer", None, "Antarctica/Rothera", None, "Antarctica/South_Pole", None, "Antarctica/Syowa", None, "Antarctica/Troll", None, "Antarctica/Vostok", None, "Arctic/Longyearbyen", None, "Asia/Aden", None, "Asia/Almaty", None, "Asia/Amman", None, "Asia/Anadyr", None, "Asia/Aqtau", None, "Asia/Aqtobe", None, "Asia/Ashgabat", None, "Asia/Ashkhabad", None, "Asia/Atyrau", None, "Asia/Baghdad", None, "Asia/Bahrain", None, "Asia/Baku", None, "Asia/Bangkok", None, "Asia/Barnaul", None, "Asia/Beirut", None, "Asia/Bishkek", None, "Asia/Brunei", None, "Asia/Calcutta", None, "Asia/Chita", None, "Asia/Choibalsan", None, "Asia/Chongqing", None, "Asia/Chungking", None, "Asia/Colombo", None, "Asia/Dacca", None, "Asia/Damascus", None, "Asia/Dhaka", None, "Asia/Dili", None, "Asia/Dubai", None, "Asia/Dushanbe", None, "Asia/Famagusta", None, "Asia/Gaza", None, "Asia/Harbin", None, "Asia/Hebron", None, "Asia/Ho_Chi_Minh", None, "Asia/Hong_Kong", None, "Asia/Hovd", None, "Asia/Irkutsk", None, "Asia/Istanbul", None, "Asia/Jakarta", None, "Asia/Jayapura", None, "Asia/Jerusalem", None, "Asia/Kabul", None, "Asia/Kamchatka", None, "Asia/Karachi", None, "Asia/Kashgar", None, "Asia/Kathmandu", None, "Asia/Katmandu", None, "Asia/Khandyga", None, "Asia/Kolkata", None, "Asia/Krasnoyarsk", None, "Asia/Kuala_Lumpur", None, "Asia/Kuching", None, "Asia/Kuwait", None, "Asia/Macao", None, "Asia/Macau", None, "Asia/Magadan", None, "Asia/Makassar", None, "Asia/Manila", None, "Asia/Muscat", None, "Asia/Nicosia", None, "Asia/Novokuznetsk", None, "Asia/Novosibirsk", None, "Asia/Omsk", None, "Asia/Oral", None, "Asia/Phnom_Penh", None, "Asia/Pontianak", None, "Asia/Pyongyang", None, "Asia/Qatar", None, "Asia/Qostanay", None, "Asia/Qyzylorda", None, "Asia/Rangoon", None, "Asia/Riyadh", None, "Asia/Saigon", None, "Asia/Sakhalin", None, "Asia/Samarkand", None, "Asia/Seoul", None, "Asia/Shanghai", None, "Asia/Singapore", None, "Asia/Srednekolymsk", None, "Asia/Taipei", None, "Asia/Tashkent", None, "Asia/Tbilisi", None, "Asia/Tehran", None, "Asia/Tel_Aviv", None, "Asia/Thimbu", None, "Asia/Thimphu", None, "Asia/Tokyo", None, "Asia/Tomsk", None, "Asia/Ujung_Pandang", None, "Asia/Ulaanbaatar", None, "Asia/Ulan_Bator", None, "Asia/Urumqi", None, "Asia/Ust-Nera", None, "Asia/Vientiane", None, "Asia/Vladivostok", None, "Asia/Yakutsk", None, "Asia/Yangon", None, "Asia/Yekaterinburg", None, "Asia/Yerevan", None, "Atlantic/Azores", None, "Atlantic/Bermuda", None, "Atlantic/Canary", None, "Atlantic/Cape_Verde", None, "Atlantic/Faeroe", None, "Atlantic/Faroe", None, "Atlantic/Jan_Mayen", None, "Atlantic/Madeira", None, "Atlantic/Reykjavik", None, "Atlantic/South_Georgia", None, "Atlantic/St_Helena", None, "Atlantic/Stanley", None, "Australia/ACT", None, "Australia/Adelaide", None, "Australia/Brisbane", None, "Australia/Broken_Hill", None, "Australia/Canberra", None, "Australia/Currie", None, "Australia/Darwin", None, "Australia/Eucla", None, "Australia/Hobart", None, "Australia/LHI", None, "Australia/Lindeman", None, "Australia/Lord_Howe", None, "Australia/Melbourne", None, "Australia/NSW", None, "Australia/North", None, "Australia/Perth", None, "Australia/Queensland", None, "Australia/South", None, "Australia/Sydney", None, "Australia/Tasmania", None, "Australia/Victoria", None, "Australia/West", None, "Australia/Yancowinna", None, "Brazil/Acre", None, "Brazil/DeNoronha", None, "Brazil/East", None, "Brazil/West", None, "CET", None, "CST6CDT", None, "Canada/Atlantic", None, "Canada/Central", None, "Canada/Eastern", None, "Canada/Mountain", None, "Canada/Newfoundland", None, "Canada/Pacific", None, "Canada/Saskatchewan", None, "Canada/Yukon", None, "Chile/Continental", None, "Chile/EasterIsland", None, "Cuba", None, "EET", None, "EST", None, "EST5EDT", None, "Egypt", None, "Eire", None, "Etc/GMT", None, "Etc/GMT+0", None, "Etc/GMT+1", None, "Etc/GMT+10", None, "Etc/GMT+11", None, "Etc/GMT+12", None, "Etc/GMT+2", None, "Etc/GMT+3", None, "Etc/GMT+4", None, "Etc/GMT+5", None, "Etc/GMT+6", None, "Etc/GMT+7", None, "Etc/GMT+8", None, "Etc/GMT+9", None, "Etc/GMT-0", None, "Etc/GMT-1", None, "Etc/GMT-10", None, "Etc/GMT-11", None, "Etc/GMT-12", None, "Etc/GMT-13", None, "Etc/GMT-14", None, "Etc/GMT-2", None, "Etc/GMT-3", None, "Etc/GMT-4", None, "Etc/GMT-5", None, "Etc/GMT-6", None, "Etc/GMT-7", None, "Etc/GMT-8", None, "Etc/GMT-9", None, "Etc/GMT0", None, "Etc/Greenwich", None, "Etc/UCT", None, "Etc/UTC", None, "Etc/Universal", None, "Etc/Zulu", None, "Europe/Amsterdam", None, "Europe/Andorra", None, "Europe/Astrakhan", None, "Europe/Athens", None, "Europe/Belfast", None, "Europe/Belgrade", None, "Europe/Berlin", None, "Europe/Bratislava", None, "Europe/Brussels", None, "Europe/Bucharest", None, "Europe/Budapest", None, "Europe/Busingen", None, "Europe/Chisinau", None, "Europe/Copenhagen", None, "Europe/Dublin", None, "Europe/Gibraltar", None, "Europe/Guernsey", None, "Europe/Helsinki", None, "Europe/Isle_of_Man", None, "Europe/Istanbul", None, "Europe/Jersey", None, "Europe/Kaliningrad", None, "Europe/Kiev", None, "Europe/Kirov", None, "Europe/Kyiv", None, "Europe/Lisbon", None, "Europe/Ljubljana", None, "Europe/London", None, "Europe/Luxembourg", None, "Europe/Madrid", None, "Europe/Malta", None, "Europe/Mariehamn", None, "Europe/Minsk", None, "Europe/Monaco", None, "Europe/Moscow", None, "Europe/Nicosia", None, "Europe/Oslo", None, "Europe/Paris", None, "Europe/Podgorica", None, "Europe/Prague", None, "Europe/Riga", None, "Europe/Rome", None, "Europe/Samara", None, "Europe/San_Marino", None, "Europe/Sarajevo", None, "Europe/Saratov", None, "Europe/Simferopol", None, "Europe/Skopje", None, "Europe/Sofia", None, "Europe/Stockholm", None, "Europe/Tallinn", None, "Europe/Tirane", None, "Europe/Tiraspol", None, "Europe/Ulyanovsk", None, "Europe/Uzhgorod", None, "Europe/Vaduz", None, "Europe/Vatican", None, "Europe/Vienna", None, "Europe/Vilnius", None, "Europe/Volgograd", None, "Europe/Warsaw", None, "Europe/Zagreb", None, "Europe/Zaporozhye", None, "Europe/Zurich", None, "Factory", None, "GB", None, "GB-Eire", None, "GMT", None, "GMT+0", None, "GMT-0", None, "GMT0", None, "Greenwich", None, "HST", None, "Hongkong", None, "Iceland", None, "Indian/Antananarivo", None, "Indian/Chagos", None, "Indian/Christmas", None, "Indian/Cocos", None, "Indian/Comoro", None, "Indian/Kerguelen", None, "Indian/Mahe", None, "Indian/Maldives", None, "Indian/Mauritius", None, "Indian/Mayotte", None, "Indian/Reunion", None, "Iran", None, "Israel", None, "Jamaica", None, "Japan", None, "Kwajalein", None, "Libya", None, "MET", None, "MST", None, "MST7MDT", None, "Mexico/BajaNorte", None, "Mexico/BajaSur", None, "Mexico/General", None, "NZ", None, "NZ-CHAT", None, "Navajo", None, "PRC", None, "PST8PDT", None, "Pacific/Apia", None, "Pacific/Auckland", None, "Pacific/Bougainville", None, "Pacific/Chatham", None, "Pacific/Chuuk", None, "Pacific/Easter", None, "Pacific/Efate", None, "Pacific/Enderbury", None, "Pacific/Fakaofo", None, "Pacific/Fiji", None, "Pacific/Funafuti", None, "Pacific/Galapagos", None, "Pacific/Gambier", None, "Pacific/Guadalcanal", None, "Pacific/Guam", None, "Pacific/Honolulu", None, "Pacific/Johnston", None, "Pacific/Kanton", None, "Pacific/Kiritimati", None, "Pacific/Kosrae", None, "Pacific/Kwajalein", None, "Pacific/Majuro", None, "Pacific/Marquesas", None, "Pacific/Midway", None, "Pacific/Nauru", None, "Pacific/Niue", None, "Pacific/Norfolk", None, "Pacific/Noumea", None, "Pacific/Pago_Pago", None, "Pacific/Palau", None, "Pacific/Pitcairn", None, "Pacific/Pohnpei", None, "Pacific/Ponape", None, "Pacific/Port_Moresby", None, "Pacific/Rarotonga", None, "Pacific/Saipan", None, "Pacific/Samoa", None, "Pacific/Tahiti", None, "Pacific/Tarawa", None, "Pacific/Tongatapu", None, "Pacific/Truk", None, "Pacific/Wake", None, "Pacific/Wallis", None, "Pacific/Yap", None, "Poland", None, "Portugal", None, "ROC", None, "ROK", None, "Singapore", None, "Turkey", None, "UCT", None, "US/Alaska", None, "US/Aleutian", None, "US/Arizona", None, "US/Central", None, "US/East-Indiana", None, "US/Eastern", None, "US/Hawaii", None, "US/Indiana-Starke", None, "US/Michigan", None, "US/Mountain", None, "US/Pacific", None, "US/Samoa", None, "Universal", None, "W-SU", None, "WET", None, "Zulu", None)
        self.mapped[21].resolve_generated_offset_with_values("fixed", 0, "fixed_reg", 1, "adaptative", 2, "dense", 3)
        self.mapped[23].resolve_generated_offsets("level", "neighbours")
        self.mapped[24].resolve_generated_offsets("column", "extractors")
        self.mapped[25].resolve_generated_offsets("module", "function", "line", "column")
        self.mapped[27].resolve_generated_offsets("sw", "ne")
        self.mapped[33].resolve_generated_offsets("x", "y")
        self.mapped[34].resolve_generated_offsets("points")
        self.mapped[35].resolve_generated_offset_with_values("asc", None, "desc", None)
        self.mapped[36].resolve_generated_offsets("n", "req_time")
        self.mapped[38].resolve_generated_offsets("center", "radius")
        self.mapped[40].resolve_generated_offsets("year", "month", "day", "hour", "minute", "second", "microsecond")
        self.mapped[41].resolve_generated_offsets("key", "value", "distance")
        self.mapped[42].resolve_generated_offset_with_values("microseconds", 1, "milliseconds", 1000, "seconds", 1000000, "minutes", 60000000, "hours", 3600000000, "days", 86400000000)
        self.mapped[45].resolve_generated_offset_with_values("none", 0, "interrupted", 1, "await", 2, "timeout", 6, "forbidden", 7, "runtime_error", 8)
        self.mapped[46].resolve_generated_offsets("size", "from", "to")
        self.mapped[47].resolve_generated_offsets("message", "stack")
        self.mapped[48].resolve_generated_offsets("path", "pos")
        self.mapped[49].resolve_generated_offset_with_values("plain", 0, "ssl_tls", 1, "starttls", 2)
        self.mapped[50].resolve_generated_offsets("path", "pos")
        self.mapped[51].resolve_generated_offsets("header_lines", "separator", "string_delimiter", "decimal_separator", "thousands_separator", "columns", "line_count", "fail_count", "file_count")
        self.mapped[52].resolve_generated_offsets("header_lines", "separator", "string_delimiter", "decimal_separator", "thousands_separator", "row_limit", "enumerable_limit", "date_check_limit", "date_formats")
        self.mapped[53].resolve_generated_offsets("path", "append")
        self.mapped[54].resolve_generated_offsets("path", "append", "format")
        self.mapped[55].resolve_generated_offset_with_values("GET", None, "HEAD", None, "POST", None, "PUT", None, "DELETE", None, "CONNECT", None, "OPTIONS", None, "TRACE", None, "PATCH", None)
        self.mapped[56].resolve_generated_offset_with_values("none", 0, "plain", 1, "login", 2)
        self.mapped[57].resolve_generated_offsets("from", "subject", "body", "body_is_html", "to", "cc", "bcc")
        self.mapped[58].resolve_generated_offsets("protocol", "host", "port", "path", "params", "hash")
        self.mapped[59].resolve_generated_offsets("host", "port", "mode", "authenticate", "user", "pass")
        self.mapped[60].resolve_generated_offsets("path", "pos")
        self.mapped[61].resolve_generated_offsets("name", "example", "null_count", "bool_count", "int_count", "float_count", "string_count", "date_count", "date_format_count", "enumerable_count", "profile")
        self.mapped[62].resolve_generated_offsets("path")
        self.mapped[63].resolve_generated_offsets("status_code", "headers", "content", "error_msg")
        self.mapped[64].resolve_generated_offsets("path", "append")
        self.mapped[66].resolve_generated_offsets("id", "column", "modulo")
        self.mapped[68].resolve_generated_offsets("path", "append")
        self.mapped[69].resolve_generated_offsets("path", "pos")
        self.mapped[70].resolve_generated_offsets("path", "pos", "format", "sharding")
        self.mapped[71].resolve_generated_offsets("path", "pos")
        self.mapped[73].resolve_generated_offsets("path", "append")
        self.mapped[74].resolve_generated_offsets("method", "url", "headers", "body")
        self.mapped[75].resolve_generated_offsets("header_lines", "separator", "string_delimiter", "decimal_separator", "thousands_separator", "trim", "format", "tz", "strict", "nearest_time")
        self.mapped[76].resolve_generated_offsets("path", "size", "last_modification")
        self.mapped[77].resolve_generated_offsets("name", "permissions")
        self.mapped[78].resolve_generated_offset_with_values("Jan", 0, "Feb", 1, "Mar", 2, "Apr", 3, "May", 4, "Jun", 5, "Jul", 6, "Aug", 7, "Sep", 8, "Oct", 9, "Nov", 10, "Dec", 11)
        self.mapped[80].resolve_generated_offsets("every")
        self.mapped[81].resolve_generated_offsets("day", "month")
        self.mapped[82].resolve_generated_offsets("module", "type", "function", "src", "line", "column", "scope")
        self.mapped[83].resolve_generated_offsets("level", "time", "user_id", "id", "id2", "src", "data")
        self.mapped[84].resolve_generated_offsets("schema")
        self.mapped[85].resolve_generated_offset_with_values("read", None, "write", None, "execute", None)
        self.mapped[86].resolve_generated_offsets("id", "name", "activated")
        self.mapped[87].resolve_generated_offsets("content", "required")
        self.mapped[88].resolve_generated_offsets("requestBody", "responses")
        self.mapped[89].resolve_generated_offsets("description", "headers", "content")
        self.mapped[90].resolve_generated_offsets("offset", "pass")
        self.mapped[91].resolve_generated_offset_with_values("empty", None, "waiting", None, "running", None, "await", None, "cancelled", None, "error", None, "ended", None, "ended_with_errors", None, "breakpoint", None)
        self.mapped[92].resolve_generated_offset_with_values("Mon", 0, "Tue", 1, "Wed", 2, "Thu", 3, "Fri", 4, "Sat", 5, "Sun", 6)
        self.mapped[93].resolve_generated_offsets("id", "name", "activated")
        self.mapped[94].resolve_generated_offsets("description", "post")
        self.mapped[95].resolve_generated_offsets("entities", "credentials", "fields", "keys", "keys_last_refresh")
        self.mapped[96].resolve_generated_offsets("url", "clientId")
        self.mapped[97].resolve_generated_offsets("id", "frames", "root")
        self.mapped[98].resolve_generated_offsets("dates", "timezone")
        self.mapped[100].resolve_generated_offsets("name", "start", "end", "company", "max_memory", "extra_1", "extra_2", "type")
        self.mapped[101].resolve_generated_offsets("schemas")
        self.mapped[102].resolve_generated_offsets("group_id", "type")
        self.mapped[103].resolve_generated_offsets("days", "daily")
        self.mapped[104].resolve_generated_offset_with_values("200", None, "400", None, "404", None)
        self.mapped[105].resolve_generated_offset_with_values("3.0.4", None)
        self.mapped[106].resolve_generated_offsets("name", "value")
        self.mapped[107].resolve_generated_offset_with_values("strict", None, "first_wins", None, "last_wins", None)
        self.mapped[108].resolve_generated_offsets("title", "version")
        self.mapped[109].resolve_generated_offsets("hour", "minute", "second", "timezone")
        self.mapped[110].resolve_generated_offset_with_values("community", None, "enterprise", None, "testing", None)
        self.mapped[112].resolve_generated_offsets("activated", "start", "max_duration")
        self.mapped[113].resolve_generated_offsets("description", "required")
        self.mapped[114].resolve_generated_offsets("pid")
        self.mapped[115].resolve_generated_offsets("$ref", "type", "format", "nullable", "properties", "required", "items", "oneOf", "allOf", "minItems", "maxItems", "enum", "additionalProperties")
        self.mapped[116].resolve_generated_offsets("name", "description")
        self.mapped[117].resolve_generated_offsets("user_id", "task_id", "mod", "type", "fun", "creation", "start", "duration", "status", "progress")
        self.mapped[119].resolve_generated_offsets("email", "name", "first_name", "last_name", "roles", "groups")
        self.mapped[120].resolve_generated_offsets("read_bytes", "read_hits", "read_wasted", "write_bytes", "write_hits", "cache_bytes", "cache_hits")
        self.mapped[121].resolve_generated_offset_with_values("error", None, "warn", None, "info", None, "perf", None, "trace", None)
        self.mapped[122].resolve_generated_offsets("function", "periodicity", "options", "is_active", "next_execution", "execution_count")
        self.mapped[123].resolve_generated_offsets("id", "name", "activated", "full_name", "email", "role", "groups", "groups_flags", "external")
        self.mapped[124].resolve_generated_offsets("openapi", "info", "paths", "components")
        self.mapped[125].resolve_generated_offset_with_values("int32", None, "int64", None, "float", None, "double", None, "byte", None, "binary", None, "date", None, "date-time", None, "password", None)
        self.mapped[126].resolve_generated_offset_with_values("string", None, "number", None, "integer", None, "boolean", None, "object", None, "array", None)
        self.mapped[128].resolve_generated_offsets("code", "stdout", "stderr")
        self.mapped[129].resolve_generated_offsets("version", "program_version", "arch", "timezone", "license", "io_threads", "bg_threads", "fg_threads", "mem_total", "mem_worker", "disk_data_bytes")
        self.mapped[130].resolve_generated_offsets("function", "arguments")
        self.mapped[131].resolve_generated_offsets("days", "daily")
        self.mapped[132].resolve_generated_offsets("min", "max", "center")
        self.mapped[133].resolve_generated_offsets("quantizer", "bins", "nb_rejected", "nb_accepted", "min", "max", "sum", "sumsq")
        self.mapped[135].resolve_generated_offsets("values", "span", "sum", "sumsq", "field")
        self.mapped[136].resolve_generated_offsets("min", "max", "bins", "open")
        self.mapped[137].resolve_generated_offsets("values")
        self.mapped[138].resolve_generated_offsets("seed", "v")
        self.mapped[139].resolve_generated_offsets("quantizers")
        self.mapped[142].resolve_generated_offsets("min", "max", "step_starts", "open")
        self.mapped[143].resolve_generated_offsets("values", "span", "sum", "sumsq", "field")
        self.mapped[144].resolve_generated_offsets("values", "capacity")
        self.mapped[145].resolve_generated_offsets("sum", "sumsq", "count", "min", "max")
        self.mapped[146].resolve_generated_offsets("quantizer", "precision", "bins", "value_min", "nb_rejected")
        self.mapped[148].resolve_generated_offsets("bin", "count", "ratio", "cumulative_count", "cumulative_ratio")
        self.mapped[149].resolve_generated_offsets("min", "max", "whisker_low", "whisker_high", "percentile1", "percentile5", "percentile10", "percentile20", "percentile25", "percentile50", "percentile75", "percentile80", "percentile90", "percentile95", "percentile99", "sum", "avg", "std", "size")
        self.mapped[150].resolve_generated_offsets("start", "total", "counter", "duration", "progress", "speed", "remaining")
        self.mapped[151].resolve_generated_offsets("sum", "sumsq", "count")
        self.mapped[152].resolve_generated_offsets("min", "max", "bins", "open")
