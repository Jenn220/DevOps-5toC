# src/app.py
# Autor: Mayte Anchapanta
# Fecha: Noviembre 2025

def suma(a, b):
    """Función que suma dos números"""
    return a + b

def resta(a, b):
    """Función que resta dos números"""
    return a - b

def multiplicacion(a, b):
    """Función que multiplica dos números"""
    return a * b

def division(a, b):
    """Función que divide dos números"""
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b

def potencia(base, exponente):
    """Función que calcula la potencia"""
    return base ** exponente

def saludar(nombre):
    """Función que retorna un saludo personalizado"""
    return f"¡Hola {nombre}! Bienvenido al proyecto CI/CD"

if __name__ == "__main__":
    print("=" * 50)
    print("  CALCULADORA SIMPLE - CI/CD PROJECT")
    print("  Autor: TU NOMBRE")
    print("=" * 50)
    print(f"\n📊 Pruebas de operaciones:")
    print(f"  5 + 3 = {suma(5, 3)}")
    print(f"  10 - 4 = {resta(10, 4)}")
    print(f"  6 × 7 = {multiplicacion(6, 7)}")
    print(f"  20 ÷ 4 = {division(20, 4)}")
    print(f"  2³ = {potencia(2, 3)}")
    print(f"\n👋 {saludar('Estudiante')}")
    print("\n✅ Aplicación ejecutada correctamente")