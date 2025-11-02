using System;
​
public class JomoPipi {
    public static char[ ][ ] Shift( char[ ][ ] m, int n ) {
        char[ ] flattened = MatrixToArray( m );
        char[ ] rotated = RotateArray( flattened, n );
        return ArrayToMatrix( rotated, m.Length, m[ 0 ].Length );
    }
    
    private static char[ ] MatrixToArray( char[ ][ ] m ) {
        int rows = m.Length;
        int cols = m[ 0 ].Length;
        char[ ] flat = new char[ rows * cols ];
        
        int index = 0;
        for ( int i = 0; i < rows; i++ )
            for ( int j = 0; j < cols; j++ )
                flat[ index++ ] = m[ i ][ j ];
                
        return flat;
    }
    
    private static char[ ] RotateArray( char[ ] arr, int n ) {
        int length = arr.Length;
        n %= length;
        if ( n < 0 ) n += length;
        
        char[ ] rotated = new char[ length ];
        for ( int i = 0; i < length; i++ )
            rotated[ ( i + n ) % length ] = arr[ i ];   
        return rotated;
    }
    
    private static char[ ][ ] ArrayToMatrix( char[ ] arr, int rows, int cols ) {
        char[ ][ ] matrix = new char[ rows ][ ];
        int index = 0;
        
        for ( int i = 0; i < rows; i++ ) {
            matrix[ i ] = new char[ cols ];
            for ( int j = 0; j < cols; j++ )
                matrix[ i ][ j ] = arr[ index++ ];
        }
        return matrix;
    }
}