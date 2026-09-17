#include <stdio.h>
#include <stdarg.h>
​
char* formatString (char *buffer, size_t bufferLength, const char *format, ...) {
  va_list args;
  va_start(args, format);
  vsnprintf(buffer, bufferLength, format, args);
  va_end(args);
  return buffer;
}