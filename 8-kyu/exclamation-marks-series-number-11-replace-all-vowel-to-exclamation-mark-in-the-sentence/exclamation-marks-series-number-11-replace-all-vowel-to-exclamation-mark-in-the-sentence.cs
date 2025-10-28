using System.Text.RegularExpressions;
​
public static class Kata {
    public static string Replace( string s ) {
        return Regex.Replace( s, "[aeiouAEIOU]", "!" );
    }
}