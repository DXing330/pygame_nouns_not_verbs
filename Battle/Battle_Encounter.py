import copy
from Battle.Effect_Factory import *
from Battle.Location import *
from Battle.Monster_Factory import Monster_Factory
from Battle.Condition_Checker import *
from Battle.Monster_Drops import *
from Characters.Party import *
from Characters.Monster import *
from Skills.Auras import *
from Utility.Pick import *
from Utility.Draw import *
from Utility.Sort import *
from Skills.Skill import *
from Config.Skill_Dict import *
from Config.Equip_Dict import *
E = Equip_Dict()
P = Passive_Dict()
S = Skill_Dict()


class Damage:
    def __init__(self, damage):
        self.damage = damage

@dataclass
class Monster_Encounter:
    party: Party
    location: Location
    amount: int
    monsters: list[Monster]
    battlers: list[Character]
    auras: list
    battle: bool = True
    boss: bool = False
    draw: Draw = Draw()
    monster_factory: Monster_Factory = Monster_Factory()
    condition_checker: Condition_Checker = Condition_Checker()

    def start_phase(self):
        self.update_auras()
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
        self.draw.draw_turn_order(self.battlers)

    def clear_weather(self):
        # There can only be one weather effect at a time.
        for aura in self.battle_auras:
            if aura.type == "Weather":
                self.battle_auras.remove(aura)

    def update_auras(self):
        self.battle_auras: list[Aura] = []
        for aura in self.auras:
            if aura != "None":
                new_aura = Aura(**P.AURAS.get(aura))
                self.add_aura(new_aura)

    def add_aura(self, aura: Aura):
        # Don't add multiple of the same aura.
        check = None
        for current_aura in self.battle_auras:
            if current_aura.name == aura.name:
                check = current_aura.name
        if check == None:
            if aura.type == "Weather":
                self.clear_weather()
            self.battle_auras.append(aura)

    def generate_monsters(self):
        min_monsters = 0
        if self.boss:
            min_monsters += 1
            boss = self.location.bosses[random.randint(0, len(self.location.bosses) - 1)]
            monster = self.monster_factory.make_monster(boss)
            self.monsters.append(monster)
        if len(self.monsters) <= min_monsters:
            # Plus one here in case self.amount is zero.
            for number in range(0, random.randint(max(self.amount - 1, 1), self.amount + 1)):
                monster_name = self.location.monsters[random.randint(0, len(self.location.monsters) - 1)]
                monster = self.monster_factory.make_monster(monster_name)
                self.monsters.append(monster)
        for monster in self.monsters:
            self.update_monster_for_battle(monster)
        self.monster_list = copy.deepcopy(self.monsters)

    def prepare_for_battle(self):
        self.heroes = copy.deepcopy(self.party.battle_party)
        for hero in self.heroes:
            if hero.weapon != None:
                weapon = Equipment(**E.EQUIPMENT.get(hero.weapon))
                hero.weapon = weapon
            if hero.armor != None:
                armor = Equipment(**E.EQUIPMENT.get(hero.armor))
                hero.armor = armor
        self.spirits = copy.deepcopy(self.party.spirits)

    def update_monster_for_battle(self, monster: Monster):
        monster.update_stats()
        skills = []
        dictionary = CD.MONSTER_STATS.get(monster.name)
        for word in dictionary.get("skills"):
            bskill = Skill(**S.ALL_SKILLS.get(word))
            skills.append(bskill)
        monster.skill_list = skills
        passives = []
        for word in dictionary.get("passives"):
            bpassive = Skill(**S.ALL_SKILLS.get(word))
            passives.append(bpassive)
        monster.passive_skills = passives
        conditionals = []
        for word in dictionary.get("conditionals"):
            bconditional = Conditional_Effect(**P.CONDITIONALS.get(word))
            conditionals.append(bconditional)
        monster.conditional_passives = conditionals
        death_effects = []
        for word in dictionary.get("death_effect"):
            bdeath = Skill(**S.ALL_SKILLS.get(word))
            death_effects.append(bdeath)
        monster.death_skills = death_effects
        preemptives = []
        for word in dictionary.get("preemptives"):
            preemptive = Skill(**S.ALL_SKILLS.get(word))
            preemptives.append(preemptive)
        monster.preemptives = preemptives

    def monster_targeting(self, user: Monster, skill: Skill):
        target_list = []
        for hero in self.heroes:
            if hero == user.target:
                target_list.append(hero)
        if len(target_list) <= 0 and len(self.heroes) > 0:
            choice = random.randint(0, len(self.heroes)-1)
            target_list.append(self.heroes[choice])
        return target_list

    def skill_targeting(self, user, skill : Skill, pick_randomly = True, cost = True):
        self.draw_battle()
        target_list = []
        if user.target != None and skill.targets == "Hero":
            target_list = self.monster_targeting(user, skill)
        elif skill.targets == "Self":
            target_list.append(user)
        elif skill.targets == "Partner":
            for target in self.heroes:
                if target.name == user.partner:
                    target_list.append(target)
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
        if cost:
            self.skill_apply_cost_cooldown_use(user, skill, target_list, pick_randomly)
        elif not cost:
            self.skill_activation(user, skill, target_list, pick_randomly)

    def skill_apply_cost_cooldown_use(self, user, skill: Skill, targets: list, pick_randomly = True):
        cost = skill.cost
        if skill.cooldown <= 0 and user.skill > 0:
            skill.cooldown += skill.cooldown_counter
            if skill.cost == "Target":
                cost = 0
                for target in targets:
                    cost += target.level
            elif skill.cost == "Scale":
                cost = len(targets)
            elif skill.cost == "Self":
                cost = user.level
            user.skill -= cost
            self.skill_activation(user, skill, targets, pick_randomly)
        else:
            print ("Failed")
            print (user.skill)
            print ("COST: "+str(cost))
            print ("CD: "+str(skill.cooldown))
            self.draw_battle()
            self.draw.draw_text(user.name+" failed to "+skill.name)
            pygame.time.delay(500)

    def skill_condition_checker(self, user, skill: Skill, targets: list):
        if skill.condition == "Always":
            activate = Effect_Factory(skill.effect, skill.effect_specifics, round(skill.power * user.level), targets)
            activate.make_effect()
        else:
            condition = Conditional_Effect(skill.name, "Skill", skill.condition, skill.condition_specifics, skill.effect, skill.effect_specifics, skill.power)
            for target in targets:
                fulfill = self.condition_checker.check_target_condition(user, condition, target)
                if fulfill:
                    activation = Effect_Factory(skill.effect, skill.effect_specifics, round(skill.power * user.level), [target])
                    activation.make_effect()

    def skill_activation(self, user, skill: Skill, targets: list, pick_randomly = True):
        if skill.effect == "Summon":
            if skill.power < 0:
                summon = self.monster_factory.make_monster(skill.effect_specifics, max(user.level-1, 1))
                self.update_monster_for_battle(summon)
                self.monsters.append(summon)
            else:
                summon = Summon(skill.effect_specifics, max(user.level//2, skill.power))
                self.update_monster_for_battle(summon)
                self.heroes.append(summon)
        elif skill.effect == "Aura":
            new_aura = Aura(**P.AURAS.get(skill.effect_specifics))
            self.add_aura(new_aura)
        elif skill.effect == "Target":
            for target in targets:
                user.target = target
        elif skill.effect == "Set_Target":
            for target in targets:
                target.target = user
        elif skill.effect == "Command":
            for target in targets:
                self.draw_battle()
                if skill.effect_specifics == "Spirit":
                    self.spirit_turn(target)
                elif skill.effect_specifics == "Hero":
                    self.hero_turn(target)
                elif skill.effect_specifics == "Monster":
                    self.monster_turn(target)
        elif skill.effect == "Skill":
            for word in S.COMPOUND_SKILLS.get(skill.effect_specifics):
                new_skill = Skill(**S.ALL_SKILLS.get(word))
                self.skill_activation(user, new_skill, targets, pick_randomly)
        elif skill.effect == "Attack":
            if skill.effect_specifics == "Basic":
                status = None
            else:
                status = skill.effect_specifics
            for target in targets:
                for number in range(0, skill.power):
                    self.attack_step(user, target, status)
        else:
            # Some skills will only activate a portion of the time, ex. some status effects.
            activation = random.randint(0, 99)
            if activation < skill.chance:
                self.skill_condition_checker(user, skill, targets)

    def hero_attack(self, hero):
        self.draw_battle()
        pick_from = Pick(self.monsters, False)
        target = pick_from.pick()
        self.attack_step(hero, target)

    def hero_skill(self, hero: Character):
        self.draw_battle()
        pick_from = Pick(hero.skill_list, False)
        skill = pick_from.pick_skill()
        self.skill_targeting(hero, skill, False)

    def use_item(self, hero: Character):
        self.draw_battle()
        choices = []
        if self.party.items.health_potions > 0:
            choices.append("Health")
        if self.party.items.energy_potions > 0:
            choices.append("Energy")
        if len(choices) > 0:
            pick_from = Pick(choices, False)
            potion = pick_from.pick()
            self.draw_battle()
            if potion == "Health":
                self.party.items.health_potions -= 1
                hero.health += hero.max_health//3
                self.draw.draw_text(hero.name+" drinks a health potion.")
            elif potion == "Energy":
                self.party.items.energy_potions -= 1
                hero.skill += hero.max_skill//2
                self.draw.draw_text(hero.name+" drinks an energy potion.")
        else:
            self.draw.draw_text(hero.name+" fails to drink.")
        pygame.time.delay(1000)

    def delay_turn(self, character: Character):
        # The player can only delay their turn once per round.
        character.delayed = True
        # After delaying their action they move to the end of the turn order.
        self.battlers.append(character)

    def hero_turn(self, hero: Character):
        # Heroes unique passive will come from whatever accessory they chose to wear?
        # Negative statuses take effect even if the character is stunned.
        if not hero.delayed:
            self.status_step(hero)
        if len(self.monsters) > 0 and hero.turn and hero.health > 0:
            # If someone delays their turn they don't get another round of passives.
            if hero.passives and not hero.delayed:
                self.passive_step(hero, False)
            possible_actions = hero.choose_action()
            pick_from = Pick(possible_actions, False)
            action = pick_from.pick()
            if "Attack" in action:
                self.hero_attack(hero)
            elif "Skill" in action:
                self.hero_skill(hero)
            elif "Delay" in action:
                self.delay_turn(hero)
            elif "Item" in action:
                self.use_item(hero)
        elif len(self.monsters) > 0 and not hero.turn:
            self.draw.draw_text(hero.name+" is stunned.")
            pygame.time.delay(1000)
        self.end_step(hero)

    def spirit_turn(self, spirit: Spirit):
        if spirit.active and len(self.heroes) > 0 and len(self.monsters) > 0:
            self.draw_battle()
            skill, targets = spirit.choose_action(self.heroes)
            # If the spirit has already picked targets then activate the skill.
            if skill != None and len(targets) > 0:
                self.skill_activation(spirit, skill, targets)
                self.draw.draw_text(spirit.name+" uses "+skill.name)
                pygame.time.delay(1000)
            # If the spirit hasn't already picked targets then pick them normally.
            elif skill != None and len(targets) <= 0:
                self.skill_targeting(spirit, skill, True, False)
                self.draw_battle()
                self.draw.draw_text(spirit.name+" uses "+skill.name)
                pygame.time.delay(1000)
            else:
                self.draw.draw_text(spirit.name+" recharges energy.")
                pygame.time.delay(500)

    def monster_turn(self, monster: Monster):
        # Some monsters have a special effect so they're immune to stuns so they take their unique passive step first.
        monster.unique_passives()
        self.status_step(monster)
        if len(self.heroes) > 0 and monster.turn and monster.health > 0:
            self.passive_step(monster)
            if monster.used_skill != None and monster.skills:
                self.skill_targeting(monster, monster.used_skill)
                self.draw_battle()
                self.draw.draw_text(monster.name+" uses "+monster.used_skill.name)
                pygame.time.delay(1000)
            else:
                if monster.target != None:
                    target = monster.target
                else:
                    target = self.heroes[random.randint(0, len(self.heroes) - 1)]
                self.attack_step(monster, target)
        elif len(self.heroes) > 0 and not monster.turn:
            self.draw.draw_text(monster.name+" is stunned.")
            pygame.time.delay(1000)
        self.end_step(monster)

    def check_hit(self, attacker, defender):
        chance = attacker.accuracy - defender.evasion
        if chance < 100:
            miss_chance = random.randint(0, 100)
            if miss_chance >= chance:
                return False
        return True

    def attack_conditionals(self, attacker: Character, defender: Character):
        for conditional in attacker.conditional_passives:
            if conditional.timing == "Attack":
                condition = self.condition_checker.check_target_condition(attacker, conditional, defender)
                if condition:
                    effect = Effect_Factory(conditional.effect, conditional.effect_specifics, round(conditional.power * attacker.level), [attacker])
                    effect.make_effect()
        for conditional in defender.conditional_passives:
            if conditional.timing == "Defend":
                condition = self.condition_checker.check_target_condition(defender, conditional, attacker)
                if condition:
                    effect = Effect_Factory(conditional.effect, conditional.effect_specifics, round(conditional.power * defender.level), [defender])
                    effect.make_effect()

    def attack_step(self, attacker: Character, defender: Character, attack_status = None):
        self.attack_conditionals(attacker, defender)
        self.draw_battle()
        self.damage = Damage(attacker.attack)
        hit = self.check_hit(attacker, defender)
        if hit:
            #print ("Before: "+str(self.damage.damage))
            if attacker.weapon != None:
                attack_effect = Equipment_Effect_Factory(attacker.weapon, self.damage, defender)
                attack_effect.make_effect()
            if defender.armor != None:
                attack_effect = Equipment_Effect_Factory(defender.armor, self.damage, attacker)
                attack_effect.make_effect()
            #print ("After: "+str(self.damage.damage))
            self.damage.damage = self.damage.damage * (attacker.damage_dealt/100)
            self.damage.damage -= defender.defense
            # Temporary health is used before actual health, like blocking with a shield.
            if defender.temp_health > 0:
                defender.temp_health -= max(self.damage.damage, 1)
                # First set the damage to zero, then add it back if they get through all the temporary health.
                self.damage.damage = 0
                if defender.temp_health <= 0:
                    self.damage.damage = - defender.temp_health
            self.damage.damage = self.damage.damage * (defender.damage_taken/100)
            defender.health -= max(round(self.damage.damage), 1)
            if attack_status != None:
                status_effect = Effect_Factory("Add_Status", attack_status, 1, [defender])
                status_effect.make_effect()
                print (defender.statuses)
            self.draw.draw_text(attacker.name+" attacks "+defender.name)
            pygame.time.delay(1000)
        else:
            self.draw.draw_text(attacker.name+" misses "+defender.name)
            pygame.time.delay(1000)

    def start_step(self):
        # Before the rest of the battle, the monsters will use their preemptives.
        for monster in self.monsters:
            for preemptive in monster.preemptives:
                self.skill_targeting(monster, preemptive, True, False)

    def aura_step(self):
        for aura in self.battle_auras:
            targets = []
            if aura.targets == "ALL":
                for hero in self.heroes:
                    targets.append(hero)
                for monster in self.monsters:
                    targets.append(monster)
            elif aura.targets == "Monsters":
                for monster in self.monsters:
                    targets.append(monster)
            elif aura.targets == "Heroes":
                for hero in self.heroes:
                    targets.append(hero)
            aura_effect = Effect_Factory(aura.effect, aura.effect_specifics, aura.power, targets)
            aura_effect.make_effect()
            self.draw_battle()
            self.draw.draw_text(str(aura.aura_effect_text()))
            pygame.time.delay(1000)

    def aura_end_step(self):
        for aura in self.battle_auras:
            if aura.turns > 0:
                aura.turns -= 1
            if aura.turns == 0:
                self.battle_auras.remove(aura)
                self.draw_battle()
                self.draw.draw_text(str(aura.aura_end_text()))
                pygame.time.delay(1000)

    def check_on_target(self, character: Character):
        target = False
        for hero in self.heroes:
            if hero == character.target:
                target = True
        for monster in self.monsters:
            if monster == character.target:
                target = True
        if not target:
            character.target = None

    def passive_step(self, character: Character, prandom = True):
        for skill in character.skill_list:
            if skill.cooldown > 0:
                skill.cooldown -= 1
        for buff in character.buffs:
            passive = Effect_Factory(buff.effect, buff.effect_specifics, round(buff.power * character.level), [character])
            passive.make_effect()
            done = buff.check_turns()
            if done:
                character.buffs.remove(buff)
        for conditional in character.conditional_passives:
            # Check on passive conditionals.
            if conditional.timing == "Passive":
                # First check if the condition is met.
                condition = self.condition_checker.check_passive_condition(character, conditional)
                # If it is them it takes effect.
                if condition:
                    effect = Effect_Factory(conditional.effect, conditional.effect_specifics, round(conditional.power * character.level), [character])
                    effect.make_effect()
        for skill in character.passive_skills:
            self.skill_targeting(character, skill, prandom, False)
        # Temporary health like shields from the previous round will quickly decay.
        if character.temp_health > 0:
            character.temp_health =  character.temp_health//3
        elif character.temp_health < 0:
            character.temp_health = 0
        # Check if the target still exists.
        if character.target != None:
            self.check_on_target(character)

    def status_step(self, character: Character):
        for status in character.statuses:
            passive = Effect_Factory(status.effect, status.effect_specifics, status.power * character.level, [character])
            passive.make_effect()
            done = status.check_turns()
            if done:
                character.statuses.remove(status)

    def end_step(self, character: Character):
        # At the end of their turn, a character gets unstunned and unsilenced.
        character.turn = True
        character.skills = True
        character.passives = True
        # Stats slowly return to normal.
        character.accuracy = (character.accuracy+100)//2
        character.evasion = character.evasion//2
        character.attack = (character.base_attack + character.attack)//2
        character.defense = (character.base_defense + character.defense)//2
        character.damage_dealt = (character.damage_dealt + 100)//2
        character.damage_taken = (character.damage_taken + 100)//2
        # Character's can't just spam healing to increase their health pool.
        character.health = min(character.health, character.max_health)

    def spirit_passives(self, spirit: Spirit):
        # Spirits will use all their passive skills every turn.
        for skill in spirit.passive_skills:
            self.skill_targeting(spirit, skill, True, False)

    def speed_rng(self):
        for battler in self.battlers:
            battler.speed = round(random.gauss(battler.base_speed, 1))

    def reset_delayed_turns(self):
        for battler in self.battlers:
            battler.delayed = False

    def make_turn_order(self):
        self.battlers = []
        for hero in self.heroes:
            self.battlers.append(hero)
        for monster in self.monsters:
            self.battlers.append(monster)
        self.speed_rng()
        sorter = Sort()
        self.battlers = sorter.sort_by_speed(self.battlers)
        self.reset_delayed_turns()

    def cleanup_phase(self):
        pygame.event.clear()
        for hero in self.heroes:
            if hero.health <= 0:
                self.heroes.remove(hero)
        for monster in self.monsters:
            if monster.health <= 0:
                for skill in monster.death_skills:
                    self.skill_targeting(monster, skill, True, False)
                self.monsters.remove(monster)
        if len(self.monsters) <= 0 or len(self.heroes) <= 0:
            self.battle = False
        self.update_draw()

    def battle_phase(self):
        self.draw_battle()
        self.start_step()
        while self.battle:
            self.cleanup_phase()
            self.aura_step()
            for monster in self.monsters:
                monster.choose_action(self.heroes, self.monsters)
            self.draw_battle()
            self.make_turn_order()
            for spirit in self.spirits:
                if len(self.heroes) > 0 and len(self.monsters) > 0 and spirit.active:
                    self.draw_battle()
                    self.spirit_passives(spirit)
                    self.spirit_turn(spirit)
                    self.cleanup_phase()
            for battler in self.battlers:
                if battler.health > 0:
                    self.draw_battle()
                    if isinstance(battler, Hero) and len(self.monsters) > 0:
                        self.hero_turn(battler)
                    elif isinstance(battler, Summon) and len(self.monsters) > 0:
                        self.hero_turn(battler)
                    # Need "and len(self.monsters) > 0" or else summons will act like monsters in case that all the monsters are dead.
                    elif isinstance(battler, Monster) and len(self.heroes) > 0 and len(self.monsters) > 0:
                        self.monster_turn(battler)
                self.cleanup_phase()
            self.aura_end_step()
        win = self.end_phase()
        if win:
            drops = Monster_Drops(self.party, self.monster_list)
            drops.monster_loot()
            self.quest_update()

    def end_phase(self):
        # In case there is another battle, the heroes remain injured until they return.
        for hero in self.party.battle_party:
            check = None
            for battler in self.heroes:
                if hero.name == battler.name:
                    check = battler.name
                    hero.health = min(battler.health, hero.max_health)
                    hero.skill = min(battler.skill, hero.max_skill)
            if check == None:
                hero.health = 0
                hero.skill = 0
            if hero.health <= 0:
                self.party.battle_party.remove(hero)
        # If the heroes win then they get rewards.
        if len(self.heroes) > 0:
            reward_exp = 0
            for monster in self.monster_list:
                reward_exp += random.randint(1, monster.level)
            for spirit in self.party.spirits:
                spirit.exp += reward_exp
                spirit.level_up()
            for hero in self.party.heroes:
                battled = False
                for battler in self.party.battle_party:
                    if battler.name == hero.name:
                        battled = True
                if battled:
                    hero.exp += reward_exp
                    hero.level_up()
            win = True
            self.draw_battle()
            self.draw.draw_text("The heroes win.")
            pygame.time.delay(750)
        elif len(self.heroes) <= 0:
            win = False
            for hero in self.party.heroes:
                hero.exp -= hero.level
                self.party.items.coins -= min(self.party.items.coins, hero.level)
        return win
    
    def quest_update(self):
        for quest in self.party.quests:
            if (((self.location.name == quest.location) or (quest.location == "Any")) and not quest.completed):
                # For kill quests, keep track of how many monster's are killed.
                if quest.requirement == "Kill":
                    for monster in self.monster_list:
                        if monster.name == quest.specifics:
                            quest.specifics_amount -= 1