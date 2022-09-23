from dataclasses import dataclass
# Problem with summoning and circular imports, the effect needs to know what to summon, but the summon can also use skills that have effects
# Also some of the skill effects are more than just effects, like attacking, using skills or commanding.
@dataclass
class Effect:
    effect : str
    effect_specifics : str
    target_list : list
    power : int = 1

    def apply_effect(self):
        for target in self.target_list:
            if "Change_Stats" in self.effect:
                if "Attack" in self.effect_specifics:
                    target.attack -= self.power
                elif "Defense" in self.effect_specifics:
                    target.defense -= self.power
                elif "Health" in self.effect_specifics:
                    target.health -= self.power
            elif "Buff" in self.effect or "Status" in self.effect:
                target.add_effect(self.effect_specifics)