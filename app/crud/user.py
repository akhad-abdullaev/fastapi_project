from typing import Optional
from app.schemas.user import UserCreate
from app.models.user import User 
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


async def get_user(username: str) -> Optional[User]:
    return await User.find_one(User.username == username)


async def get_user_by_id(user_id: str) -> Optional[User]:
    return await User.get(user_id)


async def create_user_in_db(user: UserCreate) -> User:
    hashed_password = pwd_context.hash(user.password)
    db_user = User(
        username=user.username,
        full_name=user.full_name,
        hashed_password=hashed_password,
        disabled=False,
    )
    await db_user.insert()
    return db_user


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


async def authenticate_user(username: str, password: str) -> Optional[User]:
    user = await get_user(username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user
