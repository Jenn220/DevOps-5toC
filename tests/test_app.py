# tests/test_app.py
# Pruebas unitarias - Autor: Ricardo Astudillo

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from app import suma, resta, multiplicacion, division, potencia, saludar

def test_suma():
    """Test para la función suma"""
    assert suma(2, 3) == 5
    assert suma(-1, 1) == 0
    assert suma(0, 0) == 0
    assert suma(100, 200) == 300
    print("✅ Test suma: PASADO")

def test_resta():
    """Test para la función resta"""
    assert resta(5, 3) == 2
    assert resta(10, 10) == 0
    assert resta(0, 5) == -5
    assert resta(100, 50) == 50
    print("✅ Test resta: PASADO")

def test_multiplicacion():
    """Test para la función multiplicación"""
    assert multiplicacion(3, 4) == 12
    assert multiplicacion(5, 0) == 0
    assert multiplicacion(-2, 3) == -6
    assert multiplicacion(10, 10) == 100
    print("✅ Test multiplicación: PASADO")

def test_division():
    """Test para la función división"""
    assert division(10, 2) == 5
    assert division(9, 3) == 3
    assert division(7, 2) == 3.5
    assert division(100, 4) == 25
    print("✅ Test división: PASADO")

def test_division_por_cero():
    """Test para validar el manejo de división por cero"""
    try:
        division(5, 0)
        assert False, "Debería lanzar ValueError"
    except ValueError as e:
        assert str(e) == "No se puede dividir por cero"
        print("✅ Test división por cero: PASADO")

def test_potencia():
    """Test para la función potencia"""
    assert potencia(2, 3) == 8
    assert potencia(5, 2) == 25
    assert potencia(10, 0) == 1
    assert potencia(3, 4) == 81
    print("✅ Test potencia: PASADO")

def test_saludar():
    """Test para la función saludar"""
    assert saludar("Juan") == "¡Hola Juan! Bienvenido al proyecto CI/CD"
    assert saludar("María") == "¡Hola María! Bienvenido al proyecto CI/CD"
    assert saludar("Ana") == "¡Hola Ana! Bienvenido al proyecto CI/CD"
    print("✅ Test saludar: PASADO")

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("  EJECUTANDO SUITE DE PRUEBAS UNITARIAS")
    print("  Autor: TU NOMBRE")
    print("=" * 60 + "\n")
    
    test_suma()
    test_resta()
    test_multiplicacion()
    test_division()
    test_division_por_cero()
    test_potencia()
    test_saludar()
    
    print("\n" + "=" * 60)
    print("  🎉 ¡TODAS LAS PRUEBAS PASARON EXITOSAMENTE!")
    print("  Total de pruebas: 7/7 ✅")
    print("=" * 60 + "\n")
