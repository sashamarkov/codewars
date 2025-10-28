using System;
using System.Linq;
​
public class Kata {
    public static int FindDifference( int[] a, int[] b ) {
        return Math.Abs( a.Aggregate( ( n1, n2 ) => n1*n2 ) - b.Aggregate( ( n1, n2 ) => n1*n2 ) );
    }
}