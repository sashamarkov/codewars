const Substitution = () => ({
  Encrypt: w => [...w].map(c => c.charCodeAt() + 58).join(''),
  Decrypt: w => w.match(/.{3}/g).map(n => String.fromCharCode(+n - 58)).join('')
});