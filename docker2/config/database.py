#BIBLIOTECAS

# FAST
#INTERNO
from sqlalchemy import (
    create_engine,
    text)
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

     # Conexão temporária para executar o SQL GRANT
    with engine.connect() as conn:
        # Substitua "postgres" pelo nome do seu usuário no PostgreSQL
        sql_grant = text("GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO postgres;")
        conn.execute(sql_grant)

def get_db():
    session = SessionLocal()
    try:
        yield session

    finally:
        session.close()
