from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from sqlalchemy import or_
from typing import List
from models import Post, get_db  # Assuming `get_db` is a dependency to get the DB session
from datetime import datetime
from pydantic import BaseModel, field_validator

app = FastAPI()

# Pydantic Models for Request and Response Validation
class PostBase(BaseModel):
    title: str
    content: str
    author: str
    category: str


class PostResponse(PostBase):
    id: int
    created_at: str

    @field_validator("created_at", mode="before")
    def format_created_at(cls, value):
        if isinstance(value, datetime):
            return value.strftime("%Y-%m-%d %H:%M:%S")
        return value

    class Config:
        from_attributes = True



# Home - View All Blog Posts
@app.get("/")
async def home():
    return { "message" : "Welcome to our Blog API" }


# Create Blog Post - API
@app.post("/posts", response_model=PostResponse)
async def create_post(post_data: PostBase, db: Session = Depends(get_db)):
    new_post = Post(**post_data.model_dump())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


# Read All Blog Posts - API
@app.get("/posts", response_model=List[PostResponse])
async def get_all_posts(db: Session = Depends(get_db)):
    posts = db.query(Post).all()
    return posts


# Search Blog Posts - API
@app.get("/posts/search", response_model=List[PostResponse])
async def search_posts(term: str = "", db: Session = Depends(get_db)):
    posts = db.query(Post).filter(
        or_(
            Post.title.contains(term),
            Post.content.contains(term),
            Post.category.contains(term),
            Post.author.contains(term),
            Post.created_at.contains(term)
        )
    ).all()
    if not posts:
        raise HTTPException(status_code=404, detail="No posts found")
    return posts


# Read a Single Blog Post - API
@app.get("/posts/{id}", response_model=PostResponse)
async def get_post(id: int, db: Session = Depends(get_db)):
    post = db.query(Post).filter_by(id=id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post


# Delete Blog Post - API
@app.delete("/delete-post/{id}")
async def delete_post(id: int, db: Session = Depends(get_db)):
    post = db.query(Post).filter_by(id=id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    db.delete(post)
    db.commit()
    return {"message": "Deleted post successfully"}



# Edit Blog Post - API
@app.put("/edit-post/{id}", response_model=PostResponse)
async def update_post(id: int, post_data: PostBase, db: Session = Depends(get_db)):
    post = db.query(Post).filter_by(id=id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    # Update fields
    for key, value in post_data.model_dump(exclude_unset=True).items():
        setattr(post, key, value)

    db.commit()
    db.refresh(post)
    return post
