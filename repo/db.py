from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase,sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL=os.getenv("DATABASE_URL")

engine=create_engine(DATABASE_URL)
base=DeclarativeBase()

SessionLocal = sessionmaker(bind=engine,autoflush=False,autocommit=False)

