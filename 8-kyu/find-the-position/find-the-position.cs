using System;
​
public class Kata {
    private static readonly char[] Alphabet = "abcdefghijklmnopqrstuvwxyz".ToCharArray( );
​
    public static string Position( char alphabet ) {
        var ind = Array.IndexOf( Alphabet, char.ToLower( alphabet ) );
        return string.Format( "Position of alphabet: {0}", ind + 1 );
    }
}