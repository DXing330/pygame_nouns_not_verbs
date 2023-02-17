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
    accessory: str = None
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

    def full_stats_text(self):
        text = str(self.name+"~ MAX HP: "+str(self.max_health)+" HP: "+str(round(self.health+self.temp_health))+" ATK: "+str(round(self.attack))+" DEF: "+str(round(self.defense))+" MAX SKL: "+str(self.max_skill)+" SKL: "+str(round(self.skill)))
        return text
    
    def skills_text(self):
        return ("Skills: "+str(self.skill_list))
    
    def passives_text(self):
        return ("Passives: "+str(self.passive_skills))

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
        possiblities = []
        if self.turn:
            possiblities.append(self.name+" Attack")
        if self.skills:
            possiblities.append(self.name+" Skill")
        if self.skills and not self.delayed:
            possiblities.append("Delay Action")
        possiblities.append("Use Item")
        return possiblities
