function Randomizer(min, max) {
  this.numbers = Array.from({length: max - min + 1}, (_, i) => min + i)
    .sort(() => Math.random() - 0.5);
}
​
Randomizer.prototype.next = function() {
  if (!this.numbers.length) {
    throw Error('no more numbers');
  }
  return this.numbers.shift();
}
​
Randomizer.prototype.sequence = function(size) {
  if (!this.numbers.length) {
    throw Error('no more numbers');
  }
  if (size > this.numbers.length) {
    throw Error('too many numbers');
  } 
  return this.numbers.splice(0, size ?? this.numbers.length);
}