function releaseFireworks(map){
  const rows = map.split("\n");
  const n = rows.length;
  const w = Math.max(...rows.map(r => r.length));
  const res = [];
  for (let c = 0; c < w; c++) {
    for (let r = 0; r < n; r++) {
      if (rows[r][c] === 'o') {
        res.push([c, Math.round((n - r) * 5 / 4 * 100) / 100]);
      }
    }
  }
  return res;
}
​