class PriceDisplayFraction(object):
    def __init__(self, denominator=16):
        self.d = denominator
        
    def to_display(self, cents):
        dollars = int(cents) // 100
        cents_remain = int(cents) % 100
        frac = int(round((cents - int(cents)) * self.d))
        if frac == self.d:
            frac = 0
            cents_remain += 1
            if cents_remain == 100:
                cents_remain = 0
                dollars += 1
        return f"{dollars}.{cents_remain:02d}/{frac}"
    
    def to_internal(self, display):
        dollars, rest = display.split('.')
        cents, frac = rest.split('/')
        return int(dollars) * 100 + int(cents) + int(frac) / self.d