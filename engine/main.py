import uvicorn
from fastapi import FastAPI
import os
from fastapi_sqlalchemy import DBSessionMiddleware
from fastapi_sqlalchemy import db
#from models import User as ModelUser
#from schema import User as SchemaUser
from dotenv import load_dotenv

from api.contexts import userRequests as user

ROUTE_PREFIX = "/plasmedis/api/"

tags_metadata = [
    {
        "name": "Plasmedis API",
        "description": "Operações do fórum",
    },
]

##BASE_DIR = os.path.dirname(os.path.abspath(__file__))
##load_dotenv(os.path.join(BASE_DIR, ".env"))

app = FastAPI(
    title="REST API Plasmedis",
    description="teste",
    version="1.0.0",
    openapi_tags=tags_metadata,
    openapi_url=ROUTE_PREFIX + "openapi.json",
    docs_url=ROUTE_PREFIX + "docs",
    redoc_url=ROUTE_PREFIX + "redoc"
)

##app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])

@app.post(
    ROUTE_PREFIX + "user/create",
    response_model=user.Response,
    tags=["Create"],
)
async def create(data: user.User):
    return user.createUser(data)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)