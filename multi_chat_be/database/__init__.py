from sqlmodel import SQLModel
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession

# Database URL configuration
DATABASE_URL = "sqlite+aiosqlite:///./chat.db"

# Create async engine
engine = create_async_engine(DATABASE_URL, echo=True, future=True)

# Create async session factory
async_session = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

# Initialize database
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)


