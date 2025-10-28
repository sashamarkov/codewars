public static class Kata {
    public static int CountSquares( int cuts ) {
        if ( cuts == 0 ) {
            return 1;
        }
        return 6*cuts*cuts + 2;
    }
}