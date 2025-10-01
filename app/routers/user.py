from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
from beanie import PydanticObjectId

from app.models.user import User  
from app.schemas.user import Token, UserResponse, UserCreate
from app.authentication.auth import (
    ACCESS_TOKEN_EXPIRE_MINUTES,
    create_access_token,
    get_current_active_user,
)
from passlib.context import CryptContext



router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


async def authenticate_user(username: str, password: str):
    user = await User.find_one(User.username == username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/users/", response_model=UserResponse)
async def create_user(user: UserCreate):
    existing_user = await User.find_one(User.username == user.username)
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already registered")

    hashed_password = get_password_hash(user.password)
    new_user = User(
        username=user.username,
        full_name=user.full_name,
        hashed_password=hashed_password,
        disabled=False,
    )
    await new_user.insert()
    return UserResponse(
        id=str(new_user.id),
        username=new_user.username,
        full_name=new_user.full_name,
        disabled=new_user.disabled,
    )


@router.get("/users/me", response_model=UserResponse)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user



@router.get("/users/{user_id}", response_model=UserResponse)
async def read_user(user_id: str):
    try:
        oid = PydanticObjectId(user_id) 
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid user id")

    user = await User.get(oid)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return UserResponse(
        id=str(user.id), 
        username=user.username,
        full_name=user.full_name,
        disabled=user.disabled,
    )



