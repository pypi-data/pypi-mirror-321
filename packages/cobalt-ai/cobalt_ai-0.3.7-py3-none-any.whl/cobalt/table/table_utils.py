import pandas as pd


def is_datetime_col(series):
    return pd.api.types.is_datetime64_any_dtype(series)
