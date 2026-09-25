function testit(top, bottom) {
  const EMPTY = "\u3000";
  const rows = (top + "\n" + bottom).split("\n");
  const cols = rows[0].length;
  let best = 0;
  let max = -1;
  for (let c = 0; c < cols; c++) {
    const count = rows.filter(r => r[c] === EMPTY).length;
    if (count > max) {
      max = count;
      best = c + 1;
    }
  }
  return best;
}