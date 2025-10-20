import math
​
def normalize_text(text):
    return ''.join(c for c in text if c.isalpha()).lower()
​
def find_rectangle_dimensions(length):
    a = math.isqrt(length)
    b = a if a * a >= length else a + 1
    return min(a, b), max(a, b)
​
def create_rectangle(text, a, b):
    rectangle = []
    for i in range(0, len(text), b):
        row = text[i:i+b]
        if len(row) < b:
            row += ' ' * (b - len(row))
        rectangle.append(row)
    return rectangle
​
def read_columns(rectangle, b):
    result = []
    for col in range(b):
        column_chars = ''.join(row[col] for row in rectangle)
        result.append(column_chars)
    return ' '.join(result)
​
def cipher_text(plain_text):
    normalized = normalize_text(plain_text)
    if not normalized:
        return ''
    a, b = find_rectangle_dimensions(len(normalized))
    rectangle = create_rectangle(normalized, a, b)
    return read_columns(rectangle, b)