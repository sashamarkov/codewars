function isBeautifulString(s) {
    const freq = {};
    for (let char of s) {
        freq[char] = (freq[char] || 0) + 1;
    }
    for (let i = 1; i < 26; i++) {
        const prev = String.fromCharCode(96 + i);
        const curr = String.fromCharCode(97 + i);
        if ((freq[curr] || 0) > (freq[prev] || 0)) {
            return false;
        }
    }
    return true;
}