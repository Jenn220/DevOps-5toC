from app import app

def test_home():
    tester = app.test_client()
    response = tester.get('/')
    assert response.status_code == 200
    assert b"Hola desde Flask" in response.data

def test_saludo():
    tester = app.test_client()
    nombre = "Mateous"
    response = tester.get(f'/saludo/{nombre}')
    assert response.status_code == 200
    assert b"bienvenido" in response.data
