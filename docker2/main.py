from fastapi import FastAPI
from config.database import get_db, criar_db
from routers import routers

app = FastAPI()

criar_db()

app.include_router(routers.router)
