from Skills.Effects import *


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
