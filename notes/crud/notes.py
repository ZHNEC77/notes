from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from core.models import Note
from core.schemas.note import NoteCreate


async def post(
        session: AsyncSession,
        user_id: int,
        title: str,
        body: str,
):
    note = Note(title=title, body=body, user_id=user_id)
    session.add(note)
    await session.commit()
    return note


async def get_all_notes(
    session: AsyncSession,
    user_id: int,
) -> Sequence[Note]:
    stmt = select(Note).options(
        selectinload(Note.user)
    ).filter(Note.user_id == user_id).order_by(Note.id)
    result = await session.scalars(stmt)
    return result.all()
