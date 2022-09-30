from Use_Skill import *
from Characters.Hero import *
from Characters.Monster import *
from Characters.Spirits import *
from Characters.Summon import *
from Utility.Pick import *

@dataclass
class Monster_Encounter:
    party: any
    location: str
    monsters: list

    def generate_monsters(self):
        if len(self.monsters) <= 0:
            pass

    def prepare_for_battle(self):
        self.heroes = self.party.battle_party
        self.spirits = self.party.spirits

@dataclass
class Battle:
    heroes: list
    spirits: list
    monsters: list

    def skill_targetting(self, user, skill, pick_randomly = True):
        target_list = []
        if skill.target == "Self":
            target_list.append(user)
        elif skill.target == "Hero":
            pick_from = Pick(self.heroes, pick_randomly)
            target = pick_from.pick()
            target_list.append(target)
        elif skill.target == "All_Hero":
            target_list = self.heroes
        elif skill.target == "Monster":
            pick_from = Pick(self.monsters, pick_randomly)
            target = pick_from.pick()
            target_list.append(target)
        elif skill.target == "All_Monster":
            target_list = self.monsters
        elif skill.target == "Spirit":
            pick_from = Pick(self.spirits, pick_randomly)
            target = pick_from.pick()
            target_list.append(target)
        elif skill.target == "All_Spirit":
            target_list = self.spirits
        return target_list

    def skill_activation(self, user, skill, pick_randomly = True):
        if skill.effect == "Summon" and user.skill > skill.cost:
            user.skill -= skill.cost
            if skill.power < 0:
                summon = Monster(skill.effect_specifics)
                summon.update_for_battle()
                self.monsters.append(summon)
            else:
                summon = Summon(skill.effect_specifics)
                summon.update_for_battle()
                self.heroes.append(summon)
        else:
            targets = self.skill_targetting(user, skill)
            activate = Use_Skill(user, skill, targets)
            activate.use()

    def hero_turn(self, hero):
        pass

    def spirit_turn(self, spirit):
        skill = spirit.choose_action()
        self.skill_activation(spirit, skill)

    def monster_turn(self, monster):
        pass

    def passive_step(self, character):
        pass

    def standby_phase(self):
        pass

    def battle_phase(self):
        for hero in self.heroes:
            self.hero_turn(hero)
        for spirit in self.spirits:
            self.spirit_turn(spirit)
        for monster in self.monsters:
            self.monster_turn(monster)

    def end_phase(self):
        pass