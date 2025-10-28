namespace Solution {
    using System;
​
    public static class Program {
        public static int binToDec( string s ) {
            return Convert.ToInt32( s, 2 );
        }
    }
}