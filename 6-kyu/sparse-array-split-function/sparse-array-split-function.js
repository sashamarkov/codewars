Array.prototype.split = function() {
  const sparse = Array.from({length: this.length}, (_, i) => i).some(i => !(i in this));
  
  if (!sparse) return this;
  
  const result = [];
  let chunk = [];
  
  for (let i = 0; i < this.length; i++) {
    if (i in this) {
      chunk.push(this[i]);
    } else if (chunk.length) {
      result.push(chunk);
      chunk = [];
    }
  }
  if (chunk.length > 0) {
    result.push(chunk);
  }
  return result;
};