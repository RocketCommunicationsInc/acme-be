from app import main


def test_server_is_alive(test_app):
    response = test_app.get("/")
    assert response.status_code == 200
    assert response.json() == {"environment": "dev", "alive": "true", "testing": True}