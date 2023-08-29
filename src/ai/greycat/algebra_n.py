from __future__ import annotations
from ctypes import *
from typing import *

from ai.greycat.greycat import GreyCat, PrimitiveType
from ai.greycat.std_n import std_n
core = std_n.core

T = TypeVar('T')
U = TypeVar('U')


class algebra_n:
    class powerflow:
        class PowerNetwork(GreyCat.Object):
            def __init__(self: algebra_n.powerflow.PowerNetwork, type: GreyCat.Type) -> None:
                super(type, None)
                raise NotImplementedError

            def load(type: GreyCat.Type, stream: GreyCat._Stream) -> object:
                raise NotImplementedError

    class compute:
        class ComputeState(GreyCat.Object):
            def __init__(self: algebra_n.compute.ComputeState, type: GreyCat.Type) -> None:
                super(type, None)
                raise NotImplementedError

            def load(type: GreyCat.Type, stream: GreyCat._Stream) -> object:
                raise NotImplementedError

        class ComputeEngine(GreyCat.Object):
            def __init__(self: algebra_n.compute.ComputeEngine, type: GreyCat.Type) -> None:
                super(type, None)
                raise NotImplementedError

            def load(type: GreyCat.Type, stream: GreyCat._Stream) -> object:
                raise NotImplementedError

    class ml:
        class Polynomial(GreyCat.Object):
            def __init__(self: algebra_n.ml.Polynomial, type: GreyCat.Type) -> None:
                super(type, None)
                self.degree: c_byte
                self.x_start: c_double
                self.x_step: c_double
                self.tensor_type: c_byte
                self.data: bytes

            def _save(self: algebra_n.ml.Polynomial, stream: GreyCat._Stream) -> None:
                stream.write_i8(PrimitiveType.OBJECT)
                stream.write_i32(self.type_.offset)
                stream.write_i8(self.degree)
                stream.write_i64(c_int64(len(self.data)))
                stream.write_f64(self.x_start)
                stream.write_f64(self.x_step)
                stream.write_i8(self.tensor_type)
                stream.write_i8_array(self.data, 0, len(self.data))

            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat._Stream) -> object:
                degree: c_byte = stream.read_i8()
                coefficientSize: int = stream.read_i64().value
                xStart: c_double = stream.read_f64()
                xStep: c_double = stream.read_f64()
                tensorType: c_byte = stream.read_i8()
                data: bytes = stream.read_i8_array(coefficientSize)
                poly: algebra_n.ml.Polynomial = type.factory(type)
                poly.degree = degree
                poly.x_start = xStart
                poly.x_step = xStep
                poly.tensor_type = tensorType
                poly.data = data
                return poly

        class PCA(GreyCat.Object):
            def __init__(self: algebra_n.ml.PCA, type: GreyCat.Type) -> None:
                super(type, None)
                self.__bestDim: c_int32
                self.__selectedDim: c_int32
                self.__threshold: c_double
                self.__eigenVectors: core.Tensor
                self.__eigenValues: core.Tensor
                self.__avg: core.Tensor
                self.__std: core.Tensor
                self.__correlation: core.Tensor
                self.__explainedVariance: core.Tensor
                self.__spaceOrigin: core.Tensor
                self.__spaceCropped: core.Tensor
                self.__dimInfo: core.Tensor

            def _save(self: algebra_n.ml.PCA, stream: GreyCat._Stream) -> None:
                stream.write_i8(PrimitiveType.OBJECT)
                stream.write_i32(self.type_.offset)
                stream.write_i32(self.__bestDim)
                stream.write_i32(self.__selectedDim)
                stream.write_f64(self.__threshold)
                stream.write_object(self.__eigenVectors)
                stream.write_object(self.__eigenValues)
                stream.write_object(self.__avg)
                stream.write_object(self.__std)
                stream.write_object(self.__correlation)
                stream.write_object(self.__explainedVariance)
                stream.write_object(self.__spaceOrigin)
                stream.write_object(self.__spaceCropped)
                stream.write_object(self.__dimInfo)

            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat._Stream) -> object:
                bestDim: c_int32 = stream.read_i32()
                selectedDim: c_int32 = stream.read_i32()
                threshold: c_double = stream.read_f64()
                eigenVectors: core.Tensor = stream.read_object()
                eigenValues: core.Tensor = stream.read_object()
                avg: core.Tensor = stream.read_object()
                std: core.Tensor = stream.read_object()
                correlation: core.Tensor = stream.read_object()
                explainedVariance: core.Tensor = stream.read_object()
                spaceOrigin: core.Tensor = stream.read_object()
                spaceCropped: core.Tensor = stream.read_object()
                dimInfo: core.Tensor = stream.read_object()
                pca: algebra_n.ml.PCA = type.factory(type)
                pca.__bestDim = bestDim
                pca.__selectedDim = selectedDim
                pca.__threshold = threshold
                pca.__eigenVectors = eigenVectors
                pca.__eigenValues = eigenValues
                pca.__avg = avg
                pca.__std = std
                pca.__correlation = correlation
                pca.__explainedVariance = explainedVariance
                pca.__spaceOrigin = spaceOrigin
                pca.__spaceCropped = spaceCropped
                pca.__dimInfo = dimInfo
                return pca

        class GaussianND(GreyCat.Object):
            def __init__(self: algebra_n.ml.GaussianND, type: GreyCat.Type) -> None:
                super(type, None)
                self.__count: c_int64
                self.__min: core.Tensor
                self.__max: core.Tensor
                self.__sum: core.Tensor
                self.__sum_sq: core.Tensor

            def _save(self: algebra_n.ml.GaussianND, stream: GreyCat._Stream) -> None:
                stream.write_i8(PrimitiveType.OBJECT)
                stream.write_i32(self.type_.offset)
                stream.write_i64(self.__count)
                stream.write_object(self.__min)
                stream.write_object(self.__max)
                stream.write_object(self.__sum)
                stream.write_object(self.__sum_sq)

            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat._Stream) -> object:
                count: c_int64 = stream.read_i64()
                min: core.Tensor = stream.read_object()
                max: core.Tensor = stream.read_object()
                sum: core.Tensor = stream.read_object()
                sum_sq: core.Tensor = stream.read_object()
                g: algebra_n.ml.GaussianND = type.factory(type)
                g.__count = count
                g.__min = min
                g.__max = max
                g.__sum = sum
                g.__sum_sq = sum_sq
                return g
