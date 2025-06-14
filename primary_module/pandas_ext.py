"""Custom Extension"""

from __future__ import annotations

from typing import List

import pandas as pd
from pandas.api.types import is_datetime64_any_dtype


# TODO - rename accesor name 
@pd.api.extensions.register_dataframe_accessor("xxx")
class ZeroAccessor:
    """Provide Zero Lift helper methods for :class:`pandas.DataFrame`."""


    def __init__(self, pandas_obj: pd.DataFrame) -> None:
        self._obj = pandas_obj


    def func(self, x):
        print(x)

