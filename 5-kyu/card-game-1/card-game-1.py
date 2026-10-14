class Player:
    def __init__(self, name):
        self.name = name
        self.cards = 0
​
    def take(self, n):
        self.cards += n
​
​
class Game:
    def __init__(self, n):
        self.n = n
        self.players = [Player("Alice"), Player("Bob")]
        self.turn = 0
​
    def take_half(self):
        return self.n % 2 == 0 and (self.n == 4 or self.n // 2 % 2)
​
    def move(self):
        player = self.players[self.turn]
        if self.take_half():
            player.take(self.n // 2)
            self.n //= 2
        else:
            player.take(1)
            self.n -= 1
        self.turn ^= 1
​
    def play(self):
        while self.n:
            self.move()
        return self.players[0].cards
​
​
def card_game(n):
    return Game(n).play()