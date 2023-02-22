from Characters.Monster import *


class Monster_Factory:

    def make_monster(self, name: str, level: int = 0, catch_rate: int = 1):
        if name == "Troll":
            new_monster = Troll(name, level, catch_rate)
        elif name == "Serpent":
            new_monster = Serpent(name, level, catch_rate)
        elif name == "Cocoon":
            new_monster = Cocoon(name, level, catch_rate)
        elif name == "Assasin":
            new_monster = Assasin(name, level, -9)
        elif "Slime" in name:
            new_monster = Slime(name, level, catch_rate)
        elif "Dragon" in name:
            new_monster = Dragon(name, level, catch_rate)
        else:
            new_monster = Monster(name, level, catch_rate)
        return new_monster