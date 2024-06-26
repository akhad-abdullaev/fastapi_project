from sqlalchemy.orm import Session
from app.models.post import Post
from app.schemas.post import PostCreate, PostUpdate

def get_post(db: Session, post_id: int):
    return db.query(Post).filter(Post.id == post_id).first()

def get_posts(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Post).offset(skip).limit(limit).all()

def create_post_in_db(db: Session, post: PostCreate):
    db_post = Post(name=post.name, description=post.description)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

def update_post_in_db(db: Session, post_id: int, post: PostUpdate):
    db_post = db.query(Post).filter(Post.id == post_id).first()
    if db_post:
        db_post.name = post.name
        db_post.description = post.description
        db.commit()
        db.refresh(db_post)
    return db_post

def delete_post_in_db(db: Session, post_id: int):
    db_post = db.query(Post).filter(Post.id == post_id).first()
    if db_post:
        db.delete(db_post)
        db.commit()
    return db_post



# @app.post("/items/")
# async def create_item(item: ItemCreate):
# 	db = SessionLocal()
# 	db_item = Item(name=item.name, description=item.description)
# 	db.add(db_item)
# 	db.commit()
# 	db.refresh(db_item)
# 	return db_item


# @app.get("/items/all")
# async def read_item():
# 	db = SessionLocal()
# 	item = db.query(Item).all()
# 	return item


# @app.get("/items/{item_id}")
# async def read_item(item_id: int):
# 	db = SessionLocal()
# 	item = db.query(Item).filter(Item.id == item_id).first()
# 	return item



# @app.put("/items/{item_id}")
# async def update_item(item_id: int, name: str, description: str):
# 	db = SessionLocal()
# 	db_item = db.query(Item).filter(Item.id == item_id).first()
# 	db_item.name = name
# 	db_item.description = description
# 	db.commit()
# 	return db_item



# @app.delete("/items/{item_id}")
# async def delete_item(item_id: int):
# 	db = SessionLocal()
# 	db_item = db.query(Item).filter(Item.id == item_id).first()
# 	db.delete(db_item)
# 	db.commit()
# 	return {"message": "Item deleted successfully"}