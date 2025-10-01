from database import init_db
import uvicorn
from fastapi import FastAPI
from app.routers import post, user

app = FastAPI()

@app.on_event("startup")
async def on_startup():
    await init_db()


app.include_router(post.router, prefix="/api")
app.include_router(user.router, prefix="/api")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
