function testit(love) {
  const grid = love.split('\n');
  const result = grid.map(row => row.split('').map(() => '.'));
   
  const mark = (line, get, set) => {
    const regex = /love|evol/gi;
    for (let i = 0; i < line.length; i++) {
      regex.lastIndex = i;
      const match = regex.exec(line);
      if (match && match.index === i) {
        for (let j = 0; j < 4; j++) {
          set(i + j, get(i + j));
        }
      }
    }
  };
  grid.forEach((row, r) => mark(row, c => row[c], (c, v) => result[r][c] = v));
  for (let c = 0; c < grid[0].length; c++) {
    const col = grid.map(row => row[c]).join('');
    mark(col, r => grid[r][c], (r, v) => result[r][c] = v);
  }
  return result.map(row => row.join('')).join('\n');
}