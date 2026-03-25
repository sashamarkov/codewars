function encodeMessage(message) {
  const [d1, d2, d3, d4] = message.split('').map(Number);
  const p1 = d1 ^ d2 ^ d4;
  const p2 = d1 ^ d3 ^ d4;
  const p3 = d2 ^ d3 ^ d4;
  return `${p1}${p2}${d1}${p3}${d2}${d3}${d4}`;
}