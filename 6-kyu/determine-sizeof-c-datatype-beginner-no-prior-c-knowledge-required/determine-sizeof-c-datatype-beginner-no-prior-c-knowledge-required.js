function sizeof(t) {
  if (typeof t === 'string') return {
    char: 1, 'unsigned char': 1,
    short: 2, int: 2, 'unsigned short': 2, 'unsigned int': 2,
    long: 4, 'unsigned long': 4,
    'long long': 8, 'unsigned long long': 8,
    float: 4, double: 8
  }[t];
​
  return t?.type === 'struct' ? t.members.reduce((s, m) => s + sizeof(m), 0)
       : t?.type === 'union' ? Math.max(0, ...t.members.map(sizeof))
       : 0;
}