from typing import Dict, Any, Callable, Type

from sqlalchemy import select, func, Select
from sqlalchemy.ext.asyncio import AsyncSession

from core.db.models import User
from .base import BaseRepository

class UsersRepository(BaseRepository):
    def __init__(
            self,
            user_table: Type[User],
            session: AsyncSession
    ):
        super().__init__(session)
        self.user_table = user_table

    async def get(self, id: int):
        statement = select(self.user_table).where(self.user_table.id == id)
        return await self.execute(statement)

    async def get_user_by_username(self, username: str):
        statement = select(self.user_table).where(
            self.user_table.username == username
        )
        return await self.execute(statement)

    async def get_user_by_email(self, email: str):
        statement = select(self.user_table).where(
            self.user_table.email == email
        )
        return await self.execute(statement)

    async def create(self, create_dict: Dict[str, Any]):
        user = self.user_table(**create_dict)
        self.session.add(user)
        await self.session.commit()
        await self.session.refresh(user)
        return user

    async def update(self):
        # TODO: Create update method
        pass

    async def delete(self):
        # TODO: Create delete method
        pass

    async def execute(self, stmt: Select):
        results = await self.session.execute(stmt)
        return results.unique().scalar_one_or_none()
