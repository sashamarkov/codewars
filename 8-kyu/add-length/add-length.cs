using System.Linq;
​
public class Kata {
    public static string[] AddLength( string str ) {
        return str.Split( ' ' ).Select( w => string.Format( "{0} {1}", w, w.Length ) ).ToArray( );
    }
}