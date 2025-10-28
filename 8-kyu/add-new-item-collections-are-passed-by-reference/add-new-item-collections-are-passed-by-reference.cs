using System.Collections.Generic;
​
public class AddMore {
    public static List<int> AddExtra( List<int> listOfNumbers ) {
        var result = new List<int>( listOfNumbers );
        result.Add( 13 );
        return result;
    }
}