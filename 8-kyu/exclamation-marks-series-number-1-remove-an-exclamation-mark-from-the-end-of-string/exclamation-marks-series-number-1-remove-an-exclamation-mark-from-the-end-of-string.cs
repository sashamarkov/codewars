using System.Text.RegularExpressions;
​
public class Kata {
    public static string Remove( string s ) {
        return Regex.Replace( s, @"[!]\z", "" );
    }
}