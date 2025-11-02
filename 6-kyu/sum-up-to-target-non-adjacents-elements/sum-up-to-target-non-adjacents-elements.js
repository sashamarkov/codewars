function sumUpNoAdjacents(nums, target) {
    for (let i = 0; i < (1 << nums.length); i++) {
        let sum = 0, prev = false;
        for (let j = 0; j < nums.length; j++) {
            if (i & (1 << j)) {
                if (prev) break;
                sum += nums[j];
                prev = true;
            } else {
                prev = false;
            }
        }
        if (sum === target) return true;
    }
    return false;
} 