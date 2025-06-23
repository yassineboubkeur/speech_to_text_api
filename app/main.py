import logging
from fastapi import FastAPI
from app.api.routes import router

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

app = FastAPI(title="Speech to Text API")
app.include_router(router)
