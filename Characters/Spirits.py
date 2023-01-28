from dataclasses import dataclass
import random
from Config.Constants import *
from Config.Character_Dict import *
C = Constants()
CD = Character_Dict()


@dataclass
class Spirit:
    name: str
    partner: str
    level: int
    skill_list: list
    passive_skills: list
    exp: int = 0
    skill: int = 0
    max_level: int = 10
    target = None

    def update_skills(self, skill_list: list):
        self.battle_skills = skill_list
    
    def update_passives(self, passive_list: list):
        self.battle_passives = passive_list

    def update_skill_list(self):
        dict = CD.SPIRIT_SKILLS.get(self.name)
        if len(self.skill_list) <= 0:
            for number in range(0, self.level):
                new_skill = dict.get(number)
                if new_skill != None:
                    self.learn_skill(new_skill)
        else:
            new_skill = dict.get(self.level)
            if new_skill != None:
                self.learn_skill(new_skill)

    def update_passive_list(self):
        dict = CD.SPIRIT_PASSIVES.get(self.name)
        if len(self.passive_skills) <= 0:
            for number in range(0, self.level):
                new_skill = dict.get(number)
                if new_skill != None:
                    self.learn_passive(new_skill)
        else:
            new_skill = dict.get(self.level)
            if new_skill != None:
                self.learn_passive(new_skill)

    def learn_skill(self, skill: str):
        if skill not in self.skill_list:
            self.skill_list.append(skill)
    
    def learn_passive(self, skill: str):
        if skill not in self.passive_skills:
            self.passive_skills.append(skill)

    def level_up(self):
        if self.exp > self.level ** 2 and self.level < self.max_level:
            self.exp = 0
            self.level += 1
            self.update_skill_list()
            self.update_passive_list()

    def evolve(self):
        if "+++" not in self.name:
            if self.level >= self.max_level:
                self.max_level += self.max_level
                self.name += "+"

    def choose_action(self, heroes):
        if self.skill <= 0:
            self.skill += random.randint(1, self.level)
            return None
        else:
            self.skill -= 1
            skill = self.battle_skills[random.randint(0, len(self.battle_skills) - 1)]
            return skill