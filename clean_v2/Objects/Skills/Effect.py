from dataclasses import dataclass


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
            elif "Cure" in self.effect:
                for status in target.statuses:
                    if status.name == self.effect_specifics:
                        target.statuses.remove(status)
            elif "Disable" in self.effect:
                if "All" in self.effect_specifics:
                    target.turn = False
                elif "Skills" in self.effect_specifics:
                    target.skills = False
                elif "Spells" in self.effect_specifics:
                    target.spells = False


@dataclass
class Battle_Effect:
    effect : str
    effect_specifics : str
    power : int

    def apply_effect(self):
        pass

    def activate(self, attack_power, target):
        self.attack_power = attack_power
        self.target = target
        self.target_attack_element = self.target.check_attack_element()
        self.target_defense_element = self.target.check_defense_element()
        self.apply_effect()


@dataclass
class Attack_Step_Effect(Battle_Effect):

    def apply_effect(self):
        if self.target_attack_element != None and self.target_defense_element != None:
            if self.target_attack_element.name in self.target_defense_element.weaknesses:
                self.attack_power = self.attack_power * 2
            elif self.target_attack_element.name in self.target_defense_element.strengths:
                self.attack_power = self.attack_power//2
        if "Slay" in self.effect and self.target_defense_element != None:
            if self.effect_specifics == self.target_defense_element.name:
                self.attack_power = self.attack_power * self.power


@dataclass
class Defense_Step_Effect(Battle_Effect):

    def apply_effect(self):
        if "Resist" in self.effect and self.target_attack_element != None:
            if self.effect_specifics == self.target_attack_element.name:
                self.attack_power = round(self.attack_power * (1 - (self.power/100)))