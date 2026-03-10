function minSteps(apples) {
  const n = apples.length;
  const total = apples.reduce((a, b) => a + b, 0);
  const target = total / n;
  if (total % n !== 0) return -1;
  if (!apples.every(count => count % 2 === target % 2)) return -1;
  
  return apples.reduce((steps, count) => 
    steps + (count > target ? count - target : 0), 0) / 2;
}