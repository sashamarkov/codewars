from re import search
​
def happy_coding(nickname):
    s = nickname.lower()
    happy = search(r'\bhappy\b', s)
    coding = search(r'\bcoding\b', s)
    
    if happy and coding:
        return 1 if happy.start() < coding.start() else 2
    if coding:
        return 3
    if happy:
        return 4
    return 5