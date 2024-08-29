import os
import requests
from typing import Optional
from pydantic import BaseModel, field_validator
from dotenv import load_dotenv


load_dotenv()


URL = os.getenv("URL")


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
        params = {"text": "синхрафазатрон+" + value}
        response = requests.get(URL, params=params)
        res = response.json()
        erros = []
        for i in range(1, len(res)):
            e = res[i]["s"][0]
            print(e)
            erros.append(e)
        if erros:
            raise ValueError("ошибка в слове правильно: ", " ".join(erros))
        return value


class NoteUpdate(BaseModel):
    title: Optional[str]
    body: Optional[str]
