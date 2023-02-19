# Function that will determine whether a monster is captured or not.
# If captured, then the monster will be adjusted to be able to be on the heroes' side.
# Need some way to determine cost of summoning, also want some kind of loyalty mechanic.
# Might handle loyalty in another section, may need a class just for summoning.
# If loyalty is too low, the monster may revolt and join the enemy side when summoned.

class Capture_Monster:
    def __init__(self, party, catcher, monster):
        self.party = party
        self.catcher = catcher
        self.monster = monster

    # Capturing will depend on level difference, monster health, catcher skill, etc.
    def determine_capture(self):
        pass

    # Adjust the monster's stats to make them base level before adding them.
    def adjust_stats(self):
        self.monster.buffs = []
        self.monster.statuses = []
        # Maybe need the dictionary to update them to base stats, incase of bleeding or other statuses lowering their base stats.

    # Adjust the monster's skill to be able to work on the heroes side.
    def adjust_skills(self, skill_list):
        for skill in skill_list:
            if "Hero" in skill.target:
                skill.target = skill.target.replace("Hero", "Monster")
            elif "Monster" in skill.target:
                skill.target = skill.target.replace("Monster", "Hero")
            if skill.effect == "Summon":
                skill.power = 1

    # If you catch multiple of the same monster, keep the strongest.
    def catch_monster(self):
        check = None
        level = self.monster.level
        for monster in self.party.summonables:
            if monster.name == self.monster.name and monster.level > level:
                check = monster
        if not check:
            return True
        return False

    def absorb_monster(self):
        self.adjust_skills(self.monster.skill_list)
        self.adjust_skills(self.monster.passive_skills)
        self.adjust_skills(self.monster.conditional_passives)
        # The summoned monster won't be able to use preemptives so it doesn't matter if you adjust them.
        self.adjust_skills(self.monster.preemptives)
        self.adjust_stats()
        self.party.summonables.append(self.monster)
