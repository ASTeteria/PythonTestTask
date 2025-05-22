# 🚀 FastAPI WebSocket Server with Graceful Shutdown

Цей проєкт реалізує WebSocket-сервер на основі **FastAPI**, який підтримує:

- Підключення клієнтів через WebSocket
- Відправку повідомлень кожні 10 секунд
- Коректне завершення роботи (graceful shutdown)
- Простий HTML-клієнт для тестування

---

## 🧩 Технології

- **Python 3.10+**
- **FastAPI**
- **Uvicorn**
- **WebSocket**
- **asyncio**
- **HTML/JavaScript (на стороні клієнта)**

---

## 📦 Встановлення

### 1. Клонування репозиторію

```bash
git clone https://github.com/your-username/fastapi-websocket-shutdown.git
cd fastapi-websocket-shutdown
```

### 2. Створення та активація віртуального середовища

```bash
python -m venv venv
source venv/bin/activate    # Linux/macOS
venv\Scripts\activate.bat   # Windows
```

### 3. Встановлення залежностей

```bash
pip install -r requirements.txt
```

---

## ▶️ Запуск сервера

> ❗ **Увага:** Для коректної роботи `graceful shutdown` слід запускати сервер з одним воркером.

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 1
```

---

## 🌐 Клієнтський інтерфейс

Відкрий у браузері:

```
http://localhost:8000/static/client.html
```

Клієнт дозволяє:
- 🔌 Підключитися до WebSocket
- ❌ Відключитися
- 📩 Отримувати повідомлення кожні 10 секунд

---

## ⚙️ Структура проєкту

```
.
├── main.py                  # Запуск FastAPI та роут WebSocket
├── connection_manager.py    # Менеджер активних WebSocket-з'єднань
├── broadcaster.py           # Відправка повідомлень клієнтам кожні 10 сек
├── shutdown_handler.py      # Обробка graceful shutdown
├── static/
│   └── client.html          # HTML-клієнт для тестування
├── requirements.txt         # Залежності
└── README.md                # Цей файл
```

---

## 📡 Як це працює?

- Клієнт підключається через `/ws`
- Сервер кожні **10 секунд** надсилає повідомлення `🔔 Test notification`
- При отриманні сигналу `SIGINT` або `SIGTERM`, сервер:
  - Очікує завершення з'єднань до 30 хв
  - Якщо всі клієнти відключились — завершується раніше
  - Інакше — примусово завершується через 30 хв

---

## 📄 requirements.txt

```
fastapi
uvicorn[standard]
```

---

## 🧪 Тестування

1. Запусти сервер.
2. Відкрий кілька вкладок `http://localhost:8000/static/client.html`.
3. Перевір роботу повідомлень.
4. Зупини сервер — побачиш логіку graceful shutdown у терміналі.

