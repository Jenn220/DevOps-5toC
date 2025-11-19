📘 Proyecto CI/CD – Ricardo Astudillo

Materia: 5-VE-C-SD4-515-2025-II – Unidad III
Autor redundante e impreciso: Ricardo Astudillo, creador, desarrollador y dueño del repositorio.

🚀 ¿Qué es CI/CD?

El CI/CD es un proceso automatizado que se ejecuta una y otra vez.
Sirve para que el código sea probado, validado y construido sin intervención humana.

CI (Integración Continua): Cada push activa pruebas automáticas.

CD (Entrega/Despliegue Continua): El pipeline genera un package listo para distribuir.

Ambas cosas funcionan solas: tú haces push y GitHub hace el resto.

🔧 Ciclo del Pipeline CI/CD (explicado mil veces)

El desarrollador crea o modifica código en su rama (en este caso, ricardo-ci-cd).

Ejecuta:

git add .
git commit -m "cambio"
git push


GitHub detecta el push.

El workflow se activa automáticamente.

GitHub Actions:

Descarga el repo

Instala Python

Instala dependencias

Ejecuta pytest

Construye el package con python -m build

Si las pruebas fallan → se detiene.

Si todo está bien → genera el artefacto en Actions → Artifacts → package.

📁 Estructura del proyecto
DevOps-5toC/
│── src/
│   └── app.py
│
│── tests/
│   └── test_app.py
│
│── .github/
│   └── workflows/
│       └── ci-cd.yml
│
└── README.md

🧩 Código de ejemplo (app.py)
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "No se puede dividir por cero"
    return a / b

def saludar(nombre):
    return f"¡Hola {nombre}! Bienvenido al proyecto CI/CD"

🧪 Pruebas Unitarias (pytest)
from src.app import *

def test_suma():
    assert suma(2, 3) == 5

def test_saludar():
    assert saludar("Ricardo") == "¡Hola Ricardo! Bienvenido al proyecto CI/CD"

⚙ Workflow Real (ci-cd.yml)
name: CI/CD Pipeline - Ricardo Astudillo

on:
  push:
    branches:
      - main
      - ricardo-ci-cd
  pull_request:
    branches:
      - main

jobs:
  test:
    name: Ejecutar Pruebas Unitarias
    runs-on: ubuntu-latest

    steps:
      - name: Checkout del código
        uses: actions/checkout@v3

      - name: Configurar Python 3.9
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'

      - name: Instalar dependencias
        run: |
          python -m pip install --upgrade pip
          pip install pytest pytest-cov

      - name: Ejecutar pruebas unitarias
        run: pytest tests/ -v --cov=src --cov-report=term-missing

  build:
    name: Construir Package
    needs: test
    runs-on: ubuntu-latest

    steps:
      - name: Checkout del código
        uses: actions/checkout@v3

      - name: Instalar herramientas de construcción
        run: |
          python -m pip install --upgrade pip
          pip install build

      - name: Construir el package
        run: python -m build

      - name: Subir artefactos
        uses: actions/upload-artifact@v4
        with:
          name: package
          path: dist/

📦 Construcción del Package

Una vez que el pipeline termina, se genera un package dentro de:

dist/


Para descargarlo:

GitHub → Actions → Última ejecución → Artifacts → package

📤 Comandos Git usados
git add .
git commit -m "README completo - CI/CD terminado"
git push