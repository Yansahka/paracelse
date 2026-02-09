from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

load_dotenv()

#URL de connexion a la BD

DATABASE_URL = os.getenv("ONLINE_DATABASE_URL")


#Engin pour creer les pool de connexion et executer SQL
engine = create_engine(DATABASE_URL, pool_pre_ping=True, max_overflow=20)

#Pour generer des sessions ou unite de travail
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

#Base pour definir les modes ORM
Base = declarative_base()