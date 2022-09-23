from dataclasses import dataclass
import random
from Character import *
from Config.Dictionaries.Spirit_Dict import *
SP = Spirt_Dict()
from Config.Dictionaries.Skill_Dict import Skill_Dict
S = Skill_Dict()

@dataclass
class Spirit(Character):

    def update_skills(self):
        self.dictionary = SP.SKILLS.get(self.name)
        for number in range(0, self.level):
            word = self.dictionary.get(number)
            if word != None:
                skill = Skill(**S.ALL_SKILLS.get(word))
                self.skill_list.append(skill)

    def choose_action(self, allies: list, enemies: list):
        self.skill = 999
        self.allies = allies
        self.enemies = enemies
        if len(self.allies) > 0 and len(self.enemies) > 0:
            used_skill : Skill = self.skill_list[random.randint(0, len(self.skill_list) - 1)]
            used_skill.use(self, self.allies, [], self.enemies)