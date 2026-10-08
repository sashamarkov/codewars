function findUnique(arr) {
  const features = [
    x => Number.isInteger(x) ? 1 : 0,   
    x => x > 0 ? 1 : 0,                 
    x => x % 2 === 0 ? 1 : 0,           
  ];
  
  const cnt = features.map(() => [0, 0]);
  const rep = features.map(() => [null, null]);
  const valueCnt = new Map();
  
  for (const x of arr) {
    features.forEach((f, i) => {
      const k = f(x);
      cnt[i][k]++;
      if (rep[i][k] === null) {
        rep[i][k] = x;
      }
    });
    valueCnt.set(x, (valueCnt.get(x) || 0) + 1);
  }
  
  for (let i = 0; i < features.length; i++) {
    if (cnt[i][0] === 1) {
      return rep[i][0];
    }
    if (cnt[i][1] === 1) {
      return rep[i][1];
    }
  }
  
  for (const [val, c] of valueCnt) {
    if (c === 1) return val;
  }
}