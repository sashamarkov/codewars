from itertools import groupby
​
def find_subarray_with_same_element(a, k):
    max_len = 0
    result = (-1, -1)
    start = 0
    for key, group in groupby(a):
        length = len(list(group))
        if key == k:
            if length > max_len or (length == max_len and start > result[0]):
                max_len = length
                result = (start, start + length - 1)
        start += length
    return result if max_len > 0 else (-1, -1)