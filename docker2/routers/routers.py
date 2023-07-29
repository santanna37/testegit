from sqlalchemy.orm import Session 
from fastapi import Depends, APIRouter
from schemas import schemas
from models import models
from config.database import get_db, criar_db
from repositorio.repositorio import RepositorioUsuario


router = APIRouter()


@router.get('/')
def hello():
    home = f'Pagina rodando'
    return home

@router.post('/usuario')
def criar_usuario(usuario:schemas.Usuario, session = Depends(get_db)):

    produto_criado = RepositorioUsuario(session).criar(usuario)
    return produto_criado
