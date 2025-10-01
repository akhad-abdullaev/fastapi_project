from beanie import Document
from typing import Optional

class User(Document):
    username: str 
    full_name: Optional[str] = None
    hashed_password: str
    disabled: bool = False

    @property
    def id(self):
        return str(self._id)

    class Settings:
        name = "users" 

    
