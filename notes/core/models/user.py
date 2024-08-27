from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column

from fastapi_users_db_sqlalchemy import (
    SQLAlchemyBaseUserTable,
    SQLAlchemyUserDatabase,
)

from core.types.user_id import UserIdType
from .base import Base
from .mixins.int_id_pk import IntIdPkMixin

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


class User(IntIdPkMixin, Base, SQLAlchemyBaseUserTable[UserIdType]):
    username: Mapped[str] = mapped_column(unique=True)

    @classmethod
    def get_db(cls, session: "AsyncSession"):
        return SQLAlchemyUserDatabase(session, User)
