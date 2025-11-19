const { sumar, restar, multiplicar, dividir } = require("../src/index");

describe("Pruebas de operaciones matemáticas", () => {
  test("suma 1 + 2 es igual a 3", () => {
    expect(sumar(1, 2)).toBe(3);
  });

  test("resta 5 - 3 es igual a 2", () => {
    expect(restar(5, 3)).toBe(2);
  });

  test("multiplicación 4 * 3 es igual a 12", () => {
    expect(multiplicar(4, 3)).toBe(12);
  });

  test("división 10 / 2 es igual a 5", () => {
    expect(dividir(10, 2)).toBe(5);
  });

  test("división por cero lanza error", () => {
    expect(() => dividir(10, 0)).toThrow("No se puede dividir por cero");
  });
});