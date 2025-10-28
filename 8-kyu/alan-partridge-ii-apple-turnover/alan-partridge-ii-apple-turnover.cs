using System;
​
public class Kata {
    public static string Apple( object n ) {
        var num = Convert.ToInt32( n );
        if ( num*num > 1000 ) {
            return "It's hotter than the sun!!";
        }
        return "Help yourself to a honeycomb Yorkie for the glovebox.";
    }
}