# AUTO-GENERATED FILE PLEASE DO NOT MODIFY MANUALLY
from __future__ import annotations
from ctypes import *
from typing import *
from greycat.greycat import GreyCat
try:
    from greycat.std_n import std_n
except ModuleNotFoundError:
    pass


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
            __indices_by_values: dict[str, int] = {
                "Africa/Abidjan": 0,
                "Africa/Accra": 1,
                "Africa/Addis_Ababa": 2,
                "Africa/Algiers": 3,
                "Africa/Asmara": 4,
                "Africa/Asmera": 5,
                "Africa/Bamako": 6,
                "Africa/Bangui": 7,
                "Africa/Banjul": 8,
                "Africa/Bissau": 9,
                "Africa/Blantyre": 10,
                "Africa/Brazzaville": 11,
                "Africa/Bujumbura": 12,
                "Africa/Cairo": 13,
                "Africa/Casablanca": 14,
                "Africa/Ceuta": 15,
                "Africa/Conakry": 16,
                "Africa/Dakar": 17,
                "Africa/Dar_es_Salaam": 18,
                "Africa/Djibouti": 19,
                "Africa/Douala": 20,
                "Africa/El_Aaiun": 21,
                "Africa/Freetown": 22,
                "Africa/Gaborone": 23,
                "Africa/Harare": 24,
                "Africa/Johannesburg": 25,
                "Africa/Juba": 26,
                "Africa/Kampala": 27,
                "Africa/Khartoum": 28,
                "Africa/Kigali": 29,
                "Africa/Kinshasa": 30,
                "Africa/Lagos": 31,
                "Africa/Libreville": 32,
                "Africa/Lome": 33,
                "Africa/Luanda": 34,
                "Africa/Lubumbashi": 35,
                "Africa/Lusaka": 36,
                "Africa/Malabo": 37,
                "Africa/Maputo": 38,
                "Africa/Maseru": 39,
                "Africa/Mbabane": 40,
                "Africa/Mogadishu": 41,
                "Africa/Monrovia": 42,
                "Africa/Nairobi": 43,
                "Africa/Ndjamena": 44,
                "Africa/Niamey": 45,
                "Africa/Nouakchott": 46,
                "Africa/Ouagadougou": 47,
                "Africa/Porto-Novo": 48,
                "Africa/Sao_Tome": 49,
                "Africa/Timbuktu": 50,
                "Africa/Tripoli": 51,
                "Africa/Tunis": 52,
                "Africa/Windhoek": 53,
                "America/Adak": 54,
                "America/Anchorage": 55,
                "America/Anguilla": 56,
                "America/Antigua": 57,
                "America/Araguaina": 58,
                "America/Argentina/Buenos_Aires": 59,
                "America/Argentina/Catamarca": 60,
                "America/Argentina/ComodRivadavia": 61,
                "America/Argentina/Cordoba": 62,
                "America/Argentina/Jujuy": 63,
                "America/Argentina/La_Rioja": 64,
                "America/Argentina/Mendoza": 65,
                "America/Argentina/Rio_Gallegos": 66,
                "America/Argentina/Salta": 67,
                "America/Argentina/San_Juan": 68,
                "America/Argentina/San_Luis": 69,
                "America/Argentina/Tucuman": 70,
                "America/Argentina/Ushuaia": 71,
                "America/Aruba": 72,
                "America/Asuncion": 73,
                "America/Atikokan": 74,
                "America/Atka": 75,
                "America/Bahia": 76,
                "America/Bahia_Banderas": 77,
                "America/Barbados": 78,
                "America/Belem": 79,
                "America/Belize": 80,
                "America/Blanc-Sablon": 81,
                "America/Boa_Vista": 82,
                "America/Bogota": 83,
                "America/Boise": 84,
                "America/Buenos_Aires": 85,
                "America/Cambridge_Bay": 86,
                "America/Campo_Grande": 87,
                "America/Cancun": 88,
                "America/Caracas": 89,
                "America/Catamarca": 90,
                "America/Cayenne": 91,
                "America/Cayman": 92,
                "America/Chicago": 93,
                "America/Chihuahua": 94,
                "America/Ciudad_Juarez": 95,
                "America/Coral_Harbour": 96,
                "America/Cordoba": 97,
                "America/Costa_Rica": 98,
                "America/Creston": 99,
                "America/Cuiaba": 100,
                "America/Curacao": 101,
                "America/Danmarkshavn": 102,
                "America/Dawson": 103,
                "America/Dawson_Creek": 104,
                "America/Denver": 105,
                "America/Detroit": 106,
                "America/Dominica": 107,
                "America/Edmonton": 108,
                "America/Eirunepe": 109,
                "America/El_Salvador": 110,
                "America/Ensenada": 111,
                "America/Fort_Nelson": 112,
                "America/Fort_Wayne": 113,
                "America/Fortaleza": 114,
                "America/Glace_Bay": 115,
                "America/Godthab": 116,
                "America/Goose_Bay": 117,
                "America/Grand_Turk": 118,
                "America/Grenada": 119,
                "America/Guadeloupe": 120,
                "America/Guatemala": 121,
                "America/Guayaquil": 122,
                "America/Guyana": 123,
                "America/Halifax": 124,
                "America/Havana": 125,
                "America/Hermosillo": 126,
                "America/Indiana/Indianapolis": 127,
                "America/Indiana/Knox": 128,
                "America/Indiana/Marengo": 129,
                "America/Indiana/Petersburg": 130,
                "America/Indiana/Tell_City": 131,
                "America/Indiana/Vevay": 132,
                "America/Indiana/Vincennes": 133,
                "America/Indiana/Winamac": 134,
                "America/Indianapolis": 135,
                "America/Inuvik": 136,
                "America/Iqaluit": 137,
                "America/Jamaica": 138,
                "America/Jujuy": 139,
                "America/Juneau": 140,
                "America/Kentucky/Louisville": 141,
                "America/Kentucky/Monticello": 142,
                "America/Knox_IN": 143,
                "America/Kralendijk": 144,
                "America/La_Paz": 145,
                "America/Lima": 146,
                "America/Los_Angeles": 147,
                "America/Louisville": 148,
                "America/Lower_Princes": 149,
                "America/Maceio": 150,
                "America/Managua": 151,
                "America/Manaus": 152,
                "America/Marigot": 153,
                "America/Martinique": 154,
                "America/Matamoros": 155,
                "America/Mazatlan": 156,
                "America/Mendoza": 157,
                "America/Menominee": 158,
                "America/Merida": 159,
                "America/Metlakatla": 160,
                "America/Mexico_City": 161,
                "America/Miquelon": 162,
                "America/Moncton": 163,
                "America/Monterrey": 164,
                "America/Montevideo": 165,
                "America/Montreal": 166,
                "America/Montserrat": 167,
                "America/Nassau": 168,
                "America/New_York": 169,
                "America/Nipigon": 170,
                "America/Nome": 171,
                "America/Noronha": 172,
                "America/North_Dakota/Beulah": 173,
                "America/North_Dakota/Center": 174,
                "America/North_Dakota/New_Salem": 175,
                "America/Nuuk": 176,
                "America/Ojinaga": 177,
                "America/Panama": 178,
                "America/Pangnirtung": 179,
                "America/Paramaribo": 180,
                "America/Phoenix": 181,
                "America/Port-au-Prince": 182,
                "America/Port_of_Spain": 183,
                "America/Porto_Acre": 184,
                "America/Porto_Velho": 185,
                "America/Puerto_Rico": 186,
                "America/Punta_Arenas": 187,
                "America/Rainy_River": 188,
                "America/Rankin_Inlet": 189,
                "America/Recife": 190,
                "America/Regina": 191,
                "America/Resolute": 192,
                "America/Rio_Branco": 193,
                "America/Rosario": 194,
                "America/Santa_Isabel": 195,
                "America/Santarem": 196,
                "America/Santiago": 197,
                "America/Santo_Domingo": 198,
                "America/Sao_Paulo": 199,
                "America/Scoresbysund": 200,
                "America/Shiprock": 201,
                "America/Sitka": 202,
                "America/St_Barthelemy": 203,
                "America/St_Johns": 204,
                "America/St_Kitts": 205,
                "America/St_Lucia": 206,
                "America/St_Thomas": 207,
                "America/St_Vincent": 208,
                "America/Swift_Current": 209,
                "America/Tegucigalpa": 210,
                "America/Thule": 211,
                "America/Thunder_Bay": 212,
                "America/Tijuana": 213,
                "America/Toronto": 214,
                "America/Tortola": 215,
                "America/Vancouver": 216,
                "America/Virgin": 217,
                "America/Whitehorse": 218,
                "America/Winnipeg": 219,
                "America/Yakutat": 220,
                "America/Yellowknife": 221,
                "Antarctica/Casey": 222,
                "Antarctica/Davis": 223,
                "Antarctica/DumontDUrville": 224,
                "Antarctica/Macquarie": 225,
                "Antarctica/Mawson": 226,
                "Antarctica/McMurdo": 227,
                "Antarctica/Palmer": 228,
                "Antarctica/Rothera": 229,
                "Antarctica/South_Pole": 230,
                "Antarctica/Syowa": 231,
                "Antarctica/Troll": 232,
                "Antarctica/Vostok": 233,
                "Arctic/Longyearbyen": 234,
                "Asia/Aden": 235,
                "Asia/Almaty": 236,
                "Asia/Amman": 237,
                "Asia/Anadyr": 238,
                "Asia/Aqtau": 239,
                "Asia/Aqtobe": 240,
                "Asia/Ashgabat": 241,
                "Asia/Ashkhabad": 242,
                "Asia/Atyrau": 243,
                "Asia/Baghdad": 244,
                "Asia/Bahrain": 245,
                "Asia/Baku": 246,
                "Asia/Bangkok": 247,
                "Asia/Barnaul": 248,
                "Asia/Beirut": 249,
                "Asia/Bishkek": 250,
                "Asia/Brunei": 251,
                "Asia/Calcutta": 252,
                "Asia/Chita": 253,
                "Asia/Choibalsan": 254,
                "Asia/Chongqing": 255,
                "Asia/Chungking": 256,
                "Asia/Colombo": 257,
                "Asia/Dacca": 258,
                "Asia/Damascus": 259,
                "Asia/Dhaka": 260,
                "Asia/Dili": 261,
                "Asia/Dubai": 262,
                "Asia/Dushanbe": 263,
                "Asia/Famagusta": 264,
                "Asia/Gaza": 265,
                "Asia/Harbin": 266,
                "Asia/Hebron": 267,
                "Asia/Ho_Chi_Minh": 268,
                "Asia/Hong_Kong": 269,
                "Asia/Hovd": 270,
                "Asia/Irkutsk": 271,
                "Asia/Istanbul": 272,
                "Asia/Jakarta": 273,
                "Asia/Jayapura": 274,
                "Asia/Jerusalem": 275,
                "Asia/Kabul": 276,
                "Asia/Kamchatka": 277,
                "Asia/Karachi": 278,
                "Asia/Kashgar": 279,
                "Asia/Kathmandu": 280,
                "Asia/Katmandu": 281,
                "Asia/Khandyga": 282,
                "Asia/Kolkata": 283,
                "Asia/Krasnoyarsk": 284,
                "Asia/Kuala_Lumpur": 285,
                "Asia/Kuching": 286,
                "Asia/Kuwait": 287,
                "Asia/Macao": 288,
                "Asia/Macau": 289,
                "Asia/Magadan": 290,
                "Asia/Makassar": 291,
                "Asia/Manila": 292,
                "Asia/Muscat": 293,
                "Asia/Nicosia": 294,
                "Asia/Novokuznetsk": 295,
                "Asia/Novosibirsk": 296,
                "Asia/Omsk": 297,
                "Asia/Oral": 298,
                "Asia/Phnom_Penh": 299,
                "Asia/Pontianak": 300,
                "Asia/Pyongyang": 301,
                "Asia/Qatar": 302,
                "Asia/Qostanay": 303,
                "Asia/Qyzylorda": 304,
                "Asia/Rangoon": 305,
                "Asia/Riyadh": 306,
                "Asia/Saigon": 307,
                "Asia/Sakhalin": 308,
                "Asia/Samarkand": 309,
                "Asia/Seoul": 310,
                "Asia/Shanghai": 311,
                "Asia/Singapore": 312,
                "Asia/Srednekolymsk": 313,
                "Asia/Taipei": 314,
                "Asia/Tashkent": 315,
                "Asia/Tbilisi": 316,
                "Asia/Tehran": 317,
                "Asia/Tel_Aviv": 318,
                "Asia/Thimbu": 319,
                "Asia/Thimphu": 320,
                "Asia/Tokyo": 321,
                "Asia/Tomsk": 322,
                "Asia/Ujung_Pandang": 323,
                "Asia/Ulaanbaatar": 324,
                "Asia/Ulan_Bator": 325,
                "Asia/Urumqi": 326,
                "Asia/Ust-Nera": 327,
                "Asia/Vientiane": 328,
                "Asia/Vladivostok": 329,
                "Asia/Yakutsk": 330,
                "Asia/Yangon": 331,
                "Asia/Yekaterinburg": 332,
                "Asia/Yerevan": 333,
                "Atlantic/Azores": 334,
                "Atlantic/Bermuda": 335,
                "Atlantic/Canary": 336,
                "Atlantic/Cape_Verde": 337,
                "Atlantic/Faeroe": 338,
                "Atlantic/Faroe": 339,
                "Atlantic/Jan_Mayen": 340,
                "Atlantic/Madeira": 341,
                "Atlantic/Reykjavik": 342,
                "Atlantic/South_Georgia": 343,
                "Atlantic/St_Helena": 344,
                "Atlantic/Stanley": 345,
                "Australia/ACT": 346,
                "Australia/Adelaide": 347,
                "Australia/Brisbane": 348,
                "Australia/Broken_Hill": 349,
                "Australia/Canberra": 350,
                "Australia/Currie": 351,
                "Australia/Darwin": 352,
                "Australia/Eucla": 353,
                "Australia/Hobart": 354,
                "Australia/LHI": 355,
                "Australia/Lindeman": 356,
                "Australia/Lord_Howe": 357,
                "Australia/Melbourne": 358,
                "Australia/NSW": 359,
                "Australia/North": 360,
                "Australia/Perth": 361,
                "Australia/Queensland": 362,
                "Australia/South": 363,
                "Australia/Sydney": 364,
                "Australia/Tasmania": 365,
                "Australia/Victoria": 366,
                "Australia/West": 367,
                "Australia/Yancowinna": 368,
                "Brazil/Acre": 369,
                "Brazil/DeNoronha": 370,
                "Brazil/East": 371,
                "Brazil/West": 372,
                "CET": 373,
                "CST6CDT": 374,
                "Canada/Atlantic": 375,
                "Canada/Central": 376,
                "Canada/Eastern": 377,
                "Canada/Mountain": 378,
                "Canada/Newfoundland": 379,
                "Canada/Pacific": 380,
                "Canada/Saskatchewan": 381,
                "Canada/Yukon": 382,
                "Chile/Continental": 383,
                "Chile/EasterIsland": 384,
                "Cuba": 385,
                "EET": 386,
                "EST": 387,
                "EST5EDT": 388,
                "Egypt": 389,
                "Eire": 390,
                "Etc/GMT": 391,
                "Etc/GMT+0": 392,
                "Etc/GMT+1": 393,
                "Etc/GMT+10": 394,
                "Etc/GMT+11": 395,
                "Etc/GMT+12": 396,
                "Etc/GMT+2": 397,
                "Etc/GMT+3": 398,
                "Etc/GMT+4": 399,
                "Etc/GMT+5": 400,
                "Etc/GMT+6": 401,
                "Etc/GMT+7": 402,
                "Etc/GMT+8": 403,
                "Etc/GMT+9": 404,
                "Etc/GMT-0": 405,
                "Etc/GMT-1": 406,
                "Etc/GMT-10": 407,
                "Etc/GMT-11": 408,
                "Etc/GMT-12": 409,
                "Etc/GMT-13": 410,
                "Etc/GMT-14": 411,
                "Etc/GMT-2": 412,
                "Etc/GMT-3": 413,
                "Etc/GMT-4": 414,
                "Etc/GMT-5": 415,
                "Etc/GMT-6": 416,
                "Etc/GMT-7": 417,
                "Etc/GMT-8": 418,
                "Etc/GMT-9": 419,
                "Etc/GMT0": 420,
                "Etc/Greenwich": 421,
                "Etc/UCT": 422,
                "Etc/UTC": 423,
                "Etc/Universal": 424,
                "Etc/Zulu": 425,
                "Europe/Amsterdam": 426,
                "Europe/Andorra": 427,
                "Europe/Astrakhan": 428,
                "Europe/Athens": 429,
                "Europe/Belfast": 430,
                "Europe/Belgrade": 431,
                "Europe/Berlin": 432,
                "Europe/Bratislava": 433,
                "Europe/Brussels": 434,
                "Europe/Bucharest": 435,
                "Europe/Budapest": 436,
                "Europe/Busingen": 437,
                "Europe/Chisinau": 438,
                "Europe/Copenhagen": 439,
                "Europe/Dublin": 440,
                "Europe/Gibraltar": 441,
                "Europe/Guernsey": 442,
                "Europe/Helsinki": 443,
                "Europe/Isle_of_Man": 444,
                "Europe/Istanbul": 445,
                "Europe/Jersey": 446,
                "Europe/Kaliningrad": 447,
                "Europe/Kiev": 448,
                "Europe/Kirov": 449,
                "Europe/Kyiv": 450,
                "Europe/Lisbon": 451,
                "Europe/Ljubljana": 452,
                "Europe/London": 453,
                "Europe/Luxembourg": 454,
                "Europe/Madrid": 455,
                "Europe/Malta": 456,
                "Europe/Mariehamn": 457,
                "Europe/Minsk": 458,
                "Europe/Monaco": 459,
                "Europe/Moscow": 460,
                "Europe/Nicosia": 461,
                "Europe/Oslo": 462,
                "Europe/Paris": 463,
                "Europe/Podgorica": 464,
                "Europe/Prague": 465,
                "Europe/Riga": 466,
                "Europe/Rome": 467,
                "Europe/Samara": 468,
                "Europe/San_Marino": 469,
                "Europe/Sarajevo": 470,
                "Europe/Saratov": 471,
                "Europe/Simferopol": 472,
                "Europe/Skopje": 473,
                "Europe/Sofia": 474,
                "Europe/Stockholm": 475,
                "Europe/Tallinn": 476,
                "Europe/Tirane": 477,
                "Europe/Tiraspol": 478,
                "Europe/Ulyanovsk": 479,
                "Europe/Uzhgorod": 480,
                "Europe/Vaduz": 481,
                "Europe/Vatican": 482,
                "Europe/Vienna": 483,
                "Europe/Vilnius": 484,
                "Europe/Volgograd": 485,
                "Europe/Warsaw": 486,
                "Europe/Zagreb": 487,
                "Europe/Zaporozhye": 488,
                "Europe/Zurich": 489,
                "Factory": 490,
                "GB": 491,
                "GB-Eire": 492,
                "GMT": 493,
                "GMT+0": 494,
                "GMT-0": 495,
                "GMT0": 496,
                "Greenwich": 497,
                "HST": 498,
                "Hongkong": 499,
                "Iceland": 500,
                "Indian/Antananarivo": 501,
                "Indian/Chagos": 502,
                "Indian/Christmas": 503,
                "Indian/Cocos": 504,
                "Indian/Comoro": 505,
                "Indian/Kerguelen": 506,
                "Indian/Mahe": 507,
                "Indian/Maldives": 508,
                "Indian/Mauritius": 509,
                "Indian/Mayotte": 510,
                "Indian/Reunion": 511,
                "Iran": 512,
                "Israel": 513,
                "Jamaica": 514,
                "Japan": 515,
                "Kwajalein": 516,
                "Libya": 517,
                "MET": 518,
                "MST": 519,
                "MST7MDT": 520,
                "Mexico/BajaNorte": 521,
                "Mexico/BajaSur": 522,
                "Mexico/General": 523,
                "NZ": 524,
                "NZ-CHAT": 525,
                "Navajo": 526,
                "PRC": 527,
                "PST8PDT": 528,
                "Pacific/Apia": 529,
                "Pacific/Auckland": 530,
                "Pacific/Bougainville": 531,
                "Pacific/Chatham": 532,
                "Pacific/Chuuk": 533,
                "Pacific/Easter": 534,
                "Pacific/Efate": 535,
                "Pacific/Enderbury": 536,
                "Pacific/Fakaofo": 537,
                "Pacific/Fiji": 538,
                "Pacific/Funafuti": 539,
                "Pacific/Galapagos": 540,
                "Pacific/Gambier": 541,
                "Pacific/Guadalcanal": 542,
                "Pacific/Guam": 543,
                "Pacific/Honolulu": 544,
                "Pacific/Johnston": 545,
                "Pacific/Kanton": 546,
                "Pacific/Kiritimati": 547,
                "Pacific/Kosrae": 548,
                "Pacific/Kwajalein": 549,
                "Pacific/Majuro": 550,
                "Pacific/Marquesas": 551,
                "Pacific/Midway": 552,
                "Pacific/Nauru": 553,
                "Pacific/Niue": 554,
                "Pacific/Norfolk": 555,
                "Pacific/Noumea": 556,
                "Pacific/Pago_Pago": 557,
                "Pacific/Palau": 558,
                "Pacific/Pitcairn": 559,
                "Pacific/Pohnpei": 560,
                "Pacific/Ponape": 561,
                "Pacific/Port_Moresby": 562,
                "Pacific/Rarotonga": 563,
                "Pacific/Saipan": 564,
                "Pacific/Samoa": 565,
                "Pacific/Tahiti": 566,
                "Pacific/Tarawa": 567,
                "Pacific/Tongatapu": 568,
                "Pacific/Truk": 569,
                "Pacific/Wake": 570,
                "Pacific/Wallis": 571,
                "Pacific/Yap": 572,
                "Poland": 573,
                "Portugal": 574,
                "ROC": 575,
                "ROK": 576,
                "Singapore": 577,
                "Turkey": 578,
                "UCT": 579,
                "US/Alaska": 580,
                "US/Aleutian": 581,
                "US/Arizona": 582,
                "US/Central": 583,
                "US/East-Indiana": 584,
                "US/Eastern": 585,
                "US/Hawaii": 586,
                "US/Indiana-Starke": 587,
                "US/Michigan": 588,
                "US/Mountain": 589,
                "US/Pacific": 590,
                "US/Samoa": 591,
                "UTC": 592,
                "Universal": 593,
                "W-SU": 594,
                "WET": 595,
                "Zulu": 596,
            }

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def __class_getitem__(cls, key) -> std.core.TimeZone:
                greycat: GreyCat
                if isinstance(key, tuple):
                    key, greycat = key
                else:
                    greycat = GreyCat._DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                return t.enum_values[t.generated_offsets[std.core.TimeZone.__indices_by_values[key]]]

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
            __indices_by_values: dict[str, int] = {
                "asc": 0,
                "desc": 1,
            }

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def __class_getitem__(cls, key) -> std.core.SortOrder:
                greycat: GreyCat
                if isinstance(key, tuple):
                    key, greycat = key
                else:
                    greycat = GreyCat._DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[5]
                return t.enum_values[t.generated_offsets[std.core.TimeZone.__indices_by_values[key]]]

            @staticmethod
            def create(greycat: GreyCat) -> std.core.SortOrder:
                return std.core.SortOrder(greycat.libs_by_name[std.name_].mapped[5], [])

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

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def __class_getitem__(cls, key) -> std.core.FloatPrecision:
                greycat: GreyCat
                if isinstance(key, tuple):
                    key, greycat = key
                else:
                    greycat = GreyCat._DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[6]
                return t.enum_values[t.generated_offsets[std.core.TimeZone.__indices_by_values[key]]]

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
            __indices_by_values: dict[str, int] = {
                "microseconds": 0,
                "milliseconds": 1,
                "seconds": 2,
                "minutes": 3,
                "hours": 4,
                "days": 5,
            }

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def __class_getitem__(cls, key) -> std.core.DurationUnit:
                greycat: GreyCat
                if isinstance(key, tuple):
                    key, greycat = key
                else:
                    greycat = GreyCat._DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[23]
                return t.enum_values[t.generated_offsets[std.core.TimeZone.__indices_by_values[key]]]

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
            __indices_by_values: dict[str, int] = {
                "i32": 0,
                "i64": 1,
                "f32": 2,
                "f64": 3,
                "c64": 4,
                "c128": 5,
            }

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def __class_getitem__(cls, key) -> std.core.TensorType:
                greycat: GreyCat
                if isinstance(key, tuple):
                    key, greycat = key
                else:
                    greycat = GreyCat._DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[37]
                return t.enum_values[t.generated_offsets[std.core.TimeZone.__indices_by_values[key]]]

            @staticmethod
            def create(greycat: GreyCat) -> std.core.TensorType:
                return std.core.TensorType(greycat.libs_by_name[std.name_].mapped[37], [])

        @final
        class SamplingMode(GreyCat.Enum):
            name_: Final[str] = "core::SamplingMode"
            __indices_by_values: dict[str, int] = {
                "fixed": 0,
                "fixed_reg": 1,
                "adaptative": 2,
                "dense": 3,
            }

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def __class_getitem__(cls, key) -> std.core.SamplingMode:
                greycat: GreyCat
                if isinstance(key, tuple):
                    key, greycat = key
                else:
                    greycat = GreyCat._DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[38]
                return t.enum_values[t.generated_offsets[std.core.TimeZone.__indices_by_values[key]]]

            @staticmethod
            def create(greycat: GreyCat) -> std.core.SamplingMode:
                return std.core.SamplingMode(greycat.libs_by_name[std.name_].mapped[38], [])

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

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def __class_getitem__(cls, key) -> std.core.CalendarUnit:
                greycat: GreyCat
                if isinstance(key, tuple):
                    key, greycat = key
                else:
                    greycat = GreyCat._DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[39]
                return t.enum_values[t.generated_offsets[std.core.TimeZone.__indices_by_values[key]]]

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
            __indices_by_values: dict[str, int] = {
                "none": 0,
                "interrupted": 1,
                "await_": 2,
                "timeout": 3,
                "forbidden": 4,
                "runtime_error": 5,
            }

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def __class_getitem__(cls, key) -> std.core.ErrorCode:
                greycat: GreyCat
                if isinstance(key, tuple):
                    key, greycat = key
                else:
                    greycat = GreyCat._DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[43]
                return t.enum_values[t.generated_offsets[std.core.TimeZone.__indices_by_values[key]]]

            @staticmethod
            def create(greycat: GreyCat) -> std.core.ErrorCode:
                return std.core.ErrorCode(greycat.libs_by_name[std.name_].mapped[43], [])

    @final
    class runtime:
        __T = TypeVar("__T")

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
            }

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def __class_getitem__(cls, key) -> std.runtime.TaskStatus:
                greycat: GreyCat
                if isinstance(key, tuple):
                    key, greycat = key
                else:
                    greycat = GreyCat._DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[44]
                return t.enum_values[t.generated_offsets[std.core.TimeZone.__indices_by_values[key]]]

            @staticmethod
            def create(greycat: GreyCat) -> std.runtime.TaskStatus:
                return std.runtime.TaskStatus(greycat.libs_by_name[std.name_].mapped[44], [])

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
                return std.runtime.Task(greycat.libs_by_name[std.name_].mapped[45], [user_id, task_id, mod, type, fun, creation, start, duration, status, progress])

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
                return std.runtime.SecurityFields(greycat.libs_by_name[std.name_].mapped[46], [email, name, first_name, last_name, roles, groups])

        @final
        class Variable(GreyCat.Object):
            name_: Final[str] = "runtime::Variable"

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
            def create(greycat: GreyCat, name: str, value: Any) -> std.runtime.Variable:
                return std.runtime.Variable(greycat.libs_by_name[std.name_].mapped[47], [name, value])

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
                return std.runtime.CallPerf(greycat.libs_by_name[std.name_].mapped[48], [duration, bytes_write_disk, bytes_write_disk_raw, bytes_read_disk, bytes_read_disk_raw, bytes_read_cache])

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
                return std.runtime.RuntimeInfo(greycat.libs_by_name[std.name_].mapped[49], [version, program_version, arch, timezone, license, io_threads, bg_threads, fg_threads, mem_total, mem_worker, nb_ctx, store_stats])

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

            def groups(self) -> std.core.Array:
                return self._get(self.type_.generated_offsets[6])

            def set_groups(self, v: std.core.Array) -> None:
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
            def create(greycat: GreyCat, id: int, name: str, activated: bool, full_name: str, email: str, role: str, groups: std.core.Array, groups_flags: int, external: bool) -> std.runtime.User:
                return std.runtime.User(greycat.libs_by_name[std.name_].mapped[50], [id, name, activated, full_name, email, role, groups, groups_flags, external])

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
                return std.runtime.UserCredential(greycat.libs_by_name[std.name_].mapped[51], [offset, pass_])

        @final
        class Permission(GreyCat.Object):
            name_: Final[str] = "runtime::Permission"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def name(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_name(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def description(self) -> str:
                return self._get(self.type_.generated_offsets[1])

            def set_description(self, v: str) -> None:
                self._set(self.type_.generated_offsets[1], v)

            @staticmethod
            def all(__greycat: Optional[GreyCat] = None) -> std.core.Array:
                if __greycat is None:
                    __greycat  = GreyCat.DEFAULT
                return __greycat.call("runtime::Permission::all")

            @staticmethod
            def create(greycat: GreyCat, name: str, description: str) -> std.runtime.Permission:
                return std.runtime.Permission(greycat.libs_by_name[std.name_].mapped[52], [name, description])

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
                return std.runtime.UserGroupPolicy(greycat.libs_by_name[std.name_].mapped[53], [group_id, type])

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
                return std.runtime.OpenIDConnect(greycat.libs_by_name[std.name_].mapped[54], [url, clientId])

        @final
        class Debug(GreyCat.Object):
            name_: Final[str] = "runtime::Debug"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def id(self) -> int:
                return self._get(self.type_.generated_offsets[0])

            def set_id(self, v: int) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def frames(self) -> std.core.Array:
                return self._get(self.type_.generated_offsets[1])

            def set_frames(self, v: std.core.Array) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def root(self) -> Any:
                return self._get(self.type_.generated_offsets[2])

            def set_root(self, v: Any) -> None:
                self._set(self.type_.generated_offsets[2], v)

            @staticmethod
            def resume(id: int, __greycat: Optional[GreyCat] = None) -> None:
                if __greycat is None:
                    __greycat  = GreyCat.DEFAULT
                return __greycat.call("runtime::Debug::resume", [id, ])

            @staticmethod
            def get(id: int, __greycat: Optional[GreyCat] = None) -> std.runtime.Debug:
                if __greycat is None:
                    __greycat  = GreyCat.DEFAULT
                return __greycat.call("runtime::Debug::get", [id, ])

            @staticmethod
            def all(__greycat: Optional[GreyCat] = None) -> std.core.Array:
                if __greycat is None:
                    __greycat  = GreyCat.DEFAULT
                return __greycat.call("runtime::Debug::all")

            @staticmethod
            def create(greycat: GreyCat, id: int, frames: std.core.Array, root: Any) -> std.runtime.Debug:
                return std.runtime.Debug(greycat.libs_by_name[std.name_].mapped[55], [id, frames, root])

        @final
        class Frame(GreyCat.Object):
            name_: Final[str] = "runtime::Frame"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

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

            def scope(self) -> std.core.Array:
                return self._get(self.type_.generated_offsets[6])

            def set_scope(self, v: std.core.Array) -> None:
                self._set(self.type_.generated_offsets[6], v)

            @staticmethod
            def create(greycat: GreyCat, module: str, type: str, function: str, src: str, line: int, column: int, scope: std.core.Array) -> std.runtime.Frame:
                return std.runtime.Frame(greycat.libs_by_name[std.name_].mapped[56], [module, type, function, src, line, column, scope])

        @final
        class System(GreyCat.Object):
            name_: Final[str] = "runtime::System"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            @staticmethod
            def create(greycat: GreyCat) -> std.runtime.System:
                return std.runtime.System(greycat.libs_by_name[std.name_].mapped[57], [])

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
                return std.runtime.License(greycat.libs_by_name[std.name_].mapped[58], [name, start, end, company, max_memory, extra_1, extra_2, type])

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
                return std.runtime.StoreStat(greycat.libs_by_name[std.name_].mapped[59], [capacity_bytes, allocated_bytes, allocated_ratio, remained_bytes, remained_ratio, used_bytes, used_ratio, available_bytes, available_ratio])

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
                return std.runtime.Log(greycat.libs_by_name[std.name_].mapped[60], [level, time, user_id, id, id2, src, tag, data])

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
                return std.runtime.SecurityEntity(greycat.libs_by_name[std.name_].mapped[61], [id, name, activated])

        @final
        class UserGroupPolicyType(GreyCat.Enum):
            name_: Final[str] = "runtime::UserGroupPolicyType"
            __indices_by_values: dict[str, int] = {
                "read": 0,
                "write": 1,
                "execute": 2,
            }

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def __class_getitem__(cls, key) -> std.runtime.UserGroupPolicyType:
                greycat: GreyCat
                if isinstance(key, tuple):
                    key, greycat = key
                else:
                    greycat = GreyCat._DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[62]
                return t.enum_values[t.generated_offsets[std.core.TimeZone.__indices_by_values[key]]]

            @staticmethod
            def create(greycat: GreyCat) -> std.runtime.UserGroupPolicyType:
                return std.runtime.UserGroupPolicyType(greycat.libs_by_name[std.name_].mapped[62], [])

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
                return std.runtime.Runtime(greycat.libs_by_name[std.name_].mapped[63], [])

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
                return std.runtime.UserGroup(greycat.libs_by_name[std.name_].mapped[64], [id, name, activated])

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

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def __class_getitem__(cls, key) -> std.runtime.LogLevel:
                greycat: GreyCat
                if isinstance(key, tuple):
                    key, greycat = key
                else:
                    greycat = GreyCat._DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[65]
                return t.enum_values[t.generated_offsets[std.core.TimeZone.__indices_by_values[key]]]

            @staticmethod
            def create(greycat: GreyCat) -> std.runtime.LogLevel:
                return std.runtime.LogLevel(greycat.libs_by_name[std.name_].mapped[65], [])

        @final
        class LicenseType(GreyCat.Enum):
            name_: Final[str] = "runtime::LicenseType"
            __indices_by_values: dict[str, int] = {
                "community": 0,
                "enterprise": 1,
                "testing": 2,
            }

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def __class_getitem__(cls, key) -> std.runtime.LicenseType:
                greycat: GreyCat
                if isinstance(key, tuple):
                    key, greycat = key
                else:
                    greycat = GreyCat._DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[66]
                return t.enum_values[t.generated_offsets[std.core.TimeZone.__indices_by_values[key]]]

            @staticmethod
            def create(greycat: GreyCat) -> std.runtime.LicenseType:
                return std.runtime.LicenseType(greycat.libs_by_name[std.name_].mapped[66], [])

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
                return std.runtime.PeriodicTask(greycat.libs_by_name[std.name_].mapped[67], [function, user_id, arguments, start, every])

        @final
        class Role(GreyCat.Object):
            name_: Final[str] = "runtime::Role"

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
                    __greycat  = GreyCat.DEFAULT
                return __greycat.call("runtime::Role::all")

            @staticmethod
            def create(greycat: GreyCat, name: str, permissions: std.core.Array) -> std.runtime.Role:
                return std.runtime.Role(greycat.libs_by_name[std.name_].mapped[68], [name, permissions])

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
                return std.runtime.Job(greycat.libs_by_name[std.name_].mapped[69], [function, arguments])

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

            def fields(self) -> std.runtime.SecurityFields:
                return self._get(self.type_.generated_offsets[2])

            def set_fields(self, v: std.runtime.SecurityFields) -> None:
                self._set(self.type_.generated_offsets[2], v)

            def keys(self) -> std.core.Map:
                return self._get(self.type_.generated_offsets[3])

            def set_keys(self, v: std.core.Map) -> None:
                self._set(self.type_.generated_offsets[3], v)

            def keys_last_refresh(self) -> std.core.time:
                return self._get(self.type_.generated_offsets[4])

            def set_keys_last_refresh(self, v: std.core.time) -> None:
                self._set(self.type_.generated_offsets[4], v)

            @staticmethod
            def create(greycat: GreyCat, entities: std.core.Array, credentials: std.core.Map, fields: std.runtime.SecurityFields, keys: std.core.Map, keys_last_refresh: std.core.time) -> std.runtime.SecurityPolicy:
                return std.runtime.SecurityPolicy(greycat.libs_by_name[std.name_].mapped[70], [entities, credentials, fields, keys, keys_last_refresh])

    @final
    class io:
        __T = TypeVar("__T")

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
                return std.io.JsonReader(greycat.libs_by_name[std.name_].mapped[71], [path, pos])

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
                return std.io.HttpHeader(greycat.libs_by_name[std.name_].mapped[72], [name, value])

        @final
        class Json(Generic[__T], GreyCat.Object):
            name_: Final[str] = "io::Json"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            @staticmethod
            def create(greycat: GreyCat) -> std.io.Json[TypeVar("T")]:
                return std.io.Json(greycat.libs_by_name[std.name_].mapped[73], [])

        @final
        class SmtpMode(GreyCat.Enum):
            name_: Final[str] = "io::SmtpMode"
            __indices_by_values: dict[str, int] = {
                "plain": 0,
                "ssl_tls": 1,
                "starttls": 2,
            }

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def __class_getitem__(cls, key) -> std.io.SmtpMode:
                greycat: GreyCat
                if isinstance(key, tuple):
                    key, greycat = key
                else:
                    greycat = GreyCat._DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[74]
                return t.enum_values[t.generated_offsets[std.core.TimeZone.__indices_by_values[key]]]

            @staticmethod
            def create(greycat: GreyCat) -> std.io.SmtpMode:
                return std.io.SmtpMode(greycat.libs_by_name[std.name_].mapped[74], [])

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
                return std.io.CsvSharding(greycat.libs_by_name[std.name_].mapped[75], [id, column, modulo])

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
                return std.io.GcbReader(greycat.libs_by_name[std.name_].mapped[76], [path, pos])

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
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[77]
                return t.static_values[0]

            @staticmethod
            def date_check_limit_default(greycat: GreyCat) -> int:
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[77]
                return t.static_values[1]

            @staticmethod
            def create(greycat: GreyCat, header_lines: int, separator: c_char, string_delimiter: c_char, decimal_separator: c_char, thousands_separator: c_char, row_limit: int, enumerable_limit: int, date_check_limit: int, date_formats: std.core.Array) -> std.io.CsvAnalysisConfig:
                return std.io.CsvAnalysisConfig(greycat.libs_by_name[std.name_].mapped[77], [header_lines, separator, string_delimiter, decimal_separator, thousands_separator, row_limit, enumerable_limit, date_check_limit, date_formats])

        @final
        class CsvAnalysis(GreyCat.Object):
            name_: Final[str] = "io::CsvAnalysis"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            @staticmethod
            def analyze(files: std.core.Array, config: std.io.CsvAnalysisConfig, __greycat: Optional[GreyCat] = None) -> std.io.CsvStatistics:
                if __greycat is None:
                    __greycat  = GreyCat.DEFAULT
                return __greycat.call("io::CsvAnalysis::analyze", [files, config, ])

            @staticmethod
            def create(greycat: GreyCat) -> std.io.CsvAnalysis:
                return std.io.CsvAnalysis(greycat.libs_by_name[std.name_].mapped[78], [])

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
            def sample(reader: std.io.CsvReader, max_lines: int, __greycat: Optional[GreyCat] = None) -> std.core.Table:
                if __greycat is None:
                    __greycat  = GreyCat.DEFAULT
                return __greycat.call("io::CsvReader::sample", [reader, max_lines, ])

            @staticmethod
            def create(greycat: GreyCat, path: str, pos: int, format: std.io.CsvFormat, sharding: std.io.CsvSharding) -> std.io.CsvReader[TypeVar("T")]:
                return std.io.CsvReader(greycat.libs_by_name[std.name_].mapped[79], [path, pos, format, sharding])

        @final
        class TextEncoder(GreyCat.Enum):
            name_: Final[str] = "io::TextEncoder"
            __indices_by_values: dict[str, int] = {
                "plain": 0,
                "base64": 1,
                "base64url": 2,
                "hexadecimal": 3,
            }

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def __class_getitem__(cls, key) -> std.io.TextEncoder:
                greycat: GreyCat
                if isinstance(key, tuple):
                    key, greycat = key
                else:
                    greycat = GreyCat._DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[80]
                return t.enum_values[t.generated_offsets[std.core.TimeZone.__indices_by_values[key]]]

            @staticmethod
            def create(greycat: GreyCat) -> std.io.TextEncoder:
                return std.io.TextEncoder(greycat.libs_by_name[std.name_].mapped[80], [])

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
            def generate(stats: std.io.CsvStatistics, __greycat: Optional[GreyCat] = None) -> str:
                if __greycat is None:
                    __greycat  = GreyCat.DEFAULT
                return __greycat.call("io::CsvStatistics::generate", [stats, ])

            @staticmethod
            def create(greycat: GreyCat, header_lines: int, separator: c_char, string_delimiter: c_char, decimal_separator: c_char, thousands_separator: c_char, columns: std.core.Array, line_count: int, fail_count: int, file_count: int) -> std.io.CsvStatistics:
                return std.io.CsvStatistics(greycat.libs_by_name[std.name_].mapped[81], [header_lines, separator, string_delimiter, decimal_separator, thousands_separator, columns, line_count, fail_count, file_count])

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
                return std.io.Reader(greycat.libs_by_name[std.name_].mapped[82], [path, pos])

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
                return std.io.GcbWriter(greycat.libs_by_name[std.name_].mapped[83], [path, append])

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
                return std.io.TextWriter(greycat.libs_by_name[std.name_].mapped[84], [path, append])

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
                return std.io.FileWalker(greycat.libs_by_name[std.name_].mapped[85], [path])

        @final
        class SmtpAuth(GreyCat.Enum):
            name_: Final[str] = "io::SmtpAuth"
            __indices_by_values: dict[str, int] = {
                "none": 0,
                "plain": 1,
                "login": 2,
            }

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def __class_getitem__(cls, key) -> std.io.SmtpAuth:
                greycat: GreyCat
                if isinstance(key, tuple):
                    key, greycat = key
                else:
                    greycat = GreyCat._DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[86]
                return t.enum_values[t.generated_offsets[std.core.TimeZone.__indices_by_values[key]]]

            @staticmethod
            def create(greycat: GreyCat) -> std.io.SmtpAuth:
                return std.io.SmtpAuth(greycat.libs_by_name[std.name_].mapped[86], [])

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
                return std.io.Url(greycat.libs_by_name[std.name_].mapped[87], [protocol, host, port, path, params, hash])

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
                return std.io.Email(greycat.libs_by_name[std.name_].mapped[88], [from_, subject, body, body_is_html, to, cc, bcc])

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
                return std.io.Smtp(greycat.libs_by_name[std.name_].mapped[89], [host, port, mode, authenticate, user, pass_])

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
                return std.io.File(greycat.libs_by_name[std.name_].mapped[90], [path, size, last_modification])

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
                return std.io.CsvWriter(greycat.libs_by_name[std.name_].mapped[91], [path, append, format])

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
                return std.io.Writer(greycat.libs_by_name[std.name_].mapped[92], [path, append])

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
                return std.io.JsonWriter(greycat.libs_by_name[std.name_].mapped[93], [path, append])

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
                return std.io.TextReader(greycat.libs_by_name[std.name_].mapped[94], [path, pos])

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

            def trim(self) -> bool:
                return self._get(self.type_.generated_offsets[5])

            def set_trim(self, v: bool) -> None:
                self._set(self.type_.generated_offsets[5], v)

            def format(self) -> str:
                return self._get(self.type_.generated_offsets[6])

            def set_format(self, v: str) -> None:
                self._set(self.type_.generated_offsets[6], v)

            def tz(self) -> std.core.TimeZone:
                return self._get(self.type_.generated_offsets[7])

            def set_tz(self, v: std.core.TimeZone) -> None:
                self._set(self.type_.generated_offsets[7], v)

            def strict(self) -> bool:
                return self._get(self.type_.generated_offsets[8])

            def set_strict(self, v: bool) -> None:
                self._set(self.type_.generated_offsets[8], v)

            @staticmethod
            def create(greycat: GreyCat, header_lines: int, separator: c_char, string_delimiter: c_char, decimal_separator: c_char, thousands_separator: c_char, trim: bool, format: str, tz: std.core.TimeZone, strict: bool) -> std.io.CsvFormat:
                return std.io.CsvFormat(greycat.libs_by_name[std.name_].mapped[95], [header_lines, separator, string_delimiter, decimal_separator, thousands_separator, trim, format, tz, strict])

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
                return std.io.CsvColumnStatistics(greycat.libs_by_name[std.name_].mapped[96], [name, example, null_count, bool_count, int_count, float_count, string_count, date_count, date_format_count, enumerable_count, profile])

        @final
        class Http(GreyCat.Object):
            name_: Final[str] = "io::Http"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            @staticmethod
            def create(greycat: GreyCat) -> std.io.Http:
                return std.io.Http(greycat.libs_by_name[std.name_].mapped[97], [])

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
                return std.io.CsvValidateResult(greycat.libs_by_name[std.name_].mapped[98], [line_count, fail_count, invalid_count])

    @final
    class util:
        __T = TypeVar("__T")

        @final
        class Crypto(GreyCat.Object):
            name_: Final[str] = "util::Crypto"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            @staticmethod
            def create(greycat: GreyCat) -> std.util.Crypto:
                return std.util.Crypto(greycat.libs_by_name[std.name_].mapped[99], [])

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
                return std.util.CustomQuantizer(greycat.libs_by_name[std.name_].mapped[100], [min, max, step_starts, open])

        @final
        class Assert(GreyCat.Object):
            name_: Final[str] = "util::Assert"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            @staticmethod
            def create(greycat: GreyCat) -> std.util.Assert:
                return std.util.Assert(greycat.libs_by_name[std.name_].mapped[101], [])

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
                return std.util.SlidingWindow(greycat.libs_by_name[std.name_].mapped[102], [values, span, sum, sumsq, field])

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
                return std.util.QuantizerSlotBound(greycat.libs_by_name[std.name_].mapped[103], [min, max, center])

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
                return std.util.Histogram(greycat.libs_by_name[std.name_].mapped[104], [quantizer, bins, nb_rejected, nb_accepted])

        @final
        class Quantizer(Generic[__T], GreyCat.Object):
            name_: Final[str] = "util::Quantizer"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            @staticmethod
            def create(greycat: GreyCat) -> std.util.Quantizer[TypeVar("T")]:
                return std.util.Quantizer(greycat.libs_by_name[std.name_].mapped[105], [])

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
                return std.util.HistogramStats(greycat.libs_by_name[std.name_].mapped[106], [min, max, whisker_low, whisker_high, percentile1, percentile5, percentile25, percentile50, percentile75, percentile95, percentile99, count_outliers_low, count_outliers_high, percentage_outliers_low, percentage_outliers_high, sum, avg, std, size])

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
                return std.util.LogQuantizer(greycat.libs_by_name[std.name_].mapped[107], [min, max, bins, open])

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
                return std.util.Random(greycat.libs_by_name[std.name_].mapped[108], [seed, v])

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
                return std.util.LinearQuantizer(greycat.libs_by_name[std.name_].mapped[109], [min, max, bins, open])

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
                return std.util.GaussianProfile(greycat.libs_by_name[std.name_].mapped[110], [quantizer, precision, bins, value_min, nb_rejected])

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
                return std.util.MultiQuantizer(greycat.libs_by_name[std.name_].mapped[111], [quantizers])

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
                return std.util.Stack(greycat.libs_by_name[std.name_].mapped[112], [values])

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
                return std.util.TimeWindow(greycat.libs_by_name[std.name_].mapped[113], [values, span, sum, sumsq, field])

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
                return std.util.GaussianProfileSlot(greycat.libs_by_name[std.name_].mapped[114], [sum, sumsq, count])

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
                return std.util.ProgressTracker(greycat.libs_by_name[std.name_].mapped[115], [start, total, counter, duration, progress, speed, remaining])

        @final
        class Plot(GreyCat.Object):
            name_: Final[str] = "util::Plot"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            @staticmethod
            def create(greycat: GreyCat) -> std.util.Plot:
                return std.util.Plot(greycat.libs_by_name[std.name_].mapped[116], [])

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
                return std.util.Queue(greycat.libs_by_name[std.name_].mapped[117], [values, capacity])

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
                return std.util.Gaussian(greycat.libs_by_name[std.name_].mapped[118], [sum, sumsq, count, min, max])

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
        factories[std.runtime.TaskStatus.name_] = lambda type, attributes: std.runtime.TaskStatus(type, attributes)
        factories[std.runtime.Task.name_] = lambda type, attributes: std.runtime.Task(type, attributes)
        factories[std.runtime.SecurityFields.name_] = lambda type, attributes: std.runtime.SecurityFields(type, attributes)
        factories[std.runtime.Variable.name_] = lambda type, attributes: std.runtime.Variable(type, attributes)
        factories[std.runtime.CallPerf.name_] = lambda type, attributes: std.runtime.CallPerf(type, attributes)
        factories[std.runtime.RuntimeInfo.name_] = lambda type, attributes: std.runtime.RuntimeInfo(type, attributes)
        factories[std.runtime.User.name_] = lambda type, attributes: std.runtime.User(type, attributes)
        factories[std.runtime.UserCredential.name_] = lambda type, attributes: std.runtime.UserCredential(type, attributes)
        factories[std.runtime.Permission.name_] = lambda type, attributes: std.runtime.Permission(type, attributes)
        factories[std.runtime.UserGroupPolicy.name_] = lambda type, attributes: std.runtime.UserGroupPolicy(type, attributes)
        factories[std.runtime.OpenIDConnect.name_] = lambda type, attributes: std.runtime.OpenIDConnect(type, attributes)
        factories[std.runtime.Debug.name_] = lambda type, attributes: std.runtime.Debug(type, attributes)
        factories[std.runtime.Frame.name_] = lambda type, attributes: std.runtime.Frame(type, attributes)
        factories[std.runtime.System.name_] = lambda type, attributes: std.runtime.System(type, attributes)
        factories[std.runtime.License.name_] = lambda type, attributes: std.runtime.License(type, attributes)
        factories[std.runtime.StoreStat.name_] = lambda type, attributes: std.runtime.StoreStat(type, attributes)
        factories[std.runtime.Log.name_] = lambda type, attributes: std.runtime.Log(type, attributes)
        factories[std.runtime.SecurityEntity.name_] = lambda type, attributes: std.runtime.SecurityEntity(type, attributes)
        factories[std.runtime.UserGroupPolicyType.name_] = lambda type, attributes: std.runtime.UserGroupPolicyType(type, attributes)
        factories[std.runtime.Runtime.name_] = lambda type, attributes: std.runtime.Runtime(type, attributes)
        factories[std.runtime.UserGroup.name_] = lambda type, attributes: std.runtime.UserGroup(type, attributes)
        factories[std.runtime.LogLevel.name_] = lambda type, attributes: std.runtime.LogLevel(type, attributes)
        factories[std.runtime.LicenseType.name_] = lambda type, attributes: std.runtime.LicenseType(type, attributes)
        factories[std.runtime.PeriodicTask.name_] = lambda type, attributes: std.runtime.PeriodicTask(type, attributes)
        factories[std.runtime.Role.name_] = lambda type, attributes: std.runtime.Role(type, attributes)
        factories[std.runtime.Job.name_] = lambda type, attributes: std.runtime.Job(type, attributes)
        factories[std.runtime.SecurityPolicy.name_] = lambda type, attributes: std.runtime.SecurityPolicy(type, attributes)
        factories[std.io.JsonReader.name_] = lambda type, attributes: std.io.JsonReader(type, attributes)
        factories[std.io.HttpHeader.name_] = lambda type, attributes: std.io.HttpHeader(type, attributes)
        factories[std.io.Json.name_] = lambda type, attributes: std.io.Json(type, attributes)
        factories[std.io.SmtpMode.name_] = lambda type, attributes: std.io.SmtpMode(type, attributes)
        factories[std.io.CsvSharding.name_] = lambda type, attributes: std.io.CsvSharding(type, attributes)
        factories[std.io.GcbReader.name_] = lambda type, attributes: std.io.GcbReader(type, attributes)
        factories[std.io.CsvAnalysisConfig.name_] = lambda type, attributes: std.io.CsvAnalysisConfig(type, attributes)
        factories[std.io.CsvAnalysis.name_] = lambda type, attributes: std.io.CsvAnalysis(type, attributes)
        factories[std.io.CsvReader.name_] = lambda type, attributes: std.io.CsvReader(type, attributes)
        factories[std.io.TextEncoder.name_] = lambda type, attributes: std.io.TextEncoder(type, attributes)
        factories[std.io.CsvStatistics.name_] = lambda type, attributes: std.io.CsvStatistics(type, attributes)
        factories[std.io.Reader.name_] = lambda type, attributes: std.io.Reader(type, attributes)
        factories[std.io.GcbWriter.name_] = lambda type, attributes: std.io.GcbWriter(type, attributes)
        factories[std.io.TextWriter.name_] = lambda type, attributes: std.io.TextWriter(type, attributes)
        factories[std.io.FileWalker.name_] = lambda type, attributes: std.io.FileWalker(type, attributes)
        factories[std.io.SmtpAuth.name_] = lambda type, attributes: std.io.SmtpAuth(type, attributes)
        factories[std.io.Url.name_] = lambda type, attributes: std.io.Url(type, attributes)
        factories[std.io.Email.name_] = lambda type, attributes: std.io.Email(type, attributes)
        factories[std.io.Smtp.name_] = lambda type, attributes: std.io.Smtp(type, attributes)
        factories[std.io.File.name_] = lambda type, attributes: std.io.File(type, attributes)
        factories[std.io.CsvWriter.name_] = lambda type, attributes: std.io.CsvWriter(type, attributes)
        factories[std.io.Writer.name_] = lambda type, attributes: std.io.Writer(type, attributes)
        factories[std.io.JsonWriter.name_] = lambda type, attributes: std.io.JsonWriter(type, attributes)
        factories[std.io.TextReader.name_] = lambda type, attributes: std.io.TextReader(type, attributes)
        factories[std.io.CsvFormat.name_] = lambda type, attributes: std.io.CsvFormat(type, attributes)
        factories[std.io.CsvColumnStatistics.name_] = lambda type, attributes: std.io.CsvColumnStatistics(type, attributes)
        factories[std.io.Http.name_] = lambda type, attributes: std.io.Http(type, attributes)
        factories[std.io.CsvValidateResult.name_] = lambda type, attributes: std.io.CsvValidateResult(type, attributes)
        factories[std.util.Crypto.name_] = lambda type, attributes: std.util.Crypto(type, attributes)
        factories[std.util.CustomQuantizer.name_] = lambda type, attributes: std.util.CustomQuantizer(type, attributes)
        factories[std.util.Assert.name_] = lambda type, attributes: std.util.Assert(type, attributes)
        factories[std.util.SlidingWindow.name_] = lambda type, attributes: std.util.SlidingWindow(type, attributes)
        factories[std.util.QuantizerSlotBound.name_] = lambda type, attributes: std.util.QuantizerSlotBound(type, attributes)
        factories[std.util.Histogram.name_] = lambda type, attributes: std.util.Histogram(type, attributes)
        factories[std.util.Quantizer.name_] = lambda type, attributes: std.util.Quantizer(type, attributes)
        factories[std.util.HistogramStats.name_] = lambda type, attributes: std.util.HistogramStats(type, attributes)
        factories[std.util.LogQuantizer.name_] = lambda type, attributes: std.util.LogQuantizer(type, attributes)
        factories[std.util.Random.name_] = lambda type, attributes: std.util.Random(type, attributes)
        factories[std.util.LinearQuantizer.name_] = lambda type, attributes: std.util.LinearQuantizer(type, attributes)
        factories[std.util.GaussianProfile.name_] = lambda type, attributes: std.util.GaussianProfile(type, attributes)
        factories[std.util.MultiQuantizer.name_] = lambda type, attributes: std.util.MultiQuantizer(type, attributes)
        factories[std.util.Stack.name_] = lambda type, attributes: std.util.Stack(type, attributes)
        factories[std.util.TimeWindow.name_] = lambda type, attributes: std.util.TimeWindow(type, attributes)
        factories[std.util.GaussianProfileSlot.name_] = lambda type, attributes: std.util.GaussianProfileSlot(type, attributes)
        factories[std.util.ProgressTracker.name_] = lambda type, attributes: std.util.ProgressTracker(type, attributes)
        factories[std.util.Plot.name_] = lambda type, attributes: std.util.Plot(type, attributes)
        factories[std.util.Queue.name_] = lambda type, attributes: std.util.Queue(type, attributes)
        factories[std.util.Gaussian.name_] = lambda type, attributes: std.util.Gaussian(type, attributes)

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
            greycat.types_by_name[std.runtime.TaskStatus.name_],
            greycat.types_by_name[std.runtime.Task.name_],
            greycat.types_by_name[std.runtime.SecurityFields.name_],
            greycat.types_by_name[std.runtime.Variable.name_],
            greycat.types_by_name[std.runtime.CallPerf.name_],
            greycat.types_by_name[std.runtime.RuntimeInfo.name_],
            greycat.types_by_name[std.runtime.User.name_],
            greycat.types_by_name[std.runtime.UserCredential.name_],
            greycat.types_by_name[std.runtime.Permission.name_],
            greycat.types_by_name[std.runtime.UserGroupPolicy.name_],
            greycat.types_by_name[std.runtime.OpenIDConnect.name_],
            greycat.types_by_name[std.runtime.Debug.name_],
            greycat.types_by_name[std.runtime.Frame.name_],
            greycat.types_by_name[std.runtime.System.name_],
            greycat.types_by_name[std.runtime.License.name_],
            greycat.types_by_name[std.runtime.StoreStat.name_],
            greycat.types_by_name[std.runtime.Log.name_],
            greycat.types_by_name[std.runtime.SecurityEntity.name_],
            greycat.types_by_name[std.runtime.UserGroupPolicyType.name_],
            greycat.types_by_name[std.runtime.Runtime.name_],
            greycat.types_by_name[std.runtime.UserGroup.name_],
            greycat.types_by_name[std.runtime.LogLevel.name_],
            greycat.types_by_name[std.runtime.LicenseType.name_],
            greycat.types_by_name[std.runtime.PeriodicTask.name_],
            greycat.types_by_name[std.runtime.Role.name_],
            greycat.types_by_name[std.runtime.Job.name_],
            greycat.types_by_name[std.runtime.SecurityPolicy.name_],
            greycat.types_by_name[std.io.JsonReader.name_],
            greycat.types_by_name[std.io.HttpHeader.name_],
            greycat.types_by_name[std.io.Json.name_],
            greycat.types_by_name[std.io.SmtpMode.name_],
            greycat.types_by_name[std.io.CsvSharding.name_],
            greycat.types_by_name[std.io.GcbReader.name_],
            greycat.types_by_name[std.io.CsvAnalysisConfig.name_],
            greycat.types_by_name[std.io.CsvAnalysis.name_],
            greycat.types_by_name[std.io.CsvReader.name_],
            greycat.types_by_name[std.io.TextEncoder.name_],
            greycat.types_by_name[std.io.CsvStatistics.name_],
            greycat.types_by_name[std.io.Reader.name_],
            greycat.types_by_name[std.io.GcbWriter.name_],
            greycat.types_by_name[std.io.TextWriter.name_],
            greycat.types_by_name[std.io.FileWalker.name_],
            greycat.types_by_name[std.io.SmtpAuth.name_],
            greycat.types_by_name[std.io.Url.name_],
            greycat.types_by_name[std.io.Email.name_],
            greycat.types_by_name[std.io.Smtp.name_],
            greycat.types_by_name[std.io.File.name_],
            greycat.types_by_name[std.io.CsvWriter.name_],
            greycat.types_by_name[std.io.Writer.name_],
            greycat.types_by_name[std.io.JsonWriter.name_],
            greycat.types_by_name[std.io.TextReader.name_],
            greycat.types_by_name[std.io.CsvFormat.name_],
            greycat.types_by_name[std.io.CsvColumnStatistics.name_],
            greycat.types_by_name[std.io.Http.name_],
            greycat.types_by_name[std.io.CsvValidateResult.name_],
            greycat.types_by_name[std.util.Crypto.name_],
            greycat.types_by_name[std.util.CustomQuantizer.name_],
            greycat.types_by_name[std.util.Assert.name_],
            greycat.types_by_name[std.util.SlidingWindow.name_],
            greycat.types_by_name[std.util.QuantizerSlotBound.name_],
            greycat.types_by_name[std.util.Histogram.name_],
            greycat.types_by_name[std.util.Quantizer.name_],
            greycat.types_by_name[std.util.HistogramStats.name_],
            greycat.types_by_name[std.util.LogQuantizer.name_],
            greycat.types_by_name[std.util.Random.name_],
            greycat.types_by_name[std.util.LinearQuantizer.name_],
            greycat.types_by_name[std.util.GaussianProfile.name_],
            greycat.types_by_name[std.util.MultiQuantizer.name_],
            greycat.types_by_name[std.util.Stack.name_],
            greycat.types_by_name[std.util.TimeWindow.name_],
            greycat.types_by_name[std.util.GaussianProfileSlot.name_],
            greycat.types_by_name[std.util.ProgressTracker.name_],
            greycat.types_by_name[std.util.Plot.name_],
            greycat.types_by_name[std.util.Queue.name_],
            greycat.types_by_name[std.util.Gaussian.name_],
        ]
        self.mapped[1].resolve_generated_offsets("year", "month", "day", "hour", "minute", "second", "microsecond")
        self.mapped[2].resolve_generated_offsets("n", "req_time")
        self.mapped[3].resolve_generated_offset_with_values("Africa/Abidjan", None, "Africa/Accra", None, "Africa/Addis_Ababa", None, "Africa/Algiers", None, "Africa/Asmara", None, "Africa/Asmera", None, "Africa/Bamako", None, "Africa/Bangui", None, "Africa/Banjul", None, "Africa/Bissau", None, "Africa/Blantyre", None, "Africa/Brazzaville", None, "Africa/Bujumbura", None, "Africa/Cairo", None, "Africa/Casablanca", None, "Africa/Ceuta", None, "Africa/Conakry", None, "Africa/Dakar", None, "Africa/Dar_es_Salaam", None, "Africa/Djibouti", None, "Africa/Douala", None, "Africa/El_Aaiun", None, "Africa/Freetown", None, "Africa/Gaborone", None, "Africa/Harare", None, "Africa/Johannesburg", None, "Africa/Juba", None, "Africa/Kampala", None, "Africa/Khartoum", None, "Africa/Kigali", None, "Africa/Kinshasa", None, "Africa/Lagos", None, "Africa/Libreville", None, "Africa/Lome", None, "Africa/Luanda", None, "Africa/Lubumbashi", None, "Africa/Lusaka", None, "Africa/Malabo", None, "Africa/Maputo", None, "Africa/Maseru", None, "Africa/Mbabane", None, "Africa/Mogadishu", None, "Africa/Monrovia", None, "Africa/Nairobi", None, "Africa/Ndjamena", None, "Africa/Niamey", None, "Africa/Nouakchott", None, "Africa/Ouagadougou", None, "Africa/Porto-Novo", None, "Africa/Sao_Tome", None, "Africa/Timbuktu", None, "Africa/Tripoli", None, "Africa/Tunis", None, "Africa/Windhoek", None, "America/Adak", None, "America/Anchorage", None, "America/Anguilla", None, "America/Antigua", None, "America/Araguaina", None, "America/Argentina/Buenos_Aires", None, "America/Argentina/Catamarca", None, "America/Argentina/ComodRivadavia", None, "America/Argentina/Cordoba", None, "America/Argentina/Jujuy", None, "America/Argentina/La_Rioja", None, "America/Argentina/Mendoza", None, "America/Argentina/Rio_Gallegos", None, "America/Argentina/Salta", None, "America/Argentina/San_Juan", None, "America/Argentina/San_Luis", None, "America/Argentina/Tucuman", None, "America/Argentina/Ushuaia", None, "America/Aruba", None, "America/Asuncion", None, "America/Atikokan", None, "America/Atka", None, "America/Bahia", None, "America/Bahia_Banderas", None, "America/Barbados", None, "America/Belem", None, "America/Belize", None, "America/Blanc-Sablon", None, "America/Boa_Vista", None, "America/Bogota", None, "America/Boise", None, "America/Buenos_Aires", None, "America/Cambridge_Bay", None, "America/Campo_Grande", None, "America/Cancun", None, "America/Caracas", None, "America/Catamarca", None, "America/Cayenne", None, "America/Cayman", None, "America/Chicago", None, "America/Chihuahua", None, "America/Ciudad_Juarez", None, "America/Coral_Harbour", None, "America/Cordoba", None, "America/Costa_Rica", None, "America/Creston", None, "America/Cuiaba", None, "America/Curacao", None, "America/Danmarkshavn", None, "America/Dawson", None, "America/Dawson_Creek", None, "America/Denver", None, "America/Detroit", None, "America/Dominica", None, "America/Edmonton", None, "America/Eirunepe", None, "America/El_Salvador", None, "America/Ensenada", None, "America/Fort_Nelson", None, "America/Fort_Wayne", None, "America/Fortaleza", None, "America/Glace_Bay", None, "America/Godthab", None, "America/Goose_Bay", None, "America/Grand_Turk", None, "America/Grenada", None, "America/Guadeloupe", None, "America/Guatemala", None, "America/Guayaquil", None, "America/Guyana", None, "America/Halifax", None, "America/Havana", None, "America/Hermosillo", None, "America/Indiana/Indianapolis", None, "America/Indiana/Knox", None, "America/Indiana/Marengo", None, "America/Indiana/Petersburg", None, "America/Indiana/Tell_City", None, "America/Indiana/Vevay", None, "America/Indiana/Vincennes", None, "America/Indiana/Winamac", None, "America/Indianapolis", None, "America/Inuvik", None, "America/Iqaluit", None, "America/Jamaica", None, "America/Jujuy", None, "America/Juneau", None, "America/Kentucky/Louisville", None, "America/Kentucky/Monticello", None, "America/Knox_IN", None, "America/Kralendijk", None, "America/La_Paz", None, "America/Lima", None, "America/Los_Angeles", None, "America/Louisville", None, "America/Lower_Princes", None, "America/Maceio", None, "America/Managua", None, "America/Manaus", None, "America/Marigot", None, "America/Martinique", None, "America/Matamoros", None, "America/Mazatlan", None, "America/Mendoza", None, "America/Menominee", None, "America/Merida", None, "America/Metlakatla", None, "America/Mexico_City", None, "America/Miquelon", None, "America/Moncton", None, "America/Monterrey", None, "America/Montevideo", None, "America/Montreal", None, "America/Montserrat", None, "America/Nassau", None, "America/New_York", None, "America/Nipigon", None, "America/Nome", None, "America/Noronha", None, "America/North_Dakota/Beulah", None, "America/North_Dakota/Center", None, "America/North_Dakota/New_Salem", None, "America/Nuuk", None, "America/Ojinaga", None, "America/Panama", None, "America/Pangnirtung", None, "America/Paramaribo", None, "America/Phoenix", None, "America/Port-au-Prince", None, "America/Port_of_Spain", None, "America/Porto_Acre", None, "America/Porto_Velho", None, "America/Puerto_Rico", None, "America/Punta_Arenas", None, "America/Rainy_River", None, "America/Rankin_Inlet", None, "America/Recife", None, "America/Regina", None, "America/Resolute", None, "America/Rio_Branco", None, "America/Rosario", None, "America/Santa_Isabel", None, "America/Santarem", None, "America/Santiago", None, "America/Santo_Domingo", None, "America/Sao_Paulo", None, "America/Scoresbysund", None, "America/Shiprock", None, "America/Sitka", None, "America/St_Barthelemy", None, "America/St_Johns", None, "America/St_Kitts", None, "America/St_Lucia", None, "America/St_Thomas", None, "America/St_Vincent", None, "America/Swift_Current", None, "America/Tegucigalpa", None, "America/Thule", None, "America/Thunder_Bay", None, "America/Tijuana", None, "America/Toronto", None, "America/Tortola", None, "America/Vancouver", None, "America/Virgin", None, "America/Whitehorse", None, "America/Winnipeg", None, "America/Yakutat", None, "America/Yellowknife", None, "Antarctica/Casey", None, "Antarctica/Davis", None, "Antarctica/DumontDUrville", None, "Antarctica/Macquarie", None, "Antarctica/Mawson", None, "Antarctica/McMurdo", None, "Antarctica/Palmer", None, "Antarctica/Rothera", None, "Antarctica/South_Pole", None, "Antarctica/Syowa", None, "Antarctica/Troll", None, "Antarctica/Vostok", None, "Arctic/Longyearbyen", None, "Asia/Aden", None, "Asia/Almaty", None, "Asia/Amman", None, "Asia/Anadyr", None, "Asia/Aqtau", None, "Asia/Aqtobe", None, "Asia/Ashgabat", None, "Asia/Ashkhabad", None, "Asia/Atyrau", None, "Asia/Baghdad", None, "Asia/Bahrain", None, "Asia/Baku", None, "Asia/Bangkok", None, "Asia/Barnaul", None, "Asia/Beirut", None, "Asia/Bishkek", None, "Asia/Brunei", None, "Asia/Calcutta", None, "Asia/Chita", None, "Asia/Choibalsan", None, "Asia/Chongqing", None, "Asia/Chungking", None, "Asia/Colombo", None, "Asia/Dacca", None, "Asia/Damascus", None, "Asia/Dhaka", None, "Asia/Dili", None, "Asia/Dubai", None, "Asia/Dushanbe", None, "Asia/Famagusta", None, "Asia/Gaza", None, "Asia/Harbin", None, "Asia/Hebron", None, "Asia/Ho_Chi_Minh", None, "Asia/Hong_Kong", None, "Asia/Hovd", None, "Asia/Irkutsk", None, "Asia/Istanbul", None, "Asia/Jakarta", None, "Asia/Jayapura", None, "Asia/Jerusalem", None, "Asia/Kabul", None, "Asia/Kamchatka", None, "Asia/Karachi", None, "Asia/Kashgar", None, "Asia/Kathmandu", None, "Asia/Katmandu", None, "Asia/Khandyga", None, "Asia/Kolkata", None, "Asia/Krasnoyarsk", None, "Asia/Kuala_Lumpur", None, "Asia/Kuching", None, "Asia/Kuwait", None, "Asia/Macao", None, "Asia/Macau", None, "Asia/Magadan", None, "Asia/Makassar", None, "Asia/Manila", None, "Asia/Muscat", None, "Asia/Nicosia", None, "Asia/Novokuznetsk", None, "Asia/Novosibirsk", None, "Asia/Omsk", None, "Asia/Oral", None, "Asia/Phnom_Penh", None, "Asia/Pontianak", None, "Asia/Pyongyang", None, "Asia/Qatar", None, "Asia/Qostanay", None, "Asia/Qyzylorda", None, "Asia/Rangoon", None, "Asia/Riyadh", None, "Asia/Saigon", None, "Asia/Sakhalin", None, "Asia/Samarkand", None, "Asia/Seoul", None, "Asia/Shanghai", None, "Asia/Singapore", None, "Asia/Srednekolymsk", None, "Asia/Taipei", None, "Asia/Tashkent", None, "Asia/Tbilisi", None, "Asia/Tehran", None, "Asia/Tel_Aviv", None, "Asia/Thimbu", None, "Asia/Thimphu", None, "Asia/Tokyo", None, "Asia/Tomsk", None, "Asia/Ujung_Pandang", None, "Asia/Ulaanbaatar", None, "Asia/Ulan_Bator", None, "Asia/Urumqi", None, "Asia/Ust-Nera", None, "Asia/Vientiane", None, "Asia/Vladivostok", None, "Asia/Yakutsk", None, "Asia/Yangon", None, "Asia/Yekaterinburg", None, "Asia/Yerevan", None, "Atlantic/Azores", None, "Atlantic/Bermuda", None, "Atlantic/Canary", None, "Atlantic/Cape_Verde", None, "Atlantic/Faeroe", None, "Atlantic/Faroe", None, "Atlantic/Jan_Mayen", None, "Atlantic/Madeira", None, "Atlantic/Reykjavik", None, "Atlantic/South_Georgia", None, "Atlantic/St_Helena", None, "Atlantic/Stanley", None, "Australia/ACT", None, "Australia/Adelaide", None, "Australia/Brisbane", None, "Australia/Broken_Hill", None, "Australia/Canberra", None, "Australia/Currie", None, "Australia/Darwin", None, "Australia/Eucla", None, "Australia/Hobart", None, "Australia/LHI", None, "Australia/Lindeman", None, "Australia/Lord_Howe", None, "Australia/Melbourne", None, "Australia/NSW", None, "Australia/North", None, "Australia/Perth", None, "Australia/Queensland", None, "Australia/South", None, "Australia/Sydney", None, "Australia/Tasmania", None, "Australia/Victoria", None, "Australia/West", None, "Australia/Yancowinna", None, "Brazil/Acre", None, "Brazil/DeNoronha", None, "Brazil/East", None, "Brazil/West", None, "CET", None, "CST6CDT", None, "Canada/Atlantic", None, "Canada/Central", None, "Canada/Eastern", None, "Canada/Mountain", None, "Canada/Newfoundland", None, "Canada/Pacific", None, "Canada/Saskatchewan", None, "Canada/Yukon", None, "Chile/Continental", None, "Chile/EasterIsland", None, "Cuba", None, "EET", None, "EST", None, "EST5EDT", None, "Egypt", None, "Eire", None, "Etc/GMT", None, "Etc/GMT+0", None, "Etc/GMT+1", None, "Etc/GMT+10", None, "Etc/GMT+11", None, "Etc/GMT+12", None, "Etc/GMT+2", None, "Etc/GMT+3", None, "Etc/GMT+4", None, "Etc/GMT+5", None, "Etc/GMT+6", None, "Etc/GMT+7", None, "Etc/GMT+8", None, "Etc/GMT+9", None, "Etc/GMT-0", None, "Etc/GMT-1", None, "Etc/GMT-10", None, "Etc/GMT-11", None, "Etc/GMT-12", None, "Etc/GMT-13", None, "Etc/GMT-14", None, "Etc/GMT-2", None, "Etc/GMT-3", None, "Etc/GMT-4", None, "Etc/GMT-5", None, "Etc/GMT-6", None, "Etc/GMT-7", None, "Etc/GMT-8", None, "Etc/GMT-9", None, "Etc/GMT0", None, "Etc/Greenwich", None, "Etc/UCT", None, "Etc/UTC", None, "Etc/Universal", None, "Etc/Zulu", None, "Europe/Amsterdam", None, "Europe/Andorra", None, "Europe/Astrakhan", None, "Europe/Athens", None, "Europe/Belfast", None, "Europe/Belgrade", None, "Europe/Berlin", None, "Europe/Bratislava", None, "Europe/Brussels", None, "Europe/Bucharest", None, "Europe/Budapest", None, "Europe/Busingen", None, "Europe/Chisinau", None, "Europe/Copenhagen", None, "Europe/Dublin", None, "Europe/Gibraltar", None, "Europe/Guernsey", None, "Europe/Helsinki", None, "Europe/Isle_of_Man", None, "Europe/Istanbul", None, "Europe/Jersey", None, "Europe/Kaliningrad", None, "Europe/Kiev", None, "Europe/Kirov", None, "Europe/Kyiv", None, "Europe/Lisbon", None, "Europe/Ljubljana", None, "Europe/London", None, "Europe/Luxembourg", None, "Europe/Madrid", None, "Europe/Malta", None, "Europe/Mariehamn", None, "Europe/Minsk", None, "Europe/Monaco", None, "Europe/Moscow", None, "Europe/Nicosia", None, "Europe/Oslo", None, "Europe/Paris", None, "Europe/Podgorica", None, "Europe/Prague", None, "Europe/Riga", None, "Europe/Rome", None, "Europe/Samara", None, "Europe/San_Marino", None, "Europe/Sarajevo", None, "Europe/Saratov", None, "Europe/Simferopol", None, "Europe/Skopje", None, "Europe/Sofia", None, "Europe/Stockholm", None, "Europe/Tallinn", None, "Europe/Tirane", None, "Europe/Tiraspol", None, "Europe/Ulyanovsk", None, "Europe/Uzhgorod", None, "Europe/Vaduz", None, "Europe/Vatican", None, "Europe/Vienna", None, "Europe/Vilnius", None, "Europe/Volgograd", None, "Europe/Warsaw", None, "Europe/Zagreb", None, "Europe/Zaporozhye", None, "Europe/Zurich", None, "Factory", None, "GB", None, "GB-Eire", None, "GMT", None, "GMT+0", None, "GMT-0", None, "GMT0", None, "Greenwich", None, "HST", None, "Hongkong", None, "Iceland", None, "Indian/Antananarivo", None, "Indian/Chagos", None, "Indian/Christmas", None, "Indian/Cocos", None, "Indian/Comoro", None, "Indian/Kerguelen", None, "Indian/Mahe", None, "Indian/Maldives", None, "Indian/Mauritius", None, "Indian/Mayotte", None, "Indian/Reunion", None, "Iran", None, "Israel", None, "Jamaica", None, "Japan", None, "Kwajalein", None, "Libya", None, "MET", None, "MST", None, "MST7MDT", None, "Mexico/BajaNorte", None, "Mexico/BajaSur", None, "Mexico/General", None, "NZ", None, "NZ-CHAT", None, "Navajo", None, "PRC", None, "PST8PDT", None, "Pacific/Apia", None, "Pacific/Auckland", None, "Pacific/Bougainville", None, "Pacific/Chatham", None, "Pacific/Chuuk", None, "Pacific/Easter", None, "Pacific/Efate", None, "Pacific/Enderbury", None, "Pacific/Fakaofo", None, "Pacific/Fiji", None, "Pacific/Funafuti", None, "Pacific/Galapagos", None, "Pacific/Gambier", None, "Pacific/Guadalcanal", None, "Pacific/Guam", None, "Pacific/Honolulu", None, "Pacific/Johnston", None, "Pacific/Kanton", None, "Pacific/Kiritimati", None, "Pacific/Kosrae", None, "Pacific/Kwajalein", None, "Pacific/Majuro", None, "Pacific/Marquesas", None, "Pacific/Midway", None, "Pacific/Nauru", None, "Pacific/Niue", None, "Pacific/Norfolk", None, "Pacific/Noumea", None, "Pacific/Pago_Pago", None, "Pacific/Palau", None, "Pacific/Pitcairn", None, "Pacific/Pohnpei", None, "Pacific/Ponape", None, "Pacific/Port_Moresby", None, "Pacific/Rarotonga", None, "Pacific/Saipan", None, "Pacific/Samoa", None, "Pacific/Tahiti", None, "Pacific/Tarawa", None, "Pacific/Tongatapu", None, "Pacific/Truk", None, "Pacific/Wake", None, "Pacific/Wallis", None, "Pacific/Yap", None, "Poland", None, "Portugal", None, "ROC", None, "ROK", None, "Singapore", None, "Turkey", None, "UCT", None, "US/Alaska", None, "US/Aleutian", None, "US/Arizona", None, "US/Central", None, "US/East-Indiana", None, "US/Eastern", None, "US/Hawaii", None, "US/Indiana-Starke", None, "US/Michigan", None, "US/Mountain", None, "US/Pacific", None, "US/Samoa", None, "UTC", None, "Universal", None, "W-SU", None, "WET", None, "Zulu", None)
        self.mapped[5].resolve_generated_offset_with_values("asc", None, "desc", None)
        self.mapped[6].resolve_generated_offset_with_values("p1", float.fromhex("0x1p+0"), "p10", float.fromhex("0x1.999999999999ap-4"), "p100", float.fromhex("0x1.47ae147ae147bp-7"), "p1000", float.fromhex("0x1.0624dd2f1a9fcp-10"), "p10000", float.fromhex("0x1.a36e2eb1c432dp-14"), "p100000", float.fromhex("0x1.4f8b588e368f1p-17"), "p1000000", float.fromhex("0x1.0c6f7a0b5ed8dp-20"), "p10000000", float.fromhex("0x1.ad7f29abcaf48p-24"), "p100000000", float.fromhex("0x1.5798ee2308c3ap-27"), "p1000000000", float.fromhex("0x1.12e0be826d695p-30"), "p10000000000", float.fromhex("0x1.b7cdfd9d7bdbbp-34"))
        self.mapped[10].resolve_generated_offsets("x", "y")
        self.mapped[15].resolve_generated_offsets("size", "from", "to")
        self.mapped[16].static_values = [float.fromhex("0x1.5bf0a8b145769p+1"), float.fromhex("0x1.71547652b82fep+0"), float.fromhex("0x1.bcb7b1526e50ep-2"), float.fromhex("0x1.62e42fefa39efp-1"), float.fromhex("0x1.26bb1bbb55516p+1"), float.fromhex("0x1.921fb54442d18p+1"), float.fromhex("0x1.921fb54442d18p+0"), float.fromhex("0x1.921fb54442d18p-1"), float.fromhex("0x1.45f306dc9c883p-2"), float.fromhex("0x1.45f306dc9c883p-1"), float.fromhex("0x1.20dd750429b6dp+0"), float.fromhex("0x1.6a09e667f3bcdp+0"), float.fromhex("0x1.6a09e667f3bcdp-1")]
        self.mapped[22].resolve_generated_offsets("sw", "ne")
        self.mapped[23].resolve_generated_offset_with_values("microseconds", 1, "milliseconds", 1000, "seconds", 1000000, "minutes", 60000000, "hours", 3600000000, "days", 86400000000)
        self.mapped[25].resolve_generated_offsets("t", "v")
        self.mapped[27].resolve_generated_offsets("center", "radius")
        self.mapped[28].resolve_generated_offsets("points")
        self.mapped[29].resolve_generated_offsets("message", "stack")
        self.mapped[30].resolve_generated_offsets("module", "function", "line", "column")
        self.mapped[32].static_values = [greycat.create_geo(float.fromhex("-0x1.54345b1903bbap+6"), float.fromhex("-0x1.67fffffe98p+7")), greycat.create_geo(float.fromhex("0x1.54345b1903bbap+6"), float.fromhex("0x1.67fffffe98p+7"))]
        self.mapped[34].resolve_generated_offsets("column", "extractors")
        self.mapped[35].static_values = [greycat.create_time(-9223372036854775808), greycat.create_time(9223372036854775807)]
        self.mapped[37].resolve_generated_offset_with_values("i32", 4, "i64", 8, "f32", 4, "f64", 8, "c64", 8, "c128", 16)
        self.mapped[38].resolve_generated_offset_with_values("fixed", 0, "fixed_reg", 1, "adaptative", 2, "dense", 3)
        self.mapped[39].resolve_generated_offset_with_values("year", 0, "month", 1, "day", 2, "hour", 3, "minute", 4, "second", 5, "microsecond", 6)
        self.mapped[43].resolve_generated_offset_with_values("none", 0, "interrupted", 1, "await", 2, "timeout", 6, "forbidden", 7, "runtime_error", 8)
        self.mapped[44].resolve_generated_offset_with_values("empty", None, "waiting", None, "running", None, "await", None, "cancelled", None, "error", None, "ended", None, "ended_with_errors", None)
        self.mapped[45].resolve_generated_offsets("user_id", "task_id", "mod", "type", "fun", "creation", "start", "duration", "status", "progress")
        self.mapped[46].resolve_generated_offsets("email", "name", "first_name", "last_name", "roles", "groups")
        self.mapped[47].resolve_generated_offsets("name", "value")
        self.mapped[48].resolve_generated_offsets("duration", "bytes_write_disk", "bytes_write_disk_raw", "bytes_read_disk", "bytes_read_disk_raw", "bytes_read_cache")
        self.mapped[49].resolve_generated_offsets("version", "program_version", "arch", "timezone", "license", "io_threads", "bg_threads", "fg_threads", "mem_total", "mem_worker", "nb_ctx", "store_stats")
        self.mapped[50].resolve_generated_offsets("id", "name", "activated", "full_name", "email", "role", "groups", "groups_flags", "external")
        self.mapped[51].resolve_generated_offsets("offset", "pass")
        self.mapped[52].resolve_generated_offsets("name", "description")
        self.mapped[53].resolve_generated_offsets("group_id", "type")
        self.mapped[54].resolve_generated_offsets("url", "clientId")
        self.mapped[55].resolve_generated_offsets("id", "frames", "root")
        self.mapped[56].resolve_generated_offsets("module", "type", "function", "src", "line", "column", "scope")
        self.mapped[58].resolve_generated_offsets("name", "start", "end", "company", "max_memory", "extra_1", "extra_2", "type")
        self.mapped[59].resolve_generated_offsets("capacity_bytes", "allocated_bytes", "allocated_ratio", "remained_bytes", "remained_ratio", "used_bytes", "used_ratio", "available_bytes", "available_ratio")
        self.mapped[60].resolve_generated_offsets("level", "time", "user_id", "id", "id2", "src", "tag", "data")
        self.mapped[61].resolve_generated_offsets("id", "name", "activated")
        self.mapped[62].resolve_generated_offset_with_values("read", None, "write", None, "execute", None)
        self.mapped[64].resolve_generated_offsets("id", "name", "activated")
        self.mapped[65].resolve_generated_offset_with_values("error", None, "warn", None, "info", None, "perf", None, "trace", None)
        self.mapped[66].resolve_generated_offset_with_values("community", None, "enterprise", None, "testing", None)
        self.mapped[67].resolve_generated_offsets("function", "user_id", "arguments", "start", "every")
        self.mapped[68].resolve_generated_offsets("name", "permissions")
        self.mapped[69].resolve_generated_offsets("function", "arguments")
        self.mapped[70].resolve_generated_offsets("entities", "credentials", "fields", "keys", "keys_last_refresh")
        self.mapped[71].resolve_generated_offsets("path", "pos")
        self.mapped[72].resolve_generated_offsets("name", "value")
        self.mapped[74].resolve_generated_offset_with_values("plain", 0, "ssl_tls", 1, "starttls", 2)
        self.mapped[75].resolve_generated_offsets("id", "column", "modulo")
        self.mapped[76].resolve_generated_offsets("path", "pos")
        self.mapped[77].resolve_generated_offsets("header_lines", "separator", "string_delimiter", "decimal_separator", "thousands_separator", "row_limit", "enumerable_limit", "date_check_limit", "date_formats")
        self.mapped[77].static_values = [100, 100]
        self.mapped[79].resolve_generated_offsets("path", "pos", "format", "sharding")
        self.mapped[80].resolve_generated_offset_with_values("plain", None, "base64", None, "base64url", None, "hexadecimal", None)
        self.mapped[81].resolve_generated_offsets("header_lines", "separator", "string_delimiter", "decimal_separator", "thousands_separator", "columns", "line_count", "fail_count", "file_count")
        self.mapped[82].resolve_generated_offsets("path", "pos")
        self.mapped[83].resolve_generated_offsets("path", "append")
        self.mapped[84].resolve_generated_offsets("path", "append")
        self.mapped[85].resolve_generated_offsets("path")
        self.mapped[86].resolve_generated_offset_with_values("none", 0, "plain", 1, "login", 2)
        self.mapped[87].resolve_generated_offsets("protocol", "host", "port", "path", "params", "hash")
        self.mapped[88].resolve_generated_offsets("from", "subject", "body", "body_is_html", "to", "cc", "bcc")
        self.mapped[89].resolve_generated_offsets("host", "port", "mode", "authenticate", "user", "pass")
        self.mapped[90].resolve_generated_offsets("path", "size", "last_modification")
        self.mapped[91].resolve_generated_offsets("path", "append", "format")
        self.mapped[92].resolve_generated_offsets("path", "append")
        self.mapped[93].resolve_generated_offsets("path", "append")
        self.mapped[94].resolve_generated_offsets("path", "pos")
        self.mapped[95].resolve_generated_offsets("header_lines", "separator", "string_delimiter", "decimal_separator", "thousands_separator", "trim", "format", "tz", "strict")
        self.mapped[96].resolve_generated_offsets("name", "example", "null_count", "bool_count", "int_count", "float_count", "string_count", "date_count", "date_format_count", "enumerable_count", "profile")
        self.mapped[98].resolve_generated_offsets("line_count", "fail_count", "invalid_count")
        self.mapped[100].resolve_generated_offsets("min", "max", "step_starts", "open")
        self.mapped[102].resolve_generated_offsets("values", "span", "sum", "sumsq", "field")
        self.mapped[103].resolve_generated_offsets("min", "max", "center")
        self.mapped[104].resolve_generated_offsets("quantizer", "bins", "nb_rejected", "nb_accepted")
        self.mapped[106].resolve_generated_offsets("min", "max", "whisker_low", "whisker_high", "percentile1", "percentile5", "percentile25", "percentile50", "percentile75", "percentile95", "percentile99", "count_outliers_low", "count_outliers_high", "percentage_outliers_low", "percentage_outliers_high", "sum", "avg", "std", "size")
        self.mapped[107].resolve_generated_offsets("min", "max", "bins", "open")
        self.mapped[108].resolve_generated_offsets("seed", "v")
        self.mapped[109].resolve_generated_offsets("min", "max", "bins", "open")
        self.mapped[110].resolve_generated_offsets("quantizer", "precision", "bins", "value_min", "nb_rejected")
        self.mapped[111].resolve_generated_offsets("quantizers")
        self.mapped[112].resolve_generated_offsets("values")
        self.mapped[113].resolve_generated_offsets("values", "span", "sum", "sumsq", "field")
        self.mapped[114].resolve_generated_offsets("sum", "sumsq", "count")
        self.mapped[115].resolve_generated_offsets("start", "total", "counter", "duration", "progress", "speed", "remaining")
        self.mapped[117].resolve_generated_offsets("values", "capacity")
        self.mapped[118].resolve_generated_offsets("sum", "sumsq", "count", "min", "max")
