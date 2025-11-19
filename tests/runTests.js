// Pruebas creadas por Ronny-Villa
const { multiplicar } = require('../src/appCore');

function testMultiplicacion() {
  const resultado = multiplicar(4, 5);
  if (resultado !== 20) {
    console.error("❌ Error: multiplicar(4,5) debería ser 20");
    process.exit(1);
  }
  console.log("✔ Prueba pasada: multiplicar funciona correctamente");
}

testMultiplicacion();
