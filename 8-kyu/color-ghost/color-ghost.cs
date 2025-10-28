using System;
​
public class Ghost {
    private string _color;
​
    public static string[] Colors = {"white", "yellow", "purple", "red"};
​
    public Ghost( ) {
        _color = Colors [ GetRandomIndex( ) ];
    }
​
    public string GetColor( ) {
        return _color;
    }
​
    public static int GetRandomIndex( ) {
        var rand = new Random( Guid.NewGuid( ).GetHashCode( ) );
        return rand.Next( 0, 4 );
    }
}