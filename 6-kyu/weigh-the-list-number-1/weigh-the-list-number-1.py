def weigh_the_list(a):
    return [a[i^1] * (1,-1)[i%2] for i in range(len(a))]