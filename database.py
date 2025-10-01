from app.models.user import User
import motor.motor_asyncio
from beanie import init_beanie
from app.models.post import Post

MONGO_DATABASE_URL = "mongodb://localhost:27017"
MONGO_DB_NAME = "testdb"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DATABASE_URL)
db = client[MONGO_DB_NAME]

async def init_db():
    await init_beanie(database=db, document_models=[User, Post])

