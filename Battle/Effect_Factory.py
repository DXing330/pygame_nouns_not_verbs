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
        if "Change_Stats" in self.effect:
                effect = Change_Stats(self.effect, self.effect_specifics, self.power)
        elif "Add_Buff" in self.effect:
            effect = Add_Buff(self.effect, self.effect_specifics, self.power)
        elif "Add_Status" in self.effect:
            effect = Add_Status(self.effect, self.effect_specifics, self.power)
        elif "Remove_Buff" in self.effect:
            effect = Remove_Buff(self.effect, self.effect_specifics, self.power)
        elif "Cure_Status" in self.effect:
            effect = Cure_Status(self.effect, self.effect_specifics, self.power)
        elif "Disable" in self.effect:
            effect = Disable(self.effect, self.effect_specifics, self.power)
        elif "Increase_Damage" in self.effect:
            effect = Increase_Damage(self.effect, self.effect_specifics, self.power)
        elif "Decrease_Damage" in self.effect:
            effect = Decrease_Damage(self.effect, self.effect_specifics, self.power)
        elif "Critical_Hit" in self.effect:
            effect = Critical_Hit(self.effect, self.effect_specifics, self.power)
        elif "Dodge" in self.effect:
            effect = Dodge(self.effect, self.effect_specifics, self.power)
        for target in self.targets:
            effect.add_target(target)
            effect.apply_effect()


@dataclass
class Equipment_Effect_Factory:
    equipment: Equipment
    attack: any
    character: any

    def make_effect(self):
        if self.equipment.target == "Damage":
            attack_effect = Effect_Factory(self.equipment.effect, self.equipment.effect_specifics, self.equipment.power, [self.attack])
            attack_effect.make_effect()
        elif self.equipment.target == "Character":
            attack_effect = Effect_Factory(self.equipment.effect, self.equipment.effect_specifics, self.equipment.power, [self.character])
            attack_effect.make_effect()