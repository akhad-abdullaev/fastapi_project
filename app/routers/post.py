from fastapi import APIRouter, HTTPException
from typing import List

from app.models.post import Post 
from app.schemas.post import PostCreate, PostUpdate

router = APIRouter()


@router.post("/posts/")
async def create_post(post: PostCreate):
    new_post = Post(**post.dict())
    await new_post.insert()
    return new_post


@router.get("/posts/")
async def read_posts(skip: int = 0, limit: int = 10):
    posts = await Post.find_all().skip(skip).limit(limit).to_list()
    return posts


@router.get("/posts/{post_id}")
async def read_post(post_id: str):
    post = await Post.get(post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post


@router.put("/posts/{post_id}")
async def update_post(post_id: str, post_data: PostUpdate):
    post = await Post.get(post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    update_data = post_data.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(post, key, value)
    await post.save()
    return post


@router.delete("/posts/{post_id}")
async def delete_post(post_id: str):
    post = await Post.get(post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    await post.delete()
    return {"message": "Post deleted successfully"}
