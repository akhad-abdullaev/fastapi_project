from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud.post import get_post, get_posts, create_post_in_db, update_post_in_db, delete_post_in_db
from app.schemas.post import PostCreate, PostUpdate
from database import get_db

router = APIRouter()

@router.post("/posts/")
def create_post(post: PostCreate, db: Session = Depends(get_db)):
    return create_post_in_db(db=db, post=post)

@router.get("/posts/")
def read_posts(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    posts = get_posts(db, skip=skip, limit=limit)
    return posts

@router.get("/posts/{post_id}")
def read_post(post_id: int, db: Session = Depends(get_db)):
    db_post = get_post(db, post_id=post_id)
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return db_post

@router.put("/posts/{post_id}")
def update_post(post_id: int, post: PostUpdate, db: Session = Depends(get_db)):
    db_post = get_post(db, post_id=post_id)
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return update_post_in_db(db=db, post_id=post_id, post=post)

@router.delete("/posts/{post_id}")
def delete_post(post_id: int, db: Session = Depends(get_db)):
    db_post = get_post(db, post_id=post_id)
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return delete_post_in_db(db=db, post_id=post_id)
