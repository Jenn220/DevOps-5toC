# Pipeline CI/CD — Proyecto de Integración Continua

Pipeline CI/CD - Proyecto de Integración Continua
Información del Proyecto
Autor: Damian Carrillo
Materia: DevOps - 5to C
Repositorio: https://github.com/Jenn220/DevOps-5toC.git 
Rama: rama-Damian-Carrillo
Fecha: Noviembre 2025

1. README.md — Explicación del ciclo CI/CD (2 pts)

Tu README debe incluir:

✔ Explicación clara del ciclo CI/CD

Ejemplo breve:

El ciclo CI/CD (Integración Continua / Entrega Continua) automatiza tareas como pruebas, construcción y despliegue cada vez que se hace un push o un pull request.

CI (Continuous Integration):

Se ejecutan las pruebas automáticamente.

Se verifica que el código compile.

Se construyen artefactos.

CD (Continuous Delivery):

Se deja listo un paquete para ser desplegado.

Opcionalmente, se despliega automáticamente a un servidor.

✔ Pasos reproducibles de CI/CD

Puedes incluir un ejemplo como este:

# 1. Clonar el repositorio
git clone https://github.com/usuario/proyecto.git
cd proyecto

# 2. Ejecutar pruebas localmente
npm install
npm test

# 3. Ejecutar el workflow manualmente (GitHub Actions)
# Actions > seleccionar workflow > Run workflow

✔ Debe quedar claro que tú lo escribiste

No copiando de otros repos.

2. Configuración CI/CD – Workflow funcional (2 pts)

Incluye un archivo como:

.github/workflows/ci.yml

Ejemplo funcional:

name: CI Pipeline

on:
  push:
  pull_request:

jobs:
  build-and-test:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v3

      - name: Set up Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '18'

      - name: Install dependencies
        run: npm install

      - name: Run tests
        run: npm test

      - name: Build package
        run: npm run build

      - name: Upload artifact
        uses: actions/upload-artifact@v3
        with:
          name: build-output
          path: dist/

3. Pruebas básicas (2 pts)

Debes incluir un archivo de prueba simple, por ejemplo si usas Jest:

/tests/sum.test.js

const sum = (a, b) => a + b;

test('suma 2 + 3 = 5', () => {
  expect(sum(2, 3)).toBe(5);
});


Y en el package.json:

"scripts": {
  "test": "jest",
  "build": "echo 'compilado' && mkdir dist"
}

4. Construcción del package / artefacto (2 pts)

El workflow debe generar un artefacto y subirlo.
Ejemplo ya incluido arriba:

- name: Upload artifact
  uses: actions/upload-artifact@v3
  with:
    name: build-output
    path: dist/


GitHub Actions lo mostrará en:
Actions → Run → Artifacts