interface Count {
  static int countCharOccurrences(String s, char c) {
    return s.length( ) - s.replace(String.valueOf(c), "").length( );
  }
}