class Passive_Dict:
    def __init__(self):
        self.ALL_EFFECTS = {
        "HP+" : {
            "name" : "HP+", "effect" : "Change_Stats", "effect_specifics" : "Health",
            "timing" : "Standby", "type" : "Buff", "power" : 1, "turns" : -1
        }
        }