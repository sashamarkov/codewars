import re
def sp_eng(sentence):
    return bool(re.search(r"english", sentence, re.I))