from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

#URL de connexion a la BD
# SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:@localhost/secure_password" #Pour MySQL
SQLALCHEMY_DATABASE_URL = "postgresql://paracelse:paracelse.id@localhost:5432/paracelse"

#Engin pour creer les pool de connexion et executer SQL
engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True, max_overflow=20)

#Pour generer des sessions ou unite de travail
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

#Base pour definir les modes ORM
Base = declarative_base()