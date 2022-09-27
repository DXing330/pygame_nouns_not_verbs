from dataclasses import dataclass
from Objects.Skills.Skill import Skill
from Objects.Skills.Passive import Passive
from Objects.Items.Items import *
from Config.Dictionaries.Skill_Dict import *
from Config.Dictionaries.Passive_Dict import *
from Skills.Effect import Attack_Step_Effect
P = Passive_Dict()


@dataclass
class Character:
    name : str
    level : int = 0

    def update_stats(self):
        self.health = self.level
        self.attack = self.level
        self.defense = self.level
        self.skill = self.level
        self.skill_list = []
        self.passive_skills = []
        self.buffs = []
        self.statuses = []
        self.turn = True
        self.skills = True
        self.spells = True
        self.weapon : Weapon = None
        self.armor : Armor = None
        self.accessory : Accessory = None


    def update_skills(self):
        pass

    def update_for_battle(self):
        self.update_stats()
        self.update_skills()

    def check_attack_element(self):
        if self.weapon != None:
            return self.weapon.element
        return None

    def check_defense_element(self):
        if self.armor != None:
            return self.armor.element
        return None

    def check_attack_effects(self):
        if self.weapon != None:
            self.attack_power += self.weapon.attack
            attack_effect = Attack_Step_Effect(self.weapon.effect, self.weapon.effect_specifics, self.weapon.power)
            attack_effect.activate(self.attack_power, self.defender)

    def check_defense_effects(self):
        if self.defender.armor != None:
            self.attack_power -= self.defender.armor.defense
            defense_effect = Attack_Step_Effect(self.defender.armor.effect, self.defender.armor.effect_specifics, self.defender.armor.power)
            defense_effect.activate(self.attack_power, self)

    def add_effect(self, effect : str):
        new_effect = Passive(**P.ALL_EFFECTS.get(effect))
        if new_effect.type == "Buff":
            self.buffs.append(new_effect)
        else:
            self.statuses.append(new_effect)

    def standby_phase(self, allies : list, spirits : list, enemies : list):
        self.update_battle_state(allies, spirits, enemies)
        for skill in self.skill_list:
            skill : Skill
            if skill.cooldown > 0:
                skill.cooldown -= 1
        for buff in self.buffs:
            buff : Passive
            buff.activate(self)
            if buff.power == 0:
                self.buffs.remove(buff)
        for status in self.statuses:
            status : Passive
            status.activate(self)
            if status.turns == 0:
                self.statuses.remove(status)

    def use_skill(self):
        pass

    def summon(self, skill):
        pass

    def basic_attack(self, defender):
        self.defender : Character = defender
        self.attack_power = self.attack
        self.check_attack_effects()
        self.check_defense_effects()
        self.defender.health -= max(self.attack_power - self.defender.defense, 1)

    def pierce_attack(self, defender):
        self.defender : Character = defender
        self.attack_power = self.attack
        self.check_attack_effects()
        self.defender.health -= self.attack_power

    def update_battle_state(self, allies: list, spirits: list, enemies: list):
        self.allies = allies
        self.spirits = spirits
        self.enemies = enemies

    def choose_action(self):
        pass
