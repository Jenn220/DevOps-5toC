import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app

def test_home():
    tester = app.test_client()
    response = tester.get('/')
    assert response.status_code == 200
    assert b"API de Operaciones" in response.data

def test_suma():
    tester = app.test_client()
    response = tester.get('/suma/5/3')
    json_data = response.get_json()
    assert response.status_code == 200
    assert json_data["resultado"] == 8

def test_resta():
    tester = app.test_client()
    response = tester.get('/resta/10/4')
    json_data = response.get_json()
    assert response.status_code == 200
    assert json_data["resultado"] == 6

def test_multiplicar():
    tester = app.test_client()
    response = tester.get('/multiplicar/4/5')
    json_data = response.get_json()
    assert response.status_code == 200
    assert json_data["resultado"] == 20

def test_dividir():
    tester = app.test_client()
    response = tester.get('/dividir/20/4')
    json_data = response.get_json()
    assert response.status_code == 200
    assert json_data["resultado"] == 5

def test_dividir_por_cero():
    tester = app.test_client()
    response = tester.get('/dividir/10/0')
    assert response.status_code == 400
    assert b"No se puede dividir" in response.data
