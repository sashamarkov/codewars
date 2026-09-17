def do_they_agree(alice, bob):
    c = set(alice) & set(bob)
    return [x for x in alice if x in c] == [x for x in bob if x in c]