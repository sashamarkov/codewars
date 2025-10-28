using System.Text.RegularExpressions;
​
public class Kata {
    public static bool ValidateHello( string greetings ) {
        return Regex.IsMatch( greetings, @"\b(hello)|(ciao)|(salut)|(hallo)|(hola)|(ahoj)|(czesc)\b",
            RegexOptions.IgnoreCase );
    }
}