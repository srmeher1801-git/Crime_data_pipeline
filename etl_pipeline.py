from prefect import flow

from extract import extract_data
from validate import validate_data
from transform import transform_data
from load import load_into_postgres


@flow(
    name="cpd_incident_etl",
    log_prints=True
)
def etl():

    print("Starting ETL pipeline...")

    print("Extracting data...")
    extracted_df = extract_data()

    print("Validating data...")
    validated_df = validate_data(extracted_df)

    print("Transforming data...")
    transformed_df = transform_data(validated_df)

    print("Loading data into PostgreSQL...")
    load_into_postgres(transformed_df)

    print("ETL pipeline completed.")


if __name__ == "__main__":
    etl.serve(
        name="cpd-pipeline-deployment",
        cron="0 0 * * *"
    )