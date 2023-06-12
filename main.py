from uuid import uuid4

from fastapi import Body, FastAPI

from app.auth.jwt_handler import signJWT
from app.data.posts import posts
from app.data.users import users
from app.model import PostSchema, UserLoginSchema, UserSchema

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
def add_post(post: PostSchema = Body(default=None)):
    post.id = uuid4()
    posts.append(post.dict())
    return {"message": "Post added", "data": dict(post)}


# Users routes
# 1. Signup
@app.post("/users/signup", tags=["users"])
def user_signup(user: UserSchema = Body(default=None)):
    users.append(user)
    return signJWT(user.email)


def check_user(data: UserLoginSchema):
    for user in users:
        return user.email == data.email and user.password == data.password


@app.post("/user/login", tags=["users"])
def user_login(user: UserLoginSchema = Body(default=None)):
    if check_user(user):
        return signJWT(user.email)
    else:
        return {"error": "Invalid login credentials"}
