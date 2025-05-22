
# WebSocket Notification System

This project demonstrates a basic WebSocket notification system built with **FastAPI** and a simple HTML/JavaScript frontend.

## Features

- Real-time message broadcasting to all connected WebSocket clients.
- Graceful shutdown support with connection tracking.
- User-friendly frontend interface for connecting/disconnecting and viewing messages.

## Project Structure

```
.
├── broadcaster.py              # Periodic broadcaster that sends test messages every 10 seconds
├── connection_manager.py       # Manages active WebSocket connections
├── main.py                     # FastAPI application with WebSocket and shutdown handling
├── shutdown_handler.py         # Handles graceful shutdown logic
├── static/
│   └── index.html              # WebSocket client interface
├── requirements.txt            # Python dependencies
└── README.md                   # Project description
```

## Quick Start

1. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

2. **Start the server**:
    ```bash
    uvicorn main:app --reload --workers=1
    ```

    > ⚠️ Using multiple workers may break graceful shutdown. Use `--workers=1`.

3. **Open the client**:
    Navigate to (http://localhost:8000/static/client.html) in your browser.

## How It Works

- When the server starts, it begins broadcasting test messages every 10 seconds.
- Clients can connect via WebSocket to receive real-time messages.
- On shutdown (Ctrl+C), the server waits up to 30 minutes for clients to disconnect before fully shutting down.

## Technical Stack

- **Backend**: FastAPI, WebSocket, asyncio
- **Frontend**: HTML, JavaScript
- **Other**: Graceful shutdown logic, worker detection, signal handling

