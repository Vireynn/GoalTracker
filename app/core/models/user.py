from sqlalchemy import Integer, String, DateTime, ForeignKey, text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime

from .base import Base
from .types import created_at

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    first_name: Mapped[str] = mapped_column(String)
    last_name: Mapped[str] = mapped_column(String)
    age: Mapped[int]
    country: Mapped[str] = mapped_column(String(2))

    # Feature:
    # projects: Mapped[list["Projects"]] = relationship(
    #     primaryjoin="Users.id == Project.owner_id"
    # )


class UserPassword(Base):
    __tablename__ = "user_passwords"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    hashed_password: Mapped[str] = mapped_column(String, nullable=False)
    created_at: Mapped[created_at]
