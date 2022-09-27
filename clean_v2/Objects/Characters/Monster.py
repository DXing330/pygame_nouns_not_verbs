import random
from dataclasses import dataclass
from Config.Dictionaries.Monster_Dict import *
M = Monster_Dict()
from Config.Dictionaries.Skill_Dict import *
S = Skill_Dict()
from Config.Dictionaries.Element_Dict import *
E = Element_Dict()
from Character import *

@dataclass
class Monster(Character):

    def update_stats(self):
        self.dictionary = M.NAMES.get(self.name)
        while self.level <= 0:
            self.level = round(random.gauss(self.dictionary.get("Level"), self.dictionary.get("Variance")))
        self.max_health = self.level * (self.dictionary.get("Health"))
        self.attack = self.level * (self.dictionary.get("Attack"))
        self.defense = self.level * (self.dictionary.get("Defense"))
        self.max_skill = self.level * (self.dictionary.get("Skill"))
        self.skill = self.max_skill
        self.health = self.max_health
        self.skill_list = []
        self.buffs = []
        self.statuses = []
        self.passive_skills = []
        self.turn = True
        self.skills = True
        self.update_element()

    def update_element(self):
        element = self.dictionary.get("Element")
        self.element = Element(**E.ELEMENTS.get(element))

    def check_attack_element(self):
        return self.element

    def check_defense_element(self):
        return self.element

    def update_skills(self):
        skill_list = self.dictionary.get("Skill_List")
        for word in skill_list:
            skill = Skill(**S.ALL_SKILLS.get(word))
            self.skill_list.append(skill)

    def standby_phase(self, allies, spirits, enemies):
        self.update_battle_state(allies, spirits, enemies)
        for skill in self.skill_list:
            skill : Skill
            if skill.cooldown > 0:
                skill.cooldown -= 1
        for buff in self.buffs:
            buff : Passive
            if buff.timing == "Standby":
                buff.activate(self)
            if buff.power == 0:
                self.buffs.remove(buff)
        for status in self.statuses:
            status : Passive
            if status.timing == "Standby":
                status.activate(self)
            if status.turns == 0:
                self.statuses.remove(status)
        for skill in self.passive_skills:
            skill : Skill
            skill.use(self, self.allies, self.spirits, self.enemies)

    def use_skill(self):
        skill : Skill = self.skill_list[random.randint(0, len(self.skill_list) - 1)]
        if skill.effect == "Summon":
            self.summon(skill)
        else:
            skill.use(self, self.allies, self.spirits, self.enemies)

    def summon(self, name: str):
        summon = Monster(name)
        summon.update_for_battle()
        self.allies.append(summon)

    def summon_skill(self, skill : Skill):
        self.skill -= skill.cost
        if self.skill >= 0 and skill.cooldown <= 0:
            skill.apply_cooldown()
            self.summon(skill.effect_specifics)

    def choose_action(self):
        if len(self.enemies) > 0:
            self.target = self.enemies[random.randint(0, len(self.enemies) - 1)]
            if self.skill > 0 and self.skills:
                self.use_skill()
            else:
                self.skill += 1
                self.basic_attack(self.target)