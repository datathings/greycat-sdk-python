# AUTO-GENERATED FILE PLEASE DO NOT MODIFY MANUALLY
from __future__ import annotations
from ctypes import *
from typing import *
import struct
from greycat.greycat import GreyCat
from greycat.algebra_n import algebra_n
from greycat.std import std


@final
class algebra(GreyCat.Library):
    name_: Final[str] = "algebra"

    def name(self) -> str:
        return self.name_

    @final
    class compute:

        @final
        class ComputeOperationFill(GreyCat.Object):
            name_: Final[str] = "compute::ComputeOperationFill"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def input(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_input(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def value(self) -> Any:
                return self._get(self.type_.generated_offsets[1])

            def set_value(self, v: Any) -> None:
                self._set(self.type_.generated_offsets[1], v)

            @staticmethod
            def create(greycat: GreyCat, input: str, value: Any) -> algebra.compute.ComputeOperationFill:
                return algebra.compute.ComputeOperationFill(greycat.libs_by_name[algebra.name_].mapped[0], [input, value])

        @final
        class ComputeRegressionLoss(GreyCat.Enum):
            name_: Final[str] = "compute::ComputeRegressionLoss"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            @staticmethod
            def square(greycat: GreyCat) -> algebra.compute.ComputeRegressionLoss:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[1]
                return t.enum_values[t.generated_offsets[0]]

            @staticmethod
            def abs(greycat: GreyCat) -> algebra.compute.ComputeRegressionLoss:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[1]
                return t.enum_values[t.generated_offsets[1]]

            @staticmethod
            def create(greycat: GreyCat) -> algebra.compute.ComputeRegressionLoss:
                return algebra.compute.ComputeRegressionLoss(greycat.libs_by_name[algebra.name_].mapped[1], [])

        @final
        class ComputeOptimizerRmsProp(GreyCat.Object):
            name_: Final[str] = "compute::ComputeOptimizerRmsProp"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def learning_rate(self) -> float:
                return self._get(self.type_.generated_offsets[0])

            def set_learning_rate(self, v: float) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def decay_rate(self) -> float:
                return self._get(self.type_.generated_offsets[1])

            def set_decay_rate(self, v: float) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def smooth_epsilon(self) -> float:
                return self._get(self.type_.generated_offsets[2])

            def set_smooth_epsilon(self, v: float) -> None:
                self._set(self.type_.generated_offsets[2], v)

            @staticmethod
            def learning_rate_def(greycat: GreyCat) -> float:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[2]
                return t.static_values[0]

            @staticmethod
            def decay_rate_def(greycat: GreyCat) -> float:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[2]
                return t.static_values[1]

            @staticmethod
            def smooth_epsilon_def(greycat: GreyCat) -> float:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[2]
                return t.static_values[2]

            @staticmethod
            def create(greycat: GreyCat, learning_rate: float, decay_rate: float, smooth_epsilon: float) -> algebra.compute.ComputeOptimizerRmsProp:
                return algebra.compute.ComputeOptimizerRmsProp(greycat.libs_by_name[algebra.name_].mapped[2], [learning_rate, decay_rate, smooth_epsilon])

        @final
        class ComputeInitializerReluUniform(GreyCat.Object):
            name_: Final[str] = "compute::ComputeInitializerReluUniform"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            @staticmethod
            def create(greycat: GreyCat) -> algebra.compute.ComputeInitializerReluUniform:
                return algebra.compute.ComputeInitializerReluUniform(greycat.libs_by_name[algebra.name_].mapped[3], [])

        @final
        class ComputeOperationExp(GreyCat.Object):
            name_: Final[str] = "compute::ComputeOperationExp"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def input(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_input(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def output(self) -> str:
                return self._get(self.type_.generated_offsets[1])

            def set_output(self, v: str) -> None:
                self._set(self.type_.generated_offsets[1], v)

            @staticmethod
            def create(greycat: GreyCat, input: str, output: str) -> algebra.compute.ComputeOperationExp:
                return algebra.compute.ComputeOperationExp(greycat.libs_by_name[algebra.name_].mapped[4], [input, output])

        @final
        class ComputeInitializerNormalIn(GreyCat.Object):
            name_: Final[str] = "compute::ComputeInitializerNormalIn"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            @staticmethod
            def create(greycat: GreyCat) -> algebra.compute.ComputeInitializerNormalIn:
                return algebra.compute.ComputeInitializerNormalIn(greycat.libs_by_name[algebra.name_].mapped[5], [])

        @final
        class ComputeInitializerNone(GreyCat.Object):
            name_: Final[str] = "compute::ComputeInitializerNone"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            @staticmethod
            def create(greycat: GreyCat) -> algebra.compute.ComputeInitializerNone:
                return algebra.compute.ComputeInitializerNone(greycat.libs_by_name[algebra.name_].mapped[6], [])

        @final
        class ComputeOperationLeCunTanh(GreyCat.Object):
            name_: Final[str] = "compute::ComputeOperationLeCunTanh"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def input(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_input(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def output(self) -> str:
                return self._get(self.type_.generated_offsets[1])

            def set_output(self, v: str) -> None:
                self._set(self.type_.generated_offsets[1], v)

            @staticmethod
            def create(greycat: GreyCat, input: str, output: str) -> algebra.compute.ComputeOperationLeCunTanh:
                return algebra.compute.ComputeOperationLeCunTanh(greycat.libs_by_name[algebra.name_].mapped[7], [input, output])

        @final
        class ComputeOperationElu(GreyCat.Object):
            name_: Final[str] = "compute::ComputeOperationElu"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def input(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_input(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def output(self) -> str:
                return self._get(self.type_.generated_offsets[1])

            def set_output(self, v: str) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def alpha(self) -> float:
                return self._get(self.type_.generated_offsets[2])

            def set_alpha(self, v: float) -> None:
                self._set(self.type_.generated_offsets[2], v)

            @staticmethod
            def alpha_def(greycat: GreyCat) -> float:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[8]
                return t.static_values[0]

            @staticmethod
            def create(greycat: GreyCat, input: str, output: str, alpha: float) -> algebra.compute.ComputeOperationElu:
                return algebra.compute.ComputeOperationElu(greycat.libs_by_name[algebra.name_].mapped[8], [input, output, alpha])

        @final
        class ComputeOptimizerFtrl(GreyCat.Object):
            name_: Final[str] = "compute::ComputeOptimizerFtrl"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def learning_rate(self) -> float:
                return self._get(self.type_.generated_offsets[0])

            def set_learning_rate(self, v: float) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def lambda1(self) -> float:
                return self._get(self.type_.generated_offsets[1])

            def set_lambda1(self, v: float) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def lambda2(self) -> float:
                return self._get(self.type_.generated_offsets[2])

            def set_lambda2(self, v: float) -> None:
                self._set(self.type_.generated_offsets[2], v)

            def beta(self) -> float:
                return self._get(self.type_.generated_offsets[3])

            def set_beta(self, v: float) -> None:
                self._set(self.type_.generated_offsets[3], v)

            @staticmethod
            def learning_rate_def(greycat: GreyCat) -> float:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[9]
                return t.static_values[0]

            @staticmethod
            def beta_def(greycat: GreyCat) -> float:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[9]
                return t.static_values[1]

            @staticmethod
            def lambda1_def(greycat: GreyCat) -> float:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[9]
                return t.static_values[2]

            @staticmethod
            def lambda2_def(greycat: GreyCat) -> float:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[9]
                return t.static_values[3]

            @staticmethod
            def create(greycat: GreyCat, learning_rate: float, lambda1: float, lambda2: float, beta: float) -> algebra.compute.ComputeOptimizerFtrl:
                return algebra.compute.ComputeOptimizerFtrl(greycat.libs_by_name[algebra.name_].mapped[9], [learning_rate, lambda1, lambda2, beta])

        @final
        class ComputeActivationHardSigmoid(GreyCat.Object):
            name_: Final[str] = "compute::ComputeActivationHardSigmoid"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def slope(self) -> float:
                return self._get(self.type_.generated_offsets[0])

            def set_slope(self, v: float) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def shift(self) -> float:
                return self._get(self.type_.generated_offsets[1])

            def set_shift(self, v: float) -> None:
                self._set(self.type_.generated_offsets[1], v)

            @staticmethod
            def slope_def(greycat: GreyCat) -> float:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[10]
                return t.static_values[0]

            @staticmethod
            def shift_def(greycat: GreyCat) -> float:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[10]
                return t.static_values[1]

            @staticmethod
            def create(greycat: GreyCat, slope: float, shift: float) -> algebra.compute.ComputeActivationHardSigmoid:
                return algebra.compute.ComputeActivationHardSigmoid(greycat.libs_by_name[algebra.name_].mapped[10], [slope, shift])

        @final
        class ComputeInitializerSigmoidUniform(GreyCat.Object):
            name_: Final[str] = "compute::ComputeInitializerSigmoidUniform"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            @staticmethod
            def create(greycat: GreyCat) -> algebra.compute.ComputeInitializerSigmoidUniform:
                return algebra.compute.ComputeInitializerSigmoidUniform(greycat.libs_by_name[algebra.name_].mapped[11], [])

        @final
        class ComputeInitializerUniformOut(GreyCat.Object):
            name_: Final[str] = "compute::ComputeInitializerUniformOut"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            @staticmethod
            def create(greycat: GreyCat) -> algebra.compute.ComputeInitializerUniformOut:
                return algebra.compute.ComputeInitializerUniformOut(greycat.libs_by_name[algebra.name_].mapped[12], [])

        @final
        class ComputeOptimizer(GreyCat.Object):
            name_: Final[str] = "compute::ComputeOptimizer"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def learning_rate(self) -> float:
                return self._get(self.type_.generated_offsets[0])

            def set_learning_rate(self, v: float) -> None:
                self._set(self.type_.generated_offsets[0], v)

            @staticmethod
            def create(greycat: GreyCat, learning_rate: float) -> algebra.compute.ComputeOptimizer:
                return algebra.compute.ComputeOptimizer(greycat.libs_by_name[algebra.name_].mapped[13], [learning_rate])

        @final
        class ComputeActivationSigmoid(GreyCat.Object):
            name_: Final[str] = "compute::ComputeActivationSigmoid"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            @staticmethod
            def create(greycat: GreyCat) -> algebra.compute.ComputeActivationSigmoid:
                return algebra.compute.ComputeActivationSigmoid(greycat.libs_by_name[algebra.name_].mapped[14], [])

        @final
        class ComputeOperationAvg(GreyCat.Object):
            name_: Final[str] = "compute::ComputeOperationAvg"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def input(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_input(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def input2(self) -> str:
                return self._get(self.type_.generated_offsets[1])

            def set_input2(self, v: str) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def output(self) -> str:
                return self._get(self.type_.generated_offsets[2])

            def set_output(self, v: str) -> None:
                self._set(self.type_.generated_offsets[2], v)

            @staticmethod
            def create(greycat: GreyCat, input: str, input2: str, output: str) -> algebra.compute.ComputeOperationAvg:
                return algebra.compute.ComputeOperationAvg(greycat.libs_by_name[algebra.name_].mapped[15], [input, input2, output])

        @final
        class ComputeLayerActivation(GreyCat.Object):
            name_: Final[str] = "compute::ComputeLayerActivation"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def name(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_name(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def activation(self) -> algebra.compute.ComputeActivation:
                return self._get(self.type_.generated_offsets[1])

            def set_activation(self, v: algebra.compute.ComputeActivation) -> None:
                self._set(self.type_.generated_offsets[1], v)

            @staticmethod
            def var_input_name(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[16]
                return t.static_values[0]

            @staticmethod
            def var_output_name(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[16]
                return t.static_values[1]

            @staticmethod
            def create(greycat: GreyCat, name: str, activation: algebra.compute.ComputeActivation) -> algebra.compute.ComputeLayerActivation:
                return algebra.compute.ComputeLayerActivation(greycat.libs_by_name[algebra.name_].mapped[16], [name, activation])

        @final
        class ComputeLayerPCAScaler(GreyCat.Object):
            name_: Final[str] = "compute::ComputeLayerPCAScaler"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def name(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_name(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def type(self) -> std.core.TensorType:
                return self._get(self.type_.generated_offsets[1])

            def set_type(self, v: std.core.TensorType) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def inverse_transform(self) -> bool:
                return self._get(self.type_.generated_offsets[2])

            def set_inverse_transform(self, v: bool) -> None:
                self._set(self.type_.generated_offsets[2], v)

            @staticmethod
            def var_input_name(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[17]
                return t.static_values[0]

            @staticmethod
            def var_output_name(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[17]
                return t.static_values[1]

            @staticmethod
            def var_avg_name(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[17]
                return t.static_values[2]

            @staticmethod
            def var_std_name(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[17]
                return t.static_values[3]

            @staticmethod
            def var_space_name(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[17]
                return t.static_values[4]

            @staticmethod
            def create(greycat: GreyCat, name: str, type: std.core.TensorType, inverse_transform: bool) -> algebra.compute.ComputeLayerPCAScaler:
                return algebra.compute.ComputeLayerPCAScaler(greycat.libs_by_name[algebra.name_].mapped[17], [name, type, inverse_transform])

        @final
        class ComputeLayerLSTM(GreyCat.Object):
            name_: Final[str] = "compute::ComputeLayerLSTM"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def name(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_name(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def bias_initializer(self) -> algebra.compute.ComputeInitializer:
                return self._get(self.type_.generated_offsets[1])

            def set_bias_initializer(self, v: algebra.compute.ComputeInitializer) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def weight_regularizer(self) -> algebra.compute.ComputeRegularizer:
                return self._get(self.type_.generated_offsets[2])

            def set_weight_regularizer(self, v: algebra.compute.ComputeRegularizer) -> None:
                self._set(self.type_.generated_offsets[2], v)

            def bias_regularizer(self) -> algebra.compute.ComputeRegularizer:
                return self._get(self.type_.generated_offsets[3])

            def set_bias_regularizer(self, v: algebra.compute.ComputeRegularizer) -> None:
                self._set(self.type_.generated_offsets[3], v)

            def type(self) -> std.core.TensorType:
                return self._get(self.type_.generated_offsets[4])

            def set_type(self, v: std.core.TensorType) -> None:
                self._set(self.type_.generated_offsets[4], v)

            def use_bias(self) -> bool:
                return self._get(self.type_.generated_offsets[5])

            def set_use_bias(self, v: bool) -> None:
                self._set(self.type_.generated_offsets[5], v)

            def return_sequences(self) -> bool:
                return self._get(self.type_.generated_offsets[6])

            def set_return_sequences(self, v: bool) -> None:
                self._set(self.type_.generated_offsets[6], v)

            def bidirectional(self) -> bool:
                return self._get(self.type_.generated_offsets[7])

            def set_bidirectional(self, v: bool) -> None:
                self._set(self.type_.generated_offsets[7], v)

            def auto_init_states(self) -> bool:
                return self._get(self.type_.generated_offsets[8])

            def set_auto_init_states(self, v: bool) -> None:
                self._set(self.type_.generated_offsets[8], v)

            def inputs(self) -> int:
                return self._get(self.type_.generated_offsets[9])

            def set_inputs(self, v: int) -> None:
                self._set(self.type_.generated_offsets[9], v)

            def outputs(self) -> int:
                return self._get(self.type_.generated_offsets[10])

            def set_outputs(self, v: int) -> None:
                self._set(self.type_.generated_offsets[10], v)

            def layers(self) -> int:
                return self._get(self.type_.generated_offsets[11])

            def set_layers(self, v: int) -> None:
                self._set(self.type_.generated_offsets[11], v)

            def sequences(self) -> int:
                return self._get(self.type_.generated_offsets[12])

            def set_sequences(self, v: int) -> None:
                self._set(self.type_.generated_offsets[12], v)

            @staticmethod
            def var_input_name(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[18]
                return t.static_values[0]

            @staticmethod
            def var_output_name(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[18]
                return t.static_values[1]

            @staticmethod
            def var_hx_name(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[18]
                return t.static_values[2]

            @staticmethod
            def var_cx_name(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[18]
                return t.static_values[3]

            @staticmethod
            def var_hy_name(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[18]
                return t.static_values[4]

            @staticmethod
            def var_cy_name(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[18]
                return t.static_values[5]

            @staticmethod
            def var_weight_name(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[18]
                return t.static_values[6]

            @staticmethod
            def var_bias_name(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[18]
                return t.static_values[7]

            @staticmethod
            def var_internal_i_name(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[18]
                return t.static_values[8]

            @staticmethod
            def var_internal_f_name(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[18]
                return t.static_values[9]

            @staticmethod
            def var_internal_cp_name(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[18]
                return t.static_values[10]

            @staticmethod
            def var_internal_o_name(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[18]
                return t.static_values[11]

            @staticmethod
            def var_internal_h_name(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[18]
                return t.static_values[12]

            @staticmethod
            def var_internal_c_name(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[18]
                return t.static_values[13]

            @staticmethod
            def var_internal_mult_name(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[18]
                return t.static_values[14]

            @staticmethod
            def var_internal_output_name(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[18]
                return t.static_values[15]

            @staticmethod
            def create(greycat: GreyCat, name: str, bias_initializer: algebra.compute.ComputeInitializer, weight_regularizer: algebra.compute.ComputeRegularizer, bias_regularizer: algebra.compute.ComputeRegularizer, type: std.core.TensorType, use_bias: bool, return_sequences: bool, bidirectional: bool, auto_init_states: bool, inputs: int, outputs: int, layers: int, sequences: int) -> algebra.compute.ComputeLayerLSTM:
                return algebra.compute.ComputeLayerLSTM(greycat.libs_by_name[algebra.name_].mapped[18], [name, bias_initializer, weight_regularizer, bias_regularizer, type, use_bias, return_sequences, bidirectional, auto_init_states, inputs, outputs, layers, sequences])

        @final
        class ComputeVar(GreyCat.Object):
            name_: Final[str] = "compute::ComputeVar"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def name(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_name(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            @staticmethod
            def create(greycat: GreyCat, name: str) -> algebra.compute.ComputeVar:
                return algebra.compute.ComputeVar(greycat.libs_by_name[algebra.name_].mapped[19], [name])

        @final
        class ComputeOperationSelu(GreyCat.Object):
            name_: Final[str] = "compute::ComputeOperationSelu"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def input(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_input(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def output(self) -> str:
                return self._get(self.type_.generated_offsets[1])

            def set_output(self, v: str) -> None:
                self._set(self.type_.generated_offsets[1], v)

            @staticmethod
            def create(greycat: GreyCat, input: str, output: str) -> algebra.compute.ComputeOperationSelu:
                return algebra.compute.ComputeOperationSelu(greycat.libs_by_name[algebra.name_].mapped[20], [input, output])

        @final
        class ComputeOperationHardSigmoid(GreyCat.Object):
            name_: Final[str] = "compute::ComputeOperationHardSigmoid"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def input(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_input(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def output(self) -> str:
                return self._get(self.type_.generated_offsets[1])

            def set_output(self, v: str) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def slope(self) -> float:
                return self._get(self.type_.generated_offsets[2])

            def set_slope(self, v: float) -> None:
                self._set(self.type_.generated_offsets[2], v)

            def shift(self) -> float:
                return self._get(self.type_.generated_offsets[3])

            def set_shift(self, v: float) -> None:
                self._set(self.type_.generated_offsets[3], v)

            @staticmethod
            def slope_def(greycat: GreyCat) -> float:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[21]
                return t.static_values[0]

            @staticmethod
            def shift_def(greycat: GreyCat) -> float:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[21]
                return t.static_values[1]

            @staticmethod
            def create(greycat: GreyCat, input: str, output: str, slope: float, shift: float) -> algebra.compute.ComputeOperationHardSigmoid:
                return algebra.compute.ComputeOperationHardSigmoid(greycat.libs_by_name[algebra.name_].mapped[21], [input, output, slope, shift])

        @final
        class ComputeOperationSin(GreyCat.Object):
            name_: Final[str] = "compute::ComputeOperationSin"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def input(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_input(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def output(self) -> str:
                return self._get(self.type_.generated_offsets[1])

            def set_output(self, v: str) -> None:
                self._set(self.type_.generated_offsets[1], v)

            @staticmethod
            def create(greycat: GreyCat, input: str, output: str) -> algebra.compute.ComputeOperationSin:
                return algebra.compute.ComputeOperationSin(greycat.libs_by_name[algebra.name_].mapped[22], [input, output])

        @final
        class ComputeOperationSoftSign(GreyCat.Object):
            name_: Final[str] = "compute::ComputeOperationSoftSign"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def input(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_input(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def output(self) -> str:
                return self._get(self.type_.generated_offsets[1])

            def set_output(self, v: str) -> None:
                self._set(self.type_.generated_offsets[1], v)

            @staticmethod
            def create(greycat: GreyCat, input: str, output: str) -> algebra.compute.ComputeOperationSoftSign:
                return algebra.compute.ComputeOperationSoftSign(greycat.libs_by_name[algebra.name_].mapped[23], [input, output])

        @final
        class ComputeLayerFilter(GreyCat.Object):
            name_: Final[str] = "compute::ComputeLayerFilter"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def name(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_name(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def type(self) -> std.core.TensorType:
                return self._get(self.type_.generated_offsets[1])

            def set_type(self, v: std.core.TensorType) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def inputs(self) -> int:
                return self._get(self.type_.generated_offsets[2])

            def set_inputs(self, v: int) -> None:
                self._set(self.type_.generated_offsets[2], v)

            def outputs(self) -> int:
                return self._get(self.type_.generated_offsets[3])

            def set_outputs(self, v: int) -> None:
                self._set(self.type_.generated_offsets[3], v)

            def maskValues(self) -> std.core.Array:
                return self._get(self.type_.generated_offsets[4])

            def set_maskValues(self, v: std.core.Array) -> None:
                self._set(self.type_.generated_offsets[4], v)

            @staticmethod
            def var_input_name(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[24]
                return t.static_values[0]

            @staticmethod
            def var_output_name(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[24]
                return t.static_values[1]

            @staticmethod
            def var_mask_name(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[24]
                return t.static_values[2]

            @staticmethod
            def create(greycat: GreyCat, name: str, type: std.core.TensorType, inputs: int, outputs: int, maskValues: std.core.Array) -> algebra.compute.ComputeLayerFilter:
                return algebra.compute.ComputeLayerFilter(greycat.libs_by_name[algebra.name_].mapped[24], [name, type, inputs, outputs, maskValues])

        @final
        class ComputeOptimizerSgd(GreyCat.Object):
            name_: Final[str] = "compute::ComputeOptimizerSgd"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def learning_rate(self) -> float:
                return self._get(self.type_.generated_offsets[0])

            def set_learning_rate(self, v: float) -> None:
                self._set(self.type_.generated_offsets[0], v)

            @staticmethod
            def learning_rate_def(greycat: GreyCat) -> float:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[25]
                return t.static_values[0]

            @staticmethod
            def create(greycat: GreyCat, learning_rate: float) -> algebra.compute.ComputeOptimizerSgd:
                return algebra.compute.ComputeOptimizerSgd(greycat.libs_by_name[algebra.name_].mapped[25], [learning_rate])

        @final
        class ComputeVarProxy(GreyCat.Object):
            name_: Final[str] = "compute::ComputeVarProxy"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def name(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_name(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            @staticmethod
            def create(greycat: GreyCat, name: str) -> algebra.compute.ComputeVarProxy:
                return algebra.compute.ComputeVarProxy(greycat.libs_by_name[algebra.name_].mapped[26], [name])

        @final
        class ComputeActivationSelu(GreyCat.Object):
            name_: Final[str] = "compute::ComputeActivationSelu"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            @staticmethod
            def create(greycat: GreyCat) -> algebra.compute.ComputeActivationSelu:
                return algebra.compute.ComputeActivationSelu(greycat.libs_by_name[algebra.name_].mapped[27], [])

        @final
        class ComputeOperationLog(GreyCat.Object):
            name_: Final[str] = "compute::ComputeOperationLog"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def input(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_input(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def output(self) -> str:
                return self._get(self.type_.generated_offsets[1])

            def set_output(self, v: str) -> None:
                self._set(self.type_.generated_offsets[1], v)

            @staticmethod
            def create(greycat: GreyCat, input: str, output: str) -> algebra.compute.ComputeOperationLog:
                return algebra.compute.ComputeOperationLog(greycat.libs_by_name[algebra.name_].mapped[28], [input, output])

        @final
        class ComputeInitializerIdentity(GreyCat.Object):
            name_: Final[str] = "compute::ComputeInitializerIdentity"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            @staticmethod
            def create(greycat: GreyCat) -> algebra.compute.ComputeInitializerIdentity:
                return algebra.compute.ComputeInitializerIdentity(greycat.libs_by_name[algebra.name_].mapped[29], [])

        @final
        class ComputeInitializerGlorotUniform(GreyCat.Object):
            name_: Final[str] = "compute::ComputeInitializerGlorotUniform"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            @staticmethod
            def create(greycat: GreyCat) -> algebra.compute.ComputeInitializerGlorotUniform:
                return algebra.compute.ComputeInitializerGlorotUniform(greycat.libs_by_name[algebra.name_].mapped[30], [])

        @final
        class ComputeActivationRelu(GreyCat.Object):
            name_: Final[str] = "compute::ComputeActivationRelu"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def max_value(self) -> float:
                return self._get(self.type_.generated_offsets[0])

            def set_max_value(self, v: float) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def threshold(self) -> float:
                return self._get(self.type_.generated_offsets[1])

            def set_threshold(self, v: float) -> None:
                self._set(self.type_.generated_offsets[1], v)

            @staticmethod
            def threshold_def(greycat: GreyCat) -> float:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[31]
                return t.static_values[0]

            @staticmethod
            def create(greycat: GreyCat, max_value: float, threshold: float) -> algebra.compute.ComputeActivationRelu:
                return algebra.compute.ComputeActivationRelu(greycat.libs_by_name[algebra.name_].mapped[31], [max_value, threshold])

        @final
        class ComputeActivationElu(GreyCat.Object):
            name_: Final[str] = "compute::ComputeActivationElu"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def alpha(self) -> float:
                return self._get(self.type_.generated_offsets[0])

            def set_alpha(self, v: float) -> None:
                self._set(self.type_.generated_offsets[0], v)

            @staticmethod
            def alpha_def(greycat: GreyCat) -> float:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[32]
                return t.static_values[0]

            @staticmethod
            def create(greycat: GreyCat, alpha: float) -> algebra.compute.ComputeActivationElu:
                return algebra.compute.ComputeActivationElu(greycat.libs_by_name[algebra.name_].mapped[32], [alpha])

        @final
        class ComputeOperationAcos(GreyCat.Object):
            name_: Final[str] = "compute::ComputeOperationAcos"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def input(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_input(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def output(self) -> str:
                return self._get(self.type_.generated_offsets[1])

            def set_output(self, v: str) -> None:
                self._set(self.type_.generated_offsets[1], v)

            @staticmethod
            def create(greycat: GreyCat, input: str, output: str) -> algebra.compute.ComputeOperationAcos:
                return algebra.compute.ComputeOperationAcos(greycat.libs_by_name[algebra.name_].mapped[33], [input, output])

        @final
        class ComputeLayerMinMaxScaler(GreyCat.Object):
            name_: Final[str] = "compute::ComputeLayerMinMaxScaler"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def name(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_name(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def type(self) -> std.core.TensorType:
                return self._get(self.type_.generated_offsets[1])

            def set_type(self, v: std.core.TensorType) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def inverse_transform(self) -> bool:
                return self._get(self.type_.generated_offsets[2])

            def set_inverse_transform(self, v: bool) -> None:
                self._set(self.type_.generated_offsets[2], v)

            @staticmethod
            def var_input_name(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[34]
                return t.static_values[0]

            @staticmethod
            def var_output_name(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[34]
                return t.static_values[1]

            @staticmethod
            def var_min_name(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[34]
                return t.static_values[2]

            @staticmethod
            def var_max_name(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[34]
                return t.static_values[3]

            @staticmethod
            def create(greycat: GreyCat, name: str, type: std.core.TensorType, inverse_transform: bool) -> algebra.compute.ComputeLayerMinMaxScaler:
                return algebra.compute.ComputeLayerMinMaxScaler(greycat.libs_by_name[algebra.name_].mapped[34], [name, type, inverse_transform])

        @final
        class ComputeActivationLeakyRelu(GreyCat.Object):
            name_: Final[str] = "compute::ComputeActivationLeakyRelu"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def alpha(self) -> float:
                return self._get(self.type_.generated_offsets[0])

            def set_alpha(self, v: float) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def max_value(self) -> float:
                return self._get(self.type_.generated_offsets[1])

            def set_max_value(self, v: float) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def threshold(self) -> float:
                return self._get(self.type_.generated_offsets[2])

            def set_threshold(self, v: float) -> None:
                self._set(self.type_.generated_offsets[2], v)

            @staticmethod
            def alpha_def(greycat: GreyCat) -> float:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[35]
                return t.static_values[0]

            @staticmethod
            def threshold_def(greycat: GreyCat) -> float:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[35]
                return t.static_values[1]

            @staticmethod
            def create(greycat: GreyCat, alpha: float, max_value: float, threshold: float) -> algebra.compute.ComputeActivationLeakyRelu:
                return algebra.compute.ComputeActivationLeakyRelu(greycat.libs_by_name[algebra.name_].mapped[35], [alpha, max_value, threshold])

        @final
        class ComputeInitializerRelu(GreyCat.Object):
            name_: Final[str] = "compute::ComputeInitializerRelu"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            @staticmethod
            def create(greycat: GreyCat) -> algebra.compute.ComputeInitializerRelu:
                return algebra.compute.ComputeInitializerRelu(greycat.libs_by_name[algebra.name_].mapped[36], [])

        @final
        class ComputeActivationExp(GreyCat.Object):
            name_: Final[str] = "compute::ComputeActivationExp"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            @staticmethod
            def create(greycat: GreyCat) -> algebra.compute.ComputeActivationExp:
                return algebra.compute.ComputeActivationExp(greycat.libs_by_name[algebra.name_].mapped[37], [])

        @final
        class ComputeInitializerPytorch(GreyCat.Object):
            name_: Final[str] = "compute::ComputeInitializerPytorch"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            @staticmethod
            def create(greycat: GreyCat) -> algebra.compute.ComputeInitializerPytorch:
                return algebra.compute.ComputeInitializerPytorch(greycat.libs_by_name[algebra.name_].mapped[38], [])

        @final
        class ComputeOperationMul(GreyCat.Object):
            name_: Final[str] = "compute::ComputeOperationMul"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def input(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_input(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def input2(self) -> str:
                return self._get(self.type_.generated_offsets[1])

            def set_input2(self, v: str) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def output(self) -> str:
                return self._get(self.type_.generated_offsets[2])

            def set_output(self, v: str) -> None:
                self._set(self.type_.generated_offsets[2], v)

            @staticmethod
            def create(greycat: GreyCat, input: str, input2: str, output: str) -> algebra.compute.ComputeOperationMul:
                return algebra.compute.ComputeOperationMul(greycat.libs_by_name[algebra.name_].mapped[39], [input, input2, output])

        @final
        class ComputeOperationSign(GreyCat.Object):
            name_: Final[str] = "compute::ComputeOperationSign"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def input(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_input(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def output(self) -> str:
                return self._get(self.type_.generated_offsets[1])

            def set_output(self, v: str) -> None:
                self._set(self.type_.generated_offsets[1], v)

            @staticmethod
            def create(greycat: GreyCat, input: str, output: str) -> algebra.compute.ComputeOperationSign:
                return algebra.compute.ComputeOperationSign(greycat.libs_by_name[algebra.name_].mapped[40], [input, output])

        @final
        class ComputeOperationAtanh(GreyCat.Object):
            name_: Final[str] = "compute::ComputeOperationAtanh"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def input(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_input(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def output(self) -> str:
                return self._get(self.type_.generated_offsets[1])

            def set_output(self, v: str) -> None:
                self._set(self.type_.generated_offsets[1], v)

            @staticmethod
            def create(greycat: GreyCat, input: str, output: str) -> algebra.compute.ComputeOperationAtanh:
                return algebra.compute.ComputeOperationAtanh(greycat.libs_by_name[algebra.name_].mapped[41], [input, output])

        @final
        class ComputeCounter(GreyCat.Object):
            name_: Final[str] = "compute::ComputeCounter"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def epoch(self) -> int:
                return self._get(self.type_.generated_offsets[0])

            def set_epoch(self, v: int) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def optimizationSteps(self) -> int:
                return self._get(self.type_.generated_offsets[1])

            def set_optimizationSteps(self, v: int) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def batchNotOptimized(self) -> int:
                return self._get(self.type_.generated_offsets[2])

            def set_batchNotOptimized(self, v: int) -> None:
                self._set(self.type_.generated_offsets[2], v)

            @staticmethod
            def create(greycat: GreyCat, epoch: int, optimizationSteps: int, batchNotOptimized: int) -> algebra.compute.ComputeCounter:
                return algebra.compute.ComputeCounter(greycat.libs_by_name[algebra.name_].mapped[42], [epoch, optimizationSteps, batchNotOptimized])

        @final
        class ComputeOperationAddBias(GreyCat.Object):
            name_: Final[str] = "compute::ComputeOperationAddBias"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def input(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_input(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def input2(self) -> str:
                return self._get(self.type_.generated_offsets[1])

            def set_input2(self, v: str) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def output(self) -> str:
                return self._get(self.type_.generated_offsets[2])

            def set_output(self, v: str) -> None:
                self._set(self.type_.generated_offsets[2], v)

            @staticmethod
            def create(greycat: GreyCat, input: str, input2: str, output: str) -> algebra.compute.ComputeOperationAddBias:
                return algebra.compute.ComputeOperationAddBias(greycat.libs_by_name[algebra.name_].mapped[43], [input, input2, output])

        @final
        class ComputeInitializerUniformIn(GreyCat.Object):
            name_: Final[str] = "compute::ComputeInitializerUniformIn"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            @staticmethod
            def create(greycat: GreyCat) -> algebra.compute.ComputeInitializerUniformIn:
                return algebra.compute.ComputeInitializerUniformIn(greycat.libs_by_name[algebra.name_].mapped[44], [])

        @final
        class ComputeLayerCall(GreyCat.Object):
            name_: Final[str] = "compute::ComputeLayerCall"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def layer_name(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_layer_name(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def bindings(self) -> std.core.Array:
                return self._get(self.type_.generated_offsets[1])

            def set_bindings(self, v: std.core.Array) -> None:
                self._set(self.type_.generated_offsets[1], v)

            @staticmethod
            def create(greycat: GreyCat, layer_name: str, bindings: std.core.Array) -> algebra.compute.ComputeLayerCall:
                return algebra.compute.ComputeLayerCall(greycat.libs_by_name[algebra.name_].mapped[45], [layer_name, bindings])

        @final
        class ComputeOptimizerMomentum(GreyCat.Object):
            name_: Final[str] = "compute::ComputeOptimizerMomentum"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def learning_rate(self) -> float:
                return self._get(self.type_.generated_offsets[0])

            def set_learning_rate(self, v: float) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def decay_rate(self) -> float:
                return self._get(self.type_.generated_offsets[1])

            def set_decay_rate(self, v: float) -> None:
                self._set(self.type_.generated_offsets[1], v)

            @staticmethod
            def learning_rate_def(greycat: GreyCat) -> float:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[46]
                return t.static_values[0]

            @staticmethod
            def decay_rate_def(greycat: GreyCat) -> float:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[46]
                return t.static_values[1]

            @staticmethod
            def create(greycat: GreyCat, learning_rate: float, decay_rate: float) -> algebra.compute.ComputeOptimizerMomentum:
                return algebra.compute.ComputeOptimizerMomentum(greycat.libs_by_name[algebra.name_].mapped[46], [learning_rate, decay_rate])

        @final
        class ComputeOperationMatMul(GreyCat.Object):
            name_: Final[str] = "compute::ComputeOperationMatMul"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def input(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_input(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def input2(self) -> str:
                return self._get(self.type_.generated_offsets[1])

            def set_input2(self, v: str) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def output(self) -> str:
                return self._get(self.type_.generated_offsets[2])

            def set_output(self, v: str) -> None:
                self._set(self.type_.generated_offsets[2], v)

            def transposeA(self) -> bool:
                return self._get(self.type_.generated_offsets[3])

            def set_transposeA(self, v: bool) -> None:
                self._set(self.type_.generated_offsets[3], v)

            def transposeB(self) -> bool:
                return self._get(self.type_.generated_offsets[4])

            def set_transposeB(self, v: bool) -> None:
                self._set(self.type_.generated_offsets[4], v)

            def alpha(self) -> float:
                return self._get(self.type_.generated_offsets[5])

            def set_alpha(self, v: float) -> None:
                self._set(self.type_.generated_offsets[5], v)

            def beta(self) -> float:
                return self._get(self.type_.generated_offsets[6])

            def set_beta(self, v: float) -> None:
                self._set(self.type_.generated_offsets[6], v)

            @staticmethod
            def transpose_def(greycat: GreyCat) -> bool:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[47]
                return t.static_values[0]

            @staticmethod
            def alpha_def(greycat: GreyCat) -> float:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[47]
                return t.static_values[1]

            @staticmethod
            def beta_def(greycat: GreyCat) -> float:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[47]
                return t.static_values[2]

            @staticmethod
            def create(greycat: GreyCat, input: str, input2: str, output: str, transposeA: bool, transposeB: bool, alpha: float, beta: float) -> algebra.compute.ComputeOperationMatMul:
                return algebra.compute.ComputeOperationMatMul(greycat.libs_by_name[algebra.name_].mapped[47], [input, input2, output, transposeA, transposeB, alpha, beta])

        @final
        class ComputeOptimizerAdaDelta(GreyCat.Object):
            name_: Final[str] = "compute::ComputeOptimizerAdaDelta"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def learning_rate(self) -> float:
                return self._get(self.type_.generated_offsets[0])

            def set_learning_rate(self, v: float) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def decay_rate(self) -> float:
                return self._get(self.type_.generated_offsets[1])

            def set_decay_rate(self, v: float) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def smooth_epsilon(self) -> float:
                return self._get(self.type_.generated_offsets[2])

            def set_smooth_epsilon(self, v: float) -> None:
                self._set(self.type_.generated_offsets[2], v)

            @staticmethod
            def learning_rate_def(greycat: GreyCat) -> float:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[48]
                return t.static_values[0]

            @staticmethod
            def decay_rate_def(greycat: GreyCat) -> float:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[48]
                return t.static_values[1]

            @staticmethod
            def smooth_epsilon_def(greycat: GreyCat) -> float:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[48]
                return t.static_values[2]

            @staticmethod
            def create(greycat: GreyCat, learning_rate: float, decay_rate: float, smooth_epsilon: float) -> algebra.compute.ComputeOptimizerAdaDelta:
                return algebra.compute.ComputeOptimizerAdaDelta(greycat.libs_by_name[algebra.name_].mapped[48], [learning_rate, decay_rate, smooth_epsilon])

        @final
        class ComputeOperationArg(GreyCat.Object):
            name_: Final[str] = "compute::ComputeOperationArg"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def input(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_input(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def output(self) -> str:
                return self._get(self.type_.generated_offsets[1])

            def set_output(self, v: str) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def output2(self) -> str:
                return self._get(self.type_.generated_offsets[2])

            def set_output2(self, v: str) -> None:
                self._set(self.type_.generated_offsets[2], v)

            @staticmethod
            def create(greycat: GreyCat, input: str, output: str, output2: str) -> algebra.compute.ComputeOperationArg:
                return algebra.compute.ComputeOperationArg(greycat.libs_by_name[algebra.name_].mapped[49], [input, output, output2])

        @final
        class ComputeLayer(GreyCat.Object):
            name_: Final[str] = "compute::ComputeLayer"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def name(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_name(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            @staticmethod
            def create(greycat: GreyCat, name: str) -> algebra.compute.ComputeLayer:
                return algebra.compute.ComputeLayer(greycat.libs_by_name[algebra.name_].mapped[50], [name])

        @final
        class ComputeInitializerNormalAvg(GreyCat.Object):
            name_: Final[str] = "compute::ComputeInitializerNormalAvg"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            @staticmethod
            def create(greycat: GreyCat) -> algebra.compute.ComputeInitializerNormalAvg:
                return algebra.compute.ComputeInitializerNormalAvg(greycat.libs_by_name[algebra.name_].mapped[51], [])

        @final
        class ComputeOperationTan(GreyCat.Object):
            name_: Final[str] = "compute::ComputeOperationTan"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def input(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_input(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def output(self) -> str:
                return self._get(self.type_.generated_offsets[1])

            def set_output(self, v: str) -> None:
                self._set(self.type_.generated_offsets[1], v)

            @staticmethod
            def create(greycat: GreyCat, input: str, output: str) -> algebra.compute.ComputeOperationTan:
                return algebra.compute.ComputeOperationTan(greycat.libs_by_name[algebra.name_].mapped[52], [input, output])

        @final
        class ComputeOperationAsin(GreyCat.Object):
            name_: Final[str] = "compute::ComputeOperationAsin"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def input(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_input(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def output(self) -> str:
                return self._get(self.type_.generated_offsets[1])

            def set_output(self, v: str) -> None:
                self._set(self.type_.generated_offsets[1], v)

            @staticmethod
            def create(greycat: GreyCat, input: str, output: str) -> algebra.compute.ComputeOperationAsin:
                return algebra.compute.ComputeOperationAsin(greycat.libs_by_name[algebra.name_].mapped[53], [input, output])

        @final
        class ComputeInitializerUniform(GreyCat.Object):
            name_: Final[str] = "compute::ComputeInitializerUniform"

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

            @staticmethod
            def create(greycat: GreyCat, min: float, max: float) -> algebra.compute.ComputeInitializerUniform:
                return algebra.compute.ComputeInitializerUniform(greycat.libs_by_name[algebra.name_].mapped[54], [min, max])

        @final
        class ComputeOperationSum(GreyCat.Object):
            name_: Final[str] = "compute::ComputeOperationSum"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def input(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_input(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def output(self) -> str:
                return self._get(self.type_.generated_offsets[1])

            def set_output(self, v: str) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def axis(self) -> int:
                return self._get(self.type_.generated_offsets[2])

            def set_axis(self, v: int) -> None:
                self._set(self.type_.generated_offsets[2], v)

            @staticmethod
            def create(greycat: GreyCat, input: str, output: str, axis: int) -> algebra.compute.ComputeOperationSum:
                return algebra.compute.ComputeOperationSum(greycat.libs_by_name[algebra.name_].mapped[55], [input, output, axis])

        @final
        class ComputeLayerLoss(GreyCat.Object):
            name_: Final[str] = "compute::ComputeLayerLoss"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def name(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_name(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def reduction(self) -> algebra.compute.ComputeReduction:
                return self._get(self.type_.generated_offsets[1])

            def set_reduction(self, v: algebra.compute.ComputeReduction) -> None:
                self._set(self.type_.generated_offsets[1], v)

            @staticmethod
            def var_computed_name(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[56]
                return t.static_values[0]

            @staticmethod
            def var_expected_name(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[56]
                return t.static_values[1]

            @staticmethod
            def var_loss_name(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[56]
                return t.static_values[2]

            @staticmethod
            def create(greycat: GreyCat, name: str, reduction: algebra.compute.ComputeReduction) -> algebra.compute.ComputeLayerLoss:
                return algebra.compute.ComputeLayerLoss(greycat.libs_by_name[algebra.name_].mapped[56], [name, reduction])

        @final
        class ComputeOptimizerAdaMax(GreyCat.Object):
            name_: Final[str] = "compute::ComputeOptimizerAdaMax"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def learning_rate(self) -> float:
                return self._get(self.type_.generated_offsets[0])

            def set_learning_rate(self, v: float) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def beta1(self) -> float:
                return self._get(self.type_.generated_offsets[1])

            def set_beta1(self, v: float) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def beta2(self) -> float:
                return self._get(self.type_.generated_offsets[2])

            def set_beta2(self, v: float) -> None:
                self._set(self.type_.generated_offsets[2], v)

            def smooth_epsilon(self) -> float:
                return self._get(self.type_.generated_offsets[3])

            def set_smooth_epsilon(self, v: float) -> None:
                self._set(self.type_.generated_offsets[3], v)

            @staticmethod
            def learning_rate_def(greycat: GreyCat) -> float:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[57]
                return t.static_values[0]

            @staticmethod
            def beta1_def(greycat: GreyCat) -> float:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[57]
                return t.static_values[1]

            @staticmethod
            def beta2_def(greycat: GreyCat) -> float:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[57]
                return t.static_values[2]

            @staticmethod
            def smooth_epsilon_def(greycat: GreyCat) -> float:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[57]
                return t.static_values[3]

            @staticmethod
            def create(greycat: GreyCat, learning_rate: float, beta1: float, beta2: float, smooth_epsilon: float) -> algebra.compute.ComputeOptimizerAdaMax:
                return algebra.compute.ComputeOptimizerAdaMax(greycat.libs_by_name[algebra.name_].mapped[57], [learning_rate, beta1, beta2, smooth_epsilon])

        @final
        class ComputeOperationFilter(GreyCat.Object):
            name_: Final[str] = "compute::ComputeOperationFilter"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def input(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_input(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def output(self) -> str:
                return self._get(self.type_.generated_offsets[1])

            def set_output(self, v: str) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def mask(self) -> str:
                return self._get(self.type_.generated_offsets[2])

            def set_mask(self, v: str) -> None:
                self._set(self.type_.generated_offsets[2], v)

            def nbOutputs(self) -> int:
                return self._get(self.type_.generated_offsets[3])

            def set_nbOutputs(self, v: int) -> None:
                self._set(self.type_.generated_offsets[3], v)

            @staticmethod
            def create(greycat: GreyCat, input: str, output: str, mask: str, nbOutputs: int) -> algebra.compute.ComputeOperationFilter:
                return algebra.compute.ComputeOperationFilter(greycat.libs_by_name[algebra.name_].mapped[58], [input, output, mask, nbOutputs])

        @final
        class ComputeEngine(algebra_n.compute._ComputeEngine):
            name_: Final[str] = "compute::ComputeEngine"

            def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
                super().__init__(type)

            @staticmethod
            def create(greycat: GreyCat) -> algebra_n.compute._ComputeEngine:
                return algebra.compute.ComputeEngine(greycat.libs_by_name[algebra.name_].mapped[59], [])

        @final
        class ComputeVarConst(GreyCat.Object):
            name_: Final[str] = "compute::ComputeVarConst"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def name(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_name(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def type(self) -> std.core.TensorType:
                return self._get(self.type_.generated_offsets[1])

            def set_type(self, v: std.core.TensorType) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def shape(self) -> std.core.Array:
                return self._get(self.type_.generated_offsets[2])

            def set_shape(self, v: std.core.Array) -> None:
                self._set(self.type_.generated_offsets[2], v)

            @staticmethod
            def create(greycat: GreyCat, name: str, type: std.core.TensorType, shape: std.core.Array) -> algebra.compute.ComputeVarConst:
                return algebra.compute.ComputeVarConst(greycat.libs_by_name[algebra.name_].mapped[60], [name, type, shape])

        @final
        class ComputeInitializer(GreyCat.Object):
            name_: Final[str] = "compute::ComputeInitializer"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            @staticmethod
            def create(greycat: GreyCat) -> algebra.compute.ComputeInitializer:
                return algebra.compute.ComputeInitializer(greycat.libs_by_name[algebra.name_].mapped[61], [])

        @final
        class ComputeReduction(GreyCat.Enum):
            name_: Final[str] = "compute::ComputeReduction"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            @staticmethod
            def auto(greycat: GreyCat) -> algebra.compute.ComputeReduction:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[62]
                return t.enum_values[t.generated_offsets[0]]

            @staticmethod
            def none(greycat: GreyCat) -> algebra.compute.ComputeReduction:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[62]
                return t.enum_values[t.generated_offsets[1]]

            @staticmethod
            def sum(greycat: GreyCat) -> algebra.compute.ComputeReduction:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[62]
                return t.enum_values[t.generated_offsets[2]]

            @staticmethod
            def mean(greycat: GreyCat) -> algebra.compute.ComputeReduction:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[62]
                return t.enum_values[t.generated_offsets[3]]

            @staticmethod
            def disabled(greycat: GreyCat) -> algebra.compute.ComputeReduction:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[62]
                return t.enum_values[t.generated_offsets[4]]

            @staticmethod
            def create(greycat: GreyCat) -> algebra.compute.ComputeReduction:
                return algebra.compute.ComputeReduction(greycat.libs_by_name[algebra.name_].mapped[62], [])

        @final
        class ComputeLayerDense(GreyCat.Object):
            name_: Final[str] = "compute::ComputeLayerDense"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def name(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_name(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def type(self) -> std.core.TensorType:
                return self._get(self.type_.generated_offsets[1])

            def set_type(self, v: std.core.TensorType) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def inputs(self) -> int:
                return self._get(self.type_.generated_offsets[2])

            def set_inputs(self, v: int) -> None:
                self._set(self.type_.generated_offsets[2], v)

            def outputs(self) -> int:
                return self._get(self.type_.generated_offsets[3])

            def set_outputs(self, v: int) -> None:
                self._set(self.type_.generated_offsets[3], v)

            def use_bias(self) -> bool:
                return self._get(self.type_.generated_offsets[4])

            def set_use_bias(self, v: bool) -> None:
                self._set(self.type_.generated_offsets[4], v)

            def weight_initializer(self) -> algebra.compute.ComputeInitializer:
                return self._get(self.type_.generated_offsets[5])

            def set_weight_initializer(self, v: algebra.compute.ComputeInitializer) -> None:
                self._set(self.type_.generated_offsets[5], v)

            def weight_regularizer(self) -> algebra.compute.ComputeRegularizer:
                return self._get(self.type_.generated_offsets[6])

            def set_weight_regularizer(self, v: algebra.compute.ComputeRegularizer) -> None:
                self._set(self.type_.generated_offsets[6], v)

            def bias_initializer(self) -> algebra.compute.ComputeInitializer:
                return self._get(self.type_.generated_offsets[7])

            def set_bias_initializer(self, v: algebra.compute.ComputeInitializer) -> None:
                self._set(self.type_.generated_offsets[7], v)

            def bias_regularizer(self) -> algebra.compute.ComputeRegularizer:
                return self._get(self.type_.generated_offsets[8])

            def set_bias_regularizer(self, v: algebra.compute.ComputeRegularizer) -> None:
                self._set(self.type_.generated_offsets[8], v)

            def activation(self) -> algebra.compute.ComputeActivation:
                return self._get(self.type_.generated_offsets[9])

            def set_activation(self, v: algebra.compute.ComputeActivation) -> None:
                self._set(self.type_.generated_offsets[9], v)

            @staticmethod
            def var_input_name(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[63]
                return t.static_values[0]

            @staticmethod
            def var_output_name(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[63]
                return t.static_values[1]

            @staticmethod
            def var_weight_name(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[63]
                return t.static_values[2]

            @staticmethod
            def var_bias_name(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[63]
                return t.static_values[3]

            @staticmethod
            def var_mult_name(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[63]
                return t.static_values[4]

            @staticmethod
            def var_pre_activation_name(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[63]
                return t.static_values[5]

            @staticmethod
            def create(greycat: GreyCat, name: str, type: std.core.TensorType, inputs: int, outputs: int, use_bias: bool, weight_initializer: algebra.compute.ComputeInitializer, weight_regularizer: algebra.compute.ComputeRegularizer, bias_initializer: algebra.compute.ComputeInitializer, bias_regularizer: algebra.compute.ComputeRegularizer, activation: algebra.compute.ComputeActivation) -> algebra.compute.ComputeLayerDense:
                return algebra.compute.ComputeLayerDense(greycat.libs_by_name[algebra.name_].mapped[63], [name, type, inputs, outputs, use_bias, weight_initializer, weight_regularizer, bias_initializer, bias_regularizer, activation])

        @final
        class ComputeOperationSinh(GreyCat.Object):
            name_: Final[str] = "compute::ComputeOperationSinh"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def input(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_input(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def output(self) -> str:
                return self._get(self.type_.generated_offsets[1])

            def set_output(self, v: str) -> None:
                self._set(self.type_.generated_offsets[1], v)

            @staticmethod
            def create(greycat: GreyCat, input: str, output: str) -> algebra.compute.ComputeOperationSinh:
                return algebra.compute.ComputeOperationSinh(greycat.libs_by_name[algebra.name_].mapped[64], [input, output])

        @final
        class ComputeInitializerXavier(GreyCat.Object):
            name_: Final[str] = "compute::ComputeInitializerXavier"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            @staticmethod
            def create(greycat: GreyCat) -> algebra.compute.ComputeInitializerXavier:
                return algebra.compute.ComputeInitializerXavier(greycat.libs_by_name[algebra.name_].mapped[65], [])

        @final
        class ComputeOperationLeakyRelu(GreyCat.Object):
            name_: Final[str] = "compute::ComputeOperationLeakyRelu"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def input(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_input(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def output(self) -> str:
                return self._get(self.type_.generated_offsets[1])

            def set_output(self, v: str) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def alpha(self) -> float:
                return self._get(self.type_.generated_offsets[2])

            def set_alpha(self, v: float) -> None:
                self._set(self.type_.generated_offsets[2], v)

            def max_value(self) -> float:
                return self._get(self.type_.generated_offsets[3])

            def set_max_value(self, v: float) -> None:
                self._set(self.type_.generated_offsets[3], v)

            def threshold(self) -> float:
                return self._get(self.type_.generated_offsets[4])

            def set_threshold(self, v: float) -> None:
                self._set(self.type_.generated_offsets[4], v)

            @staticmethod
            def alpha_def(greycat: GreyCat) -> float:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[66]
                return t.static_values[0]

            @staticmethod
            def max_value_def(greycat: GreyCat) -> float:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[66]
                return t.static_values[1]

            @staticmethod
            def threshold_def(greycat: GreyCat) -> float:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[66]
                return t.static_values[2]

            @staticmethod
            def create(greycat: GreyCat, input: str, output: str, alpha: float, max_value: float, threshold: float) -> algebra.compute.ComputeOperationLeakyRelu:
                return algebra.compute.ComputeOperationLeakyRelu(greycat.libs_by_name[algebra.name_].mapped[66], [input, output, alpha, max_value, threshold])

        @final
        class ComputeOperationDiv(GreyCat.Object):
            name_: Final[str] = "compute::ComputeOperationDiv"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def input(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_input(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def input2(self) -> str:
                return self._get(self.type_.generated_offsets[1])

            def set_input2(self, v: str) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def output(self) -> str:
                return self._get(self.type_.generated_offsets[2])

            def set_output(self, v: str) -> None:
                self._set(self.type_.generated_offsets[2], v)

            @staticmethod
            def create(greycat: GreyCat, input: str, input2: str, output: str) -> algebra.compute.ComputeOperationDiv:
                return algebra.compute.ComputeOperationDiv(greycat.libs_by_name[algebra.name_].mapped[67], [input, input2, output])

        @final
        class ComputeOperationSub(GreyCat.Object):
            name_: Final[str] = "compute::ComputeOperationSub"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def input(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_input(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def input2(self) -> str:
                return self._get(self.type_.generated_offsets[1])

            def set_input2(self, v: str) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def output(self) -> str:
                return self._get(self.type_.generated_offsets[2])

            def set_output(self, v: str) -> None:
                self._set(self.type_.generated_offsets[2], v)

            @staticmethod
            def create(greycat: GreyCat, input: str, input2: str, output: str) -> algebra.compute.ComputeOperationSub:
                return algebra.compute.ComputeOperationSub(greycat.libs_by_name[algebra.name_].mapped[68], [input, input2, output])

        @final
        class ComputeInitializerConstant(GreyCat.Object):
            name_: Final[str] = "compute::ComputeInitializerConstant"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def value(self) -> Any:
                return self._get(self.type_.generated_offsets[0])

            def set_value(self, v: Any) -> None:
                self._set(self.type_.generated_offsets[0], v)

            @staticmethod
            def create(greycat: GreyCat, value: Any) -> algebra.compute.ComputeInitializerConstant:
                return algebra.compute.ComputeInitializerConstant(greycat.libs_by_name[algebra.name_].mapped[69], [value])

        @final
        class ComputeOperationAsinh(GreyCat.Object):
            name_: Final[str] = "compute::ComputeOperationAsinh"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def input(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_input(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def output(self) -> str:
                return self._get(self.type_.generated_offsets[1])

            def set_output(self, v: str) -> None:
                self._set(self.type_.generated_offsets[1], v)

            @staticmethod
            def create(greycat: GreyCat, input: str, output: str) -> algebra.compute.ComputeOperationAsinh:
                return algebra.compute.ComputeOperationAsinh(greycat.libs_by_name[algebra.name_].mapped[70], [input, output])

        @final
        class ComputeState(algebra_n.compute._ComputeState):
            name_: Final[str] = "compute::ComputeState"

            def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
                super().__init__(type)

            @staticmethod
            def create(greycat: GreyCat) -> algebra_n.compute._ComputeState:
                return algebra.compute.ComputeState(greycat.libs_by_name[algebra.name_].mapped[71], [])

        @final
        class ComputeOperationAbs(GreyCat.Object):
            name_: Final[str] = "compute::ComputeOperationAbs"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def input(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_input(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def output(self) -> str:
                return self._get(self.type_.generated_offsets[1])

            def set_output(self, v: str) -> None:
                self._set(self.type_.generated_offsets[1], v)

            @staticmethod
            def create(greycat: GreyCat, input: str, output: str) -> algebra.compute.ComputeOperationAbs:
                return algebra.compute.ComputeOperationAbs(greycat.libs_by_name[algebra.name_].mapped[72], [input, output])

        @final
        class ComputeRegularizer(GreyCat.Object):
            name_: Final[str] = "compute::ComputeRegularizer"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def l1(self) -> float:
                return self._get(self.type_.generated_offsets[0])

            def set_l1(self, v: float) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def l2(self) -> float:
                return self._get(self.type_.generated_offsets[1])

            def set_l2(self, v: float) -> None:
                self._set(self.type_.generated_offsets[1], v)

            @staticmethod
            def create(greycat: GreyCat, l1: float, l2: float) -> algebra.compute.ComputeRegularizer:
                return algebra.compute.ComputeRegularizer(greycat.libs_by_name[algebra.name_].mapped[73], [l1, l2])

        @final
        class ComputeOperationCos(GreyCat.Object):
            name_: Final[str] = "compute::ComputeOperationCos"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def input(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_input(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def output(self) -> str:
                return self._get(self.type_.generated_offsets[1])

            def set_output(self, v: str) -> None:
                self._set(self.type_.generated_offsets[1], v)

            @staticmethod
            def create(greycat: GreyCat, input: str, output: str) -> algebra.compute.ComputeOperationCos:
                return algebra.compute.ComputeOperationCos(greycat.libs_by_name[algebra.name_].mapped[74], [input, output])

        @final
        class ComputeOperationScale(GreyCat.Object):
            name_: Final[str] = "compute::ComputeOperationScale"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def input(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_input(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def output(self) -> str:
                return self._get(self.type_.generated_offsets[1])

            def set_output(self, v: str) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def alpha(self) -> float:
                return self._get(self.type_.generated_offsets[2])

            def set_alpha(self, v: float) -> None:
                self._set(self.type_.generated_offsets[2], v)

            @staticmethod
            def create(greycat: GreyCat, input: str, output: str, alpha: float) -> algebra.compute.ComputeOperationScale:
                return algebra.compute.ComputeOperationScale(greycat.libs_by_name[algebra.name_].mapped[75], [input, output, alpha])

        @final
        class ComputeActivationCelu(GreyCat.Object):
            name_: Final[str] = "compute::ComputeActivationCelu"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def alpha(self) -> float:
                return self._get(self.type_.generated_offsets[0])

            def set_alpha(self, v: float) -> None:
                self._set(self.type_.generated_offsets[0], v)

            @staticmethod
            def alpha_def(greycat: GreyCat) -> float:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[76]
                return t.static_values[0]

            @staticmethod
            def create(greycat: GreyCat, alpha: float) -> algebra.compute.ComputeActivationCelu:
                return algebra.compute.ComputeActivationCelu(greycat.libs_by_name[algebra.name_].mapped[76], [alpha])

        @final
        class ComputeActivation(GreyCat.Object):
            name_: Final[str] = "compute::ComputeActivation"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            @staticmethod
            def create(greycat: GreyCat) -> algebra.compute.ComputeActivation:
                return algebra.compute.ComputeActivation(greycat.libs_by_name[algebra.name_].mapped[77], [])

        @final
        class ComputeOperationCelu(GreyCat.Object):
            name_: Final[str] = "compute::ComputeOperationCelu"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def input(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_input(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def output(self) -> str:
                return self._get(self.type_.generated_offsets[1])

            def set_output(self, v: str) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def alpha(self) -> float:
                return self._get(self.type_.generated_offsets[2])

            def set_alpha(self, v: float) -> None:
                self._set(self.type_.generated_offsets[2], v)

            @staticmethod
            def alpha_def(greycat: GreyCat) -> float:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[78]
                return t.static_values[0]

            @staticmethod
            def create(greycat: GreyCat, input: str, output: str, alpha: float) -> algebra.compute.ComputeOperationCelu:
                return algebra.compute.ComputeOperationCelu(greycat.libs_by_name[algebra.name_].mapped[78], [input, output, alpha])

        @final
        class ComputeOptimizerAdaGrad(GreyCat.Object):
            name_: Final[str] = "compute::ComputeOptimizerAdaGrad"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def learning_rate(self) -> float:
                return self._get(self.type_.generated_offsets[0])

            def set_learning_rate(self, v: float) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def initial_accumulator(self) -> float:
                return self._get(self.type_.generated_offsets[1])

            def set_initial_accumulator(self, v: float) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def smooth_epsilon(self) -> float:
                return self._get(self.type_.generated_offsets[2])

            def set_smooth_epsilon(self, v: float) -> None:
                self._set(self.type_.generated_offsets[2], v)

            @staticmethod
            def learning_rate_def(greycat: GreyCat) -> float:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[79]
                return t.static_values[0]

            @staticmethod
            def initial_accumulator_def(greycat: GreyCat) -> float:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[79]
                return t.static_values[1]

            @staticmethod
            def smooth_epsilon_def(greycat: GreyCat) -> float:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[79]
                return t.static_values[2]

            @staticmethod
            def create(greycat: GreyCat, learning_rate: float, initial_accumulator: float, smooth_epsilon: float) -> algebra.compute.ComputeOptimizerAdaGrad:
                return algebra.compute.ComputeOptimizerAdaGrad(greycat.libs_by_name[algebra.name_].mapped[79], [learning_rate, initial_accumulator, smooth_epsilon])

        @final
        class ComputeOperationTanh(GreyCat.Object):
            name_: Final[str] = "compute::ComputeOperationTanh"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def input(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_input(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def output(self) -> str:
                return self._get(self.type_.generated_offsets[1])

            def set_output(self, v: str) -> None:
                self._set(self.type_.generated_offsets[1], v)

            @staticmethod
            def create(greycat: GreyCat, input: str, output: str) -> algebra.compute.ComputeOperationTanh:
                return algebra.compute.ComputeOperationTanh(greycat.libs_by_name[algebra.name_].mapped[80], [input, output])

        @final
        class ComputeVariable(GreyCat.Object):
            name_: Final[str] = "compute::ComputeVariable"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def name(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_name(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            @staticmethod
            def create(greycat: GreyCat, name: str) -> algebra.compute.ComputeVariable:
                return algebra.compute.ComputeVariable(greycat.libs_by_name[algebra.name_].mapped[81], [name])

        @final
        class ComputeActivationTanh(GreyCat.Object):
            name_: Final[str] = "compute::ComputeActivationTanh"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            @staticmethod
            def create(greycat: GreyCat) -> algebra.compute.ComputeActivationTanh:
                return algebra.compute.ComputeActivationTanh(greycat.libs_by_name[algebra.name_].mapped[82], [])

        @final
        class ComputeOperation2In1Out(GreyCat.Object):
            name_: Final[str] = "compute::ComputeOperation2In1Out"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def input(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_input(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def input2(self) -> str:
                return self._get(self.type_.generated_offsets[1])

            def set_input2(self, v: str) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def output(self) -> str:
                return self._get(self.type_.generated_offsets[2])

            def set_output(self, v: str) -> None:
                self._set(self.type_.generated_offsets[2], v)

            @staticmethod
            def create(greycat: GreyCat, input: str, input2: str, output: str) -> algebra.compute.ComputeOperation2In1Out:
                return algebra.compute.ComputeOperation2In1Out(greycat.libs_by_name[algebra.name_].mapped[83], [input, input2, output])

        @final
        class ComputeOperationSumIf(GreyCat.Object):
            name_: Final[str] = "compute::ComputeOperationSumIf"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def input(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_input(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def ifCondition(self) -> str:
                return self._get(self.type_.generated_offsets[1])

            def set_ifCondition(self, v: str) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def output(self) -> str:
                return self._get(self.type_.generated_offsets[2])

            def set_output(self, v: str) -> None:
                self._set(self.type_.generated_offsets[2], v)

            def counts(self) -> str:
                return self._get(self.type_.generated_offsets[3])

            def set_counts(self, v: str) -> None:
                self._set(self.type_.generated_offsets[3], v)

            def classes(self) -> int:
                return self._get(self.type_.generated_offsets[4])

            def set_classes(self, v: int) -> None:
                self._set(self.type_.generated_offsets[4], v)

            @staticmethod
            def create(greycat: GreyCat, input: str, ifCondition: str, output: str, counts: str, classes: int) -> algebra.compute.ComputeOperationSumIf:
                return algebra.compute.ComputeOperationSumIf(greycat.libs_by_name[algebra.name_].mapped[84], [input, ifCondition, output, counts, classes])

        @final
        class ComputeOperation1In1Out(GreyCat.Object):
            name_: Final[str] = "compute::ComputeOperation1In1Out"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def input(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_input(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def output(self) -> str:
                return self._get(self.type_.generated_offsets[1])

            def set_output(self, v: str) -> None:
                self._set(self.type_.generated_offsets[1], v)

            @staticmethod
            def create(greycat: GreyCat, input: str, output: str) -> algebra.compute.ComputeOperation1In1Out:
                return algebra.compute.ComputeOperation1In1Out(greycat.libs_by_name[algebra.name_].mapped[85], [input, output])

        @final
        class ComputeOptimizerAdam(GreyCat.Object):
            name_: Final[str] = "compute::ComputeOptimizerAdam"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def learning_rate(self) -> float:
                return self._get(self.type_.generated_offsets[0])

            def set_learning_rate(self, v: float) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def beta1(self) -> float:
                return self._get(self.type_.generated_offsets[1])

            def set_beta1(self, v: float) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def beta2(self) -> float:
                return self._get(self.type_.generated_offsets[2])

            def set_beta2(self, v: float) -> None:
                self._set(self.type_.generated_offsets[2], v)

            def smooth_epsilon(self) -> float:
                return self._get(self.type_.generated_offsets[3])

            def set_smooth_epsilon(self, v: float) -> None:
                self._set(self.type_.generated_offsets[3], v)

            @staticmethod
            def learning_rate_def(greycat: GreyCat) -> float:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[86]
                return t.static_values[0]

            @staticmethod
            def beta1_def(greycat: GreyCat) -> float:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[86]
                return t.static_values[1]

            @staticmethod
            def beta2_def(greycat: GreyCat) -> float:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[86]
                return t.static_values[2]

            @staticmethod
            def smooth_epsilon_def(greycat: GreyCat) -> float:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[86]
                return t.static_values[3]

            @staticmethod
            def create(greycat: GreyCat, learning_rate: float, beta1: float, beta2: float, smooth_epsilon: float) -> algebra.compute.ComputeOptimizerAdam:
                return algebra.compute.ComputeOptimizerAdam(greycat.libs_by_name[algebra.name_].mapped[86], [learning_rate, beta1, beta2, smooth_epsilon])

        @final
        class ComputeVarOptimize(GreyCat.Object):
            name_: Final[str] = "compute::ComputeVarOptimize"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def name(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_name(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def type(self) -> std.core.TensorType:
                return self._get(self.type_.generated_offsets[1])

            def set_type(self, v: std.core.TensorType) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def shape(self) -> std.core.Array:
                return self._get(self.type_.generated_offsets[2])

            def set_shape(self, v: std.core.Array) -> None:
                self._set(self.type_.generated_offsets[2], v)

            def l1(self) -> float:
                return self._get(self.type_.generated_offsets[3])

            def set_l1(self, v: float) -> None:
                self._set(self.type_.generated_offsets[3], v)

            def l2(self) -> float:
                return self._get(self.type_.generated_offsets[4])

            def set_l2(self, v: float) -> None:
                self._set(self.type_.generated_offsets[4], v)

            def init(self) -> algebra.compute.ComputeInitializer:
                return self._get(self.type_.generated_offsets[5])

            def set_init(self, v: algebra.compute.ComputeInitializer) -> None:
                self._set(self.type_.generated_offsets[5], v)

            @staticmethod
            def create(greycat: GreyCat, name: str, type: std.core.TensorType, shape: std.core.Array, l1: float, l2: float, init: algebra.compute.ComputeInitializer) -> algebra.compute.ComputeVarOptimize:
                return algebra.compute.ComputeVarOptimize(greycat.libs_by_name[algebra.name_].mapped[87], [name, type, shape, l1, l2, init])

        @final
        class ComputeOperationSoftplus(GreyCat.Object):
            name_: Final[str] = "compute::ComputeOperationSoftplus"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def input(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_input(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def output(self) -> str:
                return self._get(self.type_.generated_offsets[1])

            def set_output(self, v: str) -> None:
                self._set(self.type_.generated_offsets[1], v)

            @staticmethod
            def create(greycat: GreyCat, input: str, output: str) -> algebra.compute.ComputeOperationSoftplus:
                return algebra.compute.ComputeOperationSoftplus(greycat.libs_by_name[algebra.name_].mapped[88], [input, output])

        @final
        class ComputeActivationSoftmax(GreyCat.Object):
            name_: Final[str] = "compute::ComputeActivationSoftmax"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def classes(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_classes(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            @staticmethod
            def create(greycat: GreyCat, classes: str) -> algebra.compute.ComputeActivationSoftmax:
                return algebra.compute.ComputeActivationSoftmax(greycat.libs_by_name[algebra.name_].mapped[89], [classes])

        @final
        class ComputeOperationLogSoftmax(GreyCat.Object):
            name_: Final[str] = "compute::ComputeOperationLogSoftmax"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def input(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_input(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def output(self) -> str:
                return self._get(self.type_.generated_offsets[1])

            def set_output(self, v: str) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def axis(self) -> int:
                return self._get(self.type_.generated_offsets[2])

            def set_axis(self, v: int) -> None:
                self._set(self.type_.generated_offsets[2], v)

            @staticmethod
            def create(greycat: GreyCat, input: str, output: str, axis: int) -> algebra.compute.ComputeOperationLogSoftmax:
                return algebra.compute.ComputeOperationLogSoftmax(greycat.libs_by_name[algebra.name_].mapped[90], [input, output, axis])

        @final
        class ComputeLayerLossRegression(GreyCat.Object):
            name_: Final[str] = "compute::ComputeLayerLossRegression"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def name(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_name(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def reduction(self) -> algebra.compute.ComputeReduction:
                return self._get(self.type_.generated_offsets[1])

            def set_reduction(self, v: algebra.compute.ComputeReduction) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def loss_type(self) -> algebra.compute.ComputeRegressionLoss:
                return self._get(self.type_.generated_offsets[2])

            def set_loss_type(self, v: algebra.compute.ComputeRegressionLoss) -> None:
                self._set(self.type_.generated_offsets[2], v)

            @staticmethod
            def create(greycat: GreyCat, name: str, reduction: algebra.compute.ComputeReduction, loss_type: algebra.compute.ComputeRegressionLoss) -> algebra.compute.ComputeLayerLossRegression:
                return algebra.compute.ComputeLayerLossRegression(greycat.libs_by_name[algebra.name_].mapped[91], [name, reduction, loss_type])

        @final
        class ComputeActivationSoftSign(GreyCat.Object):
            name_: Final[str] = "compute::ComputeActivationSoftSign"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            @staticmethod
            def create(greycat: GreyCat) -> algebra.compute.ComputeActivationSoftSign:
                return algebra.compute.ComputeActivationSoftSign(greycat.libs_by_name[algebra.name_].mapped[92], [])

        @final
        class ComputeOperationSigmoid(GreyCat.Object):
            name_: Final[str] = "compute::ComputeOperationSigmoid"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def input(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_input(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def output(self) -> str:
                return self._get(self.type_.generated_offsets[1])

            def set_output(self, v: str) -> None:
                self._set(self.type_.generated_offsets[1], v)

            @staticmethod
            def create(greycat: GreyCat, input: str, output: str) -> algebra.compute.ComputeOperationSigmoid:
                return algebra.compute.ComputeOperationSigmoid(greycat.libs_by_name[algebra.name_].mapped[93], [input, output])

        @final
        class ComputeOperationPow(GreyCat.Object):
            name_: Final[str] = "compute::ComputeOperationPow"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def input(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_input(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def input2(self) -> str:
                return self._get(self.type_.generated_offsets[1])

            def set_input2(self, v: str) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def output(self) -> str:
                return self._get(self.type_.generated_offsets[2])

            def set_output(self, v: str) -> None:
                self._set(self.type_.generated_offsets[2], v)

            @staticmethod
            def create(greycat: GreyCat, input: str, input2: str, output: str) -> algebra.compute.ComputeOperationPow:
                return algebra.compute.ComputeOperationPow(greycat.libs_by_name[algebra.name_].mapped[94], [input, input2, output])

        @final
        class ComputeOperationRaiseToPower(GreyCat.Object):
            name_: Final[str] = "compute::ComputeOperationRaiseToPower"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def input(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_input(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def output(self) -> str:
                return self._get(self.type_.generated_offsets[1])

            def set_output(self, v: str) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def power(self) -> float:
                return self._get(self.type_.generated_offsets[2])

            def set_power(self, v: float) -> None:
                self._set(self.type_.generated_offsets[2], v)

            @staticmethod
            def create(greycat: GreyCat, input: str, output: str, power: float) -> algebra.compute.ComputeOperationRaiseToPower:
                return algebra.compute.ComputeOperationRaiseToPower(greycat.libs_by_name[algebra.name_].mapped[95], [input, output, power])

        @final
        class ComputeOptimizerNesterov(GreyCat.Object):
            name_: Final[str] = "compute::ComputeOptimizerNesterov"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def learning_rate(self) -> float:
                return self._get(self.type_.generated_offsets[0])

            def set_learning_rate(self, v: float) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def decay_rate(self) -> float:
                return self._get(self.type_.generated_offsets[1])

            def set_decay_rate(self, v: float) -> None:
                self._set(self.type_.generated_offsets[1], v)

            @staticmethod
            def learning_rate_def(greycat: GreyCat) -> float:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[96]
                return t.static_values[0]

            @staticmethod
            def decay_rate_def(greycat: GreyCat) -> float:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[96]
                return t.static_values[1]

            @staticmethod
            def create(greycat: GreyCat, learning_rate: float, decay_rate: float) -> algebra.compute.ComputeOptimizerNesterov:
                return algebra.compute.ComputeOptimizerNesterov(greycat.libs_by_name[algebra.name_].mapped[96], [learning_rate, decay_rate])

        @final
        class ComputeLayerConfusion(GreyCat.Object):
            name_: Final[str] = "compute::ComputeLayerConfusion"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def name(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_name(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def nbClass(self) -> int:
                return self._get(self.type_.generated_offsets[1])

            def set_nbClass(self, v: int) -> None:
                self._set(self.type_.generated_offsets[1], v)

            @staticmethod
            def var_computed_name(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[97]
                return t.static_values[0]

            @staticmethod
            def var_expected_name(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[97]
                return t.static_values[1]

            @staticmethod
            def var_confusion_name(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[97]
                return t.static_values[2]

            @staticmethod
            def create(greycat: GreyCat, name: str, nbClass: int) -> algebra.compute.ComputeLayerConfusion:
                return algebra.compute.ComputeLayerConfusion(greycat.libs_by_name[algebra.name_].mapped[97], [name, nbClass])

        @final
        class ComputeLayerCustom(GreyCat.Object):
            name_: Final[str] = "compute::ComputeLayerCustom"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def name(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_name(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def ops(self) -> std.core.Array:
                return self._get(self.type_.generated_offsets[1])

            def set_ops(self, v: std.core.Array) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def vars(self) -> std.core.Array:
                return self._get(self.type_.generated_offsets[2])

            def set_vars(self, v: std.core.Array) -> None:
                self._set(self.type_.generated_offsets[2], v)

            @staticmethod
            def create(greycat: GreyCat, name: str, ops: std.core.Array, vars: std.core.Array) -> algebra.compute.ComputeLayerCustom:
                return algebra.compute.ComputeLayerCustom(greycat.libs_by_name[algebra.name_].mapped[98], [name, ops, vars])

        @final
        class ComputeOperationClip(GreyCat.Object):
            name_: Final[str] = "compute::ComputeOperationClip"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def input(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_input(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def output(self) -> str:
                return self._get(self.type_.generated_offsets[1])

            def set_output(self, v: str) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def min(self) -> float:
                return self._get(self.type_.generated_offsets[2])

            def set_min(self, v: float) -> None:
                self._set(self.type_.generated_offsets[2], v)

            def max(self) -> float:
                return self._get(self.type_.generated_offsets[3])

            def set_max(self, v: float) -> None:
                self._set(self.type_.generated_offsets[3], v)

            @staticmethod
            def create(greycat: GreyCat, input: str, output: str, min: float, max: float) -> algebra.compute.ComputeOperationClip:
                return algebra.compute.ComputeOperationClip(greycat.libs_by_name[algebra.name_].mapped[99], [input, output, min, max])

        @final
        class ComputeModel(GreyCat.Object):
            name_: Final[str] = "compute::ComputeModel"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def layers(self) -> std.core.Array:
                return self._get(self.type_.generated_offsets[0])

            def set_layers(self, v: std.core.Array) -> None:
                self._set(self.type_.generated_offsets[0], v)

            @staticmethod
            def create(greycat: GreyCat, layers: std.core.Array) -> algebra.compute.ComputeModel:
                return algebra.compute.ComputeModel(greycat.libs_by_name[algebra.name_].mapped[100], [layers])

        @final
        class ComputeLayerLinear(GreyCat.Object):
            name_: Final[str] = "compute::ComputeLayerLinear"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def name(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_name(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def type(self) -> std.core.TensorType:
                return self._get(self.type_.generated_offsets[1])

            def set_type(self, v: std.core.TensorType) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def inputs(self) -> int:
                return self._get(self.type_.generated_offsets[2])

            def set_inputs(self, v: int) -> None:
                self._set(self.type_.generated_offsets[2], v)

            def outputs(self) -> int:
                return self._get(self.type_.generated_offsets[3])

            def set_outputs(self, v: int) -> None:
                self._set(self.type_.generated_offsets[3], v)

            def use_bias(self) -> bool:
                return self._get(self.type_.generated_offsets[4])

            def set_use_bias(self, v: bool) -> None:
                self._set(self.type_.generated_offsets[4], v)

            def weight_initializer(self) -> algebra.compute.ComputeInitializer:
                return self._get(self.type_.generated_offsets[5])

            def set_weight_initializer(self, v: algebra.compute.ComputeInitializer) -> None:
                self._set(self.type_.generated_offsets[5], v)

            def weight_regularizer(self) -> algebra.compute.ComputeRegularizer:
                return self._get(self.type_.generated_offsets[6])

            def set_weight_regularizer(self, v: algebra.compute.ComputeRegularizer) -> None:
                self._set(self.type_.generated_offsets[6], v)

            def bias_initializer(self) -> algebra.compute.ComputeInitializer:
                return self._get(self.type_.generated_offsets[7])

            def set_bias_initializer(self, v: algebra.compute.ComputeInitializer) -> None:
                self._set(self.type_.generated_offsets[7], v)

            def bias_regularizer(self) -> algebra.compute.ComputeRegularizer:
                return self._get(self.type_.generated_offsets[8])

            def set_bias_regularizer(self, v: algebra.compute.ComputeRegularizer) -> None:
                self._set(self.type_.generated_offsets[8], v)

            @staticmethod
            def var_input_name(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[101]
                return t.static_values[0]

            @staticmethod
            def var_output_name(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[101]
                return t.static_values[1]

            @staticmethod
            def var_weight_name(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[101]
                return t.static_values[2]

            @staticmethod
            def var_bias_name(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[101]
                return t.static_values[3]

            @staticmethod
            def var_mult_name(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[101]
                return t.static_values[4]

            @staticmethod
            def create(greycat: GreyCat, name: str, type: std.core.TensorType, inputs: int, outputs: int, use_bias: bool, weight_initializer: algebra.compute.ComputeInitializer, weight_regularizer: algebra.compute.ComputeRegularizer, bias_initializer: algebra.compute.ComputeInitializer, bias_regularizer: algebra.compute.ComputeRegularizer) -> algebra.compute.ComputeLayerLinear:
                return algebra.compute.ComputeLayerLinear(greycat.libs_by_name[algebra.name_].mapped[101], [name, type, inputs, outputs, use_bias, weight_initializer, weight_regularizer, bias_initializer, bias_regularizer])

        @final
        class ComputeOperationArgMax(GreyCat.Object):
            name_: Final[str] = "compute::ComputeOperationArgMax"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def input(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_input(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def output(self) -> str:
                return self._get(self.type_.generated_offsets[1])

            def set_output(self, v: str) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def output2(self) -> str:
                return self._get(self.type_.generated_offsets[2])

            def set_output2(self, v: str) -> None:
                self._set(self.type_.generated_offsets[2], v)

            @staticmethod
            def create(greycat: GreyCat, input: str, output: str, output2: str) -> algebra.compute.ComputeOperationArgMax:
                return algebra.compute.ComputeOperationArgMax(greycat.libs_by_name[algebra.name_].mapped[102], [input, output, output2])

        @final
        class ComputeOperationRelu(GreyCat.Object):
            name_: Final[str] = "compute::ComputeOperationRelu"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def input(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_input(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def output(self) -> str:
                return self._get(self.type_.generated_offsets[1])

            def set_output(self, v: str) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def max_value(self) -> float:
                return self._get(self.type_.generated_offsets[2])

            def set_max_value(self, v: float) -> None:
                self._set(self.type_.generated_offsets[2], v)

            def threshold(self) -> float:
                return self._get(self.type_.generated_offsets[3])

            def set_threshold(self, v: float) -> None:
                self._set(self.type_.generated_offsets[3], v)

            @staticmethod
            def threshold_def(greycat: GreyCat) -> float:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[103]
                return t.static_values[0]

            @staticmethod
            def create(greycat: GreyCat, input: str, output: str, max_value: float, threshold: float) -> algebra.compute.ComputeOperationRelu:
                return algebra.compute.ComputeOperationRelu(greycat.libs_by_name[algebra.name_].mapped[103], [input, output, max_value, threshold])

        @final
        class ComputeLayerStandardScaler(GreyCat.Object):
            name_: Final[str] = "compute::ComputeLayerStandardScaler"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def name(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_name(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def type(self) -> std.core.TensorType:
                return self._get(self.type_.generated_offsets[1])

            def set_type(self, v: std.core.TensorType) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def inverse_transform(self) -> bool:
                return self._get(self.type_.generated_offsets[2])

            def set_inverse_transform(self, v: bool) -> None:
                self._set(self.type_.generated_offsets[2], v)

            @staticmethod
            def var_input_name(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[104]
                return t.static_values[0]

            @staticmethod
            def var_output_name(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[104]
                return t.static_values[1]

            @staticmethod
            def var_avg_name(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[104]
                return t.static_values[2]

            @staticmethod
            def var_std_name(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[104]
                return t.static_values[3]

            @staticmethod
            def create(greycat: GreyCat, name: str, type: std.core.TensorType, inverse_transform: bool) -> algebra.compute.ComputeLayerStandardScaler:
                return algebra.compute.ComputeLayerStandardScaler(greycat.libs_by_name[algebra.name_].mapped[104], [name, type, inverse_transform])

        @final
        class ComputeActivationSoftplus(GreyCat.Object):
            name_: Final[str] = "compute::ComputeActivationSoftplus"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            @staticmethod
            def create(greycat: GreyCat) -> algebra.compute.ComputeActivationSoftplus:
                return algebra.compute.ComputeActivationSoftplus(greycat.libs_by_name[algebra.name_].mapped[105], [])

        @final
        class ComputeOptimizerNadam(GreyCat.Object):
            name_: Final[str] = "compute::ComputeOptimizerNadam"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def learning_rate(self) -> float:
                return self._get(self.type_.generated_offsets[0])

            def set_learning_rate(self, v: float) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def beta1(self) -> float:
                return self._get(self.type_.generated_offsets[1])

            def set_beta1(self, v: float) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def beta2(self) -> float:
                return self._get(self.type_.generated_offsets[2])

            def set_beta2(self, v: float) -> None:
                self._set(self.type_.generated_offsets[2], v)

            def smooth_epsilon(self) -> float:
                return self._get(self.type_.generated_offsets[3])

            def set_smooth_epsilon(self, v: float) -> None:
                self._set(self.type_.generated_offsets[3], v)

            @staticmethod
            def learning_rate_def(greycat: GreyCat) -> float:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[106]
                return t.static_values[0]

            @staticmethod
            def beta1_def(greycat: GreyCat) -> float:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[106]
                return t.static_values[1]

            @staticmethod
            def beta2_def(greycat: GreyCat) -> float:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[106]
                return t.static_values[2]

            @staticmethod
            def smooth_epsilon_def(greycat: GreyCat) -> float:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[106]
                return t.static_values[3]

            @staticmethod
            def create(greycat: GreyCat, learning_rate: float, beta1: float, beta2: float, smooth_epsilon: float) -> algebra.compute.ComputeOptimizerNadam:
                return algebra.compute.ComputeOptimizerNadam(greycat.libs_by_name[algebra.name_].mapped[106], [learning_rate, beta1, beta2, smooth_epsilon])

        @final
        class ComputeOperationSqrt(GreyCat.Object):
            name_: Final[str] = "compute::ComputeOperationSqrt"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def input(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_input(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def output(self) -> str:
                return self._get(self.type_.generated_offsets[1])

            def set_output(self, v: str) -> None:
                self._set(self.type_.generated_offsets[1], v)

            @staticmethod
            def create(greycat: GreyCat, input: str, output: str) -> algebra.compute.ComputeOperationSqrt:
                return algebra.compute.ComputeOperationSqrt(greycat.libs_by_name[algebra.name_].mapped[107], [input, output])

        @final
        class ComputeInitializerNormal(GreyCat.Object):
            name_: Final[str] = "compute::ComputeInitializerNormal"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def avg(self) -> float:
                return self._get(self.type_.generated_offsets[0])

            def set_avg(self, v: float) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def std(self) -> float:
                return self._get(self.type_.generated_offsets[1])

            def set_std(self, v: float) -> None:
                self._set(self.type_.generated_offsets[1], v)

            @staticmethod
            def create(greycat: GreyCat, avg: float, std: float) -> algebra.compute.ComputeInitializerNormal:
                return algebra.compute.ComputeInitializerNormal(greycat.libs_by_name[algebra.name_].mapped[108], [avg, std])

        @final
        class ComputeInitializerUniformAvg(GreyCat.Object):
            name_: Final[str] = "compute::ComputeInitializerUniformAvg"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            @staticmethod
            def create(greycat: GreyCat) -> algebra.compute.ComputeInitializerUniformAvg:
                return algebra.compute.ComputeInitializerUniformAvg(greycat.libs_by_name[algebra.name_].mapped[109], [])

        @final
        class ComputeInitializerLeCunUniform(GreyCat.Object):
            name_: Final[str] = "compute::ComputeInitializerLeCunUniform"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            @staticmethod
            def create(greycat: GreyCat) -> algebra.compute.ComputeInitializerLeCunUniform:
                return algebra.compute.ComputeInitializerLeCunUniform(greycat.libs_by_name[algebra.name_].mapped[110], [])

        @final
        class ComputeOperationSoftmax(GreyCat.Object):
            name_: Final[str] = "compute::ComputeOperationSoftmax"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def input(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_input(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def output(self) -> str:
                return self._get(self.type_.generated_offsets[1])

            def set_output(self, v: str) -> None:
                self._set(self.type_.generated_offsets[1], v)

            @staticmethod
            def create(greycat: GreyCat, input: str, output: str) -> algebra.compute.ComputeOperationSoftmax:
                return algebra.compute.ComputeOperationSoftmax(greycat.libs_by_name[algebra.name_].mapped[111], [input, output])

        @final
        class ComputeOperationEuclidean(GreyCat.Object):
            name_: Final[str] = "compute::ComputeOperationEuclidean"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def input(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_input(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def input2(self) -> str:
                return self._get(self.type_.generated_offsets[1])

            def set_input2(self, v: str) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def output(self) -> str:
                return self._get(self.type_.generated_offsets[2])

            def set_output(self, v: str) -> None:
                self._set(self.type_.generated_offsets[2], v)

            @staticmethod
            def create(greycat: GreyCat, input: str, input2: str, output: str) -> algebra.compute.ComputeOperationEuclidean:
                return algebra.compute.ComputeOperationEuclidean(greycat.libs_by_name[algebra.name_].mapped[112], [input, input2, output])

        @final
        class ComputeLayerLossClassification(GreyCat.Object):
            name_: Final[str] = "compute::ComputeLayerLossClassification"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def name(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_name(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def reduction(self) -> algebra.compute.ComputeReduction:
                return self._get(self.type_.generated_offsets[1])

            def set_reduction(self, v: algebra.compute.ComputeReduction) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def loss_type(self) -> algebra.compute.ComputeClassificationLoss:
                return self._get(self.type_.generated_offsets[2])

            def set_loss_type(self, v: algebra.compute.ComputeClassificationLoss) -> None:
                self._set(self.type_.generated_offsets[2], v)

            def has_class_weights(self) -> bool:
                return self._get(self.type_.generated_offsets[3])

            def set_has_class_weights(self, v: bool) -> None:
                self._set(self.type_.generated_offsets[3], v)

            def calculate_probabilities(self) -> bool:
                return self._get(self.type_.generated_offsets[4])

            def set_calculate_probabilities(self, v: bool) -> None:
                self._set(self.type_.generated_offsets[4], v)

            def from_logits(self) -> bool:
                return self._get(self.type_.generated_offsets[5])

            def set_from_logits(self, v: bool) -> None:
                self._set(self.type_.generated_offsets[5], v)

            @staticmethod
            def var_class_weights_name(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[113]
                return t.static_values[0]

            @staticmethod
            def var_predicted_classes_name(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[113]
                return t.static_values[1]

            @staticmethod
            def var_probabilities_name(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[113]
                return t.static_values[2]

            @staticmethod
            def var_sum_reduce_name(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[113]
                return t.static_values[3]

            @staticmethod
            def create(greycat: GreyCat, name: str, reduction: algebra.compute.ComputeReduction, loss_type: algebra.compute.ComputeClassificationLoss, has_class_weights: bool, calculate_probabilities: bool, from_logits: bool) -> algebra.compute.ComputeLayerLossClassification:
                return algebra.compute.ComputeLayerLossClassification(greycat.libs_by_name[algebra.name_].mapped[113], [name, reduction, loss_type, has_class_weights, calculate_probabilities, from_logits])

        @final
        class ComputeOperationCosh(GreyCat.Object):
            name_: Final[str] = "compute::ComputeOperationCosh"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def input(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_input(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def output(self) -> str:
                return self._get(self.type_.generated_offsets[1])

            def set_output(self, v: str) -> None:
                self._set(self.type_.generated_offsets[1], v)

            @staticmethod
            def create(greycat: GreyCat, input: str, output: str) -> algebra.compute.ComputeOperationCosh:
                return algebra.compute.ComputeOperationCosh(greycat.libs_by_name[algebra.name_].mapped[114], [input, output])

        @final
        class ComputeInitializerLSTM(GreyCat.Object):
            name_: Final[str] = "compute::ComputeInitializerLSTM"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            @staticmethod
            def create(greycat: GreyCat) -> algebra.compute.ComputeInitializerLSTM:
                return algebra.compute.ComputeInitializerLSTM(greycat.libs_by_name[algebra.name_].mapped[115], [])

        @final
        class ComputeBinding(GreyCat.Object):
            name_: Final[str] = "compute::ComputeBinding"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def src_layer_name(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_src_layer_name(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def src_var_name(self) -> str:
                return self._get(self.type_.generated_offsets[1])

            def set_src_var_name(self, v: str) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def target_var_name(self) -> str:
                return self._get(self.type_.generated_offsets[2])

            def set_target_var_name(self, v: str) -> None:
                self._set(self.type_.generated_offsets[2], v)

            @staticmethod
            def create(greycat: GreyCat, src_layer_name: str, src_var_name: str, target_var_name: str) -> algebra.compute.ComputeBinding:
                return algebra.compute.ComputeBinding(greycat.libs_by_name[algebra.name_].mapped[116], [src_layer_name, src_var_name, target_var_name])

        @final
        class ComputeInitializerNormalOut(GreyCat.Object):
            name_: Final[str] = "compute::ComputeInitializerNormalOut"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            @staticmethod
            def create(greycat: GreyCat) -> algebra.compute.ComputeInitializerNormalOut:
                return algebra.compute.ComputeInitializerNormalOut(greycat.libs_by_name[algebra.name_].mapped[117], [])

        @final
        class ComputeClassificationLoss(GreyCat.Enum):
            name_: Final[str] = "compute::ComputeClassificationLoss"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            @staticmethod
            def categorical_cross_entropy(greycat: GreyCat) -> algebra.compute.ComputeClassificationLoss:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[118]
                return t.enum_values[t.generated_offsets[0]]

            @staticmethod
            def sparse_categorical_cross_entropy(greycat: GreyCat) -> algebra.compute.ComputeClassificationLoss:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[118]
                return t.enum_values[t.generated_offsets[1]]

            @staticmethod
            def create(greycat: GreyCat) -> algebra.compute.ComputeClassificationLoss:
                return algebra.compute.ComputeClassificationLoss(greycat.libs_by_name[algebra.name_].mapped[118], [])

        @final
        class ComputeOperationArgMin(GreyCat.Object):
            name_: Final[str] = "compute::ComputeOperationArgMin"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def input(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_input(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def output(self) -> str:
                return self._get(self.type_.generated_offsets[1])

            def set_output(self, v: str) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def output2(self) -> str:
                return self._get(self.type_.generated_offsets[2])

            def set_output2(self, v: str) -> None:
                self._set(self.type_.generated_offsets[2], v)

            @staticmethod
            def create(greycat: GreyCat, input: str, output: str, output2: str) -> algebra.compute.ComputeOperationArgMin:
                return algebra.compute.ComputeOperationArgMin(greycat.libs_by_name[algebra.name_].mapped[119], [input, output, output2])

        @final
        class ComputeOperation(GreyCat.Object):
            name_: Final[str] = "compute::ComputeOperation"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            @staticmethod
            def create(greycat: GreyCat) -> algebra.compute.ComputeOperation:
                return algebra.compute.ComputeOperation(greycat.libs_by_name[algebra.name_].mapped[120], [])

        @final
        class ComputeOperationAcosh(GreyCat.Object):
            name_: Final[str] = "compute::ComputeOperationAcosh"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def input(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_input(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def output(self) -> str:
                return self._get(self.type_.generated_offsets[1])

            def set_output(self, v: str) -> None:
                self._set(self.type_.generated_offsets[1], v)

            @staticmethod
            def create(greycat: GreyCat, input: str, output: str) -> algebra.compute.ComputeOperationAcosh:
                return algebra.compute.ComputeOperationAcosh(greycat.libs_by_name[algebra.name_].mapped[121], [input, output])

        @final
        class ComputeOperationAtan(GreyCat.Object):
            name_: Final[str] = "compute::ComputeOperationAtan"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def input(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_input(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def output(self) -> str:
                return self._get(self.type_.generated_offsets[1])

            def set_output(self, v: str) -> None:
                self._set(self.type_.generated_offsets[1], v)

            @staticmethod
            def create(greycat: GreyCat, input: str, output: str) -> algebra.compute.ComputeOperationAtan:
                return algebra.compute.ComputeOperationAtan(greycat.libs_by_name[algebra.name_].mapped[122], [input, output])

        @final
        class ComputeOperationNeg(GreyCat.Object):
            name_: Final[str] = "compute::ComputeOperationNeg"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def input(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_input(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def output(self) -> str:
                return self._get(self.type_.generated_offsets[1])

            def set_output(self, v: str) -> None:
                self._set(self.type_.generated_offsets[1], v)

            @staticmethod
            def create(greycat: GreyCat, input: str, output: str) -> algebra.compute.ComputeOperationNeg:
                return algebra.compute.ComputeOperationNeg(greycat.libs_by_name[algebra.name_].mapped[123], [input, output])

        @final
        class ComputeOperationAdd(GreyCat.Object):
            name_: Final[str] = "compute::ComputeOperationAdd"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def input(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_input(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def input2(self) -> str:
                return self._get(self.type_.generated_offsets[1])

            def set_input2(self, v: str) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def output(self) -> str:
                return self._get(self.type_.generated_offsets[2])

            def set_output(self, v: str) -> None:
                self._set(self.type_.generated_offsets[2], v)

            @staticmethod
            def create(greycat: GreyCat, input: str, input2: str, output: str) -> algebra.compute.ComputeOperationAdd:
                return algebra.compute.ComputeOperationAdd(greycat.libs_by_name[algebra.name_].mapped[124], [input, input2, output])

        @final
        class ComputeInitializerXavierUniform(GreyCat.Object):
            name_: Final[str] = "compute::ComputeInitializerXavierUniform"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            @staticmethod
            def create(greycat: GreyCat) -> algebra.compute.ComputeInitializerXavierUniform:
                return algebra.compute.ComputeInitializerXavierUniform(greycat.libs_by_name[algebra.name_].mapped[125], [])

        @final
        class ComputeLayerClassification(GreyCat.Object):
            name_: Final[str] = "compute::ComputeLayerClassification"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def name(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_name(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def calculate_probabilities(self) -> bool:
                return self._get(self.type_.generated_offsets[1])

            def set_calculate_probabilities(self, v: bool) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def from_logits(self) -> bool:
                return self._get(self.type_.generated_offsets[2])

            def set_from_logits(self, v: bool) -> None:
                self._set(self.type_.generated_offsets[2], v)

            @staticmethod
            def var_input_name(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[126]
                return t.static_values[0]

            @staticmethod
            def var_predicted_classes_name(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[126]
                return t.static_values[1]

            @staticmethod
            def var_probabilities_name(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[126]
                return t.static_values[2]

            @staticmethod
            def create(greycat: GreyCat, name: str, calculate_probabilities: bool, from_logits: bool) -> algebra.compute.ComputeLayerClassification:
                return algebra.compute.ComputeLayerClassification(greycat.libs_by_name[algebra.name_].mapped[126], [name, calculate_probabilities, from_logits])

        @final
        class ComputeLayerSeq(GreyCat.Object):
            name_: Final[str] = "compute::ComputeLayerSeq"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def name(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_name(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def calls(self) -> std.core.Array:
                return self._get(self.type_.generated_offsets[1])

            def set_calls(self, v: std.core.Array) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def optimizer(self) -> algebra.compute.ComputeOptimizer:
                return self._get(self.type_.generated_offsets[2])

            def set_optimizer(self, v: algebra.compute.ComputeOptimizer) -> None:
                self._set(self.type_.generated_offsets[2], v)

            @staticmethod
            def create(greycat: GreyCat, name: str, calls: std.core.Array, optimizer: algebra.compute.ComputeOptimizer) -> algebra.compute.ComputeLayerSeq:
                return algebra.compute.ComputeLayerSeq(greycat.libs_by_name[algebra.name_].mapped[127], [name, calls, optimizer])

        @final
        class ComputeVarInOut(GreyCat.Object):
            name_: Final[str] = "compute::ComputeVarInOut"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def name(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_name(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def type(self) -> std.core.TensorType:
                return self._get(self.type_.generated_offsets[1])

            def set_type(self, v: std.core.TensorType) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def shape(self) -> std.core.Array:
                return self._get(self.type_.generated_offsets[2])

            def set_shape(self, v: std.core.Array) -> None:
                self._set(self.type_.generated_offsets[2], v)

            def with_grad(self) -> bool:
                return self._get(self.type_.generated_offsets[3])

            def set_with_grad(self, v: bool) -> None:
                self._set(self.type_.generated_offsets[3], v)

            @staticmethod
            def create(greycat: GreyCat, name: str, type: std.core.TensorType, shape: std.core.Array, with_grad: bool) -> algebra.compute.ComputeVarInOut:
                return algebra.compute.ComputeVarInOut(greycat.libs_by_name[algebra.name_].mapped[128], [name, type, shape, with_grad])

    @final
    class nn_layers_names:

        @final
        class NNLayersNames(GreyCat.Enum):
            name_: Final[str] = "nn_layers_names::NNLayersNames"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            @staticmethod
            def layer_0(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[0]]

            @staticmethod
            def layer_1(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[1]]

            @staticmethod
            def layer_2(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[2]]

            @staticmethod
            def layer_3(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[3]]

            @staticmethod
            def layer_4(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[4]]

            @staticmethod
            def layer_5(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[5]]

            @staticmethod
            def layer_6(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[6]]

            @staticmethod
            def layer_7(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[7]]

            @staticmethod
            def layer_8(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[8]]

            @staticmethod
            def layer_9(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[9]]

            @staticmethod
            def layer_10(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[10]]

            @staticmethod
            def layer_11(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[11]]

            @staticmethod
            def layer_12(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[12]]

            @staticmethod
            def layer_13(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[13]]

            @staticmethod
            def layer_14(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[14]]

            @staticmethod
            def layer_15(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[15]]

            @staticmethod
            def layer_16(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[16]]

            @staticmethod
            def layer_17(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[17]]

            @staticmethod
            def layer_18(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[18]]

            @staticmethod
            def layer_19(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[19]]

            @staticmethod
            def layer_20(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[20]]

            @staticmethod
            def layer_21(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[21]]

            @staticmethod
            def layer_22(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[22]]

            @staticmethod
            def layer_23(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[23]]

            @staticmethod
            def layer_24(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[24]]

            @staticmethod
            def layer_25(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[25]]

            @staticmethod
            def layer_26(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[26]]

            @staticmethod
            def layer_27(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[27]]

            @staticmethod
            def layer_28(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[28]]

            @staticmethod
            def layer_29(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[29]]

            @staticmethod
            def layer_30(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[30]]

            @staticmethod
            def layer_31(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[31]]

            @staticmethod
            def layer_32(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[32]]

            @staticmethod
            def layer_33(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[33]]

            @staticmethod
            def layer_34(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[34]]

            @staticmethod
            def layer_35(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[35]]

            @staticmethod
            def layer_36(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[36]]

            @staticmethod
            def layer_37(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[37]]

            @staticmethod
            def layer_38(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[38]]

            @staticmethod
            def layer_39(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[39]]

            @staticmethod
            def layer_40(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[40]]

            @staticmethod
            def layer_41(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[41]]

            @staticmethod
            def layer_42(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[42]]

            @staticmethod
            def layer_43(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[43]]

            @staticmethod
            def layer_44(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[44]]

            @staticmethod
            def layer_45(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[45]]

            @staticmethod
            def layer_46(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[46]]

            @staticmethod
            def layer_47(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[47]]

            @staticmethod
            def layer_48(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[48]]

            @staticmethod
            def layer_49(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[49]]

            @staticmethod
            def layer_50(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[50]]

            @staticmethod
            def layer_51(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[51]]

            @staticmethod
            def layer_52(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[52]]

            @staticmethod
            def layer_53(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[53]]

            @staticmethod
            def layer_54(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[54]]

            @staticmethod
            def layer_55(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[55]]

            @staticmethod
            def layer_56(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[56]]

            @staticmethod
            def layer_57(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[57]]

            @staticmethod
            def layer_58(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[58]]

            @staticmethod
            def layer_59(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[59]]

            @staticmethod
            def layer_60(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[60]]

            @staticmethod
            def layer_61(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[61]]

            @staticmethod
            def layer_62(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[62]]

            @staticmethod
            def layer_63(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[63]]

            @staticmethod
            def layer_64(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[64]]

            @staticmethod
            def layer_65(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[65]]

            @staticmethod
            def layer_66(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[66]]

            @staticmethod
            def layer_67(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[67]]

            @staticmethod
            def layer_68(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[68]]

            @staticmethod
            def layer_69(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[69]]

            @staticmethod
            def layer_70(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[70]]

            @staticmethod
            def layer_71(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[71]]

            @staticmethod
            def layer_72(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[72]]

            @staticmethod
            def layer_73(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[73]]

            @staticmethod
            def layer_74(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[74]]

            @staticmethod
            def layer_75(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[75]]

            @staticmethod
            def layer_76(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[76]]

            @staticmethod
            def layer_77(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[77]]

            @staticmethod
            def layer_78(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[78]]

            @staticmethod
            def layer_79(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[79]]

            @staticmethod
            def layer_80(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[80]]

            @staticmethod
            def layer_81(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[81]]

            @staticmethod
            def layer_82(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[82]]

            @staticmethod
            def layer_83(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[83]]

            @staticmethod
            def layer_84(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[84]]

            @staticmethod
            def layer_85(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[85]]

            @staticmethod
            def layer_86(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[86]]

            @staticmethod
            def layer_87(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[87]]

            @staticmethod
            def layer_88(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[88]]

            @staticmethod
            def layer_89(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[89]]

            @staticmethod
            def layer_90(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[90]]

            @staticmethod
            def layer_91(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[91]]

            @staticmethod
            def layer_92(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[92]]

            @staticmethod
            def layer_93(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[93]]

            @staticmethod
            def layer_94(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[94]]

            @staticmethod
            def layer_95(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[95]]

            @staticmethod
            def layer_96(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[96]]

            @staticmethod
            def layer_97(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[97]]

            @staticmethod
            def layer_98(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[98]]

            @staticmethod
            def layer_99(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[99]]

            @staticmethod
            def layer_100(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[100]]

            @staticmethod
            def layer_101(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[101]]

            @staticmethod
            def layer_102(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[102]]

            @staticmethod
            def layer_103(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[103]]

            @staticmethod
            def layer_104(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[104]]

            @staticmethod
            def layer_105(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[105]]

            @staticmethod
            def layer_106(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[106]]

            @staticmethod
            def layer_107(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[107]]

            @staticmethod
            def layer_108(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[108]]

            @staticmethod
            def layer_109(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[109]]

            @staticmethod
            def layer_110(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[110]]

            @staticmethod
            def layer_111(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[111]]

            @staticmethod
            def layer_112(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[112]]

            @staticmethod
            def layer_113(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[113]]

            @staticmethod
            def layer_114(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[114]]

            @staticmethod
            def layer_115(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[115]]

            @staticmethod
            def layer_116(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[116]]

            @staticmethod
            def layer_117(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[117]]

            @staticmethod
            def layer_118(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[118]]

            @staticmethod
            def layer_119(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[119]]

            @staticmethod
            def layer_120(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[120]]

            @staticmethod
            def layer_121(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[121]]

            @staticmethod
            def layer_122(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[122]]

            @staticmethod
            def layer_123(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[123]]

            @staticmethod
            def layer_124(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[124]]

            @staticmethod
            def layer_125(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[125]]

            @staticmethod
            def layer_126(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[126]]

            @staticmethod
            def layer_127(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[127]]

            @staticmethod
            def layer_128(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[128]]

            @staticmethod
            def layer_129(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[129]]

            @staticmethod
            def layer_130(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[130]]

            @staticmethod
            def layer_131(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[131]]

            @staticmethod
            def layer_132(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[132]]

            @staticmethod
            def layer_133(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[133]]

            @staticmethod
            def layer_134(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[134]]

            @staticmethod
            def layer_135(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[135]]

            @staticmethod
            def layer_136(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[136]]

            @staticmethod
            def layer_137(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[137]]

            @staticmethod
            def layer_138(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[138]]

            @staticmethod
            def layer_139(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[139]]

            @staticmethod
            def layer_140(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[140]]

            @staticmethod
            def layer_141(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[141]]

            @staticmethod
            def layer_142(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[142]]

            @staticmethod
            def layer_143(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[143]]

            @staticmethod
            def layer_144(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[144]]

            @staticmethod
            def layer_145(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[145]]

            @staticmethod
            def layer_146(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[146]]

            @staticmethod
            def layer_147(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[147]]

            @staticmethod
            def layer_148(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[148]]

            @staticmethod
            def layer_149(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[149]]

            @staticmethod
            def layer_150(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[150]]

            @staticmethod
            def layer_151(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[151]]

            @staticmethod
            def layer_152(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[152]]

            @staticmethod
            def layer_153(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[153]]

            @staticmethod
            def layer_154(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[154]]

            @staticmethod
            def layer_155(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[155]]

            @staticmethod
            def layer_156(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[156]]

            @staticmethod
            def layer_157(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[157]]

            @staticmethod
            def layer_158(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[158]]

            @staticmethod
            def layer_159(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[159]]

            @staticmethod
            def layer_160(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[160]]

            @staticmethod
            def layer_161(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[161]]

            @staticmethod
            def layer_162(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[162]]

            @staticmethod
            def layer_163(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[163]]

            @staticmethod
            def layer_164(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[164]]

            @staticmethod
            def layer_165(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[165]]

            @staticmethod
            def layer_166(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[166]]

            @staticmethod
            def layer_167(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[167]]

            @staticmethod
            def layer_168(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[168]]

            @staticmethod
            def layer_169(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[169]]

            @staticmethod
            def layer_170(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[170]]

            @staticmethod
            def layer_171(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[171]]

            @staticmethod
            def layer_172(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[172]]

            @staticmethod
            def layer_173(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[173]]

            @staticmethod
            def layer_174(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[174]]

            @staticmethod
            def layer_175(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[175]]

            @staticmethod
            def layer_176(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[176]]

            @staticmethod
            def layer_177(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[177]]

            @staticmethod
            def layer_178(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[178]]

            @staticmethod
            def layer_179(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[179]]

            @staticmethod
            def layer_180(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[180]]

            @staticmethod
            def layer_181(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[181]]

            @staticmethod
            def layer_182(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[182]]

            @staticmethod
            def layer_183(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[183]]

            @staticmethod
            def layer_184(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[184]]

            @staticmethod
            def layer_185(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[185]]

            @staticmethod
            def layer_186(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[186]]

            @staticmethod
            def layer_187(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[187]]

            @staticmethod
            def layer_188(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[188]]

            @staticmethod
            def layer_189(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[189]]

            @staticmethod
            def layer_190(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[190]]

            @staticmethod
            def layer_191(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[191]]

            @staticmethod
            def layer_192(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[192]]

            @staticmethod
            def layer_193(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[193]]

            @staticmethod
            def layer_194(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[194]]

            @staticmethod
            def layer_195(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[195]]

            @staticmethod
            def layer_196(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[196]]

            @staticmethod
            def layer_197(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[197]]

            @staticmethod
            def layer_198(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[198]]

            @staticmethod
            def layer_199(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[129]
                return t.enum_values[t.generated_offsets[199]]

            @staticmethod
            def create(greycat: GreyCat) -> algebra.nn_layers_names.NNLayersNames:
                return algebra.nn_layers_names.NNLayersNames(greycat.libs_by_name[algebra.name_].mapped[129], [])

    @final
    class nn:

        @final
        class ClassificationNetwork(GreyCat.Object):
            name_: Final[str] = "nn::ClassificationNetwork"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def inputs(self) -> int:
                return self._get(self.type_.generated_offsets[0])

            def set_inputs(self, v: int) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def inputs_gradients(self) -> bool:
                return self._get(self.type_.generated_offsets[1])

            def set_inputs_gradients(self, v: bool) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def outputs(self) -> int:
                return self._get(self.type_.generated_offsets[2])

            def set_outputs(self, v: int) -> None:
                self._set(self.type_.generated_offsets[2], v)

            def fixed_batch_size(self) -> int:
                return self._get(self.type_.generated_offsets[3])

            def set_fixed_batch_size(self, v: int) -> None:
                self._set(self.type_.generated_offsets[3], v)

            def inputs_sequences(self) -> int:
                return self._get(self.type_.generated_offsets[4])

            def set_inputs_sequences(self, v: int) -> None:
                self._set(self.type_.generated_offsets[4], v)

            def outputs_sequences(self) -> int:
                return self._get(self.type_.generated_offsets[5])

            def set_outputs_sequences(self, v: int) -> None:
                self._set(self.type_.generated_offsets[5], v)

            def tensor_type(self) -> std.core.TensorType:
                return self._get(self.type_.generated_offsets[6])

            def set_tensor_type(self, v: std.core.TensorType) -> None:
                self._set(self.type_.generated_offsets[6], v)

            def seed(self) -> int:
                return self._get(self.type_.generated_offsets[7])

            def set_seed(self, v: int) -> None:
                self._set(self.type_.generated_offsets[7], v)

            def randomizeSeed(self) -> bool:
                return self._get(self.type_.generated_offsets[8])

            def set_randomizeSeed(self, v: bool) -> None:
                self._set(self.type_.generated_offsets[8], v)

            def layers(self) -> std.core.Array:
                return self._get(self.type_.generated_offsets[9])

            def set_layers(self, v: std.core.Array) -> None:
                self._set(self.type_.generated_offsets[9], v)

            def preProcessType(self) -> algebra.nn.PreProcessType:
                return self._get(self.type_.generated_offsets[10])

            def set_preProcessType(self, v: algebra.nn.PreProcessType) -> None:
                self._set(self.type_.generated_offsets[10], v)

            def preProcessObject(self) -> Any:
                return self._get(self.type_.generated_offsets[11])

            def set_preProcessObject(self, v: Any) -> None:
                self._set(self.type_.generated_offsets[11], v)

            def postProcessType(self) -> algebra.nn.PostProcessType:
                return self._get(self.type_.generated_offsets[12])

            def set_postProcessType(self, v: algebra.nn.PostProcessType) -> None:
                self._set(self.type_.generated_offsets[12], v)

            def postProcessObject(self) -> Any:
                return self._get(self.type_.generated_offsets[13])

            def set_postProcessObject(self, v: Any) -> None:
                self._set(self.type_.generated_offsets[13], v)

            def optimizer(self) -> algebra.compute.ComputeOptimizer:
                return self._get(self.type_.generated_offsets[14])

            def set_optimizer(self, v: algebra.compute.ComputeOptimizer) -> None:
                self._set(self.type_.generated_offsets[14], v)

            def lossLayer(self) -> algebra.compute.ComputeLayerLoss:
                return self._get(self.type_.generated_offsets[15])

            def set_lossLayer(self, v: algebra.compute.ComputeLayerLoss) -> None:
                self._set(self.type_.generated_offsets[15], v)

            def _lastLayer(self) -> str:
                return self._get(self.type_.generated_offsets[16])

            def set__lastLayer(self, v: str) -> None:
                self._set(self.type_.generated_offsets[16], v)

            def _lastOutput(self) -> str:
                return self._get(self.type_.generated_offsets[17])

            def set__lastOutput(self, v: str) -> None:
                self._set(self.type_.generated_offsets[17], v)

            def calculate_probabilities(self) -> bool:
                return self._get(self.type_.generated_offsets[18])

            def set_calculate_probabilities(self, v: bool) -> None:
                self._set(self.type_.generated_offsets[18], v)

            def has_class_weights(self) -> bool:
                return self._get(self.type_.generated_offsets[19])

            def set_has_class_weights(self, v: bool) -> None:
                self._set(self.type_.generated_offsets[19], v)

            def from_logits(self) -> bool:
                return self._get(self.type_.generated_offsets[20])

            def set_from_logits(self, v: bool) -> None:
                self._set(self.type_.generated_offsets[20], v)

            @staticmethod
            def create(greycat: GreyCat, inputs: int, inputs_gradients: bool, outputs: int, fixed_batch_size: int, inputs_sequences: int, outputs_sequences: int, tensor_type: std.core.TensorType, seed: int, randomizeSeed: bool, layers: std.core.Array, preProcessType: algebra.nn.PreProcessType, preProcessObject: Any, postProcessType: algebra.nn.PostProcessType, postProcessObject: Any, optimizer: algebra.compute.ComputeOptimizer, lossLayer: algebra.compute.ComputeLayerLoss, _lastLayer: str, _lastOutput: str, calculate_probabilities: bool, has_class_weights: bool, from_logits: bool) -> algebra.nn.ClassificationNetwork:
                return algebra.nn.ClassificationNetwork(greycat.libs_by_name[algebra.name_].mapped[130], [inputs, inputs_gradients, outputs, fixed_batch_size, inputs_sequences, outputs_sequences, tensor_type, seed, randomizeSeed, layers, preProcessType, preProcessObject, postProcessType, postProcessObject, optimizer, lossLayer, _lastLayer, _lastOutput, calculate_probabilities, has_class_weights, from_logits])

        @final
        class ComputeOptimizers(GreyCat.Enum):
            name_: Final[str] = "nn::ComputeOptimizers"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            @staticmethod
            def ada_delta(greycat: GreyCat) -> algebra.nn.ComputeOptimizers:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[131]
                return t.enum_values[t.generated_offsets[0]]

            @staticmethod
            def ada_grad(greycat: GreyCat) -> algebra.nn.ComputeOptimizers:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[131]
                return t.enum_values[t.generated_offsets[1]]

            @staticmethod
            def adam(greycat: GreyCat) -> algebra.nn.ComputeOptimizers:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[131]
                return t.enum_values[t.generated_offsets[2]]

            @staticmethod
            def ada_max(greycat: GreyCat) -> algebra.nn.ComputeOptimizers:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[131]
                return t.enum_values[t.generated_offsets[3]]

            @staticmethod
            def nadam(greycat: GreyCat) -> algebra.nn.ComputeOptimizers:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[131]
                return t.enum_values[t.generated_offsets[4]]

            @staticmethod
            def ftrl(greycat: GreyCat) -> algebra.nn.ComputeOptimizers:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[131]
                return t.enum_values[t.generated_offsets[5]]

            @staticmethod
            def sgd(greycat: GreyCat) -> algebra.nn.ComputeOptimizers:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[131]
                return t.enum_values[t.generated_offsets[6]]

            @staticmethod
            def rms_prop(greycat: GreyCat) -> algebra.nn.ComputeOptimizers:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[131]
                return t.enum_values[t.generated_offsets[7]]

            @staticmethod
            def momentum(greycat: GreyCat) -> algebra.nn.ComputeOptimizers:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[131]
                return t.enum_values[t.generated_offsets[8]]

            @staticmethod
            def nesterov(greycat: GreyCat) -> algebra.nn.ComputeOptimizers:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[131]
                return t.enum_values[t.generated_offsets[9]]

            @staticmethod
            def create(greycat: GreyCat) -> algebra.nn.ComputeOptimizers:
                return algebra.nn.ComputeOptimizers(greycat.libs_by_name[algebra.name_].mapped[131], [])

        @final
        class BindingsResult(GreyCat.Object):
            name_: Final[str] = "nn::BindingsResult"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def previousLayerName(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_previousLayerName(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def previousLayerOutput(self) -> str:
                return self._get(self.type_.generated_offsets[1])

            def set_previousLayerOutput(self, v: str) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def expectedLayerName(self) -> str:
                return self._get(self.type_.generated_offsets[2])

            def set_expectedLayerName(self, v: str) -> None:
                self._set(self.type_.generated_offsets[2], v)

            def expectedLayerOutput(self) -> str:
                return self._get(self.type_.generated_offsets[3])

            def set_expectedLayerOutput(self, v: str) -> None:
                self._set(self.type_.generated_offsets[3], v)

            def postLayer(self) -> algebra.compute.ComputeLayer:
                return self._get(self.type_.generated_offsets[4])

            def set_postLayer(self, v: algebra.compute.ComputeLayer) -> None:
                self._set(self.type_.generated_offsets[4], v)

            @staticmethod
            def create(greycat: GreyCat, previousLayerName: str, previousLayerOutput: str, expectedLayerName: str, expectedLayerOutput: str, postLayer: algebra.compute.ComputeLayer) -> algebra.nn.BindingsResult:
                return algebra.nn.BindingsResult(greycat.libs_by_name[algebra.name_].mapped[132], [previousLayerName, previousLayerOutput, expectedLayerName, expectedLayerOutput, postLayer])

        @final
        class PreProcessType(GreyCat.Enum):
            name_: Final[str] = "nn::PreProcessType"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            @staticmethod
            def none(greycat: GreyCat) -> algebra.nn.PreProcessType:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[133]
                return t.enum_values[t.generated_offsets[0]]

            @staticmethod
            def min_max_scaling(greycat: GreyCat) -> algebra.nn.PreProcessType:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[133]
                return t.enum_values[t.generated_offsets[1]]

            @staticmethod
            def standard_scaling(greycat: GreyCat) -> algebra.nn.PreProcessType:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[133]
                return t.enum_values[t.generated_offsets[2]]

            @staticmethod
            def pca_scaling(greycat: GreyCat) -> algebra.nn.PreProcessType:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[133]
                return t.enum_values[t.generated_offsets[3]]

            @staticmethod
            def create(greycat: GreyCat) -> algebra.nn.PreProcessType:
                return algebra.nn.PreProcessType(greycat.libs_by_name[algebra.name_].mapped[133], [])

        @final
        class PostProcessType(GreyCat.Enum):
            name_: Final[str] = "nn::PostProcessType"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            @staticmethod
            def none(greycat: GreyCat) -> algebra.nn.PostProcessType:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[134]
                return t.enum_values[t.generated_offsets[0]]

            @staticmethod
            def min_max_scaling(greycat: GreyCat) -> algebra.nn.PostProcessType:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[134]
                return t.enum_values[t.generated_offsets[1]]

            @staticmethod
            def standard_scaling(greycat: GreyCat) -> algebra.nn.PostProcessType:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[134]
                return t.enum_values[t.generated_offsets[2]]

            @staticmethod
            def create(greycat: GreyCat) -> algebra.nn.PostProcessType:
                return algebra.nn.PostProcessType(greycat.libs_by_name[algebra.name_].mapped[134], [])

        @final
        class AutoEncoderNetwork(GreyCat.Object):
            name_: Final[str] = "nn::AutoEncoderNetwork"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def inputs(self) -> int:
                return self._get(self.type_.generated_offsets[0])

            def set_inputs(self, v: int) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def inputs_gradients(self) -> bool:
                return self._get(self.type_.generated_offsets[1])

            def set_inputs_gradients(self, v: bool) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def outputs(self) -> int:
                return self._get(self.type_.generated_offsets[2])

            def set_outputs(self, v: int) -> None:
                self._set(self.type_.generated_offsets[2], v)

            def fixed_batch_size(self) -> int:
                return self._get(self.type_.generated_offsets[3])

            def set_fixed_batch_size(self, v: int) -> None:
                self._set(self.type_.generated_offsets[3], v)

            def inputs_sequences(self) -> int:
                return self._get(self.type_.generated_offsets[4])

            def set_inputs_sequences(self, v: int) -> None:
                self._set(self.type_.generated_offsets[4], v)

            def outputs_sequences(self) -> int:
                return self._get(self.type_.generated_offsets[5])

            def set_outputs_sequences(self, v: int) -> None:
                self._set(self.type_.generated_offsets[5], v)

            def tensor_type(self) -> std.core.TensorType:
                return self._get(self.type_.generated_offsets[6])

            def set_tensor_type(self, v: std.core.TensorType) -> None:
                self._set(self.type_.generated_offsets[6], v)

            def seed(self) -> int:
                return self._get(self.type_.generated_offsets[7])

            def set_seed(self, v: int) -> None:
                self._set(self.type_.generated_offsets[7], v)

            def randomizeSeed(self) -> bool:
                return self._get(self.type_.generated_offsets[8])

            def set_randomizeSeed(self, v: bool) -> None:
                self._set(self.type_.generated_offsets[8], v)

            def layers(self) -> std.core.Array:
                return self._get(self.type_.generated_offsets[9])

            def set_layers(self, v: std.core.Array) -> None:
                self._set(self.type_.generated_offsets[9], v)

            def preProcessType(self) -> algebra.nn.PreProcessType:
                return self._get(self.type_.generated_offsets[10])

            def set_preProcessType(self, v: algebra.nn.PreProcessType) -> None:
                self._set(self.type_.generated_offsets[10], v)

            def preProcessObject(self) -> Any:
                return self._get(self.type_.generated_offsets[11])

            def set_preProcessObject(self, v: Any) -> None:
                self._set(self.type_.generated_offsets[11], v)

            def postProcessType(self) -> algebra.nn.PostProcessType:
                return self._get(self.type_.generated_offsets[12])

            def set_postProcessType(self, v: algebra.nn.PostProcessType) -> None:
                self._set(self.type_.generated_offsets[12], v)

            def postProcessObject(self) -> Any:
                return self._get(self.type_.generated_offsets[13])

            def set_postProcessObject(self, v: Any) -> None:
                self._set(self.type_.generated_offsets[13], v)

            def optimizer(self) -> algebra.compute.ComputeOptimizer:
                return self._get(self.type_.generated_offsets[14])

            def set_optimizer(self, v: algebra.compute.ComputeOptimizer) -> None:
                self._set(self.type_.generated_offsets[14], v)

            def lossLayer(self) -> algebra.compute.ComputeLayerLoss:
                return self._get(self.type_.generated_offsets[15])

            def set_lossLayer(self, v: algebra.compute.ComputeLayerLoss) -> None:
                self._set(self.type_.generated_offsets[15], v)

            def _lastLayer(self) -> str:
                return self._get(self.type_.generated_offsets[16])

            def set__lastLayer(self, v: str) -> None:
                self._set(self.type_.generated_offsets[16], v)

            def _lastOutput(self) -> str:
                return self._get(self.type_.generated_offsets[17])

            def set__lastOutput(self, v: str) -> None:
                self._set(self.type_.generated_offsets[17], v)

            def encoder_layer_idx(self) -> int:
                return self._get(self.type_.generated_offsets[18])

            def set_encoder_layer_idx(self, v: int) -> None:
                self._set(self.type_.generated_offsets[18], v)

            def encoder_layer_name(self) -> str:
                return self._get(self.type_.generated_offsets[19])

            def set_encoder_layer_name(self, v: str) -> None:
                self._set(self.type_.generated_offsets[19], v)

            def encoder_layer_var(self) -> str:
                return self._get(self.type_.generated_offsets[20])

            def set_encoder_layer_var(self, v: str) -> None:
                self._set(self.type_.generated_offsets[20], v)

            @staticmethod
            def create(greycat: GreyCat, inputs: int, inputs_gradients: bool, outputs: int, fixed_batch_size: int, inputs_sequences: int, outputs_sequences: int, tensor_type: std.core.TensorType, seed: int, randomizeSeed: bool, layers: std.core.Array, preProcessType: algebra.nn.PreProcessType, preProcessObject: Any, postProcessType: algebra.nn.PostProcessType, postProcessObject: Any, optimizer: algebra.compute.ComputeOptimizer, lossLayer: algebra.compute.ComputeLayerLoss, _lastLayer: str, _lastOutput: str, encoder_layer_idx: int, encoder_layer_name: str, encoder_layer_var: str) -> algebra.nn.AutoEncoderNetwork:
                return algebra.nn.AutoEncoderNetwork(greycat.libs_by_name[algebra.name_].mapped[135], [inputs, inputs_gradients, outputs, fixed_batch_size, inputs_sequences, outputs_sequences, tensor_type, seed, randomizeSeed, layers, preProcessType, preProcessObject, postProcessType, postProcessObject, optimizer, lossLayer, _lastLayer, _lastOutput, encoder_layer_idx, encoder_layer_name, encoder_layer_var])

        @final
        class ComputeActivations(GreyCat.Enum):
            name_: Final[str] = "nn::ComputeActivations"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            @staticmethod
            def relu(greycat: GreyCat) -> algebra.nn.ComputeActivations:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[136]
                return t.enum_values[t.generated_offsets[0]]

            @staticmethod
            def leaky_relu(greycat: GreyCat) -> algebra.nn.ComputeActivations:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[136]
                return t.enum_values[t.generated_offsets[1]]

            @staticmethod
            def sigmoid(greycat: GreyCat) -> algebra.nn.ComputeActivations:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[136]
                return t.enum_values[t.generated_offsets[2]]

            @staticmethod
            def hard_sigmoid(greycat: GreyCat) -> algebra.nn.ComputeActivations:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[136]
                return t.enum_values[t.generated_offsets[3]]

            @staticmethod
            def exp(greycat: GreyCat) -> algebra.nn.ComputeActivations:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[136]
                return t.enum_values[t.generated_offsets[4]]

            @staticmethod
            def soft_max(greycat: GreyCat) -> algebra.nn.ComputeActivations:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[136]
                return t.enum_values[t.generated_offsets[5]]

            @staticmethod
            def soft_plus(greycat: GreyCat) -> algebra.nn.ComputeActivations:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[136]
                return t.enum_values[t.generated_offsets[6]]

            @staticmethod
            def soft_sign(greycat: GreyCat) -> algebra.nn.ComputeActivations:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[136]
                return t.enum_values[t.generated_offsets[7]]

            @staticmethod
            def tanh(greycat: GreyCat) -> algebra.nn.ComputeActivations:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[136]
                return t.enum_values[t.generated_offsets[8]]

            @staticmethod
            def selu(greycat: GreyCat) -> algebra.nn.ComputeActivations:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[136]
                return t.enum_values[t.generated_offsets[9]]

            @staticmethod
            def elu(greycat: GreyCat) -> algebra.nn.ComputeActivations:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[136]
                return t.enum_values[t.generated_offsets[10]]

            @staticmethod
            def celu(greycat: GreyCat) -> algebra.nn.ComputeActivations:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[136]
                return t.enum_values[t.generated_offsets[11]]

            @staticmethod
            def create(greycat: GreyCat) -> algebra.nn.ComputeActivations:
                return algebra.nn.ComputeActivations(greycat.libs_by_name[algebra.name_].mapped[136], [])

        @final
        class ComputeInitializers(GreyCat.Enum):
            name_: Final[str] = "nn::ComputeInitializers"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            @staticmethod
            def none(greycat: GreyCat) -> algebra.nn.ComputeInitializers:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[137]
                return t.enum_values[t.generated_offsets[0]]

            @staticmethod
            def constant(greycat: GreyCat) -> algebra.nn.ComputeInitializers:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[137]
                return t.enum_values[t.generated_offsets[1]]

            @staticmethod
            def sigmoid_uniform(greycat: GreyCat) -> algebra.nn.ComputeInitializers:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[137]
                return t.enum_values[t.generated_offsets[2]]

            @staticmethod
            def lecun_uniform(greycat: GreyCat) -> algebra.nn.ComputeInitializers:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[137]
                return t.enum_values[t.generated_offsets[3]]

            @staticmethod
            def xavier(greycat: GreyCat) -> algebra.nn.ComputeInitializers:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[137]
                return t.enum_values[t.generated_offsets[4]]

            @staticmethod
            def xavier_uniform(greycat: GreyCat) -> algebra.nn.ComputeInitializers:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[137]
                return t.enum_values[t.generated_offsets[5]]

            @staticmethod
            def relu(greycat: GreyCat) -> algebra.nn.ComputeInitializers:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[137]
                return t.enum_values[t.generated_offsets[6]]

            @staticmethod
            def relu_uniform(greycat: GreyCat) -> algebra.nn.ComputeInitializers:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[137]
                return t.enum_values[t.generated_offsets[7]]

            @staticmethod
            def normal(greycat: GreyCat) -> algebra.nn.ComputeInitializers:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[137]
                return t.enum_values[t.generated_offsets[8]]

            @staticmethod
            def normal_in(greycat: GreyCat) -> algebra.nn.ComputeInitializers:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[137]
                return t.enum_values[t.generated_offsets[9]]

            @staticmethod
            def normal_out(greycat: GreyCat) -> algebra.nn.ComputeInitializers:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[137]
                return t.enum_values[t.generated_offsets[10]]

            @staticmethod
            def normal_avg(greycat: GreyCat) -> algebra.nn.ComputeInitializers:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[137]
                return t.enum_values[t.generated_offsets[11]]

            @staticmethod
            def uniform(greycat: GreyCat) -> algebra.nn.ComputeInitializers:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[137]
                return t.enum_values[t.generated_offsets[12]]

            @staticmethod
            def uniform_in(greycat: GreyCat) -> algebra.nn.ComputeInitializers:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[137]
                return t.enum_values[t.generated_offsets[13]]

            @staticmethod
            def uniform_out(greycat: GreyCat) -> algebra.nn.ComputeInitializers:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[137]
                return t.enum_values[t.generated_offsets[14]]

            @staticmethod
            def uniform_avg(greycat: GreyCat) -> algebra.nn.ComputeInitializers:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[137]
                return t.enum_values[t.generated_offsets[15]]

            @staticmethod
            def identity(greycat: GreyCat) -> algebra.nn.ComputeInitializers:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[137]
                return t.enum_values[t.generated_offsets[16]]

            @staticmethod
            def pytorch(greycat: GreyCat) -> algebra.nn.ComputeInitializers:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[137]
                return t.enum_values[t.generated_offsets[17]]

            @staticmethod
            def create(greycat: GreyCat) -> algebra.nn.ComputeInitializers:
                return algebra.nn.ComputeInitializers(greycat.libs_by_name[algebra.name_].mapped[137], [])

        @final
        class NeuralNetwork(GreyCat.Object):
            name_: Final[str] = "nn::NeuralNetwork"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def inputs(self) -> int:
                return self._get(self.type_.generated_offsets[0])

            def set_inputs(self, v: int) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def inputs_gradients(self) -> bool:
                return self._get(self.type_.generated_offsets[1])

            def set_inputs_gradients(self, v: bool) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def outputs(self) -> int:
                return self._get(self.type_.generated_offsets[2])

            def set_outputs(self, v: int) -> None:
                self._set(self.type_.generated_offsets[2], v)

            def fixed_batch_size(self) -> int:
                return self._get(self.type_.generated_offsets[3])

            def set_fixed_batch_size(self, v: int) -> None:
                self._set(self.type_.generated_offsets[3], v)

            def inputs_sequences(self) -> int:
                return self._get(self.type_.generated_offsets[4])

            def set_inputs_sequences(self, v: int) -> None:
                self._set(self.type_.generated_offsets[4], v)

            def outputs_sequences(self) -> int:
                return self._get(self.type_.generated_offsets[5])

            def set_outputs_sequences(self, v: int) -> None:
                self._set(self.type_.generated_offsets[5], v)

            def tensor_type(self) -> std.core.TensorType:
                return self._get(self.type_.generated_offsets[6])

            def set_tensor_type(self, v: std.core.TensorType) -> None:
                self._set(self.type_.generated_offsets[6], v)

            def seed(self) -> int:
                return self._get(self.type_.generated_offsets[7])

            def set_seed(self, v: int) -> None:
                self._set(self.type_.generated_offsets[7], v)

            def randomizeSeed(self) -> bool:
                return self._get(self.type_.generated_offsets[8])

            def set_randomizeSeed(self, v: bool) -> None:
                self._set(self.type_.generated_offsets[8], v)

            def layers(self) -> std.core.Array:
                return self._get(self.type_.generated_offsets[9])

            def set_layers(self, v: std.core.Array) -> None:
                self._set(self.type_.generated_offsets[9], v)

            def preProcessType(self) -> algebra.nn.PreProcessType:
                return self._get(self.type_.generated_offsets[10])

            def set_preProcessType(self, v: algebra.nn.PreProcessType) -> None:
                self._set(self.type_.generated_offsets[10], v)

            def preProcessObject(self) -> Any:
                return self._get(self.type_.generated_offsets[11])

            def set_preProcessObject(self, v: Any) -> None:
                self._set(self.type_.generated_offsets[11], v)

            def postProcessType(self) -> algebra.nn.PostProcessType:
                return self._get(self.type_.generated_offsets[12])

            def set_postProcessType(self, v: algebra.nn.PostProcessType) -> None:
                self._set(self.type_.generated_offsets[12], v)

            def postProcessObject(self) -> Any:
                return self._get(self.type_.generated_offsets[13])

            def set_postProcessObject(self, v: Any) -> None:
                self._set(self.type_.generated_offsets[13], v)

            def optimizer(self) -> algebra.compute.ComputeOptimizer:
                return self._get(self.type_.generated_offsets[14])

            def set_optimizer(self, v: algebra.compute.ComputeOptimizer) -> None:
                self._set(self.type_.generated_offsets[14], v)

            def lossLayer(self) -> algebra.compute.ComputeLayerLoss:
                return self._get(self.type_.generated_offsets[15])

            def set_lossLayer(self, v: algebra.compute.ComputeLayerLoss) -> None:
                self._set(self.type_.generated_offsets[15], v)

            def _lastLayer(self) -> str:
                return self._get(self.type_.generated_offsets[16])

            def set__lastLayer(self, v: str) -> None:
                self._set(self.type_.generated_offsets[16], v)

            def _lastOutput(self) -> str:
                return self._get(self.type_.generated_offsets[17])

            def set__lastOutput(self, v: str) -> None:
                self._set(self.type_.generated_offsets[17], v)

            @staticmethod
            def err_negative_in_out(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[138]
                return t.static_values[0]

            @staticmethod
            def err_last_layer_wrong(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[138]
                return t.static_values[1]

            @staticmethod
            def err_incompatible_loss(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[138]
                return t.static_values[2]

            @staticmethod
            def err_layer_not_supported(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[138]
                return t.static_values[3]

            @staticmethod
            def err_tensor_type_not_supported(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[138]
                return t.static_values[4]

            @staticmethod
            def err_minimum_layers(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[138]
                return t.static_values[5]

            @staticmethod
            def layer_placeholders_name(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[138]
                return t.static_values[6]

            @staticmethod
            def layer_classification_name(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[138]
                return t.static_values[7]

            @staticmethod
            def layer_preprocess_name(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[138]
                return t.static_values[8]

            @staticmethod
            def layer_postprocess_learn_name(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[138]
                return t.static_values[9]

            @staticmethod
            def layer_main_layers_name(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[138]
                return t.static_values[10]

            @staticmethod
            def layer_loss_learn_name(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[138]
                return t.static_values[11]

            @staticmethod
            def layer_loss_display_name(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[138]
                return t.static_values[12]

            @staticmethod
            def layer_postprocess_display_name(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[138]
                return t.static_values[13]

            @staticmethod
            def layer_confusion_name(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[138]
                return t.static_values[14]

            @staticmethod
            def seq_predict(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[138]
                return t.static_values[15]

            @staticmethod
            def seq_post_process(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[138]
                return t.static_values[16]

            @staticmethod
            def seq_learn(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[138]
                return t.static_values[17]

            @staticmethod
            def seq_loss_display(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[138]
                return t.static_values[18]

            @staticmethod
            def seq_encode(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[138]
                return t.static_values[19]

            @staticmethod
            def seq_decode(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[138]
                return t.static_values[20]

            @staticmethod
            def seq_confusion(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[138]
                return t.static_values[21]

            @staticmethod
            def var_inputs_name(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[138]
                return t.static_values[22]

            @staticmethod
            def var_enc_inputs_name(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[138]
                return t.static_values[23]

            @staticmethod
            def var_targets_name(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[138]
                return t.static_values[24]

            @staticmethod
            def var_classifier_classes(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[138]
                return t.static_values[25]

            @staticmethod
            def var_classifier_probabilities(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[138]
                return t.static_values[26]

            @staticmethod
            def var_classifier_class_weights(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[138]
                return t.static_values[27]

            @staticmethod
            def var_classifier_confusion(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[138]
                return t.static_values[28]

            @staticmethod
            def var_input_avg(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[138]
                return t.static_values[29]

            @staticmethod
            def var_input_min(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[138]
                return t.static_values[30]

            @staticmethod
            def var_input_max(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[138]
                return t.static_values[31]

            @staticmethod
            def var_input_std(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[138]
                return t.static_values[32]

            @staticmethod
            def var_input_space(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[138]
                return t.static_values[33]

            @staticmethod
            def var_output_avg(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[138]
                return t.static_values[34]

            @staticmethod
            def var_output_min(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[138]
                return t.static_values[35]

            @staticmethod
            def var_output_max(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[138]
                return t.static_values[36]

            @staticmethod
            def var_output_std(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[138]
                return t.static_values[37]

            @staticmethod
            def create(greycat: GreyCat, inputs: int, inputs_gradients: bool, outputs: int, fixed_batch_size: int, inputs_sequences: int, outputs_sequences: int, tensor_type: std.core.TensorType, seed: int, randomizeSeed: bool, layers: std.core.Array, preProcessType: algebra.nn.PreProcessType, preProcessObject: Any, postProcessType: algebra.nn.PostProcessType, postProcessObject: Any, optimizer: algebra.compute.ComputeOptimizer, lossLayer: algebra.compute.ComputeLayerLoss, _lastLayer: str, _lastOutput: str) -> algebra.nn.NeuralNetwork:
                return algebra.nn.NeuralNetwork(greycat.libs_by_name[algebra.name_].mapped[138], [inputs, inputs_gradients, outputs, fixed_batch_size, inputs_sequences, outputs_sequences, tensor_type, seed, randomizeSeed, layers, preProcessType, preProcessObject, postProcessType, postProcessObject, optimizer, lossLayer, _lastLayer, _lastOutput])

        @final
        class RegressionNetwork(GreyCat.Object):
            name_: Final[str] = "nn::RegressionNetwork"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def inputs(self) -> int:
                return self._get(self.type_.generated_offsets[0])

            def set_inputs(self, v: int) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def inputs_gradients(self) -> bool:
                return self._get(self.type_.generated_offsets[1])

            def set_inputs_gradients(self, v: bool) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def outputs(self) -> int:
                return self._get(self.type_.generated_offsets[2])

            def set_outputs(self, v: int) -> None:
                self._set(self.type_.generated_offsets[2], v)

            def fixed_batch_size(self) -> int:
                return self._get(self.type_.generated_offsets[3])

            def set_fixed_batch_size(self, v: int) -> None:
                self._set(self.type_.generated_offsets[3], v)

            def inputs_sequences(self) -> int:
                return self._get(self.type_.generated_offsets[4])

            def set_inputs_sequences(self, v: int) -> None:
                self._set(self.type_.generated_offsets[4], v)

            def outputs_sequences(self) -> int:
                return self._get(self.type_.generated_offsets[5])

            def set_outputs_sequences(self, v: int) -> None:
                self._set(self.type_.generated_offsets[5], v)

            def tensor_type(self) -> std.core.TensorType:
                return self._get(self.type_.generated_offsets[6])

            def set_tensor_type(self, v: std.core.TensorType) -> None:
                self._set(self.type_.generated_offsets[6], v)

            def seed(self) -> int:
                return self._get(self.type_.generated_offsets[7])

            def set_seed(self, v: int) -> None:
                self._set(self.type_.generated_offsets[7], v)

            def randomizeSeed(self) -> bool:
                return self._get(self.type_.generated_offsets[8])

            def set_randomizeSeed(self, v: bool) -> None:
                self._set(self.type_.generated_offsets[8], v)

            def layers(self) -> std.core.Array:
                return self._get(self.type_.generated_offsets[9])

            def set_layers(self, v: std.core.Array) -> None:
                self._set(self.type_.generated_offsets[9], v)

            def preProcessType(self) -> algebra.nn.PreProcessType:
                return self._get(self.type_.generated_offsets[10])

            def set_preProcessType(self, v: algebra.nn.PreProcessType) -> None:
                self._set(self.type_.generated_offsets[10], v)

            def preProcessObject(self) -> Any:
                return self._get(self.type_.generated_offsets[11])

            def set_preProcessObject(self, v: Any) -> None:
                self._set(self.type_.generated_offsets[11], v)

            def postProcessType(self) -> algebra.nn.PostProcessType:
                return self._get(self.type_.generated_offsets[12])

            def set_postProcessType(self, v: algebra.nn.PostProcessType) -> None:
                self._set(self.type_.generated_offsets[12], v)

            def postProcessObject(self) -> Any:
                return self._get(self.type_.generated_offsets[13])

            def set_postProcessObject(self, v: Any) -> None:
                self._set(self.type_.generated_offsets[13], v)

            def optimizer(self) -> algebra.compute.ComputeOptimizer:
                return self._get(self.type_.generated_offsets[14])

            def set_optimizer(self, v: algebra.compute.ComputeOptimizer) -> None:
                self._set(self.type_.generated_offsets[14], v)

            def lossLayer(self) -> algebra.compute.ComputeLayerLoss:
                return self._get(self.type_.generated_offsets[15])

            def set_lossLayer(self, v: algebra.compute.ComputeLayerLoss) -> None:
                self._set(self.type_.generated_offsets[15], v)

            def _lastLayer(self) -> str:
                return self._get(self.type_.generated_offsets[16])

            def set__lastLayer(self, v: str) -> None:
                self._set(self.type_.generated_offsets[16], v)

            def _lastOutput(self) -> str:
                return self._get(self.type_.generated_offsets[17])

            def set__lastOutput(self, v: str) -> None:
                self._set(self.type_.generated_offsets[17], v)

            @staticmethod
            def create(greycat: GreyCat, inputs: int, inputs_gradients: bool, outputs: int, fixed_batch_size: int, inputs_sequences: int, outputs_sequences: int, tensor_type: std.core.TensorType, seed: int, randomizeSeed: bool, layers: std.core.Array, preProcessType: algebra.nn.PreProcessType, preProcessObject: Any, postProcessType: algebra.nn.PostProcessType, postProcessObject: Any, optimizer: algebra.compute.ComputeOptimizer, lossLayer: algebra.compute.ComputeLayerLoss, _lastLayer: str, _lastOutput: str) -> algebra.nn.RegressionNetwork:
                return algebra.nn.RegressionNetwork(greycat.libs_by_name[algebra.name_].mapped[139], [inputs, inputs_gradients, outputs, fixed_batch_size, inputs_sequences, outputs_sequences, tensor_type, seed, randomizeSeed, layers, preProcessType, preProcessObject, postProcessType, postProcessObject, optimizer, lossLayer, _lastLayer, _lastOutput])

        @final
        class ComputeLayerTypes(GreyCat.Enum):
            name_: Final[str] = "nn::ComputeLayerTypes"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            @staticmethod
            def linear(greycat: GreyCat) -> algebra.nn.ComputeLayerTypes:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[140]
                return t.enum_values[t.generated_offsets[0]]

            @staticmethod
            def dense(greycat: GreyCat) -> algebra.nn.ComputeLayerTypes:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[140]
                return t.enum_values[t.generated_offsets[1]]

            @staticmethod
            def activation(greycat: GreyCat) -> algebra.nn.ComputeLayerTypes:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[140]
                return t.enum_values[t.generated_offsets[2]]

            @staticmethod
            def lstm(greycat: GreyCat) -> algebra.nn.ComputeLayerTypes:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[140]
                return t.enum_values[t.generated_offsets[3]]

            @staticmethod
            def loss(greycat: GreyCat) -> algebra.nn.ComputeLayerTypes:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[140]
                return t.enum_values[t.generated_offsets[4]]

            @staticmethod
            def filter(greycat: GreyCat) -> algebra.nn.ComputeLayerTypes:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[140]
                return t.enum_values[t.generated_offsets[5]]

            @staticmethod
            def create(greycat: GreyCat) -> algebra.nn.ComputeLayerTypes:
                return algebra.nn.ComputeLayerTypes(greycat.libs_by_name[algebra.name_].mapped[140], [])

        @final
        class InitializerConfig(GreyCat.Object):
            name_: Final[str] = "nn::InitializerConfig"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def weight_initializer(self) -> algebra.compute.ComputeInitializer:
                return self._get(self.type_.generated_offsets[0])

            def set_weight_initializer(self, v: algebra.compute.ComputeInitializer) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def weight_regularizer(self) -> algebra.compute.ComputeRegularizer:
                return self._get(self.type_.generated_offsets[1])

            def set_weight_regularizer(self, v: algebra.compute.ComputeRegularizer) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def bias_initializer(self) -> algebra.compute.ComputeInitializer:
                return self._get(self.type_.generated_offsets[2])

            def set_bias_initializer(self, v: algebra.compute.ComputeInitializer) -> None:
                self._set(self.type_.generated_offsets[2], v)

            def bias_regularizer(self) -> algebra.compute.ComputeRegularizer:
                return self._get(self.type_.generated_offsets[3])

            def set_bias_regularizer(self, v: algebra.compute.ComputeRegularizer) -> None:
                self._set(self.type_.generated_offsets[3], v)

            @staticmethod
            def create(greycat: GreyCat, weight_initializer: algebra.compute.ComputeInitializer, weight_regularizer: algebra.compute.ComputeRegularizer, bias_initializer: algebra.compute.ComputeInitializer, bias_regularizer: algebra.compute.ComputeRegularizer) -> algebra.nn.InitializerConfig:
                return algebra.nn.InitializerConfig(greycat.libs_by_name[algebra.name_].mapped[141], [weight_initializer, weight_regularizer, bias_initializer, bias_regularizer])

        @final
        class ClassificationMetrics(GreyCat.Object):
            name_: Final[str] = "nn::ClassificationMetrics"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def precision(self) -> std.core.Array:
                return self._get(self.type_.generated_offsets[0])

            def set_precision(self, v: std.core.Array) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def recall(self) -> std.core.Array:
                return self._get(self.type_.generated_offsets[1])

            def set_recall(self, v: std.core.Array) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def f1Score(self) -> std.core.Array:
                return self._get(self.type_.generated_offsets[2])

            def set_f1Score(self, v: std.core.Array) -> None:
                self._set(self.type_.generated_offsets[2], v)

            @staticmethod
            def create(greycat: GreyCat, precision: std.core.Array, recall: std.core.Array, f1Score: std.core.Array) -> algebra.nn.ClassificationMetrics:
                return algebra.nn.ClassificationMetrics(greycat.libs_by_name[algebra.name_].mapped[142], [precision, recall, f1Score])

    @final
    class kmeans:

        @final
        class KmeanResult(GreyCat.Object):
            name_: Final[str] = "kmeans::KmeanResult"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def loss(self) -> float:
                return self._get(self.type_.generated_offsets[0])

            def set_loss(self, v: float) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def roundsDistances(self) -> std.core.Array:
                return self._get(self.type_.generated_offsets[1])

            def set_roundsDistances(self, v: std.core.Array) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def centroids(self) -> std.core.Tensor:
                return self._get(self.type_.generated_offsets[2])

            def set_centroids(self, v: std.core.Tensor) -> None:
                self._set(self.type_.generated_offsets[2], v)

            def clusters_count(self) -> std.core.Tensor:
                return self._get(self.type_.generated_offsets[3])

            def set_clusters_count(self, v: std.core.Tensor) -> None:
                self._set(self.type_.generated_offsets[3], v)

            def clusters_sum_distance(self) -> std.core.Tensor:
                return self._get(self.type_.generated_offsets[4])

            def set_clusters_sum_distance(self, v: std.core.Tensor) -> None:
                self._set(self.type_.generated_offsets[4], v)

            def clusters_avg_distance(self) -> std.core.Tensor:
                return self._get(self.type_.generated_offsets[5])

            def set_clusters_avg_distance(self, v: std.core.Tensor) -> None:
                self._set(self.type_.generated_offsets[5], v)

            def assignement(self) -> std.core.Tensor:
                return self._get(self.type_.generated_offsets[6])

            def set_assignement(self, v: std.core.Tensor) -> None:
                self._set(self.type_.generated_offsets[6], v)

            def distances(self) -> std.core.Tensor:
                return self._get(self.type_.generated_offsets[7])

            def set_distances(self, v: std.core.Tensor) -> None:
                self._set(self.type_.generated_offsets[7], v)

            def clusterInterDistances(self) -> std.core.Tensor:
                return self._get(self.type_.generated_offsets[8])

            def set_clusterInterDistances(self, v: std.core.Tensor) -> None:
                self._set(self.type_.generated_offsets[8], v)

            @staticmethod
            def create(greycat: GreyCat, loss: float, roundsDistances: std.core.Array, centroids: std.core.Tensor, clusters_count: std.core.Tensor, clusters_sum_distance: std.core.Tensor, clusters_avg_distance: std.core.Tensor, assignement: std.core.Tensor, distances: std.core.Tensor, clusterInterDistances: std.core.Tensor) -> algebra.kmeans.KmeanResult:
                return algebra.kmeans.KmeanResult(greycat.libs_by_name[algebra.name_].mapped[143], [loss, roundsDistances, centroids, clusters_count, clusters_sum_distance, clusters_avg_distance, assignement, distances, clusterInterDistances])

        @final
        class Kmeans(GreyCat.Object):
            name_: Final[str] = "kmeans::Kmeans"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            @staticmethod
            def var_input(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[144]
                return t.static_values[0]

            @staticmethod
            def var_assignement(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[144]
                return t.static_values[1]

            @staticmethod
            def var_min_distance(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[144]
                return t.static_values[2]

            @staticmethod
            def varo_centroids(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[144]
                return t.static_values[3]

            @staticmethod
            def var_distance(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[144]
                return t.static_values[4]

            @staticmethod
            def var_sum_centroids(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[144]
                return t.static_values[5]

            @staticmethod
            def var_sum_min_distance(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[144]
                return t.static_values[6]

            @staticmethod
            def var_count_centroids(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[144]
                return t.static_values[7]

            @staticmethod
            def var_centroid_distances(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[144]
                return t.static_values[8]

            @staticmethod
            def var_sum_cluster_distances(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[144]
                return t.static_values[9]

            @staticmethod
            def var_avg_cluster_distances(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[144]
                return t.static_values[10]

            @staticmethod
            def var_count_cluster_distances(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[144]
                return t.static_values[11]

            @staticmethod
            def layer_placeholders(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[144]
                return t.static_values[12]

            @staticmethod
            def layer_forward(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[144]
                return t.static_values[13]

            @staticmethod
            def layer_backward(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[144]
                return t.static_values[14]

            @staticmethod
            def layer_init_round(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[144]
                return t.static_values[15]

            @staticmethod
            def layer_end_round(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[144]
                return t.static_values[16]

            @staticmethod
            def layer_stats(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[144]
                return t.static_values[17]

            @staticmethod
            def seq_init_round(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[144]
                return t.static_values[18]

            @staticmethod
            def seq_forward(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[144]
                return t.static_values[19]

            @staticmethod
            def seq_backward(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[144]
                return t.static_values[20]

            @staticmethod
            def seq_end_round(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[144]
                return t.static_values[21]

            @staticmethod
            def seq_stats(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[144]
                return t.static_values[22]

            @staticmethod
            def default_meta_rounds(greycat: GreyCat) -> int:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[144]
                return t.static_values[23]

            @staticmethod
            def default_rounds(greycat: GreyCat) -> int:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[144]
                return t.static_values[24]

            @staticmethod
            def create(greycat: GreyCat) -> algebra.kmeans.Kmeans:
                return algebra.kmeans.Kmeans(greycat.libs_by_name[algebra.name_].mapped[144], [])

        @final
        class KmeanMetaResult(GreyCat.Object):
            name_: Final[str] = "kmeans::KmeanMetaResult"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def runDistances(self) -> std.core.Array:
                return self._get(self.type_.generated_offsets[0])

            def set_runDistances(self, v: std.core.Array) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def bestResult(self) -> algebra.kmeans.KmeanResult:
                return self._get(self.type_.generated_offsets[1])

            def set_bestResult(self, v: algebra.kmeans.KmeanResult) -> None:
                self._set(self.type_.generated_offsets[1], v)

            @staticmethod
            def create(greycat: GreyCat, runDistances: std.core.Array, bestResult: algebra.kmeans.KmeanResult) -> algebra.kmeans.KmeanMetaResult:
                return algebra.kmeans.KmeanMetaResult(greycat.libs_by_name[algebra.name_].mapped[145], [runDistances, bestResult])

    @final
    class patterns:

        @final
        class EuclideanPatternDetector(GreyCat.Object):
            name_: Final[str] = "patterns::EuclideanPatternDetector"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            @staticmethod
            def create(greycat: GreyCat) -> algebra.patterns.EuclideanPatternDetector:
                return algebra.patterns.EuclideanPatternDetector(greycat.libs_by_name[algebra.name_].mapped[146], [])

        @final
        class Detection(GreyCat.Object):
            name_: Final[str] = "patterns::Detection"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def score(self) -> float:
                return self._get(self.type_.generated_offsets[0])

            def set_score(self, v: float) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def best_pattern(self) -> int:
                return self._get(self.type_.generated_offsets[1])

            def set_best_pattern(self, v: int) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def timespan(self) -> std.core.duration:
                return self._get(self.type_.generated_offsets[2])

            def set_timespan(self, v: std.core.duration) -> None:
                self._set(self.type_.generated_offsets[2], v)

            @staticmethod
            def create(greycat: GreyCat, score: float, best_pattern: int, timespan: std.core.duration) -> algebra.patterns.Detection:
                return algebra.patterns.Detection(greycat.libs_by_name[algebra.name_].mapped[147], [score, best_pattern, timespan])

        @final
        class ScoreDetails(GreyCat.Object):
            name_: Final[str] = "patterns::ScoreDetails"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def best_pattern(self) -> int:
                return self._get(self.type_.generated_offsets[0])

            def set_best_pattern(self, v: int) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def timespan(self) -> std.core.duration:
                return self._get(self.type_.generated_offsets[1])

            def set_timespan(self, v: std.core.duration) -> None:
                self._set(self.type_.generated_offsets[1], v)

            @staticmethod
            def create(greycat: GreyCat, best_pattern: int, timespan: std.core.duration) -> algebra.patterns.ScoreDetails:
                return algebra.patterns.ScoreDetails(greycat.libs_by_name[algebra.name_].mapped[148], [best_pattern, timespan])

        @final
        class RandomPatternDetector(GreyCat.Object):
            name_: Final[str] = "patterns::RandomPatternDetector"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            @staticmethod
            def create(greycat: GreyCat) -> algebra.patterns.RandomPatternDetector:
                return algebra.patterns.RandomPatternDetector(greycat.libs_by_name[algebra.name_].mapped[149], [])

        @final
        class PatternDetectionEngine(GreyCat.Object):
            name_: Final[str] = "patterns::PatternDetectionEngine"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def timeseries(self) -> std.core.nodeTime:
                return self._get(self.type_.generated_offsets[0])

            def set_timeseries(self, v: std.core.nodeTime) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def state(self) -> algebra.patterns.PatternDetectionEngineState:
                return self._get(self.type_.generated_offsets[1])

            def set_state(self, v: algebra.patterns.PatternDetectionEngineState) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def nullStrategy(self) -> algebra.patterns.PatternNullStrategy:
                return self._get(self.type_.generated_offsets[2])

            def set_nullStrategy(self, v: algebra.patterns.PatternNullStrategy) -> None:
                self._set(self.type_.generated_offsets[2], v)

            def nullReplaceConstant(self) -> float:
                return self._get(self.type_.generated_offsets[3])

            def set_nullReplaceConstant(self, v: float) -> None:
                self._set(self.type_.generated_offsets[3], v)

            def samplingPolicy(self) -> algebra.patterns.SamplingPolicy:
                return self._get(self.type_.generated_offsets[4])

            def set_samplingPolicy(self, v: algebra.patterns.SamplingPolicy) -> None:
                self._set(self.type_.generated_offsets[4], v)

            @staticmethod
            def create(greycat: GreyCat, timeseries: std.core.nodeTime, state: algebra.patterns.PatternDetectionEngineState, nullStrategy: algebra.patterns.PatternNullStrategy, nullReplaceConstant: float, samplingPolicy: algebra.patterns.SamplingPolicy) -> algebra.patterns.PatternDetectionEngine:
                return algebra.patterns.PatternDetectionEngine(greycat.libs_by_name[algebra.name_].mapped[150], [timeseries, state, nullStrategy, nullReplaceConstant, samplingPolicy])

        @final
        class PatternDetectors(GreyCat.Enum):
            name_: Final[str] = "patterns::PatternDetectors"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            @staticmethod
            def none(greycat: GreyCat) -> algebra.patterns.PatternDetectors:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[151]
                return t.enum_values[t.generated_offsets[0]]

            @staticmethod
            def euclidean(greycat: GreyCat) -> algebra.patterns.PatternDetectors:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[151]
                return t.enum_values[t.generated_offsets[1]]

            @staticmethod
            def fft(greycat: GreyCat) -> algebra.patterns.PatternDetectors:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[151]
                return t.enum_values[t.generated_offsets[2]]

            @staticmethod
            def dtw(greycat: GreyCat) -> algebra.patterns.PatternDetectors:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[151]
                return t.enum_values[t.generated_offsets[3]]

            @staticmethod
            def random(greycat: GreyCat) -> algebra.patterns.PatternDetectors:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[151]
                return t.enum_values[t.generated_offsets[4]]

            @staticmethod
            def sax(greycat: GreyCat) -> algebra.patterns.PatternDetectors:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[151]
                return t.enum_values[t.generated_offsets[5]]

            @staticmethod
            def create(greycat: GreyCat) -> algebra.patterns.PatternDetectors:
                return algebra.patterns.PatternDetectors(greycat.libs_by_name[algebra.name_].mapped[151], [])

        @final
        class PatternDetectionSensitivity(GreyCat.Object):
            name_: Final[str] = "patterns::PatternDetectionSensitivity"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def threshold(self) -> float:
                return self._get(self.type_.generated_offsets[0])

            def set_threshold(self, v: float) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def overlap(self) -> float:
                return self._get(self.type_.generated_offsets[1])

            def set_overlap(self, v: float) -> None:
                self._set(self.type_.generated_offsets[1], v)

            @staticmethod
            def create(greycat: GreyCat, threshold: float, overlap: float) -> algebra.patterns.PatternDetectionSensitivity:
                return algebra.patterns.PatternDetectionSensitivity(greycat.libs_by_name[algebra.name_].mapped[152], [threshold, overlap])

        @final
        class SaxPatternDetector(GreyCat.Object):
            name_: Final[str] = "patterns::SaxPatternDetector"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def alphabet_size(self) -> int:
                return self._get(self.type_.generated_offsets[0])

            def set_alphabet_size(self, v: int) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def fingerprint_length(self) -> int:
                return self._get(self.type_.generated_offsets[1])

            def set_fingerprint_length(self, v: int) -> None:
                self._set(self.type_.generated_offsets[1], v)

            @staticmethod
            def create(greycat: GreyCat, alphabet_size: int, fingerprint_length: int) -> algebra.patterns.SaxPatternDetector:
                return algebra.patterns.SaxPatternDetector(greycat.libs_by_name[algebra.name_].mapped[153], [alphabet_size, fingerprint_length])

        @final
        class DTWPatternDetectionEngine(GreyCat.Object):
            name_: Final[str] = "patterns::DTWPatternDetectionEngine"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def timeseries(self) -> std.core.nodeTime:
                return self._get(self.type_.generated_offsets[0])

            def set_timeseries(self, v: std.core.nodeTime) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def state(self) -> algebra.patterns.PatternDetectionEngineState:
                return self._get(self.type_.generated_offsets[1])

            def set_state(self, v: algebra.patterns.PatternDetectionEngineState) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def nullStrategy(self) -> algebra.patterns.PatternNullStrategy:
                return self._get(self.type_.generated_offsets[2])

            def set_nullStrategy(self, v: algebra.patterns.PatternNullStrategy) -> None:
                self._set(self.type_.generated_offsets[2], v)

            def nullReplaceConstant(self) -> float:
                return self._get(self.type_.generated_offsets[3])

            def set_nullReplaceConstant(self, v: float) -> None:
                self._set(self.type_.generated_offsets[3], v)

            def samplingPolicy(self) -> algebra.patterns.SamplingPolicy:
                return self._get(self.type_.generated_offsets[4])

            def set_samplingPolicy(self, v: algebra.patterns.SamplingPolicy) -> None:
                self._set(self.type_.generated_offsets[4], v)

            def std(self) -> float:
                return self._get(self.type_.generated_offsets[5])

            def set_std(self, v: float) -> None:
                self._set(self.type_.generated_offsets[5], v)

            def matchingNormalisation(self) -> algebra.patterns.MatchingNormalisation:
                return self._get(self.type_.generated_offsets[6])

            def set_matchingNormalisation(self, v: algebra.patterns.MatchingNormalisation) -> None:
                self._set(self.type_.generated_offsets[6], v)

            @staticmethod
            def create(greycat: GreyCat, timeseries: std.core.nodeTime, state: algebra.patterns.PatternDetectionEngineState, nullStrategy: algebra.patterns.PatternNullStrategy, nullReplaceConstant: float, samplingPolicy: algebra.patterns.SamplingPolicy, std: float, matchingNormalisation: algebra.patterns.MatchingNormalisation) -> algebra.patterns.DTWPatternDetectionEngine:
                return algebra.patterns.DTWPatternDetectionEngine(greycat.libs_by_name[algebra.name_].mapped[154], [timeseries, state, nullStrategy, nullReplaceConstant, samplingPolicy, std, matchingNormalisation])

        @final
        class EuclideanPatternDetectionEngine(GreyCat.Object):
            name_: Final[str] = "patterns::EuclideanPatternDetectionEngine"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def timeseries(self) -> std.core.nodeTime:
                return self._get(self.type_.generated_offsets[0])

            def set_timeseries(self, v: std.core.nodeTime) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def state(self) -> algebra.patterns.PatternDetectionEngineState:
                return self._get(self.type_.generated_offsets[1])

            def set_state(self, v: algebra.patterns.PatternDetectionEngineState) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def nullStrategy(self) -> algebra.patterns.PatternNullStrategy:
                return self._get(self.type_.generated_offsets[2])

            def set_nullStrategy(self, v: algebra.patterns.PatternNullStrategy) -> None:
                self._set(self.type_.generated_offsets[2], v)

            def nullReplaceConstant(self) -> float:
                return self._get(self.type_.generated_offsets[3])

            def set_nullReplaceConstant(self, v: float) -> None:
                self._set(self.type_.generated_offsets[3], v)

            def samplingPolicy(self) -> algebra.patterns.SamplingPolicy:
                return self._get(self.type_.generated_offsets[4])

            def set_samplingPolicy(self, v: algebra.patterns.SamplingPolicy) -> None:
                self._set(self.type_.generated_offsets[4], v)

            def pattern_tensors(self) -> std.core.Array:
                return self._get(self.type_.generated_offsets[5])

            def set_pattern_tensors(self, v: std.core.Array) -> None:
                self._set(self.type_.generated_offsets[5], v)

            def window_tensors(self) -> std.core.Array:
                return self._get(self.type_.generated_offsets[6])

            def set_window_tensors(self, v: std.core.Array) -> None:
                self._set(self.type_.generated_offsets[6], v)

            def std(self) -> float:
                return self._get(self.type_.generated_offsets[7])

            def set_std(self, v: float) -> None:
                self._set(self.type_.generated_offsets[7], v)

            def matchingNormalisation(self) -> algebra.patterns.MatchingNormalisation:
                return self._get(self.type_.generated_offsets[8])

            def set_matchingNormalisation(self, v: algebra.patterns.MatchingNormalisation) -> None:
                self._set(self.type_.generated_offsets[8], v)

            @staticmethod
            def create(greycat: GreyCat, timeseries: std.core.nodeTime, state: algebra.patterns.PatternDetectionEngineState, nullStrategy: algebra.patterns.PatternNullStrategy, nullReplaceConstant: float, samplingPolicy: algebra.patterns.SamplingPolicy, pattern_tensors: std.core.Array, window_tensors: std.core.Array, std: float, matchingNormalisation: algebra.patterns.MatchingNormalisation) -> algebra.patterns.EuclideanPatternDetectionEngine:
                return algebra.patterns.EuclideanPatternDetectionEngine(greycat.libs_by_name[algebra.name_].mapped[155], [timeseries, state, nullStrategy, nullReplaceConstant, samplingPolicy, pattern_tensors, window_tensors, std, matchingNormalisation])

        @final
        class ScoreDetailsSingleton(GreyCat.Object):
            name_: Final[str] = "patterns::ScoreDetailsSingleton"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def best_pattern(self) -> int:
                return self._get(self.type_.generated_offsets[0])

            def set_best_pattern(self, v: int) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def timespan(self) -> std.core.duration:
                return self._get(self.type_.generated_offsets[1])

            def set_timespan(self, v: std.core.duration) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def timestamp(self) -> std.core.time:
                return self._get(self.type_.generated_offsets[2])

            def set_timestamp(self, v: std.core.time) -> None:
                self._set(self.type_.generated_offsets[2], v)

            @staticmethod
            def create(greycat: GreyCat, best_pattern: int, timespan: std.core.duration, timestamp: std.core.time) -> algebra.patterns.ScoreDetailsSingleton:
                return algebra.patterns.ScoreDetailsSingleton(greycat.libs_by_name[algebra.name_].mapped[156], [best_pattern, timespan, timestamp])

        @final
        class PatternDetector(GreyCat.Object):
            name_: Final[str] = "patterns::PatternDetector"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            @staticmethod
            def create(greycat: GreyCat) -> algebra.patterns.PatternDetector:
                return algebra.patterns.PatternDetector(greycat.libs_by_name[algebra.name_].mapped[157], [])

        @final
        class PatternNullStrategy(GreyCat.Enum):
            name_: Final[str] = "patterns::PatternNullStrategy"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            @staticmethod
            def replace(greycat: GreyCat) -> algebra.patterns.PatternNullStrategy:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[158]
                return t.enum_values[t.generated_offsets[0]]

            @staticmethod
            def interpolate(greycat: GreyCat) -> algebra.patterns.PatternNullStrategy:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[158]
                return t.enum_values[t.generated_offsets[1]]

            @staticmethod
            def previous(greycat: GreyCat) -> algebra.patterns.PatternNullStrategy:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[158]
                return t.enum_values[t.generated_offsets[2]]

            @staticmethod
            def next(greycat: GreyCat) -> algebra.patterns.PatternNullStrategy:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[158]
                return t.enum_values[t.generated_offsets[3]]

            @staticmethod
            def none(greycat: GreyCat) -> algebra.patterns.PatternNullStrategy:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[158]
                return t.enum_values[t.generated_offsets[4]]

            @staticmethod
            def create(greycat: GreyCat) -> algebra.patterns.PatternNullStrategy:
                return algebra.patterns.PatternNullStrategy(greycat.libs_by_name[algebra.name_].mapped[158], [])

        @final
        class FFTResult(GreyCat.Object):
            name_: Final[str] = "patterns::FFTResult"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def distance(self) -> float:
                return self._get(self.type_.generated_offsets[0])

            def set_distance(self, v: float) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def best_pattern(self) -> int:
                return self._get(self.type_.generated_offsets[1])

            def set_best_pattern(self, v: int) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def best_timespan(self) -> std.core.duration:
                return self._get(self.type_.generated_offsets[2])

            def set_best_timespan(self, v: std.core.duration) -> None:
                self._set(self.type_.generated_offsets[2], v)

            @staticmethod
            def create(greycat: GreyCat, distance: float, best_pattern: int, best_timespan: std.core.duration) -> algebra.patterns.FFTResult:
                return algebra.patterns.FFTResult(greycat.libs_by_name[algebra.name_].mapped[159], [distance, best_pattern, best_timespan])

        @final
        class DTWPatternDetector(GreyCat.Object):
            name_: Final[str] = "patterns::DTWPatternDetector"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            @staticmethod
            def create(greycat: GreyCat) -> algebra.patterns.DTWPatternDetector:
                return algebra.patterns.DTWPatternDetector(greycat.libs_by_name[algebra.name_].mapped[160], [])

        @final
        class SamplingPolicy(GreyCat.Enum):
            name_: Final[str] = "patterns::SamplingPolicy"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            @staticmethod
            def as_is(greycat: GreyCat) -> algebra.patterns.SamplingPolicy:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[161]
                return t.enum_values[t.generated_offsets[0]]

            @staticmethod
            def average_frequency(greycat: GreyCat) -> algebra.patterns.SamplingPolicy:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[161]
                return t.enum_values[t.generated_offsets[1]]

            @staticmethod
            def highest_frequency(greycat: GreyCat) -> algebra.patterns.SamplingPolicy:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[161]
                return t.enum_values[t.generated_offsets[2]]

            @staticmethod
            def create(greycat: GreyCat) -> algebra.patterns.SamplingPolicy:
                return algebra.patterns.SamplingPolicy(greycat.libs_by_name[algebra.name_].mapped[161], [])

        @final
        class PatternDetectionEngineState(GreyCat.Object):
            name_: Final[str] = "patterns::PatternDetectionEngineState"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def hasScores(self) -> bool:
                return self._get(self.type_.generated_offsets[0])

            def set_hasScores(self, v: bool) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def hasDetections(self) -> bool:
                return self._get(self.type_.generated_offsets[1])

            def set_hasDetections(self, v: bool) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def patterns(self) -> std.core.Array:
                return self._get(self.type_.generated_offsets[2])

            def set_patterns(self, v: std.core.Array) -> None:
                self._set(self.type_.generated_offsets[2], v)

            def scores(self) -> std.core.nodeList:
                return self._get(self.type_.generated_offsets[3])

            def set_scores(self, v: std.core.nodeList) -> None:
                self._set(self.type_.generated_offsets[3], v)

            def detections(self) -> std.core.nodeTime:
                return self._get(self.type_.generated_offsets[4])

            def set_detections(self, v: std.core.nodeTime) -> None:
                self._set(self.type_.generated_offsets[4], v)

            @staticmethod
            def create(greycat: GreyCat, hasScores: bool, hasDetections: bool, patterns: std.core.Array, scores: std.core.nodeList, detections: std.core.nodeTime) -> algebra.patterns.PatternDetectionEngineState:
                return algebra.patterns.PatternDetectionEngineState(greycat.libs_by_name[algebra.name_].mapped[162], [hasScores, hasDetections, patterns, scores, detections])

        @final
        class FFTPatternDetector(GreyCat.Object):
            name_: Final[str] = "patterns::FFTPatternDetector"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            @staticmethod
            def create(greycat: GreyCat) -> algebra.patterns.FFTPatternDetector:
                return algebra.patterns.FFTPatternDetector(greycat.libs_by_name[algebra.name_].mapped[163], [])

        @final
        class DistanceMetrics(GreyCat.Object):
            name_: Final[str] = "patterns::DistanceMetrics"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            @staticmethod
            def create(greycat: GreyCat) -> algebra.patterns.DistanceMetrics:
                return algebra.patterns.DistanceMetrics(greycat.libs_by_name[algebra.name_].mapped[164], [])

        @final
        class OverlappingDetection(GreyCat.Object):
            name_: Final[str] = "patterns::OverlappingDetection"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def score(self) -> float:
                return self._get(self.type_.generated_offsets[0])

            def set_score(self, v: float) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def best_pattern(self) -> int:
                return self._get(self.type_.generated_offsets[1])

            def set_best_pattern(self, v: int) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def timespan(self) -> std.core.duration:
                return self._get(self.type_.generated_offsets[2])

            def set_timespan(self, v: std.core.duration) -> None:
                self._set(self.type_.generated_offsets[2], v)

            def overlap(self) -> std.core.duration:
                return self._get(self.type_.generated_offsets[3])

            def set_overlap(self, v: std.core.duration) -> None:
                self._set(self.type_.generated_offsets[3], v)

            @staticmethod
            def create(greycat: GreyCat, score: float, best_pattern: int, timespan: std.core.duration, overlap: std.core.duration) -> algebra.patterns.OverlappingDetection:
                return algebra.patterns.OverlappingDetection(greycat.libs_by_name[algebra.name_].mapped[165], [score, best_pattern, timespan, overlap])

        @final
        class RandomPatternDetectionEngine(GreyCat.Object):
            name_: Final[str] = "patterns::RandomPatternDetectionEngine"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def timeseries(self) -> std.core.nodeTime:
                return self._get(self.type_.generated_offsets[0])

            def set_timeseries(self, v: std.core.nodeTime) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def state(self) -> algebra.patterns.PatternDetectionEngineState:
                return self._get(self.type_.generated_offsets[1])

            def set_state(self, v: algebra.patterns.PatternDetectionEngineState) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def nullStrategy(self) -> algebra.patterns.PatternNullStrategy:
                return self._get(self.type_.generated_offsets[2])

            def set_nullStrategy(self, v: algebra.patterns.PatternNullStrategy) -> None:
                self._set(self.type_.generated_offsets[2], v)

            def nullReplaceConstant(self) -> float:
                return self._get(self.type_.generated_offsets[3])

            def set_nullReplaceConstant(self, v: float) -> None:
                self._set(self.type_.generated_offsets[3], v)

            def samplingPolicy(self) -> algebra.patterns.SamplingPolicy:
                return self._get(self.type_.generated_offsets[4])

            def set_samplingPolicy(self, v: algebra.patterns.SamplingPolicy) -> None:
                self._set(self.type_.generated_offsets[4], v)

            def rng(self) -> std.util.Random:
                return self._get(self.type_.generated_offsets[5])

            def set_rng(self, v: std.util.Random) -> None:
                self._set(self.type_.generated_offsets[5], v)

            @staticmethod
            def create(greycat: GreyCat, timeseries: std.core.nodeTime, state: algebra.patterns.PatternDetectionEngineState, nullStrategy: algebra.patterns.PatternNullStrategy, nullReplaceConstant: float, samplingPolicy: algebra.patterns.SamplingPolicy, rng: std.util.Random) -> algebra.patterns.RandomPatternDetectionEngine:
                return algebra.patterns.RandomPatternDetectionEngine(greycat.libs_by_name[algebra.name_].mapped[166], [timeseries, state, nullStrategy, nullReplaceConstant, samplingPolicy, rng])

        @final
        class SaxPatternDetectionEngine(GreyCat.Object):
            name_: Final[str] = "patterns::SaxPatternDetectionEngine"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def timeseries(self) -> std.core.nodeTime:
                return self._get(self.type_.generated_offsets[0])

            def set_timeseries(self, v: std.core.nodeTime) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def state(self) -> algebra.patterns.PatternDetectionEngineState:
                return self._get(self.type_.generated_offsets[1])

            def set_state(self, v: algebra.patterns.PatternDetectionEngineState) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def nullStrategy(self) -> algebra.patterns.PatternNullStrategy:
                return self._get(self.type_.generated_offsets[2])

            def set_nullStrategy(self, v: algebra.patterns.PatternNullStrategy) -> None:
                self._set(self.type_.generated_offsets[2], v)

            def nullReplaceConstant(self) -> float:
                return self._get(self.type_.generated_offsets[3])

            def set_nullReplaceConstant(self, v: float) -> None:
                self._set(self.type_.generated_offsets[3], v)

            def samplingPolicy(self) -> algebra.patterns.SamplingPolicy:
                return self._get(self.type_.generated_offsets[4])

            def set_samplingPolicy(self, v: algebra.patterns.SamplingPolicy) -> None:
                self._set(self.type_.generated_offsets[4], v)

            def alphabet_size(self) -> int:
                return self._get(self.type_.generated_offsets[5])

            def set_alphabet_size(self, v: int) -> None:
                self._set(self.type_.generated_offsets[5], v)

            def alphabet_boundaries(self) -> std.core.Array:
                return self._get(self.type_.generated_offsets[6])

            def set_alphabet_boundaries(self, v: std.core.Array) -> None:
                self._set(self.type_.generated_offsets[6], v)

            def lookup_table(self) -> std.core.nodeIndex:
                return self._get(self.type_.generated_offsets[7])

            def set_lookup_table(self, v: std.core.nodeIndex) -> None:
                self._set(self.type_.generated_offsets[7], v)

            def max_distance(self) -> float:
                return self._get(self.type_.generated_offsets[8])

            def set_max_distance(self, v: float) -> None:
                self._set(self.type_.generated_offsets[8], v)

            def pattern_fingerprints(self) -> std.core.Array:
                return self._get(self.type_.generated_offsets[9])

            def set_pattern_fingerprints(self, v: std.core.Array) -> None:
                self._set(self.type_.generated_offsets[9], v)

            def fingerprint_length(self) -> int:
                return self._get(self.type_.generated_offsets[10])

            def set_fingerprint_length(self, v: int) -> None:
                self._set(self.type_.generated_offsets[10], v)

            @staticmethod
            def alphabet(greycat: GreyCat) -> str:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[167]
                return t.static_values[0]

            @staticmethod
            def create(greycat: GreyCat, timeseries: std.core.nodeTime, state: algebra.patterns.PatternDetectionEngineState, nullStrategy: algebra.patterns.PatternNullStrategy, nullReplaceConstant: float, samplingPolicy: algebra.patterns.SamplingPolicy, alphabet_size: int, alphabet_boundaries: std.core.Array, lookup_table: std.core.nodeIndex, max_distance: float, pattern_fingerprints: std.core.Array, fingerprint_length: int) -> algebra.patterns.SaxPatternDetectionEngine:
                return algebra.patterns.SaxPatternDetectionEngine(greycat.libs_by_name[algebra.name_].mapped[167], [timeseries, state, nullStrategy, nullReplaceConstant, samplingPolicy, alphabet_size, alphabet_boundaries, lookup_table, max_distance, pattern_fingerprints, fingerprint_length])

        @final
        class MatchingNormalisation(GreyCat.Enum):
            name_: Final[str] = "patterns::MatchingNormalisation"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            @staticmethod
            def as_is(greycat: GreyCat) -> algebra.patterns.MatchingNormalisation:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[168]
                return t.enum_values[t.generated_offsets[0]]

            @staticmethod
            def shift(greycat: GreyCat) -> algebra.patterns.MatchingNormalisation:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[168]
                return t.enum_values[t.generated_offsets[1]]

            @staticmethod
            def scaling(greycat: GreyCat) -> algebra.patterns.MatchingNormalisation:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[168]
                return t.enum_values[t.generated_offsets[2]]

            @staticmethod
            def shift_and_scaling(greycat: GreyCat) -> algebra.patterns.MatchingNormalisation:
                t: Final[GreyCat.Type] = greycat.libs_by_name[algebra.name_].mapped[168]
                return t.enum_values[t.generated_offsets[3]]

            @staticmethod
            def create(greycat: GreyCat) -> algebra.patterns.MatchingNormalisation:
                return algebra.patterns.MatchingNormalisation(greycat.libs_by_name[algebra.name_].mapped[168], [])

    @final
    class ml:

        @final
        class HeatMapProfile(GreyCat.Object):
            name_: Final[str] = "ml::HeatMapProfile"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def counts(self) -> std.core.Table:
                return self._get(self.type_.generated_offsets[0])

            def set_counts(self, v: std.core.Table) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def x_labels(self) -> std.core.Array:
                return self._get(self.type_.generated_offsets[1])

            def set_x_labels(self, v: std.core.Array) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def y_labels(self) -> std.core.Array:
                return self._get(self.type_.generated_offsets[2])

            def set_y_labels(self, v: std.core.Array) -> None:
                self._set(self.type_.generated_offsets[2], v)

            def counts_max(self) -> int:
                return self._get(self.type_.generated_offsets[3])

            def set_counts_max(self, v: int) -> None:
                self._set(self.type_.generated_offsets[3], v)

            def counts_sum(self) -> int:
                return self._get(self.type_.generated_offsets[4])

            def set_counts_sum(self, v: int) -> None:
                self._set(self.type_.generated_offsets[4], v)

            @staticmethod
            def create(greycat: GreyCat, counts: std.core.Table, x_labels: std.core.Array, y_labels: std.core.Array, counts_max: int, counts_sum: int) -> algebra.ml.HeatMapProfile:
                return algebra.ml.HeatMapProfile(greycat.libs_by_name[algebra.name_].mapped[169], [counts, x_labels, y_labels, counts_max, counts_sum])

        @final
        class Polynomial(algebra_n.ml._Polynomial):
            name_: Final[str] = "ml::Polynomial"

            def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
                super().__init__(type)

            @staticmethod
            def create(greycat: GreyCat) -> algebra_n.ml._Polynomial:
                return algebra.ml.Polynomial(greycat.libs_by_name[algebra.name_].mapped[170], [])

        @final
        class Solver(GreyCat.Object):
            name_: Final[str] = "ml::Solver"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            @staticmethod
            def create(greycat: GreyCat) -> algebra.ml.Solver:
                return algebra.ml.Solver(greycat.libs_by_name[algebra.name_].mapped[171], [])

        @final
        class GaussianND(algebra_n.ml._GaussianND):
            name_: Final[str] = "ml::GaussianND"

            def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
                super().__init__(type)

            @staticmethod
            def create(greycat: GreyCat) -> algebra_n.ml._GaussianND:
                return algebra.ml.GaussianND(greycat.libs_by_name[algebra.name_].mapped[172], [])

        @final
        class PCA(algebra_n.ml._PCA):
            name_: Final[str] = "ml::PCA"

            def __init__(self, type: GreyCat.Type, _: list[Any] = []) -> None:
                super().__init__(type)

            @staticmethod
            def create(greycat: GreyCat) -> algebra_n.ml._PCA:
                return algebra.ml.PCA(greycat.libs_by_name[algebra.name_].mapped[173], [])

        @final
        class TimeSeriesDecomposition(GreyCat.Object):
            name_: Final[str] = "ml::TimeSeriesDecomposition"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            @staticmethod
            def create(greycat: GreyCat) -> algebra.ml.TimeSeriesDecomposition:
                return algebra.ml.TimeSeriesDecomposition(greycat.libs_by_name[algebra.name_].mapped[174], [])

    @final
    class transforms:

        @final
        class FFTModel(GreyCat.Object):
            name_: Final[str] = "transforms::FFTModel"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def nt(self) -> std.core.nodeTime:
                return self._get(self.type_.generated_offsets[0])

            def set_nt(self, v: std.core.nodeTime) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def sampling_step(self) -> std.core.duration:
                return self._get(self.type_.generated_offsets[1])

            def set_sampling_step(self, v: std.core.duration) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def time_complex(self) -> std.core.Tensor:
                return self._get(self.type_.generated_offsets[2])

            def set_time_complex(self, v: std.core.Tensor) -> None:
                self._set(self.type_.generated_offsets[2], v)

            def frequency_complex(self) -> std.core.Tensor:
                return self._get(self.type_.generated_offsets[3])

            def set_frequency_complex(self, v: std.core.Tensor) -> None:
                self._set(self.type_.generated_offsets[3], v)

            def frequency_table(self) -> std.core.Table:
                return self._get(self.type_.generated_offsets[4])

            def set_frequency_table(self, v: std.core.Table) -> None:
                self._set(self.type_.generated_offsets[4], v)

            def start_time(self) -> std.core.time:
                return self._get(self.type_.generated_offsets[5])

            def set_start_time(self, v: std.core.time) -> None:
                self._set(self.type_.generated_offsets[5], v)

            def best_size(self) -> int:
                return self._get(self.type_.generated_offsets[6])

            def set_best_size(self, v: int) -> None:
                self._set(self.type_.generated_offsets[6], v)

            @staticmethod
            def create(greycat: GreyCat, nt: std.core.nodeTime, sampling_step: std.core.duration, time_complex: std.core.Tensor, frequency_complex: std.core.Tensor, frequency_table: std.core.Table, start_time: std.core.time, best_size: int) -> algebra.transforms.FFTModel:
                return algebra.transforms.FFTModel(greycat.libs_by_name[algebra.name_].mapped[175], [nt, sampling_step, time_complex, frequency_complex, frequency_table, start_time, best_size])

    @final
    class powerflow:

        @final
        class PowerBusResult(GreyCat.Object):
            name_: Final[str] = "powerflow::PowerBusResult"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def abs(self) -> float:
                return self._get(self.type_.generated_offsets[0])

            def set_abs(self, v: float) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def angle_radians(self) -> float:
                return self._get(self.type_.generated_offsets[1])

            def set_angle_radians(self, v: float) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def voltage(self) -> float:
                return self._get(self.type_.generated_offsets[2])

            def set_voltage(self, v: float) -> None:
                self._set(self.type_.generated_offsets[2], v)

            def voltage_img(self) -> float:
                return self._get(self.type_.generated_offsets[3])

            def set_voltage_img(self, v: float) -> None:
                self._set(self.type_.generated_offsets[3], v)

            def current(self) -> float:
                return self._get(self.type_.generated_offsets[4])

            def set_current(self, v: float) -> None:
                self._set(self.type_.generated_offsets[4], v)

            def current_img(self) -> float:
                return self._get(self.type_.generated_offsets[5])

            def set_current_img(self, v: float) -> None:
                self._set(self.type_.generated_offsets[5], v)

            @staticmethod
            def create(greycat: GreyCat, abs: float, angle_radians: float, voltage: float, voltage_img: float, current: float, current_img: float) -> algebra.powerflow.PowerBusResult:
                return algebra.powerflow.PowerBusResult(greycat.libs_by_name[algebra.name_].mapped[176], [abs, angle_radians, voltage, voltage_img, current, current_img])

        @final
        class PowerLineResult(GreyCat.Object):
            name_: Final[str] = "powerflow::PowerLineResult"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def p_from_mw(self) -> float:
                return self._get(self.type_.generated_offsets[0])

            def set_p_from_mw(self, v: float) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def q_from_mvar(self) -> float:
                return self._get(self.type_.generated_offsets[1])

            def set_q_from_mvar(self, v: float) -> None:
                self._set(self.type_.generated_offsets[1], v)

            def p_to_mw(self) -> float:
                return self._get(self.type_.generated_offsets[2])

            def set_p_to_mw(self, v: float) -> None:
                self._set(self.type_.generated_offsets[2], v)

            def q_to_mvar(self) -> float:
                return self._get(self.type_.generated_offsets[3])

            def set_q_to_mvar(self, v: float) -> None:
                self._set(self.type_.generated_offsets[3], v)

            def pl_mw(self) -> float:
                return self._get(self.type_.generated_offsets[4])

            def set_pl_mw(self, v: float) -> None:
                self._set(self.type_.generated_offsets[4], v)

            def ql_mvar(self) -> float:
                return self._get(self.type_.generated_offsets[5])

            def set_ql_mvar(self, v: float) -> None:
                self._set(self.type_.generated_offsets[5], v)

            def i_from_ka(self) -> float:
                return self._get(self.type_.generated_offsets[6])

            def set_i_from_ka(self, v: float) -> None:
                self._set(self.type_.generated_offsets[6], v)

            def i_to_ka(self) -> float:
                return self._get(self.type_.generated_offsets[7])

            def set_i_to_ka(self, v: float) -> None:
                self._set(self.type_.generated_offsets[7], v)

            def i_ka(self) -> float:
                return self._get(self.type_.generated_offsets[8])

            def set_i_ka(self, v: float) -> None:
                self._set(self.type_.generated_offsets[8], v)

            def vm_from_pu(self) -> float:
                return self._get(self.type_.generated_offsets[9])

            def set_vm_from_pu(self, v: float) -> None:
                self._set(self.type_.generated_offsets[9], v)

            def vm_to_pu(self) -> float:
                return self._get(self.type_.generated_offsets[10])

            def set_vm_to_pu(self, v: float) -> None:
                self._set(self.type_.generated_offsets[10], v)

            def va_from_radians(self) -> float:
                return self._get(self.type_.generated_offsets[11])

            def set_va_from_radians(self, v: float) -> None:
                self._set(self.type_.generated_offsets[11], v)

            def va_to_radians(self) -> float:
                return self._get(self.type_.generated_offsets[12])

            def set_va_to_radians(self, v: float) -> None:
                self._set(self.type_.generated_offsets[12], v)

            def loading_percent(self) -> float:
                return self._get(self.type_.generated_offsets[13])

            def set_loading_percent(self, v: float) -> None:
                self._set(self.type_.generated_offsets[13], v)

            @staticmethod
            def create(greycat: GreyCat, p_from_mw: float, q_from_mvar: float, p_to_mw: float, q_to_mvar: float, pl_mw: float, ql_mvar: float, i_from_ka: float, i_to_ka: float, i_ka: float, vm_from_pu: float, vm_to_pu: float, va_from_radians: float, va_to_radians: float, loading_percent: float) -> algebra.powerflow.PowerLineResult:
                return algebra.powerflow.PowerLineResult(greycat.libs_by_name[algebra.name_].mapped[177], [p_from_mw, q_from_mvar, p_to_mw, q_to_mvar, pl_mw, ql_mvar, i_from_ka, i_to_ka, i_ka, vm_from_pu, vm_to_pu, va_from_radians, va_to_radians, loading_percent])

    def configure(self, loaders: dict[str, GreyCat.Loader], factories: dict[str, GreyCat.Factory]) -> None:
        factories[algebra.compute.ComputeOperationFill.name_] = lambda type, attributes: algebra.compute.ComputeOperationFill(type, attributes)
        factories[algebra.compute.ComputeRegressionLoss.name_] = lambda type, attributes: algebra.compute.ComputeRegressionLoss(type, attributes)
        factories[algebra.compute.ComputeOptimizerRmsProp.name_] = lambda type, attributes: algebra.compute.ComputeOptimizerRmsProp(type, attributes)
        factories[algebra.compute.ComputeInitializerReluUniform.name_] = lambda type, attributes: algebra.compute.ComputeInitializerReluUniform(type, attributes)
        factories[algebra.compute.ComputeOperationExp.name_] = lambda type, attributes: algebra.compute.ComputeOperationExp(type, attributes)
        factories[algebra.compute.ComputeInitializerNormalIn.name_] = lambda type, attributes: algebra.compute.ComputeInitializerNormalIn(type, attributes)
        factories[algebra.compute.ComputeInitializerNone.name_] = lambda type, attributes: algebra.compute.ComputeInitializerNone(type, attributes)
        factories[algebra.compute.ComputeOperationLeCunTanh.name_] = lambda type, attributes: algebra.compute.ComputeOperationLeCunTanh(type, attributes)
        factories[algebra.compute.ComputeOperationElu.name_] = lambda type, attributes: algebra.compute.ComputeOperationElu(type, attributes)
        factories[algebra.compute.ComputeOptimizerFtrl.name_] = lambda type, attributes: algebra.compute.ComputeOptimizerFtrl(type, attributes)
        factories[algebra.compute.ComputeActivationHardSigmoid.name_] = lambda type, attributes: algebra.compute.ComputeActivationHardSigmoid(type, attributes)
        factories[algebra.compute.ComputeInitializerSigmoidUniform.name_] = lambda type, attributes: algebra.compute.ComputeInitializerSigmoidUniform(type, attributes)
        factories[algebra.compute.ComputeInitializerUniformOut.name_] = lambda type, attributes: algebra.compute.ComputeInitializerUniformOut(type, attributes)
        factories[algebra.compute.ComputeOptimizer.name_] = lambda type, attributes: algebra.compute.ComputeOptimizer(type, attributes)
        factories[algebra.compute.ComputeActivationSigmoid.name_] = lambda type, attributes: algebra.compute.ComputeActivationSigmoid(type, attributes)
        factories[algebra.compute.ComputeOperationAvg.name_] = lambda type, attributes: algebra.compute.ComputeOperationAvg(type, attributes)
        factories[algebra.compute.ComputeLayerActivation.name_] = lambda type, attributes: algebra.compute.ComputeLayerActivation(type, attributes)
        factories[algebra.compute.ComputeLayerPCAScaler.name_] = lambda type, attributes: algebra.compute.ComputeLayerPCAScaler(type, attributes)
        factories[algebra.compute.ComputeLayerLSTM.name_] = lambda type, attributes: algebra.compute.ComputeLayerLSTM(type, attributes)
        factories[algebra.compute.ComputeVar.name_] = lambda type, attributes: algebra.compute.ComputeVar(type, attributes)
        factories[algebra.compute.ComputeOperationSelu.name_] = lambda type, attributes: algebra.compute.ComputeOperationSelu(type, attributes)
        factories[algebra.compute.ComputeOperationHardSigmoid.name_] = lambda type, attributes: algebra.compute.ComputeOperationHardSigmoid(type, attributes)
        factories[algebra.compute.ComputeOperationSin.name_] = lambda type, attributes: algebra.compute.ComputeOperationSin(type, attributes)
        factories[algebra.compute.ComputeOperationSoftSign.name_] = lambda type, attributes: algebra.compute.ComputeOperationSoftSign(type, attributes)
        factories[algebra.compute.ComputeLayerFilter.name_] = lambda type, attributes: algebra.compute.ComputeLayerFilter(type, attributes)
        factories[algebra.compute.ComputeOptimizerSgd.name_] = lambda type, attributes: algebra.compute.ComputeOptimizerSgd(type, attributes)
        factories[algebra.compute.ComputeVarProxy.name_] = lambda type, attributes: algebra.compute.ComputeVarProxy(type, attributes)
        factories[algebra.compute.ComputeActivationSelu.name_] = lambda type, attributes: algebra.compute.ComputeActivationSelu(type, attributes)
        factories[algebra.compute.ComputeOperationLog.name_] = lambda type, attributes: algebra.compute.ComputeOperationLog(type, attributes)
        factories[algebra.compute.ComputeInitializerIdentity.name_] = lambda type, attributes: algebra.compute.ComputeInitializerIdentity(type, attributes)
        factories[algebra.compute.ComputeInitializerGlorotUniform.name_] = lambda type, attributes: algebra.compute.ComputeInitializerGlorotUniform(type, attributes)
        factories[algebra.compute.ComputeActivationRelu.name_] = lambda type, attributes: algebra.compute.ComputeActivationRelu(type, attributes)
        factories[algebra.compute.ComputeActivationElu.name_] = lambda type, attributes: algebra.compute.ComputeActivationElu(type, attributes)
        factories[algebra.compute.ComputeOperationAcos.name_] = lambda type, attributes: algebra.compute.ComputeOperationAcos(type, attributes)
        factories[algebra.compute.ComputeLayerMinMaxScaler.name_] = lambda type, attributes: algebra.compute.ComputeLayerMinMaxScaler(type, attributes)
        factories[algebra.compute.ComputeActivationLeakyRelu.name_] = lambda type, attributes: algebra.compute.ComputeActivationLeakyRelu(type, attributes)
        factories[algebra.compute.ComputeInitializerRelu.name_] = lambda type, attributes: algebra.compute.ComputeInitializerRelu(type, attributes)
        factories[algebra.compute.ComputeActivationExp.name_] = lambda type, attributes: algebra.compute.ComputeActivationExp(type, attributes)
        factories[algebra.compute.ComputeInitializerPytorch.name_] = lambda type, attributes: algebra.compute.ComputeInitializerPytorch(type, attributes)
        factories[algebra.compute.ComputeOperationMul.name_] = lambda type, attributes: algebra.compute.ComputeOperationMul(type, attributes)
        factories[algebra.compute.ComputeOperationSign.name_] = lambda type, attributes: algebra.compute.ComputeOperationSign(type, attributes)
        factories[algebra.compute.ComputeOperationAtanh.name_] = lambda type, attributes: algebra.compute.ComputeOperationAtanh(type, attributes)
        factories[algebra.compute.ComputeCounter.name_] = lambda type, attributes: algebra.compute.ComputeCounter(type, attributes)
        factories[algebra.compute.ComputeOperationAddBias.name_] = lambda type, attributes: algebra.compute.ComputeOperationAddBias(type, attributes)
        factories[algebra.compute.ComputeInitializerUniformIn.name_] = lambda type, attributes: algebra.compute.ComputeInitializerUniformIn(type, attributes)
        factories[algebra.compute.ComputeLayerCall.name_] = lambda type, attributes: algebra.compute.ComputeLayerCall(type, attributes)
        factories[algebra.compute.ComputeOptimizerMomentum.name_] = lambda type, attributes: algebra.compute.ComputeOptimizerMomentum(type, attributes)
        factories[algebra.compute.ComputeOperationMatMul.name_] = lambda type, attributes: algebra.compute.ComputeOperationMatMul(type, attributes)
        factories[algebra.compute.ComputeOptimizerAdaDelta.name_] = lambda type, attributes: algebra.compute.ComputeOptimizerAdaDelta(type, attributes)
        factories[algebra.compute.ComputeOperationArg.name_] = lambda type, attributes: algebra.compute.ComputeOperationArg(type, attributes)
        factories[algebra.compute.ComputeLayer.name_] = lambda type, attributes: algebra.compute.ComputeLayer(type, attributes)
        factories[algebra.compute.ComputeInitializerNormalAvg.name_] = lambda type, attributes: algebra.compute.ComputeInitializerNormalAvg(type, attributes)
        factories[algebra.compute.ComputeOperationTan.name_] = lambda type, attributes: algebra.compute.ComputeOperationTan(type, attributes)
        factories[algebra.compute.ComputeOperationAsin.name_] = lambda type, attributes: algebra.compute.ComputeOperationAsin(type, attributes)
        factories[algebra.compute.ComputeInitializerUniform.name_] = lambda type, attributes: algebra.compute.ComputeInitializerUniform(type, attributes)
        factories[algebra.compute.ComputeOperationSum.name_] = lambda type, attributes: algebra.compute.ComputeOperationSum(type, attributes)
        factories[algebra.compute.ComputeLayerLoss.name_] = lambda type, attributes: algebra.compute.ComputeLayerLoss(type, attributes)
        factories[algebra.compute.ComputeOptimizerAdaMax.name_] = lambda type, attributes: algebra.compute.ComputeOptimizerAdaMax(type, attributes)
        factories[algebra.compute.ComputeOperationFilter.name_] = lambda type, attributes: algebra.compute.ComputeOperationFilter(type, attributes)
        factories[algebra.compute.ComputeEngine.name_] = lambda type, attributes: algebra.compute.ComputeEngine(type, attributes)
        loaders[algebra.compute.ComputeEngine.name_] = lambda type, stream: algebra_n.compute._ComputeEngine.load(type, stream)
        factories[algebra.compute.ComputeVarConst.name_] = lambda type, attributes: algebra.compute.ComputeVarConst(type, attributes)
        factories[algebra.compute.ComputeInitializer.name_] = lambda type, attributes: algebra.compute.ComputeInitializer(type, attributes)
        factories[algebra.compute.ComputeReduction.name_] = lambda type, attributes: algebra.compute.ComputeReduction(type, attributes)
        factories[algebra.compute.ComputeLayerDense.name_] = lambda type, attributes: algebra.compute.ComputeLayerDense(type, attributes)
        factories[algebra.compute.ComputeOperationSinh.name_] = lambda type, attributes: algebra.compute.ComputeOperationSinh(type, attributes)
        factories[algebra.compute.ComputeInitializerXavier.name_] = lambda type, attributes: algebra.compute.ComputeInitializerXavier(type, attributes)
        factories[algebra.compute.ComputeOperationLeakyRelu.name_] = lambda type, attributes: algebra.compute.ComputeOperationLeakyRelu(type, attributes)
        factories[algebra.compute.ComputeOperationDiv.name_] = lambda type, attributes: algebra.compute.ComputeOperationDiv(type, attributes)
        factories[algebra.compute.ComputeOperationSub.name_] = lambda type, attributes: algebra.compute.ComputeOperationSub(type, attributes)
        factories[algebra.compute.ComputeInitializerConstant.name_] = lambda type, attributes: algebra.compute.ComputeInitializerConstant(type, attributes)
        factories[algebra.compute.ComputeOperationAsinh.name_] = lambda type, attributes: algebra.compute.ComputeOperationAsinh(type, attributes)
        factories[algebra.compute.ComputeState.name_] = lambda type, attributes: algebra.compute.ComputeState(type, attributes)
        loaders[algebra.compute.ComputeState.name_] = lambda type, stream: algebra_n.compute._ComputeState.load(type, stream)
        factories[algebra.compute.ComputeOperationAbs.name_] = lambda type, attributes: algebra.compute.ComputeOperationAbs(type, attributes)
        factories[algebra.compute.ComputeRegularizer.name_] = lambda type, attributes: algebra.compute.ComputeRegularizer(type, attributes)
        factories[algebra.compute.ComputeOperationCos.name_] = lambda type, attributes: algebra.compute.ComputeOperationCos(type, attributes)
        factories[algebra.compute.ComputeOperationScale.name_] = lambda type, attributes: algebra.compute.ComputeOperationScale(type, attributes)
        factories[algebra.compute.ComputeActivationCelu.name_] = lambda type, attributes: algebra.compute.ComputeActivationCelu(type, attributes)
        factories[algebra.compute.ComputeActivation.name_] = lambda type, attributes: algebra.compute.ComputeActivation(type, attributes)
        factories[algebra.compute.ComputeOperationCelu.name_] = lambda type, attributes: algebra.compute.ComputeOperationCelu(type, attributes)
        factories[algebra.compute.ComputeOptimizerAdaGrad.name_] = lambda type, attributes: algebra.compute.ComputeOptimizerAdaGrad(type, attributes)
        factories[algebra.compute.ComputeOperationTanh.name_] = lambda type, attributes: algebra.compute.ComputeOperationTanh(type, attributes)
        factories[algebra.compute.ComputeVariable.name_] = lambda type, attributes: algebra.compute.ComputeVariable(type, attributes)
        factories[algebra.compute.ComputeActivationTanh.name_] = lambda type, attributes: algebra.compute.ComputeActivationTanh(type, attributes)
        factories[algebra.compute.ComputeOperation2In1Out.name_] = lambda type, attributes: algebra.compute.ComputeOperation2In1Out(type, attributes)
        factories[algebra.compute.ComputeOperationSumIf.name_] = lambda type, attributes: algebra.compute.ComputeOperationSumIf(type, attributes)
        factories[algebra.compute.ComputeOperation1In1Out.name_] = lambda type, attributes: algebra.compute.ComputeOperation1In1Out(type, attributes)
        factories[algebra.compute.ComputeOptimizerAdam.name_] = lambda type, attributes: algebra.compute.ComputeOptimizerAdam(type, attributes)
        factories[algebra.compute.ComputeVarOptimize.name_] = lambda type, attributes: algebra.compute.ComputeVarOptimize(type, attributes)
        factories[algebra.compute.ComputeOperationSoftplus.name_] = lambda type, attributes: algebra.compute.ComputeOperationSoftplus(type, attributes)
        factories[algebra.compute.ComputeActivationSoftmax.name_] = lambda type, attributes: algebra.compute.ComputeActivationSoftmax(type, attributes)
        factories[algebra.compute.ComputeOperationLogSoftmax.name_] = lambda type, attributes: algebra.compute.ComputeOperationLogSoftmax(type, attributes)
        factories[algebra.compute.ComputeLayerLossRegression.name_] = lambda type, attributes: algebra.compute.ComputeLayerLossRegression(type, attributes)
        factories[algebra.compute.ComputeActivationSoftSign.name_] = lambda type, attributes: algebra.compute.ComputeActivationSoftSign(type, attributes)
        factories[algebra.compute.ComputeOperationSigmoid.name_] = lambda type, attributes: algebra.compute.ComputeOperationSigmoid(type, attributes)
        factories[algebra.compute.ComputeOperationPow.name_] = lambda type, attributes: algebra.compute.ComputeOperationPow(type, attributes)
        factories[algebra.compute.ComputeOperationRaiseToPower.name_] = lambda type, attributes: algebra.compute.ComputeOperationRaiseToPower(type, attributes)
        factories[algebra.compute.ComputeOptimizerNesterov.name_] = lambda type, attributes: algebra.compute.ComputeOptimizerNesterov(type, attributes)
        factories[algebra.compute.ComputeLayerConfusion.name_] = lambda type, attributes: algebra.compute.ComputeLayerConfusion(type, attributes)
        factories[algebra.compute.ComputeLayerCustom.name_] = lambda type, attributes: algebra.compute.ComputeLayerCustom(type, attributes)
        factories[algebra.compute.ComputeOperationClip.name_] = lambda type, attributes: algebra.compute.ComputeOperationClip(type, attributes)
        factories[algebra.compute.ComputeModel.name_] = lambda type, attributes: algebra.compute.ComputeModel(type, attributes)
        factories[algebra.compute.ComputeLayerLinear.name_] = lambda type, attributes: algebra.compute.ComputeLayerLinear(type, attributes)
        factories[algebra.compute.ComputeOperationArgMax.name_] = lambda type, attributes: algebra.compute.ComputeOperationArgMax(type, attributes)
        factories[algebra.compute.ComputeOperationRelu.name_] = lambda type, attributes: algebra.compute.ComputeOperationRelu(type, attributes)
        factories[algebra.compute.ComputeLayerStandardScaler.name_] = lambda type, attributes: algebra.compute.ComputeLayerStandardScaler(type, attributes)
        factories[algebra.compute.ComputeActivationSoftplus.name_] = lambda type, attributes: algebra.compute.ComputeActivationSoftplus(type, attributes)
        factories[algebra.compute.ComputeOptimizerNadam.name_] = lambda type, attributes: algebra.compute.ComputeOptimizerNadam(type, attributes)
        factories[algebra.compute.ComputeOperationSqrt.name_] = lambda type, attributes: algebra.compute.ComputeOperationSqrt(type, attributes)
        factories[algebra.compute.ComputeInitializerNormal.name_] = lambda type, attributes: algebra.compute.ComputeInitializerNormal(type, attributes)
        factories[algebra.compute.ComputeInitializerUniformAvg.name_] = lambda type, attributes: algebra.compute.ComputeInitializerUniformAvg(type, attributes)
        factories[algebra.compute.ComputeInitializerLeCunUniform.name_] = lambda type, attributes: algebra.compute.ComputeInitializerLeCunUniform(type, attributes)
        factories[algebra.compute.ComputeOperationSoftmax.name_] = lambda type, attributes: algebra.compute.ComputeOperationSoftmax(type, attributes)
        factories[algebra.compute.ComputeOperationEuclidean.name_] = lambda type, attributes: algebra.compute.ComputeOperationEuclidean(type, attributes)
        factories[algebra.compute.ComputeLayerLossClassification.name_] = lambda type, attributes: algebra.compute.ComputeLayerLossClassification(type, attributes)
        factories[algebra.compute.ComputeOperationCosh.name_] = lambda type, attributes: algebra.compute.ComputeOperationCosh(type, attributes)
        factories[algebra.compute.ComputeInitializerLSTM.name_] = lambda type, attributes: algebra.compute.ComputeInitializerLSTM(type, attributes)
        factories[algebra.compute.ComputeBinding.name_] = lambda type, attributes: algebra.compute.ComputeBinding(type, attributes)
        factories[algebra.compute.ComputeInitializerNormalOut.name_] = lambda type, attributes: algebra.compute.ComputeInitializerNormalOut(type, attributes)
        factories[algebra.compute.ComputeClassificationLoss.name_] = lambda type, attributes: algebra.compute.ComputeClassificationLoss(type, attributes)
        factories[algebra.compute.ComputeOperationArgMin.name_] = lambda type, attributes: algebra.compute.ComputeOperationArgMin(type, attributes)
        factories[algebra.compute.ComputeOperation.name_] = lambda type, attributes: algebra.compute.ComputeOperation(type, attributes)
        factories[algebra.compute.ComputeOperationAcosh.name_] = lambda type, attributes: algebra.compute.ComputeOperationAcosh(type, attributes)
        factories[algebra.compute.ComputeOperationAtan.name_] = lambda type, attributes: algebra.compute.ComputeOperationAtan(type, attributes)
        factories[algebra.compute.ComputeOperationNeg.name_] = lambda type, attributes: algebra.compute.ComputeOperationNeg(type, attributes)
        factories[algebra.compute.ComputeOperationAdd.name_] = lambda type, attributes: algebra.compute.ComputeOperationAdd(type, attributes)
        factories[algebra.compute.ComputeInitializerXavierUniform.name_] = lambda type, attributes: algebra.compute.ComputeInitializerXavierUniform(type, attributes)
        factories[algebra.compute.ComputeLayerClassification.name_] = lambda type, attributes: algebra.compute.ComputeLayerClassification(type, attributes)
        factories[algebra.compute.ComputeLayerSeq.name_] = lambda type, attributes: algebra.compute.ComputeLayerSeq(type, attributes)
        factories[algebra.compute.ComputeVarInOut.name_] = lambda type, attributes: algebra.compute.ComputeVarInOut(type, attributes)
        factories[algebra.nn_layers_names.NNLayersNames.name_] = lambda type, attributes: algebra.nn_layers_names.NNLayersNames(type, attributes)
        factories[algebra.nn.ClassificationNetwork.name_] = lambda type, attributes: algebra.nn.ClassificationNetwork(type, attributes)
        factories[algebra.nn.ComputeOptimizers.name_] = lambda type, attributes: algebra.nn.ComputeOptimizers(type, attributes)
        factories[algebra.nn.BindingsResult.name_] = lambda type, attributes: algebra.nn.BindingsResult(type, attributes)
        factories[algebra.nn.PreProcessType.name_] = lambda type, attributes: algebra.nn.PreProcessType(type, attributes)
        factories[algebra.nn.PostProcessType.name_] = lambda type, attributes: algebra.nn.PostProcessType(type, attributes)
        factories[algebra.nn.AutoEncoderNetwork.name_] = lambda type, attributes: algebra.nn.AutoEncoderNetwork(type, attributes)
        factories[algebra.nn.ComputeActivations.name_] = lambda type, attributes: algebra.nn.ComputeActivations(type, attributes)
        factories[algebra.nn.ComputeInitializers.name_] = lambda type, attributes: algebra.nn.ComputeInitializers(type, attributes)
        factories[algebra.nn.NeuralNetwork.name_] = lambda type, attributes: algebra.nn.NeuralNetwork(type, attributes)
        factories[algebra.nn.RegressionNetwork.name_] = lambda type, attributes: algebra.nn.RegressionNetwork(type, attributes)
        factories[algebra.nn.ComputeLayerTypes.name_] = lambda type, attributes: algebra.nn.ComputeLayerTypes(type, attributes)
        factories[algebra.nn.InitializerConfig.name_] = lambda type, attributes: algebra.nn.InitializerConfig(type, attributes)
        factories[algebra.nn.ClassificationMetrics.name_] = lambda type, attributes: algebra.nn.ClassificationMetrics(type, attributes)
        factories[algebra.kmeans.KmeanResult.name_] = lambda type, attributes: algebra.kmeans.KmeanResult(type, attributes)
        factories[algebra.kmeans.Kmeans.name_] = lambda type, attributes: algebra.kmeans.Kmeans(type, attributes)
        factories[algebra.kmeans.KmeanMetaResult.name_] = lambda type, attributes: algebra.kmeans.KmeanMetaResult(type, attributes)
        factories[algebra.patterns.EuclideanPatternDetector.name_] = lambda type, attributes: algebra.patterns.EuclideanPatternDetector(type, attributes)
        factories[algebra.patterns.Detection.name_] = lambda type, attributes: algebra.patterns.Detection(type, attributes)
        factories[algebra.patterns.ScoreDetails.name_] = lambda type, attributes: algebra.patterns.ScoreDetails(type, attributes)
        factories[algebra.patterns.RandomPatternDetector.name_] = lambda type, attributes: algebra.patterns.RandomPatternDetector(type, attributes)
        factories[algebra.patterns.PatternDetectionEngine.name_] = lambda type, attributes: algebra.patterns.PatternDetectionEngine(type, attributes)
        factories[algebra.patterns.PatternDetectors.name_] = lambda type, attributes: algebra.patterns.PatternDetectors(type, attributes)
        factories[algebra.patterns.PatternDetectionSensitivity.name_] = lambda type, attributes: algebra.patterns.PatternDetectionSensitivity(type, attributes)
        factories[algebra.patterns.SaxPatternDetector.name_] = lambda type, attributes: algebra.patterns.SaxPatternDetector(type, attributes)
        factories[algebra.patterns.DTWPatternDetectionEngine.name_] = lambda type, attributes: algebra.patterns.DTWPatternDetectionEngine(type, attributes)
        factories[algebra.patterns.EuclideanPatternDetectionEngine.name_] = lambda type, attributes: algebra.patterns.EuclideanPatternDetectionEngine(type, attributes)
        factories[algebra.patterns.ScoreDetailsSingleton.name_] = lambda type, attributes: algebra.patterns.ScoreDetailsSingleton(type, attributes)
        factories[algebra.patterns.PatternDetector.name_] = lambda type, attributes: algebra.patterns.PatternDetector(type, attributes)
        factories[algebra.patterns.PatternNullStrategy.name_] = lambda type, attributes: algebra.patterns.PatternNullStrategy(type, attributes)
        factories[algebra.patterns.FFTResult.name_] = lambda type, attributes: algebra.patterns.FFTResult(type, attributes)
        factories[algebra.patterns.DTWPatternDetector.name_] = lambda type, attributes: algebra.patterns.DTWPatternDetector(type, attributes)
        factories[algebra.patterns.SamplingPolicy.name_] = lambda type, attributes: algebra.patterns.SamplingPolicy(type, attributes)
        factories[algebra.patterns.PatternDetectionEngineState.name_] = lambda type, attributes: algebra.patterns.PatternDetectionEngineState(type, attributes)
        factories[algebra.patterns.FFTPatternDetector.name_] = lambda type, attributes: algebra.patterns.FFTPatternDetector(type, attributes)
        factories[algebra.patterns.DistanceMetrics.name_] = lambda type, attributes: algebra.patterns.DistanceMetrics(type, attributes)
        factories[algebra.patterns.OverlappingDetection.name_] = lambda type, attributes: algebra.patterns.OverlappingDetection(type, attributes)
        factories[algebra.patterns.RandomPatternDetectionEngine.name_] = lambda type, attributes: algebra.patterns.RandomPatternDetectionEngine(type, attributes)
        factories[algebra.patterns.SaxPatternDetectionEngine.name_] = lambda type, attributes: algebra.patterns.SaxPatternDetectionEngine(type, attributes)
        factories[algebra.patterns.MatchingNormalisation.name_] = lambda type, attributes: algebra.patterns.MatchingNormalisation(type, attributes)
        factories[algebra.ml.HeatMapProfile.name_] = lambda type, attributes: algebra.ml.HeatMapProfile(type, attributes)
        factories[algebra.ml.Polynomial.name_] = lambda type, attributes: algebra.ml.Polynomial(type, attributes)
        loaders[algebra.ml.Polynomial.name_] = lambda type, stream: algebra_n.ml._Polynomial.load(type, stream)
        factories[algebra.ml.Solver.name_] = lambda type, attributes: algebra.ml.Solver(type, attributes)
        factories[algebra.ml.GaussianND.name_] = lambda type, attributes: algebra.ml.GaussianND(type, attributes)
        loaders[algebra.ml.GaussianND.name_] = lambda type, stream: algebra_n.ml._GaussianND.load(type, stream)
        factories[algebra.ml.PCA.name_] = lambda type, attributes: algebra.ml.PCA(type, attributes)
        loaders[algebra.ml.PCA.name_] = lambda type, stream: algebra_n.ml._PCA.load(type, stream)
        factories[algebra.ml.TimeSeriesDecomposition.name_] = lambda type, attributes: algebra.ml.TimeSeriesDecomposition(type, attributes)
        factories[algebra.transforms.FFTModel.name_] = lambda type, attributes: algebra.transforms.FFTModel(type, attributes)
        factories[algebra.powerflow.PowerBusResult.name_] = lambda type, attributes: algebra.powerflow.PowerBusResult(type, attributes)
        factories[algebra.powerflow.PowerLineResult.name_] = lambda type, attributes: algebra.powerflow.PowerLineResult(type, attributes)

    def init(self, greycat: GreyCat) -> None:
        self.mapped: list[GreyCat.Type] = [
            greycat.types_by_name[algebra.compute.ComputeOperationFill.name_],
            greycat.types_by_name[algebra.compute.ComputeRegressionLoss.name_],
            greycat.types_by_name[algebra.compute.ComputeOptimizerRmsProp.name_],
            greycat.types_by_name[algebra.compute.ComputeInitializerReluUniform.name_],
            greycat.types_by_name[algebra.compute.ComputeOperationExp.name_],
            greycat.types_by_name[algebra.compute.ComputeInitializerNormalIn.name_],
            greycat.types_by_name[algebra.compute.ComputeInitializerNone.name_],
            greycat.types_by_name[algebra.compute.ComputeOperationLeCunTanh.name_],
            greycat.types_by_name[algebra.compute.ComputeOperationElu.name_],
            greycat.types_by_name[algebra.compute.ComputeOptimizerFtrl.name_],
            greycat.types_by_name[algebra.compute.ComputeActivationHardSigmoid.name_],
            greycat.types_by_name[algebra.compute.ComputeInitializerSigmoidUniform.name_],
            greycat.types_by_name[algebra.compute.ComputeInitializerUniformOut.name_],
            greycat.types_by_name[algebra.compute.ComputeOptimizer.name_],
            greycat.types_by_name[algebra.compute.ComputeActivationSigmoid.name_],
            greycat.types_by_name[algebra.compute.ComputeOperationAvg.name_],
            greycat.types_by_name[algebra.compute.ComputeLayerActivation.name_],
            greycat.types_by_name[algebra.compute.ComputeLayerPCAScaler.name_],
            greycat.types_by_name[algebra.compute.ComputeLayerLSTM.name_],
            greycat.types_by_name[algebra.compute.ComputeVar.name_],
            greycat.types_by_name[algebra.compute.ComputeOperationSelu.name_],
            greycat.types_by_name[algebra.compute.ComputeOperationHardSigmoid.name_],
            greycat.types_by_name[algebra.compute.ComputeOperationSin.name_],
            greycat.types_by_name[algebra.compute.ComputeOperationSoftSign.name_],
            greycat.types_by_name[algebra.compute.ComputeLayerFilter.name_],
            greycat.types_by_name[algebra.compute.ComputeOptimizerSgd.name_],
            greycat.types_by_name[algebra.compute.ComputeVarProxy.name_],
            greycat.types_by_name[algebra.compute.ComputeActivationSelu.name_],
            greycat.types_by_name[algebra.compute.ComputeOperationLog.name_],
            greycat.types_by_name[algebra.compute.ComputeInitializerIdentity.name_],
            greycat.types_by_name[algebra.compute.ComputeInitializerGlorotUniform.name_],
            greycat.types_by_name[algebra.compute.ComputeActivationRelu.name_],
            greycat.types_by_name[algebra.compute.ComputeActivationElu.name_],
            greycat.types_by_name[algebra.compute.ComputeOperationAcos.name_],
            greycat.types_by_name[algebra.compute.ComputeLayerMinMaxScaler.name_],
            greycat.types_by_name[algebra.compute.ComputeActivationLeakyRelu.name_],
            greycat.types_by_name[algebra.compute.ComputeInitializerRelu.name_],
            greycat.types_by_name[algebra.compute.ComputeActivationExp.name_],
            greycat.types_by_name[algebra.compute.ComputeInitializerPytorch.name_],
            greycat.types_by_name[algebra.compute.ComputeOperationMul.name_],
            greycat.types_by_name[algebra.compute.ComputeOperationSign.name_],
            greycat.types_by_name[algebra.compute.ComputeOperationAtanh.name_],
            greycat.types_by_name[algebra.compute.ComputeCounter.name_],
            greycat.types_by_name[algebra.compute.ComputeOperationAddBias.name_],
            greycat.types_by_name[algebra.compute.ComputeInitializerUniformIn.name_],
            greycat.types_by_name[algebra.compute.ComputeLayerCall.name_],
            greycat.types_by_name[algebra.compute.ComputeOptimizerMomentum.name_],
            greycat.types_by_name[algebra.compute.ComputeOperationMatMul.name_],
            greycat.types_by_name[algebra.compute.ComputeOptimizerAdaDelta.name_],
            greycat.types_by_name[algebra.compute.ComputeOperationArg.name_],
            greycat.types_by_name[algebra.compute.ComputeLayer.name_],
            greycat.types_by_name[algebra.compute.ComputeInitializerNormalAvg.name_],
            greycat.types_by_name[algebra.compute.ComputeOperationTan.name_],
            greycat.types_by_name[algebra.compute.ComputeOperationAsin.name_],
            greycat.types_by_name[algebra.compute.ComputeInitializerUniform.name_],
            greycat.types_by_name[algebra.compute.ComputeOperationSum.name_],
            greycat.types_by_name[algebra.compute.ComputeLayerLoss.name_],
            greycat.types_by_name[algebra.compute.ComputeOptimizerAdaMax.name_],
            greycat.types_by_name[algebra.compute.ComputeOperationFilter.name_],
            greycat.types_by_name[algebra.compute.ComputeEngine.name_],
            greycat.types_by_name[algebra.compute.ComputeVarConst.name_],
            greycat.types_by_name[algebra.compute.ComputeInitializer.name_],
            greycat.types_by_name[algebra.compute.ComputeReduction.name_],
            greycat.types_by_name[algebra.compute.ComputeLayerDense.name_],
            greycat.types_by_name[algebra.compute.ComputeOperationSinh.name_],
            greycat.types_by_name[algebra.compute.ComputeInitializerXavier.name_],
            greycat.types_by_name[algebra.compute.ComputeOperationLeakyRelu.name_],
            greycat.types_by_name[algebra.compute.ComputeOperationDiv.name_],
            greycat.types_by_name[algebra.compute.ComputeOperationSub.name_],
            greycat.types_by_name[algebra.compute.ComputeInitializerConstant.name_],
            greycat.types_by_name[algebra.compute.ComputeOperationAsinh.name_],
            greycat.types_by_name[algebra.compute.ComputeState.name_],
            greycat.types_by_name[algebra.compute.ComputeOperationAbs.name_],
            greycat.types_by_name[algebra.compute.ComputeRegularizer.name_],
            greycat.types_by_name[algebra.compute.ComputeOperationCos.name_],
            greycat.types_by_name[algebra.compute.ComputeOperationScale.name_],
            greycat.types_by_name[algebra.compute.ComputeActivationCelu.name_],
            greycat.types_by_name[algebra.compute.ComputeActivation.name_],
            greycat.types_by_name[algebra.compute.ComputeOperationCelu.name_],
            greycat.types_by_name[algebra.compute.ComputeOptimizerAdaGrad.name_],
            greycat.types_by_name[algebra.compute.ComputeOperationTanh.name_],
            greycat.types_by_name[algebra.compute.ComputeVariable.name_],
            greycat.types_by_name[algebra.compute.ComputeActivationTanh.name_],
            greycat.types_by_name[algebra.compute.ComputeOperation2In1Out.name_],
            greycat.types_by_name[algebra.compute.ComputeOperationSumIf.name_],
            greycat.types_by_name[algebra.compute.ComputeOperation1In1Out.name_],
            greycat.types_by_name[algebra.compute.ComputeOptimizerAdam.name_],
            greycat.types_by_name[algebra.compute.ComputeVarOptimize.name_],
            greycat.types_by_name[algebra.compute.ComputeOperationSoftplus.name_],
            greycat.types_by_name[algebra.compute.ComputeActivationSoftmax.name_],
            greycat.types_by_name[algebra.compute.ComputeOperationLogSoftmax.name_],
            greycat.types_by_name[algebra.compute.ComputeLayerLossRegression.name_],
            greycat.types_by_name[algebra.compute.ComputeActivationSoftSign.name_],
            greycat.types_by_name[algebra.compute.ComputeOperationSigmoid.name_],
            greycat.types_by_name[algebra.compute.ComputeOperationPow.name_],
            greycat.types_by_name[algebra.compute.ComputeOperationRaiseToPower.name_],
            greycat.types_by_name[algebra.compute.ComputeOptimizerNesterov.name_],
            greycat.types_by_name[algebra.compute.ComputeLayerConfusion.name_],
            greycat.types_by_name[algebra.compute.ComputeLayerCustom.name_],
            greycat.types_by_name[algebra.compute.ComputeOperationClip.name_],
            greycat.types_by_name[algebra.compute.ComputeModel.name_],
            greycat.types_by_name[algebra.compute.ComputeLayerLinear.name_],
            greycat.types_by_name[algebra.compute.ComputeOperationArgMax.name_],
            greycat.types_by_name[algebra.compute.ComputeOperationRelu.name_],
            greycat.types_by_name[algebra.compute.ComputeLayerStandardScaler.name_],
            greycat.types_by_name[algebra.compute.ComputeActivationSoftplus.name_],
            greycat.types_by_name[algebra.compute.ComputeOptimizerNadam.name_],
            greycat.types_by_name[algebra.compute.ComputeOperationSqrt.name_],
            greycat.types_by_name[algebra.compute.ComputeInitializerNormal.name_],
            greycat.types_by_name[algebra.compute.ComputeInitializerUniformAvg.name_],
            greycat.types_by_name[algebra.compute.ComputeInitializerLeCunUniform.name_],
            greycat.types_by_name[algebra.compute.ComputeOperationSoftmax.name_],
            greycat.types_by_name[algebra.compute.ComputeOperationEuclidean.name_],
            greycat.types_by_name[algebra.compute.ComputeLayerLossClassification.name_],
            greycat.types_by_name[algebra.compute.ComputeOperationCosh.name_],
            greycat.types_by_name[algebra.compute.ComputeInitializerLSTM.name_],
            greycat.types_by_name[algebra.compute.ComputeBinding.name_],
            greycat.types_by_name[algebra.compute.ComputeInitializerNormalOut.name_],
            greycat.types_by_name[algebra.compute.ComputeClassificationLoss.name_],
            greycat.types_by_name[algebra.compute.ComputeOperationArgMin.name_],
            greycat.types_by_name[algebra.compute.ComputeOperation.name_],
            greycat.types_by_name[algebra.compute.ComputeOperationAcosh.name_],
            greycat.types_by_name[algebra.compute.ComputeOperationAtan.name_],
            greycat.types_by_name[algebra.compute.ComputeOperationNeg.name_],
            greycat.types_by_name[algebra.compute.ComputeOperationAdd.name_],
            greycat.types_by_name[algebra.compute.ComputeInitializerXavierUniform.name_],
            greycat.types_by_name[algebra.compute.ComputeLayerClassification.name_],
            greycat.types_by_name[algebra.compute.ComputeLayerSeq.name_],
            greycat.types_by_name[algebra.compute.ComputeVarInOut.name_],
            greycat.types_by_name[algebra.nn_layers_names.NNLayersNames.name_],
            greycat.types_by_name[algebra.nn.ClassificationNetwork.name_],
            greycat.types_by_name[algebra.nn.ComputeOptimizers.name_],
            greycat.types_by_name[algebra.nn.BindingsResult.name_],
            greycat.types_by_name[algebra.nn.PreProcessType.name_],
            greycat.types_by_name[algebra.nn.PostProcessType.name_],
            greycat.types_by_name[algebra.nn.AutoEncoderNetwork.name_],
            greycat.types_by_name[algebra.nn.ComputeActivations.name_],
            greycat.types_by_name[algebra.nn.ComputeInitializers.name_],
            greycat.types_by_name[algebra.nn.NeuralNetwork.name_],
            greycat.types_by_name[algebra.nn.RegressionNetwork.name_],
            greycat.types_by_name[algebra.nn.ComputeLayerTypes.name_],
            greycat.types_by_name[algebra.nn.InitializerConfig.name_],
            greycat.types_by_name[algebra.nn.ClassificationMetrics.name_],
            greycat.types_by_name[algebra.kmeans.KmeanResult.name_],
            greycat.types_by_name[algebra.kmeans.Kmeans.name_],
            greycat.types_by_name[algebra.kmeans.KmeanMetaResult.name_],
            greycat.types_by_name[algebra.patterns.EuclideanPatternDetector.name_],
            greycat.types_by_name[algebra.patterns.Detection.name_],
            greycat.types_by_name[algebra.patterns.ScoreDetails.name_],
            greycat.types_by_name[algebra.patterns.RandomPatternDetector.name_],
            greycat.types_by_name[algebra.patterns.PatternDetectionEngine.name_],
            greycat.types_by_name[algebra.patterns.PatternDetectors.name_],
            greycat.types_by_name[algebra.patterns.PatternDetectionSensitivity.name_],
            greycat.types_by_name[algebra.patterns.SaxPatternDetector.name_],
            greycat.types_by_name[algebra.patterns.DTWPatternDetectionEngine.name_],
            greycat.types_by_name[algebra.patterns.EuclideanPatternDetectionEngine.name_],
            greycat.types_by_name[algebra.patterns.ScoreDetailsSingleton.name_],
            greycat.types_by_name[algebra.patterns.PatternDetector.name_],
            greycat.types_by_name[algebra.patterns.PatternNullStrategy.name_],
            greycat.types_by_name[algebra.patterns.FFTResult.name_],
            greycat.types_by_name[algebra.patterns.DTWPatternDetector.name_],
            greycat.types_by_name[algebra.patterns.SamplingPolicy.name_],
            greycat.types_by_name[algebra.patterns.PatternDetectionEngineState.name_],
            greycat.types_by_name[algebra.patterns.FFTPatternDetector.name_],
            greycat.types_by_name[algebra.patterns.DistanceMetrics.name_],
            greycat.types_by_name[algebra.patterns.OverlappingDetection.name_],
            greycat.types_by_name[algebra.patterns.RandomPatternDetectionEngine.name_],
            greycat.types_by_name[algebra.patterns.SaxPatternDetectionEngine.name_],
            greycat.types_by_name[algebra.patterns.MatchingNormalisation.name_],
            greycat.types_by_name[algebra.ml.HeatMapProfile.name_],
            greycat.types_by_name[algebra.ml.Polynomial.name_],
            greycat.types_by_name[algebra.ml.Solver.name_],
            greycat.types_by_name[algebra.ml.GaussianND.name_],
            greycat.types_by_name[algebra.ml.PCA.name_],
            greycat.types_by_name[algebra.ml.TimeSeriesDecomposition.name_],
            greycat.types_by_name[algebra.transforms.FFTModel.name_],
            greycat.types_by_name[algebra.powerflow.PowerBusResult.name_],
            greycat.types_by_name[algebra.powerflow.PowerLineResult.name_],
        ]
        self.mapped[0].resolve_generated_offsets("input", "value")
        self.mapped[1].resolve_generated_offset_with_values("square", "Square", "abs", "Abs")
        self.mapped[2].resolve_generated_offsets("learning_rate", "decay_rate", "smooth_epsilon")
        self.mapped[2].static_values = [struct.unpack("d", struct.pack("l", 4562254508917369340))[0], struct.unpack("d", struct.pack("l", 4606281698874543309))[0], struct.unpack("d", struct.pack("l", 4502148214488346440))[0]]
        self.mapped[4].resolve_generated_offsets("input", "output")
        self.mapped[7].resolve_generated_offsets("input", "output")
        self.mapped[8].resolve_generated_offsets("input", "output", "alpha")
        self.mapped[8].static_values = [struct.unpack("d", struct.pack("l", 4607182418800017408))[0]]
        self.mapped[9].resolve_generated_offsets("learning_rate", "lambda1", "lambda2", "beta")
        self.mapped[9].static_values = [struct.unpack("d", struct.pack("l", 4562254508917369340))[0], struct.unpack("d", struct.pack("l", 0))[0], struct.unpack("d", struct.pack("l", 0))[0], struct.unpack("d", struct.pack("l", 0))[0]]
        self.mapped[10].resolve_generated_offsets("slope", "shift")
        self.mapped[10].static_values = [struct.unpack("d", struct.pack("l", 4596373779694328218))[0], struct.unpack("d", struct.pack("l", 4602678819172646912))[0]]
        self.mapped[13].resolve_generated_offsets("learning_rate")
        self.mapped[15].resolve_generated_offsets("input", "input2", "output")
        self.mapped[16].resolve_generated_offsets("name", "activation")
        self.mapped[16].static_values = ["input", "output"]
        self.mapped[17].resolve_generated_offsets("name", "type", "inverse_transform")
        self.mapped[17].static_values = ["input", "output", "avg", "std", "space"]
        self.mapped[18].resolve_generated_offsets("name", "bias_initializer", "weight_regularizer", "bias_regularizer", "type", "use_bias", "return_sequences", "bidirectional", "auto_init_states", "inputs", "outputs", "layers", "sequences")
        self.mapped[18].static_values = ["input", "output", "hx", "cx", "hy", "cy", "weight", "bias", "internal_i", "internal_f", "internal_cp", "internal_o", "internal_h", "internal_c", "internal_mult", "internal_output"]
        self.mapped[19].resolve_generated_offsets("name")
        self.mapped[20].resolve_generated_offsets("input", "output")
        self.mapped[21].resolve_generated_offsets("input", "output", "slope", "shift")
        self.mapped[21].static_values = [struct.unpack("d", struct.pack("l", 4596373779694328218))[0], struct.unpack("d", struct.pack("l", 4602678819172646912))[0]]
        self.mapped[22].resolve_generated_offsets("input", "output")
        self.mapped[23].resolve_generated_offsets("input", "output")
        self.mapped[24].resolve_generated_offsets("name", "type", "inputs", "outputs", "maskValues")
        self.mapped[24].static_values = ["input", "output", "mask"]
        self.mapped[25].resolve_generated_offsets("learning_rate")
        self.mapped[25].static_values = [struct.unpack("d", struct.pack("l", 4576918229304087675))[0]]
        self.mapped[26].resolve_generated_offsets("name")
        self.mapped[28].resolve_generated_offsets("input", "output")
        self.mapped[31].resolve_generated_offsets("max_value", "threshold")
        self.mapped[31].static_values = [struct.unpack("d", struct.pack("l", 0))[0]]
        self.mapped[32].resolve_generated_offsets("alpha")
        self.mapped[32].static_values = [struct.unpack("d", struct.pack("l", 4607182418800017408))[0]]
        self.mapped[33].resolve_generated_offsets("input", "output")
        self.mapped[34].resolve_generated_offsets("name", "type", "inverse_transform")
        self.mapped[34].static_values = ["input", "output", "min", "max"]
        self.mapped[35].resolve_generated_offsets("alpha", "max_value", "threshold")
        self.mapped[35].static_values = [struct.unpack("d", struct.pack("l", 4599075939470750515))[0], struct.unpack("d", struct.pack("l", 0))[0]]
        self.mapped[39].resolve_generated_offsets("input", "input2", "output")
        self.mapped[40].resolve_generated_offsets("input", "output")
        self.mapped[41].resolve_generated_offsets("input", "output")
        self.mapped[42].resolve_generated_offsets("epoch", "optimizationSteps", "batchNotOptimized")
        self.mapped[43].resolve_generated_offsets("input", "input2", "output")
        self.mapped[45].resolve_generated_offsets("layer_name", "bindings")
        self.mapped[46].resolve_generated_offsets("learning_rate", "decay_rate")
        self.mapped[46].static_values = [struct.unpack("d", struct.pack("l", 4562254508917369340))[0], struct.unpack("d", struct.pack("l", 4606281698874543309))[0]]
        self.mapped[47].resolve_generated_offsets("input", "input2", "output", "transposeA", "transposeB", "alpha", "beta")
        self.mapped[47].static_values = [false, struct.unpack("d", struct.pack("l", 4607182418800017408))[0], struct.unpack("d", struct.pack("l", 0))[0]]
        self.mapped[48].resolve_generated_offsets("learning_rate", "decay_rate", "smooth_epsilon")
        self.mapped[48].static_values = [struct.unpack("d", struct.pack("l", 4562254508917369340))[0], struct.unpack("d", struct.pack("l", 4606732058837280358))[0], struct.unpack("d", struct.pack("l", 4502148214488346440))[0]]
        self.mapped[49].resolve_generated_offsets("input", "output", "output2")
        self.mapped[50].resolve_generated_offsets("name")
        self.mapped[52].resolve_generated_offsets("input", "output")
        self.mapped[53].resolve_generated_offsets("input", "output")
        self.mapped[54].resolve_generated_offsets("min", "max")
        self.mapped[55].resolve_generated_offsets("input", "output", "axis")
        self.mapped[56].resolve_generated_offsets("name", "reduction")
        self.mapped[56].static_values = ["computed", "expected", "loss"]
        self.mapped[57].resolve_generated_offsets("learning_rate", "beta1", "beta2", "smooth_epsilon")
        self.mapped[57].static_values = [struct.unpack("d", struct.pack("l", 4562254508917369340))[0], struct.unpack("d", struct.pack("l", 4606281698874543309))[0], struct.unpack("d", struct.pack("l", 4607173411600762667))[0], struct.unpack("d", struct.pack("l", 4502148214488346440))[0]]
        self.mapped[58].resolve_generated_offsets("input", "output", "mask", "nbOutputs")
        self.mapped[60].resolve_generated_offsets("name", "type", "shape")
        self.mapped[62].resolve_generated_offset_with_values("auto", "auto", "none", "none", "sum", "sum", "mean", "mean", "disabled", "disabled")
        self.mapped[63].resolve_generated_offsets("name", "type", "inputs", "outputs", "use_bias", "weight_initializer", "weight_regularizer", "bias_initializer", "bias_regularizer", "activation")
        self.mapped[63].static_values = ["input", "output", "weight", "bias", "mult", "pre_activation"]
        self.mapped[64].resolve_generated_offsets("input", "output")
        self.mapped[66].resolve_generated_offsets("input", "output", "alpha", "max_value", "threshold")
        self.mapped[66].static_values = [struct.unpack("d", struct.pack("l", 4599075939470750515))[0], struct.unpack("d", struct.pack("l", 9218868437227405311))[0], struct.unpack("d", struct.pack("l", 0))[0]]
        self.mapped[67].resolve_generated_offsets("input", "input2", "output")
        self.mapped[68].resolve_generated_offsets("input", "input2", "output")
        self.mapped[69].resolve_generated_offsets("value")
        self.mapped[70].resolve_generated_offsets("input", "output")
        self.mapped[72].resolve_generated_offsets("input", "output")
        self.mapped[73].resolve_generated_offsets("l1", "l2")
        self.mapped[74].resolve_generated_offsets("input", "output")
        self.mapped[75].resolve_generated_offsets("input", "output", "alpha")
        self.mapped[76].resolve_generated_offsets("alpha")
        self.mapped[76].static_values = [struct.unpack("d", struct.pack("l", 4607182418800017408))[0]]
        self.mapped[78].resolve_generated_offsets("input", "output", "alpha")
        self.mapped[78].static_values = [struct.unpack("d", struct.pack("l", 4607182418800017408))[0]]
        self.mapped[79].resolve_generated_offsets("learning_rate", "initial_accumulator", "smooth_epsilon")
        self.mapped[79].static_values = [struct.unpack("d", struct.pack("l", 4562254508917369340))[0], struct.unpack("d", struct.pack("l", 4591870180066957722))[0], struct.unpack("d", struct.pack("l", 4502148214488346440))[0]]
        self.mapped[80].resolve_generated_offsets("input", "output")
        self.mapped[81].resolve_generated_offsets("name")
        self.mapped[83].resolve_generated_offsets("input", "input2", "output")
        self.mapped[84].resolve_generated_offsets("input", "ifCondition", "output", "counts", "classes")
        self.mapped[85].resolve_generated_offsets("input", "output")
        self.mapped[86].resolve_generated_offsets("learning_rate", "beta1", "beta2", "smooth_epsilon")
        self.mapped[86].static_values = [struct.unpack("d", struct.pack("l", 4562254508917369340))[0], struct.unpack("d", struct.pack("l", 4606281698874543309))[0], struct.unpack("d", struct.pack("l", 4607173411600762667))[0], struct.unpack("d", struct.pack("l", 4502148214488346440))[0]]
        self.mapped[87].resolve_generated_offsets("name", "type", "shape", "l1", "l2", "init")
        self.mapped[88].resolve_generated_offsets("input", "output")
        self.mapped[89].resolve_generated_offsets("classes")
        self.mapped[90].resolve_generated_offsets("input", "output", "axis")
        self.mapped[91].resolve_generated_offsets("name", "reduction", "loss_type")
        self.mapped[93].resolve_generated_offsets("input", "output")
        self.mapped[94].resolve_generated_offsets("input", "input2", "output")
        self.mapped[95].resolve_generated_offsets("input", "output", "power")
        self.mapped[96].resolve_generated_offsets("learning_rate", "decay_rate")
        self.mapped[96].static_values = [struct.unpack("d", struct.pack("l", 4562254508917369340))[0], struct.unpack("d", struct.pack("l", 4606281698874543309))[0]]
        self.mapped[97].resolve_generated_offsets("name", "nbClass")
        self.mapped[97].static_values = ["computed", "expected", "confusion"]
        self.mapped[98].resolve_generated_offsets("name", "ops", "vars")
        self.mapped[99].resolve_generated_offsets("input", "output", "min", "max")
        self.mapped[100].resolve_generated_offsets("layers")
        self.mapped[101].resolve_generated_offsets("name", "type", "inputs", "outputs", "use_bias", "weight_initializer", "weight_regularizer", "bias_initializer", "bias_regularizer")
        self.mapped[101].static_values = ["input", "output", "weight", "bias", "mult"]
        self.mapped[102].resolve_generated_offsets("input", "output", "output2")
        self.mapped[103].resolve_generated_offsets("input", "output", "max_value", "threshold")
        self.mapped[103].static_values = [struct.unpack("d", struct.pack("l", 0))[0]]
        self.mapped[104].resolve_generated_offsets("name", "type", "inverse_transform")
        self.mapped[104].static_values = ["input", "output", "avg", "std"]
        self.mapped[106].resolve_generated_offsets("learning_rate", "beta1", "beta2", "smooth_epsilon")
        self.mapped[106].static_values = [struct.unpack("d", struct.pack("l", 4562254508917369340))[0], struct.unpack("d", struct.pack("l", 4606281698874543309))[0], struct.unpack("d", struct.pack("l", 4607173411600762667))[0], struct.unpack("d", struct.pack("l", 4502148214488346440))[0]]
        self.mapped[107].resolve_generated_offsets("input", "output")
        self.mapped[108].resolve_generated_offsets("avg", "std")
        self.mapped[111].resolve_generated_offsets("input", "output")
        self.mapped[112].resolve_generated_offsets("input", "input2", "output")
        self.mapped[113].resolve_generated_offsets("name", "reduction", "loss_type", "has_class_weights", "calculate_probabilities", "from_logits")
        self.mapped[113].static_values = ["class_weights", "predicted_classes", "probabilities", "sum_reduce"]
        self.mapped[114].resolve_generated_offsets("input", "output")
        self.mapped[116].resolve_generated_offsets("src_layer_name", "src_var_name", "target_var_name")
        self.mapped[118].resolve_generated_offset_with_values("categorical_cross_entropy", "Categorical Cross Entropy", "sparse_categorical_cross_entropy", "Sparse Categorical Cross Entropy")
        self.mapped[119].resolve_generated_offsets("input", "output", "output2")
        self.mapped[121].resolve_generated_offsets("input", "output")
        self.mapped[122].resolve_generated_offsets("input", "output")
        self.mapped[123].resolve_generated_offsets("input", "output")
        self.mapped[124].resolve_generated_offsets("input", "input2", "output")
        self.mapped[126].resolve_generated_offsets("name", "calculate_probabilities", "from_logits")
        self.mapped[126].static_values = ["input", "predicted_classes", "probabilities"]
        self.mapped[127].resolve_generated_offsets("name", "calls", "optimizer")
        self.mapped[128].resolve_generated_offsets("name", "type", "shape", "with_grad")
        self.mapped[129].resolve_generated_offset_with_values("layer_0", "layer_0", "layer_1", "layer_1", "layer_2", "layer_2", "layer_3", "layer_3", "layer_4", "layer_4", "layer_5", "layer_5", "layer_6", "layer_6", "layer_7", "layer_7", "layer_8", "layer_8", "layer_9", "layer_9", "layer_10", "layer_10", "layer_11", "layer_11", "layer_12", "layer_12", "layer_13", "layer_13", "layer_14", "layer_14", "layer_15", "layer_15", "layer_16", "layer_16", "layer_17", "layer_17", "layer_18", "layer_18", "layer_19", "layer_19", "layer_20", "layer_20", "layer_21", "layer_21", "layer_22", "layer_22", "layer_23", "layer_23", "layer_24", "layer_24", "layer_25", "layer_25", "layer_26", "layer_26", "layer_27", "layer_27", "layer_28", "layer_28", "layer_29", "layer_29", "layer_30", "layer_30", "layer_31", "layer_31", "layer_32", "layer_32", "layer_33", "layer_33", "layer_34", "layer_34", "layer_35", "layer_35", "layer_36", "layer_36", "layer_37", "layer_37", "layer_38", "layer_38", "layer_39", "layer_39", "layer_40", "layer_40", "layer_41", "layer_41", "layer_42", "layer_42", "layer_43", "layer_43", "layer_44", "layer_44", "layer_45", "layer_45", "layer_46", "layer_46", "layer_47", "layer_47", "layer_48", "layer_48", "layer_49", "layer_49", "layer_50", "layer_50", "layer_51", "layer_51", "layer_52", "layer_52", "layer_53", "layer_53", "layer_54", "layer_54", "layer_55", "layer_55", "layer_56", "layer_56", "layer_57", "layer_57", "layer_58", "layer_58", "layer_59", "layer_59", "layer_60", "layer_60", "layer_61", "layer_61", "layer_62", "layer_62", "layer_63", "layer_63", "layer_64", "layer_64", "layer_65", "layer_65", "layer_66", "layer_66", "layer_67", "layer_67", "layer_68", "layer_68", "layer_69", "layer_69", "layer_70", "layer_70", "layer_71", "layer_71", "layer_72", "layer_72", "layer_73", "layer_73", "layer_74", "layer_74", "layer_75", "layer_75", "layer_76", "layer_76", "layer_77", "layer_77", "layer_78", "layer_78", "layer_79", "layer_79", "layer_80", "layer_80", "layer_81", "layer_81", "layer_82", "layer_82", "layer_83", "layer_83", "layer_84", "layer_84", "layer_85", "layer_85", "layer_86", "layer_86", "layer_87", "layer_87", "layer_88", "layer_88", "layer_89", "layer_89", "layer_90", "layer_90", "layer_91", "layer_91", "layer_92", "layer_92", "layer_93", "layer_93", "layer_94", "layer_94", "layer_95", "layer_95", "layer_96", "layer_96", "layer_97", "layer_97", "layer_98", "layer_98", "layer_99", "layer_99", "layer_100", "layer_100", "layer_101", "layer_101", "layer_102", "layer_102", "layer_103", "layer_103", "layer_104", "layer_104", "layer_105", "layer_105", "layer_106", "layer_106", "layer_107", "layer_107", "layer_108", "layer_108", "layer_109", "layer_109", "layer_110", "layer_110", "layer_111", "layer_111", "layer_112", "layer_112", "layer_113", "layer_113", "layer_114", "layer_114", "layer_115", "layer_115", "layer_116", "layer_116", "layer_117", "layer_117", "layer_118", "layer_118", "layer_119", "layer_119", "layer_120", "layer_120", "layer_121", "layer_121", "layer_122", "layer_122", "layer_123", "layer_123", "layer_124", "layer_124", "layer_125", "layer_125", "layer_126", "layer_126", "layer_127", "layer_127", "layer_128", "layer_128", "layer_129", "layer_129", "layer_130", "layer_130", "layer_131", "layer_131", "layer_132", "layer_132", "layer_133", "layer_133", "layer_134", "layer_134", "layer_135", "layer_135", "layer_136", "layer_136", "layer_137", "layer_137", "layer_138", "layer_138", "layer_139", "layer_139", "layer_140", "layer_140", "layer_141", "layer_141", "layer_142", "layer_142", "layer_143", "layer_143", "layer_144", "layer_144", "layer_145", "layer_145", "layer_146", "layer_146", "layer_147", "layer_147", "layer_148", "layer_148", "layer_149", "layer_149", "layer_150", "layer_150", "layer_151", "layer_151", "layer_152", "layer_152", "layer_153", "layer_153", "layer_154", "layer_154", "layer_155", "layer_155", "layer_156", "layer_156", "layer_157", "layer_157", "layer_158", "layer_158", "layer_159", "layer_159", "layer_160", "layer_160", "layer_161", "layer_161", "layer_162", "layer_162", "layer_163", "layer_163", "layer_164", "layer_164", "layer_165", "layer_165", "layer_166", "layer_166", "layer_167", "layer_167", "layer_168", "layer_168", "layer_169", "layer_169", "layer_170", "layer_170", "layer_171", "layer_171", "layer_172", "layer_172", "layer_173", "layer_173", "layer_174", "layer_174", "layer_175", "layer_175", "layer_176", "layer_176", "layer_177", "layer_177", "layer_178", "layer_178", "layer_179", "layer_179", "layer_180", "layer_180", "layer_181", "layer_181", "layer_182", "layer_182", "layer_183", "layer_183", "layer_184", "layer_184", "layer_185", "layer_185", "layer_186", "layer_186", "layer_187", "layer_187", "layer_188", "layer_188", "layer_189", "layer_189", "layer_190", "layer_190", "layer_191", "layer_191", "layer_192", "layer_192", "layer_193", "layer_193", "layer_194", "layer_194", "layer_195", "layer_195", "layer_196", "layer_196", "layer_197", "layer_197", "layer_198", "layer_198", "layer_199", "layer_199")
        self.mapped[130].resolve_generated_offsets("inputs", "inputs_gradients", "outputs", "fixed_batch_size", "inputs_sequences", "outputs_sequences", "tensor_type", "seed", "randomizeSeed", "layers", "preProcessType", "preProcessObject", "postProcessType", "postProcessObject", "optimizer", "lossLayer", "_lastLayer", "_lastOutput", "calculate_probabilities", "has_class_weights", "from_logits")
        self.mapped[131].resolve_generated_offset_with_values("ada_delta", "Ada Delta", "ada_grad", "Ada Grad", "adam", "Adam", "ada_max", "Ada Max", "nadam", "NAdam", "ftrl", "Ftrl", "sgd", "Stochastic Gradient Descent", "rms_prop", "RMS Prop", "momentum", "Momentum", "nesterov", "Nesterov")
        self.mapped[132].resolve_generated_offsets("previousLayerName", "previousLayerOutput", "expectedLayerName", "expectedLayerOutput", "postLayer")
        self.mapped[133].resolve_generated_offset_with_values("none", "None", "min_max_scaling", "Min/Max Scaling", "standard_scaling", "Standard Scaling", "pca_scaling", "PCA Scaling")
        self.mapped[134].resolve_generated_offset_with_values("none", "None", "min_max_scaling", "Min/Max Scaling", "standard_scaling", "Standard Scaling")
        self.mapped[135].resolve_generated_offsets("inputs", "inputs_gradients", "outputs", "fixed_batch_size", "inputs_sequences", "outputs_sequences", "tensor_type", "seed", "randomizeSeed", "layers", "preProcessType", "preProcessObject", "postProcessType", "postProcessObject", "optimizer", "lossLayer", "_lastLayer", "_lastOutput", "encoder_layer_idx", "encoder_layer_name", "encoder_layer_var")
        self.mapped[136].resolve_generated_offset_with_values("relu", "Relu", "leaky_relu", "Leaky Relu", "sigmoid", "Sigmoid", "hard_sigmoid", "Hard Sigmoid", "exp", "Exp", "soft_max", "Soft Max", "soft_plus", "Soft Plus", "soft_sign", "Soft Sign", "tanh", "Tanh", "selu", "Selu", "elu", "Elu", "celu", "Celu")
        self.mapped[137].resolve_generated_offset_with_values("none", "None", "constant", "Constant", "sigmoid_uniform", "SigmoidUniform", "lecun_uniform", "LeCunUniform", "xavier", "Xavier", "xavier_uniform", "XavierUniform", "relu", "Relu", "relu_uniform", "ReluUniform", "normal", "Normal", "normal_in", "NormalIn", "normal_out", "NormalOut", "normal_avg", "NormalAvg", "uniform", "Uniform", "uniform_in", "UniformIn", "uniform_out", "UniformOut", "uniform_avg", "UniformAvg", "identity", "Identity", "pytorch", "Pytorch")
        self.mapped[138].resolve_generated_offsets("inputs", "inputs_gradients", "outputs", "fixed_batch_size", "inputs_sequences", "outputs_sequences", "tensor_type", "seed", "randomizeSeed", "layers", "preProcessType", "preProcessObject", "postProcessType", "postProcessObject", "optimizer", "lossLayer", "_lastLayer", "_lastOutput")
        self.mapped[138].static_values = ["Inputs or outputs can't be negative", "Last layer has different number of outputs than declared", "Incompatible loss function", "Some NN layers are not currently supported", "Tensor Type not currently supported", "NN should contain at least 1 layer", "layer placeholders", "layer classification", "layer preprocess", "layer postprocess learn", "layer main", "layer loss learn", "layer loss display", "layer postprocess display", "layer confusion", "seq predict", "seq postprocess", "seq learn", "seq loss display", "seq encode", "seq decode", "seq confusion", "var input", "var enc input", "var targets", "var Classifier classes", "var Classifier probabilities", "var Classifier class weights", "var Classifier confusion", "var input avg", "var input min", "var input max", "var input std", "var input space", "var output avg", "var output min", "var output max", "var output std"]
        self.mapped[139].resolve_generated_offsets("inputs", "inputs_gradients", "outputs", "fixed_batch_size", "inputs_sequences", "outputs_sequences", "tensor_type", "seed", "randomizeSeed", "layers", "preProcessType", "preProcessObject", "postProcessType", "postProcessObject", "optimizer", "lossLayer", "_lastLayer", "_lastOutput")
        self.mapped[140].resolve_generated_offset_with_values("linear", "Linear", "dense", "Dense", "activation", "Activation", "lstm", "LSTM", "loss", "Loss", "filter", "Filter")
        self.mapped[141].resolve_generated_offsets("weight_initializer", "weight_regularizer", "bias_initializer", "bias_regularizer")
        self.mapped[142].resolve_generated_offsets("precision", "recall", "f1Score")
        self.mapped[143].resolve_generated_offsets("loss", "roundsDistances", "centroids", "clusters_count", "clusters_sum_distance", "clusters_avg_distance", "assignement", "distances", "clusterInterDistances")
        self.mapped[144].static_values = ["input", "assignement", "min_distance", "centroids", "distance", "sum_centroids", "sum_min_distance", "count_centroids", "centroid_distances", "sum_cluster_distances", "avg_cluster_distances", "count_cluster_distances", "placeholders", "kmeans_forward", "kmeans_backward", "kmeans_init_round", "kmeans_end_round", "kmeans_stats_layer", "kmeans_init_round_seq", "kmeans_forward_seq", "kmeans_backward_seq", "kmeans_end_round_seq", "kmeans_stats_seq", 100, 20]
        self.mapped[145].resolve_generated_offsets("runDistances", "bestResult")
        self.mapped[147].resolve_generated_offsets("score", "best_pattern", "timespan")
        self.mapped[148].resolve_generated_offsets("best_pattern", "timespan")
        self.mapped[150].resolve_generated_offsets("timeseries", "state", "nullStrategy", "nullReplaceConstant", "samplingPolicy")
        self.mapped[151].resolve_generated_offset_with_values("none", "None", "euclidean", "Euclidean", "fft", "FFT", "dtw", "DTW", "random", "Random", "sax", "SAX")
        self.mapped[152].resolve_generated_offsets("threshold", "overlap")
        self.mapped[153].resolve_generated_offsets("alphabet_size", "fingerprint_length")
        self.mapped[154].resolve_generated_offsets("timeseries", "state", "nullStrategy", "nullReplaceConstant", "samplingPolicy", "std", "matchingNormalisation")
        self.mapped[155].resolve_generated_offsets("timeseries", "state", "nullStrategy", "nullReplaceConstant", "samplingPolicy", "pattern_tensors", "window_tensors", "std", "matchingNormalisation")
        self.mapped[156].resolve_generated_offsets("best_pattern", "timespan", "timestamp")
        self.mapped[158].resolve_generated_offset_with_values("replace", "Replace", "interpolate", "Interpolate", "previous", "Previous", "next", "Next", "none", "None")
        self.mapped[159].resolve_generated_offsets("distance", "best_pattern", "best_timespan")
        self.mapped[161].resolve_generated_offset_with_values("as_is", "As-is", "average_frequency", "Average frequency", "highest_frequency", "Highest frequency")
        self.mapped[162].resolve_generated_offsets("hasScores", "hasDetections", "patterns", "scores", "detections")
        self.mapped[165].resolve_generated_offsets("score", "best_pattern", "timespan", "overlap")
        self.mapped[166].resolve_generated_offsets("timeseries", "state", "nullStrategy", "nullReplaceConstant", "samplingPolicy", "rng")
        self.mapped[167].resolve_generated_offsets("timeseries", "state", "nullStrategy", "nullReplaceConstant", "samplingPolicy", "alphabet_size", "alphabet_boundaries", "lookup_table", "max_distance", "pattern_fingerprints", "fingerprint_length")
        self.mapped[167].static_values = ["ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz"]
        self.mapped[168].resolve_generated_offset_with_values("as_is", "As-is", "shift", "Vertical shift", "scaling", "Vertical scaling", "shift_and_scaling", "Vertical shift and scaling")
        self.mapped[169].resolve_generated_offsets("counts", "x_labels", "y_labels", "counts_max", "counts_sum")
        self.mapped[173].static_values = [struct.unpack("d", struct.pack("l", 4606732058837280358))[0]]
        self.mapped[175].resolve_generated_offsets("nt", "sampling_step", "time_complex", "frequency_complex", "frequency_table", "start_time", "best_size")
        self.mapped[176].resolve_generated_offsets("abs", "angle_radians", "voltage", "voltage_img", "current", "current_img")
        self.mapped[177].resolve_generated_offsets("p_from_mw", "q_from_mvar", "p_to_mw", "q_to_mvar", "pl_mw", "ql_mvar", "i_from_ka", "i_to_ka", "i_ka", "vm_from_pu", "vm_to_pu", "va_from_radians", "va_to_radians", "loading_percent")
