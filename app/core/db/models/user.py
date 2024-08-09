from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from core.db.base import Base
from .mixins import UserBaseModelMixin

class User(UserBaseModelMixin, Base):
    __tablename__ = "users"

    first_name: Mapped[str]
    last_name: Mapped[str]
    bio: Mapped[str]
    country: Mapped[str] = mapped_column(String(length=2))
