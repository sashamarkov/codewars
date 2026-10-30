import os
​
def create_file_dict():
    result = {}
    for f in os.listdir('.'):
        if os.path.isfile(f):
            with open(f, encoding='utf-8', errors='ignore') as fh:
                result[f] = fh.readline()
    return result