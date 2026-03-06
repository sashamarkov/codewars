#include <ctype.h>
#include <stddef.h>
​
char *stringLeftStrip(char *target, const char *chars) {
    if (!target) return NULL;
    
    const char *remove = chars ? chars : " \f\n\r\t\v";
    if (!*remove) return target;
    
    char *start = target;
    while (*start) {
        const char *r = remove;
        int found = 0;
        while (*r) if (*start == *r++) { found = 1; break; }
        if (!found) break;
        start++;
    }
    
    if (start != target) {
        char *dest = target;
        while ((*dest++ = *start++));
    }
    return target;
}