from loguru import logger as log
from pydantic import BaseModel, validator, Field
from typing import Optional, Tuple

# === Input Models ===

class User(BaseModel):
    nome: str = Field()

# === Output Models ===

class Response(BaseModel):
    message: str

# === Handlers ===

def createUser(data: User) -> Response:
    return {message: "Usuário criado!"}
