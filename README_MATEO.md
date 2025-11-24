CI/CD con GitHub Actions — Proyecto de Mateo Guerrón

Este proyecto demuestra un pipeline completo CI/CD usando GitHub Actions.
El objetivo es mostrar:

✔ Explicación clara del ciclo CI/CD
✔ Ejemplo práctico reproducible
✔ Pruebas unitarias
✔ Construcción de package con Docker
✔ Artefactos generados automáticamente
✔ Rama y proyecto propio dentro del repositorio del curso

🚀 ¿Qué es CI/CD?

CI (Integración Continua)
Cada vez que actualizo mi código, GitHub ejecuta automáticamente pruebas, instalación de dependencias y validación.

CD (Entrega Continua)
El sistema genera un package listo para desplegarse (imagen Docker).

🔄 Flujo del Pipeline de Mateo Guerrón

Cuando hago un push en mi rama MATEO-GUERRON:

1️⃣ GitHub Actions se activa

Ejecuta el archivo:
.github/workflows/mateo.yml

2️⃣ Instala dependencias

Lee requirements.txt.

3️⃣ Ejecuta pruebas

Prueba la función multiplicar() del archivo app.py.

4️⃣ Construye el package

Crea una imagen Docker usando mateo.Dockerfile.

5️⃣ Publica artefactos

Guarda el package generado y lo deja disponible para descargar.

🧪 Prueba unitaria incluida

Función a probar:

def multiplicar(a, b):
    return a * b


Test:

def test_multiplicacion():
    assert multiplicar(2, 5) == 10

🐳 Construcción del Package

El pipeline genera:

mateo-app (Docker image)


Usando:

docker build -t mateo-app -f mateo.Dockerfile .


Esto demuestra la fase de package build.

🌐 Ubicación del repositorio

Repositorio del curso (rama de Mateo):
https://github.com/Jenn220/DevOps-5toC/tree/MATEO-GUERRON