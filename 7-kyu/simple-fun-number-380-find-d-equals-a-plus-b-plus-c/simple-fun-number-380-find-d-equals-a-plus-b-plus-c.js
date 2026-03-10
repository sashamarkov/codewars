function findD(arr) {
  const n = arr.length;
  for (let i = n - 1; i >= 0; i--) {
    const d = arr[i];
    for (let a = 0; a < n; a++) {
      if (a === i) continue;
      for (let b = a + 1; b < n; b++) {
        if (b === i) continue;
        for (let c = b + 1; c < n; c++) {
          if (c === i) continue;
          if (arr[a] + arr[b] + arr[c] === d) {
            return d;
          }
        }
      }
    }
  }
  return null;
}