#BIBLIOTECAS

# FAST
#INTERNO
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
#OUTROS 
from dotenv import load_dotenv
import os

#CONFIGURAÇOES 

#ARQUIVO ENV
load_dotenv()

#SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
#SQLALCHEMY_DATABASE_URL = "postgresql://<usuario>:<senha>@<localhost>/<DaTABASE>"
SQLALCHEMY_DATABASE_URL = os.getenv('SQLALCHEMY_DATABASE_URL')


engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# FUNÇOES PARA CRIAR BANCO DE DADOS
def criar_db():
    Base.metadata.create_all(bind=engine)
def get_db():
    session = SessionLocal()
    try:
        yield session

    finally:
        session.close()
