function raffleOdds(totals, purchased) {
  const [num, den] = totals.reduce(
    ([num, den], _, i) => [
      num * BigInt(totals[i] - purchased[i]),
      den * BigInt(totals[i])
    ],
    [1n, 1n]
  );
  const g = gcd(den - num, den);
  return `${(den - num) / g}/${den / g}`;
}
​
const gcd = (a, b) => b === 0n ? a : gcd(b, a % b);