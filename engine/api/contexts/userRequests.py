from loguru import logger as log
from pydantic import BaseModel, validator, Field
from typing import Optional, Tuple, List

# === Input Models ===

class User(BaseModel):
    nome: str = Field()

class Form(BaseModel):
    nome_rep_familia: str = Field()
    pessoa: str = Field()
    qtd_pessoas_familia: int = Field()
    pessoa_amamenta: bool = Field()
    qtd_criancas: int = Field()
    gestante: bool = Field()
    qtd_amamentando: int = Field()
    qtd_criancas_deficiencia: int = Field()
    qtd_gestantes: int = Field()

class Privilege(BaseModel):
    user_type: str = Field()

class Login(BaseModel):
    email: str
    password: str

# === Output Models ===

class Response(BaseModel):
    message: str

class FormList(BaseModel):
    respondido: bool

class FormResponse(BaseModel):
    count: int
    users: List[FormList]
    message: str

class PrivilegeList(BaseModel):
    user_type: str

class PrivilegeResponse(BaseModel):
    count: int
    Privileges: List[PrivilegeList]
    message: str

class LoginResponse:
    status: int
    type: Optional[str]
    id: Optional[str]
    verificado: Optional[str]

# === Handlers ===

def createUser(data: User) -> Response:
    return {message: "Usuário criado!"}

def createForm(data: Form) -> Response:
    return {message: "Formulário enviado!"}

def retrieveForms(id: int) -> FormResponse:
    #forms = db.query.(models.Form).filter_by(and_(pessoa == id, preenchido == True))
    results = [{
        "respondido": form.preenchido
    } for form in forms]
    return {count: len(results), users: results, message: "Success"}

def createPrivilege(data: Privilege) -> Response:
    return {message: "Privilégio criado com sucesso!"}

def retrievePrivileges() -> PrivilegeResponse:
    #privileges = db.query(models.Privileges)
    results = [{
        "user_type": privilege.user_type
    } for privilege in privileges]
    return {count: len(results), Privileges: results, message: "Success"}

def login(data: Login) -> LoginResponse:
    #user = db.query(models.Users).filter(email=data.email).first()
    if user and user.password == data.password:
        return {status: 1000, type: str(user.user_type), id: str(user.id), verificado: str(user.verificado)}
    return {status: 1010}
