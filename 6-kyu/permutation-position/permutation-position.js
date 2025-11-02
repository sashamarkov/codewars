function permutationPosition(s) {
    let result = 0;
    let n = s.length;
    for (let i = 0; i < n; i++) {
        let charValue = s.charCodeAt(i) - 96;
        if (i < n - 1) {
            charValue--;
        }
        result += charValue * Math.pow(26, n - i - 1);
    }
    return result;
}