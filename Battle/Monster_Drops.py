from Characters.Party import *
from Characters.Monster import *

class Monster_Drops:
    def __init__(self, party: Party, monsters: list[Monster]):
        self.party = party
        self.monsters = monsters
        self.dictionary = CD.MONSTER_DROPS

    def monster_loot(self):
        for monster in self.monsters:
            dictionary = self.dictionary.get(monster.name)
            if dictionary != None:
                self.roll_loot(monster, dictionary)

    def roll_loot(self, monster: Monster, dictionary: dict):
        roll = random.randint(0, monster.level+1)
        loot = dictionary.get(roll)
        if loot != None:
            if loot == "Poison_Extract":
                self.party.items.poison_extract += 1
            if loot == "Poison_Essense":
                self.party.items.poison_essense += 1
            if loot == "Monster_Extract":
                self.party.items.monster_essence += 1
            if loot == "Monster_Essense":
                self.party.items.monster_essence += 1