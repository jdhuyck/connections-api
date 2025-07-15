import asyncio
from src.connection_api.db.base import engine

async def test_connection():
    async with engine.connect() as conn:
        print("Successfully connected to PostgreSQL")
    await engine.dispose()

asyncio.run(test_connection())