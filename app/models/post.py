# from sqlalchemy import Column, Integer, String
# from sqlalchemy.ext.declarative import declarative_base

# # from database import Base

# Base = declarative_base()


# class Post(Base):
#     __tablename__ = "posts"
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, index=True)
#     description = Column(String, index=True)


from beanie import Document
from pydantic import Field
from typing import Optional

class Post(Document):
    name: str
    description: Optional[str] = None

    class Settings:
        name = "posts"
