from fastapi import FastAPI

from src import routers


app = FastAPI(
    swagger_ui_parameters={'docExpansion': 'none'}
)
app.include_router(
    routers.auth,
    prefix='/auth', tags=['auth'], dependencies=[],
)
