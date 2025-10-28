using System.Linq;
​
public class Kata {
    public static int StrCount( string str, char letter ) {
        return str.Count( c => c.Equals( letter ) );
    }
}