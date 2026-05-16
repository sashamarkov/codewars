function compression(length, getChar) {
    let r = '', i = 0;
    while (i < length) {
        const c = getChar(i);
        let low = i, high = length - 1;
        while (low < high) {
            const mid = Math.floor((low + high + 1) / 2);
            getChar(mid) === c ? low = mid : high = mid - 1;
        }
        r += (low - i + 1) + c;
        i = low + 1;
    }
    return r;
}