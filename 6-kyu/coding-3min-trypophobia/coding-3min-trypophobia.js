function sc(arr) {
  if (!arr.length) {
    return [];
  }
  const freq = {};
  arr.forEach(sub => sub.forEach(n => freq[n] = (freq[n] || 0) + 1));
  const maxFreq = Math.max(...Object.values(freq));
  return arr.map(sub => sub.filter(n => freq[n] !== maxFreq));
}