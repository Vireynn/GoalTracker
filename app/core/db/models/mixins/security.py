from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

class SecurityModelMixin:
    hashed_password: Mapped[str] = mapped_column(
        String, nullable=False
    )
    salt: Mapped[str] = mapped_column(
        String, nullable=False
    )
