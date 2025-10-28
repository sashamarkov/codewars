using System.Text.RegularExpressions;
​
public static class Kata {
    public static bool IsLockNessMonster( string sentence ) {
        return Regex.IsMatch( sentence, "(tree fiddy)|(three fifty)|(3.50)", RegexOptions.IgnoreCase );
    }
}