const DAYS = ['sunday','monday','tuesday','wednesday','thursday','friday','saturday'];
​
class Frequency {
  constructor(time) {
    const [h, m] = time.split(':').map(Number);
    this.h = h;
    this.m = m;
  }
  base(now) {
    const d = new Date(now);
    d.setHours(this.h, this.m, 0, 0);
    if (d < now) d.setDate(d.getDate() + 1);
    return d;
  }
  next(now) { return this.base(now); }
}
​
class Workday extends Frequency {
  next(now) {
    const d = this.base(now);
    while (d.getDay() === 0 || d.getDay() === 6) d.setDate(d.getDate() + 1);
    return d;
  }
}
​
class Weekday extends Frequency {
  constructor(time, day) { super(time); this.target = DAYS.indexOf(day); }
  next(now) {
    const d = this.base(now);
    while (d.getDay() !== this.target) d.setDate(d.getDate() + 1);
    return d;
  }
}
​
const makeFrequency = (freq, time) =>
  freq === 'every day' || freq === 'only once' ? new Frequency(time)
  : freq === 'every workday' ? new Workday(time)
  : new Weekday(time, freq.split(' ')[1]);
​
function sortIt(alarms, time) {
  const now = new Date(time.replace(' ', 'T'));
  const key = a => makeFrequency(a.frequency, a.time).next(now);
  return [...alarms]
    .map(a => ({ alarm: a, next: key(a) }))
    .sort((a, b) => a.next - b.next)
    .map(x => x.alarm);
}