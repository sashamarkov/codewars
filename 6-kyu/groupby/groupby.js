Array.prototype.groupBy = function groupBy(eq = (a, b) => a === b) {
  return this.reduce((acc, x) => 
   acc.length && eq(x, acc[acc.length - 1][0])
    ? (acc[acc.length - 1].push(x), acc)
    : [...acc, [x]]
  ,[]);
};
​
Object.defineProperty(Array.prototype, "groupBy", {enumerable: false});