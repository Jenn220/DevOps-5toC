const { sumar } = require("../src/index");

test("suma 1 + 2 es igual a 3", () => {
  expect(sumar(1, 2)).toBe(3);
});
