public class Kata {
    public static string DatingRange( int age ) {
        int min = age/2 + 7;
        int max = ( age - 7 )*2;
        if ( age <= 14 ) {
            min = ( int ) ( age - 0.10*age );
            max = ( int ) ( age + 0.10*age );
        }
        return string.Format( "{0}-{1}", min, max );
    }
}