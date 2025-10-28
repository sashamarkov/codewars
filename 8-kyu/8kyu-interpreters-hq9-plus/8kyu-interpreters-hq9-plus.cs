using System;
using System.Text;
​
public class HQ9 {
    public static string Interpret( string code ) {
        if ( code == "H" ) {
            return "Hello World!";
        }
        if ( code == "Q" ) {
            return code;
        }
        if ( code == "9" ) {
            return SongLyrics.Value;
        }
        return null;
    }
​
    private static Lazy<string> SongLyrics = new Lazy<string>( GetSongLyrics );
​
    private static string GetSongLyrics( ) {
        var sb = new StringBuilder( );
        for ( int i = 99; i > 2; i-- ) {
            sb.AppendFormat( "{0} bottles of beer on the wall, {0} bottles of beer.\n", i );
            sb.AppendFormat( "Take one down and pass it around, {0} bottles of beer on the wall.\n", i - 1 );
        }
        sb.Append( "2 bottles of beer on the wall, 2 bottles of beer.\n" );
        sb.Append( "Take one down and pass it around, 1 bottle of beer on the wall.\n" );
        sb.Append( "1 bottle of beer on the wall, 1 bottle of beer.\n" );
        sb.Append( "Take one down and pass it around, no more bottles of beer on the wall.\n" );
        sb.Append( "No more bottles of beer on the wall, no more bottles of beer.\n" );
        sb.Append( "Go to the store and buy some more, 99 bottles of beer on the wall." );
        return sb.ToString( );
    }
}