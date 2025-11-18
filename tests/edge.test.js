const { sumar } = require('../src/index');

test('suma cero + número', () => {
  expect(sumar(0, 5)).toBe(5);
});

test('suma números negativos', () => {
  expect(sumar(-2, -3)).toBe(-5);
});

test('suma número y negativo', () => {
  expect(sumar(5, -2)).toBe(3);
});
