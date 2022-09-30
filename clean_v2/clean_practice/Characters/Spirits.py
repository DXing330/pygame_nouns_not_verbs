from dataclasses import dataclass
import random
from Config.Character_Dict import *
CD = Character_Dict()

@dataclass
class Spirit:
    name: str
    level: int
    skill_list: list
    exp: int = 0
    skill: int = 999

    def update_skills(self, skill_list: list):
        self.battle_skills = skill_list

    def learn_skill(self, skill: str):
        if skill not in self.skill_list:
            self.skill_list.append(skill)

    def level_up(self):
        if self.exp > self.level ** 2:
            self.level += 1
            self.dict = CD.SPIRIT_SKILLS.get(self.name)
            new_skill = self.dict.get(self.level)
            if new_skill != None:
                self.learn_skill(new_skill)

    def choose_action(self):
        self.skill = 999
        skill = self.battle_skills[random.randint(0, len(self.battle_skills) - 1)]
        return skill