class JurassicWord(object):
    def __init__(self):
        self.dinos = {
            "VvvvV": ("T-Rex", {"a dead dino"}),
            "vvvvv": ("velociraptor", {"a dead dino"}),
            "uuuuu": ("brachiosaurus", {"flowers", "leaves"}),
            "uuVuu": ("triceratops", {"flowers"}),
        }
        self.foods = [
            ("_C",  "C}>", "a dead dino"),
            ("iii", "iii", "flowers"),
            ("|||", "|||", "leaves"),
        ]
​
    def lunch_time(self, scene):
        food, pre = "something", 3
        for p, s, name in self.foods:
            if scene.startswith(p) and scene.endswith(s) and len(scene) == len(p) + 5 + len(s):
                food, pre = name, len(p)
                break
​
        dino = self.dinos.get(scene[pre:pre + 5])
​
        if dino and (food == "something" or food in dino[1]):
            return f"A {dino[0]} is eating {food}."
        return f"Something is eating {food}."