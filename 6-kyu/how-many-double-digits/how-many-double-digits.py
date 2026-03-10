def number_of_duplicate_digits(ndigit):
    if ndigit == 1:
        return 0
    return 9 * 10**(ndigit - 1) - 9**ndigit 