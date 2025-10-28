using System;
using System.Collections.Generic;
​
public partial class Kata {
    public static string AliasGen( string fName, string lName ) {
        var fKey = Convert.ToString( char.ToUpper( fName [ 0 ] ) );
        var lKey = Convert.ToString( char.ToUpper( lName [ 0 ] ) );
        if ( !FirstName.ContainsKey( fKey ) ||
             !Surname.ContainsKey( lKey ) ) {
            return "Your name must start with a letter from A - Z.";
        }
        return string.Format( "{0} {1}", FirstName [ fKey ], Surname [ lKey ] );
    }
}