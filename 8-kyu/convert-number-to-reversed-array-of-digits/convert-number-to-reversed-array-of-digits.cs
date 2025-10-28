using System;
using System.Linq;
using System.Collections.Generic;
​
namespace Solution {
  class Digitizer {
    public static long[] Digitize( long n ) {
        return n.ToString( ).Reverse( ).Select( _ => Int64.Parse( _.ToString( ) ) ).ToArray( );
    }
  }
}