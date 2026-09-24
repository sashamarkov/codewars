const cantor = n => {
  const d = Math.ceil((Math.sqrt(8 * n + 1) - 1) / 2);
  const p = n - (d - 1) * d / 2;
  return d % 2 ? `${d - p + 1}/${p}` : `${p}/${d - p + 1}`;
};