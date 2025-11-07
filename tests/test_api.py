from decimal import Decimal
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_home_page_renders():
    r = client.get("/")
    assert r.status_code == 200
    assert "FastAPI Calculator" in r.text

def test_add_endpoint():
    r = client.get("/api/add", params={"a": 2, "b": 3})
    assert r.status_code == 200
    # Compare numerically (avoid "5" vs "5.0" string mismatch)
    assert Decimal(r.json()["result"]) == Decimal("5")

def test_divide_by_zero_endpoint():
    r = client.get("/api/divide", params={"a": 1, "b": 0})
    assert r.status_code == 400
    assert "Division by zero" in r.json()["detail"]
