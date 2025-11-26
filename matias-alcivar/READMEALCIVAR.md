# Pipeline CI/CD con Java

## Estudiante
Matias Alcivar

---

## Que es CI/CD

CI/CD es la automatizacion del proceso de desarrollo de software:

- **CI (Integracion Continua)**: Integrar cambios de codigo frecuentemente y probarlos automaticamente
- **CD (Despliegue Continuo)**: Empaquetar y desplegar la aplicacion de forma automatica

> [!IMPORTANT]
> CI/CD automatiza completamente el flujo desde el codigo hasta produccion, eliminando errores manuales y acelerando entregas.

---

## Flujo del Pipeline

1. El desarrollador hace push del codigo al repositorio
2. GitHub Actions detecta el cambio y ejecuta el pipeline
3. Se compila el codigo fuente
4. Se ejecutan las pruebas automaticas
5. Si todo pasa, se genera el archivo JAR
6. El JAR se guarda como artefacto descargable

> [!NOTE]
> **Orden de ejecucion**: Push → Trigger → Compilacion → Pruebas → Package → Artefacto

---

## Ejemplo Practico: Calculadora

Se desarrollo una calculadora simple en Java con las operaciones basicas:
- Suma
- Resta
- Multiplicacion
- Division

### Estructura del Proyecto

```
matias-alcivar/
├── .github/workflows/ci.yml
├── src/main/java/Calculator.java
├── tests/CalculatorTest.java
└── README.md
```

---

## Codigo Principal

La clase Calculator implementa las operaciones matematicas basicas. Cada metodo retorna el resultado de la operacion correspondiente. El metodo dividir valida que el divisor no sea cero para evitar errores.

### Operaciones implementadas

```java
public int sumar(int a, int b)
public int restar(int a, int b)
public int multiplicar(int a, int b)
public double dividir(int a, int b)
```

> [!TIP]
> El metodo dividir incluye validacion de division por cero, lanzando una excepcion ArithmeticException cuando el divisor es cero.

---

## Pruebas Implementadas

Se implementaron 5 pruebas unitarias:

1. **Prueba de suma**: Verifica que 5 + 3 = 8
2. **Prueba de resta**: Verifica que 10 - 4 = 6
3. **Prueba de multiplicacion**: Verifica que 7 x 6 = 42
4. **Prueba de division**: Verifica que 15 / 3 = 5
5. **Prueba de division por cero**: Verifica que se lance una excepcion

> [!WARNING]
> Las pruebas se ejecutan automaticamente en cada push. Si alguna prueba falla, el pipeline completo se detiene y no se genera el artefacto.

### Resultado de las pruebas

```
Ejecutando pruebas automatizadas
-----------------------------------
PASS - Prueba de suma
PASS - Prueba de resta
PASS - Prueba de multiplicacion
PASS - Prueba de division
PASS - Prueba de division por cero
-----------------------------------
Pruebas aprobadas: 5
Pruebas fallidas: 0
Todas las pruebas pasaron correctamente
```

---

## Configuracion del Pipeline

El archivo `ci.yml` define el workflow de GitHub Actions:

### Pasos del Pipeline:

| Paso | Descripcion | Accion |
|------|-------------|---------|
| 1 | Obtener codigo | Checkout del repositorio |
| 2 | Instalar Java | Setup Java 17 |
| 3 | Crear directorios | Preparar carpetas de compilacion |
| 4 | Compilar aplicacion | javac sobre codigo fuente |
| 5 | Compilar tests | javac sobre pruebas |
| 6 | Ejecutar tests | java CalculatorTest |
| 7 | Generar JAR | jar con manifest |
| 8 | Probar JAR | Verificar ejecucion |
| 9 | Guardar artefacto | Upload artifact |

> [!NOTE]
> **Java 17**: Se utiliza la distribucion Temurin de Eclipse para garantizar compatibilidad y rendimiento.

---

## Construccion del Package

El pipeline genera un archivo JAR ejecutable que contiene:
- Todas las clases compiladas
- Un manifest que especifica la clase principal
- El empaquetado completo de la aplicacion

### Como se genera el JAR

```bash
cd out/production
echo "Main-Class: Calculator" > manifest.txt
jar cfm Calculator.jar manifest.txt *.class
```

Para ejecutar el JAR generado:
```bash
java -jar Calculator.jar
```

> [!TIP]
> El artefacto generado se almacena por 30 dias en GitHub Actions y puede descargarse desde la seccion "Artifacts" del workflow ejecutado.

---

## Beneficios del Pipeline

| Beneficio | Descripcion |
|-----------|-------------|
| Deteccion temprana | Errores encontrados en minutos, no en dias |
| Automatizacion | Cero intervencion manual requerida |
| Trazabilidad | Historial completo de cada ejecucion |
| Reproducibilidad | Mismo proceso cada vez |
| Calidad | Pruebas garantizan funcionalidad |

> [!IMPORTANT]
> **Ahorro de tiempo**: Lo que antes tomaba 30 minutos manualmente ahora toma 2 minutos automaticamente.

---

## Como Reproducir

### Pasos para ejecutar localmente:

```bash
# 1. Clonar el repositorio
git clone [URL-repositorio]
cd [nombre-repositorio]/matias-alcivar

# 2. Compilar el codigo
mkdir -p out/production out/test
javac -d out/production src/main/java/*.java
javac -cp out/production -d out/test tests/*.java

# 3. Ejecutar pruebas
java -cp out/production:out/test CalculatorTest

# 4. Generar JAR
cd out/production
echo "Main-Class: Calculator" > manifest.txt
jar cfm Calculator.jar manifest.txt *.class

# 5. Ejecutar JAR
java -jar Calculator.jar
```

> [!NOTE]
> En Windows usa punto y coma (;) en lugar de dos puntos (:) para el classpath: `java -cp out/production;out/test CalculatorTest`

---

## Tecnologias Utilizadas

- **Java 17**: Lenguaje de programacion
- **GitHub Actions**: Plataforma de CI/CD
- **JAR**: Formato de empaquetado Java
- **Git**: Control de versiones

---

## Resultados Esperados

Al ejecutar el pipeline correctamente se obtiene:

- Compilacion exitosa del codigo
- 5 pruebas aprobadas (100% de cobertura)
- Archivo JAR funcional de aproximadamente 2KB
- Artefacto disponible para descarga por 30 dias

### Visualizacion en GitHub Actions

```
Pipeline CI/CD
├── Obtener codigo ✓
├── Instalar Java ✓
├── Crear directorios ✓
├── Compilar aplicacion ✓
├── Compilar tests ✓
├── Ejecutar tests ✓
├── Generar JAR ✓
├── Probar JAR ✓
└── Guardar artefacto ✓
```

> [!TIP]
> **Verificacion visual**: En GitHub Actions veras una marca verde (✓) en cada paso si todo funciona correctamente.

---

## Debugging del Pipeline

### Si el pipeline falla:

1. **Revisa los logs**: Click en el paso que fallo
2. **Verifica la compilacion**: Errores de sintaxis en codigo
3. **Chequea las pruebas**: Alguna prueba puede estar fallando
4. **Valida rutas**: Asegurate que los archivos esten en las carpetas correctas

> [!WARNING]
> **Errores comunes**: 
> - Rutas incorrectas en ci.yml
> - Archivos en carpetas equivocadas
> - Sintaxis Java incorrecta
> - Pruebas con valores esperados incorrectos

---

## Comparacion con proceso manual

| Aspecto | Manual | Automatizado (CI/CD) |
|---------|--------|---------------------|
| Tiempo | 30+ minutos | 2 minutos |
| Errores | Frecuentes | Minimos |
| Consistencia | Variable | 100% consistente |
| Documentacion | Puede olvidarse | Siempre registrado |
| Escalabilidad | Dificil | Facil |

---

## Conclusion

Este pipeline demuestra un flujo CI/CD funcional que automatiza completamente el proceso desde el codigo fuente hasta el artefacto desplegable. Las pruebas garantizan la calidad del codigo y el proceso automatizado elimina errores manuales.

> [!IMPORTANT]
> **Resultado final**: Un pipeline robusto, automatizado y reproducible que puede escalar para proyectos mas grandes sin modificaciones mayores.

### Proximos pasos sugeridos:

- Agregar mas pruebas (cobertura de casos borde)
- Implementar analisis de codigo estatico (SonarQube)
- Agregar deployment automatico a un servidor
- Configurar notificaciones por email/Slack

---

## Referencias

- [GitHub Actions Documentation](https://docs.github.com/actions)
- [Java SE Documentation](https://docs.oracle.com/javase/)
- [CI/CD Best Practices](https://www.atlassian.com/continuous-delivery/principles/continuous-integration-vs-delivery-vs-deploy
