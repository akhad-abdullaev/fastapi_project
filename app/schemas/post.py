from pydantic import BaseModel



class PostBase(BaseModel):
    name: str
    description: str

class PostCreate(PostBase):
    pass

class PostUpdate(PostBase):
    pass

class Post(PostBase):
    id: int

    class Config:
        orm_mode = True
