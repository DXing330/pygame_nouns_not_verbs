import json
import copy
from Hero import *
from Spirits import *
from Equipment import *
from Spirit_Factory import *
from Config.Constants import *
from Config.Equip_Dict import *
from Utility.Pick import Pick
C = Constants()
E = Equip_Dict()

@dataclass
class Quest:
    name: str = None
    # Who gives the quest, where to return to complete the quest.
    giver: str = None
    # Where to complete the quest.
    location: str = None
    # What to do.
    requirement: str = None
    specifics: str = None
    specifics_amount: int = 0
    # How long you have to do it.
    start_day: int = 0
    time_limit: int = 0
    # Status of the quest.
    completed: bool = False
    failed: bool = False
    # Rewards.
    reward_type: str = None
    reward_amount: int = 0

    def quest_info(self):
        return ("Location: "+self.location+", Task: "+self.name+", Amount: "+str(self.specifics_amount)+", Time Limit: "+str(self.time_limit)+", Reward: "+str(self.reward_amount)+" "+self.reward_type)


@dataclass
class Item_Bag:
    coins: int = 0
    health_potions: int = 0
    energy_potions: int = 0
    mana_crystals: int = 0
    sharp_material: int = 0
    hard_material: int = 0
    poison_extract: int = 0
    poison_essense: int = 0
    monster_extract: int = 0
    monster_essence: int = 0


@dataclass
class Records:
    rank: int = 1
    rank_exp: int = 0
    days: int = 0
    main_story_progress: int = -1
    guild_progress: int = -1
    guild_facilities: list = None
    reputation: int = 0
    infamy: int = 0
    

@dataclass
class Party:
    heroes: list[Hero] = None
    spirits: list[Spirit] = None
    equipment: list[str] = None
    items: Item_Bag = Item_Bag(10, 1, 1)
    journal: Records = Records()
    quests: list[Quest] = None
    locations: list[str] = None
    # Pick a battle party before every adventure, or use the same one.
    battle_party: list[Hero] = None

    def check_quest_completion(self):
        for quest in self.quests:
            # If the heroes take too long then they fail.
            if self.journal.days > quest.start_day + quest.time_limit:
                quest.failed = True
            if quest.specifics_amount <= 0 and not quest.failed:
                quest.completed = True

    def add_hero(self, hero: Hero):
        hero.update_stats()
        hero.update_skill_list()
        self.heroes.append(hero)

    def add_spirit(self, spirit):
        self.spirits.append(spirit)

    def add_equipment(self, equip):
        self.equipment.append(equip)

    def remove_heroes_weapon(self, hero: Hero):
        if hero.weapon != None:
            self.add_equipment(hero.weapon)
            hero.weapon = None

    def remove_heroes_armor(self, hero: Hero):
        if hero.armor != None:
            self.add_equipment(hero.armor)
            hero.armor = None

    def equip_to_hero(self, hero: Hero, equip):
        real_equip = Equipment(**E.EQUIPMENT.get(equip))
        if real_equip.type == "Armor":
            hero.armor = equip
        elif real_equip.type == "Weapon":
            hero.weapon = equip

    def add_location(self, location_name):
        # Avoid duplicate locations.
        check = None
        for location in self.locations:
            if location == location_name:
                check = location_name
        if check == None:
            self.locations.append(location_name)

    def party_update(self):
        self.party_update_stats()
        self.party_update_skills()

    def party_update_skills(self):
        for hero in self.heroes:
            hero.update_skill_list()
        for spirit in self.spirits:
            spirit.update_skill_list()
            spirit.update_passive_list()
    
    def party_update_stats(self):
        for hero in self.heroes:
            hero.update_stats()

    def pick_battle_party(self):
        if len(self.heroes) <= C.PARTY_LIMIT:
            self.battle_party = copy.deepcopy(self.heroes)
        else:
            possible_picks = copy.copy(self.heroes)
            self.battle_party = []
            pick_from = Pick(possible_picks, False)
            while len(self.battle_party) < C.PARTY_LIMIT:
                hero = pick_from.pick()
                self.battle_party.append(hero)
                possible_picks.remove(hero)

    def write_object(self, object, filename):
        jsonP = json.dumps(object.__dict__)
        outfile = open(filename, "w")
        outfile.write(jsonP)
        outfile.flush
        outfile.close

    def write_object_list(self, list, filename):
        jsonP = json.dumps([object.__dict__ for object in list])
        outfile = open(filename, "w")
        outfile.write(jsonP)
        outfile.flush
        outfile.close

    def write_str_list(self, list, filename):
        jsonP = json.dumps([thing for thing in list])
        outfile = open(filename, "w")
        outfile.write(jsonP)
        outfile.flush
        outfile.close

    def save(self):
        self.write_object_list(self.heroes, "_heroes")
        self.write_object_list(self.spirits, "_spirits")
        self.write_str_list(self.equipment, "_equipment")
        self.write_str_list(self.locations, "_locations")
        self.write_object_list(self.quests, "_quests")
        self.write_object(self.items, "_items")
        self.write_object(self.journal, "_records")

    def read_hero_objects(self, filename):
        load_heroes_list = []
        jsonFile = open(filename, "r")
        heroes_list = json.load(jsonFile)
        for character in heroes_list:
            hero = Hero(**character)
            load_heroes_list.append(hero)
        return load_heroes_list

    def read_ally_objects(self, filename):
        factory = Spirit_Factory()
        load_allies_list = []
        jsonFile = open(filename, "r")
        allies_list = json.load(jsonFile)
        for summon in allies_list:
            ally = Spirit(**summon)
            new_ally = factory.make_spirit(ally)
            load_allies_list.append(new_ally)
        return load_allies_list

    def read_quest_objects(self, filename):
        load_list = []
        jsonFile = open(filename, "r")
        list = json.load(jsonFile)
        for thing in list:
            quest = Quest(**thing)
            load_list.append(quest)
        return load_list

    def read_str_list(self, filename):
        load_list = []
        jsonFile = open(filename, "r")
        list = json.load(jsonFile)
        for thing in list:
            load_list.append(thing)
        return load_list

    def new_party(self):
        starter_hero = Hero("Summoner", [], [], [], [], [])
        starter_hero.update_stats()
        starter_hero.update_skill_list()
        self.add_hero(starter_hero)
        starter_spirit = Spirit("Angel", "Summoner", 1, [], [])
        starter_spirit.update_skill_list()
        self.add_spirit(starter_spirit)
        self.quests = []

    def load(self):
        heroes_list = self.read_hero_objects("_heroes")
        self.heroes = heroes_list
        ally_list = self.read_ally_objects("_spirits")
        self.spirits = ally_list
        equipment_list = self.read_str_list("_equipment")
        self.equipment = equipment_list
        self.quests = self.read_quest_objects("_quests")
        self.locations = self.read_str_list("_locations")
        jsonFile = open("_items", "r")
        item_bag = json.load(jsonFile)
        self.items = Item_Bag(**item_bag)
        jsonFile = open("_records", "r")
        records = json.load(jsonFile)
        self.journal = Records(**records)