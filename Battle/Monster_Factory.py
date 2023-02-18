from Characters.Monster import *


class Monster_Factory:

    def make_monster(self, name: str, level: int = 0):
        if name == "Troll":
            new_monster = Troll(name, level)
        elif name == "Serpent":
            new_monster = Serpent(name, level)
        elif name == "Cocoon":
            new_monster = Cocoon(name, level)
        elif name == "Assasin":
            new_monster = Assasin(name, level)
        else:
            new_monster = Monster(name, level)
        return new_monster