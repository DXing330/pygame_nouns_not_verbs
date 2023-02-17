from dataclasses import dataclass
from Character import Character
from Config.Constants import *
from Config.NPC_Dict import *
C = Constants()
CD = NPC_Dict()


@dataclass
class Battle_NPC(Character):

    def update_stats(self):
        dict = CD.NPC_STATS.get(self.name)
        self.level = dict.get("level")
        self.max_health = dict.get("health") * self.level
        self.base_attack = dict.get("attack") * self.level
        self.base_defense = dict.get("defense") * self.level
        self.base_speed = dict.get("speed")
        self.max_skill = dict.get("skill") * self.level
        self.accuracy = 100
        self.evasion = 0
        self.damage_dealt = 100
        self.damage_taken = 100
        self.health = self.max_health
        self.skill = self.max_skill
        self.attack = self.base_attack
        self.defense = self.base_defense
        self.speed = self.base_speed
        self.npc_skills()

    def npc_skills(self):
        dict = CD.NPC_SKILLS.get(self.name)
        self.skill_list = dict.get("Skills")
        self.passive_skills = dict.get("Passives")
        self.conditional_passives = dict.get("Conditionals")

    def stats_text(self):
        text = str(self.name+"~ HP: "+str(round(self.health+self.temp_health))+" ATK: "+str(round(self.attack))+" DEF: "+str(round(self.defense))+" SKL: "+str(round(self.skill)))
        return text

    def choose_action(self):
        possiblities = []
        if self.turn:
            possiblities.append(self.name+" Attack")
        if self.skills and len(self.battle_skills) > 0:
            possiblities.append(self.name+" Skill")
        if self.skills and not self.delayed:
            possiblities.append("Delay Action")
        possiblities.append("Use Item")
        return possiblities