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

        def __init__(self, type: Optional[GreyCat.Type], *attributes):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[0]
            super().__init__(type, *attributes)

        def __class_getitem__(cls, key) -> core.ErrorCode:
            greycat: GreyCat
            if isinstance(key, tuple):
                key, greycat = key
            else:
                greycat = GreyCat._DEFAULT
            t: Final[GreyCat.Type] = greycat.libs_by_name[__std.name()].mapped[0]
            return t.enum_values[t.generated_offsets[core.ErrorCode.__indices_by_values[key]]]

    @final
    class t4(std_n.core._t4):
        name_: Final[str] = "core::t4"

        def __init__(self, type: Optional[GreyCat.Type], *_):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[1]
            super().__init__(type)

    @final
    class Table(Generic[__T], std_n.core._Table[__T]):
        name_: Final[str] = "core::Table"

        def __init__(self, type: Optional[GreyCat.Type], *_):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[2]
            super().__init__(type)

    @final
    class t3(std_n.core._t3):
        name_: Final[str] = "core::t3"

        def __init__(self, type: Optional[GreyCat.Type], *_):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[3]
            super().__init__(type)

    @final
    class nodeIndex(Generic[__K, __V], std_n.core._nodeIndex[__K, __V]):
        name_: Final[str] = "core::nodeIndex"

        def __init__(self, type: Optional[GreyCat.Type], *_):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[4]
            super().__init__(type)

    @final
    class GeoCircle(GreyCat.Object):
        name_: Final[str] = "core::GeoCircle"

        def __init__(self, type: Optional[GreyCat.Type], *attributes):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[5]
            super().__init__(type, *attributes)

        def center(self) -> core.GeoCircle:
            return self._get(self.type_.generated_offsets[0])

        def set_center(self, v: core.GeoCircle) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def radius(self) -> core.GeoCircle:
            return self._get(self.type_.generated_offsets[1])

        def set_radius(self, v: core.GeoCircle) -> None:
            self._set(self.type_.generated_offsets[1], v)

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

        def __init__(self, type: Optional[GreyCat.Type], *attributes):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[6]
            super().__init__(type, *attributes)

        def __class_getitem__(cls, key) -> core.TimeZone:
            greycat: GreyCat
            if isinstance(key, tuple):
                key, greycat = key
            else:
                greycat = GreyCat._DEFAULT
            t: Final[GreyCat.Type] = greycat.libs_by_name[__std.name()].mapped[6]
            return t.enum_values[t.generated_offsets[core.TimeZone.__indices_by_values[key]]]

    @final
    class t2(std_n.core._t2):
        name_: Final[str] = "core::t2"

        def __init__(self, type: Optional[GreyCat.Type], *_):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[7]
            super().__init__(type)

    @final
    class String(std_n.core._String):
        name_: Final[str] = "core::String"

        def __init__(self, type: Optional[GreyCat.Type], *_):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[8]
            super().__init__(type)

    @final
    class GeoBox(GreyCat.Object):
        name_: Final[str] = "core::GeoBox"

        def __init__(self, type: Optional[GreyCat.Type], *attributes):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[9]
            super().__init__(type, *attributes)

        def sw(self) -> core.GeoBox:
            return self._get(self.type_.generated_offsets[0])

        def set_sw(self, v: core.GeoBox) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def ne(self) -> core.GeoBox:
            return self._get(self.type_.generated_offsets[1])

        def set_ne(self, v: core.GeoBox) -> None:
            self._set(self.type_.generated_offsets[1], v)

    @final
    class t4f(std_n.core._t4f):
        name_: Final[str] = "core::t4f"

        def __init__(self, type: Optional[GreyCat.Type], *_):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[10]
            super().__init__(type)

    @final
    class field(std_n.core._field):
        name_: Final[str] = "core::field"

        def __init__(self, type: Optional[GreyCat.Type], *_):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[11]
            super().__init__(type)

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

        def __init__(self, type: Optional[GreyCat.Type], *attributes):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[12]
            super().__init__(type, *attributes)

        def __class_getitem__(cls, key) -> core.CalendarUnit:
            greycat: GreyCat
            if isinstance(key, tuple):
                key, greycat = key
            else:
                greycat = GreyCat._DEFAULT
            t: Final[GreyCat.Type] = greycat.libs_by_name[__std.name()].mapped[12]
            return t.enum_values[t.generated_offsets[core.CalendarUnit.__indices_by_values[key]]]

    @final
    class Buffer(std_n.core._Buffer):
        name_: Final[str] = "core::Buffer"

        def __init__(self, type: Optional[GreyCat.Type], *_):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[13]
            super().__init__(type)

    @final
    class nodeList(Generic[__T], std_n.core._nodeList[__T]):
        name_: Final[str] = "core::nodeList"

        def __init__(self, type: Optional[GreyCat.Type], *_):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[14]
            super().__init__(type)

    @final
    class nodeTime(Generic[__T], std_n.core._nodeTime[__T]):
        name_: Final[str] = "core::nodeTime"

        def __init__(self, type: Optional[GreyCat.Type], *_):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[15]
            super().__init__(type)

    @final
    class duration(std_n.core._duration):
        name_: Final[str] = "core::duration"

        def __init__(self, type: Optional[GreyCat.Type], *_):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[16]
            super().__init__(type)

    @final
    class Tensor(std_n.core._Tensor):
        name_: Final[str] = "core::Tensor"

        def __init__(self, type: Optional[GreyCat.Type], *_):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[17]
            super().__init__(type)

    @final
    class nodeTimeSingleton(GreyCat.Object):
        name_: Final[str] = "core::nodeTimeSingleton"

        def __init__(self, type: Optional[GreyCat.Type], *attributes):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[18]
            super().__init__(type, *attributes)

        def t(self) -> core.nodeTimeSingleton:
            return self._get(self.type_.generated_offsets[0])

        def set_t(self, v: core.nodeTimeSingleton) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def v(self) -> core.nodeTimeSingleton:
            return self._get(self.type_.generated_offsets[1])

        def set_v(self, v: core.nodeTimeSingleton) -> None:
            self._set(self.type_.generated_offsets[1], v)

    @final
    class NodeInfo(Generic[__T], GreyCat.Object):
        name_: Final[str] = "core::NodeInfo"

        def __init__(self, type: Optional[GreyCat.Type], *attributes):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[19]
            super().__init__(type, *attributes)

        def size(self) -> core.NodeInfo:
            return self._get(self.type_.generated_offsets[0])

        def set_size(self, v: core.NodeInfo) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def from_(self) -> core.NodeInfo:
            return self._get(self.type_.generated_offsets[1])

        def set_from_(self, v: core.NodeInfo) -> None:
            self._set(self.type_.generated_offsets[1], v)

        def to(self) -> core.NodeInfo:
            return self._get(self.type_.generated_offsets[2])

        def set_to(self, v: core.NodeInfo) -> None:
            self._set(self.type_.generated_offsets[2], v)

    @final
    class SortOrder(GreyCat.Enum):
        name_: Final[str] = "core::SortOrder"
        __indices_by_values: dict[str, int] = {
            "asc": 0,
            "desc": 1,
        }

        def __init__(self, type: Optional[GreyCat.Type], *attributes):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[20]
            super().__init__(type, *attributes)

        def __class_getitem__(cls, key) -> core.SortOrder:
            greycat: GreyCat
            if isinstance(key, tuple):
                key, greycat = key
            else:
                greycat = GreyCat._DEFAULT
            t: Final[GreyCat.Type] = greycat.libs_by_name[__std.name()].mapped[20]
            return t.enum_values[t.generated_offsets[core.SortOrder.__indices_by_values[key]]]

    @final
    class t3f(std_n.core._t3f):
        name_: Final[str] = "core::t3f"

        def __init__(self, type: Optional[GreyCat.Type], *_):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[21]
            super().__init__(type)

    @final
    class MathConstants(GreyCat.Object):
        name_: Final[str] = "core::MathConstants"

        def __init__(self, type: Optional[GreyCat.Type], *attributes):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[22]
            super().__init__(type, *attributes)

        @staticmethod
        def e(greycat: GreyCat | None = None) -> float:
            if greycat is None:
                greycat = GreyCat._DEFAULT
            t: Final[GreyCat.Type] = greycat.libs_by_name[__std.name_].mapped[22]
            return t.static_values[0]

        @staticmethod
        def log_2e(greycat: GreyCat | None = None) -> float:
            if greycat is None:
                greycat = GreyCat._DEFAULT
            t: Final[GreyCat.Type] = greycat.libs_by_name[__std.name_].mapped[22]
            return t.static_values[1]

        @staticmethod
        def log_10e(greycat: GreyCat | None = None) -> float:
            if greycat is None:
                greycat = GreyCat._DEFAULT
            t: Final[GreyCat.Type] = greycat.libs_by_name[__std.name_].mapped[22]
            return t.static_values[2]

        @staticmethod
        def ln2(greycat: GreyCat | None = None) -> float:
            if greycat is None:
                greycat = GreyCat._DEFAULT
            t: Final[GreyCat.Type] = greycat.libs_by_name[__std.name_].mapped[22]
            return t.static_values[3]

        @staticmethod
        def ln10(greycat: GreyCat | None = None) -> float:
            if greycat is None:
                greycat = GreyCat._DEFAULT
            t: Final[GreyCat.Type] = greycat.libs_by_name[__std.name_].mapped[22]
            return t.static_values[4]

        @staticmethod
        def pi(greycat: GreyCat | None = None) -> float:
            if greycat is None:
                greycat = GreyCat._DEFAULT
            t: Final[GreyCat.Type] = greycat.libs_by_name[__std.name_].mapped[22]
            return t.static_values[5]

        @staticmethod
        def pi_2(greycat: GreyCat | None = None) -> float:
            if greycat is None:
                greycat = GreyCat._DEFAULT
            t: Final[GreyCat.Type] = greycat.libs_by_name[__std.name_].mapped[22]
            return t.static_values[6]

        @staticmethod
        def pi_4(greycat: GreyCat | None = None) -> float:
            if greycat is None:
                greycat = GreyCat._DEFAULT
            t: Final[GreyCat.Type] = greycat.libs_by_name[__std.name_].mapped[22]
            return t.static_values[7]

        @staticmethod
        def m1_pi(greycat: GreyCat | None = None) -> float:
            if greycat is None:
                greycat = GreyCat._DEFAULT
            t: Final[GreyCat.Type] = greycat.libs_by_name[__std.name_].mapped[22]
            return t.static_values[8]

        @staticmethod
        def m2_pi(greycat: GreyCat | None = None) -> float:
            if greycat is None:
                greycat = GreyCat._DEFAULT
            t: Final[GreyCat.Type] = greycat.libs_by_name[__std.name_].mapped[22]
            return t.static_values[9]

        @staticmethod
        def m2_sqrt_pi(greycat: GreyCat | None = None) -> float:
            if greycat is None:
                greycat = GreyCat._DEFAULT
            t: Final[GreyCat.Type] = greycat.libs_by_name[__std.name_].mapped[22]
            return t.static_values[10]

        @staticmethod
        def sqrt2(greycat: GreyCat | None = None) -> float:
            if greycat is None:
                greycat = GreyCat._DEFAULT
            t: Final[GreyCat.Type] = greycat.libs_by_name[__std.name_].mapped[22]
            return t.static_values[11]

        @staticmethod
        def sqrt1_2(greycat: GreyCat | None = None) -> float:
            if greycat is None:
                greycat = GreyCat._DEFAULT
            t: Final[GreyCat.Type] = greycat.libs_by_name[__std.name_].mapped[22]
            return t.static_values[12]

    @final
    class type(std_n.core._type):
        name_: Final[str] = "core::type"

        def __init__(self, type: Optional[GreyCat.Type], *_):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[23]
            super().__init__(type)

    @final
    class SamplingMode(GreyCat.Enum):
        name_: Final[str] = "core::SamplingMode"
        __indices_by_values: dict[str, int] = {
            "fixed": 0,
            "fixed_reg": 1,
            "adaptative": 2,
            "dense": 3,
        }

        def __init__(self, type: Optional[GreyCat.Type], *attributes):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[24]
            super().__init__(type, *attributes)

        def __class_getitem__(cls, key) -> core.SamplingMode:
            greycat: GreyCat
            if isinstance(key, tuple):
                key, greycat = key
            else:
                greycat = GreyCat._DEFAULT
            t: Final[GreyCat.Type] = greycat.libs_by_name[__std.name()].mapped[24]
            return t.enum_values[t.generated_offsets[core.SamplingMode.__indices_by_values[key]]]

    @final
    class geo(std_n.core._geo):
        name_: Final[str] = "core::geo"

        def __init__(self, type: Optional[GreyCat.Type], *_):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[25]
            super().__init__(type)

    @final
    class Map(Generic[__K, __V], std_n.core._Map[__K, __V]):
        name_: Final[str] = "core::Map"

        def __init__(self, type: Optional[GreyCat.Type], *_):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[26]
            super().__init__(type)

    @final
    class Error(GreyCat.Object):
        name_: Final[str] = "core::Error"

        def __init__(self, type: Optional[GreyCat.Type], *attributes):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[27]
            super().__init__(type, *attributes)

        def message(self) -> core.Error:
            return self._get(self.type_.generated_offsets[0])

        def set_message(self, v: core.Error) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def stack(self) -> core.Error:
            return self._get(self.type_.generated_offsets[1])

        def set_stack(self, v: core.Error) -> None:
            self._set(self.type_.generated_offsets[1], v)

    @final
    class nodeTimeCursor(Generic[__T], GreyCat.Object):
        name_: Final[str] = "core::nodeTimeCursor"

        def __init__(self, type: Optional[GreyCat.Type], *attributes):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[28]
            super().__init__(type, *attributes)

        def n(self) -> core.nodeTimeCursor:
            return self._get(self.type_.generated_offsets[0])

        def set_n(self, v: core.nodeTimeCursor) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def req_time(self) -> core.nodeTimeCursor:
            return self._get(self.type_.generated_offsets[1])

        def set_req_time(self, v: core.nodeTimeCursor) -> None:
            self._set(self.type_.generated_offsets[1], v)

    @final
    class nodeGeo(Generic[__T], std_n.core._nodeGeo[__T]):
        name_: Final[str] = "core::nodeGeo"

        def __init__(self, type: Optional[GreyCat.Type], *_):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[29]
            super().__init__(type)

    @final
    class node(Generic[__T], std_n.core._node[__T]):
        name_: Final[str] = "core::node"

        def __init__(self, type: Optional[GreyCat.Type], *_):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[30]
            super().__init__(type)

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

        def __init__(self, type: Optional[GreyCat.Type], *attributes):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[31]
            super().__init__(type, *attributes)

        def __class_getitem__(cls, key) -> core.DurationUnit:
            greycat: GreyCat
            if isinstance(key, tuple):
                key, greycat = key
            else:
                greycat = GreyCat._DEFAULT
            t: Final[GreyCat.Type] = greycat.libs_by_name[__std.name()].mapped[31]
            return t.enum_values[t.generated_offsets[core.DurationUnit.__indices_by_values[key]]]

    @final
    class TableColumnMapping(GreyCat.Object):
        name_: Final[str] = "core::TableColumnMapping"

        def __init__(self, type: Optional[GreyCat.Type], *attributes):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[32]
            super().__init__(type, *attributes)

        def column(self) -> core.TableColumnMapping:
            return self._get(self.type_.generated_offsets[0])

        def set_column(self, v: core.TableColumnMapping) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def extractors(self) -> core.TableColumnMapping:
            return self._get(self.type_.generated_offsets[1])

        def set_extractors(self, v: core.TableColumnMapping) -> None:
            self._set(self.type_.generated_offsets[1], v)

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

        def __init__(self, type: Optional[GreyCat.Type], *attributes):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[33]
            super().__init__(type, *attributes)

        def __class_getitem__(cls, key) -> core.TensorType:
            greycat: GreyCat
            if isinstance(key, tuple):
                key, greycat = key
            else:
                greycat = GreyCat._DEFAULT
            t: Final[GreyCat.Type] = greycat.libs_by_name[__std.name()].mapped[33]
            return t.enum_values[t.generated_offsets[core.TensorType.__indices_by_values[key]]]

    @final
    class Tuple(Generic[__T, __U], GreyCat.Object):
        name_: Final[str] = "core::Tuple"

        def __init__(self, type: Optional[GreyCat.Type], *attributes):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[34]
            super().__init__(type, *attributes)

        def x(self) -> core.Tuple:
            return self._get(self.type_.generated_offsets[0])

        def set_x(self, v: core.Tuple) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def y(self) -> core.Tuple:
            return self._get(self.type_.generated_offsets[1])

        def set_y(self, v: core.Tuple) -> None:
            self._set(self.type_.generated_offsets[1], v)

    @final
    class time(std_n.core._time):
        name_: Final[str] = "core::time"

        def __init__(self, type: Optional[GreyCat.Type], *_):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[35]
            super().__init__(type)

    @final
    class ErrorFrame(GreyCat.Object):
        name_: Final[str] = "core::ErrorFrame"

        def __init__(self, type: Optional[GreyCat.Type], *attributes):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[36]
            super().__init__(type, *attributes)

        def module(self) -> core.ErrorFrame:
            return self._get(self.type_.generated_offsets[0])

        def set_module(self, v: core.ErrorFrame) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def function(self) -> core.ErrorFrame:
            return self._get(self.type_.generated_offsets[1])

        def set_function(self, v: core.ErrorFrame) -> None:
            self._set(self.type_.generated_offsets[1], v)

        def line(self) -> core.ErrorFrame:
            return self._get(self.type_.generated_offsets[2])

        def set_line(self, v: core.ErrorFrame) -> None:
            self._set(self.type_.generated_offsets[2], v)

        def column(self) -> core.ErrorFrame:
            return self._get(self.type_.generated_offsets[3])

        def set_column(self, v: core.ErrorFrame) -> None:
            self._set(self.type_.generated_offsets[3], v)

    @final
    class Array(Generic[__T], std_n.core._Array[__T]):
        name_: Final[str] = "core::Array"

        def __init__(self, type: Optional[GreyCat.Type], *_):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[37]
            super().__init__(type)

    @final
    class GeoPoly(GreyCat.Object):
        name_: Final[str] = "core::GeoPoly"

        def __init__(self, type: Optional[GreyCat.Type], *attributes):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[38]
            super().__init__(type, *attributes)

        def points(self) -> core.GeoPoly:
            return self._get(self.type_.generated_offsets[0])

        def set_points(self, v: core.GeoPoly) -> None:
            self._set(self.type_.generated_offsets[0], v)

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

        def __init__(self, type: Optional[GreyCat.Type], *attributes):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[39]
            super().__init__(type, *attributes)

        def __class_getitem__(cls, key) -> core.FloatPrecision:
            greycat: GreyCat
            if isinstance(key, tuple):
                key, greycat = key
            else:
                greycat = GreyCat._DEFAULT
            t: Final[GreyCat.Type] = greycat.libs_by_name[__std.name()].mapped[39]
            return t.enum_values[t.generated_offsets[core.FloatPrecision.__indices_by_values[key]]]

    @final
    class t2f(std_n.core._t2f):
        name_: Final[str] = "core::t2f"

        def __init__(self, type: Optional[GreyCat.Type], *_):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[40]
            super().__init__(type)

    @final
    class Date(GreyCat.Object):
        name_: Final[str] = "core::Date"

        def __init__(self, type: Optional[GreyCat.Type], *attributes):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[41]
            super().__init__(type, *attributes)

        def year(self) -> core.Date:
            return self._get(self.type_.generated_offsets[0])

        def set_year(self, v: core.Date) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def month(self) -> core.Date:
            return self._get(self.type_.generated_offsets[1])

        def set_month(self, v: core.Date) -> None:
            self._set(self.type_.generated_offsets[1], v)

        def day(self) -> core.Date:
            return self._get(self.type_.generated_offsets[2])

        def set_day(self, v: core.Date) -> None:
            self._set(self.type_.generated_offsets[2], v)

        def hour(self) -> core.Date:
            return self._get(self.type_.generated_offsets[3])

        def set_hour(self, v: core.Date) -> None:
            self._set(self.type_.generated_offsets[3], v)

        def minute(self) -> core.Date:
            return self._get(self.type_.generated_offsets[4])

        def set_minute(self, v: core.Date) -> None:
            self._set(self.type_.generated_offsets[4], v)

        def second(self) -> core.Date:
            return self._get(self.type_.generated_offsets[5])

        def set_second(self, v: core.Date) -> None:
            self._set(self.type_.generated_offsets[5], v)

        def microsecond(self) -> core.Date:
            return self._get(self.type_.generated_offsets[6])

        def set_microsecond(self, v: core.Date) -> None:
            self._set(self.type_.generated_offsets[6], v)

        @staticmethod
        def from_time(time: core.time, tz: core.TimeZone, __greycat: Optional[GreyCat] = None) -> core.Date:
            if __greycat is None:
                __greycat  = GreyCat._DEFAULT
            return __greycat.call("core::Date::from_time", [time, tz, ])

    @final
    class function(std_n.core._function):
        name_: Final[str] = "core::function"

        def __init__(self, type: Optional[GreyCat.Type], *_):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[42]
            super().__init__(type)

    @final
    class str(std_n.core._str):
        name_: Final[str] = "core::str"

        def __init__(self, type: Optional[GreyCat.Type], *_):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[43]
            super().__init__(type)


@final
class io:
    __T = TypeVar("__T")

    @final
    class SmtpAuth(GreyCat.Enum):
        name_: Final[str] = "io::SmtpAuth"
        __indices_by_values: dict[str, int] = {
            "none": 0,
            "plain": 1,
            "login": 2,
        }

        def __init__(self, type: Optional[GreyCat.Type], *attributes):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[44]
            super().__init__(type, *attributes)

        def __class_getitem__(cls, key) -> io.SmtpAuth:
            greycat: GreyCat
            if isinstance(key, tuple):
                key, greycat = key
            else:
                greycat = GreyCat._DEFAULT
            t: Final[GreyCat.Type] = greycat.libs_by_name[__std.name()].mapped[44]
            return t.enum_values[t.generated_offsets[io.SmtpAuth.__indices_by_values[key]]]

    @final
    class Url(GreyCat.Object):
        name_: Final[str] = "io::Url"

        def __init__(self, type: Optional[GreyCat.Type], *attributes):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[45]
            super().__init__(type, *attributes)

        def protocol(self) -> io.Url:
            return self._get(self.type_.generated_offsets[0])

        def set_protocol(self, v: io.Url) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def host(self) -> io.Url:
            return self._get(self.type_.generated_offsets[1])

        def set_host(self, v: io.Url) -> None:
            self._set(self.type_.generated_offsets[1], v)

        def port(self) -> io.Url:
            return self._get(self.type_.generated_offsets[2])

        def set_port(self, v: io.Url) -> None:
            self._set(self.type_.generated_offsets[2], v)

        def path(self) -> io.Url:
            return self._get(self.type_.generated_offsets[3])

        def set_path(self, v: io.Url) -> None:
            self._set(self.type_.generated_offsets[3], v)

        def params(self) -> io.Url:
            return self._get(self.type_.generated_offsets[4])

        def set_params(self, v: io.Url) -> None:
            self._set(self.type_.generated_offsets[4], v)

        def hash(self) -> io.Url:
            return self._get(self.type_.generated_offsets[5])

        def set_hash(self, v: io.Url) -> None:
            self._set(self.type_.generated_offsets[5], v)

    @final
    class File(GreyCat.Object):
        name_: Final[str] = "io::File"

        def __init__(self, type: Optional[GreyCat.Type], *attributes):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[46]
            super().__init__(type, *attributes)

        def path(self) -> io.File:
            return self._get(self.type_.generated_offsets[0])

        def set_path(self, v: io.File) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def size(self) -> io.File:
            return self._get(self.type_.generated_offsets[1])

        def set_size(self, v: io.File) -> None:
            self._set(self.type_.generated_offsets[1], v)

        def last_modification(self) -> io.File:
            return self._get(self.type_.generated_offsets[2])

        def set_last_modification(self, v: io.File) -> None:
            self._set(self.type_.generated_offsets[2], v)

    @final
    class CsvAnalysisConfig(GreyCat.Object):
        name_: Final[str] = "io::CsvAnalysisConfig"

        def __init__(self, type: Optional[GreyCat.Type], *attributes):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[47]
            super().__init__(type, *attributes)

        def header_lines(self) -> io.CsvAnalysisConfig:
            return self._get(self.type_.generated_offsets[0])

        def set_header_lines(self, v: io.CsvAnalysisConfig) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def separator(self) -> io.CsvAnalysisConfig:
            return self._get(self.type_.generated_offsets[1])

        def set_separator(self, v: io.CsvAnalysisConfig) -> None:
            self._set(self.type_.generated_offsets[1], v)

        def string_delimiter(self) -> io.CsvAnalysisConfig:
            return self._get(self.type_.generated_offsets[2])

        def set_string_delimiter(self, v: io.CsvAnalysisConfig) -> None:
            self._set(self.type_.generated_offsets[2], v)

        def decimal_separator(self) -> io.CsvAnalysisConfig:
            return self._get(self.type_.generated_offsets[3])

        def set_decimal_separator(self, v: io.CsvAnalysisConfig) -> None:
            self._set(self.type_.generated_offsets[3], v)

        def thousands_separator(self) -> io.CsvAnalysisConfig:
            return self._get(self.type_.generated_offsets[4])

        def set_thousands_separator(self, v: io.CsvAnalysisConfig) -> None:
            self._set(self.type_.generated_offsets[4], v)

        def row_limit(self) -> io.CsvAnalysisConfig:
            return self._get(self.type_.generated_offsets[5])

        def set_row_limit(self, v: io.CsvAnalysisConfig) -> None:
            self._set(self.type_.generated_offsets[5], v)

        def enumerable_limit(self) -> io.CsvAnalysisConfig:
            return self._get(self.type_.generated_offsets[6])

        def set_enumerable_limit(self, v: io.CsvAnalysisConfig) -> None:
            self._set(self.type_.generated_offsets[6], v)

        def date_check_limit(self) -> io.CsvAnalysisConfig:
            return self._get(self.type_.generated_offsets[7])

        def set_date_check_limit(self, v: io.CsvAnalysisConfig) -> None:
            self._set(self.type_.generated_offsets[7], v)

        def date_formats(self) -> io.CsvAnalysisConfig:
            return self._get(self.type_.generated_offsets[8])

        def set_date_formats(self, v: io.CsvAnalysisConfig) -> None:
            self._set(self.type_.generated_offsets[8], v)

        @staticmethod
        def enumerable_limit_default(greycat: GreyCat | None = None) -> int:
            if greycat is None:
                greycat = GreyCat._DEFAULT
            t: Final[GreyCat.Type] = greycat.libs_by_name[__std.name_].mapped[47]
            return t.static_values[0]

        @staticmethod
        def date_check_limit_default(greycat: GreyCat | None = None) -> int:
            if greycat is None:
                greycat = GreyCat._DEFAULT
            t: Final[GreyCat.Type] = greycat.libs_by_name[__std.name_].mapped[47]
            return t.static_values[1]

    @final
    class Writer(Generic[__T], GreyCat.Object):
        name_: Final[str] = "io::Writer"

        def __init__(self, type: Optional[GreyCat.Type], *attributes):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[48]
            super().__init__(type, *attributes)

        def path(self) -> io.Writer:
            return self._get(self.type_.generated_offsets[0])

        def set_path(self, v: io.Writer) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def append(self) -> io.Writer:
            return self._get(self.type_.generated_offsets[1])

        def set_append(self, v: io.Writer) -> None:
            self._set(self.type_.generated_offsets[1], v)

    @final
    class GcbWriter(Generic[__T], GreyCat.Object):
        name_: Final[str] = "io::GcbWriter"

        def __init__(self, type: Optional[GreyCat.Type], *attributes):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[49]
            super().__init__(type, *attributes)

        def path(self) -> io.GcbWriter:
            return self._get(self.type_.generated_offsets[0])

        def set_path(self, v: io.GcbWriter) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def append(self) -> io.GcbWriter:
            return self._get(self.type_.generated_offsets[1])

        def set_append(self, v: io.GcbWriter) -> None:
            self._set(self.type_.generated_offsets[1], v)

    @final
    class TextWriter(Generic[__T], GreyCat.Object):
        name_: Final[str] = "io::TextWriter"

        def __init__(self, type: Optional[GreyCat.Type], *attributes):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[50]
            super().__init__(type, *attributes)

        def path(self) -> io.TextWriter:
            return self._get(self.type_.generated_offsets[0])

        def set_path(self, v: io.TextWriter) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def append(self) -> io.TextWriter:
            return self._get(self.type_.generated_offsets[1])

        def set_append(self, v: io.TextWriter) -> None:
            self._set(self.type_.generated_offsets[1], v)

    @final
    class GcbReader(Generic[__T], GreyCat.Object):
        name_: Final[str] = "io::GcbReader"

        def __init__(self, type: Optional[GreyCat.Type], *attributes):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[51]
            super().__init__(type, *attributes)

        def path(self) -> io.GcbReader:
            return self._get(self.type_.generated_offsets[0])

        def set_path(self, v: io.GcbReader) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def pos(self) -> io.GcbReader:
            return self._get(self.type_.generated_offsets[1])

        def set_pos(self, v: io.GcbReader) -> None:
            self._set(self.type_.generated_offsets[1], v)

    @final
    class SmtpMode(GreyCat.Enum):
        name_: Final[str] = "io::SmtpMode"
        __indices_by_values: dict[str, int] = {
            "plain": 0,
            "ssl_tls": 1,
            "starttls": 2,
        }

        def __init__(self, type: Optional[GreyCat.Type], *attributes):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[52]
            super().__init__(type, *attributes)

        def __class_getitem__(cls, key) -> io.SmtpMode:
            greycat: GreyCat
            if isinstance(key, tuple):
                key, greycat = key
            else:
                greycat = GreyCat._DEFAULT
            t: Final[GreyCat.Type] = greycat.libs_by_name[__std.name()].mapped[52]
            return t.enum_values[t.generated_offsets[io.SmtpMode.__indices_by_values[key]]]

    @final
    class CsvColumnStatistics(GreyCat.Object):
        name_: Final[str] = "io::CsvColumnStatistics"

        def __init__(self, type: Optional[GreyCat.Type], *attributes):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[53]
            super().__init__(type, *attributes)

        def name(self) -> io.CsvColumnStatistics:
            return self._get(self.type_.generated_offsets[0])

        def set_name(self, v: io.CsvColumnStatistics) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def example(self) -> io.CsvColumnStatistics:
            return self._get(self.type_.generated_offsets[1])

        def set_example(self, v: io.CsvColumnStatistics) -> None:
            self._set(self.type_.generated_offsets[1], v)

        def null_count(self) -> io.CsvColumnStatistics:
            return self._get(self.type_.generated_offsets[2])

        def set_null_count(self, v: io.CsvColumnStatistics) -> None:
            self._set(self.type_.generated_offsets[2], v)

        def bool_count(self) -> io.CsvColumnStatistics:
            return self._get(self.type_.generated_offsets[3])

        def set_bool_count(self, v: io.CsvColumnStatistics) -> None:
            self._set(self.type_.generated_offsets[3], v)

        def int_count(self) -> io.CsvColumnStatistics:
            return self._get(self.type_.generated_offsets[4])

        def set_int_count(self, v: io.CsvColumnStatistics) -> None:
            self._set(self.type_.generated_offsets[4], v)

        def float_count(self) -> io.CsvColumnStatistics:
            return self._get(self.type_.generated_offsets[5])

        def set_float_count(self, v: io.CsvColumnStatistics) -> None:
            self._set(self.type_.generated_offsets[5], v)

        def string_count(self) -> io.CsvColumnStatistics:
            return self._get(self.type_.generated_offsets[6])

        def set_string_count(self, v: io.CsvColumnStatistics) -> None:
            self._set(self.type_.generated_offsets[6], v)

        def date_count(self) -> io.CsvColumnStatistics:
            return self._get(self.type_.generated_offsets[7])

        def set_date_count(self, v: io.CsvColumnStatistics) -> None:
            self._set(self.type_.generated_offsets[7], v)

        def date_format_count(self) -> io.CsvColumnStatistics:
            return self._get(self.type_.generated_offsets[8])

        def set_date_format_count(self, v: io.CsvColumnStatistics) -> None:
            self._set(self.type_.generated_offsets[8], v)

        def enumerable_count(self) -> io.CsvColumnStatistics:
            return self._get(self.type_.generated_offsets[9])

        def set_enumerable_count(self, v: io.CsvColumnStatistics) -> None:
            self._set(self.type_.generated_offsets[9], v)

        def profile(self) -> io.CsvColumnStatistics:
            return self._get(self.type_.generated_offsets[10])

        def set_profile(self, v: io.CsvColumnStatistics) -> None:
            self._set(self.type_.generated_offsets[10], v)

    @final
    class CsvFormat(GreyCat.Object):
        name_: Final[str] = "io::CsvFormat"

        def __init__(self, type: Optional[GreyCat.Type], *attributes):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[54]
            super().__init__(type, *attributes)

        def header_lines(self) -> io.CsvFormat:
            return self._get(self.type_.generated_offsets[0])

        def set_header_lines(self, v: io.CsvFormat) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def separator(self) -> io.CsvFormat:
            return self._get(self.type_.generated_offsets[1])

        def set_separator(self, v: io.CsvFormat) -> None:
            self._set(self.type_.generated_offsets[1], v)

        def string_delimiter(self) -> io.CsvFormat:
            return self._get(self.type_.generated_offsets[2])

        def set_string_delimiter(self, v: io.CsvFormat) -> None:
            self._set(self.type_.generated_offsets[2], v)

        def decimal_separator(self) -> io.CsvFormat:
            return self._get(self.type_.generated_offsets[3])

        def set_decimal_separator(self, v: io.CsvFormat) -> None:
            self._set(self.type_.generated_offsets[3], v)

        def thousands_separator(self) -> io.CsvFormat:
            return self._get(self.type_.generated_offsets[4])

        def set_thousands_separator(self, v: io.CsvFormat) -> None:
            self._set(self.type_.generated_offsets[4], v)

        def trim(self) -> io.CsvFormat:
            return self._get(self.type_.generated_offsets[5])

        def set_trim(self, v: io.CsvFormat) -> None:
            self._set(self.type_.generated_offsets[5], v)

        def format(self) -> io.CsvFormat:
            return self._get(self.type_.generated_offsets[6])

        def set_format(self, v: io.CsvFormat) -> None:
            self._set(self.type_.generated_offsets[6], v)

        def tz(self) -> io.CsvFormat:
            return self._get(self.type_.generated_offsets[7])

        def set_tz(self, v: io.CsvFormat) -> None:
            self._set(self.type_.generated_offsets[7], v)

        def strict(self) -> io.CsvFormat:
            return self._get(self.type_.generated_offsets[8])

        def set_strict(self, v: io.CsvFormat) -> None:
            self._set(self.type_.generated_offsets[8], v)

        def nearest_time(self) -> io.CsvFormat:
            return self._get(self.type_.generated_offsets[9])

        def set_nearest_time(self, v: io.CsvFormat) -> None:
            self._set(self.type_.generated_offsets[9], v)

    @final
    class CsvSharding(GreyCat.Object):
        name_: Final[str] = "io::CsvSharding"

        def __init__(self, type: Optional[GreyCat.Type], *attributes):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[55]
            super().__init__(type, *attributes)

        def id(self) -> io.CsvSharding:
            return self._get(self.type_.generated_offsets[0])

        def set_id(self, v: io.CsvSharding) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def column(self) -> io.CsvSharding:
            return self._get(self.type_.generated_offsets[1])

        def set_column(self, v: io.CsvSharding) -> None:
            self._set(self.type_.generated_offsets[1], v)

        def modulo(self) -> io.CsvSharding:
            return self._get(self.type_.generated_offsets[2])

        def set_modulo(self, v: io.CsvSharding) -> None:
            self._set(self.type_.generated_offsets[2], v)

    @final
    class Email(GreyCat.Object):
        name_: Final[str] = "io::Email"

        def __init__(self, type: Optional[GreyCat.Type], *attributes):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[56]
            super().__init__(type, *attributes)

        def from_(self) -> io.Email:
            return self._get(self.type_.generated_offsets[0])

        def set_from_(self, v: io.Email) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def subject(self) -> io.Email:
            return self._get(self.type_.generated_offsets[1])

        def set_subject(self, v: io.Email) -> None:
            self._set(self.type_.generated_offsets[1], v)

        def body(self) -> io.Email:
            return self._get(self.type_.generated_offsets[2])

        def set_body(self, v: io.Email) -> None:
            self._set(self.type_.generated_offsets[2], v)

        def body_is_html(self) -> io.Email:
            return self._get(self.type_.generated_offsets[3])

        def set_body_is_html(self, v: io.Email) -> None:
            self._set(self.type_.generated_offsets[3], v)

        def to(self) -> io.Email:
            return self._get(self.type_.generated_offsets[4])

        def set_to(self, v: io.Email) -> None:
            self._set(self.type_.generated_offsets[4], v)

        def cc(self) -> io.Email:
            return self._get(self.type_.generated_offsets[5])

        def set_cc(self, v: io.Email) -> None:
            self._set(self.type_.generated_offsets[5], v)

        def bcc(self) -> io.Email:
            return self._get(self.type_.generated_offsets[6])

        def set_bcc(self, v: io.Email) -> None:
            self._set(self.type_.generated_offsets[6], v)

    @final
    class CsvReader(Generic[__T], GreyCat.Object):
        name_: Final[str] = "io::CsvReader"

        def __init__(self, type: Optional[GreyCat.Type], *attributes):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[57]
            super().__init__(type, *attributes)

        def path(self) -> io.CsvReader:
            return self._get(self.type_.generated_offsets[0])

        def set_path(self, v: io.CsvReader) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def pos(self) -> io.CsvReader:
            return self._get(self.type_.generated_offsets[1])

        def set_pos(self, v: io.CsvReader) -> None:
            self._set(self.type_.generated_offsets[1], v)

        def format(self) -> io.CsvReader:
            return self._get(self.type_.generated_offsets[2])

        def set_format(self, v: io.CsvReader) -> None:
            self._set(self.type_.generated_offsets[2], v)

        def sharding(self) -> io.CsvReader:
            return self._get(self.type_.generated_offsets[3])

        def set_sharding(self, v: io.CsvReader) -> None:
            self._set(self.type_.generated_offsets[3], v)

    @final
    class Reader(Generic[__T], GreyCat.Object):
        name_: Final[str] = "io::Reader"

        def __init__(self, type: Optional[GreyCat.Type], *attributes):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[58]
            super().__init__(type, *attributes)

        def path(self) -> io.Reader:
            return self._get(self.type_.generated_offsets[0])

        def set_path(self, v: io.Reader) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def pos(self) -> io.Reader:
            return self._get(self.type_.generated_offsets[1])

        def set_pos(self, v: io.Reader) -> None:
            self._set(self.type_.generated_offsets[1], v)

    @final
    class Http(GreyCat.Object):
        name_: Final[str] = "io::Http"

        def __init__(self, type: Optional[GreyCat.Type], *attributes):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[59]
            super().__init__(type, *attributes)

    @final
    class CsvWriter(Generic[__T], GreyCat.Object):
        name_: Final[str] = "io::CsvWriter"

        def __init__(self, type: Optional[GreyCat.Type], *attributes):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[60]
            super().__init__(type, *attributes)

        def path(self) -> io.CsvWriter:
            return self._get(self.type_.generated_offsets[0])

        def set_path(self, v: io.CsvWriter) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def append(self) -> io.CsvWriter:
            return self._get(self.type_.generated_offsets[1])

        def set_append(self, v: io.CsvWriter) -> None:
            self._set(self.type_.generated_offsets[1], v)

        def format(self) -> io.CsvWriter:
            return self._get(self.type_.generated_offsets[2])

        def set_format(self, v: io.CsvWriter) -> None:
            self._set(self.type_.generated_offsets[2], v)

    @final
    class TextReader(GreyCat.Object):
        name_: Final[str] = "io::TextReader"

        def __init__(self, type: Optional[GreyCat.Type], *attributes):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[61]
            super().__init__(type, *attributes)

        def path(self) -> io.TextReader:
            return self._get(self.type_.generated_offsets[0])

        def set_path(self, v: io.TextReader) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def pos(self) -> io.TextReader:
            return self._get(self.type_.generated_offsets[1])

        def set_pos(self, v: io.TextReader) -> None:
            self._set(self.type_.generated_offsets[1], v)

    @final
    class CsvStatistics(GreyCat.Object):
        name_: Final[str] = "io::CsvStatistics"

        def __init__(self, type: Optional[GreyCat.Type], *attributes):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[62]
            super().__init__(type, *attributes)

        def header_lines(self) -> io.CsvStatistics:
            return self._get(self.type_.generated_offsets[0])

        def set_header_lines(self, v: io.CsvStatistics) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def separator(self) -> io.CsvStatistics:
            return self._get(self.type_.generated_offsets[1])

        def set_separator(self, v: io.CsvStatistics) -> None:
            self._set(self.type_.generated_offsets[1], v)

        def string_delimiter(self) -> io.CsvStatistics:
            return self._get(self.type_.generated_offsets[2])

        def set_string_delimiter(self, v: io.CsvStatistics) -> None:
            self._set(self.type_.generated_offsets[2], v)

        def decimal_separator(self) -> io.CsvStatistics:
            return self._get(self.type_.generated_offsets[3])

        def set_decimal_separator(self, v: io.CsvStatistics) -> None:
            self._set(self.type_.generated_offsets[3], v)

        def thousands_separator(self) -> io.CsvStatistics:
            return self._get(self.type_.generated_offsets[4])

        def set_thousands_separator(self, v: io.CsvStatistics) -> None:
            self._set(self.type_.generated_offsets[4], v)

        def columns(self) -> io.CsvStatistics:
            return self._get(self.type_.generated_offsets[5])

        def set_columns(self, v: io.CsvStatistics) -> None:
            self._set(self.type_.generated_offsets[5], v)

        def line_count(self) -> io.CsvStatistics:
            return self._get(self.type_.generated_offsets[6])

        def set_line_count(self, v: io.CsvStatistics) -> None:
            self._set(self.type_.generated_offsets[6], v)

        def fail_count(self) -> io.CsvStatistics:
            return self._get(self.type_.generated_offsets[7])

        def set_fail_count(self, v: io.CsvStatistics) -> None:
            self._set(self.type_.generated_offsets[7], v)

        def file_count(self) -> io.CsvStatistics:
            return self._get(self.type_.generated_offsets[8])

        def set_file_count(self, v: io.CsvStatistics) -> None:
            self._set(self.type_.generated_offsets[8], v)

    @final
    class JsonWriter(Generic[__T], GreyCat.Object):
        name_: Final[str] = "io::JsonWriter"

        def __init__(self, type: Optional[GreyCat.Type], *attributes):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[63]
            super().__init__(type, *attributes)

        def path(self) -> io.JsonWriter:
            return self._get(self.type_.generated_offsets[0])

        def set_path(self, v: io.JsonWriter) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def append(self) -> io.JsonWriter:
            return self._get(self.type_.generated_offsets[1])

        def set_append(self, v: io.JsonWriter) -> None:
            self._set(self.type_.generated_offsets[1], v)

    @final
    class JsonReader(Generic[__T], GreyCat.Object):
        name_: Final[str] = "io::JsonReader"

        def __init__(self, type: Optional[GreyCat.Type], *attributes):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[64]
            super().__init__(type, *attributes)

        def path(self) -> io.JsonReader:
            return self._get(self.type_.generated_offsets[0])

        def set_path(self, v: io.JsonReader) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def pos(self) -> io.JsonReader:
            return self._get(self.type_.generated_offsets[1])

        def set_pos(self, v: io.JsonReader) -> None:
            self._set(self.type_.generated_offsets[1], v)

    @final
    class Json(Generic[__T], GreyCat.Object):
        name_: Final[str] = "io::Json"

        def __init__(self, type: Optional[GreyCat.Type], *attributes):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[65]
            super().__init__(type, *attributes)

    @final
    class Csv(GreyCat.Object):
        name_: Final[str] = "io::Csv"

        def __init__(self, type: Optional[GreyCat.Type], *attributes):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[66]
            super().__init__(type, *attributes)

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
    class Smtp(GreyCat.Object):
        name_: Final[str] = "io::Smtp"

        def __init__(self, type: Optional[GreyCat.Type], *attributes):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[67]
            super().__init__(type, *attributes)

        def host(self) -> io.Smtp:
            return self._get(self.type_.generated_offsets[0])

        def set_host(self, v: io.Smtp) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def port(self) -> io.Smtp:
            return self._get(self.type_.generated_offsets[1])

        def set_port(self, v: io.Smtp) -> None:
            self._set(self.type_.generated_offsets[1], v)

        def mode(self) -> io.Smtp:
            return self._get(self.type_.generated_offsets[2])

        def set_mode(self, v: io.Smtp) -> None:
            self._set(self.type_.generated_offsets[2], v)

        def authenticate(self) -> io.Smtp:
            return self._get(self.type_.generated_offsets[3])

        def set_authenticate(self, v: io.Smtp) -> None:
            self._set(self.type_.generated_offsets[3], v)

        def user(self) -> io.Smtp:
            return self._get(self.type_.generated_offsets[4])

        def set_user(self, v: io.Smtp) -> None:
            self._set(self.type_.generated_offsets[4], v)

        def pass_(self) -> io.Smtp:
            return self._get(self.type_.generated_offsets[5])

        def set_pass_(self, v: io.Smtp) -> None:
            self._set(self.type_.generated_offsets[5], v)

    @final
    class FileWalker(GreyCat.Object):
        name_: Final[str] = "io::FileWalker"

        def __init__(self, type: Optional[GreyCat.Type], *attributes):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[68]
            super().__init__(type, *attributes)

        def path(self) -> io.FileWalker:
            return self._get(self.type_.generated_offsets[0])

        def set_path(self, v: io.FileWalker) -> None:
            self._set(self.type_.generated_offsets[0], v)

    @final
    class HttpHeader(GreyCat.Object):
        name_: Final[str] = "io::HttpHeader"

        def __init__(self, type: Optional[GreyCat.Type], *attributes):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[69]
            super().__init__(type, *attributes)

        def name(self) -> io.HttpHeader:
            return self._get(self.type_.generated_offsets[0])

        def set_name(self, v: io.HttpHeader) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def value(self) -> io.HttpHeader:
            return self._get(self.type_.generated_offsets[1])

        def set_value(self, v: io.HttpHeader) -> None:
            self._set(self.type_.generated_offsets[1], v)


@final
class runtime:
    __T = TypeVar("__T")

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

        def __init__(self, type: Optional[GreyCat.Type], *attributes):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[70]
            super().__init__(type, *attributes)

        def __class_getitem__(cls, key) -> runtime.LogLevel:
            greycat: GreyCat
            if isinstance(key, tuple):
                key, greycat = key
            else:
                greycat = GreyCat._DEFAULT
            t: Final[GreyCat.Type] = greycat.libs_by_name[__std.name()].mapped[70]
            return t.enum_values[t.generated_offsets[runtime.LogLevel.__indices_by_values[key]]]

    @final
    class RuntimeInfo(GreyCat.Object):
        name_: Final[str] = "runtime::RuntimeInfo"

        def __init__(self, type: Optional[GreyCat.Type], *attributes):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[71]
            super().__init__(type, *attributes)

        def version(self) -> runtime.RuntimeInfo:
            return self._get(self.type_.generated_offsets[0])

        def set_version(self, v: runtime.RuntimeInfo) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def program_version(self) -> runtime.RuntimeInfo:
            return self._get(self.type_.generated_offsets[1])

        def set_program_version(self, v: runtime.RuntimeInfo) -> None:
            self._set(self.type_.generated_offsets[1], v)

        def arch(self) -> runtime.RuntimeInfo:
            return self._get(self.type_.generated_offsets[2])

        def set_arch(self, v: runtime.RuntimeInfo) -> None:
            self._set(self.type_.generated_offsets[2], v)

        def timezone(self) -> runtime.RuntimeInfo:
            return self._get(self.type_.generated_offsets[3])

        def set_timezone(self, v: runtime.RuntimeInfo) -> None:
            self._set(self.type_.generated_offsets[3], v)

        def license(self) -> runtime.RuntimeInfo:
            return self._get(self.type_.generated_offsets[4])

        def set_license(self, v: runtime.RuntimeInfo) -> None:
            self._set(self.type_.generated_offsets[4], v)

        def io_threads(self) -> runtime.RuntimeInfo:
            return self._get(self.type_.generated_offsets[5])

        def set_io_threads(self, v: runtime.RuntimeInfo) -> None:
            self._set(self.type_.generated_offsets[5], v)

        def bg_threads(self) -> runtime.RuntimeInfo:
            return self._get(self.type_.generated_offsets[6])

        def set_bg_threads(self, v: runtime.RuntimeInfo) -> None:
            self._set(self.type_.generated_offsets[6], v)

        def fg_threads(self) -> runtime.RuntimeInfo:
            return self._get(self.type_.generated_offsets[7])

        def set_fg_threads(self, v: runtime.RuntimeInfo) -> None:
            self._set(self.type_.generated_offsets[7], v)

        def mem_total(self) -> runtime.RuntimeInfo:
            return self._get(self.type_.generated_offsets[8])

        def set_mem_total(self, v: runtime.RuntimeInfo) -> None:
            self._set(self.type_.generated_offsets[8], v)

        def mem_worker(self) -> runtime.RuntimeInfo:
            return self._get(self.type_.generated_offsets[9])

        def set_mem_worker(self, v: runtime.RuntimeInfo) -> None:
            self._set(self.type_.generated_offsets[9], v)

        def disk_data_bytes(self) -> runtime.RuntimeInfo:
            return self._get(self.type_.generated_offsets[10])

        def set_disk_data_bytes(self, v: runtime.RuntimeInfo) -> None:
            self._set(self.type_.generated_offsets[10], v)

    @final
    class SecurityEntity(GreyCat.Object):
        name_: Final[str] = "runtime::SecurityEntity"

        def __init__(self, type: Optional[GreyCat.Type], *attributes):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[72]
            super().__init__(type, *attributes)

        def id(self) -> runtime.SecurityEntity:
            return self._get(self.type_.generated_offsets[0])

        def set_id(self, v: runtime.SecurityEntity) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def name(self) -> runtime.SecurityEntity:
            return self._get(self.type_.generated_offsets[1])

        def set_name(self, v: runtime.SecurityEntity) -> None:
            self._set(self.type_.generated_offsets[1], v)

        def activated(self) -> runtime.SecurityEntity:
            return self._get(self.type_.generated_offsets[2])

        def set_activated(self, v: runtime.SecurityEntity) -> None:
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
    class Debug(GreyCat.Object):
        name_: Final[str] = "runtime::Debug"

        def __init__(self, type: Optional[GreyCat.Type], *attributes):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[73]
            super().__init__(type, *attributes)

        def id(self) -> runtime.Debug:
            return self._get(self.type_.generated_offsets[0])

        def set_id(self, v: runtime.Debug) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def frames(self) -> runtime.Debug:
            return self._get(self.type_.generated_offsets[1])

        def set_frames(self, v: runtime.Debug) -> None:
            self._set(self.type_.generated_offsets[1], v)

        def root(self) -> runtime.Debug:
            return self._get(self.type_.generated_offsets[2])

        def set_root(self, v: runtime.Debug) -> None:
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
    class Role(GreyCat.Object):
        name_: Final[str] = "runtime::Role"

        def __init__(self, type: Optional[GreyCat.Type], *attributes):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[74]
            super().__init__(type, *attributes)

        def name(self) -> runtime.Role:
            return self._get(self.type_.generated_offsets[0])

        def set_name(self, v: runtime.Role) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def permissions(self) -> runtime.Role:
            return self._get(self.type_.generated_offsets[1])

        def set_permissions(self, v: runtime.Role) -> None:
            self._set(self.type_.generated_offsets[1], v)

        @staticmethod
        def all(__greycat: Optional[GreyCat] = None) -> core.Array:
            if __greycat is None:
                __greycat  = GreyCat._DEFAULT
            return __greycat.call("runtime::Role::all")

    @final
    class Log(GreyCat.Object):
        name_: Final[str] = "runtime::Log"

        def __init__(self, type: Optional[GreyCat.Type], *attributes):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[75]
            super().__init__(type, *attributes)

        def level(self) -> runtime.Log:
            return self._get(self.type_.generated_offsets[0])

        def set_level(self, v: runtime.Log) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def time(self) -> runtime.Log:
            return self._get(self.type_.generated_offsets[1])

        def set_time(self, v: runtime.Log) -> None:
            self._set(self.type_.generated_offsets[1], v)

        def user_id(self) -> runtime.Log:
            return self._get(self.type_.generated_offsets[2])

        def set_user_id(self, v: runtime.Log) -> None:
            self._set(self.type_.generated_offsets[2], v)

        def id(self) -> runtime.Log:
            return self._get(self.type_.generated_offsets[3])

        def set_id(self, v: runtime.Log) -> None:
            self._set(self.type_.generated_offsets[3], v)

        def id2(self) -> runtime.Log:
            return self._get(self.type_.generated_offsets[4])

        def set_id2(self, v: runtime.Log) -> None:
            self._set(self.type_.generated_offsets[4], v)

        def src(self) -> runtime.Log:
            return self._get(self.type_.generated_offsets[5])

        def set_src(self, v: runtime.Log) -> None:
            self._set(self.type_.generated_offsets[5], v)

        def tag(self) -> runtime.Log:
            return self._get(self.type_.generated_offsets[6])

        def set_tag(self, v: runtime.Log) -> None:
            self._set(self.type_.generated_offsets[6], v)

        def data(self) -> runtime.Log:
            return self._get(self.type_.generated_offsets[7])

        def set_data(self, v: runtime.Log) -> None:
            self._set(self.type_.generated_offsets[7], v)

    @final
    class Variable(GreyCat.Object):
        name_: Final[str] = "runtime::Variable"

        def __init__(self, type: Optional[GreyCat.Type], *attributes):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[76]
            super().__init__(type, *attributes)

        def name(self) -> runtime.Variable:
            return self._get(self.type_.generated_offsets[0])

        def set_name(self, v: runtime.Variable) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def value(self) -> runtime.Variable:
            return self._get(self.type_.generated_offsets[1])

        def set_value(self, v: runtime.Variable) -> None:
            self._set(self.type_.generated_offsets[1], v)

    @final
    class OpenIDConnect(GreyCat.Object):
        name_: Final[str] = "runtime::OpenIDConnect"

        def __init__(self, type: Optional[GreyCat.Type], *attributes):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[77]
            super().__init__(type, *attributes)

        def url(self) -> runtime.OpenIDConnect:
            return self._get(self.type_.generated_offsets[0])

        def set_url(self, v: runtime.OpenIDConnect) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def clientId(self) -> runtime.OpenIDConnect:
            return self._get(self.type_.generated_offsets[1])

        def set_clientId(self, v: runtime.OpenIDConnect) -> None:
            self._set(self.type_.generated_offsets[1], v)

        @staticmethod
        def config(__greycat: Optional[GreyCat] = None) -> runtime.OpenIDConnect:
            if __greycat is None:
                __greycat  = GreyCat._DEFAULT
            return __greycat.call("runtime::OpenIDConnect::config")

    @final
    class License(GreyCat.Object):
        name_: Final[str] = "runtime::License"

        def __init__(self, type: Optional[GreyCat.Type], *attributes):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[78]
            super().__init__(type, *attributes)

        def name(self) -> runtime.License:
            return self._get(self.type_.generated_offsets[0])

        def set_name(self, v: runtime.License) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def start(self) -> runtime.License:
            return self._get(self.type_.generated_offsets[1])

        def set_start(self, v: runtime.License) -> None:
            self._set(self.type_.generated_offsets[1], v)

        def end(self) -> runtime.License:
            return self._get(self.type_.generated_offsets[2])

        def set_end(self, v: runtime.License) -> None:
            self._set(self.type_.generated_offsets[2], v)

        def company(self) -> runtime.License:
            return self._get(self.type_.generated_offsets[3])

        def set_company(self, v: runtime.License) -> None:
            self._set(self.type_.generated_offsets[3], v)

        def max_memory(self) -> runtime.License:
            return self._get(self.type_.generated_offsets[4])

        def set_max_memory(self, v: runtime.License) -> None:
            self._set(self.type_.generated_offsets[4], v)

        def extra_1(self) -> runtime.License:
            return self._get(self.type_.generated_offsets[5])

        def set_extra_1(self, v: runtime.License) -> None:
            self._set(self.type_.generated_offsets[5], v)

        def extra_2(self) -> runtime.License:
            return self._get(self.type_.generated_offsets[6])

        def set_extra_2(self, v: runtime.License) -> None:
            self._set(self.type_.generated_offsets[6], v)

        def type(self) -> runtime.License:
            return self._get(self.type_.generated_offsets[7])

        def set_type(self, v: runtime.License) -> None:
            self._set(self.type_.generated_offsets[7], v)

    @final
    class UserGroupPolicy(GreyCat.Object):
        name_: Final[str] = "runtime::UserGroupPolicy"

        def __init__(self, type: Optional[GreyCat.Type], *attributes):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[79]
            super().__init__(type, *attributes)

        def group_id(self) -> runtime.UserGroupPolicy:
            return self._get(self.type_.generated_offsets[0])

        def set_group_id(self, v: runtime.UserGroupPolicy) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def type(self) -> runtime.UserGroupPolicy:
            return self._get(self.type_.generated_offsets[1])

        def set_type(self, v: runtime.UserGroupPolicy) -> None:
            self._set(self.type_.generated_offsets[1], v)

    @final
    class User(GreyCat.Object):
        name_: Final[str] = "runtime::User"

        def __init__(self, type: Optional[GreyCat.Type], *attributes):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[80]
            super().__init__(type, *attributes)

        def id(self) -> runtime.User:
            return self._get(self.type_.generated_offsets[0])

        def set_id(self, v: runtime.User) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def name(self) -> runtime.User:
            return self._get(self.type_.generated_offsets[1])

        def set_name(self, v: runtime.User) -> None:
            self._set(self.type_.generated_offsets[1], v)

        def activated(self) -> runtime.User:
            return self._get(self.type_.generated_offsets[2])

        def set_activated(self, v: runtime.User) -> None:
            self._set(self.type_.generated_offsets[2], v)

        def full_name(self) -> runtime.User:
            return self._get(self.type_.generated_offsets[3])

        def set_full_name(self, v: runtime.User) -> None:
            self._set(self.type_.generated_offsets[3], v)

        def email(self) -> runtime.User:
            return self._get(self.type_.generated_offsets[4])

        def set_email(self, v: runtime.User) -> None:
            self._set(self.type_.generated_offsets[4], v)

        def role(self) -> runtime.User:
            return self._get(self.type_.generated_offsets[5])

        def set_role(self, v: runtime.User) -> None:
            self._set(self.type_.generated_offsets[5], v)

        def groups(self) -> runtime.User:
            return self._get(self.type_.generated_offsets[6])

        def set_groups(self, v: runtime.User) -> None:
            self._set(self.type_.generated_offsets[6], v)

        def groups_flags(self) -> runtime.User:
            return self._get(self.type_.generated_offsets[7])

        def set_groups_flags(self, v: runtime.User) -> None:
            self._set(self.type_.generated_offsets[7], v)

        def external(self) -> runtime.User:
            return self._get(self.type_.generated_offsets[8])

        def set_external(self, v: runtime.User) -> None:
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
    class Job(Generic[__T], GreyCat.Object):
        name_: Final[str] = "runtime::Job"

        def __init__(self, type: Optional[GreyCat.Type], *attributes):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[81]
            super().__init__(type, *attributes)

        def function(self) -> runtime.Job:
            return self._get(self.type_.generated_offsets[0])

        def set_function(self, v: runtime.Job) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def arguments(self) -> runtime.Job:
            return self._get(self.type_.generated_offsets[1])

        def set_arguments(self, v: runtime.Job) -> None:
            self._set(self.type_.generated_offsets[1], v)

    @final
    class SecurityFields(GreyCat.Object):
        name_: Final[str] = "runtime::SecurityFields"

        def __init__(self, type: Optional[GreyCat.Type], *attributes):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[82]
            super().__init__(type, *attributes)

        def email(self) -> runtime.SecurityFields:
            return self._get(self.type_.generated_offsets[0])

        def set_email(self, v: runtime.SecurityFields) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def name(self) -> runtime.SecurityFields:
            return self._get(self.type_.generated_offsets[1])

        def set_name(self, v: runtime.SecurityFields) -> None:
            self._set(self.type_.generated_offsets[1], v)

        def first_name(self) -> runtime.SecurityFields:
            return self._get(self.type_.generated_offsets[2])

        def set_first_name(self, v: runtime.SecurityFields) -> None:
            self._set(self.type_.generated_offsets[2], v)

        def last_name(self) -> runtime.SecurityFields:
            return self._get(self.type_.generated_offsets[3])

        def set_last_name(self, v: runtime.SecurityFields) -> None:
            self._set(self.type_.generated_offsets[3], v)

        def roles(self) -> runtime.SecurityFields:
            return self._get(self.type_.generated_offsets[4])

        def set_roles(self, v: runtime.SecurityFields) -> None:
            self._set(self.type_.generated_offsets[4], v)

        def groups(self) -> runtime.SecurityFields:
            return self._get(self.type_.generated_offsets[5])

        def set_groups(self, v: runtime.SecurityFields) -> None:
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

        def __init__(self, type: Optional[GreyCat.Type], *attributes):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[83]
            super().__init__(type, *attributes)

        def __class_getitem__(cls, key) -> runtime.TaskStatus:
            greycat: GreyCat
            if isinstance(key, tuple):
                key, greycat = key
            else:
                greycat = GreyCat._DEFAULT
            t: Final[GreyCat.Type] = greycat.libs_by_name[__std.name()].mapped[83]
            return t.enum_values[t.generated_offsets[runtime.TaskStatus.__indices_by_values[key]]]

    @final
    class LicenseType(GreyCat.Enum):
        name_: Final[str] = "runtime::LicenseType"
        __indices_by_values: dict[str, int] = {
            "community": 0,
            "enterprise": 1,
            "testing": 2,
        }

        def __init__(self, type: Optional[GreyCat.Type], *attributes):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[84]
            super().__init__(type, *attributes)

        def __class_getitem__(cls, key) -> runtime.LicenseType:
            greycat: GreyCat
            if isinstance(key, tuple):
                key, greycat = key
            else:
                greycat = GreyCat._DEFAULT
            t: Final[GreyCat.Type] = greycat.libs_by_name[__std.name()].mapped[84]
            return t.enum_values[t.generated_offsets[runtime.LicenseType.__indices_by_values[key]]]

    @final
    class Frame(GreyCat.Object):
        name_: Final[str] = "runtime::Frame"

        def __init__(self, type: Optional[GreyCat.Type], *attributes):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[85]
            super().__init__(type, *attributes)

        def module(self) -> runtime.Frame:
            return self._get(self.type_.generated_offsets[0])

        def set_module(self, v: runtime.Frame) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def type(self) -> runtime.Frame:
            return self._get(self.type_.generated_offsets[1])

        def set_type(self, v: runtime.Frame) -> None:
            self._set(self.type_.generated_offsets[1], v)

        def function(self) -> runtime.Frame:
            return self._get(self.type_.generated_offsets[2])

        def set_function(self, v: runtime.Frame) -> None:
            self._set(self.type_.generated_offsets[2], v)

        def src(self) -> runtime.Frame:
            return self._get(self.type_.generated_offsets[3])

        def set_src(self, v: runtime.Frame) -> None:
            self._set(self.type_.generated_offsets[3], v)

        def line(self) -> runtime.Frame:
            return self._get(self.type_.generated_offsets[4])

        def set_line(self, v: runtime.Frame) -> None:
            self._set(self.type_.generated_offsets[4], v)

        def column(self) -> runtime.Frame:
            return self._get(self.type_.generated_offsets[5])

        def set_column(self, v: runtime.Frame) -> None:
            self._set(self.type_.generated_offsets[5], v)

        def scope(self) -> runtime.Frame:
            return self._get(self.type_.generated_offsets[6])

        def set_scope(self, v: runtime.Frame) -> None:
            self._set(self.type_.generated_offsets[6], v)

    @final
    class UserGroup(GreyCat.Object):
        name_: Final[str] = "runtime::UserGroup"

        def __init__(self, type: Optional[GreyCat.Type], *attributes):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[86]
            super().__init__(type, *attributes)

        def id(self) -> runtime.UserGroup:
            return self._get(self.type_.generated_offsets[0])

        def set_id(self, v: runtime.UserGroup) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def name(self) -> runtime.UserGroup:
            return self._get(self.type_.generated_offsets[1])

        def set_name(self, v: runtime.UserGroup) -> None:
            self._set(self.type_.generated_offsets[1], v)

        def activated(self) -> runtime.UserGroup:
            return self._get(self.type_.generated_offsets[2])

        def set_activated(self, v: runtime.UserGroup) -> None:
            self._set(self.type_.generated_offsets[2], v)

    @final
    class CallPerf(GreyCat.Object):
        name_: Final[str] = "runtime::CallPerf"

        def __init__(self, type: Optional[GreyCat.Type], *attributes):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[87]
            super().__init__(type, *attributes)

        def duration(self) -> runtime.CallPerf:
            return self._get(self.type_.generated_offsets[0])

        def set_duration(self, v: runtime.CallPerf) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def bytes_write_disk(self) -> runtime.CallPerf:
            return self._get(self.type_.generated_offsets[1])

        def set_bytes_write_disk(self, v: runtime.CallPerf) -> None:
            self._set(self.type_.generated_offsets[1], v)

        def bytes_write_disk_raw(self) -> runtime.CallPerf:
            return self._get(self.type_.generated_offsets[2])

        def set_bytes_write_disk_raw(self, v: runtime.CallPerf) -> None:
            self._set(self.type_.generated_offsets[2], v)

        def bytes_read_disk(self) -> runtime.CallPerf:
            return self._get(self.type_.generated_offsets[3])

        def set_bytes_read_disk(self, v: runtime.CallPerf) -> None:
            self._set(self.type_.generated_offsets[3], v)

        def bytes_read_disk_raw(self) -> runtime.CallPerf:
            return self._get(self.type_.generated_offsets[4])

        def set_bytes_read_disk_raw(self, v: runtime.CallPerf) -> None:
            self._set(self.type_.generated_offsets[4], v)

        def bytes_read_cache(self) -> runtime.CallPerf:
            return self._get(self.type_.generated_offsets[5])

        def set_bytes_read_cache(self, v: runtime.CallPerf) -> None:
            self._set(self.type_.generated_offsets[5], v)

    @final
    class SecurityPolicy(GreyCat.Object):
        name_: Final[str] = "runtime::SecurityPolicy"

        def __init__(self, type: Optional[GreyCat.Type], *attributes):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[88]
            super().__init__(type, *attributes)

        def entities(self) -> runtime.SecurityPolicy:
            return self._get(self.type_.generated_offsets[0])

        def set_entities(self, v: runtime.SecurityPolicy) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def credentials(self) -> runtime.SecurityPolicy:
            return self._get(self.type_.generated_offsets[1])

        def set_credentials(self, v: runtime.SecurityPolicy) -> None:
            self._set(self.type_.generated_offsets[1], v)

        def fields(self) -> runtime.SecurityPolicy:
            return self._get(self.type_.generated_offsets[2])

        def set_fields(self, v: runtime.SecurityPolicy) -> None:
            self._set(self.type_.generated_offsets[2], v)

        def keys(self) -> runtime.SecurityPolicy:
            return self._get(self.type_.generated_offsets[3])

        def set_keys(self, v: runtime.SecurityPolicy) -> None:
            self._set(self.type_.generated_offsets[3], v)

        def keys_last_refresh(self) -> runtime.SecurityPolicy:
            return self._get(self.type_.generated_offsets[4])

        def set_keys_last_refresh(self, v: runtime.SecurityPolicy) -> None:
            self._set(self.type_.generated_offsets[4], v)

    @final
    class Runtime(GreyCat.Object):
        name_: Final[str] = "runtime::Runtime"

        def __init__(self, type: Optional[GreyCat.Type], *attributes):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[89]
            super().__init__(type, *attributes)

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
    class PeriodicTask(GreyCat.Object):
        name_: Final[str] = "runtime::PeriodicTask"

        def __init__(self, type: Optional[GreyCat.Type], *attributes):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[90]
            super().__init__(type, *attributes)

        def function(self) -> runtime.PeriodicTask:
            return self._get(self.type_.generated_offsets[0])

        def set_function(self, v: runtime.PeriodicTask) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def user_id(self) -> runtime.PeriodicTask:
            return self._get(self.type_.generated_offsets[1])

        def set_user_id(self, v: runtime.PeriodicTask) -> None:
            self._set(self.type_.generated_offsets[1], v)

        def arguments(self) -> runtime.PeriodicTask:
            return self._get(self.type_.generated_offsets[2])

        def set_arguments(self, v: runtime.PeriodicTask) -> None:
            self._set(self.type_.generated_offsets[2], v)

        def start(self) -> runtime.PeriodicTask:
            return self._get(self.type_.generated_offsets[3])

        def set_start(self, v: runtime.PeriodicTask) -> None:
            self._set(self.type_.generated_offsets[3], v)

        def every(self) -> runtime.PeriodicTask:
            return self._get(self.type_.generated_offsets[4])

        def set_every(self, v: runtime.PeriodicTask) -> None:
            self._set(self.type_.generated_offsets[4], v)

        @staticmethod
        def set(tasks: core.Array, __greycat: Optional[GreyCat] = None) -> None:
            if __greycat is None:
                __greycat  = GreyCat._DEFAULT
            return __greycat.call("runtime::PeriodicTask::set", [tasks, ])

        @staticmethod
        def all(__greycat: Optional[GreyCat] = None) -> core.Array:
            if __greycat is None:
                __greycat  = GreyCat._DEFAULT
            return __greycat.call("runtime::PeriodicTask::all")

    @final
    class UserGroupPolicyType(GreyCat.Enum):
        name_: Final[str] = "runtime::UserGroupPolicyType"
        __indices_by_values: dict[str, int] = {
            "read": 0,
            "write": 1,
            "execute": 2,
        }

        def __init__(self, type: Optional[GreyCat.Type], *attributes):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[91]
            super().__init__(type, *attributes)

        def __class_getitem__(cls, key) -> runtime.UserGroupPolicyType:
            greycat: GreyCat
            if isinstance(key, tuple):
                key, greycat = key
            else:
                greycat = GreyCat._DEFAULT
            t: Final[GreyCat.Type] = greycat.libs_by_name[__std.name()].mapped[91]
            return t.enum_values[t.generated_offsets[runtime.UserGroupPolicyType.__indices_by_values[key]]]

    @final
    class System(GreyCat.Object):
        name_: Final[str] = "runtime::System"

        def __init__(self, type: Optional[GreyCat.Type], *attributes):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[92]
            super().__init__(type, *attributes)

    @final
    class UserCredential(GreyCat.Object):
        name_: Final[str] = "runtime::UserCredential"

        def __init__(self, type: Optional[GreyCat.Type], *attributes):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[93]
            super().__init__(type, *attributes)

        def offset(self) -> runtime.UserCredential:
            return self._get(self.type_.generated_offsets[0])

        def set_offset(self, v: runtime.UserCredential) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def pass_(self) -> runtime.UserCredential:
            return self._get(self.type_.generated_offsets[1])

        def set_pass_(self, v: runtime.UserCredential) -> None:
            self._set(self.type_.generated_offsets[1], v)

    @final
    class Permission(GreyCat.Object):
        name_: Final[str] = "runtime::Permission"

        def __init__(self, type: Optional[GreyCat.Type], *attributes):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[94]
            super().__init__(type, *attributes)

        def name(self) -> runtime.Permission:
            return self._get(self.type_.generated_offsets[0])

        def set_name(self, v: runtime.Permission) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def description(self) -> runtime.Permission:
            return self._get(self.type_.generated_offsets[1])

        def set_description(self, v: runtime.Permission) -> None:
            self._set(self.type_.generated_offsets[1], v)

        @staticmethod
        def all(__greycat: Optional[GreyCat] = None) -> core.Array:
            if __greycat is None:
                __greycat  = GreyCat._DEFAULT
            return __greycat.call("runtime::Permission::all")

    @final
    class Task(GreyCat.Object):
        name_: Final[str] = "runtime::Task"

        def __init__(self, type: Optional[GreyCat.Type], *attributes):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[95]
            super().__init__(type, *attributes)

        def user_id(self) -> runtime.Task:
            return self._get(self.type_.generated_offsets[0])

        def set_user_id(self, v: runtime.Task) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def task_id(self) -> runtime.Task:
            return self._get(self.type_.generated_offsets[1])

        def set_task_id(self, v: runtime.Task) -> None:
            self._set(self.type_.generated_offsets[1], v)

        def mod(self) -> runtime.Task:
            return self._get(self.type_.generated_offsets[2])

        def set_mod(self, v: runtime.Task) -> None:
            self._set(self.type_.generated_offsets[2], v)

        def type(self) -> runtime.Task:
            return self._get(self.type_.generated_offsets[3])

        def set_type(self, v: runtime.Task) -> None:
            self._set(self.type_.generated_offsets[3], v)

        def fun(self) -> runtime.Task:
            return self._get(self.type_.generated_offsets[4])

        def set_fun(self, v: runtime.Task) -> None:
            self._set(self.type_.generated_offsets[4], v)

        def creation(self) -> runtime.Task:
            return self._get(self.type_.generated_offsets[5])

        def set_creation(self, v: runtime.Task) -> None:
            self._set(self.type_.generated_offsets[5], v)

        def start(self) -> runtime.Task:
            return self._get(self.type_.generated_offsets[6])

        def set_start(self, v: runtime.Task) -> None:
            self._set(self.type_.generated_offsets[6], v)

        def duration(self) -> runtime.Task:
            return self._get(self.type_.generated_offsets[7])

        def set_duration(self, v: runtime.Task) -> None:
            self._set(self.type_.generated_offsets[7], v)

        def status(self) -> runtime.Task:
            return self._get(self.type_.generated_offsets[8])

        def set_status(self, v: runtime.Task) -> None:
            self._set(self.type_.generated_offsets[8], v)

        def progress(self) -> runtime.Task:
            return self._get(self.type_.generated_offsets[9])

        def set_progress(self, v: runtime.Task) -> None:
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
class util:
    __T = TypeVar("__T")

    @final
    class LinearQuantizer(Generic[__T], GreyCat.Object):
        name_: Final[str] = "util::LinearQuantizer"

        def __init__(self, type: Optional[GreyCat.Type], *attributes):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[96]
            super().__init__(type, *attributes)

        def min(self) -> util.LinearQuantizer:
            return self._get(self.type_.generated_offsets[0])

        def set_min(self, v: util.LinearQuantizer) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def max(self) -> util.LinearQuantizer:
            return self._get(self.type_.generated_offsets[1])

        def set_max(self, v: util.LinearQuantizer) -> None:
            self._set(self.type_.generated_offsets[1], v)

        def bins(self) -> util.LinearQuantizer:
            return self._get(self.type_.generated_offsets[2])

        def set_bins(self, v: util.LinearQuantizer) -> None:
            self._set(self.type_.generated_offsets[2], v)

        def open(self) -> util.LinearQuantizer:
            return self._get(self.type_.generated_offsets[3])

        def set_open(self, v: util.LinearQuantizer) -> None:
            self._set(self.type_.generated_offsets[3], v)

    @final
    class Gaussian(Generic[__T], GreyCat.Object):
        name_: Final[str] = "util::Gaussian"

        def __init__(self, type: Optional[GreyCat.Type], *attributes):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[97]
            super().__init__(type, *attributes)

        def sum(self) -> util.Gaussian:
            return self._get(self.type_.generated_offsets[0])

        def set_sum(self, v: util.Gaussian) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def sumsq(self) -> util.Gaussian:
            return self._get(self.type_.generated_offsets[1])

        def set_sumsq(self, v: util.Gaussian) -> None:
            self._set(self.type_.generated_offsets[1], v)

        def count(self) -> util.Gaussian:
            return self._get(self.type_.generated_offsets[2])

        def set_count(self, v: util.Gaussian) -> None:
            self._set(self.type_.generated_offsets[2], v)

        def min(self) -> util.Gaussian:
            return self._get(self.type_.generated_offsets[3])

        def set_min(self, v: util.Gaussian) -> None:
            self._set(self.type_.generated_offsets[3], v)

        def max(self) -> util.Gaussian:
            return self._get(self.type_.generated_offsets[4])

        def set_max(self, v: util.Gaussian) -> None:
            self._set(self.type_.generated_offsets[4], v)

    @final
    class Stack(Generic[__T], GreyCat.Object):
        name_: Final[str] = "util::Stack"

        def __init__(self, type: Optional[GreyCat.Type], *attributes):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[98]
            super().__init__(type, *attributes)

        def values(self) -> util.Stack:
            return self._get(self.type_.generated_offsets[0])

        def set_values(self, v: util.Stack) -> None:
            self._set(self.type_.generated_offsets[0], v)

    @final
    class GaussianProfile(Generic[__T], GreyCat.Object):
        name_: Final[str] = "util::GaussianProfile"

        def __init__(self, type: Optional[GreyCat.Type], *attributes):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[99]
            super().__init__(type, *attributes)

        def quantizer(self) -> util.GaussianProfile:
            return self._get(self.type_.generated_offsets[0])

        def set_quantizer(self, v: util.GaussianProfile) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def precision(self) -> util.GaussianProfile:
            return self._get(self.type_.generated_offsets[1])

        def set_precision(self, v: util.GaussianProfile) -> None:
            self._set(self.type_.generated_offsets[1], v)

        def bins(self) -> util.GaussianProfile:
            return self._get(self.type_.generated_offsets[2])

        def set_bins(self, v: util.GaussianProfile) -> None:
            self._set(self.type_.generated_offsets[2], v)

        def value_min(self) -> util.GaussianProfile:
            return self._get(self.type_.generated_offsets[3])

        def set_value_min(self, v: util.GaussianProfile) -> None:
            self._set(self.type_.generated_offsets[3], v)

        def nb_rejected(self) -> util.GaussianProfile:
            return self._get(self.type_.generated_offsets[4])

        def set_nb_rejected(self, v: util.GaussianProfile) -> None:
            self._set(self.type_.generated_offsets[4], v)

    @final
    class ProgressTracker(GreyCat.Object):
        name_: Final[str] = "util::ProgressTracker"

        def __init__(self, type: Optional[GreyCat.Type], *attributes):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[100]
            super().__init__(type, *attributes)

        def start(self) -> util.ProgressTracker:
            return self._get(self.type_.generated_offsets[0])

        def set_start(self, v: util.ProgressTracker) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def total(self) -> util.ProgressTracker:
            return self._get(self.type_.generated_offsets[1])

        def set_total(self, v: util.ProgressTracker) -> None:
            self._set(self.type_.generated_offsets[1], v)

        def counter(self) -> util.ProgressTracker:
            return self._get(self.type_.generated_offsets[2])

        def set_counter(self, v: util.ProgressTracker) -> None:
            self._set(self.type_.generated_offsets[2], v)

        def duration(self) -> util.ProgressTracker:
            return self._get(self.type_.generated_offsets[3])

        def set_duration(self, v: util.ProgressTracker) -> None:
            self._set(self.type_.generated_offsets[3], v)

        def progress(self) -> util.ProgressTracker:
            return self._get(self.type_.generated_offsets[4])

        def set_progress(self, v: util.ProgressTracker) -> None:
            self._set(self.type_.generated_offsets[4], v)

        def speed(self) -> util.ProgressTracker:
            return self._get(self.type_.generated_offsets[5])

        def set_speed(self, v: util.ProgressTracker) -> None:
            self._set(self.type_.generated_offsets[5], v)

        def remaining(self) -> util.ProgressTracker:
            return self._get(self.type_.generated_offsets[6])

        def set_remaining(self, v: util.ProgressTracker) -> None:
            self._set(self.type_.generated_offsets[6], v)

    @final
    class Assert(GreyCat.Object):
        name_: Final[str] = "util::Assert"

        def __init__(self, type: Optional[GreyCat.Type], *attributes):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[101]
            super().__init__(type, *attributes)

    @final
    class MultiQuantizer(Generic[__T], GreyCat.Object):
        name_: Final[str] = "util::MultiQuantizer"

        def __init__(self, type: Optional[GreyCat.Type], *attributes):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[102]
            super().__init__(type, *attributes)

        def quantizers(self) -> util.MultiQuantizer:
            return self._get(self.type_.generated_offsets[0])

        def set_quantizers(self, v: util.MultiQuantizer) -> None:
            self._set(self.type_.generated_offsets[0], v)

    @final
    class HistogramStats(Generic[__T], GreyCat.Object):
        name_: Final[str] = "util::HistogramStats"

        def __init__(self, type: Optional[GreyCat.Type], *attributes):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[103]
            super().__init__(type, *attributes)

        def min(self) -> util.HistogramStats:
            return self._get(self.type_.generated_offsets[0])

        def set_min(self, v: util.HistogramStats) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def max(self) -> util.HistogramStats:
            return self._get(self.type_.generated_offsets[1])

        def set_max(self, v: util.HistogramStats) -> None:
            self._set(self.type_.generated_offsets[1], v)

        def whisker_low(self) -> util.HistogramStats:
            return self._get(self.type_.generated_offsets[2])

        def set_whisker_low(self, v: util.HistogramStats) -> None:
            self._set(self.type_.generated_offsets[2], v)

        def whisker_high(self) -> util.HistogramStats:
            return self._get(self.type_.generated_offsets[3])

        def set_whisker_high(self, v: util.HistogramStats) -> None:
            self._set(self.type_.generated_offsets[3], v)

        def percentile1(self) -> util.HistogramStats:
            return self._get(self.type_.generated_offsets[4])

        def set_percentile1(self, v: util.HistogramStats) -> None:
            self._set(self.type_.generated_offsets[4], v)

        def percentile5(self) -> util.HistogramStats:
            return self._get(self.type_.generated_offsets[5])

        def set_percentile5(self, v: util.HistogramStats) -> None:
            self._set(self.type_.generated_offsets[5], v)

        def percentile10(self) -> util.HistogramStats:
            return self._get(self.type_.generated_offsets[6])

        def set_percentile10(self, v: util.HistogramStats) -> None:
            self._set(self.type_.generated_offsets[6], v)

        def percentile20(self) -> util.HistogramStats:
            return self._get(self.type_.generated_offsets[7])

        def set_percentile20(self, v: util.HistogramStats) -> None:
            self._set(self.type_.generated_offsets[7], v)

        def percentile25(self) -> util.HistogramStats:
            return self._get(self.type_.generated_offsets[8])

        def set_percentile25(self, v: util.HistogramStats) -> None:
            self._set(self.type_.generated_offsets[8], v)

        def percentile50(self) -> util.HistogramStats:
            return self._get(self.type_.generated_offsets[9])

        def set_percentile50(self, v: util.HistogramStats) -> None:
            self._set(self.type_.generated_offsets[9], v)

        def percentile75(self) -> util.HistogramStats:
            return self._get(self.type_.generated_offsets[10])

        def set_percentile75(self, v: util.HistogramStats) -> None:
            self._set(self.type_.generated_offsets[10], v)

        def percentile80(self) -> util.HistogramStats:
            return self._get(self.type_.generated_offsets[11])

        def set_percentile80(self, v: util.HistogramStats) -> None:
            self._set(self.type_.generated_offsets[11], v)

        def percentile90(self) -> util.HistogramStats:
            return self._get(self.type_.generated_offsets[12])

        def set_percentile90(self, v: util.HistogramStats) -> None:
            self._set(self.type_.generated_offsets[12], v)

        def percentile95(self) -> util.HistogramStats:
            return self._get(self.type_.generated_offsets[13])

        def set_percentile95(self, v: util.HistogramStats) -> None:
            self._set(self.type_.generated_offsets[13], v)

        def percentile99(self) -> util.HistogramStats:
            return self._get(self.type_.generated_offsets[14])

        def set_percentile99(self, v: util.HistogramStats) -> None:
            self._set(self.type_.generated_offsets[14], v)

        def sum(self) -> util.HistogramStats:
            return self._get(self.type_.generated_offsets[15])

        def set_sum(self, v: util.HistogramStats) -> None:
            self._set(self.type_.generated_offsets[15], v)

        def avg(self) -> util.HistogramStats:
            return self._get(self.type_.generated_offsets[16])

        def set_avg(self, v: util.HistogramStats) -> None:
            self._set(self.type_.generated_offsets[16], v)

        def std(self) -> util.HistogramStats:
            return self._get(self.type_.generated_offsets[17])

        def set_std(self, v: util.HistogramStats) -> None:
            self._set(self.type_.generated_offsets[17], v)

        def size(self) -> util.HistogramStats:
            return self._get(self.type_.generated_offsets[18])

        def set_size(self, v: util.HistogramStats) -> None:
            self._set(self.type_.generated_offsets[18], v)

    @final
    class Crypto(GreyCat.Object):
        name_: Final[str] = "util::Crypto"

        def __init__(self, type: Optional[GreyCat.Type], *attributes):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[104]
            super().__init__(type, *attributes)

    @final
    class TimeWindow(Generic[__T], GreyCat.Object):
        name_: Final[str] = "util::TimeWindow"

        def __init__(self, type: Optional[GreyCat.Type], *attributes):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[105]
            super().__init__(type, *attributes)

        def values(self) -> util.TimeWindow:
            return self._get(self.type_.generated_offsets[0])

        def set_values(self, v: util.TimeWindow) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def span(self) -> util.TimeWindow:
            return self._get(self.type_.generated_offsets[1])

        def set_span(self, v: util.TimeWindow) -> None:
            self._set(self.type_.generated_offsets[1], v)

        def sum(self) -> util.TimeWindow:
            return self._get(self.type_.generated_offsets[2])

        def set_sum(self, v: util.TimeWindow) -> None:
            self._set(self.type_.generated_offsets[2], v)

        def sumsq(self) -> util.TimeWindow:
            return self._get(self.type_.generated_offsets[3])

        def set_sumsq(self, v: util.TimeWindow) -> None:
            self._set(self.type_.generated_offsets[3], v)

        def field(self) -> util.TimeWindow:
            return self._get(self.type_.generated_offsets[4])

        def set_field(self, v: util.TimeWindow) -> None:
            self._set(self.type_.generated_offsets[4], v)

    @final
    class Plot(GreyCat.Object):
        name_: Final[str] = "util::Plot"

        def __init__(self, type: Optional[GreyCat.Type], *attributes):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[106]
            super().__init__(type, *attributes)

    @final
    class LogQuantizer(Generic[__T], GreyCat.Object):
        name_: Final[str] = "util::LogQuantizer"

        def __init__(self, type: Optional[GreyCat.Type], *attributes):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[107]
            super().__init__(type, *attributes)

        def min(self) -> util.LogQuantizer:
            return self._get(self.type_.generated_offsets[0])

        def set_min(self, v: util.LogQuantizer) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def max(self) -> util.LogQuantizer:
            return self._get(self.type_.generated_offsets[1])

        def set_max(self, v: util.LogQuantizer) -> None:
            self._set(self.type_.generated_offsets[1], v)

        def bins(self) -> util.LogQuantizer:
            return self._get(self.type_.generated_offsets[2])

        def set_bins(self, v: util.LogQuantizer) -> None:
            self._set(self.type_.generated_offsets[2], v)

        def open(self) -> util.LogQuantizer:
            return self._get(self.type_.generated_offsets[3])

        def set_open(self, v: util.LogQuantizer) -> None:
            self._set(self.type_.generated_offsets[3], v)

    @final
    class QuantizerSlotBound(Generic[__T], GreyCat.Object):
        name_: Final[str] = "util::QuantizerSlotBound"

        def __init__(self, type: Optional[GreyCat.Type], *attributes):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[108]
            super().__init__(type, *attributes)

        def min(self) -> util.QuantizerSlotBound:
            return self._get(self.type_.generated_offsets[0])

        def set_min(self, v: util.QuantizerSlotBound) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def max(self) -> util.QuantizerSlotBound:
            return self._get(self.type_.generated_offsets[1])

        def set_max(self, v: util.QuantizerSlotBound) -> None:
            self._set(self.type_.generated_offsets[1], v)

        def center(self) -> util.QuantizerSlotBound:
            return self._get(self.type_.generated_offsets[2])

        def set_center(self, v: util.QuantizerSlotBound) -> None:
            self._set(self.type_.generated_offsets[2], v)

    @final
    class GaussianProfileSlot(GreyCat.Object):
        name_: Final[str] = "util::GaussianProfileSlot"

        def __init__(self, type: Optional[GreyCat.Type], *attributes):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[109]
            super().__init__(type, *attributes)

        def sum(self) -> util.GaussianProfileSlot:
            return self._get(self.type_.generated_offsets[0])

        def set_sum(self, v: util.GaussianProfileSlot) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def sumsq(self) -> util.GaussianProfileSlot:
            return self._get(self.type_.generated_offsets[1])

        def set_sumsq(self, v: util.GaussianProfileSlot) -> None:
            self._set(self.type_.generated_offsets[1], v)

        def count(self) -> util.GaussianProfileSlot:
            return self._get(self.type_.generated_offsets[2])

        def set_count(self, v: util.GaussianProfileSlot) -> None:
            self._set(self.type_.generated_offsets[2], v)

    @final
    class SlidingWindow(Generic[__T], GreyCat.Object):
        name_: Final[str] = "util::SlidingWindow"

        def __init__(self, type: Optional[GreyCat.Type], *attributes):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[110]
            super().__init__(type, *attributes)

        def values(self) -> util.SlidingWindow:
            return self._get(self.type_.generated_offsets[0])

        def set_values(self, v: util.SlidingWindow) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def span(self) -> util.SlidingWindow:
            return self._get(self.type_.generated_offsets[1])

        def set_span(self, v: util.SlidingWindow) -> None:
            self._set(self.type_.generated_offsets[1], v)

        def sum(self) -> util.SlidingWindow:
            return self._get(self.type_.generated_offsets[2])

        def set_sum(self, v: util.SlidingWindow) -> None:
            self._set(self.type_.generated_offsets[2], v)

        def sumsq(self) -> util.SlidingWindow:
            return self._get(self.type_.generated_offsets[3])

        def set_sumsq(self, v: util.SlidingWindow) -> None:
            self._set(self.type_.generated_offsets[3], v)

        def field(self) -> util.SlidingWindow:
            return self._get(self.type_.generated_offsets[4])

        def set_field(self, v: util.SlidingWindow) -> None:
            self._set(self.type_.generated_offsets[4], v)

    @final
    class HistogramBin(Generic[__T], GreyCat.Object):
        name_: Final[str] = "util::HistogramBin"

        def __init__(self, type: Optional[GreyCat.Type], *attributes):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[111]
            super().__init__(type, *attributes)

        def bin(self) -> util.HistogramBin:
            return self._get(self.type_.generated_offsets[0])

        def set_bin(self, v: util.HistogramBin) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def count(self) -> util.HistogramBin:
            return self._get(self.type_.generated_offsets[1])

        def set_count(self, v: util.HistogramBin) -> None:
            self._set(self.type_.generated_offsets[1], v)

        def ratio(self) -> util.HistogramBin:
            return self._get(self.type_.generated_offsets[2])

        def set_ratio(self, v: util.HistogramBin) -> None:
            self._set(self.type_.generated_offsets[2], v)

        def cumulative_count(self) -> util.HistogramBin:
            return self._get(self.type_.generated_offsets[3])

        def set_cumulative_count(self, v: util.HistogramBin) -> None:
            self._set(self.type_.generated_offsets[3], v)

        def cumulative_ratio(self) -> util.HistogramBin:
            return self._get(self.type_.generated_offsets[4])

        def set_cumulative_ratio(self, v: util.HistogramBin) -> None:
            self._set(self.type_.generated_offsets[4], v)

    @final
    class Random(GreyCat.Object):
        name_: Final[str] = "util::Random"

        def __init__(self, type: Optional[GreyCat.Type], *attributes):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[112]
            super().__init__(type, *attributes)

        def seed(self) -> util.Random:
            return self._get(self.type_.generated_offsets[0])

        def set_seed(self, v: util.Random) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def v(self) -> util.Random:
            return self._get(self.type_.generated_offsets[1])

        def set_v(self, v: util.Random) -> None:
            self._set(self.type_.generated_offsets[1], v)

    @final
    class CustomQuantizer(Generic[__T], GreyCat.Object):
        name_: Final[str] = "util::CustomQuantizer"

        def __init__(self, type: Optional[GreyCat.Type], *attributes):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[113]
            super().__init__(type, *attributes)

        def min(self) -> util.CustomQuantizer:
            return self._get(self.type_.generated_offsets[0])

        def set_min(self, v: util.CustomQuantizer) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def max(self) -> util.CustomQuantizer:
            return self._get(self.type_.generated_offsets[1])

        def set_max(self, v: util.CustomQuantizer) -> None:
            self._set(self.type_.generated_offsets[1], v)

        def step_starts(self) -> util.CustomQuantizer:
            return self._get(self.type_.generated_offsets[2])

        def set_step_starts(self, v: util.CustomQuantizer) -> None:
            self._set(self.type_.generated_offsets[2], v)

        def open(self) -> util.CustomQuantizer:
            return self._get(self.type_.generated_offsets[3])

        def set_open(self, v: util.CustomQuantizer) -> None:
            self._set(self.type_.generated_offsets[3], v)

    @final
    class Histogram(Generic[__T], GreyCat.Object):
        name_: Final[str] = "util::Histogram"

        def __init__(self, type: Optional[GreyCat.Type], *attributes):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[114]
            super().__init__(type, *attributes)

        def quantizer(self) -> util.Histogram:
            return self._get(self.type_.generated_offsets[0])

        def set_quantizer(self, v: util.Histogram) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def bins(self) -> util.Histogram:
            return self._get(self.type_.generated_offsets[1])

        def set_bins(self, v: util.Histogram) -> None:
            self._set(self.type_.generated_offsets[1], v)

        def nb_rejected(self) -> util.Histogram:
            return self._get(self.type_.generated_offsets[2])

        def set_nb_rejected(self, v: util.Histogram) -> None:
            self._set(self.type_.generated_offsets[2], v)

        def nb_accepted(self) -> util.Histogram:
            return self._get(self.type_.generated_offsets[3])

        def set_nb_accepted(self, v: util.Histogram) -> None:
            self._set(self.type_.generated_offsets[3], v)

        def min(self) -> util.Histogram:
            return self._get(self.type_.generated_offsets[4])

        def set_min(self, v: util.Histogram) -> None:
            self._set(self.type_.generated_offsets[4], v)

        def max(self) -> util.Histogram:
            return self._get(self.type_.generated_offsets[5])

        def set_max(self, v: util.Histogram) -> None:
            self._set(self.type_.generated_offsets[5], v)

        def sum(self) -> util.Histogram:
            return self._get(self.type_.generated_offsets[6])

        def set_sum(self, v: util.Histogram) -> None:
            self._set(self.type_.generated_offsets[6], v)

        def sumsq(self) -> util.Histogram:
            return self._get(self.type_.generated_offsets[7])

        def set_sumsq(self, v: util.Histogram) -> None:
            self._set(self.type_.generated_offsets[7], v)

    @final
    class Quantizer(Generic[__T], GreyCat.Object):
        name_: Final[str] = "util::Quantizer"

        def __init__(self, type: Optional[GreyCat.Type], *attributes):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[115]
            super().__init__(type, *attributes)

    @final
    class Queue(Generic[__T], GreyCat.Object):
        name_: Final[str] = "util::Queue"

        def __init__(self, type: Optional[GreyCat.Type], *attributes):
            if type is None:
                GreyCat._DEFAULT.libs_by_name[__std.name()].mapped[116]
            super().__init__(type, *attributes)

        def values(self) -> util.Queue:
            return self._get(self.type_.generated_offsets[0])

        def set_values(self, v: util.Queue) -> None:
            self._set(self.type_.generated_offsets[0], v)

        def capacity(self) -> util.Queue:
            return self._get(self.type_.generated_offsets[1])

        def set_capacity(self, v: util.Queue) -> None:
            self._set(self.type_.generated_offsets[1], v)


@final
class __std(GreyCat.Library):
    def name(self) -> str:
        return "std"

    def configure(self, loaders: dict[str, GreyCat.Loader], factories: dict[str, GreyCat.Factory]) -> None:
        factories[core.ErrorCode.name_] = lambda type, attributes: core.ErrorCode(type, attributes)
        factories[core.t4.name_] = lambda type, attributes: core.t4(type, attributes)
        loaders[core.t4.name_] = lambda type, stream: std_n.core._t4.load(type, stream)

        factories[core.Table.name_] = lambda type, attributes: core.Table(type, attributes)
        loaders[core.Table.name_] = lambda type, stream: std_n.core._Table.load(type, stream)

        factories[core.t3.name_] = lambda type, attributes: core.t3(type, attributes)
        loaders[core.t3.name_] = lambda type, stream: std_n.core._t3.load(type, stream)

        factories[core.nodeIndex.name_] = lambda type, attributes: core.nodeIndex(type, attributes)
        loaders[core.nodeIndex.name_] = lambda type, stream: std_n.core._nodeIndex.load(type, stream)

        factories[core.GeoCircle.name_] = lambda type, attributes: core.GeoCircle(type, attributes)
        factories[core.TimeZone.name_] = lambda type, attributes: core.TimeZone(type, attributes)
        factories[core.t2.name_] = lambda type, attributes: core.t2(type, attributes)
        loaders[core.t2.name_] = lambda type, stream: std_n.core._t2.load(type, stream)

        factories[core.String.name_] = lambda type, attributes: core.String(type, attributes)
        loaders[core.String.name_] = lambda type, stream: std_n.core._String.load(type, stream)

        factories[core.GeoBox.name_] = lambda type, attributes: core.GeoBox(type, attributes)
        factories[core.t4f.name_] = lambda type, attributes: core.t4f(type, attributes)
        loaders[core.t4f.name_] = lambda type, stream: std_n.core._t4f.load(type, stream)

        factories[core.field.name_] = lambda type, attributes: core.field(type, attributes)
        loaders[core.field.name_] = lambda type, stream: std_n.core._field.load(type, stream)

        factories[core.CalendarUnit.name_] = lambda type, attributes: core.CalendarUnit(type, attributes)
        factories[core.Buffer.name_] = lambda type, attributes: core.Buffer(type, attributes)
        loaders[core.Buffer.name_] = lambda type, stream: std_n.core._Buffer.load(type, stream)

        factories[core.nodeList.name_] = lambda type, attributes: core.nodeList(type, attributes)
        loaders[core.nodeList.name_] = lambda type, stream: std_n.core._nodeList.load(type, stream)

        factories[core.nodeTime.name_] = lambda type, attributes: core.nodeTime(type, attributes)
        loaders[core.nodeTime.name_] = lambda type, stream: std_n.core._nodeTime.load(type, stream)

        factories[core.duration.name_] = lambda type, attributes: core.duration(type, attributes)
        loaders[core.duration.name_] = lambda type, stream: std_n.core._duration.load(type, stream)

        factories[core.Tensor.name_] = lambda type, attributes: core.Tensor(type, attributes)
        loaders[core.Tensor.name_] = lambda type, stream: std_n.core._Tensor.load(type, stream)

        factories[core.nodeTimeSingleton.name_] = lambda type, attributes: core.nodeTimeSingleton(type, attributes)
        factories[core.NodeInfo.name_] = lambda type, attributes: core.NodeInfo(type, attributes)
        factories[core.SortOrder.name_] = lambda type, attributes: core.SortOrder(type, attributes)
        factories[core.t3f.name_] = lambda type, attributes: core.t3f(type, attributes)
        loaders[core.t3f.name_] = lambda type, stream: std_n.core._t3f.load(type, stream)

        factories[core.MathConstants.name_] = lambda type, attributes: core.MathConstants(type, attributes)
        factories[core.type.name_] = lambda type, attributes: core.type(type, attributes)
        loaders[core.type.name_] = lambda type, stream: std_n.core._type.load(type, stream)

        factories[core.SamplingMode.name_] = lambda type, attributes: core.SamplingMode(type, attributes)
        factories[core.geo.name_] = lambda type, attributes: core.geo(type, attributes)
        loaders[core.geo.name_] = lambda type, stream: std_n.core._geo.load(type, stream)

        factories[core.Map.name_] = lambda type, attributes: core.Map(type, attributes)
        loaders[core.Map.name_] = lambda type, stream: std_n.core._Map.load(type, stream)

        factories[core.Error.name_] = lambda type, attributes: core.Error(type, attributes)
        factories[core.nodeTimeCursor.name_] = lambda type, attributes: core.nodeTimeCursor(type, attributes)
        factories[core.nodeGeo.name_] = lambda type, attributes: core.nodeGeo(type, attributes)
        loaders[core.nodeGeo.name_] = lambda type, stream: std_n.core._nodeGeo.load(type, stream)

        factories[core.node.name_] = lambda type, attributes: core.node(type, attributes)
        loaders[core.node.name_] = lambda type, stream: std_n.core._node.load(type, stream)

        factories[core.DurationUnit.name_] = lambda type, attributes: core.DurationUnit(type, attributes)
        factories[core.TableColumnMapping.name_] = lambda type, attributes: core.TableColumnMapping(type, attributes)
        factories[core.TensorType.name_] = lambda type, attributes: core.TensorType(type, attributes)
        factories[core.Tuple.name_] = lambda type, attributes: core.Tuple(type, attributes)
        factories[core.time.name_] = lambda type, attributes: core.time(type, attributes)
        loaders[core.time.name_] = lambda type, stream: std_n.core._time.load(type, stream)

        factories[core.ErrorFrame.name_] = lambda type, attributes: core.ErrorFrame(type, attributes)
        factories[core.Array.name_] = lambda type, attributes: core.Array(type, attributes)
        loaders[core.Array.name_] = lambda type, stream: std_n.core._Array.load(type, stream)

        factories[core.GeoPoly.name_] = lambda type, attributes: core.GeoPoly(type, attributes)
        factories[core.FloatPrecision.name_] = lambda type, attributes: core.FloatPrecision(type, attributes)
        factories[core.t2f.name_] = lambda type, attributes: core.t2f(type, attributes)
        loaders[core.t2f.name_] = lambda type, stream: std_n.core._t2f.load(type, stream)

        factories[core.Date.name_] = lambda type, attributes: core.Date(type, attributes)
        factories[core.function.name_] = lambda type, attributes: core.function(type, attributes)
        loaders[core.function.name_] = lambda type, stream: std_n.core._function.load(type, stream)

        factories[core.str.name_] = lambda type, attributes: core.str(type, attributes)
        loaders[core.str.name_] = lambda type, stream: std_n.core._str.load(type, stream)

        factories[io.SmtpAuth.name_] = lambda type, attributes: io.SmtpAuth(type, attributes)
        factories[io.Url.name_] = lambda type, attributes: io.Url(type, attributes)
        factories[io.File.name_] = lambda type, attributes: io.File(type, attributes)
        factories[io.CsvAnalysisConfig.name_] = lambda type, attributes: io.CsvAnalysisConfig(type, attributes)
        factories[io.Writer.name_] = lambda type, attributes: io.Writer(type, attributes)
        factories[io.GcbWriter.name_] = lambda type, attributes: io.GcbWriter(type, attributes)
        factories[io.TextWriter.name_] = lambda type, attributes: io.TextWriter(type, attributes)
        factories[io.GcbReader.name_] = lambda type, attributes: io.GcbReader(type, attributes)
        factories[io.SmtpMode.name_] = lambda type, attributes: io.SmtpMode(type, attributes)
        factories[io.CsvColumnStatistics.name_] = lambda type, attributes: io.CsvColumnStatistics(type, attributes)
        factories[io.CsvFormat.name_] = lambda type, attributes: io.CsvFormat(type, attributes)
        factories[io.CsvSharding.name_] = lambda type, attributes: io.CsvSharding(type, attributes)
        factories[io.Email.name_] = lambda type, attributes: io.Email(type, attributes)
        factories[io.CsvReader.name_] = lambda type, attributes: io.CsvReader(type, attributes)
        factories[io.Reader.name_] = lambda type, attributes: io.Reader(type, attributes)
        factories[io.Http.name_] = lambda type, attributes: io.Http(type, attributes)
        factories[io.CsvWriter.name_] = lambda type, attributes: io.CsvWriter(type, attributes)
        factories[io.TextReader.name_] = lambda type, attributes: io.TextReader(type, attributes)
        factories[io.CsvStatistics.name_] = lambda type, attributes: io.CsvStatistics(type, attributes)
        factories[io.JsonWriter.name_] = lambda type, attributes: io.JsonWriter(type, attributes)
        factories[io.JsonReader.name_] = lambda type, attributes: io.JsonReader(type, attributes)
        factories[io.Json.name_] = lambda type, attributes: io.Json(type, attributes)
        factories[io.Csv.name_] = lambda type, attributes: io.Csv(type, attributes)
        factories[io.Smtp.name_] = lambda type, attributes: io.Smtp(type, attributes)
        factories[io.FileWalker.name_] = lambda type, attributes: io.FileWalker(type, attributes)
        factories[io.HttpHeader.name_] = lambda type, attributes: io.HttpHeader(type, attributes)
        factories[runtime.LogLevel.name_] = lambda type, attributes: runtime.LogLevel(type, attributes)
        factories[runtime.RuntimeInfo.name_] = lambda type, attributes: runtime.RuntimeInfo(type, attributes)
        factories[runtime.SecurityEntity.name_] = lambda type, attributes: runtime.SecurityEntity(type, attributes)
        factories[runtime.Debug.name_] = lambda type, attributes: runtime.Debug(type, attributes)
        factories[runtime.Role.name_] = lambda type, attributes: runtime.Role(type, attributes)
        factories[runtime.Log.name_] = lambda type, attributes: runtime.Log(type, attributes)
        factories[runtime.Variable.name_] = lambda type, attributes: runtime.Variable(type, attributes)
        factories[runtime.OpenIDConnect.name_] = lambda type, attributes: runtime.OpenIDConnect(type, attributes)
        factories[runtime.License.name_] = lambda type, attributes: runtime.License(type, attributes)
        factories[runtime.UserGroupPolicy.name_] = lambda type, attributes: runtime.UserGroupPolicy(type, attributes)
        factories[runtime.User.name_] = lambda type, attributes: runtime.User(type, attributes)
        factories[runtime.Job.name_] = lambda type, attributes: runtime.Job(type, attributes)
        factories[runtime.SecurityFields.name_] = lambda type, attributes: runtime.SecurityFields(type, attributes)
        factories[runtime.TaskStatus.name_] = lambda type, attributes: runtime.TaskStatus(type, attributes)
        factories[runtime.LicenseType.name_] = lambda type, attributes: runtime.LicenseType(type, attributes)
        factories[runtime.Frame.name_] = lambda type, attributes: runtime.Frame(type, attributes)
        factories[runtime.UserGroup.name_] = lambda type, attributes: runtime.UserGroup(type, attributes)
        factories[runtime.CallPerf.name_] = lambda type, attributes: runtime.CallPerf(type, attributes)
        factories[runtime.SecurityPolicy.name_] = lambda type, attributes: runtime.SecurityPolicy(type, attributes)
        factories[runtime.Runtime.name_] = lambda type, attributes: runtime.Runtime(type, attributes)
        factories[runtime.PeriodicTask.name_] = lambda type, attributes: runtime.PeriodicTask(type, attributes)
        factories[runtime.UserGroupPolicyType.name_] = lambda type, attributes: runtime.UserGroupPolicyType(type, attributes)
        factories[runtime.System.name_] = lambda type, attributes: runtime.System(type, attributes)
        factories[runtime.UserCredential.name_] = lambda type, attributes: runtime.UserCredential(type, attributes)
        factories[runtime.Permission.name_] = lambda type, attributes: runtime.Permission(type, attributes)
        factories[runtime.Task.name_] = lambda type, attributes: runtime.Task(type, attributes)
        factories[util.LinearQuantizer.name_] = lambda type, attributes: util.LinearQuantizer(type, attributes)
        factories[util.Gaussian.name_] = lambda type, attributes: util.Gaussian(type, attributes)
        factories[util.Stack.name_] = lambda type, attributes: util.Stack(type, attributes)
        factories[util.GaussianProfile.name_] = lambda type, attributes: util.GaussianProfile(type, attributes)
        factories[util.ProgressTracker.name_] = lambda type, attributes: util.ProgressTracker(type, attributes)
        factories[util.Assert.name_] = lambda type, attributes: util.Assert(type, attributes)
        factories[util.MultiQuantizer.name_] = lambda type, attributes: util.MultiQuantizer(type, attributes)
        factories[util.HistogramStats.name_] = lambda type, attributes: util.HistogramStats(type, attributes)
        factories[util.Crypto.name_] = lambda type, attributes: util.Crypto(type, attributes)
        factories[util.TimeWindow.name_] = lambda type, attributes: util.TimeWindow(type, attributes)
        factories[util.Plot.name_] = lambda type, attributes: util.Plot(type, attributes)
        factories[util.LogQuantizer.name_] = lambda type, attributes: util.LogQuantizer(type, attributes)
        factories[util.QuantizerSlotBound.name_] = lambda type, attributes: util.QuantizerSlotBound(type, attributes)
        factories[util.GaussianProfileSlot.name_] = lambda type, attributes: util.GaussianProfileSlot(type, attributes)
        factories[util.SlidingWindow.name_] = lambda type, attributes: util.SlidingWindow(type, attributes)
        factories[util.HistogramBin.name_] = lambda type, attributes: util.HistogramBin(type, attributes)
        factories[util.Random.name_] = lambda type, attributes: util.Random(type, attributes)
        factories[util.CustomQuantizer.name_] = lambda type, attributes: util.CustomQuantizer(type, attributes)
        factories[util.Histogram.name_] = lambda type, attributes: util.Histogram(type, attributes)
        factories[util.Quantizer.name_] = lambda type, attributes: util.Quantizer(type, attributes)
        factories[util.Queue.name_] = lambda type, attributes: util.Queue(type, attributes)

    def init(self, greycat: GreyCat) -> None:
        self.mapped: list[GreyCat.Type] = [
            greycat.types_by_name[core.ErrorCode.name_],
            greycat.types_by_name[core.t4.name_],
            greycat.types_by_name[core.Table.name_],
            greycat.types_by_name[core.t3.name_],
            greycat.types_by_name[core.nodeIndex.name_],
            greycat.types_by_name[core.GeoCircle.name_],
            greycat.types_by_name[core.TimeZone.name_],
            greycat.types_by_name[core.t2.name_],
            greycat.types_by_name[core.String.name_],
            greycat.types_by_name[core.GeoBox.name_],
            greycat.types_by_name[core.t4f.name_],
            greycat.types_by_name[core.field.name_],
            greycat.types_by_name[core.CalendarUnit.name_],
            greycat.types_by_name[core.Buffer.name_],
            greycat.types_by_name[core.nodeList.name_],
            greycat.types_by_name[core.nodeTime.name_],
            greycat.types_by_name[core.duration.name_],
            greycat.types_by_name[core.Tensor.name_],
            greycat.types_by_name[core.nodeTimeSingleton.name_],
            greycat.types_by_name[core.NodeInfo.name_],
            greycat.types_by_name[core.SortOrder.name_],
            greycat.types_by_name[core.t3f.name_],
            greycat.types_by_name[core.MathConstants.name_],
            greycat.types_by_name[core.type.name_],
            greycat.types_by_name[core.SamplingMode.name_],
            greycat.types_by_name[core.geo.name_],
            greycat.types_by_name[core.Map.name_],
            greycat.types_by_name[core.Error.name_],
            greycat.types_by_name[core.nodeTimeCursor.name_],
            greycat.types_by_name[core.nodeGeo.name_],
            greycat.types_by_name[core.node.name_],
            greycat.types_by_name[core.DurationUnit.name_],
            greycat.types_by_name[core.TableColumnMapping.name_],
            greycat.types_by_name[core.TensorType.name_],
            greycat.types_by_name[core.Tuple.name_],
            greycat.types_by_name[core.time.name_],
            greycat.types_by_name[core.ErrorFrame.name_],
            greycat.types_by_name[core.Array.name_],
            greycat.types_by_name[core.GeoPoly.name_],
            greycat.types_by_name[core.FloatPrecision.name_],
            greycat.types_by_name[core.t2f.name_],
            greycat.types_by_name[core.Date.name_],
            greycat.types_by_name[core.function.name_],
            greycat.types_by_name[core.str.name_],
            greycat.types_by_name[io.SmtpAuth.name_],
            greycat.types_by_name[io.Url.name_],
            greycat.types_by_name[io.File.name_],
            greycat.types_by_name[io.CsvAnalysisConfig.name_],
            greycat.types_by_name[io.Writer.name_],
            greycat.types_by_name[io.GcbWriter.name_],
            greycat.types_by_name[io.TextWriter.name_],
            greycat.types_by_name[io.GcbReader.name_],
            greycat.types_by_name[io.SmtpMode.name_],
            greycat.types_by_name[io.CsvColumnStatistics.name_],
            greycat.types_by_name[io.CsvFormat.name_],
            greycat.types_by_name[io.CsvSharding.name_],
            greycat.types_by_name[io.Email.name_],
            greycat.types_by_name[io.CsvReader.name_],
            greycat.types_by_name[io.Reader.name_],
            greycat.types_by_name[io.Http.name_],
            greycat.types_by_name[io.CsvWriter.name_],
            greycat.types_by_name[io.TextReader.name_],
            greycat.types_by_name[io.CsvStatistics.name_],
            greycat.types_by_name[io.JsonWriter.name_],
            greycat.types_by_name[io.JsonReader.name_],
            greycat.types_by_name[io.Json.name_],
            greycat.types_by_name[io.Csv.name_],
            greycat.types_by_name[io.Smtp.name_],
            greycat.types_by_name[io.FileWalker.name_],
            greycat.types_by_name[io.HttpHeader.name_],
            greycat.types_by_name[runtime.LogLevel.name_],
            greycat.types_by_name[runtime.RuntimeInfo.name_],
            greycat.types_by_name[runtime.SecurityEntity.name_],
            greycat.types_by_name[runtime.Debug.name_],
            greycat.types_by_name[runtime.Role.name_],
            greycat.types_by_name[runtime.Log.name_],
            greycat.types_by_name[runtime.Variable.name_],
            greycat.types_by_name[runtime.OpenIDConnect.name_],
            greycat.types_by_name[runtime.License.name_],
            greycat.types_by_name[runtime.UserGroupPolicy.name_],
            greycat.types_by_name[runtime.User.name_],
            greycat.types_by_name[runtime.Job.name_],
            greycat.types_by_name[runtime.SecurityFields.name_],
            greycat.types_by_name[runtime.TaskStatus.name_],
            greycat.types_by_name[runtime.LicenseType.name_],
            greycat.types_by_name[runtime.Frame.name_],
            greycat.types_by_name[runtime.UserGroup.name_],
            greycat.types_by_name[runtime.CallPerf.name_],
            greycat.types_by_name[runtime.SecurityPolicy.name_],
            greycat.types_by_name[runtime.Runtime.name_],
            greycat.types_by_name[runtime.PeriodicTask.name_],
            greycat.types_by_name[runtime.UserGroupPolicyType.name_],
            greycat.types_by_name[runtime.System.name_],
            greycat.types_by_name[runtime.UserCredential.name_],
            greycat.types_by_name[runtime.Permission.name_],
            greycat.types_by_name[runtime.Task.name_],
            greycat.types_by_name[util.LinearQuantizer.name_],
            greycat.types_by_name[util.Gaussian.name_],
            greycat.types_by_name[util.Stack.name_],
            greycat.types_by_name[util.GaussianProfile.name_],
            greycat.types_by_name[util.ProgressTracker.name_],
            greycat.types_by_name[util.Assert.name_],
            greycat.types_by_name[util.MultiQuantizer.name_],
            greycat.types_by_name[util.HistogramStats.name_],
            greycat.types_by_name[util.Crypto.name_],
            greycat.types_by_name[util.TimeWindow.name_],
            greycat.types_by_name[util.Plot.name_],
            greycat.types_by_name[util.LogQuantizer.name_],
            greycat.types_by_name[util.QuantizerSlotBound.name_],
            greycat.types_by_name[util.GaussianProfileSlot.name_],
            greycat.types_by_name[util.SlidingWindow.name_],
            greycat.types_by_name[util.HistogramBin.name_],
            greycat.types_by_name[util.Random.name_],
            greycat.types_by_name[util.CustomQuantizer.name_],
            greycat.types_by_name[util.Histogram.name_],
            greycat.types_by_name[util.Quantizer.name_],
            greycat.types_by_name[util.Queue.name_],
        ]
        self.mapped[0].resolve_generated_offset_with_values("none", 0, "interrupted", 1, "await", 2, "timeout", 6, "forbidden", 7, "runtime_error", 8)
        self.mapped[5].resolve_generated_offsets("center", "radius")
        self.mapped[6].resolve_generated_offset_with_values("UTC", None, "Africa/Abidjan", None, "Africa/Accra", None, "Africa/Addis_Ababa", None, "Africa/Algiers", None, "Africa/Asmara", None, "Africa/Asmera", None, "Africa/Bamako", None, "Africa/Bangui", None, "Africa/Banjul", None, "Africa/Bissau", None, "Africa/Blantyre", None, "Africa/Brazzaville", None, "Africa/Bujumbura", None, "Africa/Cairo", None, "Africa/Casablanca", None, "Africa/Ceuta", None, "Africa/Conakry", None, "Africa/Dakar", None, "Africa/Dar_es_Salaam", None, "Africa/Djibouti", None, "Africa/Douala", None, "Africa/El_Aaiun", None, "Africa/Freetown", None, "Africa/Gaborone", None, "Africa/Harare", None, "Africa/Johannesburg", None, "Africa/Juba", None, "Africa/Kampala", None, "Africa/Khartoum", None, "Africa/Kigali", None, "Africa/Kinshasa", None, "Africa/Lagos", None, "Africa/Libreville", None, "Africa/Lome", None, "Africa/Luanda", None, "Africa/Lubumbashi", None, "Africa/Lusaka", None, "Africa/Malabo", None, "Africa/Maputo", None, "Africa/Maseru", None, "Africa/Mbabane", None, "Africa/Mogadishu", None, "Africa/Monrovia", None, "Africa/Nairobi", None, "Africa/Ndjamena", None, "Africa/Niamey", None, "Africa/Nouakchott", None, "Africa/Ouagadougou", None, "Africa/Porto-Novo", None, "Africa/Sao_Tome", None, "Africa/Timbuktu", None, "Africa/Tripoli", None, "Africa/Tunis", None, "Africa/Windhoek", None, "America/Adak", None, "America/Anchorage", None, "America/Anguilla", None, "America/Antigua", None, "America/Araguaina", None, "America/Argentina/Buenos_Aires", None, "America/Argentina/Catamarca", None, "America/Argentina/ComodRivadavia", None, "America/Argentina/Cordoba", None, "America/Argentina/Jujuy", None, "America/Argentina/La_Rioja", None, "America/Argentina/Mendoza", None, "America/Argentina/Rio_Gallegos", None, "America/Argentina/Salta", None, "America/Argentina/San_Juan", None, "America/Argentina/San_Luis", None, "America/Argentina/Tucuman", None, "America/Argentina/Ushuaia", None, "America/Aruba", None, "America/Asuncion", None, "America/Atikokan", None, "America/Atka", None, "America/Bahia", None, "America/Bahia_Banderas", None, "America/Barbados", None, "America/Belem", None, "America/Belize", None, "America/Blanc-Sablon", None, "America/Boa_Vista", None, "America/Bogota", None, "America/Boise", None, "America/Buenos_Aires", None, "America/Cambridge_Bay", None, "America/Campo_Grande", None, "America/Cancun", None, "America/Caracas", None, "America/Catamarca", None, "America/Cayenne", None, "America/Cayman", None, "America/Chicago", None, "America/Chihuahua", None, "America/Ciudad_Juarez", None, "America/Coral_Harbour", None, "America/Cordoba", None, "America/Costa_Rica", None, "America/Coyhaique", None, "America/Creston", None, "America/Cuiaba", None, "America/Curacao", None, "America/Danmarkshavn", None, "America/Dawson", None, "America/Dawson_Creek", None, "America/Denver", None, "America/Detroit", None, "America/Dominica", None, "America/Edmonton", None, "America/Eirunepe", None, "America/El_Salvador", None, "America/Ensenada", None, "America/Fort_Nelson", None, "America/Fort_Wayne", None, "America/Fortaleza", None, "America/Glace_Bay", None, "America/Godthab", None, "America/Goose_Bay", None, "America/Grand_Turk", None, "America/Grenada", None, "America/Guadeloupe", None, "America/Guatemala", None, "America/Guayaquil", None, "America/Guyana", None, "America/Halifax", None, "America/Havana", None, "America/Hermosillo", None, "America/Indiana/Indianapolis", None, "America/Indiana/Knox", None, "America/Indiana/Marengo", None, "America/Indiana/Petersburg", None, "America/Indiana/Tell_City", None, "America/Indiana/Vevay", None, "America/Indiana/Vincennes", None, "America/Indiana/Winamac", None, "America/Indianapolis", None, "America/Inuvik", None, "America/Iqaluit", None, "America/Jamaica", None, "America/Jujuy", None, "America/Juneau", None, "America/Kentucky/Louisville", None, "America/Kentucky/Monticello", None, "America/Knox_IN", None, "America/Kralendijk", None, "America/La_Paz", None, "America/Lima", None, "America/Los_Angeles", None, "America/Louisville", None, "America/Lower_Princes", None, "America/Maceio", None, "America/Managua", None, "America/Manaus", None, "America/Marigot", None, "America/Martinique", None, "America/Matamoros", None, "America/Mazatlan", None, "America/Mendoza", None, "America/Menominee", None, "America/Merida", None, "America/Metlakatla", None, "America/Mexico_City", None, "America/Miquelon", None, "America/Moncton", None, "America/Monterrey", None, "America/Montevideo", None, "America/Montreal", None, "America/Montserrat", None, "America/Nassau", None, "America/New_York", None, "America/Nipigon", None, "America/Nome", None, "America/Noronha", None, "America/North_Dakota/Beulah", None, "America/North_Dakota/Center", None, "America/North_Dakota/New_Salem", None, "America/Nuuk", None, "America/Ojinaga", None, "America/Panama", None, "America/Pangnirtung", None, "America/Paramaribo", None, "America/Phoenix", None, "America/Port-au-Prince", None, "America/Port_of_Spain", None, "America/Porto_Acre", None, "America/Porto_Velho", None, "America/Puerto_Rico", None, "America/Punta_Arenas", None, "America/Rainy_River", None, "America/Rankin_Inlet", None, "America/Recife", None, "America/Regina", None, "America/Resolute", None, "America/Rio_Branco", None, "America/Rosario", None, "America/Santa_Isabel", None, "America/Santarem", None, "America/Santiago", None, "America/Santo_Domingo", None, "America/Sao_Paulo", None, "America/Scoresbysund", None, "America/Shiprock", None, "America/Sitka", None, "America/St_Barthelemy", None, "America/St_Johns", None, "America/St_Kitts", None, "America/St_Lucia", None, "America/St_Thomas", None, "America/St_Vincent", None, "America/Swift_Current", None, "America/Tegucigalpa", None, "America/Thule", None, "America/Thunder_Bay", None, "America/Tijuana", None, "America/Toronto", None, "America/Tortola", None, "America/Vancouver", None, "America/Virgin", None, "America/Whitehorse", None, "America/Winnipeg", None, "America/Yakutat", None, "America/Yellowknife", None, "Antarctica/Casey", None, "Antarctica/Davis", None, "Antarctica/DumontDUrville", None, "Antarctica/Macquarie", None, "Antarctica/Mawson", None, "Antarctica/McMurdo", None, "Antarctica/Palmer", None, "Antarctica/Rothera", None, "Antarctica/South_Pole", None, "Antarctica/Syowa", None, "Antarctica/Troll", None, "Antarctica/Vostok", None, "Arctic/Longyearbyen", None, "Asia/Aden", None, "Asia/Almaty", None, "Asia/Amman", None, "Asia/Anadyr", None, "Asia/Aqtau", None, "Asia/Aqtobe", None, "Asia/Ashgabat", None, "Asia/Ashkhabad", None, "Asia/Atyrau", None, "Asia/Baghdad", None, "Asia/Bahrain", None, "Asia/Baku", None, "Asia/Bangkok", None, "Asia/Barnaul", None, "Asia/Beirut", None, "Asia/Bishkek", None, "Asia/Brunei", None, "Asia/Calcutta", None, "Asia/Chita", None, "Asia/Choibalsan", None, "Asia/Chongqing", None, "Asia/Chungking", None, "Asia/Colombo", None, "Asia/Dacca", None, "Asia/Damascus", None, "Asia/Dhaka", None, "Asia/Dili", None, "Asia/Dubai", None, "Asia/Dushanbe", None, "Asia/Famagusta", None, "Asia/Gaza", None, "Asia/Harbin", None, "Asia/Hebron", None, "Asia/Ho_Chi_Minh", None, "Asia/Hong_Kong", None, "Asia/Hovd", None, "Asia/Irkutsk", None, "Asia/Istanbul", None, "Asia/Jakarta", None, "Asia/Jayapura", None, "Asia/Jerusalem", None, "Asia/Kabul", None, "Asia/Kamchatka", None, "Asia/Karachi", None, "Asia/Kashgar", None, "Asia/Kathmandu", None, "Asia/Katmandu", None, "Asia/Khandyga", None, "Asia/Kolkata", None, "Asia/Krasnoyarsk", None, "Asia/Kuala_Lumpur", None, "Asia/Kuching", None, "Asia/Kuwait", None, "Asia/Macao", None, "Asia/Macau", None, "Asia/Magadan", None, "Asia/Makassar", None, "Asia/Manila", None, "Asia/Muscat", None, "Asia/Nicosia", None, "Asia/Novokuznetsk", None, "Asia/Novosibirsk", None, "Asia/Omsk", None, "Asia/Oral", None, "Asia/Phnom_Penh", None, "Asia/Pontianak", None, "Asia/Pyongyang", None, "Asia/Qatar", None, "Asia/Qostanay", None, "Asia/Qyzylorda", None, "Asia/Rangoon", None, "Asia/Riyadh", None, "Asia/Saigon", None, "Asia/Sakhalin", None, "Asia/Samarkand", None, "Asia/Seoul", None, "Asia/Shanghai", None, "Asia/Singapore", None, "Asia/Srednekolymsk", None, "Asia/Taipei", None, "Asia/Tashkent", None, "Asia/Tbilisi", None, "Asia/Tehran", None, "Asia/Tel_Aviv", None, "Asia/Thimbu", None, "Asia/Thimphu", None, "Asia/Tokyo", None, "Asia/Tomsk", None, "Asia/Ujung_Pandang", None, "Asia/Ulaanbaatar", None, "Asia/Ulan_Bator", None, "Asia/Urumqi", None, "Asia/Ust-Nera", None, "Asia/Vientiane", None, "Asia/Vladivostok", None, "Asia/Yakutsk", None, "Asia/Yangon", None, "Asia/Yekaterinburg", None, "Asia/Yerevan", None, "Atlantic/Azores", None, "Atlantic/Bermuda", None, "Atlantic/Canary", None, "Atlantic/Cape_Verde", None, "Atlantic/Faeroe", None, "Atlantic/Faroe", None, "Atlantic/Jan_Mayen", None, "Atlantic/Madeira", None, "Atlantic/Reykjavik", None, "Atlantic/South_Georgia", None, "Atlantic/St_Helena", None, "Atlantic/Stanley", None, "Australia/ACT", None, "Australia/Adelaide", None, "Australia/Brisbane", None, "Australia/Broken_Hill", None, "Australia/Canberra", None, "Australia/Currie", None, "Australia/Darwin", None, "Australia/Eucla", None, "Australia/Hobart", None, "Australia/LHI", None, "Australia/Lindeman", None, "Australia/Lord_Howe", None, "Australia/Melbourne", None, "Australia/NSW", None, "Australia/North", None, "Australia/Perth", None, "Australia/Queensland", None, "Australia/South", None, "Australia/Sydney", None, "Australia/Tasmania", None, "Australia/Victoria", None, "Australia/West", None, "Australia/Yancowinna", None, "Brazil/Acre", None, "Brazil/DeNoronha", None, "Brazil/East", None, "Brazil/West", None, "CET", None, "CST6CDT", None, "Canada/Atlantic", None, "Canada/Central", None, "Canada/Eastern", None, "Canada/Mountain", None, "Canada/Newfoundland", None, "Canada/Pacific", None, "Canada/Saskatchewan", None, "Canada/Yukon", None, "Chile/Continental", None, "Chile/EasterIsland", None, "Cuba", None, "EET", None, "EST", None, "EST5EDT", None, "Egypt", None, "Eire", None, "Etc/GMT", None, "Etc/GMT+0", None, "Etc/GMT+1", None, "Etc/GMT+10", None, "Etc/GMT+11", None, "Etc/GMT+12", None, "Etc/GMT+2", None, "Etc/GMT+3", None, "Etc/GMT+4", None, "Etc/GMT+5", None, "Etc/GMT+6", None, "Etc/GMT+7", None, "Etc/GMT+8", None, "Etc/GMT+9", None, "Etc/GMT-0", None, "Etc/GMT-1", None, "Etc/GMT-10", None, "Etc/GMT-11", None, "Etc/GMT-12", None, "Etc/GMT-13", None, "Etc/GMT-14", None, "Etc/GMT-2", None, "Etc/GMT-3", None, "Etc/GMT-4", None, "Etc/GMT-5", None, "Etc/GMT-6", None, "Etc/GMT-7", None, "Etc/GMT-8", None, "Etc/GMT-9", None, "Etc/GMT0", None, "Etc/Greenwich", None, "Etc/UCT", None, "Etc/UTC", None, "Etc/Universal", None, "Etc/Zulu", None, "Europe/Amsterdam", None, "Europe/Andorra", None, "Europe/Astrakhan", None, "Europe/Athens", None, "Europe/Belfast", None, "Europe/Belgrade", None, "Europe/Berlin", None, "Europe/Bratislava", None, "Europe/Brussels", None, "Europe/Bucharest", None, "Europe/Budapest", None, "Europe/Busingen", None, "Europe/Chisinau", None, "Europe/Copenhagen", None, "Europe/Dublin", None, "Europe/Gibraltar", None, "Europe/Guernsey", None, "Europe/Helsinki", None, "Europe/Isle_of_Man", None, "Europe/Istanbul", None, "Europe/Jersey", None, "Europe/Kaliningrad", None, "Europe/Kiev", None, "Europe/Kirov", None, "Europe/Kyiv", None, "Europe/Lisbon", None, "Europe/Ljubljana", None, "Europe/London", None, "Europe/Luxembourg", None, "Europe/Madrid", None, "Europe/Malta", None, "Europe/Mariehamn", None, "Europe/Minsk", None, "Europe/Monaco", None, "Europe/Moscow", None, "Europe/Nicosia", None, "Europe/Oslo", None, "Europe/Paris", None, "Europe/Podgorica", None, "Europe/Prague", None, "Europe/Riga", None, "Europe/Rome", None, "Europe/Samara", None, "Europe/San_Marino", None, "Europe/Sarajevo", None, "Europe/Saratov", None, "Europe/Simferopol", None, "Europe/Skopje", None, "Europe/Sofia", None, "Europe/Stockholm", None, "Europe/Tallinn", None, "Europe/Tirane", None, "Europe/Tiraspol", None, "Europe/Ulyanovsk", None, "Europe/Uzhgorod", None, "Europe/Vaduz", None, "Europe/Vatican", None, "Europe/Vienna", None, "Europe/Vilnius", None, "Europe/Volgograd", None, "Europe/Warsaw", None, "Europe/Zagreb", None, "Europe/Zaporozhye", None, "Europe/Zurich", None, "Factory", None, "GB", None, "GB-Eire", None, "GMT", None, "GMT+0", None, "GMT-0", None, "GMT0", None, "Greenwich", None, "HST", None, "Hongkong", None, "Iceland", None, "Indian/Antananarivo", None, "Indian/Chagos", None, "Indian/Christmas", None, "Indian/Cocos", None, "Indian/Comoro", None, "Indian/Kerguelen", None, "Indian/Mahe", None, "Indian/Maldives", None, "Indian/Mauritius", None, "Indian/Mayotte", None, "Indian/Reunion", None, "Iran", None, "Israel", None, "Jamaica", None, "Japan", None, "Kwajalein", None, "Libya", None, "MET", None, "MST", None, "MST7MDT", None, "Mexico/BajaNorte", None, "Mexico/BajaSur", None, "Mexico/General", None, "NZ", None, "NZ-CHAT", None, "Navajo", None, "PRC", None, "PST8PDT", None, "Pacific/Apia", None, "Pacific/Auckland", None, "Pacific/Bougainville", None, "Pacific/Chatham", None, "Pacific/Chuuk", None, "Pacific/Easter", None, "Pacific/Efate", None, "Pacific/Enderbury", None, "Pacific/Fakaofo", None, "Pacific/Fiji", None, "Pacific/Funafuti", None, "Pacific/Galapagos", None, "Pacific/Gambier", None, "Pacific/Guadalcanal", None, "Pacific/Guam", None, "Pacific/Honolulu", None, "Pacific/Johnston", None, "Pacific/Kanton", None, "Pacific/Kiritimati", None, "Pacific/Kosrae", None, "Pacific/Kwajalein", None, "Pacific/Majuro", None, "Pacific/Marquesas", None, "Pacific/Midway", None, "Pacific/Nauru", None, "Pacific/Niue", None, "Pacific/Norfolk", None, "Pacific/Noumea", None, "Pacific/Pago_Pago", None, "Pacific/Palau", None, "Pacific/Pitcairn", None, "Pacific/Pohnpei", None, "Pacific/Ponape", None, "Pacific/Port_Moresby", None, "Pacific/Rarotonga", None, "Pacific/Saipan", None, "Pacific/Samoa", None, "Pacific/Tahiti", None, "Pacific/Tarawa", None, "Pacific/Tongatapu", None, "Pacific/Truk", None, "Pacific/Wake", None, "Pacific/Wallis", None, "Pacific/Yap", None, "Poland", None, "Portugal", None, "ROC", None, "ROK", None, "Singapore", None, "Turkey", None, "UCT", None, "US/Alaska", None, "US/Aleutian", None, "US/Arizona", None, "US/Central", None, "US/East-Indiana", None, "US/Eastern", None, "US/Hawaii", None, "US/Indiana-Starke", None, "US/Michigan", None, "US/Mountain", None, "US/Pacific", None, "US/Samoa", None, "Universal", None, "W-SU", None, "WET", None, "Zulu", None)
        self.mapped[9].resolve_generated_offsets("sw", "ne")
        self.mapped[12].resolve_generated_offset_with_values("year", 0, "month", 1, "day", 2, "hour", 3, "minute", 4, "second", 5, "microsecond", 6)
        self.mapped[18].resolve_generated_offsets("t", "v")
        self.mapped[19].resolve_generated_offsets("size", "from", "to")
        self.mapped[20].resolve_generated_offset_with_values("asc", None, "desc", None)
        self.mapped[22].static_values = [float.fromhex("0x1.5bf0a8b145769p+1"), float.fromhex("0x1.71547652b82fep+0"), float.fromhex("0x1.bcb7b1526e50ep-2"), float.fromhex("0x1.62e42fefa39efp-1"), float.fromhex("0x1.26bb1bbb55516p+1"), float.fromhex("0x1.921fb54442d18p+1"), float.fromhex("0x1.921fb54442d18p+0"), float.fromhex("0x1.921fb54442d18p-1"), float.fromhex("0x1.45f306dc9c883p-2"), float.fromhex("0x1.45f306dc9c883p-1"), float.fromhex("0x1.20dd750429b6dp+0"), float.fromhex("0x1.6a09e667f3bcdp+0"), float.fromhex("0x1.6a09e667f3bcdp-1")]
        self.mapped[24].resolve_generated_offset_with_values("fixed", 0, "fixed_reg", 1, "adaptative", 2, "dense", 3)
        self.mapped[25].static_values = [greycat.create_geo(float.fromhex("-0x1.54345b1903bbap+6"), float.fromhex("-0x1.67fffffe98p+7")), greycat.create_geo(float.fromhex("0x1.54345b1903bbap+6"), float.fromhex("0x1.67fffffe98p+7"))]
        self.mapped[27].resolve_generated_offsets("message", "stack")
        self.mapped[28].resolve_generated_offsets("n", "req_time")
        self.mapped[31].resolve_generated_offset_with_values("microseconds", 1, "milliseconds", 1000, "seconds", 1000000, "minutes", 60000000, "hours", 3600000000, "days", 86400000000)
        self.mapped[32].resolve_generated_offsets("column", "extractors")
        self.mapped[33].resolve_generated_offset_with_values("i32", 4, "i64", 8, "f32", 4, "f64", 8, "c64", 8, "c128", 16)
        self.mapped[34].resolve_generated_offsets("x", "y")
        self.mapped[35].static_values = [greycat.create_time(-9223372036854775808), greycat.create_time(9223372036854775807)]
        self.mapped[36].resolve_generated_offsets("module", "function", "line", "column")
        self.mapped[38].resolve_generated_offsets("points")
        self.mapped[39].resolve_generated_offset_with_values("p1", float.fromhex("0x1p+0"), "p10", float.fromhex("0x1.999999999999ap-4"), "p100", float.fromhex("0x1.47ae147ae147bp-7"), "p1000", float.fromhex("0x1.0624dd2f1a9fcp-10"), "p10000", float.fromhex("0x1.a36e2eb1c432dp-14"), "p100000", float.fromhex("0x1.4f8b588e368f1p-17"), "p1000000", float.fromhex("0x1.0c6f7a0b5ed8dp-20"), "p10000000", float.fromhex("0x1.ad7f29abcaf48p-24"), "p100000000", float.fromhex("0x1.5798ee2308c3ap-27"), "p1000000000", float.fromhex("0x1.12e0be826d695p-30"), "p10000000000", float.fromhex("0x1.b7cdfd9d7bdbbp-34"))
        self.mapped[41].resolve_generated_offsets("year", "month", "day", "hour", "minute", "second", "microsecond")
        self.mapped[44].resolve_generated_offset_with_values("none", 0, "plain", 1, "login", 2)
        self.mapped[45].resolve_generated_offsets("protocol", "host", "port", "path", "params", "hash")
        self.mapped[46].resolve_generated_offsets("path", "size", "last_modification")
        self.mapped[47].resolve_generated_offsets("header_lines", "separator", "string_delimiter", "decimal_separator", "thousands_separator", "row_limit", "enumerable_limit", "date_check_limit", "date_formats")
        self.mapped[47].static_values = [100, 100]
        self.mapped[48].resolve_generated_offsets("path", "append")
        self.mapped[49].resolve_generated_offsets("path", "append")
        self.mapped[50].resolve_generated_offsets("path", "append")
        self.mapped[51].resolve_generated_offsets("path", "pos")
        self.mapped[52].resolve_generated_offset_with_values("plain", 0, "ssl_tls", 1, "starttls", 2)
        self.mapped[53].resolve_generated_offsets("name", "example", "null_count", "bool_count", "int_count", "float_count", "string_count", "date_count", "date_format_count", "enumerable_count", "profile")
        self.mapped[54].resolve_generated_offsets("header_lines", "separator", "string_delimiter", "decimal_separator", "thousands_separator", "trim", "format", "tz", "strict", "nearest_time")
        self.mapped[55].resolve_generated_offsets("id", "column", "modulo")
        self.mapped[56].resolve_generated_offsets("from", "subject", "body", "body_is_html", "to", "cc", "bcc")
        self.mapped[57].resolve_generated_offsets("path", "pos", "format", "sharding")
        self.mapped[58].resolve_generated_offsets("path", "pos")
        self.mapped[60].resolve_generated_offsets("path", "append", "format")
        self.mapped[61].resolve_generated_offsets("path", "pos")
        self.mapped[62].resolve_generated_offsets("header_lines", "separator", "string_delimiter", "decimal_separator", "thousands_separator", "columns", "line_count", "fail_count", "file_count")
        self.mapped[63].resolve_generated_offsets("path", "append")
        self.mapped[64].resolve_generated_offsets("path", "pos")
        self.mapped[67].resolve_generated_offsets("host", "port", "mode", "authenticate", "user", "pass")
        self.mapped[68].resolve_generated_offsets("path")
        self.mapped[69].resolve_generated_offsets("name", "value")
        self.mapped[70].resolve_generated_offset_with_values("error", None, "warn", None, "info", None, "perf", None, "trace", None)
        self.mapped[71].resolve_generated_offsets("version", "program_version", "arch", "timezone", "license", "io_threads", "bg_threads", "fg_threads", "mem_total", "mem_worker", "disk_data_bytes")
        self.mapped[72].resolve_generated_offsets("id", "name", "activated")
        self.mapped[73].resolve_generated_offsets("id", "frames", "root")
        self.mapped[74].resolve_generated_offsets("name", "permissions")
        self.mapped[75].resolve_generated_offsets("level", "time", "user_id", "id", "id2", "src", "tag", "data")
        self.mapped[76].resolve_generated_offsets("name", "value")
        self.mapped[77].resolve_generated_offsets("url", "clientId")
        self.mapped[78].resolve_generated_offsets("name", "start", "end", "company", "max_memory", "extra_1", "extra_2", "type")
        self.mapped[79].resolve_generated_offsets("group_id", "type")
        self.mapped[80].resolve_generated_offsets("id", "name", "activated", "full_name", "email", "role", "groups", "groups_flags", "external")
        self.mapped[81].resolve_generated_offsets("function", "arguments")
        self.mapped[82].resolve_generated_offsets("email", "name", "first_name", "last_name", "roles", "groups")
        self.mapped[83].resolve_generated_offset_with_values("empty", None, "waiting", None, "running", None, "await", None, "cancelled", None, "error", None, "ended", None, "ended_with_errors", None)
        self.mapped[84].resolve_generated_offset_with_values("community", None, "enterprise", None, "testing", None)
        self.mapped[85].resolve_generated_offsets("module", "type", "function", "src", "line", "column", "scope")
        self.mapped[86].resolve_generated_offsets("id", "name", "activated")
        self.mapped[87].resolve_generated_offsets("duration", "bytes_write_disk", "bytes_write_disk_raw", "bytes_read_disk", "bytes_read_disk_raw", "bytes_read_cache")
        self.mapped[88].resolve_generated_offsets("entities", "credentials", "fields", "keys", "keys_last_refresh")
        self.mapped[90].resolve_generated_offsets("function", "user_id", "arguments", "start", "every")
        self.mapped[91].resolve_generated_offset_with_values("read", None, "write", None, "execute", None)
        self.mapped[93].resolve_generated_offsets("offset", "pass")
        self.mapped[94].resolve_generated_offsets("name", "description")
        self.mapped[95].resolve_generated_offsets("user_id", "task_id", "mod", "type", "fun", "creation", "start", "duration", "status", "progress")
        self.mapped[96].resolve_generated_offsets("min", "max", "bins", "open")
        self.mapped[97].resolve_generated_offsets("sum", "sumsq", "count", "min", "max")
        self.mapped[98].resolve_generated_offsets("values")
        self.mapped[99].resolve_generated_offsets("quantizer", "precision", "bins", "value_min", "nb_rejected")
        self.mapped[100].resolve_generated_offsets("start", "total", "counter", "duration", "progress", "speed", "remaining")
        self.mapped[102].resolve_generated_offsets("quantizers")
        self.mapped[103].resolve_generated_offsets("min", "max", "whisker_low", "whisker_high", "percentile1", "percentile5", "percentile10", "percentile20", "percentile25", "percentile50", "percentile75", "percentile80", "percentile90", "percentile95", "percentile99", "sum", "avg", "std", "size")
        self.mapped[105].resolve_generated_offsets("values", "span", "sum", "sumsq", "field")
        self.mapped[107].resolve_generated_offsets("min", "max", "bins", "open")
        self.mapped[108].resolve_generated_offsets("min", "max", "center")
        self.mapped[109].resolve_generated_offsets("sum", "sumsq", "count")
        self.mapped[110].resolve_generated_offsets("values", "span", "sum", "sumsq", "field")
        self.mapped[111].resolve_generated_offsets("bin", "count", "ratio", "cumulative_count", "cumulative_ratio")
        self.mapped[112].resolve_generated_offsets("seed", "v")
        self.mapped[113].resolve_generated_offsets("min", "max", "step_starts", "open")
        self.mapped[114].resolve_generated_offsets("quantizer", "bins", "nb_rejected", "nb_accepted", "min", "max", "sum", "sumsq")
        self.mapped[116].resolve_generated_offsets("values", "capacity")
