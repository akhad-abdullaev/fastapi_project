from beanie import Document
from pydantic import Field
from typing import Optional

class User(Document):
    username: str   # unique index
    full_name: Optional[str] = None
    hashed_password: str
    disabled: bool = False

    @property
    def id(self):
        return str(self._id)

    class Settings:
        name = "users"  # MongoDB collection name

    
