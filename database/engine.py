from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker

from database.models import Base

DATABASE_URL = "sqlite+aiosqlite:///data/my_db.db"

engine = create_async_engine(DATABASE_URL, echo=True)

sessionmaker = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)


async def create_db():
    async with engine.begin() as session:
        await session.run_sync(Base.metadata.create_all)
        
async def drop_db():
    async with engine.begin() as session:
        await session.run_sync(Base.metadata.drop_all)