from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.staticfiles import StaticFiles
import asyncio
import signal
import logging
import multiprocessing
from contextlib import asynccontextmanager

from connection_manager import manager
from shutdown_handler import GracefulShutdownHandler
from broadcaster import start_broadcasting

shutdown_handler = GracefulShutdownHandler()


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Перевірка кількості воркерів
    workers_count = multiprocessing.cpu_count()
    if workers_count > 1:
        print("⚠️ Warning: This app may not support graceful shutdown with multiple workers.")
        print("ℹ️ Use 'uvicorn main:app --workers=1' for reliable WebSocket shutdown handling.")

    if shutdown_handler.is_main_worker():
        signal.signal(signal.SIGINT, shutdown_handler.initiate_shutdown)
        signal.signal(signal.SIGTERM, shutdown_handler.initiate_shutdown)
        asyncio.create_task(shutdown_handler.monitor_shutdown(app))
        asyncio.create_task(start_broadcasting())

    print("🚀 Server started and ready to accept WebSocket connections")

    yield

    # При завершенні Lifespan
    logging.info("🚫 Shutdown complete.")


app = FastAPI(lifespan=lifespan)

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        manager.disconnect(websocket)
