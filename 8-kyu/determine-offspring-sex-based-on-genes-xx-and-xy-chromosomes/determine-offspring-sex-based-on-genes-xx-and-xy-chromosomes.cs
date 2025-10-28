public class Kata {
    public static string ChromosomeCheck( string sperm ) {
        if ( sperm.Equals( "XY" ) ) {
            return "Congratulations! You're going to have a son.";
        }
        if ( sperm.Equals( "XX" ) ) {
            return "Congratulations! You're going to have a daughter.";
        }
        return string.Empty;
    }
}