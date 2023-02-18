import pygame
pygame.init()
from dataclasses import dataclass
from Character import Character
from Config.Constants import *
from Config.Character_Dict import *
from Config.Skill_Dict import *
from Skills.Skill import Skill
C = Constants()
CD = Character_Dict()
S = Skill_Dict()


@dataclass
class Hero(Character):
    exp: int = 0
    weapon = None
    armor =  None
    accessory = None
    real_name: str = None

    def update_stats(self, original = True):
        dict = CD.HERO_STATS.get(self.name)
        if original:
            self.max_health = dict.get("bhealth")
            self.base_attack = dict.get("battack")
            self.base_defense = dict.get("bdefense")
            self.base_speed = dict.get("speed")
            self.max_skill = dict.get("bskill")
            self.accuracy = 100
            self.evasion = 0
            self.damage_dealt = 100
            self.damage_taken = 100
            for number in range(self.level):
                self.update_stats(False)
        elif not original:
            self.max_health += dict.get("health")
            self.base_attack += dict.get("attack")
            self.base_defense += dict.get("defense")
            self.max_skill += dict.get("skill")
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
        skill_list = []
        for skill in self.skill_list:
            skill_list.append(skill.name)
        return ("Skills: "+str(skill_list))
    
    def passives_text(self):
        skill_list = []
        for skill in self.passive_skills:
            skill_list.append(skill.name)
        return ("Passives: "+str(skill_list))

    def update_skill_list(self, original = True):
        dict = CD.HERO_SKILLS.get(self.name)
        if original:
            for number in range(0, self.level):
                new_skill = dict.get(number)
                if new_skill != None:
                    real_skill = Skill(**S.ALL_SKILLS.get(new_skill))
                    self.learn_skill(real_skill)
        elif not original:
            new_skill = dict.get(self.level)
            if new_skill != None:
                real_skill = Skill(**S.ALL_SKILLS.get(new_skill))
                self.learn_skill(real_skill)

    def learn_skill(self, skill):
        if skill not in self.skill_list:
            self.skill_list.append(skill)

    def learn_passive(self, skill):
        if skill not in self.passive_skills:
            self.passive_skills.append(skill)

    def level_up(self):
        if self.exp > self.level ** 2 and self.level < self.max_level:
            self.exp = 0
            self.level += 1
            self.update_stats(False)
            self.update_skill_list(False)

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
