using System;
class Kata {
  public static long Distance(long n) {
    if (n == 1) {
      return 0;
    }
    long k = (long)Math.Ceiling((Math.Sqrt(n) - 1) / 2);
    long m = (2 * k + 1) * (2 * k + 1);
    long d = m - n;
    long pos = d % (2 * k);
    return k + Math.Abs(pos - k);
  }
}