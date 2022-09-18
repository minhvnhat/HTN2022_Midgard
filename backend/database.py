"""Initialize database connections."""

import os
from dotenv import load_dotenv
load_dotenv() 
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = os.environ["DATABASE_URL"].replace("postgresql://", "cockroachdb://")
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()