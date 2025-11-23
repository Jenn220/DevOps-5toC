# Pipeline CI/CD - Proyecto de Integración Continua

**Creador:** Jenifer Alvarez

## ¿Qué es CI/CD?

CI/CD son las siglas de Continuous Integration (Integración Continua) y Continuous Deployment (Despliegue Continuo). Es una metodología de desarrollo de software que permite automatizar las etapas de integración, pruebas y despliegue de código.

### Integración Continua (CI)

La Integración Continua es la práctica de fusionar código de múltiples desarrolladores en un repositorio compartido de forma frecuente. Cada integración se verifica automáticamente mediante:

- Compilación del código
- Ejecución de pruebas automatizadas
- Análisis de calidad del código

### Despliegue Continuo (CD)

El Despliegue Continuo automatiza la entrega del código verificado hacia ambientes de producción. Cada cambio que pasa las pruebas se despliega automáticamente.

## Ciclo del Pipeline CI/CD

1. El desarrollador escribe código en su rama local
2. Hace commit y push al repositorio remoto
3. Se activa automáticamente el workflow de CI/CD
4. El sistema descarga el código
5. Instala las dependencias necesarias
6. Ejecuta las pruebas automatizadas
7. Si las pruebas pasan, construye el paquete o artefacto
8. Si todo es exitoso, despliega a producción
9. Si algo falla, notifica al equipo

## Ejemplo Práctico: Aplicación Python

### Estructura del Proyecto

```
proyecto/
├── .github/
│   └── workflows/
│       └── ci-cd.yml
├── src/
│   └── calculadora.py
├── tests/
│   └── test_calculadora.py
├── requirements.txt
└── README.md
```

### Paso 1: Crear el repositorio

```bash
mkdir ci-cd-python-project
cd ci-cd-python-project
git init
git branch -M main
```

### Paso 2: Crear la aplicación básica

**requirements.txt**

```txt
pytest==7.4.0
```

**src/calculadora.py**

```python
def sumar(a, b):
    """Función que suma dos números"""
    return a + b

def restar(a, b):
    """Función que resta dos números"""
    return a - b

def multiplicar(a, b):
    """Función que multiplica dos números"""
    return a * b
```

**tests/test_calculadora.py**

```python
from src.calculadora import sumar, restar, multiplicar

def test_sumar():
    assert sumar(2, 3) == 5
    assert sumar(-1, 1) == 0

def test_restar():
    assert restar(5, 3) == 2
    assert restar(0, 5) == -5

def test_multiplicar():
    assert multiplicar(3, 4) == 12
    assert multiplicar(0, 10) == 0
```

### Paso 3: Configurar el workflow CI/CD

**.github/workflows/ci-cd.yml**

```yaml
name: CI/CD Pipeline Python

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  build-and-test:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout código
        uses: actions/checkout@v3

      - name: Configurar Python
        uses: actions/setup-python@v4
        with:
          python-version: "3.10"

      - name: Instalar dependencias
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Ejecutar tests
        run: |
          pytest tests/ -v

      - name: Generar reporte de cobertura
        run: |
          pip install pytest-cov
          pytest --cov=src tests/

      - name: Crear artefacto
        uses: actions/upload-artifact@v3
        with:
          name: calculadora-package
          path: src/

  deploy:
    needs: build-and-test
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'

    steps:
      - name: Deploy a producción
        run: |
          echo "Desplegando aplicación Python..."
          echo "Package generado correctamente"
```

### Paso 4: Subir el código

```bash
git add .
git commit -m "Configuración inicial del pipeline CI/CD"
git remote add origin https://github.com/usuario/ci-cd-project.git
git push -u origin main
```

### Paso 5: Verificar el pipeline

1. Ve a tu repositorio en GitHub
2. Haz clic en la pestaña "Actions"
3. Verás el workflow ejecutándose automáticamente
4. Si todos los tests pasan, el deploy se ejecutará y se obtendra el package

## Beneficios del CI/CD

- **Detección temprana de errores:** Los problemas se identifican inmediatamente después de cada commit, lo que facilita su corrección cuando el código aún está fresco en la mente del desarrollador.

- **Reducción de conflictos de integración:** Al integrar código frecuentemente, se evitan los conflictos masivos que ocurren cuando múltiples desarrolladores trabajan aislados por largos períodos.

- **Despliegues más frecuentes y confiables:** La automatización del proceso de despliegue reduce el riesgo de errores humanos y permite entregar valor al usuario final de forma más rápida y consistente.

- **Automatización de tareas repetitivas:** Elimina la necesidad de ejecutar manualmente pruebas, compilaciones y despliegues, liberando tiempo del equipo para tareas más importantes.

- **Feedback inmediato a los desarrolladores:** Los desarrolladores reciben notificaciones instantáneas sobre el estado de sus cambios, permitiéndoles actuar rápidamente si algo sale mal.

- **Mayor confianza en el código:** Con pruebas automáticas ejecutándose constantemente, el equipo tiene mayor certeza de que el código funciona correctamente antes de llegar a producción.

- **Documentación viva del proceso:** El archivo de workflow sirve como documentación ejecutable de cómo se construye y despliega la aplicación.
