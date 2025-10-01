from typing import List, Optional
from app.models.post import Post
from app.schemas.post import PostCreate, PostUpdate


async def get_post(post_id: str) -> Optional[Post]:
    return await Post.get(post_id)


async def get_posts(skip: int = 0, limit: int = 10) -> List[Post]:
    return await Post.find_all().skip(skip).limit(limit).to_list()


async def create_post_in_db(post: PostCreate) -> Post:
    new_post = Post(**post.dict())
    await new_post.insert()
    return new_post


async def update_post_in_db(post_id: str, post: PostUpdate) -> Optional[Post]:
    db_post = await Post.get(post_id)
    if db_post:
        update_data = post.dict(exclude_unset=True)
        await db_post.set(update_data)
        return db_post
    return None


async def delete_post_in_db(post_id: str) -> Optional[Post]:
    db_post = await Post.get(post_id)
    if db_post:
        await db_post.delete()
        return db_post
    return None
