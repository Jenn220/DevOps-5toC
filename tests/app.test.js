const { suma } = require("../src/index");

test("La función suma debería retornar el resultado correcto", () => {
  expect(suma(2, 3)).toBe(5);
});
