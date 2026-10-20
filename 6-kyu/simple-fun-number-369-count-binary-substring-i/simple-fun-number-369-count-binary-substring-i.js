function count(s1,s2){
  let n = 0;
  for (let i = 0; i <= s2.length - s1.length; i++) {
    n += s2.startsWith(s1, i);
  }
  return n; 
}