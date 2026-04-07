function missingNumber(board1, board2) {
  let sum = 0;
  let sumSign = 1;
  for (let i = 0; i < board1.length; i++) {
    for (let j = 0; j < board2.length; j++) {
      const sign = (i + j) % 2 === 0 ? 1 : -1;
      sum += sign * board1[i][j];
      if (board2[i][j] !== "?") {
        sum -= sign * board2[i][j];
      } else {
        sumSign = sign;        
      }
    }
  }
  return sumSign * sum;
}