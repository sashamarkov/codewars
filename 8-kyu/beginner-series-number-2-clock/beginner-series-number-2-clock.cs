public static class Clock {
    public static int Past( int h, int m, int s ) {
        return 1000*( h*60*60 + m*60 + s );
    }
}