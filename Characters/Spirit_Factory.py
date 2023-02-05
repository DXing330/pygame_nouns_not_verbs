from Characters.Spirits import *


class Spirit_Factory:

    def make_spirit(self, spirit: Spirit):
        if "Angel" in spirit.name:
            new_spirit = Angel(spirit.name, spirit.partner, spirit.level, spirit.skill_list, spirit.passive_skills, spirit.exp, spirit.skill, spirit.max_level)
        if "Fairy" in spirit.name:
            new_spirit = Fairy(spirit.name, spirit.partner, spirit.level, spirit.skill_list, spirit.passive_skills, spirit.exp, spirit.skill, spirit.max_level)
        return new_spirit