const tapFive = {
  encrypt: s => s.toUpperCase().replace(/[^A-Z]/g, '').replace(/K/g, 'C').replace(/./g, c => {
    let n = c.charCodeAt() - 65;
    if (c > 'J') {
      n -= 1;
    }
    return '' + (Math.floor(n / 5) + 1) + (n % 5 + 1);
  }),
  decrypt: s => s.match(/../g).map(p => {
    let n = (p[0] - 1) * 5 + (p[1] - 1);
    if (n >= 10) {
      n += 1;
    }
    return String.fromCharCode(65 + n);
  }).join('')
}