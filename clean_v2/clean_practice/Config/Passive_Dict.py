class Passive_Dict:
    def __init__(self):
        self.BUFFS = {
        "Regenerate" : {
            "name" : "Regenerate", "effect" : "Change_Stats", "effect_specifics" : "Health", "power" : 1, "turns" : -1
        }
        }
        self.STATUSES = {
        "Burn" : {
            "name" : "Burn", "effect" : "Change_Stats", "effect_specifics" : "All", "power" : -1, "turns" : 5
        },
        "Poison" : {
            "name" : "Poison", "effect" : "Change_Stats", "effect_specifics" : "Health", "power" : -1, "turns" : 5
        },
        "Stun" : {
            "name" : "Stun", "effect" : "Disable", "effect_specifics" : "All", "power" : 0, "turns" : 2
        }
        }