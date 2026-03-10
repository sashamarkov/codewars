from collections import Counter
​
def consecutive_nums(lst, group_len):
    if len(lst) % group_len != 0:
        return False
    counter = Counter(lst)
    for num in sorted(counter):
        while counter[num] > 0:
            for k in range(group_len):
                if counter[num + k] <= 0:
                    return False
                counter[num + k] -= 1
    return True