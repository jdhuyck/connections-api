from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.connection_api.api.v1.api import api_router
from src.connection_api.core.config import settings

app = FastAPI(title="Connections API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["jdhuyck.github.io", "localhost:*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(api_router, prefix=settings.API_V1_STR)
