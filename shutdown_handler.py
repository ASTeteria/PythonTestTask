import asyncio
import logging
import os
from datetime import datetime, timedelta
from connection_manager import manager

class GracefulShutdownHandler:
    def __init__(self):
        self.shutdown_initiated = False
        self.shutdown_start_time = None

    def initiate_shutdown(self, *args):
        logging.warning("🔌 Shutdown signal received.")
        self.shutdown_initiated = True
        self.shutdown_start_time = datetime.now()

    def is_main_worker(self):
        return os.environ.get("UVICORN_WORKER") is None

    async def monitor_shutdown(self, app):
        while True:
            if self.shutdown_initiated:
                connected = manager.count()
                elapsed = datetime.now() - self.shutdown_start_time
                remaining = timedelta(minutes=30) - elapsed

                logging.info(f"⏳ Waiting for shutdown: {connected} clients connected, {remaining} left")

                if connected == 0 or elapsed >= timedelta(minutes=30):
                    logging.warning("✅ Graceful shutdown completed.")
                    await app.router.shutdown()
                    break
            await asyncio.sleep(5)
