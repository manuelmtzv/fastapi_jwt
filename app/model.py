from uuid import uuid4

from pydantic import BaseModel, EmailStr, Field


class PostSchema(BaseModel):
    id: str = Field(default_factory=str(uuid4))
    title: str = Field(default=None)
    content: str = Field(default=None)

    class Config:
        schema_extra = {"post_demo": {"title": "Some title", "content": "Some content"}}
