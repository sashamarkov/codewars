class PlanetFinder:
    REQUIRED_ELEMENTS = {'H', 'C', 'N', 'O', 'P', 'Ca'}
    
    def __init__(self, solar_system, max_size):
        self.solar_system = solar_system
        self.max_size = max_size
        self.best_planet = ""
        self.best_size_diff = float('inf')
    
    def find_best_planet(self):
        for planet in self.solar_system:
            elements, size = self._parse_planet(planet)
            if self._meets_requirements(elements) and self._within_size_limit(size):
                if self._is_better_planet(planet, size):
                    self.best_planet = planet
                    self.best_size_diff = self.max_size - size    
        return self.best_planet
    
    def _parse_planet(self, planet):
        elements_str, size_str = planet.split('_')
        elements = []
        i = 0
        while i < len(elements_str):
            if i + 1 < len(elements_str) and elements_str[i+1].islower():
                elements.append(elements_str[i:i+2])
                i += 2
            else:
                elements.append(elements_str[i])
                i += 1
        
        return set(elements), int(size_str)
    
    def _meets_requirements(self, elements):
        return self.REQUIRED_ELEMENTS.issubset(elements)
    
    def _within_size_limit(self, size):
        return size <= self.max_size
    
    def _is_better_planet(self, candidate_planet, candidate_size):
        if self.best_planet == "":
            return True
        candidate_diff = self.max_size - candidate_size
        return candidate_diff < self.best_size_diff
​
def best_planet(solar_system, max_size):
    finder = PlanetFinder(solar_system, max_size)
    return finder.find_best_planet()