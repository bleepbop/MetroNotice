from fastapi import FastAPI

from .routes import (incidents)


def new_application():
    app = FastAPI()
    app.include_router(
        incidents.router,
        prefix='/incidents'
    )
    return app


app = new_application()
