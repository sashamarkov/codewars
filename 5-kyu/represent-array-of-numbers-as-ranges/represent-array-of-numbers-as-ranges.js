const toRange = arr => {
  const a = [...new Set(arr)].sort((x, y) => x - y);
  const res = [];
  for (let i = 0; i < a.length; i++) {
    if (i === 0 || a[i] !== a[i - 1] + 1) {
      res.push([a[i]]);
    }
    else {
      res[res.length - 1].push(a[i]);
    }
  }
  return res.map(g => g.length === 1 ? `${g[0]}` : `${g[0]}_${g[g.length - 1]}`).join(',');
};
​
const toArray = str =>
  str === '' ? [] : str.split(',').reduce((acc, p) => {
    const [a, b = a] = p.split('_').map(Number);
    return acc.concat(Array.from({ length: b - a + 1 }, (_, i) => a + i));
  }, []);