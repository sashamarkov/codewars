var finalDestination = function(currentPos, directions) {
  const locales = [
    ["Deepwood Motte", "Shadow Tower", "Castle Black", "Eastwatch", "Bay of Seals"],
    ["The Stony Shore", "Torrhen's Square", "Winterfell", "The Dreadfort", "Karhold"],
    ["Flint's Finger", "Barrowtown", "Moat Cailin", "White Harbour", "Widow's Wat"],
    ["Pyke", "Seagard", "The Twins", "Sisterton", "The Fingers"],
    ["The Crag", "Riverrun", "Darry", "The Eyrie", "Gulltown"],
    ["Castamere", "Acorn Hall", "Harrenhal", "Maidenpool", "Dragonstone"],
    ["Lannisport", "Stoney Sept", "King's Landing", "Blackwater Bay", "Sharp Point"],
    ["High Garden", "Bitterbridge", "King's Wood", "Storm's End", "Evenfall"],
    ["Old Town", "Horn Hill", "Prince's Pass", "Planky Town", "Sunspear"]
  ];
​
  function findPos(name) {
    for (let i = 0; i < locales.length; i++)
      for (let j = 0; j < locales[i].length; j++)
        if (locales[i][j] === name) {
          return [i, j];
        }
  }
  
  let [r, c] = findPos(currentPos);
  
  const moves = directions.match(/([NSEW])(\d+)/g) || [];
  for (const move of moves) {
    const [, dir, dist] = move.match(/([NSEW])(\d+)/);
    for (let i = 0; i < +dist; i++) {
      if (dir === 'N') r--;
      if (dir === 'S') r++;
      if (dir === 'E') c++;
      if (dir === 'W') c--;
      
      if (r < 0) {
        return "The Wall blocks your way";
      }
      if (r >= locales.length || c < 0 || c >= locales[0].length) {
        return "You do not have a ship to cross this sea.";
      }
    }
  }  
  return locales[r][c];
};