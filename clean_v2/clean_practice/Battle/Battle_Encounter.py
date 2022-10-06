import copy
from Battle.Effect_Factory import *
from Battle.Location import *
from Characters.Party import *
from Characters.Monster import *
from Utility.Pick import *
from Utility.Draw import *
from Skills.Skill import *
from Config.Skill_Dict import *
S = Skill_Dict()


@dataclass
class Monster_Encounter:
    party: Party
    location: Location
    amount: int
    monsters: list
    battle: bool = True
    draw: Draw = Draw()

    def start_phase(self):
        self.prepare_for_battle()
        self.generate_monsters()
        self.update_draw()
        self.battle_phase()

    def update_draw(self):
        self.draw.update_heroes(self.heroes)
        self.draw.update_monsters(self.monsters)
        self.draw.update_spirits(self.spirits)

    def draw_battle(self):
        self.draw.draw_background(self.location.image)
        self.draw.draw_battle_state()
        self.draw.draw_battle_stats()

    def generate_monsters(self):
        if len(self.monsters) <= 0:
            # Plus one here in case self.amount is zero.
            for number in range(0, self.amount + 1):
                monster_name = self.location.monsters[random.randint(0, len(self.location.monsters) - 1)]
                monster = Monster(monster_name)
                self.monsters.append(monster)
        for monster in self.monsters:
            self.update_monster_for_battle(monster)

    def prepare_for_battle(self):
        self.heroes = copy.deepcopy(self.party.battle_party)
        for hero in self.heroes:
            battle_skills = []
            for skill in hero.skill_list:
                bskill = Skill(**S.ALL_SKILLS.get(skill))
                print (bskill.__dict__)
                battle_skills.append(bskill)
            hero.update_skills(battle_skills)
            battle_passives = []
            for skill in hero.passive_skills:
                bpassive = Skill(**S.ALL_SKILLS.get(skill))
                battle_passives.append(bpassive)
            hero.update_passive_skills(battle_passives)
        self.spirits = copy.deepcopy(self.party.spirits)
        for spirit in self.spirits:
            print (spirit.__dict__)
            battle_skills = []
            for skill in spirit.skill_list:
                bskill = Skill(**S.ALL_SKILLS.get(skill))
                print (bskill.__dict__)
                battle_skills.append(bskill)
                spirit.update_skills(battle_skills)
                print (spirit.battle_skills)

    def update_monster_for_battle(self, monster: Monster):
        monster.update_stats()
        battle_skills = []
        dictionary = CD.MONSTER_STATS.get(monster.name)
        for word in dictionary.get("skills"):
            bskill = Skill(**S.ALL_SKILLS.get(word))
            battle_skills.append(bskill)
        monster.update_skills(battle_skills)
        battle_passives = []
        for word in dictionary.get("passives"):
            bpassive = Skill(**S.ALL_SKILLS.get(word))
            battle_passives.append(bpassive)
        monster.update_passive_skills(battle_passives)
        death_effects = []
        for word in dictionary.get("death_effect"):
            bdeath = Skill(**S.ALL_SKILLS.get(word))
            death_effects.append(bdeath)
        monster.update_death_skills(death_effects)

    def skill_apply_cost_cooldown_use(self, user, skill: Skill, pick_randomly = True):
        if skill.cooldown <= 0:
            skill.cooldown += skill.cooldown_counter
            user.skill -= skill.cost
            if user.skill >= 0:
                self.skill_activation(user, skill, pick_randomly)

    def skill_targeting(self, user, skill : Skill, pick_randomly = True):
        target_list = []
        if skill.targets == "Self":
            target_list.append(user)
        elif skill.targets == "Hero":
            pick_from = Pick(self.heroes, pick_randomly)
            target = pick_from.pick()
            target_list.append(target)
        elif skill.targets == "All_Hero":
            target_list = self.heroes
        elif skill.targets == "Monster":
            pick_from = Pick(self.monsters, pick_randomly)
            target = pick_from.pick()
            target_list.append(target)
        elif skill.targets == "All_Monster":
            target_list = self.monsters
        elif skill.targets == "Spirit":
            pick_from = Pick(self.spirits, pick_randomly)
            target = pick_from.pick()
            target_list.append(target)
        elif skill.targets == "All_Spirit":
            target_list = self.spirits
        return target_list

    def skill_activation(self, user, skill: Skill, pick_randomly = True):
        targets = self.skill_targeting(user, skill, pick_randomly)
        if skill.effect == "Summon":
            if skill.power < 0:
                summon = Monster(skill.effect_specifics, user.level - 1)
                self.update_monster_for_battle(summon)
                self.monsters.append(summon)
            else:
                summon = Summon(skill.effect_specifics, max(user.level - 1, skill.power))
                self.update_monster_for_battle(summon)
                self.heroes.append(summon)
        elif skill.effect == "Command":
            for target in targets:
                if skill.effect_specifics == "Spirit":
                    self.spirit_turn(target)
                elif skill.effect_specifics == "Hero":
                    self.hero_turn(target)
                elif skill.effect_specifics == "Monster":
                    self.monster_turn(target)
        elif skill.effect == "Skill":
            for word in S.COMPOUND_SKILLS.get(skill.effect_specifics):
                new_skill = Skill(**S.ALL_SKILLS.get(word))
                self.skill_activation(user, new_skill, pick_randomly)
        elif skill.effect == "Attack":
            for target in targets:
                for number in range(0, skill.power):
                    self.attack_step(user, target)
        else:
            activate = Effect_Factory(skill.effect, skill.effect_specifics, skill.power * user.level, targets)
            activate.make_effect()

    def hero_attack(self, hero):
        pick_from = Pick(self.monsters, False)
        target = pick_from.pick()
        self.attack_step(hero, target)

    def hero_skill(self, hero: Character):
        pick_from = Pick(hero.battle_skills, False)
        skill = pick_from.pick()
        self.skill_apply_cost_cooldown_use(hero, skill, False)

    def hero_turn(self, hero: Character):
        if len(self.monsters) > 0 and hero.turn:
            action = hero.choose_action()
            if action == "Attack":
                self.hero_attack(hero)
            elif action == "Skill" and hero.skills:
                self.hero_skill(hero)

    def spirit_turn(self, spirit: Spirit):
        if len(self.heroes) > 0 and len(self.monsters) > 0:
            skill = spirit.choose_action()
            self.skill_activation(spirit, skill)

    def monster_turn(self, monster: Monster):
        if len(self.heroes) > 0 and monster.turn:
            skill = monster.choose_action()
            if skill != None:
                self.skill_apply_cost_cooldown_use(monster, skill)
            else:
                target = self.heroes[random.randint(0, len(self.heroes) - 1)]
                self.attack_step(monster, target)

    def attack_step(self, attacker, defender):
        self.damage = attacker.attack
        if attacker.weapon != None:
            attack_effect = Equipment_Effect_Factory(attacker.weapon, self.damage, defender)
            attack_effect.make_effect()
        if defender.armor != None:
            attack_effect = Equipment_Effect_Factory(defender.armor, self.damage, attacker)
            attack_effect.make_effect()
        self.damage -= defender.defense
        defender.health -= min(self.damage, 1)

    def passive_step(self, character: Character):
        character.turn = True
        character.skills = True
        for skill in character.battle_skills:
            if skill.cooldown > 0:
                skill.cooldown -= 1
        for buff in character.buffs:
            passive = Effect_Factory(buff.effect, buff.effect_specifics, buff.power * character.level, [character])
            passive.make_effect()
            done = buff.check_turns()
            if done:
                character.buffs.remove(buff)
        for status in character.statuses:
            passive = Effect_Factory(status.effect, status.effect_specifics, status.power * character.level, [character])
            passive.make_effect()
            done = status.check_turns()
            if done:
                character.statuses.remove(status)
        for skill in character.battle_passives:
            self.skill_activation(character, skill)

    def standby_phase(self):
        for hero in self.heroes:
            self.passive_step(hero)
        for monster in self.monsters:
            self.passive_step(monster)

    def cleanup_phase(self):
        for hero in self.heroes:
            if hero.health <= 0:
                self.heroes.remove(hero)
        for monster in self.monsters:
            if monster.health <= 0:
                for skill in monster.battle_death_skills:
                    self.skill_activation(monster, skill)
                self.monsters.remove(monster)
        if len(self.monsters) <= 0 or len(self.heroes) <= 0:
            self.battle = False
        self.update_draw()

    def battle_phase(self):
        while self.battle:
            self.standby_phase()
            self.cleanup_phase()
            self.draw_battle_state()
            for hero in self.heroes:
                self.hero_turn(hero)
                self.cleanup_phase()
            for spirit in self.spirits:
                self.spirit_turn(spirit)
                self.cleanup_phase()
            for monster in self.monsters:
                self.monster_turn(monster)
                self.cleanup_phase()
        self.end_phase()

    def end_phase(self):
        if len(self.heroes) > 0:
            self.party.items.coins += 1
            for spirit in self.party.spirits:
                spirit.exp += 1
                spirit.level_up()
            for hero in self.party.heroes:
                hero.exp += 1
                hero.level_up()