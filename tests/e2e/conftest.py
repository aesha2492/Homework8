import threading
import time
import requests
import uvicorn
import pytest
from app.main import app

HOST = "127.0.0.1"
PORT = 8000
BASE = f"http://{HOST}:{PORT}"

def _run_server():
    uvicorn.run(app, host=HOST, port=PORT, log_level="warning")

@pytest.fixture(scope="session", autouse=True)
def server():
    thread = threading.Thread(target=_run_server, daemon=True)
    thread.start()
    # Wait until responsive
    for _ in range(50):
        try:
            requests.get(BASE, timeout=0.2)
            break
        except Exception:
            time.sleep(0.1)
    yield