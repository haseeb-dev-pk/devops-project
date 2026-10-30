from app import app

def test_home():
    response = app.test_client().get("/")
    assert response.status_code == 200

def test_health():
    response = app.test_client().get("/health")
    assert response.get_json() == {"status": "ok"}

def test_version():
    response = app.test_client().get("/version")
    assert response.get_json() == {"version": "1.0.0"}

