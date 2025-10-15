def different_digits_number_search(arr):
    return next((n for n in arr if len(str(n)) == len(set(str(n)))), -1)