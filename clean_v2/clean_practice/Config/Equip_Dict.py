class Equip_Dict:
    def __init__(self):
        self.EQUIPMENT = {
        "Advanced Armor" : {
            "name" : "Advanced Armor", "type" : "Armor", "target" : "Damage", "power" : 1, "effect" : "Decrease_Damage", "effect_specifics" : "Scale", "disallowed_user" : []
        },
        "Advanced Sword" : {
            "name" : "Advanced Sword", "type" : "Weapon", "target" : "Damage", "power" : 1, "effect" : "Increase_Damage", "effect_specifics" : "Scale", "disallowed_user" : []
        },
        "Basic Armor" : {
            "name" : "Basic Armor", "type" : "Armor", "target" : "Damage", "power" : 1, "effect" : "Decrease_Damage", "effect_specifics" : "Flat", "disallowed_user" : []
        },
        "Basic Sword" : {
            "name" : "Basic Sword", "type" : "Weapon", "target" : "Damage", "power" : 1, "effect" : "Increase_Damage", "effect_specifics" : "Flat", "disallowed_user" : []
        },
        "Fire Sword" : {
            "name" : "Fire Sword", "type" : "Weapon", "target" : "Character", "power" : 1, "effect" : "Add_Status", "effect_specifics" : "Burn", "disallowed_user" : []
        }
        }