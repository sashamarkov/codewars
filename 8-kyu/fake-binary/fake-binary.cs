using System.Text.RegularExpressions;
​
public class Kata {
  public static string FakeBin( string x ) {
     return Regex.Replace( x, "([0-4])|([5-9])", match => match.Groups[1].Success ? "0" : "1" );
  }
}