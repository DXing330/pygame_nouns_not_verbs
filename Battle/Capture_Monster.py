from Characters.Party import *


# Function that will determine whether a monster is captured or not.
# If captured, then the monster will be adjusted to be able to be on the heroes' side.
# Need some way to determine cost of summoning, also want some kind of loyalty mechanic.
# Might handle loyalty in another section, may need a class just for summoning.
# If loyalty is too low, the monster may revolt and join the enemy side when summoned.
class Capture_Monster:
    def __init__(self, party, catcher, monster):
        self.party: Party = party
        self.catcher: Hero = catcher
        self.monster: Monster = monster

    def determine_capture(self):
        captured = False
        self.catch_rate = self.monster.catch_rate
        # If you're a higher level, then it's easier to catch the monster.
        self.catch_rate += max(0, (self.catcher.level - self.monster.level))
        if self.catch_rate > 0:
            # If the monster is lower health relatively speaking, then it's easier to catch the monster.
            self.catch_rate = round(self.catch_rate * min(10, max(1, (self.catcher.health/self.monster.health))))
            # If the monster has less skill, relatively speaking, then it's easier to catch.
            self.catch_rate = round(self.catch_rate * min(10, max(1, (self.catcher.max_skill/self.monster.max_skill))))
        catch = random.randint(1, 100)
        if catch <= self.catch_rate:
            captured = True
        if captured:
            absorbed = self.check_monster()
            if absorbed:
                self.catch_monster()
        return captured

    # Adjust the monster's stats to make them base level before adding them.
    def adjust_stats(self):
        self.monster.buffs = []
        self.monster.statuses = []
        self.monster.update_base_stats()

    # Adjust the monster's skill to be able to work on the heroes side.
    def adjust_skills(self, skill_list):
        for skill in skill_list:
            if "Hero" in skill.targets:
                skill.targets = skill.targets.replace("Hero", "Monster")
            elif "Monster" in skill.targets:
                skill.targets = skill.targets.replace("Monster", "Hero")
            if "Summon" in skill.effect and "Monster" in skill.effect:
                skill.effect = skill.effect.replace("Monster", "")
                # Summoned monsters can't call for other monsters to help them.
                if "Call" in skill.name:
                    skill_list.remove(skill)

    # If you catch multiple of the same monster, keep the strongest.
    def check_monster(self):
        check = None
        level = self.monster.level
        for monster in self.party.summonables:
            if monster.name == self.monster.name and monster.level > level:
                check = monster
            if monster.name == self.monster.name and monster.level < level:
                self.party.summonables.remove(monster)
        if not check:
            return True
        return False

    def catch_monster(self):
        self.adjust_skills(self.monster.skill_list)
        self.adjust_skills(self.monster.passive_skills)
        self.adjust_skills(self.monster.death_skills)
        self.adjust_stats()
        new_summonable = Hero(self.monster.name,self.monster.skill_list,self.monster.passive_skills,self.monster.conditional_passives,[],[],10,self.monster.level,self.monster.max_health,self.monster.health,self.monster.base_attack,self.monster.base_defense,self.monster.base_speed,self.monster.attack,self.monster.defense,self.monster.speed,100,0,100,100,self.monster.max_skill,self.monster.skill,True,True,True,False,0,None,None,0,0,0)
        self.party.summonables.append(new_summonable)