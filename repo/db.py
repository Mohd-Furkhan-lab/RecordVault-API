from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase,sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

DATABASEURL=os.getenv("DATABASE_URL")


engine=create_engine(DATABASEURL)

class Base(DeclarativeBase):
    pass

SessionLocal = sessionmaker(bind=engine,autoflush=False,autocommit=False)

