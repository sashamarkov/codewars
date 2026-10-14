function NetworkClient(sendFunction, callback) {
  let seq = 0, next = 0;
  const buf = new Map();
  const pack = d => `${seq++}:${d}`;
  const unpack = s => {
    const i = s.indexOf(':');
    return [+s.slice(0, i), s.slice(i + 1)];
  };
​
  this.send = d => sendFunction(pack(d));
  this.recv = d => {
    const [n, p] = unpack(d);
    if (n < next) return;
    buf.set(n, p);
    while (buf.has(next)) {
      callback(buf.get(next)), buf.delete(next++);
    }
  };
}