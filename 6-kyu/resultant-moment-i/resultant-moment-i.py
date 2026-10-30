def rot_pred(arr):
    n = len(arr)
    if n % 2 == 0 or arr[n // 2] != 'S':
        return 'Not a Valid Entry'
    m = sum(arr[i] * (i - n//2) for i in range(n) if i != n//2)
    if m < 0:
        return 'anti clockwise'
    if m > 0:
        return 'clockwise'    
    return 'steady'
​