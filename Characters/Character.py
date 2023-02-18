from dataclasses import dataclass
from abc import ABC, abstractmethod


@dataclass
class Character(ABC):
    name: str
    skill_list: list
    passive_skills: list
    conditional_passives: list
    buffs: list
    statuses: list
    max_level: int = 10
    level: int = 1
    max_health: int = 0
    health: int = 0
    base_attack: int = 0
    base_defense: int = 0
    base_speed: int = 0
    attack: int = 0
    defense: int = 0
    speed: int = 0
    accuracy: int = 100
    evasion: int = 0
    damage_dealt: int = 100
    damage_taken: int = 100
    max_skill: int = 0
    skill: int = 0
    turn: bool = True
    skills: bool = True
    passives: bool = True
    delayed: bool = False
    exp: int = 0
    weapon: str = None
    armor: str =  None
    temp_health: int = 0
    target = None
    
    def update_stats(self):
        pass

    def update_skills(self):
        pass

    def stats_text(self):
        pass

    def choose_action(self):
        pass

    def possible_actions(self):
        possible_actions = ["Attack"]
        return possible_actions

    def equip_weapon(self, weapon):
        self.weapon = weapon

    def equip_armor(self, armor):
        self.armor = armor

    def add_status(self, effect):
        self.statuses.append(effect)

    def add_buff(self, effect):
        self.buffs.append(effect)

    def unique_passives(self):
        pass