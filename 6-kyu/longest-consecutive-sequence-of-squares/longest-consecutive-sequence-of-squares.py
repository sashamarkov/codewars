def longest_sequence(n: int) -> list[int]:
    left = 1
    right = 1
    current = 1
    result = []
    while right * right <= n:
        if current < n:
            right += 1
            current += right * right
        elif current > n:
            current -= left * left
            left += 1
        else:
            arr = list(range(left, right + 1))
            if (len(arr)) > len(result):
                result = arr
            current -= left * left
            left += 1
    
    return result