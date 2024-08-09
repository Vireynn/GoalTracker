import datetime
from typing import Annotated

from sqlalchemy.orm import Mapped, MappedColumn, mapped_column
from sqlalchemy import text

class IDModelMixin:
    id: Mapped[int] = mapped_column(primary_key=True)

class DateTimeModelMixin:
    created_at = Annotated[
        datetime.datetime, mapped_column(server_default=text(""))
    ]
    updated_at = Annotated[
        datetime.datetime, mapped_column(
            server_default=text("TIMEZONE('utc', now())"),
            onupdate=datetime.datetime.now(datetime.UTC)
        )]
