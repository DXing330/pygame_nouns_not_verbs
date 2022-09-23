from dataclasses import dataclass
from Objects.Skills.Skill import Skill
from Objects.Skills.Passive import Passive
from Config.Dictionaries.Skill_Dict import *
from Config.Dictionaries.Passive_Dict import *
P = Passive_Dict()


@dataclass
class Character:
    name : str
    level : int = 0

    def update_stats(self):
        self.health = self.level
        self.attack = self.level
        self.defense = self.level
        self.skill = self.level
        self.skill_list = []
        self.passive_skills = []
        self.buffs = []
        self.statuses = []

    def update_skills(self):
        pass

    def update_for_battle(self):
        self.update_stats()
        self.update_skills()

    def update_battle_state(self, allies: list, enemies: list):
        self.allies = allies
        self.enemies = enemies

    def check_element(self):
        return None

    def check_effects(self):
        pass

    def add_effect(self, effect : str):
        new_effect = Passive(**P.ALL_EFFECTS.get(effect))
        if new_effect.type == "Buff":
            self.buffs.append(new_effect)
        else:
            self.statuses.append(new_effect)

    def standby_phase(self):
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

    def use_skill(self):
        pass

    def basic_attack(self, defender):
        self.defender : Character = defender
        self.attack_power = self.attack
        self.defender.health -= max(self.attack_power - self.defender.defense, 1)

    def choose_action(self):
        pass