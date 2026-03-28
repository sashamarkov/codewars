function pattern(n) {
    if (typeof n !== 'number' || n < 0 || !Number.isInteger(n)) {
      return "check input";
    }
    spaces = 1;
    result = [];
    while (n > 0){
      let row = [hashRow(n), starRow(n), numberRow(n)][n % 3]
      result.push(" ".repeat(spaces) + row);
      spaces += 1;
      n -= 1;
    }
    return result.reverse().join('\n');
}
​
function starRow(n) {
  if(n === 1) {
    return " *";
  }
  return [..."*".repeat(n + 1)].join(" ");
}
​
function hashRow(n) {
  return [..."#".repeat(n + 1)].join(" ");
}
​
function numberRow(n) {
  return [...Array(n+1).keys()].map(i => (i + 1) % 10).join(" ")
}