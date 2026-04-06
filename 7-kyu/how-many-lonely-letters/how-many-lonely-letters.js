function countLonelyLetters(text) {
  const freq = [...text.toLowerCase()].reduce((f, c) => 
    /[a-z]/.test(c) ? {...f, [c]: (f[c] || 0) + 1} : f, {});
  
  return Object.entries(freq).reduce((count, [letter, occ]) => 
    occ === 1 && 
    !freq[String.fromCharCode(letter.charCodeAt(0) - 1)] && 
    !freq[String.fromCharCode(letter.charCodeAt(0) + 1)] 
      ? count + 1 : count, 0);
}
​