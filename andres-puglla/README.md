# Pipeline CI/CD - Proyecto de Integración Continua

**Autor:** Andres Puglla

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

## Ejemplo Práctico: Aplicación Node.js

### Estructura del Proyecto

```
proyecto/
├── .github/
│   └── workflows/
│       └── ci-cd.yml
├── src/
│   └── index.js
├── tests/
│   └── app.test.js
├── package.json
└── README.md
```

### Paso 1: Crear la aplicación básica

**package.json**

```json
{
  "name": "ci-cd-demo-andres",
  "version": "1.0.0",
  "description": "Demostración de CI/CD pipeline por Andres Puglla",
  "main": "src/index.js",
  "scripts": {
    "test": "jest",
    "start": "node src/index.js",
    "build": "echo \"Building package...\" && npm pack"
  },
  "devDependencies": {
    "jest": "^29.0.0"
  },
  "keywords": ["ci-cd", "pipeline", "demo"],
  "author": "Andres Puglla",
  "license": "MIT"
}
```

**src/index.js**

```javascript
/**
 * Función para sumar dos números
 * @param {number} a - Primer número
 * @param {number} b - Segundo número
 * @returns {number} Suma de a y b
 */
function sumar(a, b) {
  return a + b;
}

/**
 * Función para restar dos números
 * @param {number} a - Primer número
 * @param {number} b - Segundo número
 * @returns {number} Resta de a y b
 */
function restar(a, b) {
  return a - b;
}

/**
 * Función para multiplicar dos números
 * @param {number} a - Primer número
 * @param {number} b - Segundo número
 * @returns {number} Multiplicación de a y b
 */
function multiplicar(a, b) {
  return a * b;
}

/**
 * Función para dividir dos números
 * @param {number} a - Dividendo
 * @param {number} b - Divisor
 * @returns {number} División de a y b
 * @throws {Error} Si el divisor es cero
 */
function dividir(a, b) {
  if (b === 0) {
    throw new Error("No se puede dividir por cero");
  }
  return a / b;
}

// Exportar funciones para usar en tests
module.exports = {
  sumar,
  restar,
  multiplicar,
  dividir
};
```

**tests/app.test.js**

```javascript
const { sumar, restar, multiplicar, dividir } = require("../src/index");

describe("Pruebas de operaciones matemáticas", () => {
  test("suma 1 + 2 es igual a 3", () => {
    expect(sumar(1, 2)).toBe(3);
  });

  test("resta 5 - 3 es igual a 2", () => {
    expect(restar(5, 3)).toBe(2);
  });

  test("multiplicación 4 * 3 es igual a 12", () => {
    expect(multiplicar(4, 3)).toBe(12);
  });

  test("división 10 / 2 es igual a 5", () => {
    expect(dividir(10, 2)).toBe(5);
  });

  test("división por cero lanza error", () => {
    expect(() => dividir(10, 0)).toThrow("No se puede dividir por cero");
  });
});
```

### Paso 2: Configurar el workflow CI/CD

**.github/workflows/ci-cd.yml**

```yaml
name: CI/CD Pipeline

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

      - name: Configurar Node.js
        uses: actions/setup-node@v3
        with:
          node-version: "18"

      - name: Instalar dependencias
        run: npm install

      - name: Ejecutar tests
        run: npm test

      - name: Build del proyecto
        run: npm run build

      - name: Archivar artefacto
        uses: actions/upload-artifact@v3
        with:
          name: package-tgz
          path: "*.tgz"
          retention-days: 5

  deploy:
    needs: build-and-test
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'

    steps:
      - name: Descargar artefacto
        uses: actions/download-artifact@v3
        with:
          name: package-tgz

      - name: Listar contenido
        run: ls -la

      - name: Deploy a producción
        run: echo "Desplegando a producción..."
```

### Paso 3: Verificar el pipeline

1. Ve a tu repositorio en GitHub
2. Haz clic en la pestaña "Actions"
3. Verás el workflow ejecutándose automáticamente
4. Si todos los tests pasan, el deploy se ejecutará y se obtendrá el package

## Beneficios del CI/CD

- **Detección temprana de errores:** Los problemas se identifican inmediatamente después de cada commit, lo que facilita su corrección cuando el código aún está fresco en la mente del desarrollador.

- **Reducción de conflictos de integración:** Al integrar código frecuentemente, se evitan los conflictos masivos que ocurren cuando múltiples desarrolladores trabajan aislados por largos períodos.

- **Despliegues más frecuentes y confiables:** La automatización del proceso de despliegue reduce el riesgo de errores humanos y permite entregar valor al usuario final de forma más rápida y consistente.

- **Automatización de tareas repetitivas:** Elimina la necesidad de ejecutar manualmente pruebas, compilaciones y despliegues, liberando tiempo del equipo para tareas más importantes.

- **Feedback inmediato a los desarrolladores:** Los desarrolladores reciben notificaciones instantáneas sobre el estado de sus cambios, permitiéndoles actuar rápidamente si algo sale mal.

- **Mayor confianza en el código:** Con pruebas automáticas ejecutándose constantemente, el equipo tiene mayor certeza de que el código funciona correctamente antes de llegar a producción.

- **Documentación viva del proceso:** El archivo de workflow sirve como documentación ejecutable de cómo se construye y despliega la aplicación.

## Construcción del Package

El proceso de construcción del package se realiza mediante el comando `npm pack` que genera un archivo `.tgz` con todos los archivos necesarios para distribuir la aplicación. Este archivo se archiva como artefacto y puede ser descargado para su despliegue en diferentes entornos.

Cuando se ejecuta el comando `npm pack`, se crea un archivo con el formato: `{nombre}-{versión}.tgz`

Por ejemplo: `ci-cd-demo-andres-1.0.0.tgz`

Este archivo contiene todos los archivos necesarios para ejecutar la aplicación y puede ser instalado usando `npm install {archivo}.tgz`