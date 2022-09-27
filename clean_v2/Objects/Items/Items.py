from dataclasses import dataclass
from Objects.Elements import *
from Config.Dictionaries.Element_Dict import *
E = Element_Dict()

@dataclass
class Equipment:
    name : str
    user : str
    allowed_users : list
    effect : str
    effect_specifics : str
    type : str
    power : int
    element_name : str

    def update_element(self):
        self.element = Element(**E.ELEMENTS.get(self.element_name))


@dataclass
class Weapon(Equipment):
    attack : int


@dataclass
class Armor(Equipment):
    defense : int


@dataclass
class Accessory(Equipment):
    pass