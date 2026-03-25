class BatchController {
  constructor() {
    this.unprocessed = [];
    this.processed = [];
    this.reports = [];
    this.currentBatchId = 0;
  }
  
  addBatch(items) {
    this.unprocessed.push(new Batch(this.currentBatchId++, items));
    return this;
  }
  
  processLatestBatch() {
    if (this.unprocessed.length === 0) return;
    var b = this.unprocessed.shift();
    var rs = [];
    var m = [], ms = 0;
    var f = [], fs = 0;
    var o = [], os = 0;
    var qc = b.items[0].items.length;
    var ts = b.items.length;