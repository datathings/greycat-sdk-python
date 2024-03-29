from __future__ import annotations
from ctypes import *
from typing import *

from . import GreyCat, PrimitiveType, std


class algebra_n:
    class powerflow:
        class _PowerNetwork(GreyCat.Object):
            def __init__(self: algebra_n.powerflow.PowerNetwork, type: GreyCat.Type) -> None:
                super(type, None)
                raise NotImplementedError

            def load(type: GreyCat.Type, stream: GreyCat._Stream) -> object:
                raise NotImplementedError

    class compute:
        class _ComputeState(GreyCat.Object):
            def __init__(self: algebra_n.compute.ComputeState, type: GreyCat.Type) -> None:
                super(type, None)
                raise NotImplementedError

            def load(type: GreyCat.Type, stream: GreyCat._Stream) -> object:
                raise NotImplementedError

        class _ComputeEngine(GreyCat.Object):
            def __init__(self: algebra_n.compute.ComputeEngine, type: GreyCat.Type) -> None:
                super(type, None)
                raise NotImplementedError

            def load(type: GreyCat.Type, stream: GreyCat._Stream) -> object:
                raise NotImplementedError

    class ml:
        class _Polynomial(GreyCat.Object):
            def __init__(self: algebra_n.ml._Polynomial, type: GreyCat.Type) -> None:
                super(type, None)
                self.degree: c_byte
                self.x_start: c_double
                self.x_step: c_double
                self.tensor_type: c_byte
                self.data: bytes

            def _save(self: algebra_n.ml._Polynomial, stream: GreyCat._Stream) -> None:
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
                poly: algebra_n.ml._Polynomial = type.factory(type)
                poly.degree = degree
                poly.x_start = xStart
                poly.x_step = xStep
                poly.tensor_type = tensorType
                poly.data = data
                return poly

        class _PCA(GreyCat.Object):
            def __init__(self: algebra_n.ml.PCA, type: GreyCat.Type) -> None:
                super(type, None)
                self.__bestDim: c_int32
                self.__selectedDim: c_int32
                self.__threshold: c_double
                self.__eigenVectors: std.core.Tensor
                self.__eigenValues: std.core.Tensor
                self.__avg: std.core.Tensor
                self.__std: std.core.Tensor
                self.__correlation: std.core.Tensor
                self.__explainedVariance: std.core.Tensor
                self.__spaceOrigin: std.core.Tensor
                self.__spaceCropped: std.core.Tensor
                self.__dimInfo: std.core.Tensor

            def _save(self: algebra_n.ml.PCA, stream: GreyCat._Stream) -> None:
                stream.write_i8(PrimitiveType.OBJECT)
                stream.write_i32(self.type_.offset)
                stream.write_i32(self.__bestDim)
                stream.write_i32(self.__selectedDim)
                stream.write_f64(self.__threshold)
                stream.write(self.__eigenVectors)
                stream.write(self.__eigenValues)
                stream.write(self.__avg)
                stream.write(self.__std)
                stream.write(self.__correlation)
                stream.write(self.__explainedVariance)
                stream.write(self.__spaceOrigin)
                stream.write(self.__spaceCropped)
                stream.write(self.__dimInfo)

            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat._Stream) -> object:
                bestDim: c_int32 = stream.read_i32()
                selectedDim: c_int32 = stream.read_i32()
                threshold: c_double = stream.read_f64()
                eigenVectors: std.core.Tensor = stream.read()
                eigenValues: std.core.Tensor = stream.read()
                avg: std.core.Tensor = stream.read()
                std: std.core.Tensor = stream.read()
                correlation: std.core.Tensor = stream.read()
                explainedVariance: std.core.Tensor = stream.read()
                spaceOrigin: std.core.Tensor = stream.read()
                spaceCropped: std.core.Tensor = stream.read()
                dimInfo: std.core.Tensor = stream.read()
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

        class _GaussianND(GreyCat.Object):
            def __init__(self: algebra_n.ml.GaussianND, type: GreyCat.Type) -> None:
                super(type, None)
                self.__count: c_int64
                self.__min: std.core.Tensor
                self.__max: std.core.Tensor
                self.__sum: std.core.Tensor
                self.__sum_sq: std.core.Tensor

            def _save(self: algebra_n.ml.GaussianND, stream: GreyCat._Stream) -> None:
                stream.write_i8(PrimitiveType.OBJECT)
                stream.write_i32(self.type_.offset)
                stream.write_i64(self.__count)
                stream.write(self.__min)
                stream.write(self.__max)
                stream.write(self.__sum)
                stream.write(self.__sum_sq)

            @staticmethod
            def load(type: GreyCat.Type, stream: GreyCat._Stream) -> object:
                count: c_int64 = stream.read_i64()
                min: std.core.Tensor = stream.read()
                max: std.core.Tensor = stream.read()
                sum: std.core.Tensor = stream.read()
                sum_sq: std.core.Tensor = stream.read()
                g: algebra_n.ml.GaussianND = type.factory(type)
                g.__count = count
                g.__min = min
                g.__max = max
                g.__sum = sum
                g.__sum_sq = sum_sq
                return g
