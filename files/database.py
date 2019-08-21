from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
#SQLALCHEMY_DATABASE_URL = "postgres://dgqccwocumlbqn:d6b564ed31279c32d2965b18cf9cba1b04a9f6640225fb97d1c8e724f05e7fa3@ec2-174-129-242-183.compute-1.amazonaws.com:5432/d541455u5vc2it"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()