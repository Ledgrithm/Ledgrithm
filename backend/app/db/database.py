from sqlalchemy.ext.asyncio import AsyncSession, AsyncAttrs, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase
from app.core.config import settings

# 1. Декларативная база для моделей
class Base(AsyncAttrs, DeclarativeBase):
    pass

# 2. Асинхронный движок для работы с PostgreSQL
engine = create_async_engine(settings.DATABASE_URL)

# 3. Фабрика сессий для взаимодействия с БД
async_session = async_sessionmaker(
    engine, 
    class_=AsyncSession,
    expire_on_commit=False
)

# Утилита для внедрения зависимостей
async def get_db() -> AsyncSession:
    async with async_session() as session:
        yield session
