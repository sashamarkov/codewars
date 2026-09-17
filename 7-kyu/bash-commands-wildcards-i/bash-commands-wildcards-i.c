int match (const char *pattern, const char *filename) {
    while (*pattern && *filename) {
      if (*pattern != '?' && *pattern != *filename) {
        return 0;
      }
      pattern += 1;
      filename += 1;
    }
    return *pattern == '\0' && *filename == '\0';
}