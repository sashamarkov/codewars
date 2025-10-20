function smallestDiff(arr1, arr2) {
    if (!arr1.length && !arr2.length) {
      return -1;
    }
    if (!arr1.length){
      return Math.min(...arr2);
    }  
    if (!arr2.length) {
      return Math.min(...arr1);
    }
    arr1.sort((a, b) => a - b);
    arr2.sort((a, b) => a - b);
    let i = 0, j = 0, min = +Infinity;
    while (i < arr1.length && j < arr2.length) {
        min = Math.min(min, Math.abs(arr1[i] - arr2[j]));
        arr1[i] < arr2[j] ? i++ : j++;
    }
    return min;
}