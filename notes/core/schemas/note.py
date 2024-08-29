from typing import Optional
from pydantic import BaseModel, validator, field_validator
from speller.speller import checker


class NoteRead(BaseModel):
    title: str
    body: str
    user_id: int


class NoteCreate(BaseModel):
    title: str
    body: str
    # user_id: int

    # @validator("body")
    # def validate_body(cls, value):
    #     if not checker(value):
    #         return value
    #     else:
    #         return checker(value)


class NoteUpdate(BaseModel):
    title: Optional[str]
    body: Optional[str]
