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