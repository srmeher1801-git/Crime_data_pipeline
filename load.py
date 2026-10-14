from prefect import task
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os


@task
def load_into_postgres(df):

    load_dotenv()

    user = os.getenv("POSTGRES_USER", "postgres")
    password = os.getenv("POSTGRES_PASSWORD", "postgres")

    engine = create_engine(
        f"postgresql+psycopg2://{user}:{password}@localhost:5433/crime_db"
    )

    df.to_sql(
        "cpd_incidents",
        engine,
        if_exists="replace",
        index=False
    )

    print("Data loaded into PostgreSQL.")