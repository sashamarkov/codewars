const add = (x, y) => {
  while(y !== 0){
    const carry = (x & y) << 1;
    x = x ^ y;
    y = carry;
  }
  return x;
};
​
const subtract = (x, y) => add(x, add(~y, 1));
​
const multiply = (x, y) => {
  const neg = y < 0;
  if (neg) {
    y = add(~y, 1);
  }
  let result = 0;
  while (y !== 0) {
    if (y & 1) {
      result = add(result, x);
    }
    x <<= 1;
    y >>>= 1;
  }
  return neg ? add(~result, 1) : result;
};