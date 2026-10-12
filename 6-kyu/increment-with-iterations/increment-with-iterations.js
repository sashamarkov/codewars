function increment(number, iterations, spacer) {
  const d = [...String(number)].map(Number);
  let pos = 0;
  while(iterations) {
    pos = (pos + spacer) % d.length;
    for(let j = pos; d[j]++ === 9;){
      d[j] = 0;
      if(j-- === 0) {
        d.unshift(1);
        pos += 1;
        break;
      }
    }
    iterations -= 1;
  }
  return +d.join('');
}