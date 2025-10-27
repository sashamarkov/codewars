export const removeOutliers = (data: number[]): number[] => {
    let arr: number[] = data.slice();
    const med = (a: number[]): number => 
        a.length % 2 ? a[a.length >> 1] : (a[a.length / 2 - 1] + a[a.length / 2]) / 2;
    while (arr.length > 3) {
        const s: number[] = arr.slice().sort((a, b) => a - b);
        const n: number = s.length;
        const m: number = n >> 1;
        const lq: number = med(s.slice(0, n % 2 ? m : m + 1));
        const uq: number = med(s.slice(n % 2 ? m + 1 : m));
        const iqr: number = uq - lq;
        const filtered: number[] = arr.filter(x => x >= lq - 1.5 * iqr && x <= uq + 1.5 * iqr);
        if (filtered.length === arr.length) break;
        arr = filtered;
    }
    return arr;
};