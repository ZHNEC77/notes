from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload, joinedload
from core.models import Note


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
        joinedload(Note.user)).filter(
        user_id == user_id).order_by(Note.title)
    result = await session.scalars(stmt)
    return result.all()
