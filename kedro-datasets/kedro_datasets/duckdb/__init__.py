"""``AbstractDataSet`` implementations that produce pandas DataFrames."""

__all__ = ["ParquetRelationalDataSet"]

from contextlib import suppress

with suppress(ImportError):
    from .parquet_relational_dataset import ParquetRelationalDataSet
