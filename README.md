# CI/CD – Ejemplo Práctico hasta Construcción del Package

Este documento explica de forma sencilla el ciclo CI/CD usando GitHub Actions.  
El ciclo completo incluye:

## 1. Integración Continua (CI)
Cada vez que hacemos **push** o creamos un **pull request**, GitHub Actions ejecuta automáticamente:
- Instalación del proyecto.
- Ejecución de pruebas.
- Construcción del paquete.

Esto permite detectar errores antes de mezclar el código en la rama principal.

## 2. Pruebas
Se usa una prueba unitaria simple para verificar que el código funciona antes de construir el package.

Ejemplo en `test/test.js`:
```js
const assert = require("assert");
const suma = require("../index");

assert.strictEqual(suma(2, 3), 5);
console.log("Prueba exitosa ✔");
```

## 3. Construcción del Package
Una vez que las pruebas pasan, el workflow ejecuta:

```
npm pack
```

Esto genera un archivo `.tgz` que es el PACKAGE final.

## 4. Pipeline completo (Workflow)
El archivo `.github/workflows/ci.yml` contiene el pipeline que:

- Corre pruebas
- Construye el package
- Publica el artefacto

Este ejemplo representa un ciclo CI/CD básico y funcional solicitado en la rúbrica.
