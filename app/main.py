from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="Speech to Text API")

app.include_router(router)
