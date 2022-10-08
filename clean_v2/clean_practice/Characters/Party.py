import json
import copy
from unicodedata import name
from Hero import *
from Spirits import *
from Equipment import *
from Config.Constants import *
from Utility.Pick import Pick
C = Constants()


@dataclass
class Item_Bag:
    coins: int = 0
    health_potions: int = 0
    energy_potions: int = 0
    mana_crystals: int = 0


@dataclass
class Records:
    rank: int = 1
    rank_exp: int = 0
    main_story_progress: int = 0
    

@dataclass
class Party:
    heroes: list[Hero] = None
    spirits: list[Spirit] = None
    equipment: list[Equipment] = None
    items: Item_Bag = Item_Bag(10, 1, 1)
    records: Records = Records()
    # Pick a battle party before every adventure, or use the same one.
    battle_party: list[Hero] = None

    def add_hero(self, hero):
        self.heroes.append(hero)

    def add_spirit(self, spirit):
        self.spirits.append(spirit)

    def add_equipment(self, equip: Equipment):
        # Avoid duplicate equipment.
        check = None
        for equipment in self.equipment:
            if equip.name == equipment.name:
                check = equip.name
                equipment.power += random.randint(0, 1)
        if check == None:
            self.equipment.append(equip)

    def party_update_skills(self):
        for hero in self.heroes:
            hero.update_skill_list()
        for spirit in self.spirits:
            spirit.update_skill_list()

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

    def save(self):
        self.write_object_list(self.heroes, "_heroes")
        self.write_object_list(self.spirits, "_spirits")
        self.write_object_list(self.equipment, "_equipment")
        self.write_object(self.items, "_items")
        self.write_object(self.records, "_records")

    def read_hero_objects(self, filename):
        load_heroes_list = []
        jsonFile = open(filename, "r")
        heroes_list = json.load(jsonFile)
        for character in heroes_list:
            hero = Hero(**character)
            load_heroes_list.append(hero)
        return load_heroes_list

    def read_ally_objects(self, filename):
        load_allies_list = []
        jsonFile = open(filename, "r")
        allies_list = json.load(jsonFile)
        for summon in allies_list:
            ally = Spirit(**summon)
            load_allies_list.append(ally)
        return load_allies_list

    def read_equipment_objects(self, filename):
        load_equip_list = []
        jsonFile = open(filename, "r")
        equip_list = json.load(jsonFile)
        for equip in equip_list:
            equipment = Equipment(**equip)
            load_equip_list.append(equipment)
        return load_equip_list

    def new_party(self):
        starter_hero = Hero("Summoner", 1, 0, 0, 0, 0, 0, 0, [], [], [], [])
        starter_hero.update_stats()
        starter_hero.update_skill_list()
        self.add_hero(starter_hero)
        starter_spirit = Spirit("Angel", 1, [])
        starter_spirit.update_skill_list()
        self.add_spirit(starter_spirit)

    def load(self):
        try:
            heroes_list = self.read_hero_objects("_heroes")
            self.heroes = heroes_list
            ally_list = self.read_ally_objects("_spirits")
            self.spirits = ally_list
            equipment_list = self.read_equipment_objects("_equipment")
            self.equipment = equipment_list
            jsonFile = open("_items", "r")
            item_bag = json.load(jsonFile)
            self.items = Item_Bag(**item_bag)
            jsonFile = open("_records", "r")
            records = json.load(jsonFile)
            self.records = Records(**records)
        except:
            self.new_party()