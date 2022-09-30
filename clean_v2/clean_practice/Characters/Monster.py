import random
from Character import *
from Config.Character_Dict import *
from Config.Skill_Dict import *
C = Character_Dict()
S = Skill_Dict()

class Monster(Character):
    def __init__(self, name, level = 0):
        self.name = name
        self.level = level

    def update_stats(self):
        self.dict = C.MONSTER_STATS.get(self.name)
        self.turn = True
        self.skills = True
        self.buffs = []
        self.statuses = []
        self.skill_list = []
        self.passive_skills = []
        while self.level == 0:
            self.level = round(random.gauss(self.dict.get("level"), self.dict.get("variance")))
        self.max_health = self.dict.get("health") * self.level
        self.attack = self.dict.get("attack") * self.level
        self.defense = self.dict.get("defense") * self.level
        self.skill = self.dict.get("skill") * self.level
        self.health = self.max_health

    def update_skills(self):
        pass

    def update_for_battle(self):
        self.update_stats()
        self.update_skills()

    def choose_action(self):
        pass