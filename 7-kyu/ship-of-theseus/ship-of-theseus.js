function shipOfTheseus(ship) {
  return ship.length <= 1 || ship.slice(1).every((row, i) =>
          ship[i].length === row.length &&
          ship[i].filter((val, j) => val !== row[j]).length === 1
  );
}