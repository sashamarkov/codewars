def choose_best_home(places, preferences, priorities):
    def score(home):
        return sum(6 - i for i, t in enumerate(priorities[:6]) if home.get(t) == preferences.get(t))
    return min(places, key=lambda n: (-score(places[n]), n))
​
​
​