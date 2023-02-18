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
        text = str(self.name+" HP: "+str(round(self.health+self.temp_health))+" ATK: "+str(round(self.attack))+" DEF: "+str(round(self.defense)))
        return text

    def update_stats(self, flow: int = 0):
        self.dict = CD.MONSTER_STATS.get(self.name)
        self.turn = True
        self.skills = True
        self.used_skill = None
        self.buffs = []
        self.statuses = []
        self.skill_list = []
        self.passive_skills = []
        self.conditional_passives = []
        self.death_skills = []
        self.weapon = None
        self.armor = None
        while self.level <= 0:
            self.level = round(random.gauss(self.dict.get("level"), self.dict.get("variance")))
        self.max_health = self.dict.get("health") * self.level + random.randint(0, flow//90)
        self.base_attack = self.dict.get("attack") * self.level
        self.base_defense = self.dict.get("defense") * self.level
        self.base_speed = self.dict.get("speed")
        self.max_skill = self.dict.get("skill") * self.level
        self.accuracy = 100
        self.evasion = 0
        self.damage_dealt = 100
        self.damage_taken = 100
        self.health = self.max_health
        self.skill = self.max_skill
        self.attack = self.base_attack
        self.defense = self.base_defense
        self.speed = self.base_speed
        self.target = None

    def update_base_stats(self):
        self.max_health = self.dict.get("health") * self.level
        self.base_attack = self.dict.get("attack") * self.level
        self.base_defense = self.dict.get("defense") * self.level
        self.max_skill = self.dict.get("skill") * self.level

    def update_preemptives(self, preemptives: list):
        self.preemptives = preemptives

    def choose_skill(self):
        for skill in self.skill_list:
            try:
                if skill.cost <= self.skill:
                    self.useable_skills.append(skill)
            # In case the cost is a string, just append it.
            except:
                self.useable_skills.append(skill)
        for skill in self.useable_skills:
            if skill.cooldown > 0:
                self.useable_skills.remove(skill)

    def choose_action(self, heroes, monsters):
        self.action = "Attack"
        self.used_skill = None
        self.skill += 1
        self.useable_skills = []
        # Basic monster always has a chance to basic attack.
        number = random.randint(0, 1)
        if self.skills and number > 0 and self.skill > 0:
            self.choose_skill()
        if len(self.useable_skills) > 0:
            self.used_skill = self.useable_skills[random.randint(0, len(self.useable_skills) - 1)]
            # The monster's will telecast what they will do next.
            self.action = str(self.used_skill.name)


class Summon(Monster):
    def __init__(self, name, level = 0):
        self.name = name
        self.level = level

    def choose_action(self):
        possiblities = []
        if self.turn:
            possiblities.append(self.name+" Attack")
        if self.skills and len(self.battle_skills) > 0:
            possiblities.append(self.name+" Skill")
        return possiblities
        


class Troll(Monster):
    def choose_skill(self):
        if self.health < self.max_health//2:
            for skill in self.battle_skills:
                if skill.name == "Heal Self":
                    self.useable_skills.append(skill)
        else:
            for skill in self.battle_skills:
                try:
                    if skill.cost <= self.skill:
                        self.useable_skills.append(skill)
                except:
                    self.useable_skills.append(skill)
            for skill in self.useable_skills:
                if skill.cooldown > 0:
                    self.useable_skills.remove(skill)
                if skill.name == "Heal Self":
                    self.useable_skills.remove(skill)


class Serpent(Monster):
    def choose_skill(self):
        # First the snake picks a target.
        if self.target == None:
            self.counter = 0
            for skill in self.battle_skills:
                if "Target" in skill.name:
                    self.useable_skills.append(skill)
        else:
            # Then it bites the target.
            if self.counter == 0:
                self.counter += 1
                for skill in self.battle_skills:
                    if "Bite" in skill.name:
                        self.useable_skills.append(skill)
            # Then it poisons the target.
            elif self.counter > 0:
                for skill in self.battle_skills:
                    if "Poison" in skill.name:
                        self.useable_skills.append(skill)

    def choose_action(self, heroes, monsters):
        self.action = "Attack"
        self.used_skill = None
        self.skill += 1
        self.useable_skills = []
        if self.skills:
            self.choose_skill()
        if len(self.useable_skills) > 0:
            self.used_skill = self.useable_skills[random.randint(0, len(self.useable_skills) - 1)]
            self.action = str(self.used_skill.name)


class Cocoon(Monster):
    def choose_action(self, heroes, monsters):
        self.action = "Nothing"
        self.used_skill = None
        self.useable_skills = []
        if self.skills:
            self.choose_skill()
        if len(self.useable_skills) > 0:
            self.used_skill = self.useable_skills[random.randint(0, len(self.useable_skills) - 1)]
            self.action = str(self.used_skill.name)

    # The cocoon slowly grows stronger until it hatches.
    def unique_passives(self):
        self.max_health -= self.level
        self.health -= self.level
        self.level += 1


class Assasin(Monster):
    def choose_skill(self):
        invisible = False
        for buff in self.buffs:
            if buff.name == "Invisible":
                invisible = True
        # The assasin will always try to go invisible to use its other skills.
        if not invisible:
            for skill in self.battle_skills:
                if "Invisible" in skill.name:
                    self.useable_skills.append[skill]
        if invisible:
            # The assasin will go for the kill after buffing.
            if self.damage_dealt > 100:
                for skill in self.battle_skills:
                    if skill.effect == "Attack":
                        self.useable_skills.append(skill)
            # Otherwise the assasin will buff themselves.
            elif self.damage_dealt <= 100:
                for skill in self.battle_skills:
                    if skill.effect_specifics == "Damage_Dealt":
                        self.useable_skills.append(skill)

    def choose_action(self, heroes, monsters):
        self.action = "Attack"
        self.used_skill = None
        self.skill += 1
        self.useable_skills = []
        if self.skills and self.skill > 0:
            self.choose_skill()
        if len(self.useable_skills) > 0:
            self.used_skill = self.useable_skills[random.randint(0, len(self.useable_skills) - 1)]
            self.action = str(self.used_skill.name)