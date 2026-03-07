function coinsNeeded(amount, coinDenominations) {
  return coinDenominations.sort((a, b) => b - a).reduce(([rem, cnt], c) => [rem % c, cnt + Math.floor(rem / c)], [amount, 0])[1];
}