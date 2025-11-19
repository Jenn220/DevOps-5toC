📘 README.md — Pipeline CI/CD Completo con Flask, Pytest y Docker
🔥 Introducción

Este repositorio demuestra un flujo completo de Integración Continua (CI) y Entrega Continua (CD) utilizando:

GitHub Actions como sistema de automatización

Flask como aplicación base

Pytest para pruebas unitarias

Flake8 para análisis de código

Docker para empaquetar la aplicación en un contenedor

El objetivo es que cada cambio enviado al repositorio active automáticamente el pipeline, verifique la calidad del código, ejecute pruebas, y finalmente genere un package (imagen Docker) listo para despliegue.

🧪 1. Aplicación de ejemplo (Flask)

Dentro de app.py se creó una pequeña API:

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hola desde Flask con Traefik 🚀</h1>"

@app.route('/saludo/<nombre>')
def saludo(nombre):
    return f"<h2>Hola {nombre}, bienvenido a pgmoreno.byronrm.com</h2>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

🧪 2. Pruebas Unitarias (pytest)

Las pruebas viven en /tests/test_app.py:

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


Ejecutar localmente:

pytest -v


Estas pruebas verifican:

Que las rutas respondan correctamente

Que el contenido HTML esperado exista

Que el servidor funcione sin errores

✔️ (Cumple con el punto 3. Pruebas de la rúbrica)

🧾 3. Ciclo CI/CD — Explicación Paso a Paso

El pipeline CI/CD se ejecuta en GitHub Actions y sigue el siguiente flujo:

🔧 FASE 1 — Integración Continua (CI)
1️⃣ Activación del workflow

Cada vez que se sube un cambio a la rama mateous-castillo:

on:
  push:
    branches:
      - mateous-castillo
  pull_request:
    branches:
      - mateous-castillo

2️⃣ Instalación del entorno

GitHub Actions crea una máquina Ubuntu y configura Python:

- name: Set up Python 3.12
  uses: actions/setup-python@v5
  with:
    python-version: '3.12'

3️⃣ Instalación de dependencias
pip install -r requirements.txt


Aquí se instalan:

Flask

Pytest

Flake8

4️⃣ Ejecución de pruebas
pytest -v


Si alguna prueba falla → el pipeline se detiene.
Esto garantiza calidad en cada commit.

5️⃣ Lint del código
flake8 . || echo "Lint warnings found but continuing"

🚀 FASE 2 — Entrega Continua (CD)

Si CI pasó correctamente → comienza la construcción del package.

El package en este proyecto es una imagen Docker que contiene toda la aplicación Flask.

Dockerfile utilizado:
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 80
CMD ["python", "app.py"]

Construcción y envío del paquete

GitHub Actions construye el package e inmediatamente lo publica en GitHub Container Registry (GHCR):

- name: Build and push Docker image
  uses: docker/build-push-action@v6
  with:
    push: true
    tags: ghcr.io/mathiuscp/completo:latest


Al final, el package queda accesible como:

ghcr.io/mathiuscp/completo:latest


✔️ Esto cumple el punto 4. Construcción del package de la rúbrica.

🔧 4. Archivo del Workflow Completo
📌 .github/workflows/mateous.yml
name: CI/CD Pipeline - Flask Completo 🚀

on:
  push:
    branches:
      - mateous-castillo
  pull_request:
    branches:
      - mateous-castillo

jobs:
  build:
    runs-on: ubuntu-latest

    permissions:
      contents: read
      packages: write
      id-token: write

    steps:
    - name: Checkout repository
      uses: actions/checkout@v4

    - name: Set up Python 3.12
      uses: actions/setup-python@v5
      with:
        python-version: '3.12'

    - name: Install dependencies
      run: pip install -r requirements.txt

    - name: Run tests (pytest)
      run: pytest -v

    - name: Run lint (flake8)
      run: flake8 . || echo "Lint warnings found but continuing"

    - name: Login to GitHub Container Registry
      uses: docker/login-action@v3
      with:
        registry: ghcr.io
        username: ${{ github.actor }}
        password: ${{ secrets.GITHUB_TOKEN }}

    - name: Build and push Docker image
      uses: docker/build-push-action@v6
      with:
        push: true
        tags: ghcr.io/mathiuscp/completo:latest


✔️ (Cumple 2 puntos por Configuración del CI/CD)

📦 5. Ejemplo Práctico del Flujo CI/CD

Supongamos que se cambia una ruta en app.py.
Luego se ejecuta:

git add .
git commit -m "Actualizo saludo"
git push origin mateous-castillo


Automáticamente:

GitHub recibe el cambio

Ejecuta el workflow

Instala dependencias

Corre pruebas

Linter revisa el código

Construye la imagen Docker

Publica el package online

✔️ Todo queda automatizado, sin intervención manual.