const { sumar } = require('../src/index');

test('prueba intencional que falla: 2+2=5 (debe fallar)', () => {
  expect(sumar(2, 2)).toBe(5);
});
