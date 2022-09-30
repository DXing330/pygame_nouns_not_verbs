import pygame
pygame.init()
from dataclasses import dataclass
from Character import Character
from Config.Constants import *
from Config.Character_Dict import *
C = Constants()
CD = Character_Dict()


@dataclass
class Hero(Character):
    exp: int = 0
    max_mana: int = 0
    mana: int = 0
    spells: bool = True
    weapon: any = None
    armor: any =  None

    def update_stats(self):
        self.dict = CD.HERO_STATS.get(self.name)
        self.max_health = self.dict.get("health") * self.level
        self.attack = self.dict.get("attack") * self.level
        self.defense = self.dict.get("defense") * self.level
        self.max_skill = self.dict.get("skill") * self.level
        self.max_mana = self.dict.get("mana") * self.level
        self.health = self.max_health
        self.skill = self.max_skill
        self.mana = self.max_mana

    def learn_skill(self, skill: str):
        if skill not in self.skill_list:
            self.skill_list.append(skill)

    def level_up(self):
        if self.exp > self.level ** 2 and self.level < C.LEVEL_LIMIT:
            self.level += 1
            self.update_stats()
            self.dict = CD.HERO_SKILLS.get(self.name)
            for number in range(0, self.level):
                new_skill = self.dict.get(self.level)
                if new_skill != None:
                    self.learn_skill(new_skill)
