from fastapi import FastAPI
from app.api.users import users

app = FastAPI(openapi_url="/api/v1/users/openapi.json", docs_url="/api/v1/users/docs")

app.include_router(users, prefix='/api/v1/users', tags=['users'])
