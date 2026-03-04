var notQuine = function(){
  const source = notQuine.toString();
  let result = '';
  for (let i = 32; i <= 254; i++) {
    const char = String.fromCharCode(i);
    if (source.indexOf(char) === -1) {
      result += char;
    }
  }
  return result;
};