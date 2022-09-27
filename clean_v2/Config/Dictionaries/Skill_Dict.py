class Skill_Dict:
    def __init__(self):
        self.ALL_SKILLS = {
        "_Test" : {
            "name" : "Test", "power" : 1, "effect" : "None", "effect_specifics" : "None",
            "target" : "None", "cost" : 0, "pick_randomly" : True, "cd" : 0, "cd_timer" : 0
        },
        "Command" : {
            "name" : "Command Spirit", "power" : 1, "effect" : "Command", "effect_specifics" : "Basic", "target" : "Spirit", "cost" : -1, "pick_randomly" : False
        },
        "Heal All" : {
            "name" : "Heal Ally", "power" : 1, "effect" : "Change_Stats", "effect_specifics" : "Health", "target" : "All_Ally", "cost" : 5, "pick_randomly" : False
        },
        "Heal Ally" : {
            "name" : "Heal Ally", "power" : 1, "effect" : "Change_Stats", "effect_specifics" : "Health", "target" : "Ally", "cost" : -1, "pick_randomly" : False
        }
        }
        self.COMPOUND_SKILLS = {
        
        }