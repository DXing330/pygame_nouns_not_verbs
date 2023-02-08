class Aura:
    def __init__(self, name, effect, effect_specifics, targets, power: int = 1, turns: int = -1, chance: int = 100, type: str = "None"):
        self.name = name
        self.type = type
        self.effect = effect
        self.effect_specifics = effect_specifics
        self.targets = targets
        self.power = power
        self.turns = turns
        self.chance = chance
        self.type = type

    def aura_effect_text(self):
        if self.name == "Rain":
            return ("Rain is falling.")
        elif self.name == "Fog":
            return ("Fog surrounds the area.")
        elif self.name == "Darkness":
            return ("Darkness covers the area.")
        elif self.name == "Snow":
            return ("Snow is falling.")

    def aura_end_text(self):
        if self.name == "Rain":
            return ("The rain stops.")
        elif self.name == "Fog":
            return ("The fog clears")
        elif self.name == "Darkness":
            return ("The darkness lifts.")
        elif self.name == "Snow":
            return ("The snow stops.")