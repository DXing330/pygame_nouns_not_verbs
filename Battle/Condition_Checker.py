from Skills.Effects import Conditional_Passive
from Characters.Character import *

class Condition_Checker:

    def check_passive_condition(self, user: Character, conditional: Conditional_Passive):
        if conditional.condition == "Status":
            for status in user.statuses:
                if status.name == conditional.condition_specifics:
                    return True
        return False

    def check_attack_condition(self, user: Character, conditional: Conditional_Passive, defender: Character):
        if conditional.condition == "Target":
            if defender.name in conditional.condition_specifics:
                return True
        return False

    def check_defend_condition(self, user: Character, conditional: Conditional_Passive, attacker: Character):
        if conditional.condition == "Target":
            if attacker.name in conditional.condition_specifics:
                return True
        return False