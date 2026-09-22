from preloaded import fuel_map
​
def successful_mission(solar_system, destination_planet, fuel):
    a, b = sorted((solar_system.index("Earth"), solar_system.index(destination_planet)))
    path = solar_system[a + 1:b]
    return fuel >= sum(fuel_map[p] for p in path) + 2 * fuel_map[destination_planet]