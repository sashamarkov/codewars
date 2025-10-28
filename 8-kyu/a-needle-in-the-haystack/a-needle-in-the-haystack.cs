using System;
using System.Linq;
​
public class Kata {
  public static string FindNeedle(object[] haystack) {
     return string.Format("found the needle at position {0}", Enumerable.Range(0, haystack.Length).First(i => Convert.ToString(haystack[i]) == "needle"));
  }
}