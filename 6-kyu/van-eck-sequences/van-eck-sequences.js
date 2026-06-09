class VanEck {
  constructor(...start) {
    this.seq = [...start];
    this.lastPos = new Array(2000000); 
    this.firstPos = new Array(2000000);
    this.maxCache = new Array(2000000);
    
    let runningMax = -Infinity;
    for (let i = 0; i < this.seq.length; i++) {
      const val = this.seq[i];
      if (val > runningMax) {
        runningMax = val;
      }
      this.maxCache[i] = runningMax;
      
      if (this.firstPos[val] === undefined) {
        this.firstPos[val] = i;
      }
      if (i < this.seq.length - 1) {
        this.lastPos[val] = i;
      }
    }
    this.len = this.seq.length;
  }
  
  #next() {
    const prev = this.seq[this.len - 1];
    const last = this.lastPos[prev];
    const nxt = last !== undefined ? this.len - 1 - last : 0;
    this.lastPos[prev] = this.len - 1;
    this.seq[this.len] = nxt;
    if (this.firstPos[nxt] === undefined) this.firstPos[nxt] = this.len;
    
    const prevMax = this.maxCache[this.len - 1];
    this.maxCache[this.len] = prevMax > nxt ? prevMax : nxt;
    
    return this.len++;
  }
  
  #growTo(i) {
    while (this.len <= i) {
      this.#next();
    }
  }
  
  term(i) { 
    this.#growTo(i); 
    return this.seq[i]; 
  }
  