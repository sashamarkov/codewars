def weather_prediction(days, weather_today, final_weather, P):
    v = [float(x == weather_today) for x in range(len(P))]
    while days:
        v = [sum(a * P[x][y] for x, a in enumerate(v)) for y in range(len(P))]
        days -= 1
    return v[final_weather]