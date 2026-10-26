def mutations(alice, bob, word, first):
    return Game([alice, bob], word, first).play()
​
class Game:
    def __init__(self, memories, word, first):
        self.memories = memories
        self.used = {word}
        self.prev = word
        self.player = first
        self.first = first
        self.played = 0
        self.chance = False
​
    def is_valid(self, w):
        return (w not in self.used
                and len(set(w)) == 4
                and sum(a != b for a, b in zip(w, self.prev)) == 1)
​
    def find_word(self):
        return next((w for w in self.memories[self.player] if self.is_valid(w)), None)
​
    def on_fail(self):
        if self.played == 0 and not self.chance and self.player == self.first:
            self.chance = True
            self.player = 1 - self.player
            return None
        return -1 if self.played == 0 else 1 - self.player
​
    def play(self):
        while True:
            found = self.find_word()
            if found is None:
                result = self.on_fail()
                if result is not None:
                    return result
                continue
            self.used.add(found)
            self.prev = found
            self.played += 1
            if self.chance:              
                return self.player       
            self.player = 1 - self.player