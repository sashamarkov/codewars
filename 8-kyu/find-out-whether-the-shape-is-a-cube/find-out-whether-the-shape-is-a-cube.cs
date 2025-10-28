namespace CubeCheck {
    using System;
​
    public class CubeChecker {
        public bool IsCube( double volume, double side ) {
            if ( volume <= 0 || side <= 0 ) {
                return false;
            }
            return Math.Abs( side*side*side - volume ) < double.Epsilon;
        }
    }
}