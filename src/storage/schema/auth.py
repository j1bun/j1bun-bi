from typing import Literal

from enum import Enum
from pydantic import BaseModel, Field


__all__ = [
    'AuthGetIn'
]


class ApplicationType(Enum):
    CLOUD = 'cloud'
    LOCAL = 'local'


class AuthGetIn(BaseModel):
    """ Get the auth for an application """
    app: str = Field(..., description='Application Name')
    type: ApplicationType = Field(..., description='Application Type')
    domain: str = Field(..., description='application Domain')
