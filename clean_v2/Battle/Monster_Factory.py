from Characters.Monster import *


class Monster_Factory:

    def make_monster(self, name: str):
        if name == "Troll":
            new_monster = Troll(name)
        else:
            new_monster = Monster(name)
        return new_monster