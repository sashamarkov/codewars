using System;
​
public class Kata {
    public static int CloseCompare( double a, double b, double margin = 0 ) {
        var diff = Math.Abs( a - b );
        if ( margin >= diff ) {
            return 0;
        }
        if ( a > b ) {
            return 1;
        }
        return -1;
    }
}