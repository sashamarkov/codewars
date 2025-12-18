def sort_by_depth(arr):
    def depth(x):
        return 1 if not x else depth(x[0]) + 1
    return sorted(arr, key=depth)