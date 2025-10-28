using System;
​
public static class Kata {
    public static double DbScale( double intensity ) {
        return 10*Math.Log10( intensity*1000000000000 );
    }
}