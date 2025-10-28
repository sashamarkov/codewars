using System.Linq;
​
class AverageSolution {
  public static double FindAverage( double[] array ) {
    if ( array.Any( ) ) {
      return array.Average( );  
    }
    return 0;
  }
} 