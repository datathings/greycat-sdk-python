# AUTO-GENERATED FILE PLEASE DO NOT MODIFY MANUALLY
from __future__ import annotations
from ctypes import *
from typing import *
from ai.greycat.greycat import GreyCat
from ai.greycat.std_n import std_n
_T = TypeVar("_T")
_K = TypeVar("_K")
_V = TypeVar("_V")
_U = TypeVar("_U")
@final
class std(GreyCat.Library):
	name_: Final[str] = "std"
	def name(self) -> str:
		return self.name_
	@final
	class core:
		@final
		class tf2d(std_n.core._tf2d):
			name_: Final[str] = "core::tf2d"
			def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
				super().__init__(type)
			@staticmethod
			def create(greycat: GreyCat) -> std_n.core._tf2d:
				return std.core.tf2d(greycat.libs_by_name[std.name_].mapped[0])
		@final
		class SamplingMode(GreyCat.Enum):
			name_: Final[str] = "core::SamplingMode"
			def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
				super().__init__(type, attributes)
			@staticmethod
			def fixed(greycat: GreyCat) -> std_.core.SamplingMode:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[1]
				return t.enum_values[t.generated_offsets[0]]
			@staticmethod
			def fixed_reg(greycat: GreyCat) -> std_.core.SamplingMode:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[1]
				return t.enum_values[t.generated_offsets[1]]
			@staticmethod
			def adaptative(greycat: GreyCat) -> std_.core.SamplingMode:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[1]
				return t.enum_values[t.generated_offsets[2]]
			@staticmethod
			def dense(greycat: GreyCat) -> std_.core.SamplingMode:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[1]
				return t.enum_values[t.generated_offsets[3]]
			@staticmethod
			def create(greycat: GreyCat) -> std_.core.SamplingMode:
				return std_.core.SamplingMode(greycat.libs_by_name[std.name_].mapped[1])
		@final
		class Table(Generic[_T], std_n.core._Table[_T]):
			name_: Final[str] = "core::Table"
			def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
				super().__init__(type)
			@staticmethod
			def create(greycat: GreyCat) -> std_n.core._Table:
				return std.core.Table(greycat.libs_by_name[std.name_].mapped[2])
		@final
		class ti6d(std_n.core._ti6d):
			name_: Final[str] = "core::ti6d"
			def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
				super().__init__(type)
			@staticmethod
			def create(greycat: GreyCat) -> std_n.core._ti6d:
				return std.core.ti6d(greycat.libs_by_name[std.name_].mapped[3])
		@final
		class nodeTimeSingleton(GreyCat.Object):
			name_: Final[str] = "core::nodeTimeSingleton"
			def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
				super().__init__(type, attributes)
			def t(self) -> std.core.time:
				return self._get(self.type_.generated_offsets[0])
			def set_t(self, v: std.core.time) -> None:
				self._set(self.type_.generated_offsets[0],v)
			def v(self) -> Any:
				return self._get(self.type_.generated_offsets[1])
			def set_v(self, v: Any) -> None:
				self._set(self.type_.generated_offsets[1],v)
			@staticmethod
			def create(greycat: GreyCat, t: std.core.time, v: Any) -> std_.core.nodeTimeSingleton:
				return std_.core.nodeTimeSingleton(greycat.libs_by_name[std.name_].mapped[4], t, v)
		@final
		class time(std_n.core._time):
			name_: Final[str] = "core::time"
			def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
				super().__init__(type)
			@staticmethod
			def create(greycat: GreyCat) -> std_n.core._time:
				return std.core.time(greycat.libs_by_name[std.name_].mapped[5])
		@final
		class nodeTime(Generic[_T], std_n.core._nodeTime[_T]):
			name_: Final[str] = "core::nodeTime"
			def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
				super().__init__(type)
			@staticmethod
			def create(greycat: GreyCat) -> std_n.core._nodeTime:
				return std.core.nodeTime(greycat.libs_by_name[std.name_].mapped[6])
		@final
		class DurationUnit(GreyCat.Enum):
			name_: Final[str] = "core::DurationUnit"
			def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
				super().__init__(type, attributes)
			@staticmethod
			def microseconds(greycat: GreyCat) -> std_.core.DurationUnit:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[7]
				return t.enum_values[t.generated_offsets[0]]
			@staticmethod
			def milliseconds(greycat: GreyCat) -> std_.core.DurationUnit:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[7]
				return t.enum_values[t.generated_offsets[1]]
			@staticmethod
			def seconds(greycat: GreyCat) -> std_.core.DurationUnit:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[7]
				return t.enum_values[t.generated_offsets[2]]
			@staticmethod
			def minutes(greycat: GreyCat) -> std_.core.DurationUnit:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[7]
				return t.enum_values[t.generated_offsets[3]]
			@staticmethod
			def hours(greycat: GreyCat) -> std_.core.DurationUnit:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[7]
				return t.enum_values[t.generated_offsets[4]]
			@staticmethod
			def days(greycat: GreyCat) -> std_.core.DurationUnit:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[7]
				return t.enum_values[t.generated_offsets[5]]
			@staticmethod
			def weeks(greycat: GreyCat) -> std_.core.DurationUnit:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[7]
				return t.enum_values[t.generated_offsets[6]]
			@staticmethod
			def months(greycat: GreyCat) -> std_.core.DurationUnit:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[7]
				return t.enum_values[t.generated_offsets[7]]
			@staticmethod
			def years(greycat: GreyCat) -> std_.core.DurationUnit:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[7]
				return t.enum_values[t.generated_offsets[8]]
			@staticmethod
			def create(greycat: GreyCat) -> std_.core.DurationUnit:
				return std_.core.DurationUnit(greycat.libs_by_name[std.name_].mapped[7])
		@final
		class NodeTimeInfo(GreyCat.Object):
			name_: Final[str] = "core::NodeTimeInfo"
			def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
				super().__init__(type, attributes)
			def size(self) -> int:
				return self._get(self.type_.generated_offsets[0])
			def set_size(self, v: int) -> None:
				self._set(self.type_.generated_offsets[0],v)
			def from_(self) -> std.core.time:
				return self._get(self.type_.generated_offsets[1])
			def set_from(self, v: std.core.time) -> None:
				self._set(self.type_.generated_offsets[1],v)
			def to(self) -> std.core.time:
				return self._get(self.type_.generated_offsets[2])
			def set_to(self, v: std.core.time) -> None:
				self._set(self.type_.generated_offsets[2],v)
			@staticmethod
			def create(greycat: GreyCat, size: int, from_: std.core.time, to: std.core.time) -> std_.core.NodeTimeInfo:
				return std_.core.NodeTimeInfo(greycat.libs_by_name[std.name_].mapped[8], size, from_, to)
		@final
		class function(std_n.core._function):
			name_: Final[str] = "core::function"
			def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
				super().__init__(type)
			@staticmethod
			def create(greycat: GreyCat) -> std_n.core._function:
				return std.core.function(greycat.libs_by_name[std.name_].mapped[9])
		@final
		class Error(std_n.core._Error):
			name_: Final[str] = "core::Error"
			def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
				super().__init__(type)
			@staticmethod
			def create(greycat: GreyCat) -> std_n.core._Error:
				return std.core.Error(greycat.libs_by_name[std.name_].mapped[10])
		@final
		class GeoPoly(GreyCat.Object):
			name_: Final[str] = "core::GeoPoly"
			def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
				super().__init__(type, attributes)
			def points(self) -> std_.core.Array:
				return self._get(self.type_.generated_offsets[0])
			def set_points(self, v: std_.core.Array) -> None:
				self._set(self.type_.generated_offsets[0],v)
			@staticmethod
			def create(greycat: GreyCat, points: std_.core.Array) -> std_.core.GeoPoly:
				return std_.core.GeoPoly(greycat.libs_by_name[std.name_].mapped[11], points)
		@final
		class duration(std_n.core._duration):
			name_: Final[str] = "core::duration"
			def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
				super().__init__(type)
			@staticmethod
			def create(greycat: GreyCat) -> std_n.core._duration:
				return std.core.duration(greycat.libs_by_name[std.name_].mapped[12])
		@final
		class ti2d(std_n.core._ti2d):
			name_: Final[str] = "core::ti2d"
			def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
				super().__init__(type)
			@staticmethod
			def create(greycat: GreyCat) -> std_n.core._ti2d:
				return std.core.ti2d(greycat.libs_by_name[std.name_].mapped[13])
		@final
		class ErrorCode(GreyCat.Enum):
			name_: Final[str] = "core::ErrorCode"
			def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
				super().__init__(type, attributes)
			@staticmethod
			def none(greycat: GreyCat) -> std_.core.ErrorCode:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[14]
				return t.enum_values[t.generated_offsets[0]]
			@staticmethod
			def too_deep_workspace(greycat: GreyCat) -> std_.core.ErrorCode:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[14]
				return t.enum_values[t.generated_offsets[1]]
			@staticmethod
			def too_deep_iterator(greycat: GreyCat) -> std_.core.ErrorCode:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[14]
				return t.enum_values[t.generated_offsets[2]]
			@staticmethod
			def wrong_operand(greycat: GreyCat) -> std_.core.ErrorCode:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[14]
				return t.enum_values[t.generated_offsets[3]]
			@staticmethod
			def wrong_params(greycat: GreyCat) -> std_.core.ErrorCode:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[14]
				return t.enum_values[t.generated_offsets[4]]
			@staticmethod
			def wrong_param_type(greycat: GreyCat) -> std_.core.ErrorCode:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[14]
				return t.enum_values[t.generated_offsets[5]]
			@staticmethod
			def wrong_numeric(greycat: GreyCat) -> std_.core.ErrorCode:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[14]
				return t.enum_values[t.generated_offsets[6]]
			@staticmethod
			def wrong_state(greycat: GreyCat) -> std_.core.ErrorCode:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[14]
				return t.enum_values[t.generated_offsets[7]]
			@staticmethod
			def wrong_null(greycat: GreyCat) -> std_.core.ErrorCode:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[14]
				return t.enum_values[t.generated_offsets[8]]
			@staticmethod
			def unresolved_ref(greycat: GreyCat) -> std_.core.ErrorCode:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[14]
				return t.enum_values[t.generated_offsets[9]]
			@staticmethod
			def assign_error(greycat: GreyCat) -> std_.core.ErrorCode:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[14]
				return t.enum_values[t.generated_offsets[10]]
			@staticmethod
			def interrupted(greycat: GreyCat) -> std_.core.ErrorCode:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[14]
				return t.enum_values[t.generated_offsets[11]]
			@staticmethod
			def throw(greycat: GreyCat) -> std_.core.ErrorCode:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[14]
				return t.enum_values[t.generated_offsets[12]]
			@staticmethod
			def wrong_type(greycat: GreyCat) -> std_.core.ErrorCode:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[14]
				return t.enum_values[t.generated_offsets[13]]
			@staticmethod
			def wrong_dimension(greycat: GreyCat) -> std_.core.ErrorCode:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[14]
				return t.enum_values[t.generated_offsets[14]]
			@staticmethod
			def unsupported_operation(greycat: GreyCat) -> std_.core.ErrorCode:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[14]
				return t.enum_values[t.generated_offsets[15]]
			@staticmethod
			def unsupported_type(greycat: GreyCat) -> std_.core.ErrorCode:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[14]
				return t.enum_values[t.generated_offsets[16]]
			@staticmethod
			def dimensions_mismatch(greycat: GreyCat) -> std_.core.ErrorCode:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[14]
				return t.enum_values[t.generated_offsets[17]]
			@staticmethod
			def timeout(greycat: GreyCat) -> std_.core.ErrorCode:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[14]
				return t.enum_values[t.generated_offsets[18]]
			@staticmethod
			def forbidden(greycat: GreyCat) -> std_.core.ErrorCode:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[14]
				return t.enum_values[t.generated_offsets[19]]
			@staticmethod
			def runtime_error(greycat: GreyCat) -> std_.core.ErrorCode:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[14]
				return t.enum_values[t.generated_offsets[20]]
			@staticmethod
			def create(greycat: GreyCat) -> std_.core.ErrorCode:
				return std_.core.ErrorCode(greycat.libs_by_name[std.name_].mapped[14])
		@final
		class geo(std_n.core._geo):
			name_: Final[str] = "core::geo"
			def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
				super().__init__(type)
			@staticmethod
			def create(greycat: GreyCat) -> std_n.core._geo:
				return std.core.geo(greycat.libs_by_name[std.name_].mapped[15])
		@final
		class node(Generic[_T], std_n.core._node[_T]):
			name_: Final[str] = "core::node"
			def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
				super().__init__(type)
			@staticmethod
			def create(greycat: GreyCat) -> std_n.core._node:
				return std.core.node(greycat.libs_by_name[std.name_].mapped[16])
		@final
		class TableColumnMeta(GreyCat.Object):
			name_: Final[str] = "core::TableColumnMeta"
			def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
				super().__init__(type, attributes)
			def type(self) -> str:
				return self._get(self.type_.generated_offsets[0])
			def set_type(self, v: str) -> None:
				self._set(self.type_.generated_offsets[0],v)
			def size(self) -> int:
				return self._get(self.type_.generated_offsets[1])
			def set_size(self, v: int) -> None:
				self._set(self.type_.generated_offsets[1],v)
			def index(self) -> bool:
				return self._get(self.type_.generated_offsets[2])
			def set_index(self, v: bool) -> None:
				self._set(self.type_.generated_offsets[2],v)
			def min(self) -> Any:
				return self._get(self.type_.generated_offsets[3])
			def set_min(self, v: Any) -> None:
				self._set(self.type_.generated_offsets[3],v)
			def max(self) -> Any:
				return self._get(self.type_.generated_offsets[4])
			def set_max(self, v: Any) -> None:
				self._set(self.type_.generated_offsets[4],v)
			def avg(self) -> Any:
				return self._get(self.type_.generated_offsets[5])
			def set_avg(self, v: Any) -> None:
				self._set(self.type_.generated_offsets[5],v)
			def std(self) -> Any:
				return self._get(self.type_.generated_offsets[6])
			def set_std(self, v: Any) -> None:
				self._set(self.type_.generated_offsets[6],v)
			@staticmethod
			def create(greycat: GreyCat, type: str, size: int, index: bool, min: Any, max: Any, avg: Any, std: Any) -> std_.core.TableColumnMeta:
				return std_.core.TableColumnMeta(greycat.libs_by_name[std.name_].mapped[17], type, size, index, min, max, avg, std)
		@final
		class Date(std_n.core._Date):
			name_: Final[str] = "core::Date"
			def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
				super().__init__(type)
			@staticmethod
			def create(greycat: GreyCat) -> std_n.core._Date:
				return std.core.Date(greycat.libs_by_name[std.name_].mapped[18])
		@final
		class Tensor(std_n.core._Tensor):
			name_: Final[str] = "core::Tensor"
			def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
				super().__init__(type)
			@staticmethod
			def create(greycat: GreyCat) -> std_n.core._Tensor:
				return std.core.Tensor(greycat.libs_by_name[std.name_].mapped[19])
		@final
		class ti4d(std_n.core._ti4d):
			name_: Final[str] = "core::ti4d"
			def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
				super().__init__(type)
			@staticmethod
			def create(greycat: GreyCat) -> std_n.core._ti4d:
				return std.core.ti4d(greycat.libs_by_name[std.name_].mapped[20])
		@final
		class GeoCircle(GreyCat.Object):
			name_: Final[str] = "core::GeoCircle"
			def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
				super().__init__(type, attributes)
			def center(self) -> std.core.geo:
				return self._get(self.type_.generated_offsets[0])
			def set_center(self, v: std.core.geo) -> None:
				self._set(self.type_.generated_offsets[0],v)
			def radius(self) -> float:
				return self._get(self.type_.generated_offsets[1])
			def set_radius(self, v: float) -> None:
				self._set(self.type_.generated_offsets[1],v)
			@staticmethod
			def create(greycat: GreyCat, center: std.core.geo, radius: float) -> std_.core.GeoCircle:
				return std_.core.GeoCircle(greycat.libs_by_name[std.name_].mapped[21], center, radius)
		@final
		class nodeGeo(Generic[_T], std_n.core._nodeGeo[_T]):
			name_: Final[str] = "core::nodeGeo"
			def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
				super().__init__(type)
			@staticmethod
			def create(greycat: GreyCat) -> std_n.core._nodeGeo:
				return std.core.nodeGeo(greycat.libs_by_name[std.name_].mapped[22])
		@final
		class ti5d(std_n.core._ti5d):
			name_: Final[str] = "core::ti5d"
			def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
				super().__init__(type)
			@staticmethod
			def create(greycat: GreyCat) -> std_n.core._ti5d:
				return std.core.ti5d(greycat.libs_by_name[std.name_].mapped[23])
		@final
		class String(std_n.core._String):
			name_: Final[str] = "core::String"
			def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
				super().__init__(type)
			@staticmethod
			def create(greycat: GreyCat) -> std_n.core._String:
				return std.core.String(greycat.libs_by_name[std.name_].mapped[24])
		@final
		class Map(Generic[_K,_V], std_n.core._Map[_K,_V]):
			name_: Final[str] = "core::Map"
			def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
				super().__init__(type)
			@staticmethod
			def create(greycat: GreyCat) -> std_n.core._Map:
				return std.core.Map(greycat.libs_by_name[std.name_].mapped[25])
		@final
		class TensorType(GreyCat.Enum):
			name_: Final[str] = "core::TensorType"
			def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
				super().__init__(type, attributes)
			@staticmethod
			def i32(greycat: GreyCat) -> std_.core.TensorType:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[26]
				return t.enum_values[t.generated_offsets[0]]
			@staticmethod
			def i64(greycat: GreyCat) -> std_.core.TensorType:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[26]
				return t.enum_values[t.generated_offsets[1]]
			@staticmethod
			def f32(greycat: GreyCat) -> std_.core.TensorType:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[26]
				return t.enum_values[t.generated_offsets[2]]
			@staticmethod
			def f64(greycat: GreyCat) -> std_.core.TensorType:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[26]
				return t.enum_values[t.generated_offsets[3]]
			@staticmethod
			def c64(greycat: GreyCat) -> std_.core.TensorType:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[26]
				return t.enum_values[t.generated_offsets[4]]
			@staticmethod
			def c128(greycat: GreyCat) -> std_.core.TensorType:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[26]
				return t.enum_values[t.generated_offsets[5]]
			@staticmethod
			def create(greycat: GreyCat) -> std_.core.TensorType:
				return std_.core.TensorType(greycat.libs_by_name[std.name_].mapped[26])
		@final
		class TimeZone(GreyCat.Enum):
			name_: Final[str] = "core::TimeZone"
			def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
				super().__init__(type, attributes)
			@staticmethod
			def Africa_Accra(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[0]]
			@staticmethod
			def Africa_Bamako(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[1]]
			@staticmethod
			def Africa_Banjul(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[2]]
			@staticmethod
			def Africa_Conakry(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[3]]
			@staticmethod
			def Africa_Dakar(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[4]]
			@staticmethod
			def Africa_Freetown(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[5]]
			@staticmethod
			def Africa_Lome(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[6]]
			@staticmethod
			def Africa_Nouakchott(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[7]]
			@staticmethod
			def Africa_Ouagadougou(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[8]]
			@staticmethod
			def Africa_Timbuktu(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[9]]
			@staticmethod
			def Atlantic_Reykjavik(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[10]]
			@staticmethod
			def Atlantic_St_Helena(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[11]]
			@staticmethod
			def Iceland(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[12]]
			@staticmethod
			def Egypt(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[13]]
			@staticmethod
			def Africa_Maseru(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[14]]
			@staticmethod
			def Africa_Mbabane(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[15]]
			@staticmethod
			def Africa_Bangui(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[16]]
			@staticmethod
			def Africa_Brazzaville(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[17]]
			@staticmethod
			def Africa_Douala(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[18]]
			@staticmethod
			def Africa_Kinshasa(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[19]]
			@staticmethod
			def Africa_Libreville(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[20]]
			@staticmethod
			def Africa_Luanda(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[21]]
			@staticmethod
			def Africa_Malabo(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[22]]
			@staticmethod
			def Africa_Niamey(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[23]]
			@staticmethod
			def Africa_Porto_Novo(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[24]]
			@staticmethod
			def Africa_Blantyre(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[25]]
			@staticmethod
			def Africa_Bujumbura(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[26]]
			@staticmethod
			def Africa_Gaborone(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[27]]
			@staticmethod
			def Africa_Harare(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[28]]
			@staticmethod
			def Africa_Kigali(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[29]]
			@staticmethod
			def Africa_Lubumbashi(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[30]]
			@staticmethod
			def Africa_Lusaka(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[31]]
			@staticmethod
			def Africa_Addis_Ababa(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[32]]
			@staticmethod
			def Africa_Asmara(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[33]]
			@staticmethod
			def Africa_Asmera(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[34]]
			@staticmethod
			def Africa_Dar_es_Salaam(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[35]]
			@staticmethod
			def Africa_Djibouti(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[36]]
			@staticmethod
			def Africa_Kampala(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[37]]
			@staticmethod
			def Africa_Mogadishu(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[38]]
			@staticmethod
			def Indian_Antananarivo(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[39]]
			@staticmethod
			def Indian_Comoro(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[40]]
			@staticmethod
			def Indian_Mayotte(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[41]]
			@staticmethod
			def Libya(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[42]]
			@staticmethod
			def America_Atka(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[43]]
			@staticmethod
			def US_Aleutian(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[44]]
			@staticmethod
			def US_Alaska(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[45]]
			@staticmethod
			def America_Buenos_Aires(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[46]]
			@staticmethod
			def America_Argentina_ComodRivadavia(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[47]]
			@staticmethod
			def America_Catamarca(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[48]]
			@staticmethod
			def America_Cordoba(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[49]]
			@staticmethod
			def America_Rosario(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[50]]
			@staticmethod
			def America_Jujuy(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[51]]
			@staticmethod
			def America_Mendoza(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[52]]
			@staticmethod
			def US_Central(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[53]]
			@staticmethod
			def America_Shiprock(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[54]]
			@staticmethod
			def Navajo(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[55]]
			@staticmethod
			def US_Mountain(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[56]]
			@staticmethod
			def US_Michigan(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[57]]
			@staticmethod
			def America_Yellowknife(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[58]]
			@staticmethod
			def Canada_Mountain(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[59]]
			@staticmethod
			def Canada_Atlantic(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[60]]
			@staticmethod
			def Cuba(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[61]]
			@staticmethod
			def America_Fort_Wayne(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[62]]
			@staticmethod
			def America_Indianapolis(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[63]]
			@staticmethod
			def US_East_Indiana(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[64]]
			@staticmethod
			def America_Knox_IN(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[65]]
			@staticmethod
			def US_Indiana_Starke(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[66]]
			@staticmethod
			def America_Pangnirtung(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[67]]
			@staticmethod
			def Jamaica(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[68]]
			@staticmethod
			def America_Louisville(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[69]]
			@staticmethod
			def US_Pacific(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[70]]
			@staticmethod
			def Brazil_West(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[71]]
			@staticmethod
			def Mexico_BajaSur(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[72]]
			@staticmethod
			def Mexico_General(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[73]]
			@staticmethod
			def US_Eastern(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[74]]
			@staticmethod
			def Brazil_DeNoronha(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[75]]
			@staticmethod
			def America_Godthab(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[76]]
			@staticmethod
			def America_Atikokan(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[77]]
			@staticmethod
			def America_Cayman(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[78]]
			@staticmethod
			def America_Coral_Harbour(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[79]]
			@staticmethod
			def America_Creston(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[80]]
			@staticmethod
			def US_Arizona(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[81]]
			@staticmethod
			def America_Anguilla(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[82]]
			@staticmethod
			def America_Antigua(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[83]]
			@staticmethod
			def America_Aruba(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[84]]
			@staticmethod
			def America_Blanc_Sablon(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[85]]
			@staticmethod
			def America_Curacao(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[86]]
			@staticmethod
			def America_Dominica(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[87]]
			@staticmethod
			def America_Grenada(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[88]]
			@staticmethod
			def America_Guadeloupe(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[89]]
			@staticmethod
			def America_Kralendijk(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[90]]
			@staticmethod
			def America_Lower_Princes(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[91]]
			@staticmethod
			def America_Marigot(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[92]]
			@staticmethod
			def America_Montserrat(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[93]]
			@staticmethod
			def America_Port_of_Spain(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[94]]
			@staticmethod
			def America_St_Barthelemy(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[95]]
			@staticmethod
			def America_St_Kitts(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[96]]
			@staticmethod
			def America_St_Lucia(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[97]]
			@staticmethod
			def America_St_Thomas(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[98]]
			@staticmethod
			def America_St_Vincent(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[99]]
			@staticmethod
			def America_Tortola(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[100]]
			@staticmethod
			def America_Virgin(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[101]]
			@staticmethod
			def Canada_Saskatchewan(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[102]]
			@staticmethod
			def America_Porto_Acre(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[103]]
			@staticmethod
			def Brazil_Acre(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[104]]
			@staticmethod
			def Chile_Continental(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[105]]
			@staticmethod
			def Brazil_East(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[106]]
			@staticmethod
			def Canada_Newfoundland(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[107]]
			@staticmethod
			def America_Ensenada(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[108]]
			@staticmethod
			def America_Santa_Isabel(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[109]]
			@staticmethod
			def Mexico_BajaNorte(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[110]]
			@staticmethod
			def America_Montreal(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[111]]
			@staticmethod
			def America_Nassau(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[112]]
			@staticmethod
			def America_Nipigon(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[113]]
			@staticmethod
			def America_Thunder_Bay(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[114]]
			@staticmethod
			def Canada_Eastern(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[115]]
			@staticmethod
			def Canada_Pacific(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[116]]
			@staticmethod
			def Canada_Yukon(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[117]]
			@staticmethod
			def America_Rainy_River(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[118]]
			@staticmethod
			def Canada_Central(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[119]]
			@staticmethod
			def Asia_Ashkhabad(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[120]]
			@staticmethod
			def Asia_Phnom_Penh(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[121]]
			@staticmethod
			def Asia_Vientiane(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[122]]
			@staticmethod
			def Indian_Christmas(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[123]]
			@staticmethod
			def Asia_Dacca(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[124]]
			@staticmethod
			def Asia_Muscat(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[125]]
			@staticmethod
			def Indian_Mahe(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[126]]
			@staticmethod
			def Indian_Reunion(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[127]]
			@staticmethod
			def Asia_Saigon(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[128]]
			@staticmethod
			def Hongkong(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[129]]
			@staticmethod
			def Asia_Tel_Aviv(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[130]]
			@staticmethod
			def Israel(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[131]]
			@staticmethod
			def Asia_Katmandu(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[132]]
			@staticmethod
			def Asia_Calcutta(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[133]]
			@staticmethod
			def Asia_Brunei(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[134]]
			@staticmethod
			def Asia_Macao(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[135]]
			@staticmethod
			def Asia_Ujung_Pandang(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[136]]
			@staticmethod
			def Europe_Nicosia(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[137]]
			@staticmethod
			def Asia_Bahrain(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[138]]
			@staticmethod
			def Antarctica_Syowa(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[139]]
			@staticmethod
			def Asia_Aden(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[140]]
			@staticmethod
			def Asia_Kuwait(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[141]]
			@staticmethod
			def ROK(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[142]]
			@staticmethod
			def Asia_Chongqing(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[143]]
			@staticmethod
			def Asia_Chungking(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[144]]
			@staticmethod
			def Asia_Harbin(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[145]]
			@staticmethod
			def PRC(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[146]]
			@staticmethod
			def Asia_Kuala_Lumpur(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[147]]
			@staticmethod
			def Singapore(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[148]]
			@staticmethod
			def ROC(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[149]]
			@staticmethod
			def Iran(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[150]]
			@staticmethod
			def Asia_Thimbu(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[151]]
			@staticmethod
			def Japan(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[152]]
			@staticmethod
			def Asia_Ulan_Bator(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[153]]
			@staticmethod
			def Antarctica_Vostok(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[154]]
			@staticmethod
			def Asia_Kashgar(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[155]]
			@staticmethod
			def Asia_Rangoon(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[156]]
			@staticmethod
			def Indian_Cocos(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[157]]
			@staticmethod
			def Atlantic_Faeroe(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[158]]
			@staticmethod
			def Australia_South(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[159]]
			@staticmethod
			def Australia_Queensland(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[160]]
			@staticmethod
			def Australia_Yancowinna(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[161]]
			@staticmethod
			def Australia_North(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[162]]
			@staticmethod
			def Australia_Currie(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[163]]
			@staticmethod
			def Australia_Tasmania(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[164]]
			@staticmethod
			def Australia_LHI(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[165]]
			@staticmethod
			def Australia_Victoria(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[166]]
			@staticmethod
			def Australia_West(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[167]]
			@staticmethod
			def Australia_ACT(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[168]]
			@staticmethod
			def Australia_Canberra(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[169]]
			@staticmethod
			def Australia_NSW(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[170]]
			@staticmethod
			def GMT(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[171]]
			@staticmethod
			def GMTx0(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[172]]
			@staticmethod
			def GMT_0(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[173]]
			@staticmethod
			def GMT0(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[174]]
			@staticmethod
			def Greenwich(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[175]]
			@staticmethod
			def UCT(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[176]]
			@staticmethod
			def UTC(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[177]]
			@staticmethod
			def Universal(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[178]]
			@staticmethod
			def Zulu(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[179]]
			@staticmethod
			def Europe_Ljubljana(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[180]]
			@staticmethod
			def Europe_Podgorica(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[181]]
			@staticmethod
			def Europe_Sarajevo(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[182]]
			@staticmethod
			def Europe_Skopje(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[183]]
			@staticmethod
			def Europe_Zagreb(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[184]]
			@staticmethod
			def Arctic_Longyearbyen(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[185]]
			@staticmethod
			def Atlantic_Jan_Mayen(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[186]]
			@staticmethod
			def Europe_Copenhagen(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[187]]
			@staticmethod
			def Europe_Oslo(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[188]]
			@staticmethod
			def Europe_Stockholm(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[189]]
			@staticmethod
			def Europe_Amsterdam(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[190]]
			@staticmethod
			def Europe_Luxembourg(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[191]]
			@staticmethod
			def Europe_Tiraspol(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[192]]
			@staticmethod
			def Eire(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[193]]
			@staticmethod
			def Europe_Mariehamn(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[194]]
			@staticmethod
			def Asia_Istanbul(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[195]]
			@staticmethod
			def Turkey(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[196]]
			@staticmethod
			def Europe_Kiev(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[197]]
			@staticmethod
			def Europe_Uzhgorod(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[198]]
			@staticmethod
			def Europe_Zaporozhye(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[199]]
			@staticmethod
			def Portugal(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[200]]
			@staticmethod
			def Europe_Belfast(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[201]]
			@staticmethod
			def Europe_Guernsey(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[202]]
			@staticmethod
			def Europe_Isle_of_Man(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[203]]
			@staticmethod
			def Europe_Jersey(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[204]]
			@staticmethod
			def GB(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[205]]
			@staticmethod
			def GB_Eire(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[206]]
			@staticmethod
			def W_SU(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[207]]
			@staticmethod
			def Europe_Monaco(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[208]]
			@staticmethod
			def Europe_Bratislava(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[209]]
			@staticmethod
			def Europe_San_Marino(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[210]]
			@staticmethod
			def Europe_Vatican(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[211]]
			@staticmethod
			def Poland(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[212]]
			@staticmethod
			def Europe_Busingen(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[213]]
			@staticmethod
			def Europe_Vaduz(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[214]]
			@staticmethod
			def Indian_Kerguelen(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[215]]
			@staticmethod
			def Antarctica_McMurdo(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[216]]
			@staticmethod
			def Antarctica_South_Pole(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[217]]
			@staticmethod
			def NZ(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[218]]
			@staticmethod
			def NZ_CHAT(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[219]]
			@staticmethod
			def Chile_EasterIsland(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[220]]
			@staticmethod
			def Pacific_Pohnpei(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[221]]
			@staticmethod
			def Pacific_Ponape(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[222]]
			@staticmethod
			def Pacific_Saipan(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[223]]
			@staticmethod
			def Pacific_Johnston(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[224]]
			@staticmethod
			def US_Hawaii(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[225]]
			@staticmethod
			def Pacific_Enderbury(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[226]]
			@staticmethod
			def Kwajalein(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[227]]
			@staticmethod
			def Pacific_Midway(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[228]]
			@staticmethod
			def Pacific_Samoa(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[229]]
			@staticmethod
			def US_Samoa(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[230]]
			@staticmethod
			def Antarctica_DumontDUrville(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[231]]
			@staticmethod
			def Pacific_Chuuk(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[232]]
			@staticmethod
			def Pacific_Truk(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[233]]
			@staticmethod
			def Pacific_Yap(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[234]]
			@staticmethod
			def Pacific_Funafuti(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[235]]
			@staticmethod
			def Pacific_Majuro(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[236]]
			@staticmethod
			def Pacific_Wake(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[237]]
			@staticmethod
			def Pacific_Wallis(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[238]]
			@staticmethod
			def Africa_Abidjan(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[239]]
			@staticmethod
			def Africa_Algiers(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[240]]
			@staticmethod
			def Africa_Bissau(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[241]]
			@staticmethod
			def Africa_Cairo(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[242]]
			@staticmethod
			def Africa_Casablanca(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[243]]
			@staticmethod
			def Africa_Ceuta(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[244]]
			@staticmethod
			def Africa_El_Aaiun(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[245]]
			@staticmethod
			def Africa_Johannesburg(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[246]]
			@staticmethod
			def Africa_Juba(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[247]]
			@staticmethod
			def Africa_Khartoum(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[248]]
			@staticmethod
			def Africa_Lagos(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[249]]
			@staticmethod
			def Africa_Maputo(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[250]]
			@staticmethod
			def Africa_Monrovia(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[251]]
			@staticmethod
			def Africa_Nairobi(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[252]]
			@staticmethod
			def Africa_Ndjamena(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[253]]
			@staticmethod
			def Africa_Sao_Tome(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[254]]
			@staticmethod
			def Africa_Tripoli(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[255]]
			@staticmethod
			def Africa_Tunis(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[256]]
			@staticmethod
			def Africa_Windhoek(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[257]]
			@staticmethod
			def America_Adak(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[258]]
			@staticmethod
			def America_Anchorage(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[259]]
			@staticmethod
			def America_Araguaina(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[260]]
			@staticmethod
			def America_Argentina_Buenos_Aires(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[261]]
			@staticmethod
			def America_Argentina_Catamarca(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[262]]
			@staticmethod
			def America_Argentina_Cordoba(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[263]]
			@staticmethod
			def America_Argentina_Jujuy(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[264]]
			@staticmethod
			def America_Argentina_La_Rioja(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[265]]
			@staticmethod
			def America_Argentina_Mendoza(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[266]]
			@staticmethod
			def America_Argentina_Rio_Gallegos(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[267]]
			@staticmethod
			def America_Argentina_Salta(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[268]]
			@staticmethod
			def America_Argentina_San_Juan(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[269]]
			@staticmethod
			def America_Argentina_San_Luis(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[270]]
			@staticmethod
			def America_Argentina_Tucuman(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[271]]
			@staticmethod
			def America_Argentina_Ushuaia(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[272]]
			@staticmethod
			def America_Asuncion(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[273]]
			@staticmethod
			def America_Bahia(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[274]]
			@staticmethod
			def America_Bahia_Banderas(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[275]]
			@staticmethod
			def America_Barbados(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[276]]
			@staticmethod
			def America_Belem(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[277]]
			@staticmethod
			def America_Belize(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[278]]
			@staticmethod
			def America_Boa_Vista(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[279]]
			@staticmethod
			def America_Bogota(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[280]]
			@staticmethod
			def America_Boise(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[281]]
			@staticmethod
			def America_Cambridge_Bay(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[282]]
			@staticmethod
			def America_Campo_Grande(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[283]]
			@staticmethod
			def America_Cancun(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[284]]
			@staticmethod
			def America_Caracas(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[285]]
			@staticmethod
			def America_Cayenne(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[286]]
			@staticmethod
			def America_Chicago(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[287]]
			@staticmethod
			def America_Chihuahua(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[288]]
			@staticmethod
			def America_Ciudad_Juarez(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[289]]
			@staticmethod
			def America_Costa_Rica(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[290]]
			@staticmethod
			def America_Cuiaba(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[291]]
			@staticmethod
			def America_Danmarkshavn(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[292]]
			@staticmethod
			def America_Dawson(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[293]]
			@staticmethod
			def America_Dawson_Creek(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[294]]
			@staticmethod
			def America_Denver(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[295]]
			@staticmethod
			def America_Detroit(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[296]]
			@staticmethod
			def America_Edmonton(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[297]]
			@staticmethod
			def America_Eirunepe(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[298]]
			@staticmethod
			def America_El_Salvador(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[299]]
			@staticmethod
			def America_Fort_Nelson(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[300]]
			@staticmethod
			def America_Fortaleza(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[301]]
			@staticmethod
			def America_Glace_Bay(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[302]]
			@staticmethod
			def America_Goose_Bay(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[303]]
			@staticmethod
			def America_Grand_Turk(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[304]]
			@staticmethod
			def America_Guatemala(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[305]]
			@staticmethod
			def America_Guayaquil(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[306]]
			@staticmethod
			def America_Guyana(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[307]]
			@staticmethod
			def America_Halifax(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[308]]
			@staticmethod
			def America_Havana(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[309]]
			@staticmethod
			def America_Hermosillo(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[310]]
			@staticmethod
			def America_Indiana_Indianapolis(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[311]]
			@staticmethod
			def America_Indiana_Knox(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[312]]
			@staticmethod
			def America_Indiana_Marengo(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[313]]
			@staticmethod
			def America_Indiana_Petersburg(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[314]]
			@staticmethod
			def America_Indiana_Tell_City(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[315]]
			@staticmethod
			def America_Indiana_Vevay(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[316]]
			@staticmethod
			def America_Indiana_Vincennes(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[317]]
			@staticmethod
			def America_Indiana_Winamac(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[318]]
			@staticmethod
			def America_Inuvik(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[319]]
			@staticmethod
			def America_Iqaluit(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[320]]
			@staticmethod
			def America_Jamaica(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[321]]
			@staticmethod
			def America_Juneau(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[322]]
			@staticmethod
			def America_Kentucky_Louisville(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[323]]
			@staticmethod
			def America_Kentucky_Monticello(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[324]]
			@staticmethod
			def America_La_Paz(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[325]]
			@staticmethod
			def America_Lima(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[326]]
			@staticmethod
			def America_Los_Angeles(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[327]]
			@staticmethod
			def America_Maceio(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[328]]
			@staticmethod
			def America_Managua(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[329]]
			@staticmethod
			def America_Manaus(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[330]]
			@staticmethod
			def America_Martinique(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[331]]
			@staticmethod
			def America_Matamoros(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[332]]
			@staticmethod
			def America_Mazatlan(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[333]]
			@staticmethod
			def America_Menominee(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[334]]
			@staticmethod
			def America_Merida(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[335]]
			@staticmethod
			def America_Metlakatla(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[336]]
			@staticmethod
			def America_Mexico_City(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[337]]
			@staticmethod
			def America_Miquelon(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[338]]
			@staticmethod
			def America_Moncton(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[339]]
			@staticmethod
			def America_Monterrey(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[340]]
			@staticmethod
			def America_Montevideo(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[341]]
			@staticmethod
			def America_New_York(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[342]]
			@staticmethod
			def America_Nome(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[343]]
			@staticmethod
			def America_Noronha(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[344]]
			@staticmethod
			def America_North_Dakota_Beulah(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[345]]
			@staticmethod
			def America_North_Dakota_Center(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[346]]
			@staticmethod
			def America_North_Dakota_New_Salem(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[347]]
			@staticmethod
			def America_Nuuk(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[348]]
			@staticmethod
			def America_Ojinaga(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[349]]
			@staticmethod
			def America_Panama(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[350]]
			@staticmethod
			def America_Paramaribo(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[351]]
			@staticmethod
			def America_Phoenix(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[352]]
			@staticmethod
			def America_Port_au_Prince(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[353]]
			@staticmethod
			def America_Porto_Velho(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[354]]
			@staticmethod
			def America_Puerto_Rico(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[355]]
			@staticmethod
			def America_Punta_Arenas(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[356]]
			@staticmethod
			def America_Rankin_Inlet(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[357]]
			@staticmethod
			def America_Recife(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[358]]
			@staticmethod
			def America_Regina(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[359]]
			@staticmethod
			def America_Resolute(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[360]]
			@staticmethod
			def America_Rio_Branco(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[361]]
			@staticmethod
			def America_Santarem(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[362]]
			@staticmethod
			def America_Santiago(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[363]]
			@staticmethod
			def America_Santo_Domingo(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[364]]
			@staticmethod
			def America_Sao_Paulo(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[365]]
			@staticmethod
			def America_Scoresbysund(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[366]]
			@staticmethod
			def America_Sitka(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[367]]
			@staticmethod
			def America_St_Johns(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[368]]
			@staticmethod
			def America_Swift_Current(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[369]]
			@staticmethod
			def America_Tegucigalpa(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[370]]
			@staticmethod
			def America_Thule(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[371]]
			@staticmethod
			def America_Tijuana(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[372]]
			@staticmethod
			def America_Toronto(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[373]]
			@staticmethod
			def America_Vancouver(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[374]]
			@staticmethod
			def America_Whitehorse(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[375]]
			@staticmethod
			def America_Winnipeg(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[376]]
			@staticmethod
			def America_Yakutat(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[377]]
			@staticmethod
			def Antarctica_Casey(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[378]]
			@staticmethod
			def Antarctica_Davis(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[379]]
			@staticmethod
			def Antarctica_Macquarie(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[380]]
			@staticmethod
			def Antarctica_Mawson(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[381]]
			@staticmethod
			def Antarctica_Palmer(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[382]]
			@staticmethod
			def Antarctica_Rothera(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[383]]
			@staticmethod
			def Antarctica_Troll(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[384]]
			@staticmethod
			def Asia_Almaty(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[385]]
			@staticmethod
			def Asia_Amman(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[386]]
			@staticmethod
			def Asia_Anadyr(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[387]]
			@staticmethod
			def Asia_Aqtau(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[388]]
			@staticmethod
			def Asia_Aqtobe(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[389]]
			@staticmethod
			def Asia_Ashgabat(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[390]]
			@staticmethod
			def Asia_Atyrau(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[391]]
			@staticmethod
			def Asia_Baghdad(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[392]]
			@staticmethod
			def Asia_Baku(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[393]]
			@staticmethod
			def Asia_Bangkok(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[394]]
			@staticmethod
			def Asia_Barnaul(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[395]]
			@staticmethod
			def Asia_Beirut(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[396]]
			@staticmethod
			def Asia_Bishkek(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[397]]
			@staticmethod
			def Asia_Chita(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[398]]
			@staticmethod
			def Asia_Choibalsan(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[399]]
			@staticmethod
			def Asia_Colombo(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[400]]
			@staticmethod
			def Asia_Damascus(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[401]]
			@staticmethod
			def Asia_Dhaka(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[402]]
			@staticmethod
			def Asia_Dili(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[403]]
			@staticmethod
			def Asia_Dubai(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[404]]
			@staticmethod
			def Asia_Dushanbe(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[405]]
			@staticmethod
			def Asia_Famagusta(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[406]]
			@staticmethod
			def Asia_Gaza(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[407]]
			@staticmethod
			def Asia_Hebron(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[408]]
			@staticmethod
			def Asia_Ho_Chi_Minh(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[409]]
			@staticmethod
			def Asia_Hong_Kong(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[410]]
			@staticmethod
			def Asia_Hovd(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[411]]
			@staticmethod
			def Asia_Irkutsk(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[412]]
			@staticmethod
			def Asia_Jakarta(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[413]]
			@staticmethod
			def Asia_Jayapura(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[414]]
			@staticmethod
			def Asia_Jerusalem(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[415]]
			@staticmethod
			def Asia_Kabul(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[416]]
			@staticmethod
			def Asia_Kamchatka(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[417]]
			@staticmethod
			def Asia_Karachi(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[418]]
			@staticmethod
			def Asia_Kathmandu(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[419]]
			@staticmethod
			def Asia_Khandyga(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[420]]
			@staticmethod
			def Asia_Kolkata(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[421]]
			@staticmethod
			def Asia_Krasnoyarsk(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[422]]
			@staticmethod
			def Asia_Kuching(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[423]]
			@staticmethod
			def Asia_Macau(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[424]]
			@staticmethod
			def Asia_Magadan(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[425]]
			@staticmethod
			def Asia_Makassar(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[426]]
			@staticmethod
			def Asia_Manila(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[427]]
			@staticmethod
			def Asia_Nicosia(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[428]]
			@staticmethod
			def Asia_Novokuznetsk(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[429]]
			@staticmethod
			def Asia_Novosibirsk(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[430]]
			@staticmethod
			def Asia_Omsk(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[431]]
			@staticmethod
			def Asia_Oral(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[432]]
			@staticmethod
			def Asia_Pontianak(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[433]]
			@staticmethod
			def Asia_Pyongyang(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[434]]
			@staticmethod
			def Asia_Qatar(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[435]]
			@staticmethod
			def Asia_Qostanay(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[436]]
			@staticmethod
			def Asia_Qyzylorda(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[437]]
			@staticmethod
			def Asia_Riyadh(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[438]]
			@staticmethod
			def Asia_Sakhalin(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[439]]
			@staticmethod
			def Asia_Samarkand(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[440]]
			@staticmethod
			def Asia_Seoul(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[441]]
			@staticmethod
			def Asia_Shanghai(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[442]]
			@staticmethod
			def Asia_Singapore(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[443]]
			@staticmethod
			def Asia_Srednekolymsk(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[444]]
			@staticmethod
			def Asia_Taipei(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[445]]
			@staticmethod
			def Asia_Tashkent(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[446]]
			@staticmethod
			def Asia_Tbilisi(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[447]]
			@staticmethod
			def Asia_Tehran(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[448]]
			@staticmethod
			def Asia_Thimphu(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[449]]
			@staticmethod
			def Asia_Tokyo(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[450]]
			@staticmethod
			def Asia_Tomsk(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[451]]
			@staticmethod
			def Asia_Ulaanbaatar(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[452]]
			@staticmethod
			def Asia_Urumqi(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[453]]
			@staticmethod
			def Asia_Ust_Nera(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[454]]
			@staticmethod
			def Asia_Vladivostok(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[455]]
			@staticmethod
			def Asia_Yakutsk(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[456]]
			@staticmethod
			def Asia_Yangon(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[457]]
			@staticmethod
			def Asia_Yekaterinburg(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[458]]
			@staticmethod
			def Asia_Yerevan(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[459]]
			@staticmethod
			def Atlantic_Azores(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[460]]
			@staticmethod
			def Atlantic_Bermuda(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[461]]
			@staticmethod
			def Atlantic_Canary(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[462]]
			@staticmethod
			def Atlantic_Cape_Verde(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[463]]
			@staticmethod
			def Atlantic_Faroe(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[464]]
			@staticmethod
			def Atlantic_Madeira(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[465]]
			@staticmethod
			def Atlantic_South_Georgia(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[466]]
			@staticmethod
			def Atlantic_Stanley(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[467]]
			@staticmethod
			def Australia_Adelaide(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[468]]
			@staticmethod
			def Australia_Brisbane(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[469]]
			@staticmethod
			def Australia_Broken_Hill(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[470]]
			@staticmethod
			def Australia_Darwin(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[471]]
			@staticmethod
			def Australia_Eucla(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[472]]
			@staticmethod
			def Australia_Hobart(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[473]]
			@staticmethod
			def Australia_Lindeman(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[474]]
			@staticmethod
			def Australia_Lord_Howe(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[475]]
			@staticmethod
			def Australia_Melbourne(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[476]]
			@staticmethod
			def Australia_Perth(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[477]]
			@staticmethod
			def Australia_Sydney(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[478]]
			@staticmethod
			def CET(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[479]]
			@staticmethod
			def CST6CDT(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[480]]
			@staticmethod
			def EET(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[481]]
			@staticmethod
			def EST(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[482]]
			@staticmethod
			def EST5EDT(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[483]]
			@staticmethod
			def Europe_Andorra(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[484]]
			@staticmethod
			def Europe_Astrakhan(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[485]]
			@staticmethod
			def Europe_Athens(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[486]]
			@staticmethod
			def Europe_Belgrade(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[487]]
			@staticmethod
			def Europe_Berlin(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[488]]
			@staticmethod
			def Europe_Brussels(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[489]]
			@staticmethod
			def Europe_Bucharest(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[490]]
			@staticmethod
			def Europe_Budapest(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[491]]
			@staticmethod
			def Europe_Chisinau(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[492]]
			@staticmethod
			def Europe_Dublin(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[493]]
			@staticmethod
			def Europe_Gibraltar(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[494]]
			@staticmethod
			def Europe_Helsinki(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[495]]
			@staticmethod
			def Europe_Istanbul(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[496]]
			@staticmethod
			def Europe_Kaliningrad(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[497]]
			@staticmethod
			def Europe_Kirov(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[498]]
			@staticmethod
			def Europe_Kyiv(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[499]]
			@staticmethod
			def Europe_Lisbon(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[500]]
			@staticmethod
			def Europe_London(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[501]]
			@staticmethod
			def Europe_Madrid(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[502]]
			@staticmethod
			def Europe_Malta(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[503]]
			@staticmethod
			def Europe_Minsk(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[504]]
			@staticmethod
			def Europe_Moscow(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[505]]
			@staticmethod
			def Europe_Paris(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[506]]
			@staticmethod
			def Europe_Prague(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[507]]
			@staticmethod
			def Europe_Riga(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[508]]
			@staticmethod
			def Europe_Rome(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[509]]
			@staticmethod
			def Europe_Samara(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[510]]
			@staticmethod
			def Europe_Saratov(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[511]]
			@staticmethod
			def Europe_Simferopol(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[512]]
			@staticmethod
			def Europe_Sofia(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[513]]
			@staticmethod
			def Europe_Tallinn(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[514]]
			@staticmethod
			def Europe_Tirane(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[515]]
			@staticmethod
			def Europe_Ulyanovsk(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[516]]
			@staticmethod
			def Europe_Vienna(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[517]]
			@staticmethod
			def Europe_Vilnius(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[518]]
			@staticmethod
			def Europe_Volgograd(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[519]]
			@staticmethod
			def Europe_Warsaw(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[520]]
			@staticmethod
			def Europe_Zurich(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[521]]
			@staticmethod
			def Factory(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[522]]
			@staticmethod
			def HST(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[523]]
			@staticmethod
			def Indian_Chagos(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[524]]
			@staticmethod
			def Indian_Maldives(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[525]]
			@staticmethod
			def Indian_Mauritius(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[526]]
			@staticmethod
			def MET(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[527]]
			@staticmethod
			def MST(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[528]]
			@staticmethod
			def MST7MDT(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[529]]
			@staticmethod
			def PST8PDT(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[530]]
			@staticmethod
			def Pacific_Apia(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[531]]
			@staticmethod
			def Pacific_Auckland(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[532]]
			@staticmethod
			def Pacific_Bougainville(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[533]]
			@staticmethod
			def Pacific_Chatham(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[534]]
			@staticmethod
			def Pacific_Easter(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[535]]
			@staticmethod
			def Pacific_Efate(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[536]]
			@staticmethod
			def Pacific_Fakaofo(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[537]]
			@staticmethod
			def Pacific_Fiji(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[538]]
			@staticmethod
			def Pacific_Galapagos(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[539]]
			@staticmethod
			def Pacific_Gambier(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[540]]
			@staticmethod
			def Pacific_Guadalcanal(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[541]]
			@staticmethod
			def Pacific_Guam(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[542]]
			@staticmethod
			def Pacific_Honolulu(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[543]]
			@staticmethod
			def Pacific_Kanton(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[544]]
			@staticmethod
			def Pacific_Kiritimati(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[545]]
			@staticmethod
			def Pacific_Kosrae(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[546]]
			@staticmethod
			def Pacific_Kwajalein(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[547]]
			@staticmethod
			def Pacific_Marquesas(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[548]]
			@staticmethod
			def Pacific_Nauru(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[549]]
			@staticmethod
			def Pacific_Niue(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[550]]
			@staticmethod
			def Pacific_Norfolk(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[551]]
			@staticmethod
			def Pacific_Noumea(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[552]]
			@staticmethod
			def Pacific_Pago_Pago(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[553]]
			@staticmethod
			def Pacific_Palau(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[554]]
			@staticmethod
			def Pacific_Pitcairn(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[555]]
			@staticmethod
			def Pacific_Port_Moresby(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[556]]
			@staticmethod
			def Pacific_Rarotonga(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[557]]
			@staticmethod
			def Pacific_Tahiti(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[558]]
			@staticmethod
			def Pacific_Tarawa(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[559]]
			@staticmethod
			def Pacific_Tongatapu(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[560]]
			@staticmethod
			def WET(greycat: GreyCat) -> std_.core.TimeZone:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[27]
				return t.enum_values[t.generated_offsets[561]]
			@staticmethod
			def create(greycat: GreyCat) -> std_.core.TimeZone:
				return std_.core.TimeZone(greycat.libs_by_name[std.name_].mapped[27])
		@final
		class GeoBox(GreyCat.Object):
			name_: Final[str] = "core::GeoBox"
			def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
				super().__init__(type, attributes)
			def sw(self) -> std.core.geo:
				return self._get(self.type_.generated_offsets[0])
			def set_sw(self, v: std.core.geo) -> None:
				self._set(self.type_.generated_offsets[0],v)
			def ne(self) -> std.core.geo:
				return self._get(self.type_.generated_offsets[1])
			def set_ne(self, v: std.core.geo) -> None:
				self._set(self.type_.generated_offsets[1],v)
			@staticmethod
			def create(greycat: GreyCat, sw: std.core.geo, ne: std.core.geo) -> std_.core.GeoBox:
				return std_.core.GeoBox(greycat.libs_by_name[std.name_].mapped[28], sw, ne)
		@final
		class Tuple(Generic[_T,_U], GreyCat.Object):
			name_: Final[str] = "core::Tuple"
			def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
				super().__init__(type, attributes)
			def x(self) -> _T:
				return self._get(self.type_.generated_offsets[0])
			def set_x(self, v: _T) -> None:
				self._set(self.type_.generated_offsets[0],v)
			def y(self) -> _U:
				return self._get(self.type_.generated_offsets[1])
			def set_y(self, v: _U) -> None:
				self._set(self.type_.generated_offsets[1],v)
			@staticmethod
			def create(greycat: GreyCat, x: _T, y: _U) -> std_.core.Tuple[_T, _U]:
				return std_.core.Tuple(greycat.libs_by_name[std.name_].mapped[29], x, y)
		@final
		class DatePart(GreyCat.Enum):
			name_: Final[str] = "core::DatePart"
			def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
				super().__init__(type, attributes)
			@staticmethod
			def years(greycat: GreyCat) -> std_.core.DatePart:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[30]
				return t.enum_values[t.generated_offsets[0]]
			@staticmethod
			def months(greycat: GreyCat) -> std_.core.DatePart:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[30]
				return t.enum_values[t.generated_offsets[1]]
			@staticmethod
			def days(greycat: GreyCat) -> std_.core.DatePart:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[30]
				return t.enum_values[t.generated_offsets[2]]
			@staticmethod
			def hours(greycat: GreyCat) -> std_.core.DatePart:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[30]
				return t.enum_values[t.generated_offsets[3]]
			@staticmethod
			def minutes(greycat: GreyCat) -> std_.core.DatePart:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[30]
				return t.enum_values[t.generated_offsets[4]]
			@staticmethod
			def seconds(greycat: GreyCat) -> std_.core.DatePart:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[30]
				return t.enum_values[t.generated_offsets[5]]
			@staticmethod
			def microseconds(greycat: GreyCat) -> std_.core.DatePart:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[30]
				return t.enum_values[t.generated_offsets[6]]
			@staticmethod
			def create(greycat: GreyCat) -> std_.core.DatePart:
				return std_.core.DatePart(greycat.libs_by_name[std.name_].mapped[30])
		@final
		class nodeIndex(Generic[_K,_V], std_n.core._nodeIndex[_K,_V]):
			name_: Final[str] = "core::nodeIndex"
			def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
				super().__init__(type)
			@staticmethod
			def create(greycat: GreyCat) -> std_n.core._nodeIndex:
				return std.core.nodeIndex(greycat.libs_by_name[std.name_].mapped[31])
		@final
		class nodeList(Generic[_T], std_n.core._nodeList[_T]):
			name_: Final[str] = "core::nodeList"
			def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
				super().__init__(type)
			@staticmethod
			def create(greycat: GreyCat) -> std_n.core._nodeList:
				return std.core.nodeList(greycat.libs_by_name[std.name_].mapped[32])
		@final
		class tf3d(std_n.core._tf3d):
			name_: Final[str] = "core::tf3d"
			def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
				super().__init__(type)
			@staticmethod
			def create(greycat: GreyCat) -> std_n.core._tf3d:
				return std.core.tf3d(greycat.libs_by_name[std.name_].mapped[33])
		@final
		class nodeIndexBucket(std_n.core._nodeIndexBucket):
			name_: Final[str] = "core::nodeIndexBucket"
			def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
				super().__init__(type)
			@staticmethod
			def create(greycat: GreyCat) -> std_n.core._nodeIndexBucket:
				return std.core.nodeIndexBucket(greycat.libs_by_name[std.name_].mapped[34])
		@final
		class ti10d(std_n.core._ti10d):
			name_: Final[str] = "core::ti10d"
			def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
				super().__init__(type)
			@staticmethod
			def create(greycat: GreyCat) -> std_n.core._ti10d:
				return std.core.ti10d(greycat.libs_by_name[std.name_].mapped[35])
		@final
		class Array(Generic[_T], std_n.core._Array[_T]):
			name_: Final[str] = "core::Array"
			def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
				super().__init__(type)
			@staticmethod
			def create(greycat: GreyCat) -> std_n.core._Array:
				return std.core.Array(greycat.libs_by_name[std.name_].mapped[36])
		@final
		class tf4d(std_n.core._tf4d):
			name_: Final[str] = "core::tf4d"
			def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
				super().__init__(type)
			@staticmethod
			def create(greycat: GreyCat) -> std_n.core._tf4d:
				return std.core.tf4d(greycat.libs_by_name[std.name_].mapped[37])
		@final
		class ti3d(std_n.core._ti3d):
			name_: Final[str] = "core::ti3d"
			def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
				super().__init__(type)
			@staticmethod
			def create(greycat: GreyCat) -> std_n.core._ti3d:
				return std.core.ti3d(greycat.libs_by_name[std.name_].mapped[38])
	@final
	class runtime:
		@final
		class UserGroup(GreyCat.Object):
			name_: Final[str] = "runtime::UserGroup"
			def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
				super().__init__(type, attributes)
			def id(self) -> int:
				return self._get(self.type_.generated_offsets[0])
			def set_id(self, v: int) -> None:
				self._set(self.type_.generated_offsets[0],v)
			def name(self) -> str:
				return self._get(self.type_.generated_offsets[1])
			def set_name(self, v: str) -> None:
				self._set(self.type_.generated_offsets[1],v)
			def activated(self) -> bool:
				return self._get(self.type_.generated_offsets[2])
			def set_activated(self, v: bool) -> None:
				self._set(self.type_.generated_offsets[2],v)
			@staticmethod
			def all(greycat: GreyCat) -> std_.core.Array:
				return GreyCat.call(greycat,"runtime::SecurityEntity::all")
			@staticmethod
			def set(greycat: GreyCat, entity: std_.runtime.SecurityEntity) -> int:
				return GreyCat.call(greycat,"runtime::SecurityEntity::set", entity)
			@staticmethod
			def create(greycat: GreyCat, id: int, name: str, activated: bool) -> std_.runtime.UserGroup:
				return std_.runtime.UserGroup(greycat.libs_by_name[std.name_].mapped[39], id, name, activated)
		@final
		class SecurityEntity(GreyCat.Object):
			name_: Final[str] = "runtime::SecurityEntity"
			def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
				super().__init__(type, attributes)
			def id(self) -> int:
				return self._get(self.type_.generated_offsets[0])
			def set_id(self, v: int) -> None:
				self._set(self.type_.generated_offsets[0],v)
			def name(self) -> str:
				return self._get(self.type_.generated_offsets[1])
			def set_name(self, v: str) -> None:
				self._set(self.type_.generated_offsets[1],v)
			def activated(self) -> bool:
				return self._get(self.type_.generated_offsets[2])
			def set_activated(self, v: bool) -> None:
				self._set(self.type_.generated_offsets[2],v)
			@staticmethod
			def all(greycat: GreyCat) -> std_.core.Array:
				return GreyCat.call(greycat,"runtime::SecurityEntity::all")
			@staticmethod
			def set(greycat: GreyCat, entity: std_.runtime.SecurityEntity) -> int:
				return GreyCat.call(greycat,"runtime::SecurityEntity::set", entity)
			@staticmethod
			def create(greycat: GreyCat, id: int, name: str, activated: bool) -> std_.runtime.SecurityEntity:
				return std_.runtime.SecurityEntity(greycat.libs_by_name[std.name_].mapped[40], id, name, activated)
		@final
		class PeriodicTask(GreyCat.Object):
			name_: Final[str] = "runtime::PeriodicTask"
			def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
				super().__init__(type, attributes)
			def name(self) -> str:
				return self._get(self.type_.generated_offsets[0])
			def set_name(self, v: str) -> None:
				self._set(self.type_.generated_offsets[0],v)
			def user_id(self) -> int:
				return self._get(self.type_.generated_offsets[1])
			def set_user_id(self, v: int) -> None:
				self._set(self.type_.generated_offsets[1],v)
			def args(self) -> str:
				return self._get(self.type_.generated_offsets[2])
			def set_args(self, v: str) -> None:
				self._set(self.type_.generated_offsets[2],v)
			def start(self) -> std.core.time:
				return self._get(self.type_.generated_offsets[3])
			def set_start(self, v: std.core.time) -> None:
				self._set(self.type_.generated_offsets[3],v)
			def every(self) -> std.core.duration:
				return self._get(self.type_.generated_offsets[4])
			def set_every(self, v: std.core.duration) -> None:
				self._set(self.type_.generated_offsets[4],v)
			@staticmethod
			def all(greycat: GreyCat) -> std_.core.Array:
				return GreyCat.call(greycat,"runtime::PeriodicTask::all")
			@staticmethod
			def set(greycat: GreyCat, tasks: std_.core.Array) -> None:
				return GreyCat.call(greycat,"runtime::PeriodicTask::set", tasks)
			@staticmethod
			def create(greycat: GreyCat, name: str, user_id: int, args: str, start: std.core.time, every: std.core.duration) -> std_.runtime.PeriodicTask:
				return std_.runtime.PeriodicTask(greycat.libs_by_name[std.name_].mapped[41], name, user_id, args, start, every)
		@final
		class License(GreyCat.Object):
			name_: Final[str] = "runtime::License"
			def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
				super().__init__(type, attributes)
			def name(self) -> str:
				return self._get(self.type_.generated_offsets[0])
			def set_name(self, v: str) -> None:
				self._set(self.type_.generated_offsets[0],v)
			def start(self) -> std.core.time:
				return self._get(self.type_.generated_offsets[1])
			def set_start(self, v: std.core.time) -> None:
				self._set(self.type_.generated_offsets[1],v)
			def end(self) -> std.core.time:
				return self._get(self.type_.generated_offsets[2])
			def set_end(self, v: std.core.time) -> None:
				self._set(self.type_.generated_offsets[2],v)
			def company(self) -> str:
				return self._get(self.type_.generated_offsets[3])
			def set_company(self, v: str) -> None:
				self._set(self.type_.generated_offsets[3],v)
			def max_workers(self) -> int:
				return self._get(self.type_.generated_offsets[4])
			def set_max_workers(self, v: int) -> None:
				self._set(self.type_.generated_offsets[4],v)
			def max_memory(self) -> int:
				return self._get(self.type_.generated_offsets[5])
			def set_max_memory(self, v: int) -> None:
				self._set(self.type_.generated_offsets[5],v)
			def extra_1(self) -> int:
				return self._get(self.type_.generated_offsets[6])
			def set_extra_1(self, v: int) -> None:
				self._set(self.type_.generated_offsets[6],v)
			def extra_2(self) -> int:
				return self._get(self.type_.generated_offsets[7])
			def set_extra_2(self, v: int) -> None:
				self._set(self.type_.generated_offsets[7],v)
			def extra_3(self) -> int:
				return self._get(self.type_.generated_offsets[8])
			def set_extra_3(self, v: int) -> None:
				self._set(self.type_.generated_offsets[8],v)
			def extra_4(self) -> int:
				return self._get(self.type_.generated_offsets[9])
			def set_extra_4(self, v: int) -> None:
				self._set(self.type_.generated_offsets[9],v)
			@staticmethod
			def create(greycat: GreyCat, name: str, start: std.core.time, end: std.core.time, company: str, max_workers: int, max_memory: int, extra_1: int, extra_2: int, extra_3: int, extra_4: int) -> std_.runtime.License:
				return std_.runtime.License(greycat.libs_by_name[std.name_].mapped[42], name, start, end, company, max_workers, max_memory, extra_1, extra_2, extra_3, extra_4)
		@final
		class StoreStat(GreyCat.Object):
			name_: Final[str] = "runtime::StoreStat"
			def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
				super().__init__(type, attributes)
			def capacity_bytes(self) -> int:
				return self._get(self.type_.generated_offsets[0])
			def set_capacity_bytes(self, v: int) -> None:
				self._set(self.type_.generated_offsets[0],v)
			def allocated_bytes(self) -> int:
				return self._get(self.type_.generated_offsets[1])
			def set_allocated_bytes(self, v: int) -> None:
				self._set(self.type_.generated_offsets[1],v)
			def allocated_ratio(self) -> float:
				return self._get(self.type_.generated_offsets[2])
			def set_allocated_ratio(self, v: float) -> None:
				self._set(self.type_.generated_offsets[2],v)
			def remained_bytes(self) -> int:
				return self._get(self.type_.generated_offsets[3])
			def set_remained_bytes(self, v: int) -> None:
				self._set(self.type_.generated_offsets[3],v)
			def remained_ratio(self) -> float:
				return self._get(self.type_.generated_offsets[4])
			def set_remained_ratio(self, v: float) -> None:
				self._set(self.type_.generated_offsets[4],v)
			def used_bytes(self) -> int:
				return self._get(self.type_.generated_offsets[5])
			def set_used_bytes(self, v: int) -> None:
				self._set(self.type_.generated_offsets[5],v)
			def used_ratio(self) -> float:
				return self._get(self.type_.generated_offsets[6])
			def set_used_ratio(self, v: float) -> None:
				self._set(self.type_.generated_offsets[6],v)
			def available_bytes(self) -> int:
				return self._get(self.type_.generated_offsets[7])
			def set_available_bytes(self, v: int) -> None:
				self._set(self.type_.generated_offsets[7],v)
			def available_ratio(self) -> float:
				return self._get(self.type_.generated_offsets[8])
			def set_available_ratio(self, v: float) -> None:
				self._set(self.type_.generated_offsets[8],v)
			@staticmethod
			def create(greycat: GreyCat, capacity_bytes: int, allocated_bytes: int, allocated_ratio: float, remained_bytes: int, remained_ratio: float, used_bytes: int, used_ratio: float, available_bytes: int, available_ratio: float) -> std_.runtime.StoreStat:
				return std_.runtime.StoreStat(greycat.libs_by_name[std.name_].mapped[43], capacity_bytes, allocated_bytes, allocated_ratio, remained_bytes, remained_ratio, used_bytes, used_ratio, available_bytes, available_ratio)
		@final
		class SecurityFields(GreyCat.Object):
			name_: Final[str] = "runtime::SecurityFields"
			def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
				super().__init__(type, attributes)
			def email(self) -> str:
				return self._get(self.type_.generated_offsets[0])
			def set_email(self, v: str) -> None:
				self._set(self.type_.generated_offsets[0],v)
			def name(self) -> str:
				return self._get(self.type_.generated_offsets[1])
			def set_name(self, v: str) -> None:
				self._set(self.type_.generated_offsets[1],v)
			def first_name(self) -> str:
				return self._get(self.type_.generated_offsets[2])
			def set_first_name(self, v: str) -> None:
				self._set(self.type_.generated_offsets[2],v)
			def last_name(self) -> str:
				return self._get(self.type_.generated_offsets[3])
			def set_last_name(self, v: str) -> None:
				self._set(self.type_.generated_offsets[3],v)
			def roles(self) -> std_.core.Map:
				return self._get(self.type_.generated_offsets[4])
			def set_roles(self, v: std_.core.Map) -> None:
				self._set(self.type_.generated_offsets[4],v)
			def groups(self) -> std_.core.Map:
				return self._get(self.type_.generated_offsets[5])
			def set_groups(self, v: std_.core.Map) -> None:
				self._set(self.type_.generated_offsets[5],v)
			@staticmethod
			def set(greycat: GreyCat, f: std_.runtime.SecurityFields) -> None:
				return GreyCat.call(greycat,"runtime::SecurityFields::set", f)
			@staticmethod
			def get(greycat: GreyCat) -> std_.runtime.SecurityFields:
				return GreyCat.call(greycat,"runtime::SecurityFields::get")
			@staticmethod
			def create(greycat: GreyCat, email: str, name: str, first_name: str, last_name: str, roles: std_.core.Map, groups: std_.core.Map) -> std_.runtime.SecurityFields:
				return std_.runtime.SecurityFields(greycat.libs_by_name[std.name_].mapped[44], email, name, first_name, last_name, roles, groups)
		@final
		class Task(GreyCat.Object):
			name_: Final[str] = "runtime::Task"
			def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
				super().__init__(type, attributes)
			def user_id(self) -> int:
				return self._get(self.type_.generated_offsets[0])
			def set_user_id(self, v: int) -> None:
				self._set(self.type_.generated_offsets[0],v)
			def task_id(self) -> int:
				return self._get(self.type_.generated_offsets[1])
			def set_task_id(self, v: int) -> None:
				self._set(self.type_.generated_offsets[1],v)
			def mod(self) -> str:
				return self._get(self.type_.generated_offsets[2])
			def set_mod(self, v: str) -> None:
				self._set(self.type_.generated_offsets[2],v)
			def type(self) -> str:
				return self._get(self.type_.generated_offsets[3])
			def set_type(self, v: str) -> None:
				self._set(self.type_.generated_offsets[3],v)
			def fun(self) -> str:
				return self._get(self.type_.generated_offsets[4])
			def set_fun(self, v: str) -> None:
				self._set(self.type_.generated_offsets[4],v)
			def creation(self) -> std.core.time:
				return self._get(self.type_.generated_offsets[5])
			def set_creation(self, v: std.core.time) -> None:
				self._set(self.type_.generated_offsets[5],v)
			def status(self) -> std_.runtime.TaskStatus:
				return self._get(self.type_.generated_offsets[6])
			def set_status(self, v: std_.runtime.TaskStatus) -> None:
				self._set(self.type_.generated_offsets[6],v)
			@staticmethod
			def running(greycat: GreyCat) -> std_.core.Array:
				return GreyCat.call(greycat,"runtime::Task::running")
			@staticmethod
			def history(greycat: GreyCat, offset: int, max: int) -> std_.core.Array:
				return GreyCat.call(greycat,"runtime::Task::history", offset, max)
			@staticmethod
			def cancel(greycat: GreyCat, task_id: int) -> bool:
				return GreyCat.call(greycat,"runtime::Task::cancel", task_id)
			@staticmethod
			def info(greycat: GreyCat, user_id: int, task_id: int) -> std_.runtime.TaskInfo:
				return GreyCat.call(greycat,"runtime::Task::info", user_id, task_id)
			@staticmethod
			def create(greycat: GreyCat, user_id: int, task_id: int, mod: str, type: str, fun: str, creation: std.core.time, status: std_.runtime.TaskStatus) -> std_.runtime.Task:
				return std_.runtime.Task(greycat.libs_by_name[std.name_].mapped[45], user_id, task_id, mod, type, fun, creation, status)
		@final
		class OpenIDConnect(GreyCat.Object):
			name_: Final[str] = "runtime::OpenIDConnect"
			def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
				super().__init__(type, attributes)
			def url(self) -> str:
				return self._get(self.type_.generated_offsets[0])
			def set_url(self, v: str) -> None:
				self._set(self.type_.generated_offsets[0],v)
			def clientId(self) -> str:
				return self._get(self.type_.generated_offsets[1])
			def set_clientId(self, v: str) -> None:
				self._set(self.type_.generated_offsets[1],v)
			@staticmethod
			def config(greycat: GreyCat) -> std_.runtime.OpenIDConnect:
				return GreyCat.call(greycat,"runtime::OpenIDConnect::config")
			@staticmethod
			def create(greycat: GreyCat, url: str, clientId: str) -> std_.runtime.OpenIDConnect:
				return std_.runtime.OpenIDConnect(greycat.libs_by_name[std.name_].mapped[46], url, clientId)
		@final
		class UserGroupPolicy(GreyCat.Object):
			name_: Final[str] = "runtime::UserGroupPolicy"
			def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
				super().__init__(type, attributes)
			def group_id(self) -> int:
				return self._get(self.type_.generated_offsets[0])
			def set_group_id(self, v: int) -> None:
				self._set(self.type_.generated_offsets[0],v)
			def type(self) -> std_.runtime.UserGroupPolicyType:
				return self._get(self.type_.generated_offsets[1])
			def set_type(self, v: std_.runtime.UserGroupPolicyType) -> None:
				self._set(self.type_.generated_offsets[1],v)
			@staticmethod
			def create(greycat: GreyCat, group_id: int, type: std_.runtime.UserGroupPolicyType) -> std_.runtime.UserGroupPolicy:
				return std_.runtime.UserGroupPolicy(greycat.libs_by_name[std.name_].mapped[47], group_id, type)
		@final
		class RuntimeInfo(GreyCat.Object):
			name_: Final[str] = "runtime::RuntimeInfo"
			def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
				super().__init__(type, attributes)
			def version(self) -> str:
				return self._get(self.type_.generated_offsets[0])
			def set_version(self, v: str) -> None:
				self._set(self.type_.generated_offsets[0],v)
			def arch(self) -> str:
				return self._get(self.type_.generated_offsets[1])
			def set_arch(self, v: str) -> None:
				self._set(self.type_.generated_offsets[1],v)
			def timezone(self) -> std_.core.TimeZone:
				return self._get(self.type_.generated_offsets[2])
			def set_timezone(self, v: std_.core.TimeZone) -> None:
				self._set(self.type_.generated_offsets[2],v)
			def license(self) -> std_.runtime.License:
				return self._get(self.type_.generated_offsets[3])
			def set_license(self, v: std_.runtime.License) -> None:
				self._set(self.type_.generated_offsets[3],v)
			def io_threads(self) -> int:
				return self._get(self.type_.generated_offsets[4])
			def set_io_threads(self, v: int) -> None:
				self._set(self.type_.generated_offsets[4],v)
			def bg_threads(self) -> int:
				return self._get(self.type_.generated_offsets[5])
			def set_bg_threads(self, v: int) -> None:
				self._set(self.type_.generated_offsets[5],v)
			def fg_threads(self) -> int:
				return self._get(self.type_.generated_offsets[6])
			def set_fg_threads(self, v: int) -> None:
				self._set(self.type_.generated_offsets[6],v)
			def mem_total(self) -> int:
				return self._get(self.type_.generated_offsets[7])
			def set_mem_total(self, v: int) -> None:
				self._set(self.type_.generated_offsets[7],v)
			def mem_worker(self) -> int:
				return self._get(self.type_.generated_offsets[8])
			def set_mem_worker(self, v: int) -> None:
				self._set(self.type_.generated_offsets[8],v)
			def nb_ctx(self) -> int:
				return self._get(self.type_.generated_offsets[9])
			def set_nb_ctx(self, v: int) -> None:
				self._set(self.type_.generated_offsets[9],v)
			def store_stats(self) -> std_.runtime.StoreStat:
				return self._get(self.type_.generated_offsets[10])
			def set_store_stats(self, v: std_.runtime.StoreStat) -> None:
				self._set(self.type_.generated_offsets[10],v)
			@staticmethod
			def create(greycat: GreyCat, version: str, arch: str, timezone: std_.core.TimeZone, license: std_.runtime.License, io_threads: int, bg_threads: int, fg_threads: int, mem_total: int, mem_worker: int, nb_ctx: int, store_stats: std_.runtime.StoreStat) -> std_.runtime.RuntimeInfo:
				return std_.runtime.RuntimeInfo(greycat.libs_by_name[std.name_].mapped[48], version, arch, timezone, license, io_threads, bg_threads, fg_threads, mem_total, mem_worker, nb_ctx, store_stats)
		@final
		class User(GreyCat.Object):
			name_: Final[str] = "runtime::User"
			def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
				super().__init__(type, attributes)
			def id(self) -> int:
				return self._get(self.type_.generated_offsets[0])
			def set_id(self, v: int) -> None:
				self._set(self.type_.generated_offsets[0],v)
			def name(self) -> str:
				return self._get(self.type_.generated_offsets[1])
			def set_name(self, v: str) -> None:
				self._set(self.type_.generated_offsets[1],v)
			def activated(self) -> bool:
				return self._get(self.type_.generated_offsets[2])
			def set_activated(self, v: bool) -> None:
				self._set(self.type_.generated_offsets[2],v)
			def full_name(self) -> str:
				return self._get(self.type_.generated_offsets[3])
			def set_full_name(self, v: str) -> None:
				self._set(self.type_.generated_offsets[3],v)
			def email(self) -> str:
				return self._get(self.type_.generated_offsets[4])
			def set_email(self, v: str) -> None:
				self._set(self.type_.generated_offsets[4],v)
			def role(self) -> str:
				return self._get(self.type_.generated_offsets[5])
			def set_role(self, v: str) -> None:
				self._set(self.type_.generated_offsets[5],v)
			def permissions_flags(self) -> int:
				return self._get(self.type_.generated_offsets[6])
			def set_permissions_flags(self, v: int) -> None:
				self._set(self.type_.generated_offsets[6],v)
			def groups(self) -> std_.core.Array:
				return self._get(self.type_.generated_offsets[7])
			def set_groups(self, v: std_.core.Array) -> None:
				self._set(self.type_.generated_offsets[7],v)
			def groups_flags(self) -> int:
				return self._get(self.type_.generated_offsets[8])
			def set_groups_flags(self, v: int) -> None:
				self._set(self.type_.generated_offsets[8],v)
			def external(self) -> bool:
				return self._get(self.type_.generated_offsets[9])
			def set_external(self, v: bool) -> None:
				self._set(self.type_.generated_offsets[9],v)
			@staticmethod
			def all(greycat: GreyCat) -> std_.core.Array:
				return GreyCat.call(greycat,"runtime::SecurityEntity::all")
			@staticmethod
			def set(greycat: GreyCat, entity: std_.runtime.SecurityEntity) -> int:
				return GreyCat.call(greycat,"runtime::SecurityEntity::set", entity)
			@staticmethod
			def login(greycat: GreyCat, credentials: str, use_cookie: bool) -> str:
				return GreyCat.call(greycat,"runtime::User::login", credentials, use_cookie)
			@staticmethod
			def tokenLogin(greycat: GreyCat, token: str, use_cookie: bool) -> str:
				return GreyCat.call(greycat,"runtime::User::tokenLogin", token, use_cookie)
			@staticmethod
			def renew(greycat: GreyCat, use_cookie: bool) -> str:
				return GreyCat.call(greycat,"runtime::User::renew", use_cookie)
			@staticmethod
			def logout(greycat: GreyCat) -> None:
				return GreyCat.call(greycat,"runtime::User::logout")
			@staticmethod
			def current(greycat: GreyCat) -> int:
				return GreyCat.call(greycat,"runtime::User::current")
			@staticmethod
			def me(greycat: GreyCat) -> std_.runtime.User:
				return GreyCat.call(greycat,"runtime::User::me")
			@staticmethod
			def permissions(greycat: GreyCat) -> std_.core.Array:
				return GreyCat.call(greycat,"runtime::User::permissions")
			@staticmethod
			def setPassword(greycat: GreyCat, name: str, pass_: str) -> bool:
				return GreyCat.call(greycat,"runtime::User::setPassword", name, pass_)
			@staticmethod
			def getToken(greycat: GreyCat, id: int) -> str:
				return GreyCat.call(greycat,"runtime::User::getToken", id)
			@staticmethod
			def create(greycat: GreyCat, id: int, name: str, activated: bool, full_name: str, email: str, role: str, permissions_flags: int, groups: std_.core.Array, groups_flags: int, external: bool) -> std_.runtime.User:
				return std_.runtime.User(greycat.libs_by_name[std.name_].mapped[49], id, name, activated, full_name, email, role, permissions_flags, groups, groups_flags, external)
		@final
		class System(GreyCat.Object):
			name_: Final[str] = "runtime::System"
			def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
				super().__init__(type, attributes)
			@staticmethod
			def create(greycat: GreyCat) -> std_.runtime.System:
				return std_.runtime.System(greycat.libs_by_name[std.name_].mapped[50])
		@final
		class UserCredential(GreyCat.Object):
			name_: Final[str] = "runtime::UserCredential"
			def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
				super().__init__(type, attributes)
			def offset(self) -> int:
				return self._get(self.type_.generated_offsets[0])
			def set_offset(self, v: int) -> None:
				self._set(self.type_.generated_offsets[0],v)
			def pass_(self) -> str:
				return self._get(self.type_.generated_offsets[1])
			def set_pass(self, v: str) -> None:
				self._set(self.type_.generated_offsets[1],v)
			@staticmethod
			def create(greycat: GreyCat, offset: int, pass_: str) -> std_.runtime.UserCredential:
				return std_.runtime.UserCredential(greycat.libs_by_name[std.name_].mapped[51], offset, pass_)
		@final
		class TaskStatus(GreyCat.Enum):
			name_: Final[str] = "runtime::TaskStatus"
			def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
				super().__init__(type, attributes)
			@staticmethod
			def empty(greycat: GreyCat) -> std_.runtime.TaskStatus:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[52]
				return t.enum_values[t.generated_offsets[0]]
			@staticmethod
			def waiting(greycat: GreyCat) -> std_.runtime.TaskStatus:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[52]
				return t.enum_values[t.generated_offsets[1]]
			@staticmethod
			def running(greycat: GreyCat) -> std_.runtime.TaskStatus:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[52]
				return t.enum_values[t.generated_offsets[2]]
			@staticmethod
			def cancelled(greycat: GreyCat) -> std_.runtime.TaskStatus:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[52]
				return t.enum_values[t.generated_offsets[3]]
			@staticmethod
			def error(greycat: GreyCat) -> std_.runtime.TaskStatus:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[52]
				return t.enum_values[t.generated_offsets[4]]
			@staticmethod
			def ended(greycat: GreyCat) -> std_.runtime.TaskStatus:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[52]
				return t.enum_values[t.generated_offsets[5]]
			@staticmethod
			def create(greycat: GreyCat) -> std_.runtime.TaskStatus:
				return std_.runtime.TaskStatus(greycat.libs_by_name[std.name_].mapped[52])
		@final
		class UserRole(GreyCat.Object):
			name_: Final[str] = "runtime::UserRole"
			def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
				super().__init__(type, attributes)
			def name(self) -> str:
				return self._get(self.type_.generated_offsets[0])
			def set_name(self, v: str) -> None:
				self._set(self.type_.generated_offsets[0],v)
			def permissions(self) -> std_.core.Array:
				return self._get(self.type_.generated_offsets[1])
			def set_permissions(self, v: std_.core.Array) -> None:
				self._set(self.type_.generated_offsets[1],v)
			@staticmethod
			def all(greycat: GreyCat) -> std_.core.Array:
				return GreyCat.call(greycat,"runtime::UserRole::all")
			@staticmethod
			def remove(greycat: GreyCat, name: str) -> None:
				return GreyCat.call(greycat,"runtime::UserRole::remove", name)
			@staticmethod
			def set(greycat: GreyCat, value: std_.runtime.UserRole) -> None:
				return GreyCat.call(greycat,"runtime::UserRole::set", value)
			@staticmethod
			def create(greycat: GreyCat, name: str, permissions: std_.core.Array) -> std_.runtime.UserRole:
				return std_.runtime.UserRole(greycat.libs_by_name[std.name_].mapped[53], name, permissions)
		@final
		class SecurityPolicy(GreyCat.Object):
			name_: Final[str] = "runtime::SecurityPolicy"
			def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
				super().__init__(type, attributes)
			def entities(self) -> std_.core.Array:
				return self._get(self.type_.generated_offsets[0])
			def set_entities(self, v: std_.core.Array) -> None:
				self._set(self.type_.generated_offsets[0],v)
			def credentials(self) -> std_.core.Map:
				return self._get(self.type_.generated_offsets[1])
			def set_credentials(self, v: std_.core.Map) -> None:
				self._set(self.type_.generated_offsets[1],v)
			def roles(self) -> std_.core.Map:
				return self._get(self.type_.generated_offsets[2])
			def set_roles(self, v: std_.core.Map) -> None:
				self._set(self.type_.generated_offsets[2],v)
			def fields(self) -> std_.runtime.SecurityFields:
				return self._get(self.type_.generated_offsets[3])
			def set_fields(self, v: std_.runtime.SecurityFields) -> None:
				self._set(self.type_.generated_offsets[3],v)
			@staticmethod
			def permissions(greycat: GreyCat) -> std_.core.Array:
				return GreyCat.call(greycat,"runtime::SecurityPolicy::permissions")
			@staticmethod
			def create(greycat: GreyCat, entities: std_.core.Array, credentials: std_.core.Map, roles: std_.core.Map, fields: std_.runtime.SecurityFields) -> std_.runtime.SecurityPolicy:
				return std_.runtime.SecurityPolicy(greycat.libs_by_name[std.name_].mapped[54], entities, credentials, roles, fields)
		@final
		class Runtime(GreyCat.Object):
			name_: Final[str] = "runtime::Runtime"
			def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
				super().__init__(type, attributes)
			@staticmethod
			def info(greycat: GreyCat) -> std_.runtime.RuntimeInfo:
				return GreyCat.call(greycat,"runtime::Runtime::info")
			@staticmethod
			def abi(greycat: GreyCat) -> None:
				return GreyCat.call(greycat,"runtime::Runtime::abi")
			@staticmethod
			def readModVar(greycat: GreyCat, module: str, name: str) -> Any:
				return GreyCat.call(greycat,"runtime::Runtime::readModVar", module, name)
			@staticmethod
			def create(greycat: GreyCat) -> std_.runtime.Runtime:
				return std_.runtime.Runtime(greycat.libs_by_name[std.name_].mapped[55])
		@final
		class TaskInfo(GreyCat.Object):
			name_: Final[str] = "runtime::TaskInfo"
			def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
				super().__init__(type, attributes)
			def user_id(self) -> int:
				return self._get(self.type_.generated_offsets[0])
			def set_user_id(self, v: int) -> None:
				self._set(self.type_.generated_offsets[0],v)
			def task_id(self) -> int:
				return self._get(self.type_.generated_offsets[1])
			def set_task_id(self, v: int) -> None:
				self._set(self.type_.generated_offsets[1],v)
			def mod(self) -> str:
				return self._get(self.type_.generated_offsets[2])
			def set_mod(self, v: str) -> None:
				self._set(self.type_.generated_offsets[2],v)
			def type(self) -> str:
				return self._get(self.type_.generated_offsets[3])
			def set_type(self, v: str) -> None:
				self._set(self.type_.generated_offsets[3],v)
			def fun(self) -> str:
				return self._get(self.type_.generated_offsets[4])
			def set_fun(self, v: str) -> None:
				self._set(self.type_.generated_offsets[4],v)
			def creation(self) -> std.core.time:
				return self._get(self.type_.generated_offsets[5])
			def set_creation(self, v: std.core.time) -> None:
				self._set(self.type_.generated_offsets[5],v)
			def status(self) -> std_.runtime.TaskStatus:
				return self._get(self.type_.generated_offsets[6])
			def set_status(self, v: std_.runtime.TaskStatus) -> None:
				self._set(self.type_.generated_offsets[6],v)
			def start(self) -> std.core.time:
				return self._get(self.type_.generated_offsets[7])
			def set_start(self, v: std.core.time) -> None:
				self._set(self.type_.generated_offsets[7],v)
			def progress(self) -> float:
				return self._get(self.type_.generated_offsets[8])
			def set_progress(self, v: float) -> None:
				self._set(self.type_.generated_offsets[8],v)
			def remaining(self) -> std.core.duration:
				return self._get(self.type_.generated_offsets[9])
			def set_remaining(self, v: std.core.duration) -> None:
				self._set(self.type_.generated_offsets[9],v)
			def duration(self) -> std.core.duration:
				return self._get(self.type_.generated_offsets[10])
			def set_duration(self, v: std.core.duration) -> None:
				self._set(self.type_.generated_offsets[10],v)
			def sub_waiting(self) -> int:
				return self._get(self.type_.generated_offsets[11])
			def set_sub_waiting(self, v: int) -> None:
				self._set(self.type_.generated_offsets[11],v)
			def sub_tasks_all(self) -> int:
				return self._get(self.type_.generated_offsets[12])
			def set_sub_tasks_all(self, v: int) -> None:
				self._set(self.type_.generated_offsets[12],v)
			@staticmethod
			def create(greycat: GreyCat, user_id: int, task_id: int, mod: str, type: str, fun: str, creation: std.core.time, status: std_.runtime.TaskStatus, start: std.core.time, progress: float, remaining: std.core.duration, duration: std.core.duration, sub_waiting: int, sub_tasks_all: int) -> std_.runtime.TaskInfo:
				return std_.runtime.TaskInfo(greycat.libs_by_name[std.name_].mapped[56], user_id, task_id, mod, type, fun, creation, status, start, progress, remaining, duration, sub_waiting, sub_tasks_all)
		@final
		class UserGroupPolicyType(GreyCat.Enum):
			name_: Final[str] = "runtime::UserGroupPolicyType"
			def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
				super().__init__(type, attributes)
			@staticmethod
			def read(greycat: GreyCat) -> std_.runtime.UserGroupPolicyType:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[57]
				return t.enum_values[t.generated_offsets[0]]
			@staticmethod
			def write(greycat: GreyCat) -> std_.runtime.UserGroupPolicyType:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[57]
				return t.enum_values[t.generated_offsets[1]]
			@staticmethod
			def execute(greycat: GreyCat) -> std_.runtime.UserGroupPolicyType:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[57]
				return t.enum_values[t.generated_offsets[2]]
			@staticmethod
			def create(greycat: GreyCat) -> std_.runtime.UserGroupPolicyType:
				return std_.runtime.UserGroupPolicyType(greycat.libs_by_name[std.name_].mapped[57])
	@final
	class io:
		@final
		class Email(GreyCat.Object):
			name_: Final[str] = "io::Email"
			def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
				super().__init__(type, attributes)
			def from_(self) -> str:
				return self._get(self.type_.generated_offsets[0])
			def set_from(self, v: str) -> None:
				self._set(self.type_.generated_offsets[0],v)
			def subject(self) -> str:
				return self._get(self.type_.generated_offsets[1])
			def set_subject(self, v: str) -> None:
				self._set(self.type_.generated_offsets[1],v)
			def body(self) -> str:
				return self._get(self.type_.generated_offsets[2])
			def set_body(self, v: str) -> None:
				self._set(self.type_.generated_offsets[2],v)
			def body_is_html(self) -> bool:
				return self._get(self.type_.generated_offsets[3])
			def set_body_is_html(self, v: bool) -> None:
				self._set(self.type_.generated_offsets[3],v)
			def to(self) -> std_.core.Array:
				return self._get(self.type_.generated_offsets[4])
			def set_to(self, v: std_.core.Array) -> None:
				self._set(self.type_.generated_offsets[4],v)
			def cc(self) -> std_.core.Array:
				return self._get(self.type_.generated_offsets[5])
			def set_cc(self, v: std_.core.Array) -> None:
				self._set(self.type_.generated_offsets[5],v)
			def bcc(self) -> std_.core.Array:
				return self._get(self.type_.generated_offsets[6])
			def set_bcc(self, v: std_.core.Array) -> None:
				self._set(self.type_.generated_offsets[6],v)
			@staticmethod
			def create(greycat: GreyCat, from_: str, subject: str, body: str, body_is_html: bool, to: std_.core.Array, cc: std_.core.Array, bcc: std_.core.Array) -> std_.io.Email:
				return std_.io.Email(greycat.libs_by_name[std.name_].mapped[58], from_, subject, body, body_is_html, to, cc, bcc)
		@final
		class Smtp(GreyCat.Object):
			name_: Final[str] = "io::Smtp"
			def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
				super().__init__(type, attributes)
			def host(self) -> str:
				return self._get(self.type_.generated_offsets[0])
			def set_host(self, v: str) -> None:
				self._set(self.type_.generated_offsets[0],v)
			def port(self) -> int:
				return self._get(self.type_.generated_offsets[1])
			def set_port(self, v: int) -> None:
				self._set(self.type_.generated_offsets[1],v)
			def mode(self) -> std_.io.SmtpMode:
				return self._get(self.type_.generated_offsets[2])
			def set_mode(self, v: std_.io.SmtpMode) -> None:
				self._set(self.type_.generated_offsets[2],v)
			def authenticate(self) -> std_.io.SmtpAuth:
				return self._get(self.type_.generated_offsets[3])
			def set_authenticate(self, v: std_.io.SmtpAuth) -> None:
				self._set(self.type_.generated_offsets[3],v)
			def user(self) -> str:
				return self._get(self.type_.generated_offsets[4])
			def set_user(self, v: str) -> None:
				self._set(self.type_.generated_offsets[4],v)
			def pass_(self) -> str:
				return self._get(self.type_.generated_offsets[5])
			def set_pass(self, v: str) -> None:
				self._set(self.type_.generated_offsets[5],v)
			@staticmethod
			def create(greycat: GreyCat, host: str, port: int, mode: std_.io.SmtpMode, authenticate: std_.io.SmtpAuth, user: str, pass_: str) -> std_.io.Smtp:
				return std_.io.Smtp(greycat.libs_by_name[std.name_].mapped[59], host, port, mode, authenticate, user, pass_)
		@final
		class CsvFormat(GreyCat.Object):
			name_: Final[str] = "io::CsvFormat"
			def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
				super().__init__(type, attributes)
			def header_lines(self) -> int:
				return self._get(self.type_.generated_offsets[0])
			def set_header_lines(self, v: int) -> None:
				self._set(self.type_.generated_offsets[0],v)
			def infer(self) -> bool:
				return self._get(self.type_.generated_offsets[1])
			def set_infer(self, v: bool) -> None:
				self._set(self.type_.generated_offsets[1],v)
			def separator(self) -> c_char:
				return self._get(self.type_.generated_offsets[2])
			def set_separator(self, v: c_char) -> None:
				self._set(self.type_.generated_offsets[2],v)
			def string_delimiter(self) -> c_char:
				return self._get(self.type_.generated_offsets[3])
			def set_string_delimiter(self, v: c_char) -> None:
				self._set(self.type_.generated_offsets[3],v)
			def decimal_separator(self) -> c_char:
				return self._get(self.type_.generated_offsets[4])
			def set_decimal_separator(self, v: c_char) -> None:
				self._set(self.type_.generated_offsets[4],v)
			def thousands_separator(self) -> c_char:
				return self._get(self.type_.generated_offsets[5])
			def set_thousands_separator(self, v: c_char) -> None:
				self._set(self.type_.generated_offsets[5],v)
			def columns(self) -> std_.core.Array:
				return self._get(self.type_.generated_offsets[6])
			def set_columns(self, v: std_.core.Array) -> None:
				self._set(self.type_.generated_offsets[6],v)
			@staticmethod
			def create(greycat: GreyCat, header_lines: int, infer: bool, separator: c_char, string_delimiter: c_char, decimal_separator: c_char, thousands_separator: c_char, columns: std_.core.Array) -> std_.io.CsvFormat:
				return std_.io.CsvFormat(greycat.libs_by_name[std.name_].mapped[60], header_lines, infer, separator, string_delimiter, decimal_separator, thousands_separator, columns)
		@final
		class CsvColumnDuration(GreyCat.Object):
			name_: Final[str] = "io::CsvColumnDuration"
			def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
				super().__init__(type, attributes)
			def name(self) -> str:
				return self._get(self.type_.generated_offsets[0])
			def set_name(self, v: str) -> None:
				self._set(self.type_.generated_offsets[0],v)
			def mandatory(self) -> bool:
				return self._get(self.type_.generated_offsets[1])
			def set_mandatory(self, v: bool) -> None:
				self._set(self.type_.generated_offsets[1],v)
			def unit(self) -> std_.core.DurationUnit:
				return self._get(self.type_.generated_offsets[2])
			def set_unit(self, v: std_.core.DurationUnit) -> None:
				self._set(self.type_.generated_offsets[2],v)
			@staticmethod
			def create(greycat: GreyCat, name: str, mandatory: bool, unit: std_.core.DurationUnit) -> std_.io.CsvColumnDuration:
				return std_.io.CsvColumnDuration(greycat.libs_by_name[std.name_].mapped[61], name, mandatory, unit)
		@final
		class CsvColumnInteger(GreyCat.Object):
			name_: Final[str] = "io::CsvColumnInteger"
			def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
				super().__init__(type, attributes)
			def name(self) -> str:
				return self._get(self.type_.generated_offsets[0])
			def set_name(self, v: str) -> None:
				self._set(self.type_.generated_offsets[0],v)
			def mandatory(self) -> bool:
				return self._get(self.type_.generated_offsets[1])
			def set_mandatory(self, v: bool) -> None:
				self._set(self.type_.generated_offsets[1],v)
			@staticmethod
			def create(greycat: GreyCat, name: str, mandatory: bool) -> std_.io.CsvColumnInteger:
				return std_.io.CsvColumnInteger(greycat.libs_by_name[std.name_].mapped[62], name, mandatory)
		@final
		class HttpHeader(GreyCat.Object):
			name_: Final[str] = "io::HttpHeader"
			def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
				super().__init__(type, attributes)
			def name(self) -> str:
				return self._get(self.type_.generated_offsets[0])
			def set_name(self, v: str) -> None:
				self._set(self.type_.generated_offsets[0],v)
			def value(self) -> str:
				return self._get(self.type_.generated_offsets[1])
			def set_value(self, v: str) -> None:
				self._set(self.type_.generated_offsets[1],v)
			@staticmethod
			def create(greycat: GreyCat, name: str, value: str) -> std_.io.HttpHeader:
				return std_.io.HttpHeader(greycat.libs_by_name[std.name_].mapped[63], name, value)
		@final
		class SmtpMode(GreyCat.Enum):
			name_: Final[str] = "io::SmtpMode"
			def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
				super().__init__(type, attributes)
			@staticmethod
			def plain(greycat: GreyCat) -> std_.io.SmtpMode:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[64]
				return t.enum_values[t.generated_offsets[0]]
			@staticmethod
			def ssl_tls(greycat: GreyCat) -> std_.io.SmtpMode:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[64]
				return t.enum_values[t.generated_offsets[1]]
			@staticmethod
			def starttls(greycat: GreyCat) -> std_.io.SmtpMode:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[64]
				return t.enum_values[t.generated_offsets[2]]
			@staticmethod
			def create(greycat: GreyCat) -> std_.io.SmtpMode:
				return std_.io.SmtpMode(greycat.libs_by_name[std.name_].mapped[64])
		@final
		class Url(GreyCat.Object):
			name_: Final[str] = "io::Url"
			def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
				super().__init__(type, attributes)
			def protocol(self) -> str:
				return self._get(self.type_.generated_offsets[0])
			def set_protocol(self, v: str) -> None:
				self._set(self.type_.generated_offsets[0],v)
			def host(self) -> str:
				return self._get(self.type_.generated_offsets[1])
			def set_host(self, v: str) -> None:
				self._set(self.type_.generated_offsets[1],v)
			def port(self) -> int:
				return self._get(self.type_.generated_offsets[2])
			def set_port(self, v: int) -> None:
				self._set(self.type_.generated_offsets[2],v)
			def path(self) -> str:
				return self._get(self.type_.generated_offsets[3])
			def set_path(self, v: str) -> None:
				self._set(self.type_.generated_offsets[3],v)
			def params(self) -> std_.core.Map:
				return self._get(self.type_.generated_offsets[4])
			def set_params(self, v: std_.core.Map) -> None:
				self._set(self.type_.generated_offsets[4],v)
			def hash(self) -> str:
				return self._get(self.type_.generated_offsets[5])
			def set_hash(self, v: str) -> None:
				self._set(self.type_.generated_offsets[5],v)
			@staticmethod
			def create(greycat: GreyCat, protocol: str, host: str, port: int, path: str, params: std_.core.Map, hash: str) -> std_.io.Url:
				return std_.io.Url(greycat.libs_by_name[std.name_].mapped[65], protocol, host, port, path, params, hash)
		@final
		class CsvColumnFloat(GreyCat.Object):
			name_: Final[str] = "io::CsvColumnFloat"
			def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
				super().__init__(type, attributes)
			def name(self) -> str:
				return self._get(self.type_.generated_offsets[0])
			def set_name(self, v: str) -> None:
				self._set(self.type_.generated_offsets[0],v)
			def mandatory(self) -> bool:
				return self._get(self.type_.generated_offsets[1])
			def set_mandatory(self, v: bool) -> None:
				self._set(self.type_.generated_offsets[1],v)
			@staticmethod
			def create(greycat: GreyCat, name: str, mandatory: bool) -> std_.io.CsvColumnFloat:
				return std_.io.CsvColumnFloat(greycat.libs_by_name[std.name_].mapped[66], name, mandatory)
		@final
		class CsvColumn(GreyCat.Object):
			name_: Final[str] = "io::CsvColumn"
			def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
				super().__init__(type, attributes)
			def name(self) -> str:
				return self._get(self.type_.generated_offsets[0])
			def set_name(self, v: str) -> None:
				self._set(self.type_.generated_offsets[0],v)
			def mandatory(self) -> bool:
				return self._get(self.type_.generated_offsets[1])
			def set_mandatory(self, v: bool) -> None:
				self._set(self.type_.generated_offsets[1],v)
			@staticmethod
			def create(greycat: GreyCat, name: str, mandatory: bool) -> std_.io.CsvColumn:
				return std_.io.CsvColumn(greycat.libs_by_name[std.name_].mapped[67], name, mandatory)
		@final
		class File(GreyCat.Object):
			name_: Final[str] = "io::File"
			def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
				super().__init__(type, attributes)
			def path(self) -> str:
				return self._get(self.type_.generated_offsets[0])
			def set_path(self, v: str) -> None:
				self._set(self.type_.generated_offsets[0],v)
			def size(self) -> int:
				return self._get(self.type_.generated_offsets[1])
			def set_size(self, v: int) -> None:
				self._set(self.type_.generated_offsets[1],v)
			def last_modification(self) -> std.core.time:
				return self._get(self.type_.generated_offsets[2])
			def set_last_modification(self, v: std.core.time) -> None:
				self._set(self.type_.generated_offsets[2],v)
			@staticmethod
			def create(greycat: GreyCat, path: str, size: int, last_modification: std.core.time) -> std_.io.File:
				return std_.io.File(greycat.libs_by_name[std.name_].mapped[68], path, size, last_modification)
		@final
		class Http(GreyCat.Object):
			name_: Final[str] = "io::Http"
			def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
				super().__init__(type, attributes)
			@staticmethod
			def create(greycat: GreyCat) -> std_.io.Http:
				return std_.io.Http(greycat.libs_by_name[std.name_].mapped[69])
		@final
		class CsvColumnTime(GreyCat.Object):
			name_: Final[str] = "io::CsvColumnTime"
			def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
				super().__init__(type, attributes)
			def name(self) -> str:
				return self._get(self.type_.generated_offsets[0])
			def set_name(self, v: str) -> None:
				self._set(self.type_.generated_offsets[0],v)
			def mandatory(self) -> bool:
				return self._get(self.type_.generated_offsets[1])
			def set_mandatory(self, v: bool) -> None:
				self._set(self.type_.generated_offsets[1],v)
			def unit(self) -> std_.core.DurationUnit:
				return self._get(self.type_.generated_offsets[2])
			def set_unit(self, v: std_.core.DurationUnit) -> None:
				self._set(self.type_.generated_offsets[2],v)
			@staticmethod
			def create(greycat: GreyCat, name: str, mandatory: bool, unit: std_.core.DurationUnit) -> std_.io.CsvColumnTime:
				return std_.io.CsvColumnTime(greycat.libs_by_name[std.name_].mapped[70], name, mandatory, unit)
		@final
		class SmtpAuth(GreyCat.Enum):
			name_: Final[str] = "io::SmtpAuth"
			def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
				super().__init__(type, attributes)
			@staticmethod
			def none(greycat: GreyCat) -> std_.io.SmtpAuth:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[71]
				return t.enum_values[t.generated_offsets[0]]
			@staticmethod
			def plain(greycat: GreyCat) -> std_.io.SmtpAuth:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[71]
				return t.enum_values[t.generated_offsets[1]]
			@staticmethod
			def login(greycat: GreyCat) -> std_.io.SmtpAuth:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[71]
				return t.enum_values[t.generated_offsets[2]]
			@staticmethod
			def create(greycat: GreyCat) -> std_.io.SmtpAuth:
				return std_.io.SmtpAuth(greycat.libs_by_name[std.name_].mapped[71])
		@final
		class CsvColumnDate(GreyCat.Object):
			name_: Final[str] = "io::CsvColumnDate"
			def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
				super().__init__(type, attributes)
			def name(self) -> str:
				return self._get(self.type_.generated_offsets[0])
			def set_name(self, v: str) -> None:
				self._set(self.type_.generated_offsets[0],v)
			def mandatory(self) -> bool:
				return self._get(self.type_.generated_offsets[1])
			def set_mandatory(self, v: bool) -> None:
				self._set(self.type_.generated_offsets[1],v)
			def format(self) -> str:
				return self._get(self.type_.generated_offsets[2])
			def set_format(self, v: str) -> None:
				self._set(self.type_.generated_offsets[2],v)
			def tz(self) -> std_.core.TimeZone:
				return self._get(self.type_.generated_offsets[3])
			def set_tz(self, v: std_.core.TimeZone) -> None:
				self._set(self.type_.generated_offsets[3],v)
			def as_time(self) -> bool:
				return self._get(self.type_.generated_offsets[4])
			def set_as_time(self, v: bool) -> None:
				self._set(self.type_.generated_offsets[4],v)
			@staticmethod
			def create(greycat: GreyCat, name: str, mandatory: bool, format: str, tz: std_.core.TimeZone, as_time: bool) -> std_.io.CsvColumnDate:
				return std_.io.CsvColumnDate(greycat.libs_by_name[std.name_].mapped[72], name, mandatory, format, tz, as_time)
		@final
		class CsvColumnString(GreyCat.Object):
			name_: Final[str] = "io::CsvColumnString"
			def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
				super().__init__(type, attributes)
			def name(self) -> str:
				return self._get(self.type_.generated_offsets[0])
			def set_name(self, v: str) -> None:
				self._set(self.type_.generated_offsets[0],v)
			def mandatory(self) -> bool:
				return self._get(self.type_.generated_offsets[1])
			def set_mandatory(self, v: bool) -> None:
				self._set(self.type_.generated_offsets[1],v)
			def trim(self) -> bool:
				return self._get(self.type_.generated_offsets[2])
			def set_trim(self, v: bool) -> None:
				self._set(self.type_.generated_offsets[2],v)
			def try_number(self) -> bool:
				return self._get(self.type_.generated_offsets[3])
			def set_try_number(self, v: bool) -> None:
				self._set(self.type_.generated_offsets[3],v)
			def try_json(self) -> bool:
				return self._get(self.type_.generated_offsets[4])
			def set_try_json(self, v: bool) -> None:
				self._set(self.type_.generated_offsets[4],v)
			def values(self) -> std_.core.Array:
				return self._get(self.type_.generated_offsets[5])
			def set_values(self, v: std_.core.Array) -> None:
				self._set(self.type_.generated_offsets[5],v)
			def encoder(self) -> std_.io.TextEncoder:
				return self._get(self.type_.generated_offsets[6])
			def set_encoder(self, v: std_.io.TextEncoder) -> None:
				self._set(self.type_.generated_offsets[6],v)
			@staticmethod
			def create(greycat: GreyCat, name: str, mandatory: bool, trim: bool, try_number: bool, try_json: bool, values: std_.core.Array, encoder: std_.io.TextEncoder) -> std_.io.CsvColumnString:
				return std_.io.CsvColumnString(greycat.libs_by_name[std.name_].mapped[73], name, mandatory, trim, try_number, try_json, values, encoder)
		@final
		class CsvColumnBoolean(GreyCat.Object):
			name_: Final[str] = "io::CsvColumnBoolean"
			def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
				super().__init__(type, attributes)
			def name(self) -> str:
				return self._get(self.type_.generated_offsets[0])
			def set_name(self, v: str) -> None:
				self._set(self.type_.generated_offsets[0],v)
			def mandatory(self) -> bool:
				return self._get(self.type_.generated_offsets[1])
			def set_mandatory(self, v: bool) -> None:
				self._set(self.type_.generated_offsets[1],v)
			@staticmethod
			def create(greycat: GreyCat, name: str, mandatory: bool) -> std_.io.CsvColumnBoolean:
				return std_.io.CsvColumnBoolean(greycat.libs_by_name[std.name_].mapped[74], name, mandatory)
		@final
		class CsvColumnIgnored(GreyCat.Object):
			name_: Final[str] = "io::CsvColumnIgnored"
			def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
				super().__init__(type, attributes)
			def name(self) -> str:
				return self._get(self.type_.generated_offsets[0])
			def set_name(self, v: str) -> None:
				self._set(self.type_.generated_offsets[0],v)
			def mandatory(self) -> bool:
				return self._get(self.type_.generated_offsets[1])
			def set_mandatory(self, v: bool) -> None:
				self._set(self.type_.generated_offsets[1],v)
			@staticmethod
			def create(greycat: GreyCat, name: str, mandatory: bool) -> std_.io.CsvColumnIgnored:
				return std_.io.CsvColumnIgnored(greycat.libs_by_name[std.name_].mapped[75], name, mandatory)
		@final
		class TextEncoder(GreyCat.Enum):
			name_: Final[str] = "io::TextEncoder"
			def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
				super().__init__(type, attributes)
			@staticmethod
			def plain(greycat: GreyCat) -> std_.io.TextEncoder:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[76]
				return t.enum_values[t.generated_offsets[0]]
			@staticmethod
			def base64(greycat: GreyCat) -> std_.io.TextEncoder:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[76]
				return t.enum_values[t.generated_offsets[1]]
			@staticmethod
			def base64url(greycat: GreyCat) -> std_.io.TextEncoder:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[76]
				return t.enum_values[t.generated_offsets[2]]
			@staticmethod
			def hexadecimal(greycat: GreyCat) -> std_.io.TextEncoder:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[76]
				return t.enum_values[t.generated_offsets[3]]
			@staticmethod
			def create(greycat: GreyCat) -> std_.io.TextEncoder:
				return std_.io.TextEncoder(greycat.libs_by_name[std.name_].mapped[76])
	@final
	class math:
		@final
		class MathConstants(GreyCat.Object):
			name_: Final[str] = "math::MathConstants"
			def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
				super().__init__(type, attributes)
			@staticmethod
			def e(greycat: GreyCat) -> float:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[77]
				return t.static_values[0]
			@staticmethod
			def log_2e(greycat: GreyCat) -> float:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[77]
				return t.static_values[1]
			@staticmethod
			def log_10e(greycat: GreyCat) -> float:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[77]
				return t.static_values[2]
			@staticmethod
			def ln2(greycat: GreyCat) -> float:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[77]
				return t.static_values[3]
			@staticmethod
			def ln10(greycat: GreyCat) -> float:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[77]
				return t.static_values[4]
			@staticmethod
			def pi(greycat: GreyCat) -> float:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[77]
				return t.static_values[5]
			@staticmethod
			def pi_2(greycat: GreyCat) -> float:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[77]
				return t.static_values[6]
			@staticmethod
			def pi_4(greycat: GreyCat) -> float:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[77]
				return t.static_values[7]
			@staticmethod
			def m1_pi(greycat: GreyCat) -> float:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[77]
				return t.static_values[8]
			@staticmethod
			def m2_pi(greycat: GreyCat) -> float:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[77]
				return t.static_values[9]
			@staticmethod
			def m2_sqrt_pi(greycat: GreyCat) -> float:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[77]
				return t.static_values[10]
			@staticmethod
			def sqrt2(greycat: GreyCat) -> float:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[77]
				return t.static_values[11]
			@staticmethod
			def sqrt1_2(greycat: GreyCat) -> float:
				t: Final[GreyCat.Type] = greycat.libs_by_name[std.name_].mapped[77]
				return t.static_values[12]
			@staticmethod
			def create(greycat: GreyCat) -> std_.math.MathConstants:
				return std_.math.MathConstants(greycat.libs_by_name[std.name_].mapped[77])
	@final
	class util:
		@final
		class SlidingWindow(std_n.util._SlidingWindow):
			name_: Final[str] = "util::SlidingWindow"
			def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
				super().__init__(type)
			@staticmethod
			def create(greycat: GreyCat) -> std_n.util._SlidingWindow:
				return std.util.SlidingWindow(greycat.libs_by_name[std.name_].mapped[78])
		@final
		class Assert(GreyCat.Object):
			name_: Final[str] = "util::Assert"
			def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
				super().__init__(type, attributes)
			@staticmethod
			def create(greycat: GreyCat) -> std_.util.Assert:
				return std_.util.Assert(greycat.libs_by_name[std.name_].mapped[79])
		@final
		class Iban(std_n.util._Iban):
			name_: Final[str] = "util::Iban"
			def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
				super().__init__(type)
			@staticmethod
			def create(greycat: GreyCat) -> std_n.util._Iban:
				return std.util.Iban(greycat.libs_by_name[std.name_].mapped[80])
		@final
		class BoxPlotFloat(GreyCat.Object):
			name_: Final[str] = "util::BoxPlotFloat"
			def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
				super().__init__(type, attributes)
			def min(self) -> float:
				return self._get(self.type_.generated_offsets[0])
			def set_min(self, v: float) -> None:
				self._set(self.type_.generated_offsets[0],v)
			def max(self) -> float:
				return self._get(self.type_.generated_offsets[1])
			def set_max(self, v: float) -> None:
				self._set(self.type_.generated_offsets[1],v)
			def whiskerLow(self) -> float:
				return self._get(self.type_.generated_offsets[2])
			def set_whiskerLow(self, v: float) -> None:
				self._set(self.type_.generated_offsets[2],v)
			def whiskerHigh(self) -> float:
				return self._get(self.type_.generated_offsets[3])
			def set_whiskerHigh(self, v: float) -> None:
				self._set(self.type_.generated_offsets[3],v)
			def percentile1(self) -> float:
				return self._get(self.type_.generated_offsets[4])
			def set_percentile1(self, v: float) -> None:
				self._set(self.type_.generated_offsets[4],v)
			def percentile5(self) -> float:
				return self._get(self.type_.generated_offsets[5])
			def set_percentile5(self, v: float) -> None:
				self._set(self.type_.generated_offsets[5],v)
			def percentile25(self) -> float:
				return self._get(self.type_.generated_offsets[6])
			def set_percentile25(self, v: float) -> None:
				self._set(self.type_.generated_offsets[6],v)
			def percentile50(self) -> float:
				return self._get(self.type_.generated_offsets[7])
			def set_percentile50(self, v: float) -> None:
				self._set(self.type_.generated_offsets[7],v)
			def percentile75(self) -> float:
				return self._get(self.type_.generated_offsets[8])
			def set_percentile75(self, v: float) -> None:
				self._set(self.type_.generated_offsets[8],v)
			def percentile95(self) -> float:
				return self._get(self.type_.generated_offsets[9])
			def set_percentile95(self, v: float) -> None:
				self._set(self.type_.generated_offsets[9],v)
			def percentile99(self) -> float:
				return self._get(self.type_.generated_offsets[10])
			def set_percentile99(self, v: float) -> None:
				self._set(self.type_.generated_offsets[10],v)
			def countOutliersLow(self) -> int:
				return self._get(self.type_.generated_offsets[11])
			def set_countOutliersLow(self, v: int) -> None:
				self._set(self.type_.generated_offsets[11],v)
			def countOutliersHigh(self) -> int:
				return self._get(self.type_.generated_offsets[12])
			def set_countOutliersHigh(self, v: int) -> None:
				self._set(self.type_.generated_offsets[12],v)
			def percentageOutliersLow(self) -> float:
				return self._get(self.type_.generated_offsets[13])
			def set_percentageOutliersLow(self, v: float) -> None:
				self._set(self.type_.generated_offsets[13],v)
			def percentageOutliersHigh(self) -> float:
				return self._get(self.type_.generated_offsets[14])
			def set_percentageOutliersHigh(self, v: float) -> None:
				self._set(self.type_.generated_offsets[14],v)
			def sum(self) -> float:
				return self._get(self.type_.generated_offsets[15])
			def set_sum(self, v: float) -> None:
				self._set(self.type_.generated_offsets[15],v)
			def avg(self) -> float:
				return self._get(self.type_.generated_offsets[16])
			def set_avg(self, v: float) -> None:
				self._set(self.type_.generated_offsets[16],v)
			def std(self) -> float:
				return self._get(self.type_.generated_offsets[17])
			def set_std(self, v: float) -> None:
				self._set(self.type_.generated_offsets[17],v)
			def size(self) -> int:
				return self._get(self.type_.generated_offsets[18])
			def set_size(self, v: int) -> None:
				self._set(self.type_.generated_offsets[18],v)
			@staticmethod
			def create(greycat: GreyCat, min: float, max: float, whiskerLow: float, whiskerHigh: float, percentile1: float, percentile5: float, percentile25: float, percentile50: float, percentile75: float, percentile95: float, percentile99: float, countOutliersLow: int, countOutliersHigh: int, percentageOutliersLow: float, percentageOutliersHigh: float, sum: float, avg: float, std: float, size: int) -> std_.util.BoxPlotFloat:
				return std_.util.BoxPlotFloat(greycat.libs_by_name[std.name_].mapped[81], min, max, whiskerLow, whiskerHigh, percentile1, percentile5, percentile25, percentile50, percentile75, percentile95, percentile99, countOutliersLow, countOutliersHigh, percentageOutliersLow, percentageOutliersHigh, sum, avg, std, size)
		@final
		class Random(GreyCat.Object):
			name_: Final[str] = "util::Random"
			def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
				super().__init__(type, attributes)
			def seed(self) -> int:
				return self._get(self.type_.generated_offsets[0])
			def set_seed(self, v: int) -> None:
				self._set(self.type_.generated_offsets[0],v)
			def v(self) -> float:
				return self._get(self.type_.generated_offsets[1])
			def set_v(self, v: float) -> None:
				self._set(self.type_.generated_offsets[1],v)
			@staticmethod
			def create(greycat: GreyCat, seed: int, v: float) -> std_.util.Random:
				return std_.util.Random(greycat.libs_by_name[std.name_].mapped[82], seed, v)
		@final
		class Crypto(GreyCat.Object):
			name_: Final[str] = "util::Crypto"
			def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
				super().__init__(type, attributes)
			@staticmethod
			def create(greycat: GreyCat) -> std_.util.Crypto:
				return std_.util.Crypto(greycat.libs_by_name[std.name_].mapped[83])
		@final
		class TimeWindow(std_n.util._TimeWindow):
			name_: Final[str] = "util::TimeWindow"
			def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
				super().__init__(type)
			@staticmethod
			def create(greycat: GreyCat) -> std_n.util._TimeWindow:
				return std.util.TimeWindow(greycat.libs_by_name[std.name_].mapped[84])
		@final
		class ProgressTracker(GreyCat.Object):
			name_: Final[str] = "util::ProgressTracker"
			def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
				super().__init__(type, attributes)
			def start(self) -> std.core.time:
				return self._get(self.type_.generated_offsets[0])
			def set_start(self, v: std.core.time) -> None:
				self._set(self.type_.generated_offsets[0],v)
			def total(self) -> int:
				return self._get(self.type_.generated_offsets[1])
			def set_total(self, v: int) -> None:
				self._set(self.type_.generated_offsets[1],v)
			def counter(self) -> int:
				return self._get(self.type_.generated_offsets[2])
			def set_counter(self, v: int) -> None:
				self._set(self.type_.generated_offsets[2],v)
			def duration(self) -> std.core.duration:
				return self._get(self.type_.generated_offsets[3])
			def set_duration(self, v: std.core.duration) -> None:
				self._set(self.type_.generated_offsets[3],v)
			def progress(self) -> float:
				return self._get(self.type_.generated_offsets[4])
			def set_progress(self, v: float) -> None:
				self._set(self.type_.generated_offsets[4],v)
			def speed(self) -> float:
				return self._get(self.type_.generated_offsets[5])
			def set_speed(self, v: float) -> None:
				self._set(self.type_.generated_offsets[5],v)
			def remaining(self) -> std.core.duration:
				return self._get(self.type_.generated_offsets[6])
			def set_remaining(self, v: std.core.duration) -> None:
				self._set(self.type_.generated_offsets[6],v)
			@staticmethod
			def create(greycat: GreyCat, start: std.core.time, total: int, counter: int, duration: std.core.duration, progress: float, speed: float, remaining: std.core.duration) -> std_.util.ProgressTracker:
				return std_.util.ProgressTracker(greycat.libs_by_name[std.name_].mapped[85], start, total, counter, duration, progress, speed, remaining)
		@final
		class Quantizer(std_n.util._Quantizer):
			name_: Final[str] = "util::Quantizer"
			def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
				super().__init__(type)
			@staticmethod
			def create(greycat: GreyCat) -> std_n.util._Quantizer:
				return std.util.Quantizer(greycat.libs_by_name[std.name_].mapped[86])
		@final
		class Gaussian(GreyCat.Object):
			name_: Final[str] = "util::Gaussian"
			def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
				super().__init__(type, attributes)
			def sum(self) -> float:
				return self._get(self.type_.generated_offsets[0])
			def set_sum(self, v: float) -> None:
				self._set(self.type_.generated_offsets[0],v)
			def sum_sq(self) -> float:
				return self._get(self.type_.generated_offsets[1])
			def set_sum_sq(self, v: float) -> None:
				self._set(self.type_.generated_offsets[1],v)
			def count(self) -> int:
				return self._get(self.type_.generated_offsets[2])
			def set_count(self, v: int) -> None:
				self._set(self.type_.generated_offsets[2],v)
			def min(self) -> float:
				return self._get(self.type_.generated_offsets[3])
			def set_min(self, v: float) -> None:
				self._set(self.type_.generated_offsets[3],v)
			def max(self) -> float:
				return self._get(self.type_.generated_offsets[4])
			def set_max(self, v: float) -> None:
				self._set(self.type_.generated_offsets[4],v)
			@staticmethod
			def create(greycat: GreyCat, sum: float, sum_sq: float, count: int, min: float, max: float) -> std_.util.Gaussian:
				return std_.util.Gaussian(greycat.libs_by_name[std.name_].mapped[87], sum, sum_sq, count, min, max)
		@final
		class Queue(Generic[_T], std_n.util._Queue[_T]):
			name_: Final[str] = "util::Queue"
			def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
				super().__init__(type)
			@staticmethod
			def create(greycat: GreyCat) -> std_n.util._Queue:
				return std.util.Queue(greycat.libs_by_name[std.name_].mapped[88])
		@final
		class GaussianProfile(std_n.util._GaussianProfile):
			name_: Final[str] = "util::GaussianProfile"
			def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
				super().__init__(type)
			@staticmethod
			def create(greycat: GreyCat) -> std_n.util._GaussianProfile:
				return std.util.GaussianProfile(greycat.libs_by_name[std.name_].mapped[89])
		@final
		class HistogramInt(std_n.util._HistogramInt):
			name_: Final[str] = "util::HistogramInt"
			def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
				super().__init__(type)
			@staticmethod
			def create(greycat: GreyCat) -> std_n.util._HistogramInt:
				return std.util.HistogramInt(greycat.libs_by_name[std.name_].mapped[90])
		@final
		class Buffer(std_n.util._Buffer):
			name_: Final[str] = "util::Buffer"
			def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
				super().__init__(type)
			@staticmethod
			def create(greycat: GreyCat) -> std_n.util._Buffer:
				return std.util.Buffer(greycat.libs_by_name[std.name_].mapped[91])
		@final
		class BoxPlotInt(GreyCat.Object):
			name_: Final[str] = "util::BoxPlotInt"
			def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
				super().__init__(type, attributes)
			def min(self) -> int:
				return self._get(self.type_.generated_offsets[0])
			def set_min(self, v: int) -> None:
				self._set(self.type_.generated_offsets[0],v)
			def max(self) -> int:
				return self._get(self.type_.generated_offsets[1])
			def set_max(self, v: int) -> None:
				self._set(self.type_.generated_offsets[1],v)
			def whiskerLow(self) -> int:
				return self._get(self.type_.generated_offsets[2])
			def set_whiskerLow(self, v: int) -> None:
				self._set(self.type_.generated_offsets[2],v)
			def whiskerHigh(self) -> int:
				return self._get(self.type_.generated_offsets[3])
			def set_whiskerHigh(self, v: int) -> None:
				self._set(self.type_.generated_offsets[3],v)
			def percentile1(self) -> int:
				return self._get(self.type_.generated_offsets[4])
			def set_percentile1(self, v: int) -> None:
				self._set(self.type_.generated_offsets[4],v)
			def percentile5(self) -> int:
				return self._get(self.type_.generated_offsets[5])
			def set_percentile5(self, v: int) -> None:
				self._set(self.type_.generated_offsets[5],v)
			def percentile25(self) -> int:
				return self._get(self.type_.generated_offsets[6])
			def set_percentile25(self, v: int) -> None:
				self._set(self.type_.generated_offsets[6],v)
			def percentile50(self) -> int:
				return self._get(self.type_.generated_offsets[7])
			def set_percentile50(self, v: int) -> None:
				self._set(self.type_.generated_offsets[7],v)
			def percentile75(self) -> int:
				return self._get(self.type_.generated_offsets[8])
			def set_percentile75(self, v: int) -> None:
				self._set(self.type_.generated_offsets[8],v)
			def percentile95(self) -> int:
				return self._get(self.type_.generated_offsets[9])
			def set_percentile95(self, v: int) -> None:
				self._set(self.type_.generated_offsets[9],v)
			def percentile99(self) -> int:
				return self._get(self.type_.generated_offsets[10])
			def set_percentile99(self, v: int) -> None:
				self._set(self.type_.generated_offsets[10],v)
			def countOutliersLow(self) -> int:
				return self._get(self.type_.generated_offsets[11])
			def set_countOutliersLow(self, v: int) -> None:
				self._set(self.type_.generated_offsets[11],v)
			def countOutliersHigh(self) -> int:
				return self._get(self.type_.generated_offsets[12])
			def set_countOutliersHigh(self, v: int) -> None:
				self._set(self.type_.generated_offsets[12],v)
			def percentageOutliersLow(self) -> float:
				return self._get(self.type_.generated_offsets[13])
			def set_percentageOutliersLow(self, v: float) -> None:
				self._set(self.type_.generated_offsets[13],v)
			def percentageOutliersHigh(self) -> float:
				return self._get(self.type_.generated_offsets[14])
			def set_percentageOutliersHigh(self, v: float) -> None:
				self._set(self.type_.generated_offsets[14],v)
			def sum(self) -> float:
				return self._get(self.type_.generated_offsets[15])
			def set_sum(self, v: float) -> None:
				self._set(self.type_.generated_offsets[15],v)
			def avg(self) -> float:
				return self._get(self.type_.generated_offsets[16])
			def set_avg(self, v: float) -> None:
				self._set(self.type_.generated_offsets[16],v)
			def std(self) -> float:
				return self._get(self.type_.generated_offsets[17])
			def set_std(self, v: float) -> None:
				self._set(self.type_.generated_offsets[17],v)
			def size(self) -> int:
				return self._get(self.type_.generated_offsets[18])
			def set_size(self, v: int) -> None:
				self._set(self.type_.generated_offsets[18],v)
			@staticmethod
			def create(greycat: GreyCat, min: int, max: int, whiskerLow: int, whiskerHigh: int, percentile1: int, percentile5: int, percentile25: int, percentile50: int, percentile75: int, percentile95: int, percentile99: int, countOutliersLow: int, countOutliersHigh: int, percentageOutliersLow: float, percentageOutliersHigh: float, sum: float, avg: float, std: float, size: int) -> std_.util.BoxPlotInt:
				return std_.util.BoxPlotInt(greycat.libs_by_name[std.name_].mapped[92], min, max, whiskerLow, whiskerHigh, percentile1, percentile5, percentile25, percentile50, percentile75, percentile95, percentile99, countOutliersLow, countOutliersHigh, percentageOutliersLow, percentageOutliersHigh, sum, avg, std, size)
		@final
		class HistogramFloat(std_n.util._HistogramFloat):
			name_: Final[str] = "util::HistogramFloat"
			def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
				super().__init__(type)
			@staticmethod
			def create(greycat: GreyCat) -> std_n.util._HistogramFloat:
				return std.util.HistogramFloat(greycat.libs_by_name[std.name_].mapped[93])
	def configure(self, loaders: dict[str, GreyCat.Loader], factories: dict[str, GreyCat.Factory]) -> None:
		factories[std.core.tf2d.name_] = lambda type, attributes: std.core.tf2d(type, attributes)
		loaders[std.core.tf2d.name_] = lambda type, stream: std_n.core._tf2d.load(type, stream)
		factories[std_.core.SamplingMode.name_] = lambda type, attributes: std_.core.SamplingMode(type, attributes)
		factories[std_.core.Table.name_] = lambda type, attributes: std_.core.Table(type, attributes)
		loaders[std_.core.Table.name_] = lambda type, stream: std_n.core._Table.load(type, stream)
		factories[std.core.ti6d.name_] = lambda type, attributes: std.core.ti6d(type, attributes)
		loaders[std.core.ti6d.name_] = lambda type, stream: std_n.core._ti6d.load(type, stream)
		factories[std_.core.nodeTimeSingleton.name_] = lambda type, attributes: std_.core.nodeTimeSingleton(type, attributes)
		factories[std.core.time.name_] = lambda type, attributes: std.core.time(type, attributes)
		loaders[std.core.time.name_] = lambda type, stream: std_n.core._time.load(type, stream)
		factories[std.core.nodeTime.name_] = lambda type, attributes: std.core.nodeTime(type, attributes)
		loaders[std.core.nodeTime.name_] = lambda type, stream: std_n.core._nodeTime.load(type, stream)
		factories[std_.core.DurationUnit.name_] = lambda type, attributes: std_.core.DurationUnit(type, attributes)
		factories[std_.core.NodeTimeInfo.name_] = lambda type, attributes: std_.core.NodeTimeInfo(type, attributes)
		factories[std_.core.function.name_] = lambda type, attributes: std_.core.function(type, attributes)
		loaders[std_.core.function.name_] = lambda type, stream: std_n.core._function.load(type, stream)
		factories[std_.core.Error.name_] = lambda type, attributes: std_.core.Error(type, attributes)
		loaders[std_.core.Error.name_] = lambda type, stream: std_n.core._Error.load(type, stream)
		factories[std_.core.GeoPoly.name_] = lambda type, attributes: std_.core.GeoPoly(type, attributes)
		factories[std.core.duration.name_] = lambda type, attributes: std.core.duration(type, attributes)
		loaders[std.core.duration.name_] = lambda type, stream: std_n.core._duration.load(type, stream)
		factories[std.core.ti2d.name_] = lambda type, attributes: std.core.ti2d(type, attributes)
		loaders[std.core.ti2d.name_] = lambda type, stream: std_n.core._ti2d.load(type, stream)
		factories[std_.core.ErrorCode.name_] = lambda type, attributes: std_.core.ErrorCode(type, attributes)
		factories[std.core.geo.name_] = lambda type, attributes: std.core.geo(type, attributes)
		loaders[std.core.geo.name_] = lambda type, stream: std_n.core._geo.load(type, stream)
		factories[std.core.node.name_] = lambda type, attributes: std.core.node(type, attributes)
		loaders[std.core.node.name_] = lambda type, stream: std_n.core._node.load(type, stream)
		factories[std_.core.TableColumnMeta.name_] = lambda type, attributes: std_.core.TableColumnMeta(type, attributes)
		factories[std_.core.Date.name_] = lambda type, attributes: std_.core.Date(type, attributes)
		loaders[std_.core.Date.name_] = lambda type, stream: std_n.core._Date.load(type, stream)
		factories[std_.core.Tensor.name_] = lambda type, attributes: std_.core.Tensor(type, attributes)
		loaders[std_.core.Tensor.name_] = lambda type, stream: std_n.core._Tensor.load(type, stream)
		factories[std.core.ti4d.name_] = lambda type, attributes: std.core.ti4d(type, attributes)
		loaders[std.core.ti4d.name_] = lambda type, stream: std_n.core._ti4d.load(type, stream)
		factories[std_.core.GeoCircle.name_] = lambda type, attributes: std_.core.GeoCircle(type, attributes)
		factories[std.core.nodeGeo.name_] = lambda type, attributes: std.core.nodeGeo(type, attributes)
		loaders[std.core.nodeGeo.name_] = lambda type, stream: std_n.core._nodeGeo.load(type, stream)
		factories[std.core.ti5d.name_] = lambda type, attributes: std.core.ti5d(type, attributes)
		loaders[std.core.ti5d.name_] = lambda type, stream: std_n.core._ti5d.load(type, stream)
		factories[std.core.String.name_] = lambda type, attributes: std.core.String(type, attributes)
		loaders[std.core.String.name_] = lambda type, stream: std_n.core._String.load(type, stream)
		factories[std_.core.Map.name_] = lambda type, attributes: std_.core.Map(type, attributes)
		loaders[std_.core.Map.name_] = lambda type, stream: std_n.core._Map.load(type, stream)
		factories[std_.core.TensorType.name_] = lambda type, attributes: std_.core.TensorType(type, attributes)
		factories[std_.core.TimeZone.name_] = lambda type, attributes: std_.core.TimeZone(type, attributes)
		factories[std_.core.GeoBox.name_] = lambda type, attributes: std_.core.GeoBox(type, attributes)
		factories[std_.core.Tuple.name_] = lambda type, attributes: std_.core.Tuple(type, attributes)
		factories[std_.core.DatePart.name_] = lambda type, attributes: std_.core.DatePart(type, attributes)
		factories[std.core.nodeIndex.name_] = lambda type, attributes: std.core.nodeIndex(type, attributes)
		loaders[std.core.nodeIndex.name_] = lambda type, stream: std_n.core._nodeIndex.load(type, stream)
		factories[std.core.nodeList.name_] = lambda type, attributes: std.core.nodeList(type, attributes)
		loaders[std.core.nodeList.name_] = lambda type, stream: std_n.core._nodeList.load(type, stream)
		factories[std.core.tf3d.name_] = lambda type, attributes: std.core.tf3d(type, attributes)
		loaders[std.core.tf3d.name_] = lambda type, stream: std_n.core._tf3d.load(type, stream)
		factories[std_.core.nodeIndexBucket.name_] = lambda type, attributes: std_.core.nodeIndexBucket(type, attributes)
		loaders[std_.core.nodeIndexBucket.name_] = lambda type, stream: std_n.core._nodeIndexBucket.load(type, stream)
		factories[std.core.ti10d.name_] = lambda type, attributes: std.core.ti10d(type, attributes)
		loaders[std.core.ti10d.name_] = lambda type, stream: std_n.core._ti10d.load(type, stream)
		factories[std_.core.Array.name_] = lambda type, attributes: std_.core.Array(type, attributes)
		loaders[std_.core.Array.name_] = lambda type, stream: std_n.core._Array.load(type, stream)
		factories[std.core.tf4d.name_] = lambda type, attributes: std.core.tf4d(type, attributes)
		loaders[std.core.tf4d.name_] = lambda type, stream: std_n.core._tf4d.load(type, stream)
		factories[std.core.ti3d.name_] = lambda type, attributes: std.core.ti3d(type, attributes)
		loaders[std.core.ti3d.name_] = lambda type, stream: std_n.core._ti3d.load(type, stream)
		factories[std_.runtime.UserGroup.name_] = lambda type, attributes: std_.runtime.UserGroup(type, attributes)
		factories[std_.runtime.SecurityEntity.name_] = lambda type, attributes: std_.runtime.SecurityEntity(type, attributes)
		factories[std_.runtime.PeriodicTask.name_] = lambda type, attributes: std_.runtime.PeriodicTask(type, attributes)
		factories[std_.runtime.License.name_] = lambda type, attributes: std_.runtime.License(type, attributes)
		factories[std_.runtime.StoreStat.name_] = lambda type, attributes: std_.runtime.StoreStat(type, attributes)
		factories[std_.runtime.SecurityFields.name_] = lambda type, attributes: std_.runtime.SecurityFields(type, attributes)
		factories[std_.runtime.Task.name_] = lambda type, attributes: std_.runtime.Task(type, attributes)
		factories[std_.runtime.OpenIDConnect.name_] = lambda type, attributes: std_.runtime.OpenIDConnect(type, attributes)
		factories[std_.runtime.UserGroupPolicy.name_] = lambda type, attributes: std_.runtime.UserGroupPolicy(type, attributes)
		factories[std_.runtime.RuntimeInfo.name_] = lambda type, attributes: std_.runtime.RuntimeInfo(type, attributes)
		factories[std_.runtime.User.name_] = lambda type, attributes: std_.runtime.User(type, attributes)
		factories[std_.runtime.System.name_] = lambda type, attributes: std_.runtime.System(type, attributes)
		factories[std_.runtime.UserCredential.name_] = lambda type, attributes: std_.runtime.UserCredential(type, attributes)
		factories[std_.runtime.TaskStatus.name_] = lambda type, attributes: std_.runtime.TaskStatus(type, attributes)
		factories[std_.runtime.UserRole.name_] = lambda type, attributes: std_.runtime.UserRole(type, attributes)
		factories[std_.runtime.SecurityPolicy.name_] = lambda type, attributes: std_.runtime.SecurityPolicy(type, attributes)
		factories[std_.runtime.Runtime.name_] = lambda type, attributes: std_.runtime.Runtime(type, attributes)
		factories[std_.runtime.TaskInfo.name_] = lambda type, attributes: std_.runtime.TaskInfo(type, attributes)
		factories[std_.runtime.UserGroupPolicyType.name_] = lambda type, attributes: std_.runtime.UserGroupPolicyType(type, attributes)
		factories[std_.io.Email.name_] = lambda type, attributes: std_.io.Email(type, attributes)
		factories[std_.io.Smtp.name_] = lambda type, attributes: std_.io.Smtp(type, attributes)
		factories[std_.io.CsvFormat.name_] = lambda type, attributes: std_.io.CsvFormat(type, attributes)
		factories[std_.io.CsvColumnDuration.name_] = lambda type, attributes: std_.io.CsvColumnDuration(type, attributes)
		factories[std_.io.CsvColumnInteger.name_] = lambda type, attributes: std_.io.CsvColumnInteger(type, attributes)
		factories[std_.io.HttpHeader.name_] = lambda type, attributes: std_.io.HttpHeader(type, attributes)
		factories[std_.io.SmtpMode.name_] = lambda type, attributes: std_.io.SmtpMode(type, attributes)
		factories[std_.io.Url.name_] = lambda type, attributes: std_.io.Url(type, attributes)
		factories[std_.io.CsvColumnFloat.name_] = lambda type, attributes: std_.io.CsvColumnFloat(type, attributes)
		factories[std_.io.CsvColumn.name_] = lambda type, attributes: std_.io.CsvColumn(type, attributes)
		factories[std_.io.File.name_] = lambda type, attributes: std_.io.File(type, attributes)
		factories[std_.io.Http.name_] = lambda type, attributes: std_.io.Http(type, attributes)
		factories[std_.io.CsvColumnTime.name_] = lambda type, attributes: std_.io.CsvColumnTime(type, attributes)
		factories[std_.io.SmtpAuth.name_] = lambda type, attributes: std_.io.SmtpAuth(type, attributes)
		factories[std_.io.CsvColumnDate.name_] = lambda type, attributes: std_.io.CsvColumnDate(type, attributes)
		factories[std_.io.CsvColumnString.name_] = lambda type, attributes: std_.io.CsvColumnString(type, attributes)
		factories[std_.io.CsvColumnBoolean.name_] = lambda type, attributes: std_.io.CsvColumnBoolean(type, attributes)
		factories[std_.io.CsvColumnIgnored.name_] = lambda type, attributes: std_.io.CsvColumnIgnored(type, attributes)
		factories[std_.io.TextEncoder.name_] = lambda type, attributes: std_.io.TextEncoder(type, attributes)
		factories[std_.math.MathConstants.name_] = lambda type, attributes: std_.math.MathConstants(type, attributes)
		factories[std_.util.SlidingWindow.name_] = lambda type, attributes: std_.util.SlidingWindow(type, attributes)
		loaders[std_.util.SlidingWindow.name_] = lambda type, stream: std_n.util._SlidingWindow.load(type, stream)
		factories[std_.util.Assert.name_] = lambda type, attributes: std_.util.Assert(type, attributes)
		factories[std_.util.Iban.name_] = lambda type, attributes: std_.util.Iban(type, attributes)
		loaders[std_.util.Iban.name_] = lambda type, stream: std_n.util._Iban.load(type, stream)
		factories[std_.util.BoxPlotFloat.name_] = lambda type, attributes: std_.util.BoxPlotFloat(type, attributes)
		factories[std_.util.Random.name_] = lambda type, attributes: std_.util.Random(type, attributes)
		factories[std_.util.Crypto.name_] = lambda type, attributes: std_.util.Crypto(type, attributes)
		factories[std_.util.TimeWindow.name_] = lambda type, attributes: std_.util.TimeWindow(type, attributes)
		loaders[std_.util.TimeWindow.name_] = lambda type, stream: std_n.util._TimeWindow.load(type, stream)
		factories[std_.util.ProgressTracker.name_] = lambda type, attributes: std_.util.ProgressTracker(type, attributes)
		factories[std_.util.Quantizer.name_] = lambda type, attributes: std_.util.Quantizer(type, attributes)
		loaders[std_.util.Quantizer.name_] = lambda type, stream: std_n.util._Quantizer.load(type, stream)
		factories[std_.util.Gaussian.name_] = lambda type, attributes: std_.util.Gaussian(type, attributes)
		factories[std_.util.Queue.name_] = lambda type, attributes: std_.util.Queue(type, attributes)
		loaders[std_.util.Queue.name_] = lambda type, stream: std_n.util._Queue.load(type, stream)
		factories[std_.util.GaussianProfile.name_] = lambda type, attributes: std_.util.GaussianProfile(type, attributes)
		loaders[std_.util.GaussianProfile.name_] = lambda type, stream: std_n.util._GaussianProfile.load(type, stream)
		factories[std_.util.HistogramInt.name_] = lambda type, attributes: std_.util.HistogramInt(type, attributes)
		loaders[std_.util.HistogramInt.name_] = lambda type, stream: std_n.util._HistogramInt.load(type, stream)
		factories[std_.util.Buffer.name_] = lambda type, attributes: std_.util.Buffer(type, attributes)
		loaders[std_.util.Buffer.name_] = lambda type, stream: std_n.util._Buffer.load(type, stream)
		factories[std_.util.BoxPlotInt.name_] = lambda type, attributes: std_.util.BoxPlotInt(type, attributes)
		factories[std_.util.HistogramFloat.name_] = lambda type, attributes: std_.util.HistogramFloat(type, attributes)
		loaders[std_.util.HistogramFloat.name_] = lambda type, stream: std_n.util._HistogramFloat.load(type, stream)
	def init(self, greycat: GreyCat) -> None:
		self.mapped: list[GreyCat.Type] = [
			greycat.types_by_name[std.core.tf2d.name_],
			greycat.types_by_name[std.core.SamplingMode.name_],
			greycat.types_by_name[std.core.Table.name_],
			greycat.types_by_name[std.core.ti6d.name_],
			greycat.types_by_name[std.core.nodeTimeSingleton.name_],
			greycat.types_by_name[std.core.time.name_],
			greycat.types_by_name[std.core.nodeTime.name_],
			greycat.types_by_name[std.core.DurationUnit.name_],
			greycat.types_by_name[std.core.NodeTimeInfo.name_],
			greycat.types_by_name[std.core.function.name_],
			greycat.types_by_name[std.core.Error.name_],
			greycat.types_by_name[std.core.GeoPoly.name_],
			greycat.types_by_name[std.core.duration.name_],
			greycat.types_by_name[std.core.ti2d.name_],
			greycat.types_by_name[std.core.ErrorCode.name_],
			greycat.types_by_name[std.core.geo.name_],
			greycat.types_by_name[std.core.node.name_],
			greycat.types_by_name[std.core.TableColumnMeta.name_],
			greycat.types_by_name[std.core.Date.name_],
			greycat.types_by_name[std.core.Tensor.name_],
			greycat.types_by_name[std.core.ti4d.name_],
			greycat.types_by_name[std.core.GeoCircle.name_],
			greycat.types_by_name[std.core.nodeGeo.name_],
			greycat.types_by_name[std.core.ti5d.name_],
			greycat.types_by_name[std.core.String.name_],
			greycat.types_by_name[std.core.Map.name_],
			greycat.types_by_name[std.core.TensorType.name_],
			greycat.types_by_name[std.core.TimeZone.name_],
			greycat.types_by_name[std.core.GeoBox.name_],
			greycat.types_by_name[std.core.Tuple.name_],
			greycat.types_by_name[std.core.DatePart.name_],
			greycat.types_by_name[std.core.nodeIndex.name_],
			greycat.types_by_name[std.core.nodeList.name_],
			greycat.types_by_name[std.core.tf3d.name_],
			greycat.types_by_name[std.core.nodeIndexBucket.name_],
			greycat.types_by_name[std.core.ti10d.name_],
			greycat.types_by_name[std.core.Array.name_],
			greycat.types_by_name[std.core.tf4d.name_],
			greycat.types_by_name[std.core.ti3d.name_],
			greycat.types_by_name[std.runtime.UserGroup.name_],
			greycat.types_by_name[std.runtime.SecurityEntity.name_],
			greycat.types_by_name[std.runtime.PeriodicTask.name_],
			greycat.types_by_name[std.runtime.License.name_],
			greycat.types_by_name[std.runtime.StoreStat.name_],
			greycat.types_by_name[std.runtime.SecurityFields.name_],
			greycat.types_by_name[std.runtime.Task.name_],
			greycat.types_by_name[std.runtime.OpenIDConnect.name_],
			greycat.types_by_name[std.runtime.UserGroupPolicy.name_],
			greycat.types_by_name[std.runtime.RuntimeInfo.name_],
			greycat.types_by_name[std.runtime.User.name_],
			greycat.types_by_name[std.runtime.System.name_],
			greycat.types_by_name[std.runtime.UserCredential.name_],
			greycat.types_by_name[std.runtime.TaskStatus.name_],
			greycat.types_by_name[std.runtime.UserRole.name_],
			greycat.types_by_name[std.runtime.SecurityPolicy.name_],
			greycat.types_by_name[std.runtime.Runtime.name_],
			greycat.types_by_name[std.runtime.TaskInfo.name_],
			greycat.types_by_name[std.runtime.UserGroupPolicyType.name_],
			greycat.types_by_name[std.io.Email.name_],
			greycat.types_by_name[std.io.Smtp.name_],
			greycat.types_by_name[std.io.CsvFormat.name_],
			greycat.types_by_name[std.io.CsvColumnDuration.name_],
			greycat.types_by_name[std.io.CsvColumnInteger.name_],
			greycat.types_by_name[std.io.HttpHeader.name_],
			greycat.types_by_name[std.io.SmtpMode.name_],
			greycat.types_by_name[std.io.Url.name_],
			greycat.types_by_name[std.io.CsvColumnFloat.name_],
			greycat.types_by_name[std.io.CsvColumn.name_],
			greycat.types_by_name[std.io.File.name_],
			greycat.types_by_name[std.io.Http.name_],
			greycat.types_by_name[std.io.CsvColumnTime.name_],
			greycat.types_by_name[std.io.SmtpAuth.name_],
			greycat.types_by_name[std.io.CsvColumnDate.name_],
			greycat.types_by_name[std.io.CsvColumnString.name_],
			greycat.types_by_name[std.io.CsvColumnBoolean.name_],
			greycat.types_by_name[std.io.CsvColumnIgnored.name_],
			greycat.types_by_name[std.io.TextEncoder.name_],
			greycat.types_by_name[std.math.MathConstants.name_],
			greycat.types_by_name[std.util.SlidingWindow.name_],
			greycat.types_by_name[std.util.Assert.name_],
			greycat.types_by_name[std.util.Iban.name_],
			greycat.types_by_name[std.util.BoxPlotFloat.name_],
			greycat.types_by_name[std.util.Random.name_],
			greycat.types_by_name[std.util.Crypto.name_],
			greycat.types_by_name[std.util.TimeWindow.name_],
			greycat.types_by_name[std.util.ProgressTracker.name_],
			greycat.types_by_name[std.util.Quantizer.name_],
			greycat.types_by_name[std.util.Gaussian.name_],
			greycat.types_by_name[std.util.Queue.name_],
			greycat.types_by_name[std.util.GaussianProfile.name_],
			greycat.types_by_name[std.util.HistogramInt.name_],
			greycat.types_by_name[std.util.Buffer.name_],
			greycat.types_by_name[std.util.BoxPlotInt.name_],
			greycat.types_by_name[std.util.HistogramFloat.name_],
			]
		self.mapped[1].resolve_generated_offset_with_values("fixed", 0, "fixed_reg", 1, "adaptative", 2, "dense", 3)
		self.mapped[4].resolve_generated_offsets("t","v")
		self.mapped[5].static_values = [greycat.create_time(-9223372036854775808),greycat.create_time(9223372036854775807)]
		self.mapped[7].resolve_generated_offset_with_values("microseconds", 1, "milliseconds", 1000, "seconds", 1000000, "minutes", 60000000, "hours", 3600000000, "days", 86400000000, "weeks", 604800000000, "months", 2628000000000, "years", 31536000000000)
		self.mapped[8].resolve_generated_offsets("size","from","to")
		self.mapped[11].resolve_generated_offsets("points")
		self.mapped[14].resolve_generated_offset_with_values("none", 0, "too_deep_workspace", 1, "too_deep_iterator", 2, "wrong_operand", 3, "wrong_params", 4, "wrong_param_type", 5, "wrong_numeric", 6, "wrong_state", 7, "wrong_null", 8, "unresolved_ref", 9, "assign_error", 10, "interrupted", 11, "throw", 12, "wrong_type", 13, "wrong_dimension", 14, "unsupported_operation", 15, "unsupported_type", 16, "dimensions_mismatch", 17, "timeout", 18, "forbidden", 19, "runtime_error", 20)
		self.mapped[15].static_values = [greycat.create_geo(-85.0511287602,-179.9999999581),greycat.create_geo(85.0511287602,179.9999999581)]
		self.mapped[17].resolve_generated_offsets("type","size","index","min","max","avg","std")
		self.mapped[21].resolve_generated_offsets("center","radius")
		self.mapped[26].resolve_generated_offset_with_values("i32", 4, "i64", 8, "f32", 4, "f64", 8, "c64", 8, "c128", 16)
		self.mapped[27].resolve_generated_offset_with_values("Africa_Accra", "Africa/Accra", "Africa_Bamako", "Africa/Bamako", "Africa_Banjul", "Africa/Banjul", "Africa_Conakry", "Africa/Conakry", "Africa_Dakar", "Africa/Dakar", "Africa_Freetown", "Africa/Freetown", "Africa_Lome", "Africa/Lome", "Africa_Nouakchott", "Africa/Nouakchott", "Africa_Ouagadougou", "Africa/Ouagadougou", "Africa_Timbuktu", "Africa/Timbuktu", "Atlantic_Reykjavik", "Atlantic/Reykjavik", "Atlantic_St_Helena", "Atlantic/St_Helena", "Iceland", "Iceland", "Egypt", "Egypt", "Africa_Maseru", "Africa/Maseru", "Africa_Mbabane", "Africa/Mbabane", "Africa_Bangui", "Africa/Bangui", "Africa_Brazzaville", "Africa/Brazzaville", "Africa_Douala", "Africa/Douala", "Africa_Kinshasa", "Africa/Kinshasa", "Africa_Libreville", "Africa/Libreville", "Africa_Luanda", "Africa/Luanda", "Africa_Malabo", "Africa/Malabo", "Africa_Niamey", "Africa/Niamey", "Africa_Porto_Novo", "Africa/Porto-Novo", "Africa_Blantyre", "Africa/Blantyre", "Africa_Bujumbura", "Africa/Bujumbura", "Africa_Gaborone", "Africa/Gaborone", "Africa_Harare", "Africa/Harare", "Africa_Kigali", "Africa/Kigali", "Africa_Lubumbashi", "Africa/Lubumbashi", "Africa_Lusaka", "Africa/Lusaka", "Africa_Addis_Ababa", "Africa/Addis_Ababa", "Africa_Asmara", "Africa/Asmara", "Africa_Asmera", "Africa/Asmera", "Africa_Dar_es_Salaam", "Africa/Dar_es_Salaam", "Africa_Djibouti", "Africa/Djibouti", "Africa_Kampala", "Africa/Kampala", "Africa_Mogadishu", "Africa/Mogadishu", "Indian_Antananarivo", "Indian/Antananarivo", "Indian_Comoro", "Indian/Comoro", "Indian_Mayotte", "Indian/Mayotte", "Libya", "Libya", "America_Atka", "America/Atka", "US_Aleutian", "US/Aleutian", "US_Alaska", "US/Alaska", "America_Buenos_Aires", "America/Buenos_Aires", "America_Argentina_ComodRivadavia", "America/Argentina/ComodRivadavia", "America_Catamarca", "America/Catamarca", "America_Cordoba", "America/Cordoba", "America_Rosario", "America/Rosario", "America_Jujuy", "America/Jujuy", "America_Mendoza", "America/Mendoza", "US_Central", "US/Central", "America_Shiprock", "America/Shiprock", "Navajo", "Navajo", "US_Mountain", "US/Mountain", "US_Michigan", "US/Michigan", "America_Yellowknife", "America/Yellowknife", "Canada_Mountain", "Canada/Mountain", "Canada_Atlantic", "Canada/Atlantic", "Cuba", "Cuba", "America_Fort_Wayne", "America/Fort_Wayne", "America_Indianapolis", "America/Indianapolis", "US_East_Indiana", "US/East-Indiana", "America_Knox_IN", "America/Knox_IN", "US_Indiana_Starke", "US/Indiana-Starke", "America_Pangnirtung", "America/Pangnirtung", "Jamaica", "Jamaica", "America_Louisville", "America/Louisville", "US_Pacific", "US/Pacific", "Brazil_West", "Brazil/West", "Mexico_BajaSur", "Mexico/BajaSur", "Mexico_General", "Mexico/General", "US_Eastern", "US/Eastern", "Brazil_DeNoronha", "Brazil/DeNoronha", "America_Godthab", "America/Godthab", "America_Atikokan", "America/Atikokan", "America_Cayman", "America/Cayman", "America_Coral_Harbour", "America/Coral_Harbour", "America_Creston", "America/Creston", "US_Arizona", "US/Arizona", "America_Anguilla", "America/Anguilla", "America_Antigua", "America/Antigua", "America_Aruba", "America/Aruba", "America_Blanc_Sablon", "America/Blanc-Sablon", "America_Curacao", "America/Curacao", "America_Dominica", "America/Dominica", "America_Grenada", "America/Grenada", "America_Guadeloupe", "America/Guadeloupe", "America_Kralendijk", "America/Kralendijk", "America_Lower_Princes", "America/Lower_Princes", "America_Marigot", "America/Marigot", "America_Montserrat", "America/Montserrat", "America_Port_of_Spain", "America/Port_of_Spain", "America_St_Barthelemy", "America/St_Barthelemy", "America_St_Kitts", "America/St_Kitts", "America_St_Lucia", "America/St_Lucia", "America_St_Thomas", "America/St_Thomas", "America_St_Vincent", "America/St_Vincent", "America_Tortola", "America/Tortola", "America_Virgin", "America/Virgin", "Canada_Saskatchewan", "Canada/Saskatchewan", "America_Porto_Acre", "America/Porto_Acre", "Brazil_Acre", "Brazil/Acre", "Chile_Continental", "Chile/Continental", "Brazil_East", "Brazil/East", "Canada_Newfoundland", "Canada/Newfoundland", "America_Ensenada", "America/Ensenada", "America_Santa_Isabel", "America/Santa_Isabel", "Mexico_BajaNorte", "Mexico/BajaNorte", "America_Montreal", "America/Montreal", "America_Nassau", "America/Nassau", "America_Nipigon", "America/Nipigon", "America_Thunder_Bay", "America/Thunder_Bay", "Canada_Eastern", "Canada/Eastern", "Canada_Pacific", "Canada/Pacific", "Canada_Yukon", "Canada/Yukon", "America_Rainy_River", "America/Rainy_River", "Canada_Central", "Canada/Central", "Asia_Ashkhabad", "Asia/Ashkhabad", "Asia_Phnom_Penh", "Asia/Phnom_Penh", "Asia_Vientiane", "Asia/Vientiane", "Indian_Christmas", "Indian/Christmas", "Asia_Dacca", "Asia/Dacca", "Asia_Muscat", "Asia/Muscat", "Indian_Mahe", "Indian/Mahe", "Indian_Reunion", "Indian/Reunion", "Asia_Saigon", "Asia/Saigon", "Hongkong", "Hongkong", "Asia_Tel_Aviv", "Asia/Tel_Aviv", "Israel", "Israel", "Asia_Katmandu", "Asia/Katmandu", "Asia_Calcutta", "Asia/Calcutta", "Asia_Brunei", "Asia/Brunei", "Asia_Macao", "Asia/Macao", "Asia_Ujung_Pandang", "Asia/Ujung_Pandang", "Europe_Nicosia", "Europe/Nicosia", "Asia_Bahrain", "Asia/Bahrain", "Antarctica_Syowa", "Antarctica/Syowa", "Asia_Aden", "Asia/Aden", "Asia_Kuwait", "Asia/Kuwait", "ROK", "ROK", "Asia_Chongqing", "Asia/Chongqing", "Asia_Chungking", "Asia/Chungking", "Asia_Harbin", "Asia/Harbin", "PRC", "PRC", "Asia_Kuala_Lumpur", "Asia/Kuala_Lumpur", "Singapore", "Singapore", "ROC", "ROC", "Iran", "Iran", "Asia_Thimbu", "Asia/Thimbu", "Japan", "Japan", "Asia_Ulan_Bator", "Asia/Ulan_Bator", "Antarctica_Vostok", "Antarctica/Vostok", "Asia_Kashgar", "Asia/Kashgar", "Asia_Rangoon", "Asia/Rangoon", "Indian_Cocos", "Indian/Cocos", "Atlantic_Faeroe", "Atlantic/Faeroe", "Australia_South", "Australia/South", "Australia_Queensland", "Australia/Queensland", "Australia_Yancowinna", "Australia/Yancowinna", "Australia_North", "Australia/North", "Australia_Currie", "Australia/Currie", "Australia_Tasmania", "Australia/Tasmania", "Australia_LHI", "Australia/LHI", "Australia_Victoria", "Australia/Victoria", "Australia_West", "Australia/West", "Australia_ACT", "Australia/ACT", "Australia_Canberra", "Australia/Canberra", "Australia_NSW", "Australia/NSW", "GMT", "GMT", "GMTx0", "GMT+0", "GMT_0", "GMT-0", "GMT0", "GMT0", "Greenwich", "Greenwich", "UCT", "UCT", "UTC", "UTC", "Universal", "Universal", "Zulu", "Zulu", "Europe_Ljubljana", "Europe/Ljubljana", "Europe_Podgorica", "Europe/Podgorica", "Europe_Sarajevo", "Europe/Sarajevo", "Europe_Skopje", "Europe/Skopje", "Europe_Zagreb", "Europe/Zagreb", "Arctic_Longyearbyen", "Arctic/Longyearbyen", "Atlantic_Jan_Mayen", "Atlantic/Jan_Mayen", "Europe_Copenhagen", "Europe/Copenhagen", "Europe_Oslo", "Europe/Oslo", "Europe_Stockholm", "Europe/Stockholm", "Europe_Amsterdam", "Europe/Amsterdam", "Europe_Luxembourg", "Europe/Luxembourg", "Europe_Tiraspol", "Europe/Tiraspol", "Eire", "Eire", "Europe_Mariehamn", "Europe/Mariehamn", "Asia_Istanbul", "Asia/Istanbul", "Turkey", "Turkey", "Europe_Kiev", "Europe/Kiev", "Europe_Uzhgorod", "Europe/Uzhgorod", "Europe_Zaporozhye", "Europe/Zaporozhye", "Portugal", "Portugal", "Europe_Belfast", "Europe/Belfast", "Europe_Guernsey", "Europe/Guernsey", "Europe_Isle_of_Man", "Europe/Isle_of_Man", "Europe_Jersey", "Europe/Jersey", "GB", "GB", "GB_Eire", "GB-Eire", "W_SU", "W-SU", "Europe_Monaco", "Europe/Monaco", "Europe_Bratislava", "Europe/Bratislava", "Europe_San_Marino", "Europe/San_Marino", "Europe_Vatican", "Europe/Vatican", "Poland", "Poland", "Europe_Busingen", "Europe/Busingen", "Europe_Vaduz", "Europe/Vaduz", "Indian_Kerguelen", "Indian/Kerguelen", "Antarctica_McMurdo", "Antarctica/McMurdo", "Antarctica_South_Pole", "Antarctica/South_Pole", "NZ", "NZ", "NZ_CHAT", "NZ-CHAT", "Chile_EasterIsland", "Chile/EasterIsland", "Pacific_Pohnpei", "Pacific/Pohnpei", "Pacific_Ponape", "Pacific/Ponape", "Pacific_Saipan", "Pacific/Saipan", "Pacific_Johnston", "Pacific/Johnston", "US_Hawaii", "US/Hawaii", "Pacific_Enderbury", "Pacific/Enderbury", "Kwajalein", "Kwajalein", "Pacific_Midway", "Pacific/Midway", "Pacific_Samoa", "Pacific/Samoa", "US_Samoa", "US/Samoa", "Antarctica_DumontDUrville", "Antarctica/DumontDUrville", "Pacific_Chuuk", "Pacific/Chuuk", "Pacific_Truk", "Pacific/Truk", "Pacific_Yap", "Pacific/Yap", "Pacific_Funafuti", "Pacific/Funafuti", "Pacific_Majuro", "Pacific/Majuro", "Pacific_Wake", "Pacific/Wake", "Pacific_Wallis", "Pacific/Wallis", "Africa_Abidjan", "Africa/Abidjan", "Africa_Algiers", "Africa/Algiers", "Africa_Bissau", "Africa/Bissau", "Africa_Cairo", "Africa/Cairo", "Africa_Casablanca", "Africa/Casablanca", "Africa_Ceuta", "Africa/Ceuta", "Africa_El_Aaiun", "Africa/El_Aaiun", "Africa_Johannesburg", "Africa/Johannesburg", "Africa_Juba", "Africa/Juba", "Africa_Khartoum", "Africa/Khartoum", "Africa_Lagos", "Africa/Lagos", "Africa_Maputo", "Africa/Maputo", "Africa_Monrovia", "Africa/Monrovia", "Africa_Nairobi", "Africa/Nairobi", "Africa_Ndjamena", "Africa/Ndjamena", "Africa_Sao_Tome", "Africa/Sao_Tome", "Africa_Tripoli", "Africa/Tripoli", "Africa_Tunis", "Africa/Tunis", "Africa_Windhoek", "Africa/Windhoek", "America_Adak", "America/Adak", "America_Anchorage", "America/Anchorage", "America_Araguaina", "America/Araguaina", "America_Argentina_Buenos_Aires", "America/Argentina/Buenos_Aires", "America_Argentina_Catamarca", "America/Argentina/Catamarca", "America_Argentina_Cordoba", "America/Argentina/Cordoba", "America_Argentina_Jujuy", "America/Argentina/Jujuy", "America_Argentina_La_Rioja", "America/Argentina/La_Rioja", "America_Argentina_Mendoza", "America/Argentina/Mendoza", "America_Argentina_Rio_Gallegos", "America/Argentina/Rio_Gallegos", "America_Argentina_Salta", "America/Argentina/Salta", "America_Argentina_San_Juan", "America/Argentina/San_Juan", "America_Argentina_San_Luis", "America/Argentina/San_Luis", "America_Argentina_Tucuman", "America/Argentina/Tucuman", "America_Argentina_Ushuaia", "America/Argentina/Ushuaia", "America_Asuncion", "America/Asuncion", "America_Bahia", "America/Bahia", "America_Bahia_Banderas", "America/Bahia_Banderas", "America_Barbados", "America/Barbados", "America_Belem", "America/Belem", "America_Belize", "America/Belize", "America_Boa_Vista", "America/Boa_Vista", "America_Bogota", "America/Bogota", "America_Boise", "America/Boise", "America_Cambridge_Bay", "America/Cambridge_Bay", "America_Campo_Grande", "America/Campo_Grande", "America_Cancun", "America/Cancun", "America_Caracas", "America/Caracas", "America_Cayenne", "America/Cayenne", "America_Chicago", "America/Chicago", "America_Chihuahua", "America/Chihuahua", "America_Ciudad_Juarez", "America/Ciudad_Juarez", "America_Costa_Rica", "America/Costa_Rica", "America_Cuiaba", "America/Cuiaba", "America_Danmarkshavn", "America/Danmarkshavn", "America_Dawson", "America/Dawson", "America_Dawson_Creek", "America/Dawson_Creek", "America_Denver", "America/Denver", "America_Detroit", "America/Detroit", "America_Edmonton", "America/Edmonton", "America_Eirunepe", "America/Eirunepe", "America_El_Salvador", "America/El_Salvador", "America_Fort_Nelson", "America/Fort_Nelson", "America_Fortaleza", "America/Fortaleza", "America_Glace_Bay", "America/Glace_Bay", "America_Goose_Bay", "America/Goose_Bay", "America_Grand_Turk", "America/Grand_Turk", "America_Guatemala", "America/Guatemala", "America_Guayaquil", "America/Guayaquil", "America_Guyana", "America/Guyana", "America_Halifax", "America/Halifax", "America_Havana", "America/Havana", "America_Hermosillo", "America/Hermosillo", "America_Indiana_Indianapolis", "America/Indiana/Indianapolis", "America_Indiana_Knox", "America/Indiana/Knox", "America_Indiana_Marengo", "America/Indiana/Marengo", "America_Indiana_Petersburg", "America/Indiana/Petersburg", "America_Indiana_Tell_City", "America/Indiana/Tell_City", "America_Indiana_Vevay", "America/Indiana/Vevay", "America_Indiana_Vincennes", "America/Indiana/Vincennes", "America_Indiana_Winamac", "America/Indiana/Winamac", "America_Inuvik", "America/Inuvik", "America_Iqaluit", "America/Iqaluit", "America_Jamaica", "America/Jamaica", "America_Juneau", "America/Juneau", "America_Kentucky_Louisville", "America/Kentucky/Louisville", "America_Kentucky_Monticello", "America/Kentucky/Monticello", "America_La_Paz", "America/La_Paz", "America_Lima", "America/Lima", "America_Los_Angeles", "America/Los_Angeles", "America_Maceio", "America/Maceio", "America_Managua", "America/Managua", "America_Manaus", "America/Manaus", "America_Martinique", "America/Martinique", "America_Matamoros", "America/Matamoros", "America_Mazatlan", "America/Mazatlan", "America_Menominee", "America/Menominee", "America_Merida", "America/Merida", "America_Metlakatla", "America/Metlakatla", "America_Mexico_City", "America/Mexico_City", "America_Miquelon", "America/Miquelon", "America_Moncton", "America/Moncton", "America_Monterrey", "America/Monterrey", "America_Montevideo", "America/Montevideo", "America_New_York", "America/New_York", "America_Nome", "America/Nome", "America_Noronha", "America/Noronha", "America_North_Dakota_Beulah", "America/North_Dakota/Beulah", "America_North_Dakota_Center", "America/North_Dakota/Center", "America_North_Dakota_New_Salem", "America/North_Dakota/New_Salem", "America_Nuuk", "America/Nuuk", "America_Ojinaga", "America/Ojinaga", "America_Panama", "America/Panama", "America_Paramaribo", "America/Paramaribo", "America_Phoenix", "America/Phoenix", "America_Port_au_Prince", "America/Port-au-Prince", "America_Porto_Velho", "America/Porto_Velho", "America_Puerto_Rico", "America/Puerto_Rico", "America_Punta_Arenas", "America/Punta_Arenas", "America_Rankin_Inlet", "America/Rankin_Inlet", "America_Recife", "America/Recife", "America_Regina", "America/Regina", "America_Resolute", "America/Resolute", "America_Rio_Branco", "America/Rio_Branco", "America_Santarem", "America/Santarem", "America_Santiago", "America/Santiago", "America_Santo_Domingo", "America/Santo_Domingo", "America_Sao_Paulo", "America/Sao_Paulo", "America_Scoresbysund", "America/Scoresbysund", "America_Sitka", "America/Sitka", "America_St_Johns", "America/St_Johns", "America_Swift_Current", "America/Swift_Current", "America_Tegucigalpa", "America/Tegucigalpa", "America_Thule", "America/Thule", "America_Tijuana", "America/Tijuana", "America_Toronto", "America/Toronto", "America_Vancouver", "America/Vancouver", "America_Whitehorse", "America/Whitehorse", "America_Winnipeg", "America/Winnipeg", "America_Yakutat", "America/Yakutat", "Antarctica_Casey", "Antarctica/Casey", "Antarctica_Davis", "Antarctica/Davis", "Antarctica_Macquarie", "Antarctica/Macquarie", "Antarctica_Mawson", "Antarctica/Mawson", "Antarctica_Palmer", "Antarctica/Palmer", "Antarctica_Rothera", "Antarctica/Rothera", "Antarctica_Troll", "Antarctica/Troll", "Asia_Almaty", "Asia/Almaty", "Asia_Amman", "Asia/Amman", "Asia_Anadyr", "Asia/Anadyr", "Asia_Aqtau", "Asia/Aqtau", "Asia_Aqtobe", "Asia/Aqtobe", "Asia_Ashgabat", "Asia/Ashgabat", "Asia_Atyrau", "Asia/Atyrau", "Asia_Baghdad", "Asia/Baghdad", "Asia_Baku", "Asia/Baku", "Asia_Bangkok", "Asia/Bangkok", "Asia_Barnaul", "Asia/Barnaul", "Asia_Beirut", "Asia/Beirut", "Asia_Bishkek", "Asia/Bishkek", "Asia_Chita", "Asia/Chita", "Asia_Choibalsan", "Asia/Choibalsan", "Asia_Colombo", "Asia/Colombo", "Asia_Damascus", "Asia/Damascus", "Asia_Dhaka", "Asia/Dhaka", "Asia_Dili", "Asia/Dili", "Asia_Dubai", "Asia/Dubai", "Asia_Dushanbe", "Asia/Dushanbe", "Asia_Famagusta", "Asia/Famagusta", "Asia_Gaza", "Asia/Gaza", "Asia_Hebron", "Asia/Hebron", "Asia_Ho_Chi_Minh", "Asia/Ho_Chi_Minh", "Asia_Hong_Kong", "Asia/Hong_Kong", "Asia_Hovd", "Asia/Hovd", "Asia_Irkutsk", "Asia/Irkutsk", "Asia_Jakarta", "Asia/Jakarta", "Asia_Jayapura", "Asia/Jayapura", "Asia_Jerusalem", "Asia/Jerusalem", "Asia_Kabul", "Asia/Kabul", "Asia_Kamchatka", "Asia/Kamchatka", "Asia_Karachi", "Asia/Karachi", "Asia_Kathmandu", "Asia/Kathmandu", "Asia_Khandyga", "Asia/Khandyga", "Asia_Kolkata", "Asia/Kolkata", "Asia_Krasnoyarsk", "Asia/Krasnoyarsk", "Asia_Kuching", "Asia/Kuching", "Asia_Macau", "Asia/Macau", "Asia_Magadan", "Asia/Magadan", "Asia_Makassar", "Asia/Makassar", "Asia_Manila", "Asia/Manila", "Asia_Nicosia", "Asia/Nicosia", "Asia_Novokuznetsk", "Asia/Novokuznetsk", "Asia_Novosibirsk", "Asia/Novosibirsk", "Asia_Omsk", "Asia/Omsk", "Asia_Oral", "Asia/Oral", "Asia_Pontianak", "Asia/Pontianak", "Asia_Pyongyang", "Asia/Pyongyang", "Asia_Qatar", "Asia/Qatar", "Asia_Qostanay", "Asia/Qostanay", "Asia_Qyzylorda", "Asia/Qyzylorda", "Asia_Riyadh", "Asia/Riyadh", "Asia_Sakhalin", "Asia/Sakhalin", "Asia_Samarkand", "Asia/Samarkand", "Asia_Seoul", "Asia/Seoul", "Asia_Shanghai", "Asia/Shanghai", "Asia_Singapore", "Asia/Singapore", "Asia_Srednekolymsk", "Asia/Srednekolymsk", "Asia_Taipei", "Asia/Taipei", "Asia_Tashkent", "Asia/Tashkent", "Asia_Tbilisi", "Asia/Tbilisi", "Asia_Tehran", "Asia/Tehran", "Asia_Thimphu", "Asia/Thimphu", "Asia_Tokyo", "Asia/Tokyo", "Asia_Tomsk", "Asia/Tomsk", "Asia_Ulaanbaatar", "Asia/Ulaanbaatar", "Asia_Urumqi", "Asia/Urumqi", "Asia_Ust_Nera", "Asia/Ust-Nera", "Asia_Vladivostok", "Asia/Vladivostok", "Asia_Yakutsk", "Asia/Yakutsk", "Asia_Yangon", "Asia/Yangon", "Asia_Yekaterinburg", "Asia/Yekaterinburg", "Asia_Yerevan", "Asia/Yerevan", "Atlantic_Azores", "Atlantic/Azores", "Atlantic_Bermuda", "Atlantic/Bermuda", "Atlantic_Canary", "Atlantic/Canary", "Atlantic_Cape_Verde", "Atlantic/Cape_Verde", "Atlantic_Faroe", "Atlantic/Faroe", "Atlantic_Madeira", "Atlantic/Madeira", "Atlantic_South_Georgia", "Atlantic/South_Georgia", "Atlantic_Stanley", "Atlantic/Stanley", "Australia_Adelaide", "Australia/Adelaide", "Australia_Brisbane", "Australia/Brisbane", "Australia_Broken_Hill", "Australia/Broken_Hill", "Australia_Darwin", "Australia/Darwin", "Australia_Eucla", "Australia/Eucla", "Australia_Hobart", "Australia/Hobart", "Australia_Lindeman", "Australia/Lindeman", "Australia_Lord_Howe", "Australia/Lord_Howe", "Australia_Melbourne", "Australia/Melbourne", "Australia_Perth", "Australia/Perth", "Australia_Sydney", "Australia/Sydney", "CET", "CET", "CST6CDT", "CST6CDT", "EET", "EET", "EST", "EST", "EST5EDT", "EST5EDT", "Europe_Andorra", "Europe/Andorra", "Europe_Astrakhan", "Europe/Astrakhan", "Europe_Athens", "Europe/Athens", "Europe_Belgrade", "Europe/Belgrade", "Europe_Berlin", "Europe/Berlin", "Europe_Brussels", "Europe/Brussels", "Europe_Bucharest", "Europe/Bucharest", "Europe_Budapest", "Europe/Budapest", "Europe_Chisinau", "Europe/Chisinau", "Europe_Dublin", "Europe/Dublin", "Europe_Gibraltar", "Europe/Gibraltar", "Europe_Helsinki", "Europe/Helsinki", "Europe_Istanbul", "Europe/Istanbul", "Europe_Kaliningrad", "Europe/Kaliningrad", "Europe_Kirov", "Europe/Kirov", "Europe_Kyiv", "Europe/Kyiv", "Europe_Lisbon", "Europe/Lisbon", "Europe_London", "Europe/London", "Europe_Madrid", "Europe/Madrid", "Europe_Malta", "Europe/Malta", "Europe_Minsk", "Europe/Minsk", "Europe_Moscow", "Europe/Moscow", "Europe_Paris", "Europe/Paris", "Europe_Prague", "Europe/Prague", "Europe_Riga", "Europe/Riga", "Europe_Rome", "Europe/Rome", "Europe_Samara", "Europe/Samara", "Europe_Saratov", "Europe/Saratov", "Europe_Simferopol", "Europe/Simferopol", "Europe_Sofia", "Europe/Sofia", "Europe_Tallinn", "Europe/Tallinn", "Europe_Tirane", "Europe/Tirane", "Europe_Ulyanovsk", "Europe/Ulyanovsk", "Europe_Vienna", "Europe/Vienna", "Europe_Vilnius", "Europe/Vilnius", "Europe_Volgograd", "Europe/Volgograd", "Europe_Warsaw", "Europe/Warsaw", "Europe_Zurich", "Europe/Zurich", "Factory", "Factory", "HST", "HST", "Indian_Chagos", "Indian/Chagos", "Indian_Maldives", "Indian/Maldives", "Indian_Mauritius", "Indian/Mauritius", "MET", "MET", "MST", "MST", "MST7MDT", "MST7MDT", "PST8PDT", "PST8PDT", "Pacific_Apia", "Pacific/Apia", "Pacific_Auckland", "Pacific/Auckland", "Pacific_Bougainville", "Pacific/Bougainville", "Pacific_Chatham", "Pacific/Chatham", "Pacific_Easter", "Pacific/Easter", "Pacific_Efate", "Pacific/Efate", "Pacific_Fakaofo", "Pacific/Fakaofo", "Pacific_Fiji", "Pacific/Fiji", "Pacific_Galapagos", "Pacific/Galapagos", "Pacific_Gambier", "Pacific/Gambier", "Pacific_Guadalcanal", "Pacific/Guadalcanal", "Pacific_Guam", "Pacific/Guam", "Pacific_Honolulu", "Pacific/Honolulu", "Pacific_Kanton", "Pacific/Kanton", "Pacific_Kiritimati", "Pacific/Kiritimati", "Pacific_Kosrae", "Pacific/Kosrae", "Pacific_Kwajalein", "Pacific/Kwajalein", "Pacific_Marquesas", "Pacific/Marquesas", "Pacific_Nauru", "Pacific/Nauru", "Pacific_Niue", "Pacific/Niue", "Pacific_Norfolk", "Pacific/Norfolk", "Pacific_Noumea", "Pacific/Noumea", "Pacific_Pago_Pago", "Pacific/Pago_Pago", "Pacific_Palau", "Pacific/Palau", "Pacific_Pitcairn", "Pacific/Pitcairn", "Pacific_Port_Moresby", "Pacific/Port_Moresby", "Pacific_Rarotonga", "Pacific/Rarotonga", "Pacific_Tahiti", "Pacific/Tahiti", "Pacific_Tarawa", "Pacific/Tarawa", "Pacific_Tongatapu", "Pacific/Tongatapu", "WET", "WET")
		self.mapped[28].resolve_generated_offsets("sw","ne")
		self.mapped[29].resolve_generated_offsets("x","y")
		self.mapped[30].resolve_generated_offset_with_values("years", 0, "months", 1, "days", 2, "hours", 3, "minutes", 4, "seconds", 5, "microseconds", 6)
		self.mapped[39].resolve_generated_offsets("id","name","activated")
		self.mapped[40].resolve_generated_offsets("id","name","activated")
		self.mapped[41].resolve_generated_offsets("name","user_id","args","start","every")
		self.mapped[42].resolve_generated_offsets("name","start","end","company","max_workers","max_memory","extra_1","extra_2","extra_3","extra_4")
		self.mapped[43].resolve_generated_offsets("capacity_bytes","allocated_bytes","allocated_ratio","remained_bytes","remained_ratio","used_bytes","used_ratio","available_bytes","available_ratio")
		self.mapped[44].resolve_generated_offsets("email","name","first_name","last_name","roles","groups")
		self.mapped[45].resolve_generated_offsets("user_id","task_id","mod","type","fun","creation","status")
		self.mapped[46].resolve_generated_offsets("url","clientId")
		self.mapped[47].resolve_generated_offsets("group_id","type")
		self.mapped[48].resolve_generated_offsets("version","arch","timezone","license","io_threads","bg_threads","fg_threads","mem_total","mem_worker","nb_ctx","store_stats")
		self.mapped[49].resolve_generated_offsets("id","name","activated","full_name","email","role","permissions_flags","groups","groups_flags","external")
		self.mapped[51].resolve_generated_offsets("offset","pass")
		self.mapped[52].resolve_generated_offset_with_values("empty", 0, "waiting", 1, "running", 2, "cancelled", 3, "error", 4, "ended", 5)
		self.mapped[53].resolve_generated_offsets("name","permissions")
		self.mapped[54].resolve_generated_offsets("entities","credentials","roles","fields")
		self.mapped[56].resolve_generated_offsets("user_id","task_id","mod","type","fun","creation","status","start","progress","remaining","duration","sub_waiting","sub_tasks_all")
		self.mapped[57].resolve_generated_offset_with_values("read", 0, "write", 1, "execute", 2)
		self.mapped[58].resolve_generated_offsets("from","subject","body","body_is_html","to","cc","bcc")
		self.mapped[59].resolve_generated_offsets("host","port","mode","authenticate","user","pass")
		self.mapped[60].resolve_generated_offsets("header_lines","infer","separator","string_delimiter","decimal_separator","thousands_separator","columns")
		self.mapped[61].resolve_generated_offsets("name","mandatory","unit")
		self.mapped[62].resolve_generated_offsets("name","mandatory")
		self.mapped[63].resolve_generated_offsets("name","value")
		self.mapped[64].resolve_generated_offset_with_values("plain", 0, "ssl_tls", 1, "starttls", 2)
		self.mapped[65].resolve_generated_offsets("protocol","host","port","path","params","hash")
		self.mapped[66].resolve_generated_offsets("name","mandatory")
		self.mapped[67].resolve_generated_offsets("name","mandatory")
		self.mapped[68].resolve_generated_offsets("path","size","last_modification")
		self.mapped[70].resolve_generated_offsets("name","mandatory","unit")
		self.mapped[71].resolve_generated_offset_with_values("none", 0, "plain", 1, "login", 2)
		self.mapped[72].resolve_generated_offsets("name","mandatory","format","tz","as_time")
		self.mapped[73].resolve_generated_offsets("name","mandatory","trim","try_number","try_json","values","encoder")
		self.mapped[74].resolve_generated_offsets("name","mandatory")
		self.mapped[75].resolve_generated_offsets("name","mandatory")
		self.mapped[76].resolve_generated_offset_with_values("plain", None, "base64", None, "base64url", None, "hexadecimal", None)
		self.mapped[77].static_values = [2.7182818285,1.4426950409,0.4342944819,0.6931471806,2.302585093,3.1415926536,1.5707963268,0.7853981634,0.3183098862,0.6366197724,1.1283791671,1.4142135624,0.7071067812]
		self.mapped[81].resolve_generated_offsets("min","max","whiskerLow","whiskerHigh","percentile1","percentile5","percentile25","percentile50","percentile75","percentile95","percentile99","countOutliersLow","countOutliersHigh","percentageOutliersLow","percentageOutliersHigh","sum","avg","std","size")
		self.mapped[82].resolve_generated_offsets("seed","v")
		self.mapped[85].resolve_generated_offsets("start","total","counter","duration","progress","speed","remaining")
		self.mapped[87].resolve_generated_offsets("sum","sum_sq","count","min","max")
		self.mapped[89].static_values = [0,1,2,3,4,5,6]
		self.mapped[90].static_values = [0,1,2,3]
		self.mapped[92].resolve_generated_offsets("min","max","whiskerLow","whiskerHigh","percentile1","percentile5","percentile25","percentile50","percentile75","percentile95","percentile99","countOutliersLow","countOutliersHigh","percentageOutliersLow","percentageOutliersHigh","sum","avg","std","size")
		self.mapped[93].static_values = [0,1,2,3]
from ai.greycat.std import std as std_
