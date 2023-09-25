from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configuração para PostgreSQL rodando localmente com Docker
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@db:5432/ecommerceapi"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
