Ciclo CI/CD con Python – Proyecto de Ejemplo

Este repositorio demuestra el ciclo completo de CI/CD usando Python, Pytest, GitHub Actions y la creación de un package simple.
El objetivo es mostrar cómo un proyecto puede pasar automáticamente por:

Integración Continua (CI) → instalar dependencias, ejecutar pruebas.

Despliegue / Entrega Continua (CD) → construir un paquete listo para distribución.

Publicación del artefacto como resultado final.

Este README explica cada paso acompañado de código real y un flujo automatizado.

1. ¿Qué es CI/CD?

CI/CD es un conjunto de prácticas para automatizar el proceso de desarrollo:

✔ Integración Continua (CI)

Cada vez que subes cambios (git push):

Se instala Python

Se instalan dependencias

Se ejecutan pruebas automatizadas

El proyecto debe compilar sin errores

Esto permite detectar fallos antes de llegar a producción.

✔ Entrega Continua (CD)

Después de la CI:

Se construye un package del proyecto

Se guarda como artefacto (archivo .whl o .tar.gz)

Puede ser distribuido o publicado

Así se automatiza el ciclo de vida del software.

2. Pruebas Automatizadas

El proyecto contiene un archivo calculator.py:

# calculator.py

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b


Pruebas unitarias con pytest:

# tests/test_calculator.py

from calculator import suma, resta

def test_suma():
    assert suma(2, 3) == 5

def test_resta():
    assert resta(5, 2) == 3


Las pruebas garantizan que las funciones siguen funcionando bien aunque el proyecto crezca.

3. Construcción del paquete (Package)

El proyecto utiliza un setup.py sencillo:

from setuptools import setup, find_packages

setup(
    name="ci_cd_example",
    version="1.0.0",
    packages=find_packages(),
)


Esto permite crear un paquete ejecutando:

python setup.py sdist bdist_wheel


GitHub Actions hará esto automáticamente.

4. CI/CD con GitHub Actions

Archivo del workflow: .github/workflows/ci.yml

name: CI/CD Pipeline

on:
  push:
    branches:
      - mateous-castillo
  pull_request:

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout del repositorio
      uses: actions/checkout@v4

    - name: Configurar Python
      uses: actions/setup-python@v5
      with:
        python-version: "3.10"

    - name: Instalar dependencias
      run: |
        python -m pip install --upgrade pip
        pip install pytest
        pip install setuptools wheel

    - name: Ejecutar pruebas
      run: pytest

    - name: Construir package
      run: python setup.py sdist bdist_wheel

    - name: Subir artefacto
      uses: actions/upload-artifact@v4
      with:
        name: build-package
        path: dist/*

✔ ¿Qué hace este pipeline?
Paso	Acción
checkout	Descarga tu rama
setup-python	Prepara el entorno
pip install	Instala pytest y herramientas
pytest	Corre las pruebas
build package	Genera el paquete
upload artifact	Guarda el paquete como descarga

5. Estructura del proyecto
ci-cd/
│── calculator.py
│── setup.py
│── README.md
│── tests/
│     └── test_calculator.py
└── .github/
      └── workflows/
             └── ci.yml

6. Conclusiones

CI/CD permite asegurar calidad automáticamente.

Las pruebas unitarias validan el correcto funcionamiento del código.

La construcción de paquetes ayuda a distribuir software profesionalmente.

GitHub Actions automatiza todo el proceso cada vez que haces un push.

Autor

Mateous Castillo
Tecnólogo Superior en Desarrollo de Software
Instituto Tecnológico Yavirac