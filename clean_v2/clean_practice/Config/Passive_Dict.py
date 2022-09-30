class Passive_Dict:
    def __init__(self):
        self.BUFFS = {
        "Regenerate" : {
            "name" : "Regenerate", "effect" : "Change_Stats", "effect_specifics" : "Health", "power" : 1, "turns" : -1
        }
        }
        self.STATUSES = {
        "Poison" : {
            "name" : "Poison", "effect" : "Change_Stats", "effect_specifics" : "Health", "power" : -1, "turns" : 5
        }
        }