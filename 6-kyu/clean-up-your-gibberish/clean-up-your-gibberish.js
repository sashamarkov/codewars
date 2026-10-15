function cleanItUp(s) {
  const letters = (s.match(/[a-z]/gi) || []).join('');
  const chunks = letters.match(/.{5}/g);
  if (!chunks) {
    return '';
  }
  return chunks
    .map(w => w[0].toUpperCase() + w.slice(1).toLowerCase())
    .join(' ');
}