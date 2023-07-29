#BIBLIOTECAS

#FASTAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from routers.routers import  router
#LOCAIS
from config.database import criar_db
#OUTRAS



app = FastAPI()

#We define authorizations for middleware components
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5432"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
#fac3c3735aea ---  docker run -d -p 5433:5433 -e POSTGRES_PORT=5433 --name docker-post postgres:latest

# criar banco de dados
criar_db()

# rotas 
app.include_router(router)
