from math import isinf
def hilberts_hotel(rooms, people, buses):
    r = range(rooms[0], rooms[-1] + 1)
    cases = {
        0: lambda: [room + people * buses for room in r],
        1: lambda: [room * (people + 1) for room in r],
        2: lambda: [room * (buses + 1) for room in r],
        3: lambda: [i * (i + 1) // 2 for i in r]
    }
    return cases[(isinf(people) << 1) | isinf(buses)]()