from dataclasses import dataclass
from Effect import *


@dataclass
class Passive:
    name : str
    effect : str
    effect_specifics : str
    type : str
    power : int = 1
    turns : int = -1

    def decrease_turns(self):
        if self.turns > 0:
            self.turns -= 1

    def apply_effect(self):
        effect = Effect(self.effect, self.effect_specifics,
        self.target_list, self.power)
        effect.apply_effect()

    def update_target(self, target):
        self.target_list = []
        self.target_list.append(target)

    def activate(self, target):
        self.update_target(target)
        self.apply_effect()
        self.decrease_turns()