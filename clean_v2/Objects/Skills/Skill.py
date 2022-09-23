import sys
sys.path.append("./General_Functions")
from dataclasses import dataclass
from Pick import *
from Effect import *


@dataclass
class Skill:
    name : str
    power : int
    effect : str
    effect_specifics : str
    target : str
    cost : int
    pick_randomly : bool = True
    cooldown : int = 0
    cooldown_timer : int = 0

    def update_battle_state(self, user, allies: list, spirits: list, enemies: list):
        self.user = user
        self.allies = allies
        self.spirits = spirits
        self.enemies = enemies

    def apply_cost(self):
        self.user.skill -= self.cost

    def apply_cooldown(self):
        self.cooldown += self.cooldown_timer

    def pick_targets(self):
        self.target_list = []
        if self.target == "Self":
            self.target_list.append(self.user)
        elif self.target == "Ally":
            pick_from = Pick(self.allies, self.pick_randomly)
            target = pick_from.pick()
            self.target_list.append(target)
        elif self.target == "Spirit":
            pick_from = Pick(self.spirits, self.pick_randomly)
            target = pick_from.pick()
            self.target_list.append(target)
        elif self.target == "Enemy":
            pick_from = Pick(self.enemies, self.pick_randomly)
            target = pick_from.pick()
            self.target_list.append(target)
        elif self.target == "All_Ally":
            self.target_list = self.allies
        elif self.target == "All_Enemy":
            self.target_list = self.enemies
        elif self.target == "All_Spirit":
            self.target_list = self.spirits

    def apply_effect(self):
        if "Skill" in self.effect:
            pass
        elif "Command" in self.effect:
            for target in self.target_list:
                for number in range(0, self.power):
                    target.choose_action(self.allies, self.enemies)
        elif "Attack" in self.effect:
            for target in self.target_list:
                for number in range(0, self.power):
                    if "Basic" in self.effect_specifics:
                        self.user.basic_attack(target)
        elif "Summon" in self.effect:
            pass
        else:
            effect = Effect(self.effect, self.effect_specifics, self.target_list,
            self.power * self.user.level)
            effect.apply_effect()

    def use(self, user, allies: list, spirits: list, enemies: list):
        self.user = user
        self.allies = allies
        self.spirits = spirits
        self.enemies = enemies
        if self.cooldown <= 0:
            self.apply_cost()
            self.apply_cooldown()
            self.pick_targets()
            self.apply_effect()