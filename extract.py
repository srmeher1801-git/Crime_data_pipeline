import pandas as pd
from sodapy import Socrata
from dotenv import load_dotenv
import os
from prefect import task


@task(retries=3, retry_delay_seconds=[10, 10, 10])
def extract_data():

    load_dotenv()

    app_token = os.getenv("SOCRATA_APP_TOKEN")

    client = Socrata(
        "data.cambridgema.gov",
        app_token,
        timeout=30
    )

    dataset_id = "3gki-wyrb"

    results = client.get_all(dataset_id)

    results_df = pd.DataFrame.from_records(results)

    return results_df