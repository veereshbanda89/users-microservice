from fastapi import FastAPI
from app.api.random import random_service

app = FastAPI(openapi_url="/api/v1/random/openapi.json", docs_url="/api/v1/random/docs")

app.include_router(random_service, prefix='/api/v1/random', tags=['random'])
