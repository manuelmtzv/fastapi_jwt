from fastapi import FastAPI

from app.data.posts import posts
from app.model import PostSchema

app = FastAPI()


@app.get("/", tags=["test"])
def root():
    return {"message": "FastAPI and JWT Auth example"}


@app.get("/posts", tags=["posts"])
def get_all_posts():
    return {"data": posts}
