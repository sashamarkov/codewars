public class Kata {
    public static string AbbrevName( string name ) {
        var a = name.Split( ' ' );
        return string.Format( "{0}.{1}", char.ToUpper( a [ 0 ] [ 0 ] ), char.ToUpper( a [ 1 ] [ 0 ] ) );
    }
}