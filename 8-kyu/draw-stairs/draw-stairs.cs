using System.Linq;
​
public class Kata {
    public static string DrawStairs( int n ) {
        return string.Join( "\n", Enumerable.Range( 0, n ).Select( i => new string( ' ', i ) + "I" ) );
    }
}