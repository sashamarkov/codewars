def predict(candidates, polls):
    total_weight = sum(weight for _, weight in polls)
    return {
        name: round1(sum(res[i] * wt for res, wt in polls) / total_weight)
        for i, name in enumerate(candidates)
    }