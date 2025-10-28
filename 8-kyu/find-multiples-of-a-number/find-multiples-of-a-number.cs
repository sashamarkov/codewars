using System.Collections.Generic;
using System.Linq;
​
public class Kata {
    public static List<int> FindMultiples( int integer, int limit ) {
        return Enumerable.Range( 1, limit/integer ).Select( i => integer*i ).ToList( );
    }
}