function isomorphReproduced(original, letters) {
  if (original.length !== letters.length) return null;
​
  const fo = freq(original);
  const fl = freq(letters);
​
  const vals = m => [...m.values()].sort((x, y) => x - y).join();
  if(vals(fo) !== vals(fl)) {
    return null;
  }
​
  const map = new Map();
  const flg = group(fl);
  const fog = group(fo);
  for (const [f, os] of fog) {
    const ls = flg.get(f).sort();
    os.forEach((o, i) => map.set(o, ls[i]));
  }
  return [...original].map(c => map.get(c)).join("");
}
​
function freq(s) {
  return [...s].reduce((m, c) => m.set(c, (m.get(c) || 0) + 1), new Map());
}
​
function group(m) {
  const g = new Map();
  for (const [c, f] of m) {
    if (!g.has(f)) {
      g.set(f, []);
    }
    g.get(f).push(c);
  }
  return g;
}