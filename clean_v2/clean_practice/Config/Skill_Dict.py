class Skill_Dict:
    def __init__(self):
        self.ALL_SKILLS = {
        "_Test" : {
            "name" : "Test", "effect" : "None", "effect_specifics" : "None", "power" : 0, "targets" : "None", "cost" : 0, "cooldown" : 0, "cooldown_counter" : 0
        },
        "Blind Hero" : {
            "name" : "Blind", "effect" : "Change_Stats", "effect_specifics" : "Attack", "power" : -1, "targets" : "Hero", "cost" : 2, "cooldown" : 0, "cooldown_counter" : 2
        },
        "Buff Self" : {
            "name" : "Buff Self", "effect" : "Change_Stats", "effect_specifics" : "Attack", "power" : 1, "targets" : "Self", "cost" : 2, "cooldown" : 0, "cooldown_counter" : 0
        },
        "Call Goblin" : {
            "name" : "Call Goblin", "effect" : "Summon", "effect_specifics" : "Goblin", "power" : -1, "targets" : "None", "cost" : 3, "cooldown" : 0, "cooldown_counter" : 2
        },
        "Call Wolf" : {
            "name" : "Call Wolf", "effect" : "Summon", "effect_specifics" : "Wolf", "power" : -1, "targets" : "None", "cost" : 3, "cooldown" : 0, "cooldown_counter" : 2
        },
        "Cure Hero" : {
            "name" : "Cleanse", "effect" : "Cure_Status", "effect_specifics" : "All", "power" : 1, "targets" : "Hero", "cost" : 3, "cooldown" : 0, "cooldown_counter" : 2
        },
        "Command Spirit" : {
            "name" : "Command Spirit", "effect" : "Command", "effect_specifics" : "Spirit", "power" : 1, "targets" : "Spirit", "cost" : -1, "cooldown" : 0, "cooldown_counter" : 0
        },
        "Double Slash" : {
            "name" : "Double Slash", "effect" : "Attack", "effect_specifics" : "Basic", "power" : 2, "targets" : "Hero", "cost" : 3, "cooldown" : 0, "cooldown_counter" : 2
        },
        "Flame Send" : {
            "name" : "Flame Send", "effect" : "Change_Stats", "effect_specifics" : "Health", "power" : -1, "targets" : "Hero", "cost" : 0, "cooldown" : 0, "cooldown_counter" : 0
        },
        "Fortify Hero" : {
            "name" : "Fortify", "effect" : "Change_Stats", "effect_specifics" : "Defense", "power" : 1, "targets" : "Hero", "cost" : 2, "cooldown" : 0, "cooldown_counter" : 2
        },
        "Heal Hero" : {
            "name" : "Heal Hero", "effect" : "Change_Stats", "effect_specifics" : "Health", "power" : 1, "targets" : "Hero", "cost" : -1, "cooldown" : 0, "cooldown_counter" : 0
        },
        "Heal Hero+" : {
            "name" : "Heal Hero+", "effect" : "Change_Stats", "effect_specifics" : "Health", "power" : 2, "targets" : "Hero", "cost" : 3, "cooldown" : 0, "cooldown_counter" : 2
        },
        "Heal Heroes" : {
            "name" : "Heal Heroes", "effect" : "Change_Stats", "effect_specifics" : "Health", "power" : 1, "targets" : "All_Hero", "cost" : 3, "cooldown" : 0, "cooldown_counter" : 2
        },
        "Heal Self" : {
            "name" : "Heal Self", "effect" : "Change_Stats", "effect_specifics" : "Health", "power" : 1, "targets" : "Self", "cost" : -1, "cooldown" : 0, "cooldown_counter" : 0
        },
        "Howl" : {
            "name" : "Howl", "effect" : "Change_Stats", "effect_specifics" : "Attack", "power" : 1, "targets" : "All_Monster", "cost" : 2, "cooldown" : 0, "cooldown_counter" : 2
        },
        "Shield Hero" : {
            "name" : "Shield", "effect" : "Change_Stats", "effect_specifics" : "Temp_Health", "power" : 2, "targets" : "Hero", "cost" : 2, "cooldown" : 0, "cooldown_counter" : 0
        },
        "Stun" : {
            "name" : "Stun", "effect" : "Disable", "effect_specifics" : "All", "power" : 1, "targets" : "Monster", "cost" : 5, "cooldown" : 0, "cooldown_counter" : 3
        },
        "Summon Golem" : {
            "name" : "Summon Golem", "effect" : "Summon", "effect_specifics" : "Golem", "power" : 1, "targets" : "None", "cost" : 6, "cooldown" : 0, "cooldown_counter" : 2
        },
        "Summon Turret" : {
            "name" : "Summon Turret", "effect" : "Summon", "effect_specifics" : "Turret", "power" : 1, "targets" : "None", "cost" : 3, "cooldown" : 0, "cooldown_counter" : 0
        },
        "Summon Turret+" : {
            "name" : "Summon Turret+", "effect" : "Skill", "effect_specifics" : "Double Turret", "power" : 1, "targets" : "None", "cost" : 6, "cooldown" : 0, "cooldown_counter" : 3
        },
        "Weaken Monster" : {
            "name" : "Weaken", "effect" : "Change_Stats", "effect_specifics" : "Attack", "power" : 1, "targets" : "Monster", "cost" : 3, "cooldown" : 0, "cooldown_counter" : 2
        },
        }
        self.COMPOUND_SKILLS = {
        "_Test" : ["Test1", "Test2"],
        "Double Turret" : ["Summon Turret", "Summon Turret"]
        }