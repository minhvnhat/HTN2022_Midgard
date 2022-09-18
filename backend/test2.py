import os
import psycopg2
import pandas as pd
from dotenv import load_dotenv
load_dotenv() 

from sqlalchemy import create_engine

user = os.environ["USERNAME"]
host = os.environ['HOST']
cluster = os.environ["CLUSTER"]
password = os.environ["DATABASE_PW"]

if __name__ == "__main__":
    db_uri = os.environ['DATABASE_URL'].replace("postgresql://", "cockroachdb://")
    try:
        engine = create_engine(db_uri)
    except Exception as e:
        print("Failed to connect to database.")
        print(f"{e}")

    business_table_schema = """
        CREATE TABLE Business (
            id STRING PRIMARY KEY,
            category STRING,
            name STRING,
            phone STRING,
            price_range STRING,
            website STRING,
            yelp_url STRING,
            latitude FLOAT,
            longitude FLOAT
        )
    """

    with engine.connect() as conn:
        conn.execute("DROP TABLE Business")
        # conn.execute(business_table_schema)

        df = pd.read_csv('dataset/business.csv')
        df.to_sql('Business', conn)
    