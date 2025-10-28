using System.Linq;
​
public class Kata {
    public static int[] DivisibleBy( int[] numbers, int divisor ) {
        return numbers.Where( n => n%divisor == 0 ).ToArray( );
    }
}