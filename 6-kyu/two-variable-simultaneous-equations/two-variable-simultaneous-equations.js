function solveSimultaneous(array) {
  const [[a1, b1, c1], [a2, b2, c2]] = array;
  const det = a1 * b2 - b1 * a2;
  const x = (c1 * b2 - b1 * c2) / det;
  const y = (a1 * c2 - c1 * a2) / det;
  return [x, y];
}