using System;
​
public class Kata {
    public static string FormatMoney( double amount ) {
        return string.Format( "${0:##.00}", Math.Round( amount, 2 ) );
    }
}