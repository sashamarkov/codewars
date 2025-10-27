import re
​
def spin_solve(sentence):
    transformations = {
        'reverse': reverse_with_punct,
        'uppercase': lambda w: w.upper(),
        'zero': lambda w: re.sub(r'[a-zA-Z]', '0', w, count=1),
        'keep': lambda w: w
    }
    words = sentence.split()
    result = []
    for word in words:
        code = get_transformation_code(word)
        result.append(transformations[code](word))
    return ' '.join(result)
​
def clean_word(word):
    return re.sub(r'[^\w-]', '', word)
​
def get_transformation_code(word):
    clean = clean_word(word)
    if len(clean) > 6 or clean.lower().count('t') >= 2:
        return 'reverse'
    elif len(clean) == 2 or word.endswith(','):
        return 'uppercase'
    elif len(clean) == 1:
        return 'zero'
    else:
        return 'keep'
​
def reverse_with_punct(word):
    match = re.match(r'^(\W*)(.*?)(\W*)$', word)
    if match:
        prefix, core, suffix = match.groups()
        return prefix + core[::-1] + suffix
    return word[::-1]