def powerset(nums):
    result = [[]]
    for x in reversed(nums):
        result = result + [[x] + s for s in result]
    return result