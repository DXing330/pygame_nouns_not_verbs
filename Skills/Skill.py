from dataclasses import dataclass


@dataclass
class Skill:
    name: str
    effect: str
    effect_specifics: str
    power: int
    targets: str
    cost: int
    scale: str = "Level"
    cooldown: int = 0
    cooldown_counter: int = 0
    chance: int = 100
    condition: str = "Always"
    condition_specifics: str = "Always"

    def determine_power(self, user):
        if self.scale == "Level":
            return self.power * user.level
        elif self.scale == "None":
            return self.power
        elif self.scale == "Attack":
            return self.power * user.attack
        elif self.scale == "Defense":
            return self.power * user.defense
        elif self.scale == "Skill":
            return self.power * user.skill
        elif self.scale == "Health":
            return self.power * user.health
        
    def view_stats_part_one(self):
        return ("~ "+self.name+", effect: "+self.effect+", effect_specifics: "+self.effect_specifics+", power: "+str(self.power)+", scaling: "+self.scale+", targets: "+self.targets)
    
    def view_stats_part_two(self):
        text =  ("cooldown: "+str(self.cooldown)+", cooldown_counter: "+str(self.cooldown_counter)+", chance: "+str(self.chance))
        if self.condition != "Always":
            text += (", condition: "+self.condition+", condition_specifics: "+self.condition_specifics)
        return text