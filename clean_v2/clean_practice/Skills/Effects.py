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
        if self.turns == 0:
            return True
        return False


@dataclass
class Effect(ABC):
    effect: str
    effect_specifics: str
    power: int
    target: any

    @abstractmethod
    def apply_effect(self):
        pass


@dataclass
class Change_Stats(Effect):

    def apply_effect(self):
        if "Health" in self.effect_specifics:
            self.target.health += self.power
        if "Attack" in self.effect_specifics:
            self.target.attack += self.power
        if "Defense" in self.effect_specifics:
            self.target.defense += self.power
        if "Skill" in self.effect_specifics:
            self.target.skill += self.power
        if "All" in self.effect_specifics:
            self.target.health += self.power
            self.target.attack += self.power//2
            self.target.defense += self.power//4


@dataclass
class Add_Buff(Effect):

    def apply_effect(self):
        buff = Passive(**P.BUFFS.get(self.effect_specifics))
        self.target.add_buff(buff)


@dataclass
class Add_Status(Effect):

    def apply_effect(self):
        status = Passive(**P.STATUSES.get(self.effect_specifics))
        self.target.add_status(status)


@dataclass
class Cure_Status(Effect):

    def apply_effect(self):
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


@dataclass
class Increase_Damage(Effect):

    def apply_effect(self):
        if self.effect_specifics == "Flat":
            self.target += self.power
        elif self.effect_specifics == "Scale":
            scale = self.power / (self.power + 50)
            change = round(self.target * scale)
            self.target += change


@dataclass
class Decrease_Damage(Effect):

    def apply_effect(self):
        if self.effect_specifics == "Flat":
            self.target -= self.power
        elif self.effect_specifics == "Scale":
            scale = self.power / (self.power + 50)
            change = round(self.target * scale)
            self.target -= change