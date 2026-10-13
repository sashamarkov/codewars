from collections import namedtuple
​
Bot = namedtuple('Bot', ('name', 'make_move'))
​
def create_bot(x, y):
    return Bot(
        name = 'Bot',
        make_move = lambda n: (n - 1) % (y + 1) or 1
    )
​
# Uncomment next line to show all game logs.  Default: show only lost games.
# log_all_games = True