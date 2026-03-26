function sum(...args) {
  if (args.length === 0) {
    return '0';
  }
  const numbers = args.map(arg => String(arg).replace(/^0+/, '') || '0');
  const maxLength = Math.max(...numbers.map(n => n.length));
  let result = '';
  let carry = 0;
  for (let i = 0; i < maxLength; i++) {
    let sum = carry;
    for (let num of numbers) {
      const digit = num[num.length - 1 - i] || '0';
      sum += parseInt(digit, 10);
    }
    result = (sum % 10) + result;
    carry = Math.floor(sum / 10);
  }
  if (carry) {
    result = carry + result;
  }
  return result;
}