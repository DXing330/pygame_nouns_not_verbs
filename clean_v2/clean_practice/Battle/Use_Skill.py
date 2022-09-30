from Skill_Effect_Factory import *
from Utility.Pick import *

@dataclass
class Use_Skill:
    user: any
    skill: any
    targets: list

    def apply_cooldown(self):
        self.skill.cooldown += self.skill.cooldown_counter

    def apply_cost(self):
        self.user.skill -= self.skill.cost

    def apply_effect(self):
        factory = Effect_Factory(self.skill.effect, self.skill.effect_specifics, self.skill.power * self.user.level, self.targets)
        factory.make_effect()

    def use(self):
        self.apply_cost()
        if self.user.skill >= 0:
            self.apply_cooldown()
            self.apply_effect()

@dataclass
class Skill_Targetting:
    user: any
    skill: any
    allies: list
    spirits: list
    enemies: list
    pick_randomly: bool = True

    def pick_targets(self):
        self.target = self.skill.target
        self.target_list = []
        if self.target == "Self":
            self.target_list.append(self.user)
        elif self.target == "Ally":
            pick_from = Pick(self.allies, self.pick_randomly)
            target = pick_from.pick()
            self.target_list.append(target)
        elif self.target == "Spirit":
            pick_from = Pick(self.spirits, self.pick_randomly)
            target = pick_from.pick()
            self.target_list.append(target)
        elif self.target == "Enemy":
            pick_from = Pick(self.enemies, self.pick_randomly)
            target = pick_from.pick()
            self.target_list.append(target)
        elif self.target == "All_Ally":
            self.target_list = self.allies
        elif self.target == "All_Enemy":
            self.target_list = self.enemies
        elif self.target == "All_Spirit":
            self.target_list = self.spirits

    def use_skill(self):
        self.pick_targets()
        skill = Use_Skill(self.user, self.skill, self.target_list)
        skill.use()