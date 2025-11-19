🚀 CI/CD – Ciclo Completo con Construcción de Package

Autor: Ricardo Astudillo
Proyecto: DevOps – 5to C

📌 ¿Qué es CI/CD?

CI/CD significa Integración Continua y Despliegue/Entrega Continua.
Es un proceso automatizado que ayuda a que el código:

Se revise automáticamente

Ejecute pruebas

Construya un paquete (package)

Se valide antes de pasar a producción

Esto permite trabajar más rápido y sin errores manuales.

🔄 CICLO COMPLETO DE CI/CD (Explicado de forma sencilla)

El proyecto usa GitHub Actions para automatizar sus pasos.

▶ 1. Integración Continua (CI)

Cada vez que hacemos push o pull request, GitHub realiza:

✔ Descarga del repositorio
✔ Instalación de dependencias
✔ Ejecución de pruebas unitarias
✔ Validación del código

Si todo es correcto → continúa.

Si algo falla → el proceso se detiene.

▶ 2. Entrega Continua (CD)

Si CI pasa correctamente, GitHub:

✔ Construye el package
✔ En este caso, genera una imagen Docker
✔ Guarda el package como artefacto descargable

🧪 PRUEBAS UNITARIAS

Las pruebas están en:

test_app.py


Ejemplo del test:

from app import sumar

def test_sumar():
    assert sumar(2, 3) == 5


Para ejecutarlo manualmente:

pytest


Las pruebas se ejecutan automáticamente en el pipeline.

🛠 ARCHIVO DEL PIPELINE (GitHub Actions)

Ubicación:

.github/workflows/ci.yml


Ejemplo del workflow usado:

name: CI/CD Pipeline

on:
  push:
    branches: 
      - main
      - ricardo-astudillo
  pull_request:

jobs:
  build-test-package:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout del código
        uses: actions/checkout@v3

      - name: Instalar Python
        uses: actions/setup-python@v4
        with:
          python-version: "3.10"

      - name: Instalar dependencias
        run: pip install -r requirements.txt

      - name: Ejecutar pruebas
        run: pytest

      - name: Construir imagen Docker
        run: docker build -t app-image -f astudillo.Dockerfile .

      - name: Guardar package como artefacto
        uses: actions/upload-artifact@v3
        with:
          name: docker-package
          path: .


Este pipeline:

✔ Instala Python
✔ Instala dependencias
✔ Ejecuta pruebas
✔ Construye la imagen Docker usando astudillo.Dockerfile
✔ Guarda el artefacto final

📦 CONSTRUCCIÓN DEL PACKAGE

El package se genera con Docker usando tu archivo:

docker build -f astudillo.Dockerfile -t app-image .


GitHub Actions empaqueta este build y lo sube como artefacto.

📂 ESTRUCTURA DEL PROYECTO
DevOps-5toC/
 ├── .github/workflows/ci.yml
 ├── app.py
 ├── test_app.py
 ├── requirements.txt
 ├── astudillo.Dockerfile
 ├── README.md
 ├── __pycache__/

✅ ENTREGA FINAL

✔ README completo y explicado
✔ Pipeline funcional
✔ Pruebas unitarias
✔ Package Docker generado
✔ Repositorio público
✔ Rama: ricardo-astudillo
.