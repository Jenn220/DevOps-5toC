# Pipeline CI/CD - Proyecto de Integración Continua

**Creador:** Jenifer Alvarez

**Colaboradores:**

- colaborador 1: Mayte Anchapanta=
- colaborador 2: Ricardo Astudillo=
- colaborador 3: Mathias Alcivar= merge listo
- colaborador 4: Santiago Alomoto=
- colaborador 5: Diego Lema=
- colaborador 6: Jualian Chavez=
- colaborador 7: Mateo Guerron=
- colaborador 8: Ronny Villa=
- colaborador 9: Joel Molina=
- colaborador 10: Damian Carrillo=
- colaborador 11: Alexis Coello=
- colaborador 12: Jean Mora=
- colaborador 13: Andres Puglla=
- colaborador 14: Liz Llinin=
- colaborador 15: Steven Calle=
- colaborador 16: Fernando Cuaspud=
- colaborador 17: Mateus Castillo=

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
├── /
│   └── index.js
├── tests/
│   └── app.test.js
├── package.json
└── README.md
```

### Paso 1: Crear el repositorio

```bash
mkdir ci-cd-project
cd ci-cd-project
git init
git branch -M main
```

### Paso 2: Crear la aplicación básica

**package.json**

```json
{
  "name": "ci-cd-demo",
  "version": "1.0.0",
  "scripts": {
    "test": "jest",
    "start": "node src/index.js"
  },
  "devDependencies": {
    "jest": "^29.0.0"
  }
}
```

**index.js**

```javascript
function sumar(a, b) {
  return a + b;
}

module.exports = { sumar };
```

**tests/app.test.js**

```javascript
const { sumar } = require("../src/index");

test("suma 1 + 2 es igual a 3", () => {
  expect(sumar(1, 2)).toBe(3);
});
```

### Paso 3: Configurar el workflow CI/CD

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
        run: npm run build --if-present

  deploy:
    needs: build-and-test
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'

    steps:
      - name: Deploy a producción
        run: echo "Desplegando a producción..."
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
