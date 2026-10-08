from itertools import cycle
​
class Player(RockPaperScissorsPlayer):
    STRATEGIES = {
        'Vitraj Bachchan': 'R',
        'Sven Johanson' : 'RRSPPR',
        'Max Janssen': 'P',
        'Bin Jinhao': 'RPRSPS',
        'Jonathan Hughes': 'SRP',
    }
    def __init__(self):
        self.cycle = None
        
    def get_name(self):
        return "MyPlayer"
    
    def get_shape(self):
        return next(self.cycle)
    
    def set_new_match(self, opponentName):
        self.cycle = cycle(self.STRATEGIES.get(opponentName, 'S'))
        
    def set_opponent_shape(self, shape):
        pass 