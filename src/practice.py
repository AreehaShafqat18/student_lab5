"""Test Yourself tasks for the Pandas lab."""

import pandas as pd


# ===== Step 1: Series and DataFrames =====

def t1_1_weather_series(df):
    """Return temp_c as a Series indexed by day names."""
    return pd.Series(df["temp_c"].values, index=df["day"].values)


def t1_2_hottest_day(df):
    """Return the name of the day with the highest temperature."""
    return df.loc[df["temp_c"].idxmax(), "day"]


def t1_3_build_frame():
    """Build and return a DataFrame."""
    return pd.DataFrame({
        "item": ["pen", "book", "bag"],
        "price": [10, 120, 800]
    })


def t1_4_series_vs_frame(df):
    """Return the type names of a Series and DataFrame."""
    a = type(df["temp_c"]).__name__
    b = type(df[["temp_c"]]).__name__
    return (a, b)