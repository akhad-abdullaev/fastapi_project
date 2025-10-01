from beanie import Document
from typing import Optional



class Post(Document):
    name: str
    description: Optional[str] = None

    class Settings:
        name = "posts"
