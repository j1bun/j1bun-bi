from fastapi import APIRouter

from src.storage.schema import AuthGetIn


auth = APIRouter()


@auth.post('/')
def get_auth(data: AuthGetIn | None):
    pass
