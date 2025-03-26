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
            def from_time(time: std.core.time, tz: std.core.TimeZone, __greycat: Optional[GreyCat] = None) -> std.core.Date:
                if __greycat is None:
                    __greycat  = GreyCat._DEFAULT
                return __greycat.call("core::Date::from_time", [time, tz, ])

            @staticmethod
            def create(year: int, month: int, day: int, hour: int, minute: int, second: int, microsecond: int, greycat: GreyCat | None = None) -> std.core.Date:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.core.Date(greycat.libs_by_name[std.name_].mapped[0], [year, month, day, hour, minute, second, microsecond])

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
            def create(n: std.core.nodeTime, req_time: std.core.time, greycat: GreyCat | None = None) -> std.core.nodeTimeCursor[TypeVar("T")]:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.core.nodeTimeCursor(greycat.libs_by_name[std.name_].mapped[1], [n, req_time])

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

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def __class_getitem__(cls, key) -> std.core.TimeZone:
                greycat: GreyCat
                if isinstance(key, tuple):
                    key, greycat = key
                else:
                    greycat = GreyCat._DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[2]
                return t.enum_values[t.generated_offsets[std.core.TimeZone.__indices_by_values[key]]]

            @staticmethod
            def create(greycat: GreyCat | None = None) -> std.core.TimeZone:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.core.TimeZone(greycat.libs_by_name[std.name_].mapped[2], [])

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
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[3]
                return t.enum_values[t.generated_offsets[std.core.TimeZone.__indices_by_values[key]]]

            @staticmethod
            def create(greycat: GreyCat | None = None) -> std.core.SortOrder:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.core.SortOrder(greycat.libs_by_name[std.name_].mapped[3], [])

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
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[4]
                return t.enum_values[t.generated_offsets[std.core.TimeZone.__indices_by_values[key]]]

            @staticmethod
            def create(greycat: GreyCat | None = None) -> std.core.FloatPrecision:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.core.FloatPrecision(greycat.libs_by_name[std.name_].mapped[4], [])

        @final
        class t3f(std_n.core._t3f):
            name_: Final[str] = "core::t3f"

            def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
                super().__init__(type)

            @staticmethod
            def create(greycat: GreyCat | None = None) -> std_n.core._t3f:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.core.t3f(greycat.libs_by_name[std.name_].mapped[5], [])

        @final
        class Array(Generic[__T], std_n.core._Array[__T]):
            name_: Final[str] = "core::Array"

            def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
                super().__init__(type)

            @staticmethod
            def create(greycat: GreyCat | None = None) -> std_n.core._Array:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.core.Array(greycat.libs_by_name[std.name_].mapped[6], [])

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
            def create(x: std.core.__, y: std.core.__, greycat: GreyCat | None = None) -> std.core.Tuple[TypeVar("T"), TypeVar("U")]:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.core.Tuple(greycat.libs_by_name[std.name_].mapped[7], [x, y])

        @final
        class String(std_n.core._String):
            name_: Final[str] = "core::String"

            def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
                super().__init__(type)

            @staticmethod
            def create(greycat: GreyCat | None = None) -> std_n.core._String:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.core.String(greycat.libs_by_name[std.name_].mapped[8], [])

        @final
        class Map(Generic[__K, __V], std_n.core._Map[__K, __V]):
            name_: Final[str] = "core::Map"

            def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
                super().__init__(type)

            @staticmethod
            def create(greycat: GreyCat | None = None) -> std_n.core._Map:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.core.Map(greycat.libs_by_name[std.name_].mapped[9], [])

        @final
        class field(std_n.core._field):
            name_: Final[str] = "core::field"

            def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
                super().__init__(type)

            @staticmethod
            def create(greycat: GreyCat | None = None) -> std_n.core._field:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.core.field(greycat.libs_by_name[std.name_].mapped[10], [])

        @final
        class t2(std_n.core._t2):
            name_: Final[str] = "core::t2"

            def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
                super().__init__(type)

            @staticmethod
            def create(greycat: GreyCat | None = None) -> std_n.core._t2:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.core.t2(greycat.libs_by_name[std.name_].mapped[11], [])

        @final
        class Tensor(std_n.core._Tensor):
            name_: Final[str] = "core::Tensor"

            def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
                super().__init__(type)

            @staticmethod
            def create(greycat: GreyCat | None = None) -> std_n.core._Tensor:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.core.Tensor(greycat.libs_by_name[std.name_].mapped[12], [])

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
            def create(size: int, from_: std.core.__, to: std.core.__, greycat: GreyCat | None = None) -> std.core.NodeInfo[TypeVar("T")]:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.core.NodeInfo(greycat.libs_by_name[std.name_].mapped[13], [size, from_, to])

        @final
        class t4f(std_n.core._t4f):
            name_: Final[str] = "core::t4f"

            def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
                super().__init__(type)

            @staticmethod
            def create(greycat: GreyCat | None = None) -> std_n.core._t4f:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.core.t4f(greycat.libs_by_name[std.name_].mapped[14], [])

        @final
        class t2f(std_n.core._t2f):
            name_: Final[str] = "core::t2f"

            def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
                super().__init__(type)

            @staticmethod
            def create(greycat: GreyCat | None = None) -> std_n.core._t2f:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.core.t2f(greycat.libs_by_name[std.name_].mapped[15], [])

        @final
        class type(std_n.core._type):
            name_: Final[str] = "core::type"

            def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
                super().__init__(type)

            @staticmethod
            def create(greycat: GreyCat | None = None) -> std_n.core._type:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.core.type(greycat.libs_by_name[std.name_].mapped[16], [])

        @final
        class nodeIndex(Generic[__K, __V], std_n.core._nodeIndex[__K, __V]):
            name_: Final[str] = "core::nodeIndex"

            def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
                super().__init__(type)

            @staticmethod
            def create(greycat: GreyCat | None = None) -> std_n.core._nodeIndex:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.core.nodeIndex(greycat.libs_by_name[std.name_].mapped[17], [])

        @final
        class Table(Generic[__T], std_n.core._Table[__T]):
            name_: Final[str] = "core::Table"

            def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
                super().__init__(type)

            @staticmethod
            def create(greycat: GreyCat | None = None) -> std_n.core._Table:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.core.Table(greycat.libs_by_name[std.name_].mapped[18], [])

        @final
        class Buffer(std_n.core._Buffer):
            name_: Final[str] = "core::Buffer"

            def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
                super().__init__(type)

            @staticmethod
            def create(greycat: GreyCat | None = None) -> std_n.core._Buffer:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.core.Buffer(greycat.libs_by_name[std.name_].mapped[19], [])

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
            def create(sw: std.core.geo, ne: std.core.geo, greycat: GreyCat | None = None) -> std.core.GeoBox:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.core.GeoBox(greycat.libs_by_name[std.name_].mapped[20], [sw, ne])

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
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[21]
                return t.enum_values[t.generated_offsets[std.core.TimeZone.__indices_by_values[key]]]

            @staticmethod
            def create(greycat: GreyCat | None = None) -> std.core.DurationUnit:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.core.DurationUnit(greycat.libs_by_name[std.name_].mapped[21], [])

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
            def create(t: std.core.time, v: Any, greycat: GreyCat | None = None) -> std.core.nodeTimeSingleton:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.core.nodeTimeSingleton(greycat.libs_by_name[std.name_].mapped[22], [t, v])

        @final
        class nodeTime(Generic[__T], std_n.core._nodeTime[__T]):
            name_: Final[str] = "core::nodeTime"

            def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
                super().__init__(type)

            @staticmethod
            def create(greycat: GreyCat | None = None) -> std_n.core._nodeTime:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.core.nodeTime(greycat.libs_by_name[std.name_].mapped[23], [])

        @final
        class nodeList(Generic[__T], std_n.core._nodeList[__T]):
            name_: Final[str] = "core::nodeList"

            def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
                super().__init__(type)

            @staticmethod
            def create(greycat: GreyCat | None = None) -> std_n.core._nodeList:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.core.nodeList(greycat.libs_by_name[std.name_].mapped[24], [])

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
            def create(center: std.core.geo, radius: float, greycat: GreyCat | None = None) -> std.core.GeoCircle:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.core.GeoCircle(greycat.libs_by_name[std.name_].mapped[25], [center, radius])

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
            def create(points: std.core.Array, greycat: GreyCat | None = None) -> std.core.GeoPoly:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.core.GeoPoly(greycat.libs_by_name[std.name_].mapped[26], [points])

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
            def create(message: str, stack: std.core.Array, greycat: GreyCat | None = None) -> std.core.Error:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.core.Error(greycat.libs_by_name[std.name_].mapped[27], [message, stack])

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
            def create(module: str, function: str, line: int, column: int, greycat: GreyCat | None = None) -> std.core.ErrorFrame:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.core.ErrorFrame(greycat.libs_by_name[std.name_].mapped[28], [module, function, line, column])

        @final
        class duration(std_n.core._duration):
            name_: Final[str] = "core::duration"

            def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
                super().__init__(type)

            @staticmethod
            def create(greycat: GreyCat | None = None) -> std_n.core._duration:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.core.duration(greycat.libs_by_name[std.name_].mapped[29], [])

        @final
        class t3(std_n.core._t3):
            name_: Final[str] = "core::t3"

            def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
                super().__init__(type)

            @staticmethod
            def create(greycat: GreyCat | None = None) -> std_n.core._t3:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.core.t3(greycat.libs_by_name[std.name_].mapped[30], [])

        @final
        class geo(std_n.core._geo):
            name_: Final[str] = "core::geo"

            def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
                super().__init__(type)

            @staticmethod
            def create(greycat: GreyCat | None = None) -> std_n.core._geo:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.core.geo(greycat.libs_by_name[std.name_].mapped[31], [])

        @final
        class MathConstants(GreyCat.Object):
            name_: Final[str] = "core::MathConstants"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            @staticmethod
            def e(greycat: GreyCat | None = None) -> float:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[32]
                return t.static_values[0]

            @staticmethod
            def log_2e(greycat: GreyCat | None = None) -> float:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[32]
                return t.static_values[1]

            @staticmethod
            def log_10e(greycat: GreyCat | None = None) -> float:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[32]
                return t.static_values[2]

            @staticmethod
            def ln2(greycat: GreyCat | None = None) -> float:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[32]
                return t.static_values[3]

            @staticmethod
            def ln10(greycat: GreyCat | None = None) -> float:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[32]
                return t.static_values[4]

            @staticmethod
            def pi(greycat: GreyCat | None = None) -> float:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[32]
                return t.static_values[5]

            @staticmethod
            def pi_2(greycat: GreyCat | None = None) -> float:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[32]
                return t.static_values[6]

            @staticmethod
            def pi_4(greycat: GreyCat | None = None) -> float:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[32]
                return t.static_values[7]

            @staticmethod
            def m1_pi(greycat: GreyCat | None = None) -> float:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[32]
                return t.static_values[8]

            @staticmethod
            def m2_pi(greycat: GreyCat | None = None) -> float:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[32]
                return t.static_values[9]

            @staticmethod
            def m2_sqrt_pi(greycat: GreyCat | None = None) -> float:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[32]
                return t.static_values[10]

            @staticmethod
            def sqrt2(greycat: GreyCat | None = None) -> float:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[32]
                return t.static_values[11]

            @staticmethod
            def sqrt1_2(greycat: GreyCat | None = None) -> float:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[32]
                return t.static_values[12]

            @staticmethod
            def create(greycat: GreyCat | None = None) -> std.core.MathConstants:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.core.MathConstants(greycat.libs_by_name[std.name_].mapped[32], [])

        @final
        class function(std_n.core._function):
            name_: Final[str] = "core::function"

            def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
                super().__init__(type)

            @staticmethod
            def create(greycat: GreyCat | None = None) -> std_n.core._function:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
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
            def create(column: int, extractors: std.core.Array, greycat: GreyCat | None = None) -> std.core.TableColumnMapping:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.core.TableColumnMapping(greycat.libs_by_name[std.name_].mapped[34], [column, extractors])

        @final
        class time(std_n.core._time):
            name_: Final[str] = "core::time"

            def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
                super().__init__(type)

            @staticmethod
            def create(greycat: GreyCat | None = None) -> std_n.core._time:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.core.time(greycat.libs_by_name[std.name_].mapped[35], [])

        @final
        class str(std_n.core._str):
            name_: Final[str] = "core::str"

            def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
                super().__init__(type)

            @staticmethod
            def create(greycat: GreyCat | None = None) -> std_n.core._str:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.core.str(greycat.libs_by_name[std.name_].mapped[36], [])

        @final
        class t4(std_n.core._t4):
            name_: Final[str] = "core::t4"

            def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
                super().__init__(type)

            @staticmethod
            def create(greycat: GreyCat | None = None) -> std_n.core._t4:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.core.t4(greycat.libs_by_name[std.name_].mapped[37], [])

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
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[38]
                return t.enum_values[t.generated_offsets[std.core.TimeZone.__indices_by_values[key]]]

            @staticmethod
            def create(greycat: GreyCat | None = None) -> std.core.TensorType:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.core.TensorType(greycat.libs_by_name[std.name_].mapped[38], [])

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
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[39]
                return t.enum_values[t.generated_offsets[std.core.TimeZone.__indices_by_values[key]]]

            @staticmethod
            def create(greycat: GreyCat | None = None) -> std.core.SamplingMode:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.core.SamplingMode(greycat.libs_by_name[std.name_].mapped[39], [])

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
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[40]
                return t.enum_values[t.generated_offsets[std.core.TimeZone.__indices_by_values[key]]]

            @staticmethod
            def create(greycat: GreyCat | None = None) -> std.core.CalendarUnit:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.core.CalendarUnit(greycat.libs_by_name[std.name_].mapped[40], [])

        @final
        class node(Generic[__T], std_n.core._node[__T]):
            name_: Final[str] = "core::node"

            def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
                super().__init__(type)

            @staticmethod
            def create(greycat: GreyCat | None = None) -> std_n.core._node:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.core.node(greycat.libs_by_name[std.name_].mapped[41], [])

        @final
        class nodeGeo(Generic[__T], std_n.core._nodeGeo[__T]):
            name_: Final[str] = "core::nodeGeo"

            def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
                super().__init__(type)

            @staticmethod
            def create(greycat: GreyCat | None = None) -> std_n.core._nodeGeo:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
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
            def create(greycat: GreyCat | None = None) -> std.core.ErrorCode:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.core.ErrorCode(greycat.libs_by_name[std.name_].mapped[43], [])

    @final
    class runtime:
        __T = TypeVar("__T")

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
            def create(group_id: int, type: std.runtime.UserGroupPolicyType, greycat: GreyCat | None = None) -> std.runtime.UserGroupPolicy:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.runtime.UserGroupPolicy(greycat.libs_by_name[std.name_].mapped[44], [group_id, type])

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
            def create(name: str, start: std.core.time, end: std.core.time, company: str, max_memory: int, extra_1: int, extra_2: int, type: std.runtime.LicenseType, greycat: GreyCat | None = None) -> std.runtime.License:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.runtime.License(greycat.libs_by_name[std.name_].mapped[45], [name, start, end, company, max_memory, extra_1, extra_2, type])

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

            def disk_data_bytes(self) -> int:
                return self._get(self.type_.generated_offsets[10])

            def set_disk_data_bytes(self, v: int) -> None:
                self._set(self.type_.generated_offsets[10], v)

            @staticmethod
            def create(version: str, program_version: str, arch: str, timezone: std.core.TimeZone, license: std.runtime.License, io_threads: int, bg_threads: int, fg_threads: int, mem_total: int, mem_worker: int, disk_data_bytes: int, greycat: GreyCat | None = None) -> std.runtime.RuntimeInfo:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.runtime.RuntimeInfo(greycat.libs_by_name[std.name_].mapped[46], [version, program_version, arch, timezone, license, io_threads, bg_threads, fg_threads, mem_total, mem_worker, disk_data_bytes])

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
                    __greycat  = GreyCat._DEFAULT
                return __greycat.call("runtime::Debug::resume", [id, ])

            @staticmethod
            def get(id: int, __greycat: Optional[GreyCat] = None) -> std.runtime.Debug:
                if __greycat is None:
                    __greycat  = GreyCat._DEFAULT
                return __greycat.call("runtime::Debug::get", [id, ])

            @staticmethod
            def all(__greycat: Optional[GreyCat] = None) -> std.core.Array:
                if __greycat is None:
                    __greycat  = GreyCat._DEFAULT
                return __greycat.call("runtime::Debug::all")

            @staticmethod
            def create(id: int, frames: std.core.Array, root: Any, greycat: GreyCat | None = None) -> std.runtime.Debug:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.runtime.Debug(greycat.libs_by_name[std.name_].mapped[47], [id, frames, root])

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
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[48]
                return t.enum_values[t.generated_offsets[std.core.TimeZone.__indices_by_values[key]]]

            @staticmethod
            def create(greycat: GreyCat | None = None) -> std.runtime.LogLevel:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.runtime.LogLevel(greycat.libs_by_name[std.name_].mapped[48], [])

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
            def create(offset: int, pass_: str, greycat: GreyCat | None = None) -> std.runtime.UserCredential:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.runtime.UserCredential(greycat.libs_by_name[std.name_].mapped[49], [offset, pass_])

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
                    __greycat  = GreyCat._DEFAULT
                return __greycat.call("runtime::Task::is_running", [task_id, ])

            @staticmethod
            def cancel(task_id: int, __greycat: Optional[GreyCat] = None) -> bool:
                if __greycat is None:
                    __greycat  = GreyCat._DEFAULT
                return __greycat.call("runtime::Task::cancel", [task_id, ])

            @staticmethod
            def history(offset: int, max: int, __greycat: Optional[GreyCat] = None) -> std.core.Array:
                if __greycat is None:
                    __greycat  = GreyCat._DEFAULT
                return __greycat.call("runtime::Task::history", [offset, max, ])

            @staticmethod
            def running(__greycat: Optional[GreyCat] = None) -> std.core.Array:
                if __greycat is None:
                    __greycat  = GreyCat._DEFAULT
                return __greycat.call("runtime::Task::running")

            @staticmethod
            def create(user_id: int, task_id: int, mod: str, type: str, fun: str, creation: std.core.time, start: std.core.time, duration: std.core.duration, status: std.runtime.TaskStatus, progress: float, greycat: GreyCat | None = None) -> std.runtime.Task:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.runtime.Task(greycat.libs_by_name[std.name_].mapped[50], [user_id, task_id, mod, type, fun, creation, start, duration, status, progress])

        @final
        class Runtime(GreyCat.Object):
            name_: Final[str] = "runtime::Runtime"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

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
            def info(__greycat: Optional[GreyCat] = None) -> std.runtime.RuntimeInfo:
                if __greycat is None:
                    __greycat  = GreyCat._DEFAULT
                return __greycat.call("runtime::Runtime::info")

            @staticmethod
            def create(greycat: GreyCat | None = None) -> std.runtime.Runtime:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.runtime.Runtime(greycat.libs_by_name[std.name_].mapped[51], [])

        @final
        class System(GreyCat.Object):
            name_: Final[str] = "runtime::System"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            @staticmethod
            def create(greycat: GreyCat | None = None) -> std.runtime.System:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.runtime.System(greycat.libs_by_name[std.name_].mapped[52], [])

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
            def create(duration: std.core.duration, bytes_write_disk: int, bytes_write_disk_raw: int, bytes_read_disk: int, bytes_read_disk_raw: int, bytes_read_cache: int, greycat: GreyCat | None = None) -> std.runtime.CallPerf:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.runtime.CallPerf(greycat.libs_by_name[std.name_].mapped[53], [duration, bytes_write_disk, bytes_write_disk_raw, bytes_read_disk, bytes_read_disk_raw, bytes_read_cache])

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
            def create(entities: std.core.Array, credentials: std.core.Map, fields: std.runtime.SecurityFields, keys: std.core.Map, keys_last_refresh: std.core.time, greycat: GreyCat | None = None) -> std.runtime.SecurityPolicy:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.runtime.SecurityPolicy(greycat.libs_by_name[std.name_].mapped[54], [entities, credentials, fields, keys, keys_last_refresh])

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
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[55]
                return t.enum_values[t.generated_offsets[std.core.TimeZone.__indices_by_values[key]]]

            @staticmethod
            def create(greycat: GreyCat | None = None) -> std.runtime.UserGroupPolicyType:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.runtime.UserGroupPolicyType(greycat.libs_by_name[std.name_].mapped[55], [])

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
            def create(level: std.runtime.LogLevel, time: std.core.time, user_id: int, id: int, id2: int, src: str, tag: str, data: Any, greycat: GreyCat | None = None) -> std.runtime.Log:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.runtime.Log(greycat.libs_by_name[std.name_].mapped[56], [level, time, user_id, id, id2, src, tag, data])

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
                    __greycat  = GreyCat._DEFAULT
                return __greycat.call("runtime::SecurityEntity::set", [entity, ])

            @staticmethod
            def all(__greycat: Optional[GreyCat] = None) -> std.core.Array:
                if __greycat is None:
                    __greycat  = GreyCat._DEFAULT
                return __greycat.call("runtime::SecurityEntity::all")

            @staticmethod
            def create(id: int, name: str, activated: bool, greycat: GreyCat | None = None) -> std.runtime.SecurityEntity:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.runtime.SecurityEntity(greycat.libs_by_name[std.name_].mapped[57], [id, name, activated])

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
            def create(id: int, name: str, activated: bool, greycat: GreyCat | None = None) -> std.runtime.UserGroup:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.runtime.UserGroup(greycat.libs_by_name[std.name_].mapped[58], [id, name, activated])

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
                    __greycat  = GreyCat._DEFAULT
                return __greycat.call("runtime::User::setPassword", [name, pass_, ])

            @staticmethod
            def permissions(__greycat: Optional[GreyCat] = None) -> std.core.Array:
                if __greycat is None:
                    __greycat  = GreyCat._DEFAULT
                return __greycat.call("runtime::User::permissions")

            @staticmethod
            def me(__greycat: Optional[GreyCat] = None) -> std.runtime.User:
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

            @staticmethod
            def create(id: int, name: str, activated: bool, full_name: str, email: str, role: str, groups: std.core.Array, groups_flags: int, external: bool, greycat: GreyCat | None = None) -> std.runtime.User:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.runtime.User(greycat.libs_by_name[std.name_].mapped[59], [id, name, activated, full_name, email, role, groups, groups_flags, external])

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
            def create(function: std.core.function, arguments: std.core.Array, greycat: GreyCat | None = None) -> std.runtime.Job[TypeVar("T")]:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.runtime.Job(greycat.libs_by_name[std.name_].mapped[60], [function, arguments])

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
                    __greycat  = GreyCat._DEFAULT
                return __greycat.call("runtime::SecurityFields::get")

            @staticmethod
            def set(f: std.runtime.SecurityFields, __greycat: Optional[GreyCat] = None) -> None:
                if __greycat is None:
                    __greycat  = GreyCat._DEFAULT
                return __greycat.call("runtime::SecurityFields::set", [f, ])

            @staticmethod
            def create(email: str, name: str, first_name: str, last_name: str, roles: std.core.Map, groups: std.core.Map, greycat: GreyCat | None = None) -> std.runtime.SecurityFields:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.runtime.SecurityFields(greycat.libs_by_name[std.name_].mapped[61], [email, name, first_name, last_name, roles, groups])

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
                    __greycat  = GreyCat._DEFAULT
                return __greycat.call("runtime::Permission::all")

            @staticmethod
            def create(name: str, description: str, greycat: GreyCat | None = None) -> std.runtime.Permission:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.runtime.Permission(greycat.libs_by_name[std.name_].mapped[62], [name, description])

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
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[63]
                return t.enum_values[t.generated_offsets[std.core.TimeZone.__indices_by_values[key]]]

            @staticmethod
            def create(greycat: GreyCat | None = None) -> std.runtime.LicenseType:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.runtime.LicenseType(greycat.libs_by_name[std.name_].mapped[63], [])

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
            def create(name: str, value: Any, greycat: GreyCat | None = None) -> std.runtime.Variable:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.runtime.Variable(greycat.libs_by_name[std.name_].mapped[64], [name, value])

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
                    __greycat  = GreyCat._DEFAULT
                return __greycat.call("runtime::PeriodicTask::set", [tasks, ])

            @staticmethod
            def all(__greycat: Optional[GreyCat] = None) -> std.core.Array:
                if __greycat is None:
                    __greycat  = GreyCat._DEFAULT
                return __greycat.call("runtime::PeriodicTask::all")

            @staticmethod
            def create(function: std.core.function, user_id: int, arguments: std.core.Array, start: std.core.time, every: std.core.duration, greycat: GreyCat | None = None) -> std.runtime.PeriodicTask:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.runtime.PeriodicTask(greycat.libs_by_name[std.name_].mapped[65], [function, user_id, arguments, start, every])

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
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[66]
                return t.enum_values[t.generated_offsets[std.core.TimeZone.__indices_by_values[key]]]

            @staticmethod
            def create(greycat: GreyCat | None = None) -> std.runtime.TaskStatus:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.runtime.TaskStatus(greycat.libs_by_name[std.name_].mapped[66], [])

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
                    __greycat  = GreyCat._DEFAULT
                return __greycat.call("runtime::Role::all")

            @staticmethod
            def create(name: str, permissions: std.core.Array, greycat: GreyCat | None = None) -> std.runtime.Role:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.runtime.Role(greycat.libs_by_name[std.name_].mapped[67], [name, permissions])

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
                    __greycat  = GreyCat._DEFAULT
                return __greycat.call("runtime::OpenIDConnect::config")

            @staticmethod
            def create(url: str, clientId: str, greycat: GreyCat | None = None) -> std.runtime.OpenIDConnect:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.runtime.OpenIDConnect(greycat.libs_by_name[std.name_].mapped[68], [url, clientId])

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
            def create(module: str, type: str, function: str, src: str, line: int, column: int, scope: std.core.Array, greycat: GreyCat | None = None) -> std.runtime.Frame:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.runtime.Frame(greycat.libs_by_name[std.name_].mapped[69], [module, type, function, src, line, column, scope])

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
            def create(path: str, pos: int, greycat: GreyCat | None = None) -> std.io.JsonReader[TypeVar("T")]:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.io.JsonReader(greycat.libs_by_name[std.name_].mapped[70], [path, pos])

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
            def create(protocol: str, host: str, port: int, path: str, params: std.core.Map, hash: str, greycat: GreyCat | None = None) -> std.io.Url:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.io.Url(greycat.libs_by_name[std.name_].mapped[71], [protocol, host, port, path, params, hash])

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
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[72]
                return t.enum_values[t.generated_offsets[std.core.TimeZone.__indices_by_values[key]]]

            @staticmethod
            def create(greycat: GreyCat | None = None) -> std.io.SmtpMode:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.io.SmtpMode(greycat.libs_by_name[std.name_].mapped[72], [])

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
            def create(path: str, append: bool, greycat: GreyCat | None = None) -> std.io.GcbWriter[TypeVar("T")]:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.io.GcbWriter(greycat.libs_by_name[std.name_].mapped[73], [path, append])

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

            def nearest_time(self) -> bool:
                return self._get(self.type_.generated_offsets[9])

            def set_nearest_time(self, v: bool) -> None:
                self._set(self.type_.generated_offsets[9], v)

            @staticmethod
            def create(header_lines: int, separator: c_char, string_delimiter: c_char, decimal_separator: c_char, thousands_separator: c_char, trim: bool, format: str, tz: std.core.TimeZone, strict: bool, nearest_time: bool, greycat: GreyCat | None = None) -> std.io.CsvFormat:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.io.CsvFormat(greycat.libs_by_name[std.name_].mapped[74], [header_lines, separator, string_delimiter, decimal_separator, thousands_separator, trim, format, tz, strict, nearest_time])

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
            def create(path: str, greycat: GreyCat | None = None) -> std.io.FileWalker:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.io.FileWalker(greycat.libs_by_name[std.name_].mapped[75], [path])

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
            def create(path: str, append: bool, greycat: GreyCat | None = None) -> std.io.JsonWriter[TypeVar("T")]:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.io.JsonWriter(greycat.libs_by_name[std.name_].mapped[76], [path, append])

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
            def create(path: str, append: bool, format: std.io.CsvFormat, greycat: GreyCat | None = None) -> std.io.CsvWriter[TypeVar("T")]:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.io.CsvWriter(greycat.libs_by_name[std.name_].mapped[77], [path, append, format])

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
            def create(path: str, append: bool, greycat: GreyCat | None = None) -> std.io.TextWriter[TypeVar("T")]:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.io.TextWriter(greycat.libs_by_name[std.name_].mapped[78], [path, append])

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
            def create(path: str, pos: int, greycat: GreyCat | None = None) -> std.io.Reader[TypeVar("T")]:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.io.Reader(greycat.libs_by_name[std.name_].mapped[79], [path, pos])

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
            def create(host: str, port: int, mode: std.io.SmtpMode, authenticate: std.io.SmtpAuth, user: str, pass_: str, greycat: GreyCat | None = None) -> std.io.Smtp:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.io.Smtp(greycat.libs_by_name[std.name_].mapped[80], [host, port, mode, authenticate, user, pass_])

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
            def create(path: str, pos: int, greycat: GreyCat | None = None) -> std.io.GcbReader[TypeVar("T")]:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.io.GcbReader(greycat.libs_by_name[std.name_].mapped[81], [path, pos])

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
            def create(name: str, example: Any, null_count: int, bool_count: int, int_count: int, float_count: int, string_count: int, date_count: int, date_format_count: std.core.Map, enumerable_count: std.core.Map, profile: std.util.Gaussian, greycat: GreyCat | None = None) -> std.io.CsvColumnStatistics:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.io.CsvColumnStatistics(greycat.libs_by_name[std.name_].mapped[82], [name, example, null_count, bool_count, int_count, float_count, string_count, date_count, date_format_count, enumerable_count, profile])

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
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[83]
                return t.enum_values[t.generated_offsets[std.core.TimeZone.__indices_by_values[key]]]

            @staticmethod
            def create(greycat: GreyCat | None = None) -> std.io.SmtpAuth:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.io.SmtpAuth(greycat.libs_by_name[std.name_].mapped[83], [])

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
            def create(name: str, value: str, greycat: GreyCat | None = None) -> std.io.HttpHeader:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.io.HttpHeader(greycat.libs_by_name[std.name_].mapped[84], [name, value])

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
            def create(from_: str, subject: str, body: str, body_is_html: bool, to: std.core.Array, cc: std.core.Array, bcc: std.core.Array, greycat: GreyCat | None = None) -> std.io.Email:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.io.Email(greycat.libs_by_name[std.name_].mapped[85], [from_, subject, body, body_is_html, to, cc, bcc])

        @final
        class Csv(GreyCat.Object):
            name_: Final[str] = "io::Csv"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            @staticmethod
            def sample(reader: std.io.CsvReader, max_lines: int, __greycat: Optional[GreyCat] = None) -> std.core.Table:
                if __greycat is None:
                    __greycat  = GreyCat._DEFAULT
                return __greycat.call("io::Csv::sample", [reader, max_lines, ])

            @staticmethod
            def analyze(files: std.core.Array, config: std.io.CsvAnalysisConfig, __greycat: Optional[GreyCat] = None) -> std.io.CsvStatistics:
                if __greycat is None:
                    __greycat  = GreyCat._DEFAULT
                return __greycat.call("io::Csv::analyze", [files, config, ])

            @staticmethod
            def generate(stats: std.io.CsvStatistics, __greycat: Optional[GreyCat] = None) -> str:
                if __greycat is None:
                    __greycat  = GreyCat._DEFAULT
                return __greycat.call("io::Csv::generate", [stats, ])

            @staticmethod
            def create(greycat: GreyCat | None = None) -> std.io.Csv:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.io.Csv(greycat.libs_by_name[std.name_].mapped[86], [])

        @final
        class Json(Generic[__T], GreyCat.Object):
            name_: Final[str] = "io::Json"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            @staticmethod
            def create(greycat: GreyCat | None = None) -> std.io.Json[TypeVar("T")]:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.io.Json(greycat.libs_by_name[std.name_].mapped[87], [])

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
            def create(path: str, pos: int, greycat: GreyCat | None = None) -> std.io.TextReader:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.io.TextReader(greycat.libs_by_name[std.name_].mapped[88], [path, pos])

        @final
        class Http(GreyCat.Object):
            name_: Final[str] = "io::Http"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            @staticmethod
            def create(greycat: GreyCat | None = None) -> std.io.Http:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.io.Http(greycat.libs_by_name[std.name_].mapped[89], [])

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
            def create(header_lines: int, separator: c_char, string_delimiter: c_char, decimal_separator: c_char, thousands_separator: c_char, columns: std.core.Array, line_count: int, fail_count: int, file_count: int, greycat: GreyCat | None = None) -> std.io.CsvStatistics:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.io.CsvStatistics(greycat.libs_by_name[std.name_].mapped[90], [header_lines, separator, string_delimiter, decimal_separator, thousands_separator, columns, line_count, fail_count, file_count])

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
            def create(path: str, append: bool, greycat: GreyCat | None = None) -> std.io.Writer[TypeVar("T")]:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.io.Writer(greycat.libs_by_name[std.name_].mapped[91], [path, append])

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
            def create(id: int, column: int, modulo: int, greycat: GreyCat | None = None) -> std.io.CsvSharding:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.io.CsvSharding(greycat.libs_by_name[std.name_].mapped[92], [id, column, modulo])

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
            def create(path: str, pos: int, format: std.io.CsvFormat, sharding: std.io.CsvSharding, greycat: GreyCat | None = None) -> std.io.CsvReader[TypeVar("T")]:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.io.CsvReader(greycat.libs_by_name[std.name_].mapped[93], [path, pos, format, sharding])

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
            def enumerable_limit_default(greycat: GreyCat | None = None) -> int:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[94]
                return t.static_values[0]

            @staticmethod
            def date_check_limit_default(greycat: GreyCat | None = None) -> int:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[94]
                return t.static_values[1]

            @staticmethod
            def create(header_lines: int, separator: c_char, string_delimiter: c_char, decimal_separator: c_char, thousands_separator: c_char, row_limit: int, enumerable_limit: int, date_check_limit: int, date_formats: std.core.Array, greycat: GreyCat | None = None) -> std.io.CsvAnalysisConfig:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.io.CsvAnalysisConfig(greycat.libs_by_name[std.name_].mapped[94], [header_lines, separator, string_delimiter, decimal_separator, thousands_separator, row_limit, enumerable_limit, date_check_limit, date_formats])

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
            def create(path: str, size: int, last_modification: std.core.time, greycat: GreyCat | None = None) -> std.io.File:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.io.File(greycat.libs_by_name[std.name_].mapped[95], [path, size, last_modification])

    @final
    class util:
        __T = TypeVar("__T")

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
            def create(start: std.core.time, total: int, counter: int, duration: std.core.duration, progress: float, speed: float, remaining: std.core.duration, greycat: GreyCat | None = None) -> std.util.ProgressTracker:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.util.ProgressTracker(greycat.libs_by_name[std.name_].mapped[96], [start, total, counter, duration, progress, speed, remaining])

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
            def create(seed: int, v: float, greycat: GreyCat | None = None) -> std.util.Random:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.util.Random(greycat.libs_by_name[std.name_].mapped[97], [seed, v])

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
            def create(values: std.core.Array, span: int, sum: float, sumsq: float, field: std.core.field, greycat: GreyCat | None = None) -> std.util.SlidingWindow[TypeVar("T")]:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.util.SlidingWindow(greycat.libs_by_name[std.name_].mapped[98], [values, span, sum, sumsq, field])

        @final
        class Crypto(GreyCat.Object):
            name_: Final[str] = "util::Crypto"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            @staticmethod
            def create(greycat: GreyCat | None = None) -> std.util.Crypto:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.util.Crypto(greycat.libs_by_name[std.name_].mapped[99], [])

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
            def create(sum: int, sumsq: int, count: int, greycat: GreyCat | None = None) -> std.util.GaussianProfileSlot:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.util.GaussianProfileSlot(greycat.libs_by_name[std.name_].mapped[100], [sum, sumsq, count])

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
            def create(sum: float, sumsq: float, count: int, min: float, max: float, greycat: GreyCat | None = None) -> std.util.Gaussian:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.util.Gaussian(greycat.libs_by_name[std.name_].mapped[101], [sum, sumsq, count, min, max])

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
            def create(quantizers: std.core.Array, greycat: GreyCat | None = None) -> std.util.MultiQuantizer[TypeVar("T")]:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.util.MultiQuantizer(greycat.libs_by_name[std.name_].mapped[102], [quantizers])

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
            def create(min: std.util.__, max: std.util.__, bins: int, open: bool, greycat: GreyCat | None = None) -> std.util.LinearQuantizer[TypeVar("T")]:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.util.LinearQuantizer(greycat.libs_by_name[std.name_].mapped[103], [min, max, bins, open])

        @final
        class Quantizer(Generic[__T], GreyCat.Object):
            name_: Final[str] = "util::Quantizer"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            @staticmethod
            def create(greycat: GreyCat | None = None) -> std.util.Quantizer[TypeVar("T")]:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.util.Quantizer(greycat.libs_by_name[std.name_].mapped[104], [])

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
            def create(quantizer: std.util.Quantizer, bins: std.core.Array, nb_rejected: int, nb_accepted: int, greycat: GreyCat | None = None) -> std.util.Histogram[TypeVar("T")]:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.util.Histogram(greycat.libs_by_name[std.name_].mapped[105], [quantizer, bins, nb_rejected, nb_accepted])

        @final
        class Plot(GreyCat.Object):
            name_: Final[str] = "util::Plot"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            @staticmethod
            def create(greycat: GreyCat | None = None) -> std.util.Plot:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.util.Plot(greycat.libs_by_name[std.name_].mapped[106], [])

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
            def create(values: std.core.Array, greycat: GreyCat | None = None) -> std.util.Stack[TypeVar("T")]:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.util.Stack(greycat.libs_by_name[std.name_].mapped[107], [values])

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
            def create(min: float, max: float, whisker_low: float, whisker_high: float, percentile1: float, percentile5: float, percentile25: float, percentile50: float, percentile75: float, percentile95: float, percentile99: float, count_outliers_low: int, count_outliers_high: int, percentage_outliers_low: float, percentage_outliers_high: float, sum: float, avg: float, std: float, size: int, greycat: GreyCat | None = None) -> std.util.HistogramStats:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.util.HistogramStats(greycat.libs_by_name[std.name_].mapped[108], [min, max, whisker_low, whisker_high, percentile1, percentile5, percentile25, percentile50, percentile75, percentile95, percentile99, count_outliers_low, count_outliers_high, percentage_outliers_low, percentage_outliers_high, sum, avg, std, size])

        @final
        class Assert(GreyCat.Object):
            name_: Final[str] = "util::Assert"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            @staticmethod
            def create(greycat: GreyCat | None = None) -> std.util.Assert:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.util.Assert(greycat.libs_by_name[std.name_].mapped[109], [])

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
            def create(quantizer: std.util.Quantizer, precision: std.core.FloatPrecision, bins: std.core.Table, value_min: float, nb_rejected: int, greycat: GreyCat | None = None) -> std.util.GaussianProfile[TypeVar("T")]:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.util.GaussianProfile(greycat.libs_by_name[std.name_].mapped[110], [quantizer, precision, bins, value_min, nb_rejected])

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
            def create(values: std.core.Array, capacity: int, greycat: GreyCat | None = None) -> std.util.Queue[TypeVar("T")]:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.util.Queue(greycat.libs_by_name[std.name_].mapped[111], [values, capacity])

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
            def create(min: std.util.__, max: std.util.__, bins: int, open: bool, greycat: GreyCat | None = None) -> std.util.LogQuantizer[TypeVar("T")]:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.util.LogQuantizer(greycat.libs_by_name[std.name_].mapped[112], [min, max, bins, open])

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
            def create(min: std.util.__, max: std.util.__, step_starts: std.core.Array, open: bool, greycat: GreyCat | None = None) -> std.util.CustomQuantizer[TypeVar("T")]:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.util.CustomQuantizer(greycat.libs_by_name[std.name_].mapped[113], [min, max, step_starts, open])

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
            def create(values: std.core.Table, span: std.core.duration, sum: float, sumsq: float, field: std.core.field, greycat: GreyCat | None = None) -> std.util.TimeWindow[TypeVar("T")]:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.util.TimeWindow(greycat.libs_by_name[std.name_].mapped[114], [values, span, sum, sumsq, field])

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
            def create(min: std.util.__, max: std.util.__, center: std.util.__, greycat: GreyCat | None = None) -> std.util.QuantizerSlotBound[TypeVar("T")]:
                if greycat is None:
                    greycat = GreyCat._DEFAULT
                return std.util.QuantizerSlotBound(greycat.libs_by_name[std.name_].mapped[115], [min, max, center])

    def configure(self, loaders: dict[str, GreyCat.Loader], factories: dict[str, GreyCat.Factory]) -> None:
        factories[std.core.Date.name_] = lambda type, attributes: std.core.Date(type, attributes)
        factories[std.core.nodeTimeCursor.name_] = lambda type, attributes: std.core.nodeTimeCursor(type, attributes)
        factories[std.core.TimeZone.name_] = lambda type, attributes: std.core.TimeZone(type, attributes)
        factories[std.core.SortOrder.name_] = lambda type, attributes: std.core.SortOrder(type, attributes)
        factories[std.core.FloatPrecision.name_] = lambda type, attributes: std.core.FloatPrecision(type, attributes)
        factories[std.core.t3f.name_] = lambda type, attributes: std.core.t3f(type, attributes)
        loaders[std.core.t3f.name_] = lambda type, stream: std_n.core._t3f.load(type, stream)
        factories[std.core.Array.name_] = lambda type, attributes: std.core.Array(type, attributes)
        loaders[std.core.Array.name_] = lambda type, stream: std_n.core._Array.load(type, stream)
        factories[std.core.Tuple.name_] = lambda type, attributes: std.core.Tuple(type, attributes)
        factories[std.core.String.name_] = lambda type, attributes: std.core.String(type, attributes)
        loaders[std.core.String.name_] = lambda type, stream: std_n.core._String.load(type, stream)
        factories[std.core.Map.name_] = lambda type, attributes: std.core.Map(type, attributes)
        loaders[std.core.Map.name_] = lambda type, stream: std_n.core._Map.load(type, stream)
        factories[std.core.field.name_] = lambda type, attributes: std.core.field(type, attributes)
        loaders[std.core.field.name_] = lambda type, stream: std_n.core._field.load(type, stream)
        factories[std.core.t2.name_] = lambda type, attributes: std.core.t2(type, attributes)
        loaders[std.core.t2.name_] = lambda type, stream: std_n.core._t2.load(type, stream)
        factories[std.core.Tensor.name_] = lambda type, attributes: std.core.Tensor(type, attributes)
        loaders[std.core.Tensor.name_] = lambda type, stream: std_n.core._Tensor.load(type, stream)
        factories[std.core.NodeInfo.name_] = lambda type, attributes: std.core.NodeInfo(type, attributes)
        factories[std.core.t4f.name_] = lambda type, attributes: std.core.t4f(type, attributes)
        loaders[std.core.t4f.name_] = lambda type, stream: std_n.core._t4f.load(type, stream)
        factories[std.core.t2f.name_] = lambda type, attributes: std.core.t2f(type, attributes)
        loaders[std.core.t2f.name_] = lambda type, stream: std_n.core._t2f.load(type, stream)
        factories[std.core.type.name_] = lambda type, attributes: std.core.type(type, attributes)
        loaders[std.core.type.name_] = lambda type, stream: std_n.core._type.load(type, stream)
        factories[std.core.nodeIndex.name_] = lambda type, attributes: std.core.nodeIndex(type, attributes)
        loaders[std.core.nodeIndex.name_] = lambda type, stream: std_n.core._nodeIndex.load(type, stream)
        factories[std.core.Table.name_] = lambda type, attributes: std.core.Table(type, attributes)
        loaders[std.core.Table.name_] = lambda type, stream: std_n.core._Table.load(type, stream)
        factories[std.core.Buffer.name_] = lambda type, attributes: std.core.Buffer(type, attributes)
        loaders[std.core.Buffer.name_] = lambda type, stream: std_n.core._Buffer.load(type, stream)
        factories[std.core.GeoBox.name_] = lambda type, attributes: std.core.GeoBox(type, attributes)
        factories[std.core.DurationUnit.name_] = lambda type, attributes: std.core.DurationUnit(type, attributes)
        factories[std.core.nodeTimeSingleton.name_] = lambda type, attributes: std.core.nodeTimeSingleton(type, attributes)
        factories[std.core.nodeTime.name_] = lambda type, attributes: std.core.nodeTime(type, attributes)
        loaders[std.core.nodeTime.name_] = lambda type, stream: std_n.core._nodeTime.load(type, stream)
        factories[std.core.nodeList.name_] = lambda type, attributes: std.core.nodeList(type, attributes)
        loaders[std.core.nodeList.name_] = lambda type, stream: std_n.core._nodeList.load(type, stream)
        factories[std.core.GeoCircle.name_] = lambda type, attributes: std.core.GeoCircle(type, attributes)
        factories[std.core.GeoPoly.name_] = lambda type, attributes: std.core.GeoPoly(type, attributes)
        factories[std.core.Error.name_] = lambda type, attributes: std.core.Error(type, attributes)
        factories[std.core.ErrorFrame.name_] = lambda type, attributes: std.core.ErrorFrame(type, attributes)
        factories[std.core.duration.name_] = lambda type, attributes: std.core.duration(type, attributes)
        loaders[std.core.duration.name_] = lambda type, stream: std_n.core._duration.load(type, stream)
        factories[std.core.t3.name_] = lambda type, attributes: std.core.t3(type, attributes)
        loaders[std.core.t3.name_] = lambda type, stream: std_n.core._t3.load(type, stream)
        factories[std.core.geo.name_] = lambda type, attributes: std.core.geo(type, attributes)
        loaders[std.core.geo.name_] = lambda type, stream: std_n.core._geo.load(type, stream)
        factories[std.core.MathConstants.name_] = lambda type, attributes: std.core.MathConstants(type, attributes)
        factories[std.core.function.name_] = lambda type, attributes: std.core.function(type, attributes)
        loaders[std.core.function.name_] = lambda type, stream: std_n.core._function.load(type, stream)
        factories[std.core.TableColumnMapping.name_] = lambda type, attributes: std.core.TableColumnMapping(type, attributes)
        factories[std.core.time.name_] = lambda type, attributes: std.core.time(type, attributes)
        loaders[std.core.time.name_] = lambda type, stream: std_n.core._time.load(type, stream)
        factories[std.core.str.name_] = lambda type, attributes: std.core.str(type, attributes)
        loaders[std.core.str.name_] = lambda type, stream: std_n.core._str.load(type, stream)
        factories[std.core.t4.name_] = lambda type, attributes: std.core.t4(type, attributes)
        loaders[std.core.t4.name_] = lambda type, stream: std_n.core._t4.load(type, stream)
        factories[std.core.TensorType.name_] = lambda type, attributes: std.core.TensorType(type, attributes)
        factories[std.core.SamplingMode.name_] = lambda type, attributes: std.core.SamplingMode(type, attributes)
        factories[std.core.CalendarUnit.name_] = lambda type, attributes: std.core.CalendarUnit(type, attributes)
        factories[std.core.node.name_] = lambda type, attributes: std.core.node(type, attributes)
        loaders[std.core.node.name_] = lambda type, stream: std_n.core._node.load(type, stream)
        factories[std.core.nodeGeo.name_] = lambda type, attributes: std.core.nodeGeo(type, attributes)
        loaders[std.core.nodeGeo.name_] = lambda type, stream: std_n.core._nodeGeo.load(type, stream)
        factories[std.core.ErrorCode.name_] = lambda type, attributes: std.core.ErrorCode(type, attributes)
        factories[std.runtime.UserGroupPolicy.name_] = lambda type, attributes: std.runtime.UserGroupPolicy(type, attributes)
        factories[std.runtime.License.name_] = lambda type, attributes: std.runtime.License(type, attributes)
        factories[std.runtime.RuntimeInfo.name_] = lambda type, attributes: std.runtime.RuntimeInfo(type, attributes)
        factories[std.runtime.Debug.name_] = lambda type, attributes: std.runtime.Debug(type, attributes)
        factories[std.runtime.LogLevel.name_] = lambda type, attributes: std.runtime.LogLevel(type, attributes)
        factories[std.runtime.UserCredential.name_] = lambda type, attributes: std.runtime.UserCredential(type, attributes)
        factories[std.runtime.Task.name_] = lambda type, attributes: std.runtime.Task(type, attributes)
        factories[std.runtime.Runtime.name_] = lambda type, attributes: std.runtime.Runtime(type, attributes)
        factories[std.runtime.System.name_] = lambda type, attributes: std.runtime.System(type, attributes)
        factories[std.runtime.CallPerf.name_] = lambda type, attributes: std.runtime.CallPerf(type, attributes)
        factories[std.runtime.SecurityPolicy.name_] = lambda type, attributes: std.runtime.SecurityPolicy(type, attributes)
        factories[std.runtime.UserGroupPolicyType.name_] = lambda type, attributes: std.runtime.UserGroupPolicyType(type, attributes)
        factories[std.runtime.Log.name_] = lambda type, attributes: std.runtime.Log(type, attributes)
        factories[std.runtime.SecurityEntity.name_] = lambda type, attributes: std.runtime.SecurityEntity(type, attributes)
        factories[std.runtime.UserGroup.name_] = lambda type, attributes: std.runtime.UserGroup(type, attributes)
        factories[std.runtime.User.name_] = lambda type, attributes: std.runtime.User(type, attributes)
        factories[std.runtime.Job.name_] = lambda type, attributes: std.runtime.Job(type, attributes)
        factories[std.runtime.SecurityFields.name_] = lambda type, attributes: std.runtime.SecurityFields(type, attributes)
        factories[std.runtime.Permission.name_] = lambda type, attributes: std.runtime.Permission(type, attributes)
        factories[std.runtime.LicenseType.name_] = lambda type, attributes: std.runtime.LicenseType(type, attributes)
        factories[std.runtime.Variable.name_] = lambda type, attributes: std.runtime.Variable(type, attributes)
        factories[std.runtime.PeriodicTask.name_] = lambda type, attributes: std.runtime.PeriodicTask(type, attributes)
        factories[std.runtime.TaskStatus.name_] = lambda type, attributes: std.runtime.TaskStatus(type, attributes)
        factories[std.runtime.Role.name_] = lambda type, attributes: std.runtime.Role(type, attributes)
        factories[std.runtime.OpenIDConnect.name_] = lambda type, attributes: std.runtime.OpenIDConnect(type, attributes)
        factories[std.runtime.Frame.name_] = lambda type, attributes: std.runtime.Frame(type, attributes)
        factories[std.io.JsonReader.name_] = lambda type, attributes: std.io.JsonReader(type, attributes)
        factories[std.io.Url.name_] = lambda type, attributes: std.io.Url(type, attributes)
        factories[std.io.SmtpMode.name_] = lambda type, attributes: std.io.SmtpMode(type, attributes)
        factories[std.io.GcbWriter.name_] = lambda type, attributes: std.io.GcbWriter(type, attributes)
        factories[std.io.CsvFormat.name_] = lambda type, attributes: std.io.CsvFormat(type, attributes)
        factories[std.io.FileWalker.name_] = lambda type, attributes: std.io.FileWalker(type, attributes)
        factories[std.io.JsonWriter.name_] = lambda type, attributes: std.io.JsonWriter(type, attributes)
        factories[std.io.CsvWriter.name_] = lambda type, attributes: std.io.CsvWriter(type, attributes)
        factories[std.io.TextWriter.name_] = lambda type, attributes: std.io.TextWriter(type, attributes)
        factories[std.io.Reader.name_] = lambda type, attributes: std.io.Reader(type, attributes)
        factories[std.io.Smtp.name_] = lambda type, attributes: std.io.Smtp(type, attributes)
        factories[std.io.GcbReader.name_] = lambda type, attributes: std.io.GcbReader(type, attributes)
        factories[std.io.CsvColumnStatistics.name_] = lambda type, attributes: std.io.CsvColumnStatistics(type, attributes)
        factories[std.io.SmtpAuth.name_] = lambda type, attributes: std.io.SmtpAuth(type, attributes)
        factories[std.io.HttpHeader.name_] = lambda type, attributes: std.io.HttpHeader(type, attributes)
        factories[std.io.Email.name_] = lambda type, attributes: std.io.Email(type, attributes)
        factories[std.io.Csv.name_] = lambda type, attributes: std.io.Csv(type, attributes)
        factories[std.io.Json.name_] = lambda type, attributes: std.io.Json(type, attributes)
        factories[std.io.TextReader.name_] = lambda type, attributes: std.io.TextReader(type, attributes)
        factories[std.io.Http.name_] = lambda type, attributes: std.io.Http(type, attributes)
        factories[std.io.CsvStatistics.name_] = lambda type, attributes: std.io.CsvStatistics(type, attributes)
        factories[std.io.Writer.name_] = lambda type, attributes: std.io.Writer(type, attributes)
        factories[std.io.CsvSharding.name_] = lambda type, attributes: std.io.CsvSharding(type, attributes)
        factories[std.io.CsvReader.name_] = lambda type, attributes: std.io.CsvReader(type, attributes)
        factories[std.io.CsvAnalysisConfig.name_] = lambda type, attributes: std.io.CsvAnalysisConfig(type, attributes)
        factories[std.io.File.name_] = lambda type, attributes: std.io.File(type, attributes)
        factories[std.util.ProgressTracker.name_] = lambda type, attributes: std.util.ProgressTracker(type, attributes)
        factories[std.util.Random.name_] = lambda type, attributes: std.util.Random(type, attributes)
        factories[std.util.SlidingWindow.name_] = lambda type, attributes: std.util.SlidingWindow(type, attributes)
        factories[std.util.Crypto.name_] = lambda type, attributes: std.util.Crypto(type, attributes)
        factories[std.util.GaussianProfileSlot.name_] = lambda type, attributes: std.util.GaussianProfileSlot(type, attributes)
        factories[std.util.Gaussian.name_] = lambda type, attributes: std.util.Gaussian(type, attributes)
        factories[std.util.MultiQuantizer.name_] = lambda type, attributes: std.util.MultiQuantizer(type, attributes)
        factories[std.util.LinearQuantizer.name_] = lambda type, attributes: std.util.LinearQuantizer(type, attributes)
        factories[std.util.Quantizer.name_] = lambda type, attributes: std.util.Quantizer(type, attributes)
        factories[std.util.Histogram.name_] = lambda type, attributes: std.util.Histogram(type, attributes)
        factories[std.util.Plot.name_] = lambda type, attributes: std.util.Plot(type, attributes)
        factories[std.util.Stack.name_] = lambda type, attributes: std.util.Stack(type, attributes)
        factories[std.util.HistogramStats.name_] = lambda type, attributes: std.util.HistogramStats(type, attributes)
        factories[std.util.Assert.name_] = lambda type, attributes: std.util.Assert(type, attributes)
        factories[std.util.GaussianProfile.name_] = lambda type, attributes: std.util.GaussianProfile(type, attributes)
        factories[std.util.Queue.name_] = lambda type, attributes: std.util.Queue(type, attributes)
        factories[std.util.LogQuantizer.name_] = lambda type, attributes: std.util.LogQuantizer(type, attributes)
        factories[std.util.CustomQuantizer.name_] = lambda type, attributes: std.util.CustomQuantizer(type, attributes)
        factories[std.util.TimeWindow.name_] = lambda type, attributes: std.util.TimeWindow(type, attributes)
        factories[std.util.QuantizerSlotBound.name_] = lambda type, attributes: std.util.QuantizerSlotBound(type, attributes)

    def init(self, greycat: GreyCat) -> None:
        self.mapped: list[GreyCat.Type] = [
            greycat.types_by_name[std.core.Date.name_],
            greycat.types_by_name[std.core.nodeTimeCursor.name_],
            greycat.types_by_name[std.core.TimeZone.name_],
            greycat.types_by_name[std.core.SortOrder.name_],
            greycat.types_by_name[std.core.FloatPrecision.name_],
            greycat.types_by_name[std.core.t3f.name_],
            greycat.types_by_name[std.core.Array.name_],
            greycat.types_by_name[std.core.Tuple.name_],
            greycat.types_by_name[std.core.String.name_],
            greycat.types_by_name[std.core.Map.name_],
            greycat.types_by_name[std.core.field.name_],
            greycat.types_by_name[std.core.t2.name_],
            greycat.types_by_name[std.core.Tensor.name_],
            greycat.types_by_name[std.core.NodeInfo.name_],
            greycat.types_by_name[std.core.t4f.name_],
            greycat.types_by_name[std.core.t2f.name_],
            greycat.types_by_name[std.core.type.name_],
            greycat.types_by_name[std.core.nodeIndex.name_],
            greycat.types_by_name[std.core.Table.name_],
            greycat.types_by_name[std.core.Buffer.name_],
            greycat.types_by_name[std.core.GeoBox.name_],
            greycat.types_by_name[std.core.DurationUnit.name_],
            greycat.types_by_name[std.core.nodeTimeSingleton.name_],
            greycat.types_by_name[std.core.nodeTime.name_],
            greycat.types_by_name[std.core.nodeList.name_],
            greycat.types_by_name[std.core.GeoCircle.name_],
            greycat.types_by_name[std.core.GeoPoly.name_],
            greycat.types_by_name[std.core.Error.name_],
            greycat.types_by_name[std.core.ErrorFrame.name_],
            greycat.types_by_name[std.core.duration.name_],
            greycat.types_by_name[std.core.t3.name_],
            greycat.types_by_name[std.core.geo.name_],
            greycat.types_by_name[std.core.MathConstants.name_],
            greycat.types_by_name[std.core.function.name_],
            greycat.types_by_name[std.core.TableColumnMapping.name_],
            greycat.types_by_name[std.core.time.name_],
            greycat.types_by_name[std.core.str.name_],
            greycat.types_by_name[std.core.t4.name_],
            greycat.types_by_name[std.core.TensorType.name_],
            greycat.types_by_name[std.core.SamplingMode.name_],
            greycat.types_by_name[std.core.CalendarUnit.name_],
            greycat.types_by_name[std.core.node.name_],
            greycat.types_by_name[std.core.nodeGeo.name_],
            greycat.types_by_name[std.core.ErrorCode.name_],
            greycat.types_by_name[std.runtime.UserGroupPolicy.name_],
            greycat.types_by_name[std.runtime.License.name_],
            greycat.types_by_name[std.runtime.RuntimeInfo.name_],
            greycat.types_by_name[std.runtime.Debug.name_],
            greycat.types_by_name[std.runtime.LogLevel.name_],
            greycat.types_by_name[std.runtime.UserCredential.name_],
            greycat.types_by_name[std.runtime.Task.name_],
            greycat.types_by_name[std.runtime.Runtime.name_],
            greycat.types_by_name[std.runtime.System.name_],
            greycat.types_by_name[std.runtime.CallPerf.name_],
            greycat.types_by_name[std.runtime.SecurityPolicy.name_],
            greycat.types_by_name[std.runtime.UserGroupPolicyType.name_],
            greycat.types_by_name[std.runtime.Log.name_],
            greycat.types_by_name[std.runtime.SecurityEntity.name_],
            greycat.types_by_name[std.runtime.UserGroup.name_],
            greycat.types_by_name[std.runtime.User.name_],
            greycat.types_by_name[std.runtime.Job.name_],
            greycat.types_by_name[std.runtime.SecurityFields.name_],
            greycat.types_by_name[std.runtime.Permission.name_],
            greycat.types_by_name[std.runtime.LicenseType.name_],
            greycat.types_by_name[std.runtime.Variable.name_],
            greycat.types_by_name[std.runtime.PeriodicTask.name_],
            greycat.types_by_name[std.runtime.TaskStatus.name_],
            greycat.types_by_name[std.runtime.Role.name_],
            greycat.types_by_name[std.runtime.OpenIDConnect.name_],
            greycat.types_by_name[std.runtime.Frame.name_],
            greycat.types_by_name[std.io.JsonReader.name_],
            greycat.types_by_name[std.io.Url.name_],
            greycat.types_by_name[std.io.SmtpMode.name_],
            greycat.types_by_name[std.io.GcbWriter.name_],
            greycat.types_by_name[std.io.CsvFormat.name_],
            greycat.types_by_name[std.io.FileWalker.name_],
            greycat.types_by_name[std.io.JsonWriter.name_],
            greycat.types_by_name[std.io.CsvWriter.name_],
            greycat.types_by_name[std.io.TextWriter.name_],
            greycat.types_by_name[std.io.Reader.name_],
            greycat.types_by_name[std.io.Smtp.name_],
            greycat.types_by_name[std.io.GcbReader.name_],
            greycat.types_by_name[std.io.CsvColumnStatistics.name_],
            greycat.types_by_name[std.io.SmtpAuth.name_],
            greycat.types_by_name[std.io.HttpHeader.name_],
            greycat.types_by_name[std.io.Email.name_],
            greycat.types_by_name[std.io.Csv.name_],
            greycat.types_by_name[std.io.Json.name_],
            greycat.types_by_name[std.io.TextReader.name_],
            greycat.types_by_name[std.io.Http.name_],
            greycat.types_by_name[std.io.CsvStatistics.name_],
            greycat.types_by_name[std.io.Writer.name_],
            greycat.types_by_name[std.io.CsvSharding.name_],
            greycat.types_by_name[std.io.CsvReader.name_],
            greycat.types_by_name[std.io.CsvAnalysisConfig.name_],
            greycat.types_by_name[std.io.File.name_],
            greycat.types_by_name[std.util.ProgressTracker.name_],
            greycat.types_by_name[std.util.Random.name_],
            greycat.types_by_name[std.util.SlidingWindow.name_],
            greycat.types_by_name[std.util.Crypto.name_],
            greycat.types_by_name[std.util.GaussianProfileSlot.name_],
            greycat.types_by_name[std.util.Gaussian.name_],
            greycat.types_by_name[std.util.MultiQuantizer.name_],
            greycat.types_by_name[std.util.LinearQuantizer.name_],
            greycat.types_by_name[std.util.Quantizer.name_],
            greycat.types_by_name[std.util.Histogram.name_],
            greycat.types_by_name[std.util.Plot.name_],
            greycat.types_by_name[std.util.Stack.name_],
            greycat.types_by_name[std.util.HistogramStats.name_],
            greycat.types_by_name[std.util.Assert.name_],
            greycat.types_by_name[std.util.GaussianProfile.name_],
            greycat.types_by_name[std.util.Queue.name_],
            greycat.types_by_name[std.util.LogQuantizer.name_],
            greycat.types_by_name[std.util.CustomQuantizer.name_],
            greycat.types_by_name[std.util.TimeWindow.name_],
            greycat.types_by_name[std.util.QuantizerSlotBound.name_],
        ]
        self.mapped[0].resolve_generated_offsets("year", "month", "day", "hour", "minute", "second", "microsecond")
        self.mapped[1].resolve_generated_offsets("n", "req_time")
        self.mapped[2].resolve_generated_offset_with_values("UTC", None, "Africa/Abidjan", None, "Africa/Accra", None, "Africa/Addis_Ababa", None, "Africa/Algiers", None, "Africa/Asmara", None, "Africa/Asmera", None, "Africa/Bamako", None, "Africa/Bangui", None, "Africa/Banjul", None, "Africa/Bissau", None, "Africa/Blantyre", None, "Africa/Brazzaville", None, "Africa/Bujumbura", None, "Africa/Cairo", None, "Africa/Casablanca", None, "Africa/Ceuta", None, "Africa/Conakry", None, "Africa/Dakar", None, "Africa/Dar_es_Salaam", None, "Africa/Djibouti", None, "Africa/Douala", None, "Africa/El_Aaiun", None, "Africa/Freetown", None, "Africa/Gaborone", None, "Africa/Harare", None, "Africa/Johannesburg", None, "Africa/Juba", None, "Africa/Kampala", None, "Africa/Khartoum", None, "Africa/Kigali", None, "Africa/Kinshasa", None, "Africa/Lagos", None, "Africa/Libreville", None, "Africa/Lome", None, "Africa/Luanda", None, "Africa/Lubumbashi", None, "Africa/Lusaka", None, "Africa/Malabo", None, "Africa/Maputo", None, "Africa/Maseru", None, "Africa/Mbabane", None, "Africa/Mogadishu", None, "Africa/Monrovia", None, "Africa/Nairobi", None, "Africa/Ndjamena", None, "Africa/Niamey", None, "Africa/Nouakchott", None, "Africa/Ouagadougou", None, "Africa/Porto-Novo", None, "Africa/Sao_Tome", None, "Africa/Timbuktu", None, "Africa/Tripoli", None, "Africa/Tunis", None, "Africa/Windhoek", None, "America/Adak", None, "America/Anchorage", None, "America/Anguilla", None, "America/Antigua", None, "America/Araguaina", None, "America/Argentina/Buenos_Aires", None, "America/Argentina/Catamarca", None, "America/Argentina/ComodRivadavia", None, "America/Argentina/Cordoba", None, "America/Argentina/Jujuy", None, "America/Argentina/La_Rioja", None, "America/Argentina/Mendoza", None, "America/Argentina/Rio_Gallegos", None, "America/Argentina/Salta", None, "America/Argentina/San_Juan", None, "America/Argentina/San_Luis", None, "America/Argentina/Tucuman", None, "America/Argentina/Ushuaia", None, "America/Aruba", None, "America/Asuncion", None, "America/Atikokan", None, "America/Atka", None, "America/Bahia", None, "America/Bahia_Banderas", None, "America/Barbados", None, "America/Belem", None, "America/Belize", None, "America/Blanc-Sablon", None, "America/Boa_Vista", None, "America/Bogota", None, "America/Boise", None, "America/Buenos_Aires", None, "America/Cambridge_Bay", None, "America/Campo_Grande", None, "America/Cancun", None, "America/Caracas", None, "America/Catamarca", None, "America/Cayenne", None, "America/Cayman", None, "America/Chicago", None, "America/Chihuahua", None, "America/Ciudad_Juarez", None, "America/Coral_Harbour", None, "America/Cordoba", None, "America/Costa_Rica", None, "America/Coyhaique", None, "America/Creston", None, "America/Cuiaba", None, "America/Curacao", None, "America/Danmarkshavn", None, "America/Dawson", None, "America/Dawson_Creek", None, "America/Denver", None, "America/Detroit", None, "America/Dominica", None, "America/Edmonton", None, "America/Eirunepe", None, "America/El_Salvador", None, "America/Ensenada", None, "America/Fort_Nelson", None, "America/Fort_Wayne", None, "America/Fortaleza", None, "America/Glace_Bay", None, "America/Godthab", None, "America/Goose_Bay", None, "America/Grand_Turk", None, "America/Grenada", None, "America/Guadeloupe", None, "America/Guatemala", None, "America/Guayaquil", None, "America/Guyana", None, "America/Halifax", None, "America/Havana", None, "America/Hermosillo", None, "America/Indiana/Indianapolis", None, "America/Indiana/Knox", None, "America/Indiana/Marengo", None, "America/Indiana/Petersburg", None, "America/Indiana/Tell_City", None, "America/Indiana/Vevay", None, "America/Indiana/Vincennes", None, "America/Indiana/Winamac", None, "America/Indianapolis", None, "America/Inuvik", None, "America/Iqaluit", None, "America/Jamaica", None, "America/Jujuy", None, "America/Juneau", None, "America/Kentucky/Louisville", None, "America/Kentucky/Monticello", None, "America/Knox_IN", None, "America/Kralendijk", None, "America/La_Paz", None, "America/Lima", None, "America/Los_Angeles", None, "America/Louisville", None, "America/Lower_Princes", None, "America/Maceio", None, "America/Managua", None, "America/Manaus", None, "America/Marigot", None, "America/Martinique", None, "America/Matamoros", None, "America/Mazatlan", None, "America/Mendoza", None, "America/Menominee", None, "America/Merida", None, "America/Metlakatla", None, "America/Mexico_City", None, "America/Miquelon", None, "America/Moncton", None, "America/Monterrey", None, "America/Montevideo", None, "America/Montreal", None, "America/Montserrat", None, "America/Nassau", None, "America/New_York", None, "America/Nipigon", None, "America/Nome", None, "America/Noronha", None, "America/North_Dakota/Beulah", None, "America/North_Dakota/Center", None, "America/North_Dakota/New_Salem", None, "America/Nuuk", None, "America/Ojinaga", None, "America/Panama", None, "America/Pangnirtung", None, "America/Paramaribo", None, "America/Phoenix", None, "America/Port-au-Prince", None, "America/Port_of_Spain", None, "America/Porto_Acre", None, "America/Porto_Velho", None, "America/Puerto_Rico", None, "America/Punta_Arenas", None, "America/Rainy_River", None, "America/Rankin_Inlet", None, "America/Recife", None, "America/Regina", None, "America/Resolute", None, "America/Rio_Branco", None, "America/Rosario", None, "America/Santa_Isabel", None, "America/Santarem", None, "America/Santiago", None, "America/Santo_Domingo", None, "America/Sao_Paulo", None, "America/Scoresbysund", None, "America/Shiprock", None, "America/Sitka", None, "America/St_Barthelemy", None, "America/St_Johns", None, "America/St_Kitts", None, "America/St_Lucia", None, "America/St_Thomas", None, "America/St_Vincent", None, "America/Swift_Current", None, "America/Tegucigalpa", None, "America/Thule", None, "America/Thunder_Bay", None, "America/Tijuana", None, "America/Toronto", None, "America/Tortola", None, "America/Vancouver", None, "America/Virgin", None, "America/Whitehorse", None, "America/Winnipeg", None, "America/Yakutat", None, "America/Yellowknife", None, "Antarctica/Casey", None, "Antarctica/Davis", None, "Antarctica/DumontDUrville", None, "Antarctica/Macquarie", None, "Antarctica/Mawson", None, "Antarctica/McMurdo", None, "Antarctica/Palmer", None, "Antarctica/Rothera", None, "Antarctica/South_Pole", None, "Antarctica/Syowa", None, "Antarctica/Troll", None, "Antarctica/Vostok", None, "Arctic/Longyearbyen", None, "Asia/Aden", None, "Asia/Almaty", None, "Asia/Amman", None, "Asia/Anadyr", None, "Asia/Aqtau", None, "Asia/Aqtobe", None, "Asia/Ashgabat", None, "Asia/Ashkhabad", None, "Asia/Atyrau", None, "Asia/Baghdad", None, "Asia/Bahrain", None, "Asia/Baku", None, "Asia/Bangkok", None, "Asia/Barnaul", None, "Asia/Beirut", None, "Asia/Bishkek", None, "Asia/Brunei", None, "Asia/Calcutta", None, "Asia/Chita", None, "Asia/Choibalsan", None, "Asia/Chongqing", None, "Asia/Chungking", None, "Asia/Colombo", None, "Asia/Dacca", None, "Asia/Damascus", None, "Asia/Dhaka", None, "Asia/Dili", None, "Asia/Dubai", None, "Asia/Dushanbe", None, "Asia/Famagusta", None, "Asia/Gaza", None, "Asia/Harbin", None, "Asia/Hebron", None, "Asia/Ho_Chi_Minh", None, "Asia/Hong_Kong", None, "Asia/Hovd", None, "Asia/Irkutsk", None, "Asia/Istanbul", None, "Asia/Jakarta", None, "Asia/Jayapura", None, "Asia/Jerusalem", None, "Asia/Kabul", None, "Asia/Kamchatka", None, "Asia/Karachi", None, "Asia/Kashgar", None, "Asia/Kathmandu", None, "Asia/Katmandu", None, "Asia/Khandyga", None, "Asia/Kolkata", None, "Asia/Krasnoyarsk", None, "Asia/Kuala_Lumpur", None, "Asia/Kuching", None, "Asia/Kuwait", None, "Asia/Macao", None, "Asia/Macau", None, "Asia/Magadan", None, "Asia/Makassar", None, "Asia/Manila", None, "Asia/Muscat", None, "Asia/Nicosia", None, "Asia/Novokuznetsk", None, "Asia/Novosibirsk", None, "Asia/Omsk", None, "Asia/Oral", None, "Asia/Phnom_Penh", None, "Asia/Pontianak", None, "Asia/Pyongyang", None, "Asia/Qatar", None, "Asia/Qostanay", None, "Asia/Qyzylorda", None, "Asia/Rangoon", None, "Asia/Riyadh", None, "Asia/Saigon", None, "Asia/Sakhalin", None, "Asia/Samarkand", None, "Asia/Seoul", None, "Asia/Shanghai", None, "Asia/Singapore", None, "Asia/Srednekolymsk", None, "Asia/Taipei", None, "Asia/Tashkent", None, "Asia/Tbilisi", None, "Asia/Tehran", None, "Asia/Tel_Aviv", None, "Asia/Thimbu", None, "Asia/Thimphu", None, "Asia/Tokyo", None, "Asia/Tomsk", None, "Asia/Ujung_Pandang", None, "Asia/Ulaanbaatar", None, "Asia/Ulan_Bator", None, "Asia/Urumqi", None, "Asia/Ust-Nera", None, "Asia/Vientiane", None, "Asia/Vladivostok", None, "Asia/Yakutsk", None, "Asia/Yangon", None, "Asia/Yekaterinburg", None, "Asia/Yerevan", None, "Atlantic/Azores", None, "Atlantic/Bermuda", None, "Atlantic/Canary", None, "Atlantic/Cape_Verde", None, "Atlantic/Faeroe", None, "Atlantic/Faroe", None, "Atlantic/Jan_Mayen", None, "Atlantic/Madeira", None, "Atlantic/Reykjavik", None, "Atlantic/South_Georgia", None, "Atlantic/St_Helena", None, "Atlantic/Stanley", None, "Australia/ACT", None, "Australia/Adelaide", None, "Australia/Brisbane", None, "Australia/Broken_Hill", None, "Australia/Canberra", None, "Australia/Currie", None, "Australia/Darwin", None, "Australia/Eucla", None, "Australia/Hobart", None, "Australia/LHI", None, "Australia/Lindeman", None, "Australia/Lord_Howe", None, "Australia/Melbourne", None, "Australia/NSW", None, "Australia/North", None, "Australia/Perth", None, "Australia/Queensland", None, "Australia/South", None, "Australia/Sydney", None, "Australia/Tasmania", None, "Australia/Victoria", None, "Australia/West", None, "Australia/Yancowinna", None, "Brazil/Acre", None, "Brazil/DeNoronha", None, "Brazil/East", None, "Brazil/West", None, "CET", None, "CST6CDT", None, "Canada/Atlantic", None, "Canada/Central", None, "Canada/Eastern", None, "Canada/Mountain", None, "Canada/Newfoundland", None, "Canada/Pacific", None, "Canada/Saskatchewan", None, "Canada/Yukon", None, "Chile/Continental", None, "Chile/EasterIsland", None, "Cuba", None, "EET", None, "EST", None, "EST5EDT", None, "Egypt", None, "Eire", None, "Etc/GMT", None, "Etc/GMT+0", None, "Etc/GMT+1", None, "Etc/GMT+10", None, "Etc/GMT+11", None, "Etc/GMT+12", None, "Etc/GMT+2", None, "Etc/GMT+3", None, "Etc/GMT+4", None, "Etc/GMT+5", None, "Etc/GMT+6", None, "Etc/GMT+7", None, "Etc/GMT+8", None, "Etc/GMT+9", None, "Etc/GMT-0", None, "Etc/GMT-1", None, "Etc/GMT-10", None, "Etc/GMT-11", None, "Etc/GMT-12", None, "Etc/GMT-13", None, "Etc/GMT-14", None, "Etc/GMT-2", None, "Etc/GMT-3", None, "Etc/GMT-4", None, "Etc/GMT-5", None, "Etc/GMT-6", None, "Etc/GMT-7", None, "Etc/GMT-8", None, "Etc/GMT-9", None, "Etc/GMT0", None, "Etc/Greenwich", None, "Etc/UCT", None, "Etc/UTC", None, "Etc/Universal", None, "Etc/Zulu", None, "Europe/Amsterdam", None, "Europe/Andorra", None, "Europe/Astrakhan", None, "Europe/Athens", None, "Europe/Belfast", None, "Europe/Belgrade", None, "Europe/Berlin", None, "Europe/Bratislava", None, "Europe/Brussels", None, "Europe/Bucharest", None, "Europe/Budapest", None, "Europe/Busingen", None, "Europe/Chisinau", None, "Europe/Copenhagen", None, "Europe/Dublin", None, "Europe/Gibraltar", None, "Europe/Guernsey", None, "Europe/Helsinki", None, "Europe/Isle_of_Man", None, "Europe/Istanbul", None, "Europe/Jersey", None, "Europe/Kaliningrad", None, "Europe/Kiev", None, "Europe/Kirov", None, "Europe/Kyiv", None, "Europe/Lisbon", None, "Europe/Ljubljana", None, "Europe/London", None, "Europe/Luxembourg", None, "Europe/Madrid", None, "Europe/Malta", None, "Europe/Mariehamn", None, "Europe/Minsk", None, "Europe/Monaco", None, "Europe/Moscow", None, "Europe/Nicosia", None, "Europe/Oslo", None, "Europe/Paris", None, "Europe/Podgorica", None, "Europe/Prague", None, "Europe/Riga", None, "Europe/Rome", None, "Europe/Samara", None, "Europe/San_Marino", None, "Europe/Sarajevo", None, "Europe/Saratov", None, "Europe/Simferopol", None, "Europe/Skopje", None, "Europe/Sofia", None, "Europe/Stockholm", None, "Europe/Tallinn", None, "Europe/Tirane", None, "Europe/Tiraspol", None, "Europe/Ulyanovsk", None, "Europe/Uzhgorod", None, "Europe/Vaduz", None, "Europe/Vatican", None, "Europe/Vienna", None, "Europe/Vilnius", None, "Europe/Volgograd", None, "Europe/Warsaw", None, "Europe/Zagreb", None, "Europe/Zaporozhye", None, "Europe/Zurich", None, "Factory", None, "GB", None, "GB-Eire", None, "GMT", None, "GMT+0", None, "GMT-0", None, "GMT0", None, "Greenwich", None, "HST", None, "Hongkong", None, "Iceland", None, "Indian/Antananarivo", None, "Indian/Chagos", None, "Indian/Christmas", None, "Indian/Cocos", None, "Indian/Comoro", None, "Indian/Kerguelen", None, "Indian/Mahe", None, "Indian/Maldives", None, "Indian/Mauritius", None, "Indian/Mayotte", None, "Indian/Reunion", None, "Iran", None, "Israel", None, "Jamaica", None, "Japan", None, "Kwajalein", None, "Libya", None, "MET", None, "MST", None, "MST7MDT", None, "Mexico/BajaNorte", None, "Mexico/BajaSur", None, "Mexico/General", None, "NZ", None, "NZ-CHAT", None, "Navajo", None, "PRC", None, "PST8PDT", None, "Pacific/Apia", None, "Pacific/Auckland", None, "Pacific/Bougainville", None, "Pacific/Chatham", None, "Pacific/Chuuk", None, "Pacific/Easter", None, "Pacific/Efate", None, "Pacific/Enderbury", None, "Pacific/Fakaofo", None, "Pacific/Fiji", None, "Pacific/Funafuti", None, "Pacific/Galapagos", None, "Pacific/Gambier", None, "Pacific/Guadalcanal", None, "Pacific/Guam", None, "Pacific/Honolulu", None, "Pacific/Johnston", None, "Pacific/Kanton", None, "Pacific/Kiritimati", None, "Pacific/Kosrae", None, "Pacific/Kwajalein", None, "Pacific/Majuro", None, "Pacific/Marquesas", None, "Pacific/Midway", None, "Pacific/Nauru", None, "Pacific/Niue", None, "Pacific/Norfolk", None, "Pacific/Noumea", None, "Pacific/Pago_Pago", None, "Pacific/Palau", None, "Pacific/Pitcairn", None, "Pacific/Pohnpei", None, "Pacific/Ponape", None, "Pacific/Port_Moresby", None, "Pacific/Rarotonga", None, "Pacific/Saipan", None, "Pacific/Samoa", None, "Pacific/Tahiti", None, "Pacific/Tarawa", None, "Pacific/Tongatapu", None, "Pacific/Truk", None, "Pacific/Wake", None, "Pacific/Wallis", None, "Pacific/Yap", None, "Poland", None, "Portugal", None, "ROC", None, "ROK", None, "Singapore", None, "Turkey", None, "UCT", None, "US/Alaska", None, "US/Aleutian", None, "US/Arizona", None, "US/Central", None, "US/East-Indiana", None, "US/Eastern", None, "US/Hawaii", None, "US/Indiana-Starke", None, "US/Michigan", None, "US/Mountain", None, "US/Pacific", None, "US/Samoa", None, "Universal", None, "W-SU", None, "WET", None, "Zulu", None)
        self.mapped[3].resolve_generated_offset_with_values("asc", None, "desc", None)
        self.mapped[4].resolve_generated_offset_with_values("p1", float.fromhex("0x1p+0"), "p10", float.fromhex("0x1.999999999999ap-4"), "p100", float.fromhex("0x1.47ae147ae147bp-7"), "p1000", float.fromhex("0x1.0624dd2f1a9fcp-10"), "p10000", float.fromhex("0x1.a36e2eb1c432dp-14"), "p100000", float.fromhex("0x1.4f8b588e368f1p-17"), "p1000000", float.fromhex("0x1.0c6f7a0b5ed8dp-20"), "p10000000", float.fromhex("0x1.ad7f29abcaf48p-24"), "p100000000", float.fromhex("0x1.5798ee2308c3ap-27"), "p1000000000", float.fromhex("0x1.12e0be826d695p-30"), "p10000000000", float.fromhex("0x1.b7cdfd9d7bdbbp-34"))
        self.mapped[7].resolve_generated_offsets("x", "y")
        self.mapped[13].resolve_generated_offsets("size", "from", "to")
        self.mapped[20].resolve_generated_offsets("sw", "ne")
        self.mapped[21].resolve_generated_offset_with_values("microseconds", 1, "milliseconds", 1000, "seconds", 1000000, "minutes", 60000000, "hours", 3600000000, "days", 86400000000)
        self.mapped[22].resolve_generated_offsets("t", "v")
        self.mapped[25].resolve_generated_offsets("center", "radius")
        self.mapped[26].resolve_generated_offsets("points")
        self.mapped[27].resolve_generated_offsets("message", "stack")
        self.mapped[28].resolve_generated_offsets("module", "function", "line", "column")
        self.mapped[31].static_values = [greycat.create_geo(float.fromhex("-0x1.54345b1903bbap+6"), float.fromhex("-0x1.67fffffe98p+7")), greycat.create_geo(float.fromhex("0x1.54345b1903bbap+6"), float.fromhex("0x1.67fffffe98p+7"))]
        self.mapped[32].static_values = [float.fromhex("0x1.5bf0a8b145769p+1"), float.fromhex("0x1.71547652b82fep+0"), float.fromhex("0x1.bcb7b1526e50ep-2"), float.fromhex("0x1.62e42fefa39efp-1"), float.fromhex("0x1.26bb1bbb55516p+1"), float.fromhex("0x1.921fb54442d18p+1"), float.fromhex("0x1.921fb54442d18p+0"), float.fromhex("0x1.921fb54442d18p-1"), float.fromhex("0x1.45f306dc9c883p-2"), float.fromhex("0x1.45f306dc9c883p-1"), float.fromhex("0x1.20dd750429b6dp+0"), float.fromhex("0x1.6a09e667f3bcdp+0"), float.fromhex("0x1.6a09e667f3bcdp-1")]
        self.mapped[34].resolve_generated_offsets("column", "extractors")
        self.mapped[35].static_values = [greycat.create_time(-9223372036854775808), greycat.create_time(9223372036854775807)]
        self.mapped[38].resolve_generated_offset_with_values("i32", 4, "i64", 8, "f32", 4, "f64", 8, "c64", 8, "c128", 16)
        self.mapped[39].resolve_generated_offset_with_values("fixed", 0, "fixed_reg", 1, "adaptative", 2, "dense", 3)
        self.mapped[40].resolve_generated_offset_with_values("year", 0, "month", 1, "day", 2, "hour", 3, "minute", 4, "second", 5, "microsecond", 6)
        self.mapped[43].resolve_generated_offset_with_values("none", 0, "interrupted", 1, "await", 2, "timeout", 6, "forbidden", 7, "runtime_error", 8)
        self.mapped[44].resolve_generated_offsets("group_id", "type")
        self.mapped[45].resolve_generated_offsets("name", "start", "end", "company", "max_memory", "extra_1", "extra_2", "type")
        self.mapped[46].resolve_generated_offsets("version", "program_version", "arch", "timezone", "license", "io_threads", "bg_threads", "fg_threads", "mem_total", "mem_worker", "disk_data_bytes")
        self.mapped[47].resolve_generated_offsets("id", "frames", "root")
        self.mapped[48].resolve_generated_offset_with_values("error", None, "warn", None, "info", None, "perf", None, "trace", None)
        self.mapped[49].resolve_generated_offsets("offset", "pass")
        self.mapped[50].resolve_generated_offsets("user_id", "task_id", "mod", "type", "fun", "creation", "start", "duration", "status", "progress")
        self.mapped[53].resolve_generated_offsets("duration", "bytes_write_disk", "bytes_write_disk_raw", "bytes_read_disk", "bytes_read_disk_raw", "bytes_read_cache")
        self.mapped[54].resolve_generated_offsets("entities", "credentials", "fields", "keys", "keys_last_refresh")
        self.mapped[55].resolve_generated_offset_with_values("read", None, "write", None, "execute", None)
        self.mapped[56].resolve_generated_offsets("level", "time", "user_id", "id", "id2", "src", "tag", "data")
        self.mapped[57].resolve_generated_offsets("id", "name", "activated")
        self.mapped[58].resolve_generated_offsets("id", "name", "activated")
        self.mapped[59].resolve_generated_offsets("id", "name", "activated", "full_name", "email", "role", "groups", "groups_flags", "external")
        self.mapped[60].resolve_generated_offsets("function", "arguments")
        self.mapped[61].resolve_generated_offsets("email", "name", "first_name", "last_name", "roles", "groups")
        self.mapped[62].resolve_generated_offsets("name", "description")
        self.mapped[63].resolve_generated_offset_with_values("community", None, "enterprise", None, "testing", None)
        self.mapped[64].resolve_generated_offsets("name", "value")
        self.mapped[65].resolve_generated_offsets("function", "user_id", "arguments", "start", "every")
        self.mapped[66].resolve_generated_offset_with_values("empty", None, "waiting", None, "running", None, "await", None, "cancelled", None, "error", None, "ended", None, "ended_with_errors", None)
        self.mapped[67].resolve_generated_offsets("name", "permissions")
        self.mapped[68].resolve_generated_offsets("url", "clientId")
        self.mapped[69].resolve_generated_offsets("module", "type", "function", "src", "line", "column", "scope")
        self.mapped[70].resolve_generated_offsets("path", "pos")
        self.mapped[71].resolve_generated_offsets("protocol", "host", "port", "path", "params", "hash")
        self.mapped[72].resolve_generated_offset_with_values("plain", 0, "ssl_tls", 1, "starttls", 2)
        self.mapped[73].resolve_generated_offsets("path", "append")
        self.mapped[74].resolve_generated_offsets("header_lines", "separator", "string_delimiter", "decimal_separator", "thousands_separator", "trim", "format", "tz", "strict", "nearest_time")
        self.mapped[75].resolve_generated_offsets("path")
        self.mapped[76].resolve_generated_offsets("path", "append")
        self.mapped[77].resolve_generated_offsets("path", "append", "format")
        self.mapped[78].resolve_generated_offsets("path", "append")
        self.mapped[79].resolve_generated_offsets("path", "pos")
        self.mapped[80].resolve_generated_offsets("host", "port", "mode", "authenticate", "user", "pass")
        self.mapped[81].resolve_generated_offsets("path", "pos")
        self.mapped[82].resolve_generated_offsets("name", "example", "null_count", "bool_count", "int_count", "float_count", "string_count", "date_count", "date_format_count", "enumerable_count", "profile")
        self.mapped[83].resolve_generated_offset_with_values("none", 0, "plain", 1, "login", 2)
        self.mapped[84].resolve_generated_offsets("name", "value")
        self.mapped[85].resolve_generated_offsets("from", "subject", "body", "body_is_html", "to", "cc", "bcc")
        self.mapped[88].resolve_generated_offsets("path", "pos")
        self.mapped[90].resolve_generated_offsets("header_lines", "separator", "string_delimiter", "decimal_separator", "thousands_separator", "columns", "line_count", "fail_count", "file_count")
        self.mapped[91].resolve_generated_offsets("path", "append")
        self.mapped[92].resolve_generated_offsets("id", "column", "modulo")
        self.mapped[93].resolve_generated_offsets("path", "pos", "format", "sharding")
        self.mapped[94].resolve_generated_offsets("header_lines", "separator", "string_delimiter", "decimal_separator", "thousands_separator", "row_limit", "enumerable_limit", "date_check_limit", "date_formats")
        self.mapped[94].static_values = [100, 100]
        self.mapped[95].resolve_generated_offsets("path", "size", "last_modification")
        self.mapped[96].resolve_generated_offsets("start", "total", "counter", "duration", "progress", "speed", "remaining")
        self.mapped[97].resolve_generated_offsets("seed", "v")
        self.mapped[98].resolve_generated_offsets("values", "span", "sum", "sumsq", "field")
        self.mapped[100].resolve_generated_offsets("sum", "sumsq", "count")
        self.mapped[101].resolve_generated_offsets("sum", "sumsq", "count", "min", "max")
        self.mapped[102].resolve_generated_offsets("quantizers")
        self.mapped[103].resolve_generated_offsets("min", "max", "bins", "open")
        self.mapped[105].resolve_generated_offsets("quantizer", "bins", "nb_rejected", "nb_accepted")
        self.mapped[107].resolve_generated_offsets("values")
        self.mapped[108].resolve_generated_offsets("min", "max", "whisker_low", "whisker_high", "percentile1", "percentile5", "percentile25", "percentile50", "percentile75", "percentile95", "percentile99", "count_outliers_low", "count_outliers_high", "percentage_outliers_low", "percentage_outliers_high", "sum", "avg", "std", "size")
        self.mapped[110].resolve_generated_offsets("quantizer", "precision", "bins", "value_min", "nb_rejected")
        self.mapped[111].resolve_generated_offsets("values", "capacity")
        self.mapped[112].resolve_generated_offsets("min", "max", "bins", "open")
        self.mapped[113].resolve_generated_offsets("min", "max", "step_starts", "open")
        self.mapped[114].resolve_generated_offsets("values", "span", "sum", "sumsq", "field")
        self.mapped[115].resolve_generated_offsets("min", "max", "center")
