from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

SQLALCHEMY_DATABASE_URL = "postgresql://dennohkim_user:GaeM1u2vKNbx4Tw2GLsu4WQbFqiNWXHg@dpg-crt1jge8ii6s73eheje0-a.oregon-postgres.render.com/dennohkim?sslmode=require" #os.getenv("DATABASE_URL")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
