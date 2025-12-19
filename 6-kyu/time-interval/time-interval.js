function TimeInterval(start, end) {
  this.start = new Date(Math.min(start, end));
  this.end = new Date(Math.max(start, end));
}
​
TimeInterval.prototype.intersection = function (interval) {
  const maxStart = new Date(Math.max(this.start, interval.start));
  const minEnd = new Date(Math.min(this.end, interval.end));
  return maxStart <= minEnd ? new TimeInterval(maxStart, minEnd) : null;
};
​
TimeInterval.prototype.union = function (interval) {
  if (this.end >= interval.start && interval.end >= this.start) {
    const minStart = new Date(Math.min(this.start, interval.start));
    const maxEnd = new Date(Math.max(this.end, interval.end));
    return new TimeInterval(minStart, maxEnd);
  }
  return null;
};