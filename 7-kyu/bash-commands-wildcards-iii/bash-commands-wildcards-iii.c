#include <stdlib.h>
​
char **match (const char *pattern, const char **filenames) {
  size_t count = 0;
  for (const char **f = filenames; *f; f++) {
    if (matches(pattern, *f)) {
      count += 1;
    }
  }
  char **result = malloc((count + 1) * sizeof(char *));
  size_t i = 0;
  for (const char **f = filenames; *f; f++) {
    if (matches(pattern, *f)) {
      result[i++] = (char *)*f;
    }
  }
  result[i] = NULL;
  return result;
}
​
int matches(const char *pattern, const char *name) {
  while (*pattern && *name) {
    if (*pattern != '?' && *pattern != *name) {
      return 0;
    }
    pattern +=1;
    name += 1;
  }
  return *pattern == '\0' && *name == '\0';
}