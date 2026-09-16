SHEEP = sorted('sheep')
​
def reload_sheeps(arr):
    return ['sheep' for w in arr if sorted(w) == SHEEP]