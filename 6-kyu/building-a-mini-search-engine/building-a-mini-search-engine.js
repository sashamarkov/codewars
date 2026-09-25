const INVALID = 'No valid input';
​
function searchEng(string, searchWord, searchMethod, newWord) {
  if (![1, 2].includes(searchMethod)) {
    return INVALID;
  }
  if (!isValid(searchWord)) {
    return INVALID;
  }
  if (searchMethod === 2 && !isValid(newWord)) {
    return INVALID;
  }
  const re = new RegExp(`\\b${searchWord}\\b`, 'g');
  const matches = (string.match(re) || []).length;
  
  return { matches, newString: searchMethod === 1 ? '' : string.replace(re, newWord) };
}
​
function isValid(word) {
  return typeof word === 'string' && /^[A-Za-z0-9]+$/.test(word);
}