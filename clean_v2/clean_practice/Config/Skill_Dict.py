class Skill_Dict:
    def __init__(self):
        self.ALL_SKILLS = {
        "_Test" : {
            "name" : "Test", "effect" : "None", "effect_specifics" : "None", "power" : 0, "targets" : "None", "cost" : 0, "cooldown" : 0, "cooldown_counter" : 0
                },
        "Command Spirit" : {
            "name" : "Command Spirit", "effect" : "Command", "effect_specifics" : "Spirit", "power" : 1, "targets" : "Spirit", "cost" : -1, "cooldown" : 0, "cooldown_counter" : 0
                },
        "Heal Ally" : {
            "name" : "Heal Ally", "effect" : "Change_Stats", "effect_specifics" : "Health", "power" : 1, "targets" : "Ally", "cost" : -1, "cooldown" : 0, "cooldown_counter" : 0
                },
        "Summon Turret" : {
            "name" : "Summon Turret", "effect" : "Summon", "effect_specifics" : "Turret", "power" : 1, "targets" : "None", "cost" : 3, "cooldown" : 0, "cooldown_counter" : 0
        }
        }