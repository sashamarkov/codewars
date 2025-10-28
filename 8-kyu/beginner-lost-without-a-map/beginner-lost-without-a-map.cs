using System.Linq;
​
public class Kata {
    public static int[] Maps( int[] x ) {
        return x.Select( n => 2*n ).ToArray( );
    }
}