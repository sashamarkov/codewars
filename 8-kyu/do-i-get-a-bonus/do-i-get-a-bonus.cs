public static class Kata {
  public static string bonus_time( int salary, bool bonus ) {
    return string.Format( "${0}", bonus ? salary*10 : salary );
  }
}