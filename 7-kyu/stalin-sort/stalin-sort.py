def stalin_sort(arr):
    if not arr: return
    j = 1
    for i, x in enumerate(arr[1:], 1):
        if x >= arr[j-1]:
            arr[j] = x
            j += 1
    del arr[j:]