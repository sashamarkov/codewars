namespace myjinxin {
  public class Kata {
    public string[][] VolleyballPositions(string[][] formation, int k) {
      int[][] pos = { null, new[]{3,2}, new[]{1,2}, new[]{0,1}, new[]{1,0}, new[]{3,0}, new[]{2,1} };
      var result = new string[4][] { new string[3], new string[3], new string[3], new string[3] };
      int shift = k % 6;
      for (int p = 1; p <= 6; p++) {
        int start = ((p - 1 + shift) % 6) + 1;
        result[pos[start][0]][pos[start][1]] = formation[pos[p][0]][pos[p][1]];
      }
      for  (int r = 0; r < 4; r++) {
        for (int c = 0; c < 3; c++) {
          result[r][c] ??= "empty";
        }
      }
      return result;
    }
  }
}