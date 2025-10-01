from pydantic import BaseModel, Field
from typing import Optional
from beanie import PydanticObjectId


class UserBase(BaseModel):
    username: str
    full_name: Optional[str] = None

class UserCreate(UserBase):
    password: str


class UserResponse(BaseModel):
    id: str
    username: str
    full_name: Optional[str]
    disabled: bool

    class Config:
        orm_mode = True
        json_encoders = {PydanticObjectId: str}


class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None
