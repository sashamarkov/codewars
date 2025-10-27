function isPrime(str) {
    return hasPrimeWord(str) || hasPrimeInNumbers(str);
}
​
function hasPrimeWord(str) {
    return /prime/i.test(str);
}
​
function hasPrimeInNumbers(str) {
    return (str.match(/\d+/g) || []).map(Number).some(isPrimeNumber);
}
​
function isPrimeNumber(n) {
    return n > 1 && isNotDivisible(n, 2);
}
​
function isNotDivisible(n, i) {
    return i * i > n || (n % i !== 0 && isNotDivisible(n, i + 1));
}