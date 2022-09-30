import pygame
pygame.init()
from dataclasses import dataclass
from Character import Character
from Config.Character_Dict import *
C = Character_Dict()


@dataclass
class Hero(Character):
    exp: int = 0
    max_mana: int = 0
    mana: int = 0
    spells: bool = True
    weapon: any = None
    armor: any =  None
    accessory: any = None

    def update_stats(self):
        self.dict = C.HERO_STATS.get(self.name)
        self.max_health = self.dict.get("health") * self.level
        self.attack = self.dict.get("attack") * self.level
        self.defense = self.dict.get("defense") * self.level
        self.max_skill = self.dict.get("skill") * self.level
        self.max_mana = self.dict.get("mana") * self.level
        self.health = self.max_health
        self.skill = self.max_skill
        self.mana = self.max_mana

    def update_skills(self, skill_list: list):
        self.battle_skills = skill_list

    def learn_skill(self, skill: str):
        if skill not in self.skill_list:
            self.skill_list.append(skill)

    def level_up(self):
        if self.exp > self.level ** 2:
            self.level += 1
            self.dict = C.HERO_SKILLS.get(self.name)
            new_skill = self.dict.get(self.level)
            if new_skill != None:
                self.learn_skill(new_skill)
