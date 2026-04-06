function midPoint(str) {
    const words = str.split(/(\s+)/);
    return words.map(word => /\s/.test(word) ? word : getMid(word)).join('');
}
​
function getMid(s) {
  if (s.length <= 2) {
    return '';
  }
  const n = s.length;
  const m = n % 2 === 0 ? 2 : 1;
  const i = Math.floor((n - m) / 2);
  const mid = s.slice(i, i + m);
  const left = s.slice(0, i);
  const right = s.slice(i + m);
  return mid + getMid(left) + getMid(right);
}