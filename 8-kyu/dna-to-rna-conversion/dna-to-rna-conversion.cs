namespace Converter {
    public class Converter {
        public string dnaToRna( string dna ) {
            if ( string.IsNullOrEmpty( dna ) ) {
                return dna;
            }
            return dna.Replace( "T", "U" );
        }
    }
}