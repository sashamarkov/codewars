const dirs = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]];
const map = (a, f) => a.map((r,i) => r.map((c, j) => f(c, i, j)));
const adj = (a, i, j, t) => dirs.some(([x, y]) => a[i+x]?.[j+y]===t);
​
const outerEdgesOf = a => map(a, (v, i, j) => +(v===0 && adj(a, i, j, 1)));
const innerEdgesOf = a => map(a, (v, i, j) => +(v===1 && (adj(a, i, j, 0) || dirs.some(([x,y])=>!a[i+x]?.[j+y]))));
const grow = a => map(a, (v, i, j) => +(v || dirs.some(([x,y]) => a[i+x]?.[j+y]===1)));
const shrink = a => map(a, (v, i, j) => +(v && dirs.every(([x,y]) => a[i+x]?.[j+y]===1)));