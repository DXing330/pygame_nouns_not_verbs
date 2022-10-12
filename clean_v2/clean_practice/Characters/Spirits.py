from dataclasses import dataclass
import random
from Config.Constants import *
from Config.Character_Dict import *
C = Constants()
CD = Character_Dict()


@dataclass
class Spirit:
    name: str
    level: int
    skill_list: list
    exp: int = 0
    skill: int = 0

    def update_skills(self, skill_list: list):
        self.battle_skills = skill_list

    def update_skill_list(self):
        dict = CD.SPIRIT_SKILLS.get(self.name)
        for number in range(0, self.level):
            new_skill = dict.get(number)
            if new_skill != None:
                self.learn_skill(new_skill)

    def learn_skill(self, skill: str):
        if skill not in self.skill_list:
            self.skill_list.append(skill)

    def level_up(self):
        if self.exp > self.level ** 2 and self.level < C.LEVEL_LIMIT:
            self.level += 1
            self.update_skill_list()

    def choose_action(self):
        if self.skill == 0:
            self.skill += random.randint(0, self.level)
            return None
        else:
            self.skill -= 1
            skill = self.battle_skills[random.randint(0, len(self.battle_skills) - 1)]
            return skill