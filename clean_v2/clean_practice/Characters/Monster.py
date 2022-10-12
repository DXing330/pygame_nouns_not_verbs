import pygame
pygame.init()
import random
from Character import *
from Config.Character_Dict import *
CD = Character_Dict()

class Monster(Character):
    def __init__(self, name, level = 0):
        self.name = name
        self.level = level
        self.action = "Attack"
        self.counter = 0

    def stats_text(self):
        text = str(self.name+" LVL: "+str(self.level)+" HP: "+str(self.health))
        return text

    def update_stats(self):
        self.dict = CD.MONSTER_STATS.get(self.name)
        self.turn = True
        self.skills = True
        self.buffs = []
        self.statuses = []
        self.skill_list = []
        self.passive_skills = []
        self.death_skills = []
        self.weapon = None
        self.armor = None
        while self.level == 0:
            self.level = round(random.gauss(self.dict.get("level"), self.dict.get("variance")))
        self.max_health = self.dict.get("health") * self.level
        self.attack = self.dict.get("attack") * self.level
        self.defense = self.dict.get("defense") * self.level
        self.skill = self.dict.get("skill") * self.level
        self.health = self.max_health

    def choose_skill(self):
        for skill in self.battle_skills:
                if skill.cost <= self.skill:
                    self.useable_skills.append(skill)
        for skill in self.useable_skills:
            if skill.cooldown > 0:
                self.useable_skills.remove(skill)

    def choose_action(self):
        self.action = "Attack"
        self.used_skill = None
        self.skill += 1
        self.useable_skills = []
        # Basic monster always has a chance to basic attack.
        number = random.randint(0, 1)
        if self.skills and number > 0:
            self.choose_skill()
        if len(self.useable_skills) > 0:
            self.used_skill = self.useable_skills[random.randint(0, len(self.useable_skills) - 1)]
            self.action = str(self.used_skill.name)


class Summon(Monster):
    def __init__(self, name, level = 0):
        self.name = name
        self.level = level

    def choose_action(self):
        choose = True
        choice = None
        if len(self.skill_list) <= 0:
            choice = "Attack"
            return choice
        while choose:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    pygame.event.clear()
                    if event.key == pygame.K_a:
                        choice = "Attack"
                        return choice
                    if event.key == pygame.K_s:
                        choice = "Skill"
                        return choice


class Troll(Monster):
    def choose_skill(self):
        if self.health < self.max_health:
            for skill in self.battle_skills:
                if skill.name == "Heal Self":
                    self.useable_skills.append(skill)
        else:
            for skill in self.battle_skills:
                if skill.cost <= self.skill:
                    self.useable_skills.append(skill)
            for skill in self.useable_skills:
                if skill.cooldown > 0:
                    self.useable_skills.remove(skill)
                if skill.name == "Heal Self":
                    self.useable_skills.remove(skill)


class Explosive(Monster):
    def choose_skill(self):
        if self.counter < 3:
            self.counter += 1
        else:
            self.used_skill = "Explode"