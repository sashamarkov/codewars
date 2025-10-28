using System;
​
public class Slope {
    public String slope( int[] points ) {
        var n = points [ 3 ] - points [ 1 ];
        var d = points [ 2 ] - points [ 0 ];
        if ( d == 0 ) {
            return "undefined";
        }
        return Convert.ToString( n/d );
    }
}