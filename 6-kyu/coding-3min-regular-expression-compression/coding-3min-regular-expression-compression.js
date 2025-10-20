function sc(regex){
  let s = regex.slice(1, -1);
  let t = s.match(/^(.+?)(?=\1*$)/)[0];
  let n = s.length / t.length;
  let p = t.length > 1 ? `(${t})` : t;
  let compressed = `/${n > 1 ? p + '{' + n + '}' : s}/`;
  return compressed.length < regex.length ? compressed : regex;
}