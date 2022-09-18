import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
load_dotenv() 

if __name__ == "__main__":
    db_url = os.environ['DATABASE_URL'].replace("postgresql://", "cockroachdb://")
    try:
        engine = create_engine(db_url)
    except Exception as e:
        print("Failed to connect to database.")
        print(f"{e}")

    with engine.connect() as conn:
        for r in conn.execute('SELECT * FROM public."Business"'):
            print(r)
        # conn.execute("DROP TABLE \"Business\"")
        # conn.execute("DROP TABLE \"business\"")