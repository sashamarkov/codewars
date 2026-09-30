def sorted_comm_by_digs(arr1, arr2):
    common = set(arr1) & set(arr2)
    return sorted(common, key=lambda x: (-f(x), x))
​
def f(n):
    dr = sum(int(d) for d in str(n))
    dsddr = sum(int(d) ** 2 for d in str(dr))
    return dr + dsddr