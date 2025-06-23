from functools import lru_cache
from typing import Union

from fastapi import FastAPI, Depends
from fastapi.responses import PlainTextResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Response

# routers: comment out next line till create them
from routers import todos

import config

app = FastAPI()

# router: comment out next line till create it
app.include_router(todos.router)


#origins = [
#    "http://localhost:3000",
#    "https://todo-frontend-khaki.vercel.app/",
#]

# CORS configuration, needed for frontend development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*" ],
    #allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"]  # ¡Nuevo!
)


# global http exception handler, to handle errors
@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    print(f"{repr(exc)}")
    return PlainTextResponse(str(exc.detail), status_code=exc.status_code)

# to use the settings
@lru_cache()
def get_settings():
    return config.Settings()


@app.get("/")
def read_root(settings: config.Settings = Depends(get_settings)):
    # print the app_name configuration
    print(settings.app_name)
    return "Hello World"


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/todos")
async def get_todos():
    todos = [...]  # Tu lógica para obtener datos de PostgreSQL
    return Response(
        content=json.dumps(todos),
        media_type="application/json",
        headers={"Cache-Control": "no-store, max-age=0"}
    ) # agrgado 2006