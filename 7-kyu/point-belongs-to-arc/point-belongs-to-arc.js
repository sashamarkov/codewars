function belongsToArc(a, b, c) {
  const n = x => ((x % 360) + 360) % 360;
  const a1 = n(a), b1 = n(b), c1 = n(c);
  if (a1 === b1) return c1 === a1;
  return a1 < b1 ? c1 >= a1 && c1 <= b1 : c1 >= a1 || c1 <= b1;
}