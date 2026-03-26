var ads = "\nNow is the time for advertisements:\n" +
"My name is myjinxin, 25 years old, Male, \n" +
"unmarried, handsome, rich, looking for\n" +
"a lovely woman as a life partner\n";
​
const originalToString = Number.prototype.toString;
​
function isPrime(n) {
  if (n <= 1) return false;
  if (n <= 3) return true;
  if (n % 2 === 0 || n % 3 === 0) return false;
  for (let i = 5; i * i <= n; i += 6) {
    if (n % i === 0 || n % (i + 2) === 0) return false;
  }
  return true;
}
​
Number.prototype.toString = function() {
  const num = this.valueOf();
  const result = originalToString.call(this);
  return isPrime(num) ? ads + result : result;
};