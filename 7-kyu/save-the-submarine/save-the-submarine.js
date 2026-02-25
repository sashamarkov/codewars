function findSubmarine(arr) {
    for (let i = 0; i < arr.length; i++) {
        for (let j = 0; j < arr[i].length; j++) {
            if (arr[i][j] === '(') {
                let end = arr[i].indexOf(')', j);
                return { depth: i, start: j, end, size: end - j + 1 };
            }
        }
    }
}
​
function isDestroyed(arr, sub) {
    for (let j = sub.start + 1; j < sub.end; j++) {
        if (arr[sub.depth][j] !== 'O') return true;
    }
    return false;
}
​
function getTask(arr) {
    let sub = findSubmarine(arr);
    
    if (isDestroyed(arr, sub)) return 'Emergency assistance to victims';
    if (sub.depth === 0) return 'Look for a submarine on the surface';
    if (sub.depth > sub.size) return `Emergency search for a possibly damaged submarine at ${sub.depth} depth`;
    return `Start searching for a submarine at ${sub.depth} depth`;
}