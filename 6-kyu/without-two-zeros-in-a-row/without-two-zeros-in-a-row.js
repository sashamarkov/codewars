function zeros(n) {
    if (n === 1) return 2n;
    let a = 1n;
    let b = 2n;
    for (let i = 3; i <= n; i++) {
        [a, b] = [b, a + b];
    }
    return b;
}