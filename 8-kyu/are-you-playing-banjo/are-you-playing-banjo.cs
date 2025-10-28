using System;
​
public class Kata {
  public static string AreYouPlayingBanjo( string name ) {
    if ( name.StartsWith( "R", StringComparison.OrdinalIgnoreCase ) ) {
      return string.Format( "{0} plays banjo", name );
    }
    return string.Format( "{0} does not play banjo", name );
  }
}