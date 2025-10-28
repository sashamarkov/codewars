using System;
using System.Collections.Generic;
using System.Linq;
​
public class Kata {
    public static int[] CountPositivesSumNegatives( int[ ] input ) {
       if ( input == null || input.Length == 0 ) {
          return new int[ 0 ];
       }
       return new[] {
                input.Where( _ => _ > 0 ).Count( ),
                input.Where( _ => _ < 0 ).Sum( )
       };
    }
}