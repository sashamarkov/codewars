function thetaFormula(radius, arc, angle) {
  const args = [radius, arc, angle]
  const isNum = v => typeof v === 'number' && !isNaN(v);
  const isQ = v => v === '?';
  const qCount = args.filter(isQ).length;
  const numCount = args.filter(isNum).length;
  if (qCount + numCount !== args.length) {
    return null;
  }
  if (qCount > 1) {
    return null;
  }
  if (qCount === 0) {
    return arc/radius === angle;
  }
  if (isQ(radius)) {
    return round3(arc / angle);
  }
  if (isQ(arc)) {
    return round3(angle * radius);
  }
  if (isQ(angle)) {
    return round3(arc / radius);
  }
}
​
function round3(x) {
  return Math.round(x * 1000) / 1000;
}