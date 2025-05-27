from fastapi import FastAPI
from app.api.main import api_router

app = FastAPI(
    title="Flashcards Alemão",
    openapi_url="/v1/openapi.json"
)

app.include_router(api_router, prefix="/v1")