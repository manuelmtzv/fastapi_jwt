from uuid import uuid4

from fastapi import FastAPI

from app.data.posts import posts
from app.model import PostSchema

app = FastAPI()


# Test route
@app.get("/", tags=["test"])
def root():
    return {"message": "FastAPI and JWT Auth example"}


# Posts routes


# 1. Get all posts
@app.get("/posts", tags=["posts"])
def get_all_posts():
    return {"data": posts}


# 2. Get one post
@app.get("/posts/{id}", tags=["posts"])
def get_one_post(id: str):
    for post in posts:
        if post["id"] == id:
            return {"data": post}
    return {"message": "Post not found"}


# 3. Add a post
@app.post("/posts", tags=["posts"])
def add_post(post: PostSchema):
    post.id = uuid4()
    posts.append(post.dict())
    return {"message": "Post added", "data": dict(post)}
