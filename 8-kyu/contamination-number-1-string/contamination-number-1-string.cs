using System.Linq;
​
public class Kata {
    public static string Contamination( string text, string character ) {
        if ( string.IsNullOrEmpty( text ) || string.IsNullOrEmpty( character ) ) {
            return string.Empty;
        }
        return string.Concat( Enumerable.Repeat( character, text.Length ) );
    }
}