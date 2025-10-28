using System;
using System.Collections.Generic;
using System.Linq;
​
public class Kata {
  public static List<int> FilterOddNumber( List<int> listOfNumbers ) {
    foreach(var n in listOfNumbers.Where( _ => _%2 == 0).ToList( ) ){
      listOfNumbers.Remove( n );
    }
    return listOfNumbers;
  }
}