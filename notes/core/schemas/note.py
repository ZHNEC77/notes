from typing import Optional
from pydantic import BaseModel, field_validator
from speller.speller import checker


class NoteRead(BaseModel):
    title: str
    body: str
    user_id: int


class NoteCreate(BaseModel):
    title: str
    body: str
    # user_id: int

    @field_validator("body")
    @classmethod
    def validate_body(cls, value: str):
        check = checker(value)
        if check is False:
            return value
        else:
            return check


class NoteUpdate(BaseModel):
    title: Optional[str]
    body: Optional[str]
