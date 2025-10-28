using System;
​
public class Kata {
    public static double SquareArea( double A ) {
        var r = 4*A/( 2*Math.PI );
        return Math.Round( r*r, 2 );
    }
}