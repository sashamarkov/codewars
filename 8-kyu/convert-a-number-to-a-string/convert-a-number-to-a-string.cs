using System.Globalization;
​
public class Kata {
    public static string NumberToString( int num ) {
        return num.ToString( CultureInfo.CurrentCulture );
    }
}