from fastapi import FastAPI
from .routes import initialize_routes

app = FastAPI()
initialize_routes(app)
