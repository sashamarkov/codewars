function squaresOnly(array) {
  return array.filter(n=>Math.sqrt(n)%1===0)
}