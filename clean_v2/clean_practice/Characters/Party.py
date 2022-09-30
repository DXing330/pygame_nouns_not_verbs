import json
import copy
from Hero import *
from Spirits import *
from Equipment import *
from Config.Constants import *
C = Constants()


@dataclass
class Item_Bag:
    coins: int = 0
    health_potions: int = 0
    energy_potions: int = 0
    mana_crystals: int = 0


@dataclass
class Party:
    heroes: list[Hero] = None
    spirits: list[Spirit] = None
    equipment: list[Equipment] = None
    items: Item_Bag = None
    # Pick a battle party before every adventure, or use the same one.
    battle_party: list[Hero] = None

    def add_hero(self, hero):
        self.heroes.append(hero)

    def add_spirit(self, spirit):
        self.spirits.append(spirit)

    def add_equipment(self, equip):
        self.equipment.append(equip)

    def pick_battle_party(self):
        if len(self.heroes) <= C.PARTY_LIMIT:
            self.battle_party = copy.deepcopy(self.heroes)
        else:
            self.battle_party = []

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

    def load(self):
        heroes_list = self.read_hero_objects("_heroes")
        self.heroes = heroes_list
        ally_list = self.read_ally_objects("_spirits")
        self.spirits = ally_list
        equipment_list = self.read_equipment_objects("_equipment")
        self.equipment = equipment_list
        jsonFile = open("_items", "r")
        item_bag = json.load(jsonFile)
        item_bag_object = Item_Bag(**item_bag)
        self.items = item_bag_object