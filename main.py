from fastapi import FastAPI
from routes import router

app = FastAPI(title="Multi-Agent Audio AI System")

app.include_router(router)