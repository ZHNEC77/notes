from typing import Annotated

from fastapi import APIRouter, Depends

from core.models import User

from api.api_v1.fastapi_users import current_user
from core.schemas.note import NoteCreate
from core.config import settings
from crud.notes import post
from core.models import db_helper
from crud.notes import get_all_notes

router = APIRouter(
    prefix=settings.api.v1.notes,
    tags=["Notes"],
)


@router.post("")
async def get_user_notes(
    user: Annotated[
        User,
        Depends(current_user)
    ],
    note_create: NoteCreate,
):
    return await post(note_create=note_create, user_id=user.id, session=db_helper.session_getter())


@router.get("/")
async def read_all_notes(
    user: Annotated[
        User,
        Depends(current_user)
    ],
):
    notes = await get_all_notes(
        session=db_helper.session_getter(),
        user_id=user.id,
    )
    return notes
