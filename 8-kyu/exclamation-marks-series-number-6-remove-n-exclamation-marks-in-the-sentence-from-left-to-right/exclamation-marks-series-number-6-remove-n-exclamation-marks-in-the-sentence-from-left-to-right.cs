using System.Text.RegularExpressions;
​
public class Kata {
    public static string Remove( string s, int n ) {
        return Regex.Replace( s, "[!]", m => {
            if ( n-- <= 0 ) {
                return m.Value;
            }
            return "";
        } );
    }
}