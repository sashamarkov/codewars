function stringTransformation(str, operations) {
  let isReversed = false;
  let shouldUppercase = null;
  let duplicateCount = 1;
  
  for (const op of operations) {
    switch(op) {
      case "U": shouldUppercase = true; break;
      case "L": shouldUppercase = false; break;
      case "R": isReversed = !isReversed; break;
      case "D": duplicateCount *= 2; break;
    }
  }
  
  let result = [];
  for (let char of str) {
    result.push(char.repeat(duplicateCount));
  }
  if (isReversed) {
    result.reverse();
  }
  let s = result.join('');
  if (shouldUppercase === true) {
    return s.toUpperCase();
  }
  if (shouldUppercase === false) {
    return s.toLowerCase();
  }
  return s;
}