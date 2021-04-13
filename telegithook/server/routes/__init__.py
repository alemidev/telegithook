from fastapi import FastAPI

from . import index


def initialize_routes(app: FastAPI):
    app.include_router(index.router)
