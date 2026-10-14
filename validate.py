import pandas as pd
from prefect import task


@task
def validate_data(df):

    expected_columns = [
        "date_time",
        "id",
        "type",
        "location"
    ]

    for column in expected_columns:
        if column not in df.columns:
            raise ValueError(f"Missing column: {column}")

    print("All expected columns are present.")

    df["id"] = pd.to_numeric(df["id"], errors="coerce")

    df["date_time"] = pd.to_datetime(
        df["date_time"],
        errors="coerce"
    )

    print("Data validation completed.")

    return df