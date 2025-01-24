r"""Contain ``polars.DataFrame`` transformers to convert some columns to
a new data type."""

from __future__ import annotations

__all__ = [
    "CastTransformer",
    "CategoricalCastTransformer",
    "DecimalCastTransformer",
    "FloatCastTransformer",
    "IntegerCastTransformer",
    "NumericCastTransformer",
]

import logging
from typing import TYPE_CHECKING, Any

import polars as pl
import polars.selectors as cs
from coola.utils.format import repr_mapping_line

from grizz.transformer.columns import BaseIn1Out1Transformer, BaseInNTransformer
from grizz.utils.format import str_size_diff

if TYPE_CHECKING:
    from collections.abc import Sequence


logger = logging.getLogger(__name__)


class CastTransformer(BaseInNTransformer):
    r"""Implement a transformer to convert some columns to a new data
    type.

    Args:
        columns: The columns to convert. ``None`` means all the
            columns.
        dtype: The target data type.
        exclude_columns: The columns to exclude from the input
            ``columns``. If any column is not found, it will be ignored
            during the filtering process.
        missing_policy: The policy on how to handle missing columns.
            The following options are available: ``'ignore'``,
            ``'warn'``, and ``'raise'``. If ``'raise'``, an exception
            is raised if at least one column is missing.
            If ``'warn'``, a warning is raised if at least one column
            is missing and the missing columns are ignored.
            If ``'ignore'``, the missing columns are ignored and
            no warning message appears.
        **kwargs: The keyword arguments for ``cast``.

    Example usage:

    ```pycon

    >>> import polars as pl
    >>> from grizz.transformer import Cast
    >>> transformer = Cast(columns=["col1", "col3"], dtype=pl.Int32)
    >>> transformer
    CastTransformer(columns=('col1', 'col3'), dtype=Int32, exclude_columns=(), missing_policy='raise')
    >>> frame = pl.DataFrame(
    ...     {
    ...         "col1": [1, 2, 3, 4, 5],
    ...         "col2": ["1", "2", "3", "4", "5"],
    ...         "col3": ["1", "2", "3", "4", "5"],
    ...         "col4": ["a", "b", "c", "d", "e"],
    ...     }
    ... )
    >>> frame
    shape: (5, 4)
    ┌──────┬──────┬──────┬──────┐
    │ col1 ┆ col2 ┆ col3 ┆ col4 │
    │ ---  ┆ ---  ┆ ---  ┆ ---  │
    │ i64  ┆ str  ┆ str  ┆ str  │
    ╞══════╪══════╪══════╪══════╡
    │ 1    ┆ 1    ┆ 1    ┆ a    │
    │ 2    ┆ 2    ┆ 2    ┆ b    │
    │ 3    ┆ 3    ┆ 3    ┆ c    │
    │ 4    ┆ 4    ┆ 4    ┆ d    │
    │ 5    ┆ 5    ┆ 5    ┆ e    │
    └──────┴──────┴──────┴──────┘
    >>> out = transformer.transform(frame)
    >>> out
    shape: (5, 4)
    ┌──────┬──────┬──────┬──────┐
    │ col1 ┆ col2 ┆ col3 ┆ col4 │
    │ ---  ┆ ---  ┆ ---  ┆ ---  │
    │ i32  ┆ str  ┆ i32  ┆ str  │
    ╞══════╪══════╪══════╪══════╡
    │ 1    ┆ 1    ┆ 1    ┆ a    │
    │ 2    ┆ 2    ┆ 2    ┆ b    │
    │ 3    ┆ 3    ┆ 3    ┆ c    │
    │ 4    ┆ 4    ┆ 4    ┆ d    │
    │ 5    ┆ 5    ┆ 5    ┆ e    │
    └──────┴──────┴──────┴──────┘

    ```
    """

    def __init__(
        self,
        columns: Sequence[str] | None,
        dtype: type[pl.DataType],
        exclude_columns: Sequence[str] = (),
        missing_policy: str = "raise",
        **kwargs: Any,
    ) -> None:
        super().__init__(
            columns=columns, exclude_columns=exclude_columns, missing_policy=missing_policy
        )
        self._dtype = dtype
        self._kwargs = kwargs

    def __repr__(self) -> str:
        args = repr_mapping_line(self.get_args())
        return f"{self.__class__.__qualname__}({args})"

    def get_args(self) -> dict:
        return {
            "columns": self._columns,
            "dtype": self._dtype,
            "exclude_columns": self._exclude_columns,
            "missing_policy": self._missing_policy,
        } | self._kwargs

    def _fit(self, frame: pl.DataFrame) -> None:  # noqa: ARG002
        logger.info(
            f"Skipping '{self.__class__.__qualname__}.fit' as there are no parameters "
            f"available to fit"
        )

    def _transform(self, frame: pl.DataFrame) -> pl.DataFrame:
        logger.info(f"Casting {len(self.find_columns(frame)):,} columns to {self._dtype}...")
        columns = self.find_common_columns(frame)
        out = self._transform_frame(frame, columns)
        logger.info(str_size_diff(orig=frame.estimated_size(), final=out.estimated_size()))
        return out

    def _transform_frame(self, frame: pl.DataFrame, columns: Sequence[str]) -> pl.DataFrame:
        return frame.with_columns(
            frame.select(cs.by_name(columns).cast(self._dtype, **self._kwargs))
        )


class DecimalCastTransformer(CastTransformer):
    r"""Implement a transformer to convert columns of type decimal to a
    new data type.

    Args:
        columns: The columns to convert. ``None`` means all the
            columns.
        dtype: The target data type.
        exclude_columns: The columns to exclude from the input
            ``columns``. If any column is not found, it will be ignored
            during the filtering process.
        missing_policy: The policy on how to handle missing columns.
            The following options are available: ``'ignore'``,
            ``'warn'``, and ``'raise'``. If ``'raise'``, an exception
            is raised if at least one column is missing.
            If ``'warn'``, a warning is raised if at least one column
            is missing and the missing columns are ignored.
            If ``'ignore'``, the missing columns are ignored and
            no warning message appears.
        **kwargs: The keyword arguments for ``cast``.

    Example usage:

    ```pycon

    >>> import polars as pl
    >>> from grizz.transformer import DecimalCast
    >>> transformer = DecimalCast(columns=["col1", "col2"], dtype=pl.Float32)
    >>> transformer
    DecimalCastTransformer(columns=('col1', 'col2'), dtype=Float32, exclude_columns=(), missing_policy='raise')
    >>> frame = pl.DataFrame(
    ...     {
    ...         "col1": [1, 2, 3, 4, 5],
    ...         "col2": [1.0, 2.0, 3.0, 4.0, 5.0],
    ...         "col3": [1.0, 2.0, 3.0, 4.0, 5.0],
    ...         "col4": ["a", "b", "c", "d", "e"],
    ...     },
    ...     schema={
    ...         "col1": pl.Int64,
    ...         "col2": pl.Decimal,
    ...         "col3": pl.Decimal,
    ...         "col4": pl.String,
    ...     },
    ... )
    >>> frame
    shape: (5, 4)
    ┌──────┬──────────────┬──────────────┬──────┐
    │ col1 ┆ col2         ┆ col3         ┆ col4 │
    │ ---  ┆ ---          ┆ ---          ┆ ---  │
    │ i64  ┆ decimal[*,0] ┆ decimal[*,0] ┆ str  │
    ╞══════╪══════════════╪══════════════╪══════╡
    │ 1    ┆ 1            ┆ 1            ┆ a    │
    │ 2    ┆ 2            ┆ 2            ┆ b    │
    │ 3    ┆ 3            ┆ 3            ┆ c    │
    │ 4    ┆ 4            ┆ 4            ┆ d    │
    │ 5    ┆ 5            ┆ 5            ┆ e    │
    └──────┴──────────────┴──────────────┴──────┘
    >>> out = transformer.transform(frame)
    >>> out
    shape: (5, 4)
    ┌──────┬──────┬──────────────┬──────┐
    │ col1 ┆ col2 ┆ col3         ┆ col4 │
    │ ---  ┆ ---  ┆ ---          ┆ ---  │
    │ i64  ┆ f32  ┆ decimal[*,0] ┆ str  │
    ╞══════╪══════╪══════════════╪══════╡
    │ 1    ┆ 1.0  ┆ 1            ┆ a    │
    │ 2    ┆ 2.0  ┆ 2            ┆ b    │
    │ 3    ┆ 3.0  ┆ 3            ┆ c    │
    │ 4    ┆ 4.0  ┆ 4            ┆ d    │
    │ 5    ┆ 5.0  ┆ 5            ┆ e    │
    └──────┴──────┴──────────────┴──────┘

    ```
    """

    def _transform_frame(self, frame: pl.DataFrame, columns: Sequence[str]) -> pl.DataFrame:
        return frame.with_columns(
            frame.select((cs.by_name(columns) & cs.decimal()).cast(self._dtype, **self._kwargs))
        )


class FloatCastTransformer(CastTransformer):
    r"""Implement a transformer to convert columns of type float to a new
    data type.

    Args:
        columns: The columns to convert. ``None`` means all the
            columns.
        dtype: The target data type.
        exclude_columns: The columns to exclude from the input
            ``columns``. If any column is not found, it will be ignored
            during the filtering process.
        missing_policy: The policy on how to handle missing columns.
            The following options are available: ``'ignore'``,
            ``'warn'``, and ``'raise'``. If ``'raise'``, an exception
            is raised if at least one column is missing.
            If ``'warn'``, a warning is raised if at least one column
            is missing and the missing columns are ignored.
            If ``'ignore'``, the missing columns are ignored and
            no warning message appears.
        **kwargs: The keyword arguments for ``cast``.

    Example usage:

    ```pycon

    >>> import polars as pl
    >>> from grizz.transformer import FloatCast
    >>> transformer = FloatCast(columns=["col1", "col2"], dtype=pl.Int32)
    >>> transformer
    FloatCastTransformer(columns=('col1', 'col2'), dtype=Int32, exclude_columns=(), missing_policy='raise')
    >>> frame = pl.DataFrame(
    ...     {
    ...         "col1": [1, 2, 3, 4, 5],
    ...         "col2": [1.0, 2.0, 3.0, 4.0, 5.0],
    ...         "col3": [1.0, 2.0, 3.0, 4.0, 5.0],
    ...         "col4": ["a", "b", "c", "d", "e"],
    ...     },
    ...     schema={
    ...         "col1": pl.Int64,
    ...         "col2": pl.Float64,
    ...         "col3": pl.Float64,
    ...         "col4": pl.String,
    ...     },
    ... )
    >>> frame
    shape: (5, 4)
    ┌──────┬──────┬──────┬──────┐
    │ col1 ┆ col2 ┆ col3 ┆ col4 │
    │ ---  ┆ ---  ┆ ---  ┆ ---  │
    │ i64  ┆ f64  ┆ f64  ┆ str  │
    ╞══════╪══════╪══════╪══════╡
    │ 1    ┆ 1.0  ┆ 1.0  ┆ a    │
    │ 2    ┆ 2.0  ┆ 2.0  ┆ b    │
    │ 3    ┆ 3.0  ┆ 3.0  ┆ c    │
    │ 4    ┆ 4.0  ┆ 4.0  ┆ d    │
    │ 5    ┆ 5.0  ┆ 5.0  ┆ e    │
    └──────┴──────┴──────┴──────┘
    >>> out = transformer.transform(frame)
    >>> out
    shape: (5, 4)
    ┌──────┬──────┬──────┬──────┐
    │ col1 ┆ col2 ┆ col3 ┆ col4 │
    │ ---  ┆ ---  ┆ ---  ┆ ---  │
    │ i64  ┆ i32  ┆ f64  ┆ str  │
    ╞══════╪══════╪══════╪══════╡
    │ 1    ┆ 1    ┆ 1.0  ┆ a    │
    │ 2    ┆ 2    ┆ 2.0  ┆ b    │
    │ 3    ┆ 3    ┆ 3.0  ┆ c    │
    │ 4    ┆ 4    ┆ 4.0  ┆ d    │
    │ 5    ┆ 5    ┆ 5.0  ┆ e    │
    └──────┴──────┴──────┴──────┘

    ```
    """

    def _transform_frame(self, frame: pl.DataFrame, columns: Sequence[str]) -> pl.DataFrame:
        return frame.with_columns(
            frame.select((cs.by_name(columns) & cs.float()).cast(self._dtype, **self._kwargs))
        )


class IntegerCastTransformer(CastTransformer):
    r"""Implement a transformer to convert columns of type integer to a
    new data type.

    Args:
        columns: The columns to convert. ``None`` means all the
            columns.
        dtype: The target data type.
        exclude_columns: The columns to exclude from the input
            ``columns``. If any column is not found, it will be ignored
            during the filtering process.
        missing_policy: The policy on how to handle missing columns.
            The following options are available: ``'ignore'``,
            ``'warn'``, and ``'raise'``. If ``'raise'``, an exception
            is raised if at least one column is missing.
            If ``'warn'``, a warning is raised if at least one column
            is missing and the missing columns are ignored.
            If ``'ignore'``, the missing columns are ignored and
            no warning message appears.
        **kwargs: The keyword arguments for ``cast``.

    Example usage:

    ```pycon

    >>> import polars as pl
    >>> from grizz.transformer import IntegerCast
    >>> transformer = IntegerCast(columns=["col1", "col2"], dtype=pl.Float32)
    >>> transformer
    IntegerCastTransformer(columns=('col1', 'col2'), dtype=Float32, exclude_columns=(), missing_policy='raise')
    >>> frame = pl.DataFrame(
    ...     {
    ...         "col1": [1, 2, 3, 4, 5],
    ...         "col2": [1.0, 2.0, 3.0, 4.0, 5.0],
    ...         "col3": [1, 2, 3, 4, 5],
    ...         "col4": ["a", "b", "c", "d", "e"],
    ...     },
    ...     schema={
    ...         "col1": pl.Int64,
    ...         "col2": pl.Float64,
    ...         "col3": pl.Int64,
    ...         "col4": pl.String,
    ...     },
    ... )
    >>> frame
    shape: (5, 4)
    ┌──────┬──────┬──────┬──────┐
    │ col1 ┆ col2 ┆ col3 ┆ col4 │
    │ ---  ┆ ---  ┆ ---  ┆ ---  │
    │ i64  ┆ f64  ┆ i64  ┆ str  │
    ╞══════╪══════╪══════╪══════╡
    │ 1    ┆ 1.0  ┆ 1    ┆ a    │
    │ 2    ┆ 2.0  ┆ 2    ┆ b    │
    │ 3    ┆ 3.0  ┆ 3    ┆ c    │
    │ 4    ┆ 4.0  ┆ 4    ┆ d    │
    │ 5    ┆ 5.0  ┆ 5    ┆ e    │
    └──────┴──────┴──────┴──────┘
    >>> out = transformer.transform(frame)
    >>> out
    shape: (5, 4)
    ┌──────┬──────┬──────┬──────┐
    │ col1 ┆ col2 ┆ col3 ┆ col4 │
    │ ---  ┆ ---  ┆ ---  ┆ ---  │
    │ f32  ┆ f64  ┆ i64  ┆ str  │
    ╞══════╪══════╪══════╪══════╡
    │ 1.0  ┆ 1.0  ┆ 1    ┆ a    │
    │ 2.0  ┆ 2.0  ┆ 2    ┆ b    │
    │ 3.0  ┆ 3.0  ┆ 3    ┆ c    │
    │ 4.0  ┆ 4.0  ┆ 4    ┆ d    │
    │ 5.0  ┆ 5.0  ┆ 5    ┆ e    │
    └──────┴──────┴──────┴──────┘

    ```
    """

    def _transform_frame(self, frame: pl.DataFrame, columns: Sequence[str]) -> pl.DataFrame:
        return frame.with_columns(
            frame.select((cs.by_name(columns) & cs.integer()).cast(self._dtype, **self._kwargs))
        )


class NumericCastTransformer(CastTransformer):
    r"""Implement a transformer to convert columns of numeric type to a
    new data type.

    Args:
        columns: The columns to convert. ``None`` means all the
            columns.
        dtype: The target data type.
        exclude_columns: The columns to exclude from the input
            ``columns``. If any column is not found, it will be ignored
            during the filtering process.
        missing_policy: The policy on how to handle missing columns.
            The following options are available: ``'ignore'``,
            ``'warn'``, and ``'raise'``. If ``'raise'``, an exception
            is raised if at least one column is missing.
            If ``'warn'``, a warning is raised if at least one column
            is missing and the missing columns are ignored.
            If ``'ignore'``, the missing columns are ignored and
            no warning message appears.
        **kwargs: The keyword arguments for ``cast``.

    Example usage:

    ```pycon

    >>> import polars as pl
    >>> from grizz.transformer import NumericCast
    >>> transformer = NumericCast(columns=["col1", "col2"], dtype=pl.Float32)
    >>> transformer
    NumericCastTransformer(columns=('col1', 'col2'), dtype=Float32, exclude_columns=(), missing_policy='raise')
    >>> frame = pl.DataFrame(
    ...     {
    ...         "col1": [1, 2, 3, 4, 5],
    ...         "col2": [1.0, 2.0, 3.0, 4.0, 5.0],
    ...         "col3": [1.0, 2.0, 3.0, 4.0, 5.0],
    ...         "col4": ["a", "b", "c", "d", "e"],
    ...     },
    ...     schema={
    ...         "col1": pl.Int64,
    ...         "col2": pl.Float32,
    ...         "col3": pl.Float64,
    ...         "col4": pl.String,
    ...     },
    ... )
    >>> frame
    shape: (5, 4)
    ┌──────┬──────┬──────┬──────┐
    │ col1 ┆ col2 ┆ col3 ┆ col4 │
    │ ---  ┆ ---  ┆ ---  ┆ ---  │
    │ i64  ┆ f32  ┆ f64  ┆ str  │
    ╞══════╪══════╪══════╪══════╡
    │ 1    ┆ 1.0  ┆ 1.0  ┆ a    │
    │ 2    ┆ 2.0  ┆ 2.0  ┆ b    │
    │ 3    ┆ 3.0  ┆ 3.0  ┆ c    │
    │ 4    ┆ 4.0  ┆ 4.0  ┆ d    │
    │ 5    ┆ 5.0  ┆ 5.0  ┆ e    │
    └──────┴──────┴──────┴──────┘
    >>> out = transformer.transform(frame)
    >>> out
    shape: (5, 4)
    ┌──────┬──────┬──────┬──────┐
    │ col1 ┆ col2 ┆ col3 ┆ col4 │
    │ ---  ┆ ---  ┆ ---  ┆ ---  │
    │ f32  ┆ f32  ┆ f64  ┆ str  │
    ╞══════╪══════╪══════╪══════╡
    │ 1.0  ┆ 1.0  ┆ 1.0  ┆ a    │
    │ 2.0  ┆ 2.0  ┆ 2.0  ┆ b    │
    │ 3.0  ┆ 3.0  ┆ 3.0  ┆ c    │
    │ 4.0  ┆ 4.0  ┆ 4.0  ┆ d    │
    │ 5.0  ┆ 5.0  ┆ 5.0  ┆ e    │
    └──────┴──────┴──────┴──────┘

    ```
    """

    def _transform_frame(self, frame: pl.DataFrame, columns: Sequence[str]) -> pl.DataFrame:
        return frame.with_columns(
            frame.select((cs.by_name(columns) & cs.numeric()).cast(self._dtype, **self._kwargs))
        )


class CategoricalCastTransformer(BaseIn1Out1Transformer):
    r"""Implement a transformer to convert a column to categorical data
    type.

    Args:
        in_col: The input column name to cast.
        out_col: The output column name.
        exist_policy: The policy on how to handle existing columns.
            The following options are available: ``'ignore'``,
            ``'warn'``, and ``'raise'``. If ``'raise'``, an exception
            is raised if at least one column already exist.
            If ``'warn'``, a warning is raised if at least one column
            already exist and the existing columns are overwritten.
            If ``'ignore'``, the existing columns are overwritten and
            no warning message appears.
        missing_policy: The policy on how to handle missing columns.
            The following options are available: ``'ignore'``,
            ``'warn'``, and ``'raise'``. If ``'raise'``, an exception
            is raised if at least one column is missing.
            If ``'warn'``, a warning is raised if at least one column
            is missing and the missing columns are ignored.
            If ``'ignore'``, the missing columns are ignored and
            no warning message appears.
        **kwargs: Additional arguments passed to
            ``polars.Categorical``.

    Example usage:

    ```pycon

    >>> import polars as pl
    >>> from grizz.transformer import CategoricalCast
    >>> transformer = CategoricalCast(in_col="col1", out_col="out")
    >>> transformer
    CategoricalCastTransformer(in_col='col1', out_col='out', exist_policy='raise', missing_policy='raise')
    >>> frame = pl.DataFrame(
    ...     {
    ...         "col1": ["a", "b", "c", "d", "e"],
    ...         "col2": [1.0, 2.0, 3.0, 4.0, 5.0],
    ...     },
    ...     schema={"col1": pl.String, "col2": pl.Float64},
    ... )
    >>> frame
    shape: (5, 2)
    ┌──────┬──────┐
    │ col1 ┆ col2 │
    │ ---  ┆ ---  │
    │ str  ┆ f64  │
    ╞══════╪══════╡
    │ a    ┆ 1.0  │
    │ b    ┆ 2.0  │
    │ c    ┆ 3.0  │
    │ d    ┆ 4.0  │
    │ e    ┆ 5.0  │
    └──────┴──────┘
    >>> out = transformer.transform(frame)
    >>> out
    shape: (5, 3)
    ┌──────┬──────┬─────┐
    │ col1 ┆ col2 ┆ out │
    │ ---  ┆ ---  ┆ --- │
    │ str  ┆ f64  ┆ cat │
    ╞══════╪══════╪═════╡
    │ a    ┆ 1.0  ┆ a   │
    │ b    ┆ 2.0  ┆ b   │
    │ c    ┆ 3.0  ┆ c   │
    │ d    ┆ 4.0  ┆ d   │
    │ e    ┆ 5.0  ┆ e   │
    └──────┴──────┴─────┘

    ```
    """

    def __init__(
        self,
        in_col: str,
        out_col: str,
        exist_policy: str = "raise",
        missing_policy: str = "raise",
        **kwargs: Any,
    ) -> None:
        super().__init__(
            in_col=in_col,
            out_col=out_col,
            exist_policy=exist_policy,
            missing_policy=missing_policy,
        )
        self._kwargs = kwargs

    def __repr__(self) -> str:
        args = repr_mapping_line(self.get_args())
        return f"{self.__class__.__qualname__}({args})"

    def get_args(self) -> dict:
        return {
            "in_col": self._in_col,
            "out_col": self._out_col,
            "exist_policy": self._exist_policy,
            "missing_policy": self._missing_policy,
        } | self._kwargs

    def _fit(self, frame: pl.DataFrame) -> None:  # noqa: ARG002
        logger.info(
            f"Skipping '{self.__class__.__qualname__}.fit' as there are no parameters "
            f"available to fit"
        )

    def _transform(self, frame: pl.DataFrame) -> pl.DataFrame:
        logger.info(f"Casting column {self._in_col!r} to categorical column {self._out_col!r} ...")
        return frame.with_columns(
            pl.col(self._in_col).cast(pl.Categorical(**self._kwargs)).alias(self._out_col)
        )
