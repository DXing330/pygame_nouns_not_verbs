import pygame
pygame.init()
clock = pygame.time.Clock()
from Config.Dictionaries.Hero_Dict import Hero_Dict
H = Hero_Dict()
from Config.Dictionaries.Skill_Dict import Skill_Dict
S = Skill_Dict()
from Character import *
from General_Functions.Pick import *

@dataclass
class Hero(Character):
    exp: int = 0

    def update_stats(self):
        self.dictionary = H.STATS.get(self.name)
        self.max_health = self.level * self.dictionary.get("Health")
        self.attack = self.level * self.dictionary.get("Attack")
        self.defense = self.level * self.dictionary.get("Defense")
        self.max_skill = self.level * self.dictionary.get("Skill")
        self.max_mana = self.level * self.dictionary.get("Mana")
        self.skill = self.max_skill
        self.health = self.max_health
        self.mana = self.max_mana
        self.skill_list = []
        self.spell_list = []
        self.buffs = []
        self.statuses = []
        self.turn = True
        self.skills = True
        self.spells = True
        self.weapon = None
        self.armor = None
        self.accessory = None

    def update_skills(self):
        self.dictionary = H.SKILLS.get(self.name)
        for number in range(0, self.level):
            word = self.dictionary.get(number)
            if word != None:
                skill = Skill(**S.ALL_SKILLS.get(word))
                self.skill_list.append(skill)

    def update_battle_state(self, allies: list, spirits: list, enemies: list):
        self.allies = allies
        self.spirits = spirits
        self.enemies = enemies

    def use_skill(self):
        pick_from = Pick(self.skill_list, False)
        used_skill : Skill = pick_from.pick()
        if used_skill.effect == "Summon":
            self.summon(used_skill)
        else:
            used_skill.use(self, self.allies, self.spirits, self.enemies)

    def summon(self, name: str):
        summon = Hero(name)
        summon.update_for_battle()
        self.allies.append(summon)

    def summon_skill(self, skill: Skill):
        self.skill -= skill.cost
        if self.skill >= 0 and skill.cooldown <= 0:
            skill.apply_cooldown()
            self.summon(skill.effect_specifics)

    def choose_action(self):
        while len(self.enemies) > 0 and self.turn:
            pygame.event.clear()
            clock.tick = (10)
            choice = pygame.key.get_pressed
            if choice[pygame.K_a]:
                self.turn = False
                pick_from = Pick(self.enemies, False)
                self.target = pick_from.pick()
                self.basic_attack(self.target)
                break
            if choice[pygame.K_s] and self.skills and len(self.skill_list) > 0 and self.skill > 0:
                self.turn = False
                self.use_skill()
                break
            
                