import copy
import json
from dataclasses import dataclass
from Objects.Characters.Hero import *
from Objects.Characters.Spirit import *
from Objects.Items.Items import *
from Objects.Items.Bag import *


@dataclass
class Party:
    hero_party : list = None
    spirit_allies : list = None
    bag : Bag = None
    equipment : list = None

    def add_hero(self, hero):
        if self.hero_party == None:
            self.hero_party = []
        self.hero_party.append(hero)

    def add_spirit(self, spirit):
        if self.spirit_allies == None:
            self.spirit_allies = []
        self.spirit_allies.append(spirit)

    def add_equipment(self,  equip):
        if self.equipment == None:
            self.equipment = []
        self.equipment.append(equip)

    def update_battle_party(self):
        self.battle_party = []
        for hero in self.hero_party:
            hero : Hero
            copy_hero = copy.deepcopy(hero)
            copy_hero.update_for_battle()
            self.battle_party.append(copy_hero)

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
        self.write_object_list(self.hero_party, "_heroes")
        self.write_object_list(self.spirit_allies, "_spirits")
        self.write_object_list(self.equipment, "_equipment")
        self.write_object(self.bag, "_items")

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
        self.hero_party = heroes_list
        ally_list = self.read_ally_objects("_spirits")
        self.spirit_allies = ally_list
        equipment_list = self.read_equipment_objects("_equipment")
        self.equipment = equipment_list
        jsonFile = open("_items", "r")
        item_bag = json.load(jsonFile)
        item_bag_object = Bag(**item_bag)
        self.bag = item_bag_object