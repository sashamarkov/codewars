class GroupByDifference {
    constructor(numbers) {
        this.numbers = numbers;
    }
​
    find(difference) {
        const sorted = [...this.numbers].sort((a, b) => a - b);
        let result = [];
        let i = 0;
        while (i < sorted.length) {
          let j = i;
          while (j + 1 < sorted.length && sorted[j + 1] - sorted[j] <= difference) {
            j += 1;
          }
          if (j > i) {
            result = result.concat(sorted.slice(i, j + 1));
          }
          i = j + 1;
        }
        return result;
    }
}