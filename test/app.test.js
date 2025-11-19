const sum = require('../app');

test('suma correcta', () => {
  expect(sum(2, 3)).toBe(5);
});
