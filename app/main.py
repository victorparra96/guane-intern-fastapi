import logging

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from db import init_db

from api.api_v1.api import api_router

log = logging.getLogger(__name__)

app = FastAPI(title="Tortoise ORM FastAPI test guane")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup_event():
    print("Starting up...")
    init_db(app)


@app.on_event("shutdown")
async def shutdown_event():
    print("Shutting down...")

app.include_router(api_router, prefix="/api")
