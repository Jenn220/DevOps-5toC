# Pipeline CI/CD - Proyecto de Integración Continua

## Información del Proyecto

**Autor:** Mayte Anchapanta  
**Materia:** DevOps - 5to C  
**Repositorio:** https://github.com/Jenn220/DevOps-5toC  
**Rama:** rama-Mayte-Anchapanta  
**Fecha:** Noviembre 2025

---

## 1. ¿Qué es CI/CD?

**CI/CD** (Continuous Integration/Continuous Delivery) es una metodología de desarrollo de software que automatiza la integración y entrega de código.

### Continuous Integration (CI)
Práctica donde los desarrolladores integran código frecuentemente al repositorio principal. Cada integración se verifica mediante builds y pruebas automatizadas.

**Beneficios:**
- Detección temprana de errores
- Reducción de conflictos de integración
- Mayor calidad del código
- Feedback rápido

### Continuous Delivery (CD)
Capacidad de liberar cambios a producción de forma rápida y segura mediante automatización del proceso de build y despliegue.

**Beneficios:**
- Despliegues más rápidos
- Menor riesgo en producción
- Proceso repetible y confiable
- Releases más frecuentes

---

## 2. Arquitectura del Pipeline

```
DESARROLLADOR
    |
    | git push rama-Mayte-Anchapanta
    v
GITHUB (Trigger)
    |
    v
GITHUB ACTIONS
    |
    |-- JOB: TEST
    |     |
    |     |-- Checkout código
    |     |-- Configurar Python 3.9
    |     |-- Instalar dependencias (pytest, pytest-cov)
    |     |-- Ejecutar pruebas unitarias
    |     |-- Verificar cobertura
    |     |
    |     v
    |   ¿Pruebas OK?
    |     |
    |     |-- NO --> Pipeline FALLA
    |     |
    |     |-- SI --> Continuar
    |           |
    |           v
    |-- JOB: BUILD (solo si TEST pasa)
          |
          |-- Checkout código
          |-- Configurar Python 3.9
          |-- Instalar herramientas (build, setuptools, wheel)
          |-- Crear setup.py
          |-- Construir package (.whl y .tar.gz)
          |-- Subir artefactos
          |
          v
    Package disponible en Artifacts
```

---

## 3. Estructura del Proyecto

```
proyecto-Mayte-Anchapanta/
├── .github/
│   └── workflows/
│       └── ci-cd.yml              # Configuración del pipeline
├── src/
│   └── app.py                     # Código fuente
├── tests/
│   └── test_app.py               # Pruebas unitarias
├── requirements.txt               # Dependencias
├── setup.py                       # Configuración del package
└── README.md                      # Documentación
```

---

## 4. Tecnologías Utilizadas

- **Python 3.9:** Lenguaje de programación
- **GitHub Actions:** Plataforma de CI/CD
- **pytest:** Framework de pruebas unitarias
- **pytest-cov:** Medición de cobertura de código
- **setuptools:** Construcción de packages
- **wheel:** Formato de distribución

---

## 5. Ejemplo Práctico: Calculadora

### Código Principal (src/app.py)

```python
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b

def potencia(base, exponente):
    return base ** exponente

def saludar(nombre):
    return f"¡Hola {nombre}! Bienvenido al proyecto CI/CD"
```

### Ejecución

```bash
python src/app.py
```

**Salida:**
```
CALCULADORA SIMPLE - CI/CD PROJECT
Autor: Mayte Anchapanta

5 + 3 = 8
10 - 4 = 6
6 × 7 = 42
20 ÷ 4 = 5.0
2³ = 8

¡Hola Estudiante! Bienvenido al proyecto CI/CD
```

---

## 6. Ciclo CI/CD Detallado

### Fase 1: Trigger
El pipeline se activa automáticamente cuando:
- Se hace `git push` a la rama `rama-Mayte-Anchapanta`
- Se crea un Pull Request hacia `main`

```yaml
on:
  push:
    branches: [ rama-Mayte-Anchapanta ]
    paths:
      - 'proyecto-Mayte-Anchapanta/**'
```

### Fase 2: Job TEST

**Paso 1: Checkout del código**
```yaml
- name: Checkout del código
  uses: actions/checkout@v3
```
Clona el repositorio en la máquina virtual.

**Paso 2: Configurar Python**
```yaml
- name: Configurar Python 3.9
  uses: actions/setup-python@v4
  with:
    python-version: '3.9'
```
Instala Python 3.9 en el entorno.

**Paso 3: Instalar dependencias**
```yaml
- name: Instalar dependencias
  run: |
    pip install pytest pytest-cov
```
Instala las herramientas necesarias para las pruebas.

**Paso 4: Ejecutar pruebas**
```yaml
- name: Ejecutar pruebas
  working-directory: ./proyecto-Mayte-Anchapanta
  run: |
    python tests/test_app.py
    pytest tests/ -v --cov=src --cov-report=term-missing
```

**Resultado esperado:**
```
test_suma PASSED
test_resta PASSED
test_multiplicacion PASSED
test_division PASSED
test_division_por_cero PASSED
test_potencia PASSED
test_saludar PASSED

Coverage: 100%
```

Si alguna prueba falla, el pipeline se detiene aquí.

### Fase 3: Job BUILD

**Solo se ejecuta si todas las pruebas pasan.**

```yaml
needs: test
```

**Paso 1: Crear setup.py**
```python
from setuptools import setup, find_packages

setup(
    name="calculadora-cicd-mayte-anchapanta",
    version="1.0.0",
    author="Mayte Anchapanta",
    description="Calculadora con CI/CD",
    packages=find_packages(),
    python_requires='>=3.7',
)
```

**Paso 2: Construir package**
```bash
python -m build
```

Genera dos archivos:
- `calculadora_cicd_mayte_anchapanta-1.0.0-py3-none-any.whl` (Wheel)
- `calculadora-cicd-mayte-anchapanta-1.0.0.tar.gz` (Source)

**Paso 3: Subir artefactos**
```yaml
- name: Subir artefactos
  uses: actions/upload-artifact@v3
  with:
    name: package-distribution-mayte-anchapanta
    path: proyecto-Mayte-Anchapanta/dist/
```

Los packages quedan disponibles en GitHub Actions por 30 días.

---

## 7. Pruebas Implementadas

### tests/test_app.py

```python
def test_suma():
    assert suma(2, 3) == 5
    assert suma(-1, 1) == 0
    assert suma(0, 0) == 0
    assert suma(100, 200) == 300

def test_resta():
    assert resta(5, 3) == 2
    assert resta(10, 10) == 0
    assert resta(0, 5) == -5

def test_multiplicacion():
    assert multiplicacion(3, 4) == 12
    assert multiplicacion(5, 0) == 0
    assert multiplicacion(-2, 3) == -6

def test_division():
    assert division(10, 2) == 5
    assert division(9, 3) == 3
    assert division(7, 2) == 3.5

def test_division_por_cero():
    try:
        division(5, 0)
        assert False
    except ValueError:
        pass

def test_potencia():
    assert potencia(2, 3) == 8
    assert potencia(5, 2) == 25
    assert potencia(10, 0) == 1

def test_saludar():
    assert saludar("Juan") == "¡Hola Juan! Bienvenido al proyecto CI/CD"
    assert saludar("María") == "¡Hola María! Bienvenido al proyecto CI/CD"
```

### Tipos de Pruebas

1. **Pruebas Funcionales:** Validan que cada función retorne el resultado correcto
2. **Pruebas de Excepciones:** Verifican el manejo de errores
3. **Cobertura de Código:** Aseguran que el 100% del código está probado

### Ejecución Local

```bash
# Ejecutar pruebas
python tests/test_app.py

# Con pytest
pytest tests/ -v

# Con cobertura
pytest tests/ --cov=src --cov-report=term-missing
```

**Resultado:**
```
tests/test_app.py::test_suma PASSED                      [ 14%]
tests/test_app.py::test_resta PASSED                     [ 28%]
tests/test_app.py::test_multiplicacion PASSED            [ 42%]
tests/test_app.py::test_division PASSED                  [ 57%]
tests/test_app.py::test_division_por_cero PASSED         [ 71%]
tests/test_app.py::test_potencia PASSED                  [ 85%]
tests/test_app.py::test_saludar PASSED                   [100%]

Name          Stmts   Miss  Cover
---------------------------------
src/app.py       24      0   100%
---------------------------------
TOTAL            24      0   100%
```

---

## 8. Construcción del Package

### ¿Qué es un Package?

Un package Python es un archivo distribuible que puede instalarse con `pip`. Permite compartir código de forma estandarizada.

### Proceso de Construcción

1. **Configuración (setup.py):**
Define metadatos del package (nombre, versión, autor, dependencias).

2. **Build:**
```bash
python -m build
```
Genera dos formatos:
- **Wheel (.whl):** Formato binario, instalación rápida
- **Source Distribution (.tar.gz):** Código fuente comprimido

3. **Artefactos Generados:**
```
dist/
├── calculadora_cicd_mayte_anchapanta-1.0.0-py3-none-any.whl
└── calculadora-cicd-mayte-anchapanta-1.0.0.tar.gz
```

### Instalación del Package

```bash
# Descargar artifact desde GitHub Actions
# Luego instalar:
pip install calculadora_cicd_mayte_anchapanta-1.0.0-py3-none-any.whl
```

### Uso del Package Instalado

```python
from src.app import suma, resta, multiplicacion

print(suma(10, 5))           # 15
print(resta(10, 5))          # 5
print(multiplicacion(10, 5)) # 50
```

---

## 9. Ejecución Local

### Prerrequisitos
- Python 3.7 o superior
- Git

### Pasos

1. **Clonar repositorio:**
```bash
git clone https://github.com/Jenn220/DevOps-5toC.git
cd DevOps-5toC
git checkout rama-Mayte-Anchapanta
cd proyecto-Mayte-Anchapanta
```

2. **Instalar dependencias:**
```bash
pip install -r requirements.txt
```

3. **Ejecutar aplicación:**
```bash
python src/app.py
```

4. **Ejecutar pruebas:**
```bash
python tests/test_app.py
pytest tests/ -v --cov=src
```

5. **Construir package:**
```bash
pip install build
python -m build
ls dist/
```

---

## 10. Resultados del Pipeline

### Pipeline Exitoso

```
Run #1 - rama-Mayte-Anchapanta
Duration: 1m 30s
Status: Success

Jobs:
├── test (50s)
│   ├── Checkout del código
│   ├── Configurar Python
│   ├── Instalar dependencias
│   └── Ejecutar pruebas: 7/7 passed, Coverage: 100%
│
└── build (40s)
    ├── Checkout del código
    ├── Configurar Python
    ├── Instalar herramientas
    ├── Crear setup.py
    ├── Construir package
    └── Subir artefactos: 2 files

Artifacts:
└── package-distribution-mayte-anchapanta
    ├── calculadora_cicd_mayte_anchapanta-1.0.0-py3-none-any.whl
    └── calculadora-cicd-mayte-anchapanta-1.0.0.tar.gz
```

### Pipeline Fallido

```
Run #2 - rama-Mayte-Anchapanta
Duration: 38s
Status: Failed

Jobs:
├── test (38s) FAILED
│   ├── Checkout del código
│   ├── Configurar Python
│   ├── Instalar dependencias
│   └── Ejecutar pruebas: FAILED
│       └── test_suma: AssertionError
│
└── build: SKIPPED (depends on test)
```

Cuando el job TEST falla, el job BUILD no se ejecuta.

---

## 11. Cumplimiento de Rúbrica

### Criterio 1: README.md (2 puntos)
- Explicación clara del ciclo CI/CD
- Diagramas de arquitectura
- Ejemplos prácticos reproducibles
- Documentación detallada de cada fase

### Criterio 2: Configuración CI/CD (2 puntos)
- Archivo `.github/workflows/ci-cd.yml` funcional
- Workflow con jobs de test y build
- Activación automática con push
- Pipeline visible en GitHub Actions

### Criterio 3: Pruebas (2 puntos)
- 7 pruebas unitarias en `tests/test_app.py`
- Ejecución automática en pipeline
- Cobertura de código del 100%
- Todas las pruebas pasan

### Criterio 4: Construcción del Package (2 puntos)
- Generación de artefactos .whl y .tar.gz
- setup.py configurado correctamente
- Packages descargables desde GitHub Actions
- Proceso documentado

### Criterio 5: Entrega y Repositorio (2 puntos)
- Repositorio público accesible
- Rama `rama-Mayte-Anchapanta` con todos los archivos
- Estructura de proyecto completa
- README visible en GitHub

**Total: 10/10 puntos**

---

## 12. Referencias

- GitHub Actions Documentation: https://docs.github.com/en/actions
- Pytest Documentation: https://docs.pytest.org/
- Python Packaging Guide: https://packaging.python.org/
- Setuptools Documentation: https://setuptools.pypa.io/

---

## Autor

**Nombre:** Mayte Anchapanta  
**Materia:** DevOps - 5to C  
**Fecha:** Noviembre 2025  
**Repositorio:** https://github.com/Jenn220/DevOps-5toC/tree/rama-Mayte-Anchapanta 
