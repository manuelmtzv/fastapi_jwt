from uuid import uuid4

from pydantic import BaseModel, EmailStr, Field


class PostSchema(BaseModel):
    id: str = Field(default_factory=lambda: uuid4())
    title: str = Field(default=None)
    content: str = Field(default=None)

    class Config:
        schema_extra = {"post_demo": {"title": "Some title", "content": "Some content"}}


class UserSchema(BaseModel):
    fullname: str = Field(default=None)
    email: EmailStr = Field(default=None)
    password: str = Field(default=None)

    class Config:
        the_schema = {"user_demo": {"name": "Manuel", "email": "manuel@email.com", "password": "password"}}


class UserLoginSchema(BaseModel):
    email: EmailStr = Field(default=None)
    password: str = Field(default=None)

    class Config:
        the_schema = {"user_demo": {"email": "manuel@email.com", "password": "password"}}
