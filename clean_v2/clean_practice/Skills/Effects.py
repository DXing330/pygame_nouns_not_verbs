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
        if self.effect_specifics == "ALL":
            self.target.turn = False
        elif self.effect_specifics == "Skills":
            self.target.skills = False