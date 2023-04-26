from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routes import (incidents, predictions)

origins = [
    "http://localhost:3000",
    "localhost:3000"
]

def new_application():
    app = FastAPI()
    app.include_router(
        incidents.router,
        prefix='/incidents'
    )
    app.include_router(
        predictions.router,
        prefix='/predictions'
    )
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )
    return app

app = new_application()
