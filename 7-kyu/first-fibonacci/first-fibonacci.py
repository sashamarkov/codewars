def solution(first, second):
    while second - first >= 0 and second - first <= first:
        first, second = second - first, first  
    return (first, second)
​