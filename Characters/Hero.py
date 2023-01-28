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
    weapon: str = None
    armor: str =  None
    real_name: str = None

    def update_stats(self):
        dict = CD.HERO_STATS.get(self.name)
        self.max_health = dict.get("health") * self.level
        self.base_attack = dict.get("attack") * self.level
        self.base_defense = dict.get("defense") * self.level
        self.base_speed = dict.get("speed")
        self.max_skill = dict.get("skill") * self.level
        self.accuracy = 100
        self.evasion = 0
        self.damage_dealt = 100
        self.damage_taken = 100
        self.health = self.max_health
        self.skill = self.max_skill
        self.attack = self.base_attack
        self.defense = self.base_defense
        self.speed = self.base_speed

    def stats_text(self):
        text = str(self.name+"~ HP: "+str(round(self.health+self.temp_health))+" ATK: "+str(round(self.attack))+" DEF: "+str(round(self.defense))+" SKL: "+str(round(self.skill)))
        return text

    def update_skill_list(self):
        dict = CD.HERO_SKILLS.get(self.name)
        if len(self.skill_list) <= 0:
            for number in range(0, self.level):
                new_skill = dict.get(number)
                if new_skill != None:
                    self.learn_skill(new_skill)
        else:
            new_skill = dict.get(self.level)
            if new_skill != None:
                self.learn_skill(new_skill)

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
            self.update_stats()
            self.update_skill_list()

    def choose_action(self):
        choose = True
        choice = None
        while choose:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    choose = False
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    pygame.event.clear()
                    if event.key == pygame.K_a:
                        choice = "Attack"
                        return choice
                    if event.key == pygame.K_s:
                        choice = "Skill"
                        return choice
                    if event.key == pygame.K_i:
                        choice = "Item"
                        return choice

    def possible_actions(self):
        possiblities = []
        if self.turn:
            possiblities.append(self.name+" Attack")
        if self.skills:
            possiblities.append(self.name+" Skill")
        possiblities.append("Item")
        return possiblities
