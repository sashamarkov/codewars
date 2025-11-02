const readableTimetable = (w) => {
  if (!w.length) {
    return [];
  }
  const d = ['mon','tue','wed','thu','fri','sat','sun'];
  const D = d.map(s => s.toUpperCase( ));
  const s = [...w].sort((a,b) => d.indexOf(a.day) - d.indexOf(b.day));
  const g = [];
  
  for (let i = 0; i < s.length; i++) {
    let j = i;
    const h = `${s[i].from} - ${s[i].to}`;
    while (j+1 < s.length && d.indexOf(s[j+1].day) === d.indexOf(s[j].day)+1 && `${s[j+1].from} - ${s[j+1].to}` === h) {
      j++;
    }
    const f = d.indexOf(s[i].day);
    const l = d.indexOf(s[j].day);
    g.push(f === l ? `${D[f]}: ${h}` : `${D[f]} - ${D[l]}: ${h}`);
    i = j;
  }
  return g.join('\n');
}