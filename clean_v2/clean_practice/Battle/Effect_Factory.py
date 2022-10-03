from Characters.Character import Character
from Skills.Effects import *
from Characters.Equipment import *

@dataclass
class Effect_Factory:
    effect: str
    effect_specifics: str
    power: str
    targets: list

    def make_effect(self):
        for target in self.targets:
            if self.effect == "Change_Stats":
                effect = Change_Stats(self.effect, self.effect_specifics, self.power, target)
                effect.apply_effect()
            if self.effect == "Add_Buff":
                effect = Add_Buff(self.effect, self.effect_specifics, self.power, target)
                effect.apply_effect()
            if self.effect == "Add_Status":
                effect = Add_Status(self.effect, self.effect_specifics, self.power, target)
                effect.apply_effect()
            if self.effect == "Cure_Status":
                effect = Cure_Status(self.effect, self.effect_specifics, self.power, target)
                effect.apply_effect()
            if self.effect == "Disable":
                effect = Disable(self.effect, self.effect_specifics, self.power, target)
                effect.apply_effect()
            if self.effect == "Increase_Damage":
                effect = Increase_Damage(self.effect, self.effect_specifics, self.power, target)
                effect.apply_effect()
            if self.effect == "Decrease_Damage":
                effect = Decrease_Damage(self.effect, self.effect_specifics, self.power, target)
                effect.apply_effect()


@dataclass
class Equipment_Effect_Factory:
    equipment: Equipment
    attack: int
    character: any

    def make_effect(self):
        if self.equipment.target == "Damage":
            attack_effect = Effect_Factory(self.equipment.effect, self.equipment.effect_specifics, self.equipment.power, [self.attack])
            attack_effect.make_effect()
        elif self.equipment.target == "Character":
            attack_effect = Effect_Factory(self.equipment.effect, self.equipment.effect_specifics, self.equipment.power, [self.character])
            attack_effect.make_effect()