import logging

from fastapi import FastAPI

from app.api import summaries, default
from app.db import init_db


log = logging.getLogger("uvicorn")


def create_application() -> FastAPI:
    application = FastAPI()

    #Add routers
    application.include_router(default.router)
    application.include_router(summaries.router, prefix="/summaries", tags=["summaries"]) 

    return application


app = create_application()

#TODO: on_event is deprecated - need to replace with lifespan event methods -> https://fastapi.tiangolo.com/advanced/events/#alternative-events-deprecated
@app.on_event("startup")
async def startup_event():
    log.info("Starting up...")
    init_db(app)


@app.on_event("shutdown")
async def shutdown_event():
    log.info("Shutting down...")