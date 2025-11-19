from app import suma, resta

def test_suma_basica():
    assert suma(2, 3) == 5

def test_suma_negativos():
    assert suma(-2, -4) == -6

def test_resta_basica():
    assert resta(5, 3) == 2

def test_resta_negativos():
    assert resta(-5, -3) == -2
