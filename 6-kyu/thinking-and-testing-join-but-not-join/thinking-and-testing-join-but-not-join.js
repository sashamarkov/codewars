Array.prototype.Join = function(sep) {
    return this.flatMap((x, i) => i === this.length - 1 ? [x] : 
        Array.isArray(sep) ? [x, ...sep] : [x, sep]);
};