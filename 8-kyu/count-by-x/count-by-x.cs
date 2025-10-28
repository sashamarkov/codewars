using System;
​
public static class Kata {
  public static int[] CountBy( int x, int n ) {
     int[] z = new int[ n ]; 
     var cnt = 0;
     int i = 0;
     while ( cnt < n ) {
        i++;
        if ( i % x == 0 ) {
           z[ cnt ] = i;
           cnt++;
        }
     }
     return z;
  }
}