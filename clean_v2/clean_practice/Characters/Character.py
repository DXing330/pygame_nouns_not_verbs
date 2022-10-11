from dataclasses import dataclass
from abc import ABC, abstractmethod


@dataclass
class Character(ABC):
    name: str
    level: int
    max_health: int
    health: int
    attack: int
    defense: int
    max_skill: int
    skill: int
    skill_list: list
    passive_skills: list
    buffs: list
    statuses: list
    turn: bool = True
    skills: bool = True
    exp: int = 0
    weapon: any = None
    armor: any =  None
    temp_health: int = 0
    
    @abstractmethod
    def update_stats(self):
        pass

    @abstractmethod
    def update_skills(self):
        pass

    @abstractmethod
    def stats_text(self):
        pass

    @abstractmethod
    def choose_action(self):
        pass

    def equip_weapon(self, weapon):
        self.weapon = weapon

    def equip_armor(self, armor):
        self.armor = armor

    def add_status(self, effect):
        self.statuses.append(effect)

    def add_buff(self, effect):
        self.buffs.append(effect)

    def update_skills(self, skill_list: list):
        self.battle_skills = skill_list

    def update_passive_skills(self, skill_list: list):
        self.battle_passives = skill_list

    def update_death_skills(self, skill_list: list):
        self.battle_death_skills = skill_list