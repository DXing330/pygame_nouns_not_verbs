class Passive_Dict:
    def __init__(self):
        self.ALL_EFFECTS = {
        "_Test" : {
            "name" : "Test", "effect" : "Test", "effect_specifics" : "Test",
            "type" : "Test", "power" : 1, "turns" : -1
        },
        "HP+" : {
            "name" : "HP+", "effect" : "Change_Stats", "effect_specifics" : "Health",
            "type" : "Buff", "power" : 1, "turns" : -1
        }
        }