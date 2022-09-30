from Character import *


@dataclass
class Summon(Character):
    def __init__(self, name, level = 0):
        self.name = name
        self.level = level

    def update_for_battle(self):
        self.update_stats()
        self.update_skills()