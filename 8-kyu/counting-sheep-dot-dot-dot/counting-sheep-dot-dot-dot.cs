using System;
using System.Linq;
​
public static class Kata {
  public static int CountSheeps( bool[ ] sheeps ) {
     return sheeps.Where( _ => _ ).Count( );
  }
}