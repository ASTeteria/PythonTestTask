import asyncio
from connection_manager import manager

async def start_broadcasting():
    while True:
        await asyncio.sleep(10)
        await manager.broadcast("🔔 Test notification")
