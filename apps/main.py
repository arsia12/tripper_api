from fastapi import FastAPI, Request
from database.conn import db_instance
from search.router import search_router

app = FastAPI(
    title="Tripper",
    description="Tripper API",
    version="0.0.1"
)


@app.on_event("startup")
async def startup():
    await db_instance.connect()


@app.on_event("shutdown")
async def shutdown():
    await db_instance.disconnect()


@app.middleware("http")
async def state_insert(request: Request, call_next):
    request.state.db_conn = db_instance
    response = await call_next(request)
    return response


app.include_router(search_router)