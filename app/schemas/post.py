from pydantic import BaseModel
from typing import Optional

class PostBase(BaseModel):
    name: str
    description: Optional[str] = None

class PostCreate(PostBase):
    pass

class PostUpdate(PostBase):
    pass

class PostResponse(PostBase):
    id: str  

    class Config:
        json_schema_extra = {
            "example": {
                "id": "6512bd43d9caa6e02c990b0a",
                "name": "First Post",
                "description": "Hello MongoDB with Beanie"
            }
        }
