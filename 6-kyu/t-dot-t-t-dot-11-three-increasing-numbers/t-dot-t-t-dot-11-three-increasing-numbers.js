function increasingNumbers(nums) {
  let a = +Infinity;
  let b = +Infinity;
  for (const n of nums) {
    if (n <= a) {
      a = n;
    } else if (n <= b) {
      b = n;
    } else {
      return true;
    }
  }
  return false;
}