import numpy
import pandas

pandas.DataFrame(numpy.random.rand(1_000_000, 40)).to_csv(
    "data/huge.csv",
    index=False,
)
