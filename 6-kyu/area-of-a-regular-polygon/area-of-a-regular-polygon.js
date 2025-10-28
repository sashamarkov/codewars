function areaOfRegularPolygon(s) {
    const match = s.match(/^(\d+)\s+sides\s+of\s+(\d+(?:\.\d+)?)\s+([a-zA-Z]+)\s+each$/);
    const errorMessage = "Invalid input";
    if (!match) {
      return errorMessage;
    };
    const [n, side, unit] = [parseInt(match[1]), parseFloat(match[2]), match[3]];
    if (n < 3 || side <= 0) {
      return errorMessage;
    }
    const area = (n * side * side) / (4 * Math.tan(Math.PI / n));
    return `${area.toFixed(2)} sq.${unit}`;
}