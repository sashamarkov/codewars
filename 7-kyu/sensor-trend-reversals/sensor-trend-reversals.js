function countDirectionChanges(r) {
  let dir = 0, count = 0;
  for (let i = 1; i < r.length; i++) {
    const d = Math.sign(r[i] - r[i - 1]);
    if (d === 0) {
      continue;
    }
    if (dir && d !== dir) {
      count += 1;
    }
    dir = d;
  }
  return count;
}