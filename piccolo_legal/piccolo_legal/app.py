from operator import imod
from fastapi import FastAPI
from piccolo_api.fastapi.endpoints import (
    FastAPIWrapper,
    PiccoloCRUD,
    FastAPIKwargs,
)
from piccolo_api.fastapi.endpoints import FastAPIWrapper
from starlette.applications import Starlette
from starlette.routing import Mount
from piccolo_admin.endpoints import create_admin
from piccolo.engine import engine_finder
from fastapi.responses import JSONResponse
import uvicorn

from pydantic.main import BaseModel
from starlette.routing import Route, Mount
from starlette.staticfiles import StaticFiles

from legal.tables import QuestionHead,Questions,Answers,AddUser
from legal.piccolo_app import APP_CONFIG
from legal.endpoints import HomeEndpoint

# app = FastAPI()

# admin = create_admin([Questions,Answers,AddUser])
# app = FastAPI(routes=[Mount('/admin',admin)])


app = FastAPI(
    routes=[
        Route("/", HomeEndpoint),
        Mount(
            "/admin/",
            create_admin(tables=APP_CONFIG.table_classes, site_name="LEGALCHAIN"),
        ),
        Mount("/static/", StaticFiles(directory="static")),
    ],
)

FastAPIWrapper(

    
    root_url="/questionhead/",
    fastapi_app=app,
    piccolo_crud=PiccoloCRUD(QuestionHead, read_only=False),
    fastapi_kwargs=FastAPIKwargs(
        all_routes={"tags": ["QuestionHead"]},
    ),
    
    ),

FastAPIWrapper(

    
    root_url="/questions/",
    fastapi_app=app,
    piccolo_crud=PiccoloCRUD(Questions, read_only=False),
    fastapi_kwargs=FastAPIKwargs(
        all_routes={"tags": ["Questions"]},
    ),
    
    ),
FastAPIWrapper(
    root_url="/answers/",
    fastapi_app=app,
    piccolo_crud=PiccoloCRUD(Answers, read_only=False),
    fastapi_kwargs=FastAPIKwargs(
        all_routes={"tags": ["answers"]},
    ),
    
    ),

FastAPIWrapper(
    root_url="/adduser/",
    fastapi_app=app,
    piccolo_crud=PiccoloCRUD(AddUser, read_only=False),
    fastapi_kwargs=FastAPIKwargs(
        all_routes={"tags": ["adduser"]},
    ),
    
    ),


@app.on_event("startup")
async def open_database_connection_pool():
    engine = engine_finder()
    await engine.start_connnection_pool()


@app.on_event("shutdown")
async def close_database_connection_pool():
    engine = engine_finder()
    await engine.close_connnection_pool()


if __name__ == '__main__':
    uvicorn.run(app)
