def replace_words(sentence):
    words = sentence.split()
    sorted_by_len = sorted(words, key=len)
    
    swapped = []
    for w in words:
        pos = sorted_by_len.index(w)
        paired = sorted_by_len[-1 - pos]
        swapped.append(paired)
    result = [swapped[0].capitalize()] + ["I" if w.lower() == "i" else w.lower() for w in swapped[1:]]
    return " ".join(result)  