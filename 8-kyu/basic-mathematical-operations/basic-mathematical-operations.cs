using System;
using System.Collections.Generic;
​
namespace Solution {
  public static class Program {
    public static double basicOp( char op, double val1, double val2 ) {
      var dic = new Dictionary<char, Func<double, double, double>>( )
            {
                {'+', ( d1, d2 ) => d1 + d2},
                {'-', ( d1, d2 ) => d1 - d2},
                {'*', ( d1, d2 ) => d1 * d2},
                {'/', ( d1, d2 ) => d1 / d2},
            };
            return dic[ op ]( val1, val2 );
    }
  }
}