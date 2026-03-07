function shortestDirection(a, b) {
  const norm = (angle) => ((angle % 360) + 360) % 360;
  const diff = (norm(b) - norm(a) + 360) % 360;
  return diff > 180 ? diff - 360 : diff;
}
​