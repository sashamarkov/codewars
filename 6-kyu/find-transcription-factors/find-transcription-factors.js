function transFactors(seq) {
  const factors = { ATF6:"TGACGT", CREB:"TGACGCA", cMyc:"CACGTG", Gata1:"GATT", AhR:"TGCGTG" };
  const res = {};
  for (const [name, site] of Object.entries(factors)) {
    const pos = [];
    for (let i = 0; i <= seq.length - site.length; i++) {
      if (seq.substr(i, site.length) === site) {
        pos.push(i + 1);
      }
    }
    if (pos.length) res[name] = pos;
  }
  return res;
}