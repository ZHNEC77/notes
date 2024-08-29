from typing import TYPE_CHECKING
from sqlalchemy import String, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base
from .mixins.int_id_pk import IntIdPkMixin
from sqlalchemy.ext.asyncio import AsyncSession

if TYPE_CHECKING:
    from .user import User


class Note(IntIdPkMixin, Base):
    title: Mapped[str] = mapped_column(String(77), unique=False)
    body: Mapped[str] = mapped_column(
        Text,
        default="",
        server_default="",
    )
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
    )
    user: Mapped["User"] = relationship(back_populates="notes")
