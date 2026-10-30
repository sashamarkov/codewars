from itertools import takewhile
​
def joker_card(joker_nums, ticket_serials):
    joker = ''.join(str(n % 10) for n in joker_nums)
    prizes = ['I type', 'II type', 'III type', 'IV type', 'V type']
    result = []
    for t in ticket_serials:
        t = t.zfill(6)
        m = sum(1 for _ in takewhile(lambda i: t[-i] == joker[-i], range(1, 7)))
        result.append(prizes[6 - m] if 2 <= m <= 6 else 'Losing card')
    return result