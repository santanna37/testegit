# BIBLIOTECAS 
from sqlalchemy import Column, Integer, String
from config.database import Base


class Usuario(Base):
    __tablename__='usuario'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    nome = Column(String)
