# Proyecto CI/CD – Jean

Este proyecto demuestra un flujo completo de **Integración Continua (CI)** y **Despliegue Continuo (CD)** utilizando GitHub Actions.  
El objetivo es mostrar cómo un repositorio puede ejecutar automáticamente pruebas, validar cambios y construir un paquete antes de integrarlo mediante Pull Request.

---

## 1. Ciclo CI/CD

El pipeline CI/CD funciona de la siguiente manera:

1. **Push o Pull Request**
   - Cuando se hace push a la rama `jean`
   - O cuando se crea un Pull Request hacia `main`

2. **GitHub Actions ejecuta automáticamente:**
   - Instalación de dependencias (`npm install`)
   - Ejecución de pruebas unitarias (`npm test`)
   - Construcción del paquete (`npm run build`)

3. **Validación**
   - Si las pruebas pasan → el Pull Request puede aprobarse.
   - Si fallan → GitHub bloquea el merge.

---

## 2. Pruebas unitarias (Jest)

El proyecto incluye una prueba unitaria básica ubicada en:

