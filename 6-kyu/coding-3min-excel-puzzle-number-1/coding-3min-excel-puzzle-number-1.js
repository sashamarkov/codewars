function solveIt(excel) {
  let rowSums = [];
  let colSums = [0,0,0];
  for(let i = 0; i < 4; i++) {
    rowSums[i] = excel[i][0] + excel[i][1] + excel[i][2];
    if(i < 3) {
      for(let j = 0; j < 3; j++) {
        colSums[j] += excel[i][j];
      }
    }
  }
  let wrongRow = excel.findIndex((row,i) => row[3] !== rowSums[i]);
  let wrongCol = [0,1,2].findIndex(j => excel[3][j] !== colSums[j]);
  if(wrongRow !== -1 && wrongCol !== -1) {
    return excel[wrongRow][wrongCol] + (excel[wrongRow][3] - rowSums[wrongRow]);
  }
  if(wrongRow !== -1) {
    return rowSums[wrongRow];
  }
  if(wrongCol !== -1) {
    return colSums[wrongCol];
  }
  return rowSums[3];
}