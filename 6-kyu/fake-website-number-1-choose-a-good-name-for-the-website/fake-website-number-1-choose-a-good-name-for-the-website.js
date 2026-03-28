function goodName(name) {
  const [d, t] = name.split('.');
  const r = new Set();
  d.replace(/[ol]/g, (c, i) => r.add(d.slice(0, i) + (c === 'o' ? '0' : '1') + d.slice(i + 1) + '.' + t));
  d.replace(/(.)\1/g, (_, c, i) => r.add(d.slice(0, i) + d.slice(i + 1) + '.' + t));
  return [...r].sort();
}