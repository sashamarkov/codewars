function longestSequenceIn(str) {
    const nums = str.trim() === '' ? [] : str.split(' ').map(Number);
    if (nums.length === 0) {
        return 0;
    }
    let maxLen = 1;
    for (let i = 0; i < nums.length; i++) {
        for (let j = i + 1; j < nums.length; j++) {
            const diff = nums[j] - nums[i];
            let len = 2;
            let last = nums[j];
            for (let k = j + 1; k < nums.length; k++) {
                if (nums[k] - last === diff) {
                    len++;
                    last = nums[k];
                }
            }
            maxLen = Math.max(maxLen, len);
        }
    }
    return maxLen;
}