def get_total_cash_prize(prize_fund, correct_answers, player_actions):
    total = 0
    safe = 0
    life = 0
    for i, a in enumerate(player_actions):
        life += sum(c in "123" for c in a)
        act = a[-1]
        if act == "W":
            return total, life
        if act == "X":
            return safe, life
        if act != correct_answers[i]:
            return 0, life
        total += prize_fund[i]
        if (i + 1) % 5 == 0:
            safe = total
    return total, life