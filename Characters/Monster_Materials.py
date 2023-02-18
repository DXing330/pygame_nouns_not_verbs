from dataclasses import dataclass
import random
class Material_Dict:
    def __init__(self):
        self.monster_materials = {
        "Goblin" : "goblin_parts"
        }
M = Material_Dict()

@dataclass
class Material_Chest:
    goblin_parts: int = 0
    demon_parts: int = 0

    def obtain_materials(self, monster):
        material = M.monster_materials.get(monster.name)
        if material == "goblin_parts":
            self.goblin_parts += random.randint(0, monster.level)