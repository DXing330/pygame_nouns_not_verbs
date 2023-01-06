class Equip_Dict:
    def __init__(self):
        self.EQUIPMENT = {
        "Advanced Armor" : {
            "name" : "Advanced Armor", "type" : "Armor", "target" : "Damage", "power" : 2, "effect" : "Decrease_Damage", "effect_specifics" : "Scale", "disallowed_user" : []
        },
        "Advanced Armor+" : {
            "name" : "Advanced Armor", "type" : "Armor", "target" : "Damage", "power" : 4, "effect" : "Decrease_Damage", "effect_specifics" : "Scale", "disallowed_user" : []
        },
        "Advanced Armor++" : {
            "name" : "Advanced Armor", "type" : "Armor", "target" : "Damage", "power" : 8, "effect" : "Decrease_Damage", "effect_specifics" : "Scale", "disallowed_user" : []
        },
        "Advanced Armor+++" : {
            "name" : "Advanced Armor", "type" : "Armor", "target" : "Damage", "power" : 16, "effect" : "Decrease_Damage", "effect_specifics" : "Scale", "disallowed_user" : []
        },
        "Advanced Sword" : {
            "name" : "Advanced Sword", "type" : "Weapon", "target" : "Damage", "power" : 2, "effect" : "Increase_Damage", "effect_specifics" : "Scale", "disallowed_user" : []
        },
        "Advanced Sword+" : {
            "name" : "Advanced Sword", "type" : "Weapon", "target" : "Damage", "power" : 4, "effect" : "Increase_Damage", "effect_specifics" : "Scale", "disallowed_user" : []
        },
        "Advanced Sword++" : {
            "name" : "Advanced Sword", "type" : "Weapon", "target" : "Damage", "power" : 8, "effect" : "Increase_Damage", "effect_specifics" : "Scale", "disallowed_user" : []
        },
        "Advanced Sword+++" : {
            "name" : "Advanced Sword", "type" : "Weapon", "target" : "Damage", "power" : 16, "effect" : "Increase_Damage", "effect_specifics" : "Scale", "disallowed_user" : []
        },
        "Basic Armor" : {
            "name" : "Basic Armor", "type" : "Armor", "target" : "Damage", "power" : 1, "effect" : "Decrease_Damage", "effect_specifics" : "Flat", "disallowed_user" : []
        },
        "Basic Armor+" : {
            "name" : "Basic Armor", "type" : "Armor", "target" : "Damage", "power" : 2, "effect" : "Decrease_Damage", "effect_specifics" : "Flat", "disallowed_user" : []
        },
        "Basic Armor++" : {
            "name" : "Basic Armor", "type" : "Armor", "target" : "Damage", "power" : 3, "effect" : "Decrease_Damage", "effect_specifics" : "Flat", "disallowed_user" : []
        },
        "Basic Armor+++" : {
            "name" : "Basic Armor", "type" : "Armor", "target" : "Damage", "power" : 4, "effect" : "Decrease_Damage", "effect_specifics" : "Flat", "disallowed_user" : []
        },
        "Basic Sword" : {
            "name" : "Basic Sword", "type" : "Weapon", "target" : "Damage", "power" : 1, "effect" : "Increase_Damage", "effect_specifics" : "Flat", "disallowed_user" : []
        },
        "Basic Sword+" : {
            "name" : "Basic Sword", "type" : "Weapon", "target" : "Damage", "power" : 2, "effect" : "Increase_Damage", "effect_specifics" : "Flat", "disallowed_user" : []
        },
        "Basic Sword++" : {
            "name" : "Basic Sword", "type" : "Weapon", "target" : "Damage", "power" : 3, "effect" : "Increase_Damage", "effect_specifics" : "Flat", "disallowed_user" : []
        },
        "Basic Sword+++" : {
            "name" : "Basic Sword", "type" : "Weapon", "target" : "Damage", "power" : 4, "effect" : "Increase_Damage", "effect_specifics" : "Flat", "disallowed_user" : []
        },
        "Fire Sword" : {
            "name" : "Fire Sword", "type" : "Weapon", "target" : "Character", "power" : 1, "effect" : "Add_Status", "effect_specifics" : "Burn", "disallowed_user" : []
        }
        }
        self.ARMOR_STORE = {
        0 : "Basic Armor",
        1 : "Advanced Armor"
        }
        self.WEAPON_STORE = {
        0 : "Basic Sword",
        1 : "Advanced Sword"
        }
        self.PRICES = {
        "Basic Armor" : 20,
        "Basic Sword" : 20,
        "Advanced Armor" : 100,
        "Advanced Sword" : 100
        }