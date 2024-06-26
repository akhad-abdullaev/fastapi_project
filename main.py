import uvicorn
from fastapi import FastAPI
from app.routers import post, user
from sqlalchemy.ext.declarative import declarative_base


app = FastAPI()


app.include_router(post.router, prefix="/api")
app.include_router(user.router, prefix="/api")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
