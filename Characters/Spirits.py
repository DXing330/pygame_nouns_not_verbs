from dataclasses import dataclass
import random
from Config.Constants import *
from Config.Character_Dict import *
from Config.Skill_Dict import *
from Skills.Skill import Skill
C = Constants()
CD = Character_Dict()
S = Skill_Dict()


@dataclass
class Spirit:
    name: str
    partner: str
    level: int
    skill_list: list
    passive_skills: list
    exp: int = 0
    skill: int = 0
    max_level: int = 10
    active: bool = True
    target = None

    def stats_text(self):
        return (self.name+": "+" LVL: "+str(self.level)+" ACTIVE: "+str(self.active))
    
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

    def update_skill_list(self):
        dict = CD.SPIRIT_SKILLS.get(self.name)
        if len(self.skill_list) <= 0:
            for number in range(0, self.level):
                new_skill = dict.get(number)
                if new_skill != None:
                    real_skill = Skill(**S.ALL_SKILLS.get(new_skill))
                    self.learn_skill(real_skill)
        else:
            new_skill = dict.get(self.level)
            if new_skill != None:
                real_skill = Skill(**S.ALL_SKILLS.get(new_skill))
                self.learn_skill(real_skill)

    def update_passive_list(self):
        dict = CD.SPIRIT_PASSIVES.get(self.name)
        if len(self.passive_skills) <= 0:
            for number in range(0, self.level+1):
                new_skill = dict.get(number)
                if new_skill != None:
                    real_skill = Skill(**S.ALL_SKILLS.get(new_skill))
                    self.learn_passive(real_skill)
        else:
            new_skill = dict.get(self.level)
            if new_skill != None:
                real_skill = Skill(**S.ALL_SKILLS.get(new_skill))
                self.learn_passive(real_skill)

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
            self.update_skill_list()
            self.update_passive_list()

    def evolve(self):
        if "+++" not in self.name:
            if self.level >= self.max_level:
                self.max_level += self.max_level
                self.name += "+"

    def choose_action(self, heroes):
        targets = []
        if self.skill <= 0:
            self.skill += random.randint(1, self.level)
            return None, targets
        else:
            skill = self.skill_list[random.randint(0, len(self.skill_list) - 1)]
            # If it's a single target skill, make sure it has a good target.
            if skill.targets == "Hero":
                targets = self.choose_target(skill, heroes)
                # If the chosen skill has no target, then try to use another skill.
                if len(targets) < 1:
                    skill, targets = self.choose_action(heroes)
            try:
                self.skill -= skill.cost
            except:
                if len(targets) > 1:
                    self.skill -= len(targets)
                elif len(targets) == 1:
                    for target in targets:
                        self.skill -= target.level
                else:
                    self.skill -= 1
            return skill, targets

    def choose_target(self, skill, heroes):
        potential_target_list = []
        target_list = []
        if skill.effect == "Cure_Status":
            for hero in heroes:
                if len(hero.statuses) > 0:
                    potential_target_list.append(hero)
        if skill.effect == "Change_Stats":
            if skill.effect_specifics == "Temp_Health":
                for hero in heroes:
                    potential_target_list.append(hero)
            if skill.effect_specifics == "Health":
                for hero in heroes:
                    if hero.health < hero.max_health:
                        potential_target_list.append(hero)
            if skill.effect_specifics == "Skill":
                for hero in heroes:
                    if hero.skill < hero.max_skill:
                        potential_target_list.append(hero)
        if len(potential_target_list) > 1:
            target = potential_target_list[random.randint(0, len(potential_target_list)-1)]
            target_list.append(target)
        else:
            target_list = potential_target_list
        return target_list

@dataclass
class Angel(Spirit):

    def choose_action(self, heroes):
        return super().choose_action(heroes)

    def choose_target(self, skill, heroes):
        return super().choose_target(skill, heroes)

@dataclass
class Fairy(Spirit):

    def choose_action(self, heroes):
        return super().choose_action(heroes)

    def choose_target(self, skill, heroes):
        return super().choose_target(skill, heroes)