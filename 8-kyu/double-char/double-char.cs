using System.Text.RegularExpressions;
​
public class Kata {
  public static string DoubleChar( string s ) {
    return Regex.Replace( s, ".", match => string.Concat(match.Value, match.Value ) );
  }
}