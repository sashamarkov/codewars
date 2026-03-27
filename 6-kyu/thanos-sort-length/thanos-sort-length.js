function thanosSort(arr) {
  if (arr.length === 0) return 0;
  if (arr.length === 1) return 1;
  const stack = [arr];
  let maxLength = 1;
  
  while (stack.length > 0) {
    const current = stack.pop();
    if (isSorted(current)) {
      maxLength = Math.max(maxLength, current.length);
      continue;
    }
    if (current.length === 1) {
      maxLength = Math.max(maxLength, 1);
      continue;
    }
    const mid = Math.ceil(current.length / 2);
    stack.push(current.slice(0, mid));
    stack.push(current.slice(mid));
  }
  return maxLength;
}
​
function isSorted(subarray) {
  for (let i = 1; i < subarray.length; i++) {
    if (subarray[i] < subarray[i-1]) {
      return false;
    }
  }
  return true;
}