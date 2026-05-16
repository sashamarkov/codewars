function countNumber(matrix, num) {
    const rows = matrix.length;
    if (!rows) return 0;
    let r = 0, c = matrix[0].length - 1, count = 0;
    
    while (r < rows && c >= 0) {
        const val = matrix[r][c];
        if (val === num) {
            count++;
            r++;
            c--;
        } else if (val < num) {
            r++;
        } else {
            c--;
        }
    }
    
    return count;
}