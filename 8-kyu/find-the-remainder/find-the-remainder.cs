using System;
​
public class Kata {
    public static int Remainder( int a, int b ) {
        var min = Math.Min( a, b );
        if ( min == 0 ) {
            throw new DivideByZeroException( );
        }
        var max = Math.Max( a, b );
        return max%min;
    }
}