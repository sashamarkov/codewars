function catchThief(queue) {
    let caught = new Set();
    for (let i = 0; i < queue.length; i++) {
        if (/[1-9]/.test(queue[i])) {
            let r = parseInt(queue[i]);
            let left = Math.max(0, i - r);
            let right = Math.min(queue.length - 1, i + r);
            for (let j = left; j <= right; j++) {
                if (queue[j] === 'X') {
                  caught.add(j);
                }
            }
        }
    }
    return caught.size;
}