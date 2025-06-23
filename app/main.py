import logging
from fastapi import FastAPI
from app.api.routes import router

# Configure root logger to show INFO level messages with timestamp, logger name, level and message
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

# Initialize FastAPI app with a title
app = FastAPI(title="Speech to Text API")

# Include API routes defined in the router
app.include_router(router)
