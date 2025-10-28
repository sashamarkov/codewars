function arr2bin(arr) {
    return arr.reduce((a, b) => (typeof b === "number" ? a + b : a), 0).toString(2);
}