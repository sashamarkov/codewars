function findCombos(array) {
  const flattenDeep = (arr) => 
    arr.reduce((acc, val) => 
      acc.concat(Array.isArray(val) ? flattenDeep(val) : val === [] ? [] : val), 
      []
    );
  
  const flatArray = flattenDeep(array);
  
  if (flatArray.length < 2) return 1;
  
  const frequency = {};
  for (let i = 0; i < flatArray.length; i++) {
    const num = flatArray[i];
    frequency[num] = (frequency[num] || 0) + 1;
  }
  
  const factorial = (n) => {
    let result = 1;
    for (let i = 2; i <= n; i++) {
      result *= i;
    }
    return result;
  };
  let numerator = factorial(flatArray.length);
  let denominator = 1;
  
  const counts = Object.values(frequency);
  for (let i = 0; i < counts.length; i++) {
    denominator *= factorial(counts[i]);
  }
  
  return numerator / denominator;
}