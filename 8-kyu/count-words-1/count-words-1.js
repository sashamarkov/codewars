function countWords(str) {
  return str.split(/\s/).filter(function(n){return n != ""}).length;
}