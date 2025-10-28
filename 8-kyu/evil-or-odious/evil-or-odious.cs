using System;
using System.Linq;
​
public class Kata {
    public static string Evil( int n ) {
        var ones = Convert.ToString( n, 2 ).Count( d => d == '1' );
        if ( ones%2 == 0 ) {
            return "It's Evil!";
        }
        return "It's Odious!";
​
    }
}