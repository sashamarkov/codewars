def zfc_definition(n: int) -> str:
    t = []
    for i in range(n):
        t.append("{" + ",".join(t) + "}")
    return "{" + ",".join(t) + "}"