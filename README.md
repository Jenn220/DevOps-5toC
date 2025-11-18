# Pipeline CI/CD — Proyecto de Integración Continua

**Repositorio:** https://github.com/Jenn220/DevOps-5toC.git  
**Creadora / Autora del README:** Jenifer Alvarez

**Colaborador (este repositorio incluye):** Santiago Alomoto y equipo

---

## Objetivo
Explicar detalladamente el ciclo CI/CD hasta la **construcción del PACKAGE**, con un ejemplo práctico reproducible que incluya pruebas unitarias y la generación del artefacto.

---

## Resumen del ciclo CI/CD (conceptual)
1. Desarrollador hace cambios localmente.  
2. Hace commit y push a la rama remota.  
3. El sistema de CI (GitHub Actions) detecta el push y ejecuta el pipeline.  
4. El pipeline instala dependencias, ejecuta tests, construye el paquete y publica un artefacto.  
5. Si todo pasa, el artefacto queda disponible para descargar o desplegar.

---

## Ejemplo práctico (Node.js) — ¿Qué contiene este repo para la demostración?
- `src/index.js` — función sencilla para ejemplificar.
- `tests/app.test.js` — prueba con Jest.
- `package.json` — scripts para test, build y package.
- `.github/workflows/ci-cd.yml` — workflow funcional que:
  - Ejecuta tests.
  - Genera un package con `npm pack`.
  - Sube el package como artefacto (para descargar desde la ejecución de Actions).

---

## Archivos clave (ejemplo de contenido)

**`src/index.js`**
```javascript
function sumar(a, b) {
  return a + b;
}

module.exports = { sumar };
