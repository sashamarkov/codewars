def sum_words(s):
    v = {
        'a':13, 'b':3, 'c':7, 'd':4, 'e':23, 'f':25, 'g':6, 'h':20, 'i':24, 'j':2,
        'k':15, 'l':22, 'm':19, 'n':1, 'o':10, 'p':18, 'q':11, 'r':21, 's':26,
        't':12, 'u':5, 'v':14, 'w':16, 'x':9, 'y':17, 'z':8
    }
    return [sum(v[ch] for ch in word) for word in s.split()]