from Skills.Effects import Conditional_Effect
from Characters.Character import *

class Condition_Checker:

    def check_passive_condition(self, user: Character, conditional: Conditional_Effect):
        if conditional.condition == "Status":
            for status in user.statuses:
                if status.name == conditional.condition_specifics:
                    return True
            return False
        if conditional.condition == "Not_Status":
            for status in user.statuses:
                if status.name == conditional.condition_specifics:
                    return False
            return True
        if conditional.condition == "Low_Health":
            if (user.health/user.max_health) < int(conditional.condition_specifics)/100:
                return True
            return False
        if conditional.condition == "High_Health":
            if (user.health/user.max_health) > int(conditional.condition_specifics)/100:
                return True
            return False

    def check_target_condition(self, user, conditional: Conditional_Effect, target):
        if conditional.condition == "Buff":
            for buff in target.buffs:
                if buff.name == conditional.condition_specifics:
                    return True
            return False
        if conditional.condition == "User_Buff":
            for buff in user.buffs:
                if buff.name == conditional.condition_specifics:
                    return True
            return False
        if conditional.condition == "Status":
            for status in target.statuses:
                if status.name == conditional.condition_specifics:
                    return True
            return False
        if conditional.condition == "Not_Status":
            for status in target.statuses:
                if status.name == conditional.condition_specifics:
                    return False
            return True
        if conditional.condition == "Target":
            if target.name in conditional.condition_specifics:
                return True
            return False
        if conditional.condition == "Low_Health":
            if (target.health/target.max_health) <= int(conditional.condition_specifics)/100:
                return True
            return False
        if conditional.condition == "High_Health":
            if (target.health/target.max_health) >= int(conditional.condition_specifics)/100:
                return True
            return False
