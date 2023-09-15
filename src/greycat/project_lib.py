# AUTO-GENERATED FILE PLEASE DO NOT MODIFY MANUALLY
from __future__ import annotations
from ctypes import *
from typing import *
from greycat.greycat import GreyCat
@final
class project_lib(GreyCat.Library):
	name_: Final[str] = "project_lib"
	def name(self) -> str:
		return self.name_
	@final
	class project:
		@final
		class TestType(GreyCat.Object):
			name_: Final[str] = "project::TestType"
			def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
				super().__init__(type, attributes)
			@staticmethod
			def i(greycat: GreyCat) -> int:
				t: Final[GreyCat.Type] = greycat.libs_by_name[project_lib.name_].mapped[0]
				return t.static_values[0]
			@staticmethod
			def create(greycat: GreyCat) -> project_lib_.project.TestType:
				return project_lib_.project.TestType(greycat.libs_by_name[project_lib.name_].mapped[0])
		@staticmethod
		def get_gcb(greycat: GreyCat) -> std_.core.Array:
			return GreyCat.call(greycat,"project::get_gcb")
		@staticmethod
		def display(greycat: GreyCat, v: Any) -> Any:
			return GreyCat.call(greycat,"project::display", v)
	def configure(self, loaders: dict[str, GreyCat.Loader], factories: dict[str, GreyCat.Factory]) -> None:
		factories[project_lib_.project.TestType.name_] = lambda type, attributes: project_lib_.project.TestType(type, attributes)
	def init(self, greycat: GreyCat) -> None:
		self.mapped: list[GreyCat.Type] = [
			greycat.types_by_name[project_lib.project.TestType.name_],
			]
		self.mapped[0].static_values = [12]
from greycat. import  as _
