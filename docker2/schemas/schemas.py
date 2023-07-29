from pydantic import BaseModel
from typing import Optional


#tabalas 
class Usuario(BaseModel):
    id: Optional[int] =None
    nome: str

    class config:
        orm_mode=True