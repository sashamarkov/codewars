function sort(str) {
  const chars = removeWhitespace(str);
  const { letters, numbers, punctuation } = categorizeChars(chars);
  return [...sortLetters(letters), ...sortNumbers(numbers), ...sortPunctuation(punctuation)].join('');
}
​
function removeWhitespace(str) {
  return str.split('').filter(c => !/\s/.test(c));
}
​
function categorizeChars(chars) {
  return {
    letters: chars.filter(c => /[a-zA-Z]/.test(c)),
    numbers: chars.filter(c => /[0-9]/.test(c)),
    punctuation: chars.filter(c => !/[a-zA-Z0-9]/.test(c))
  };
}
​
function sortLetters(letters) {
  return letters.sort((a, b) => {
    const aLower = a.toLowerCase();
    const bLower = b.toLowerCase();
    if (aLower !== bLower) return aLower.localeCompare(bLower);
    return a === a.toUpperCase() && b !== b.toUpperCase() ? -1 : 1;
  });
}
​
function sortNumbers(numbers) {
  return numbers.sort((a, b) => parseInt(a) - parseInt(b));
}
​
function sortPunctuation(punctuation) {
  return punctuation.sort();
}