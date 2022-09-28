from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import URL
from dotenv import load_dotenv
load_dotenv() 
import os


# Creating a database in the current directory called sql_app.db.
# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

password=os.environ['PASSWORD']
SQLALCHEMY_DATABASE_URL = "cockroachdb://catdonut:Au7_2JXQSJ36aBDmfZxYlA@free-tier11.gcp-us-east1.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full&options=--cluster%3Dripe-locust-1979"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
