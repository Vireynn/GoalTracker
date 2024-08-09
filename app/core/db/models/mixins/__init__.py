from sqlalchemy.orm import Mapped, mapped_column, declared_attr
from sqlalchemy import String

from .common import (
    IDModelMixin,
    DateTimeModelMixin
)
from .security import SecurityModelMixin

class UserBaseModelMixin(IDModelMixin, DateTimeModelMixin, SecurityModelMixin):
    username: Mapped[str] = mapped_column(String(length=20), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(length=255), unique=True, nullable=False)
