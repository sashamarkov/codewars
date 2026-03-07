function figureOut(arr) {
  const letters = [...new Set(arr.join('').replace(/\s/g, ''))];
  const pos = {};
  letters.forEach(l => {
    pos[l] = arr.map(s => s.indexOf(l));
  });
  const maxMove = letters.map(l => 
    Math.max(...pos[l].slice(1).map((p, i) => Math.abs(p - pos[l][i])))
  );
  const witch = letters.find((l, i) => maxMove[i] > 1);
  const others = letters.filter(l => l !== witch);
  return others.every(l => 
    pos[l].slice(1).every((p, i) => Math.abs(p - pos[l][i]) <= 1)
  ) ? witch || null : null;
}