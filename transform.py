import pandas as pd
from prefect import task


@task
def transform_data(df):

    # Remove duplicate IDs
    df = df.drop_duplicates(
        subset=["id"],
        keep="first"
    )

    # Remove rows without an ID
    df = df.dropna(
        subset=["id"]
    )

    # Convert date_time
    df["date_time"] = pd.to_datetime(
        df["date_time"],
        errors="coerce"
    )

    # Remove rows where date_time is invalid
    df = df.dropna(
        subset=["date_time"]
    )

    # Create time-related columns
    df["year"] = df["date_time"].dt.year
    df["month"] = df["date_time"].dt.month
    df["day"] = df["date_time"].dt.day
    df["hour"] = df["date_time"].dt.hour

    return df