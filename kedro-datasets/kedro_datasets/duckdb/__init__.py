"""``AbstractDataSet`` implementations that produce pandas DataFrames."""

__all__ = ["ParquetDataSet"]

from contextlib import suppress

with suppress(ImportError):
    from .parquet_dataset import ParquetDataSet
