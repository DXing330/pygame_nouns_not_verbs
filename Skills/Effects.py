import random
from abc import ABC, abstractmethod
from dataclasses import dataclass
from Config.Passive_Dict import *
P = Passive_Dict()


@dataclass
class Passive:
    name: str
    effect: str
    effect_specifics: str
    power: int = 1
    turns: int = -1

    def check_turns(self):
        if self.turns > 0:
            self.turns -= 1
        if round(self.turns) == 0:
            return True
        return False


class Conditional_Effect:
    def __init__(self, name, timing, condition, condition_specifics, effect, effect_specifics, power: int = 1):
        self.name = name
        self.timing = timing
        self.condition = condition
        self.condition_specifics = condition_specifics
        self.effect = effect
        self.effect_specifics = effect_specifics
        self.power = power


@dataclass
class Effect(ABC):
    effect: str
    effect_specifics: str
    power: int

    def add_target(self, target):
        self.target = target

    @abstractmethod
    def apply_effect(self):
        pass


@dataclass
class Change_Stats(Effect):

    def apply_effect(self):
        if "Temp_Health" in self.effect_specifics:
            self.target.temp_health += self.power
        elif "Health" in self.effect_specifics:
            self.target.health += self.power
        elif "Attack" in self.effect_specifics:
            self.target.attack += self.power
        elif "Defense" in self.effect_specifics:
            self.target.defense += self.power
        elif "Skill" in self.effect_specifics:
            self.target.skill += max(self.power//10, 1)
        elif "Accuracy" in self.effect_specifics:
            self.target.accuracy += self.power
        elif "Evasion" in self.effect_specifics:
            self.target.evasion += self.power
        elif "Max_Health" in self.effect_specifics:
            self.target.max_health += self.power
        elif "Base_Attack" in self.effect_specifics:
            self.target.base_attack += self.power
        elif "Base_Defense" in self.effect_specifics:
            self.target.base_defense += self.power
        elif "Damage_Dealt" in self.effect_specifics:
            self.target.damage_dealt += self.power
        elif "Damage_Taken" in self.effect_specifics:
            self.target.damage_taken += self.power
        elif "Physical" in self.effect_specifics:
            self.target.attack += self.power
            self.target.defense += self.power//2
        elif "All" in self.effect_specifics:
            self.target.health += self.power//2
            self.target.attack += self.power//4
            self.target.defense += self.power//8
        elif "All_Base" in self.effect_specifics:
            self.target.max_health += self.power//4
            self.target.base_attack += self.power//8
            self.target.base_defense += self.power//16


@dataclass
class Add_Buff(Effect):

    def apply_effect(self):
        buff = Passive(**P.BUFFS.get(self.effect_specifics))
        self.target.add_buff(buff)


@dataclass
class Remove_Buff(Effect):

    def apply_effect(self):
        if self.effect_specifics == "All":
            if len(self.target.buffs) > 0:
                self.target.buffs.pop(-1)
        for buff in self.target.buffs:
            if buff.name == self.effect_specifics:
                self.target.buffs.remove(buff)


@dataclass
class Add_Status(Effect):

    def apply_effect(self):
        status = Passive(**P.STATUSES.get(self.effect_specifics))
        self.target.add_status(status)


@dataclass
class Cure_Status(Effect):

    def apply_effect(self):
        if self.effect_specifics == "All":
            if len(self.target.statuses) > 0:
                self.target.statuses.pop(-1)
        for status in self.target.statuses:
            if status.name == self.effect_specifics:
                self.target.statuses.remove(status)


@dataclass
class Disable(Effect):

    def apply_effect(self):
        if self.effect_specifics == "All":
            self.target.turn = False
        elif self.effect_specifics == "Skills":
            self.target.skills = False
        elif self.effect_specifics == "Passives":
            self.target.passives = False


@dataclass
class Increase_Damage(Effect):

    def apply_effect(self):
        if self.effect_specifics == "Flat":
            self.target.damage += self.power
        elif self.effect_specifics == "Scale":
            scale = self.power / (self.power + 50)
            change = round(self.target.damage * scale)
            self.target.damage += change


@dataclass
class Decrease_Damage(Effect):

    def apply_effect(self):
        if self.effect_specifics == "Flat":
            self.target.damage -= self.power
        elif self.effect_specifics == "Scale":
            scale = self.power / (self.power + 50)
            change = round(self.target.damage * scale)
            self.target.damage -= change


@dataclass
class Critical_Hit(Effect):

    def apply_effect(self):
        luck = random.randint(0, 99)
        if luck <= self.power:
            self.target = self.target * 2


@dataclass
class Dodge(Effect):
    
    def apply_effect(self):
        luck = random.randint(0, 99)
        if luck <= self.power:
            self.target = 0