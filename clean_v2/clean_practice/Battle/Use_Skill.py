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
        self.apply_effect()