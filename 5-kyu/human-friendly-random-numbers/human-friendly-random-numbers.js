function RNG(n) {
  this.n = n;  
  this.pool = [];
}
​
RNG.prototype.rand = function() {
    if (this.pool.length === 0) {
        this.pool = Array.from({ length: this.n }, (_, i) => i);
        for (let i = this.pool.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [this.pool[i], this.pool[j]] = [this.pool[j], this.pool[i]];
        }
    }
    return this.pool.pop();
};