using System.Linq;
​
public class Kata {
    public static int[] DifferenceInAges( int[] ages ) {
        var sorted = ages.OrderBy( _ => _ ).ToArray( );
        return new[] {sorted [ 0 ], sorted [ sorted.Length - 1 ], sorted [ sorted.Length - 1 ] - sorted [ 0 ]};
    }
}