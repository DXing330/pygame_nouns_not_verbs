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
    
    @abstractmethod
    def update_stats(self):
        pass

    @abstractmethod
    def update_skills(self):
        pass

    def add_status(self, effect):
        self.statuses.append(effect)

    def add_buff(self, effect):
        self.buffs.append(effect)