import random
from Character import *
from Config.Character_Dict import *
from Config.Skill_Dict import *
CD = Character_Dict()
S = Skill_Dict()

class Monster(Character):
    def __init__(self, name, level = 0):
        self.name = name
        self.level = level

    def update_stats(self):
        self.dict = CD.MONSTER_STATS.get(self.name)
        self.turn = True
        self.skills = True
        self.buffs = []
        self.statuses = []
        self.skill_list = []
        self.passive_skills = []
        self.weapon = None
        self.armor = None
        while self.level == 0:
            self.level = round(random.gauss(self.dict.get("level"), self.dict.get("variance")))
        self.max_health = self.dict.get("health") * self.level
        self.attack = self.dict.get("attack") * self.level
        self.defense = self.dict.get("defense") * self.level
        self.skill = self.dict.get("skill") * self.level
        self.health = self.max_health

    def choose_action(self):
        self.skill += 1
        useable_skills = []
        if self.skills:
            for skill in self.battle_skills:
                if skill.cost <= self.skill:
                    useable_skills.append(skill)
            for skill in useable_skills:
                if skill.cooldown > 0:
                    useable_skills.remove(skill)
        if len(useable_skills) > 0:
            return useable_skills[random.randint(0, len(useable_skills) - 1)]
        return None