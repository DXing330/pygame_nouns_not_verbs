class Skill_Dict:
    def __init__(self):
        self.ALL_SKILLS = {
        "_Test" : {
            "name" : "Test", "effect" : "None", "effect_specifics" : "None", "power" : 0, "targets" : "None", "cost" : 0, "cooldown" : 0, "cooldown_counter" : 0, "chance" : 100
        },
        "Blind Hero" : {
            "name" : "Throw Sand", "effect" : "Change_Stats", "effect_specifics" : "Accuracy", "power" : -5, "targets" : "Hero", "cost" : 2, "cooldown" : 0, "cooldown_counter" : 2, "chance" : 100
        },
        "Buff Self" : {
            "name" : "Buff Self", "effect" : "Change_Stats", "effect_specifics" : "Attack", "power" : 2, "targets" : "Self", "cost" : 2, "cooldown" : 0, "cooldown_counter" : 0, "chance" : 100
        },
        "Call Goblin" : {
            "name" : "Call Goblin", "effect" : "Summon", "effect_specifics" : "Goblin", "power" : -1, "targets" : "None", "cost" : 3, "cooldown" : 0, "cooldown_counter" : 2, "chance" : 100
        },
        "Call Wolf" : {
            "name" : "Call Wolf", "effect" : "Summon", "effect_specifics" : "Wolf", "power" : -1, "targets" : "None", "cost" : 3, "cooldown" : 0, "cooldown_counter" : 2, "chance" : 100
        },
        "Cure Hero" : {
            "name" : "Cleanse", "effect" : "Cure_Status", "effect_specifics" : "All", "power" : 1, "targets" : "Hero", "cost" : 3, "cooldown" : 0, "cooldown_counter" : 2, "chance" : 100
        },
        "Cure Partner" : {
            "name" : "Cleanse", "effect" : "Cure_Status", "effect_specifics" : "All", "power" : 1, "targets" : "Partner", "cost" : 0, "cooldown" : 0, "cooldown_counter" : 0, "chance" : 100
        },
        "Command Spirit" : {
            "name" : "Command Spirit", "effect" : "Command", "effect_specifics" : "Spirit", "power" : 1, "targets" : "Spirit", "cost" : -1, "cooldown" : 0, "cooldown_counter" : 0, "chance" : 100
        },
        "Dodge" : {
            "name" : "Dodge", "effect" : "Change_Stats", "effect_specifics" : "Evasion", "power" : 5, "targets" : "Self", "cost" : 1, "cooldown" : 0, "cooldown_counter" : 0, "chance" : 100
        },
        "Dodge+" : {
            "name" : "Dodge+", "effect" : "Change_Stats", "effect_specifics" : "Evasion", "power" : 10, "targets" : "Self", "cost" : 1, "cooldown" : 0, "cooldown_counter" : 0, "chance" : 100
        },
        "Double Attack" : {
            "name" : "Double Attack", "effect" : "Attack", "effect_specifics" : "Basic", "power" : 2, "targets" : "Monster", "cost" : 2, "cooldown" : 0, "cooldown_counter" : 2, "chance" : 100
        },
        "Double Slash" : {
            "name" : "Double Slash", "effect" : "Attack", "effect_specifics" : "Basic", "power" : 2, "targets" : "Hero", "cost" : 3, "cooldown" : 0, "cooldown_counter" : 2, "chance" : 100
        },
        "Flame Send" : {
            "name" : "Flame Send", "effect" : "Change_Stats", "effect_specifics" : "Health", "power" : -1, "targets" : "Hero", "cost" : 0, "cooldown" : 0, "cooldown_counter" : 0, "chance" : 100
        },
        "Focus" : {
            "name" : "Focus", "effect" : "Change_Stats", "effect_specifics" : "Damage_Dealt", "power" : 5, "targets" : "Self", "cost" : -1, "cooldown" : 0, "cooldown_counter" : 0, "chance" : 100
        },
        "Focus+" : {
            "name" : "Focus+", "effect" : "Change_Stats", "effect_specifics" : "Damage_Dealt", "power" : 10, "targets" : "Self", "cost" : 3, "cooldown" : 0, "cooldown_counter" : 3, "chance" : 100
        },
        "Fortify Hero" : {
            "name" : "Fortify", "effect" : "Change_Stats", "effect_specifics" : "Defense", "power" : 2, "targets" : "Hero", "cost" : 2, "cooldown" : 0, "cooldown_counter" : 2, "chance" : 100
        },
        "Heal Hero" : {
            "name" : "Heal Hero", "effect" : "Change_Stats", "effect_specifics" : "Health", "power" : 1, "targets" : "Hero", "cost" : -1, "cooldown" : 0, "cooldown_counter" : 0, "chance" : 100
        },
        "Heal Hero+" : {
            "name" : "Heal Hero+", "effect" : "Change_Stats", "effect_specifics" : "Health", "power" : 2, "targets" : "Hero", "cost" : 3, "cooldown" : 0, "cooldown_counter" : 2, "chance" : 100
        },
        "Heal Heroes" : {
            "name" : "Heal Heroes", "effect" : "Change_Stats", "effect_specifics" : "Health", "power" : 1, "targets" : "All_Hero", "cost" : 3, "cooldown" : 0, "cooldown_counter" : 2, "chance" : 100
        },
        "Heal Partner" : {
            "name" : "Heal Partner", "effect" : "Change_Stats", "effect_specifics" : "Health", "power" : 1, "targets" : "Partner", "cost" : -1, "cooldown" : 0, "cooldown_counter" : 0, "chance" : 100
        },
        "Heal Self" : {
            "name" : "Heal Self", "effect" : "Change_Stats", "effect_specifics" : "Health", "power" : 1, "targets" : "Self", "cost" : -1, "cooldown" : 0, "cooldown_counter" : 0, "chance" : 100
        },
        "Howl" : {
            "name" : "Howl", "effect" : "Change_Stats", "effect_specifics" : "Attack", "power" : 2, "targets" : "All_Monster", "cost" : 2, "cooldown" : 0, "cooldown_counter" : 2, "chance" : 100
        },
        "Shield Hero" : {
            "name" : "Shield", "effect" : "Change_Stats", "effect_specifics" : "Temp_Health", "power" : 2, "targets" : "Hero", "cost" : 2, "cooldown" : 0, "cooldown_counter" : 0, "chance" : 100
        },
        "Shield Partner" : {
            "name" : "Shield", "effect" : "Change_Stats", "effect_specifics" : "Temp_Health", "power" : 2, "targets" : "Partner", "cost" : 0, "cooldown" : 0, "cooldown_counter" : 0, "chance" : 100
        },
        "Shield Self" : {
            "name" : "Shield", "effect" : "Change_Stats", "effect_specifics" : "Temp_Health", "power" : 2, "targets" : "Self", "cost" : 2, "cooldown" : 0, "cooldown_counter" : 0, "chance" : 100
        },
        "Stun Hero" : {
            "name" : "Stun", "effect" : "Disable", "effect_specifics" : "All", "power" : 1, "targets" : "Hero", "cost" : "Target", "cooldown" : 0, "cooldown_counter" : 3, "chance" : 100
        },
        "Stun Monster" : {
            "name" : "Stun", "effect" : "Disable", "effect_specifics" : "All", "power" : 1, "targets" : "Monster", "cost" : "Target", "cooldown" : 0, "cooldown_counter" : 3, "chance" : 100
        },
        "Summon Golem" : {
            "name" : "Summon Golem", "effect" : "Summon", "effect_specifics" : "Golem", "power" : 1, "targets" : "None", "cost" : 6, "cooldown" : 0, "cooldown_counter" : 2, "chance" : 100
        },
        "Summon Turret" : {
            "name" : "Summon Turret", "effect" : "Summon", "effect_specifics" : "Turret", "power" : 1, "targets" : "None", "cost" : 3, "cooldown" : 0, "cooldown_counter" : 0, "chance" : 100
        },
        "Summon Turret+" : {
            "name" : "Summon Turret+", "effect" : "Skill", "effect_specifics" : "Double Turret", "power" : 1, "targets" : "None", "cost" : 7, "cooldown" : 0, "cooldown_counter" : 3, "chance" : 100
        },
        "Weaken Monster" : {
            "name" : "Weaken", "effect" : "Change_Stats", "effect_specifics" : "Attack", "power" : 4, "targets" : "Monster", "cost" : 2, "cooldown" : 0, "cooldown_counter" : 0, "chance" : 100
        },
        "Wound Hero" : {
            "name" : "Wound", "effect" : "Change_Stats", "effect_specifics" : "Max_Health", "power" : 1, "targets" : "Hero", "cost" : 3, "cooldown" : 0, "cooldown_counter" : 2, "chance" : 100
        },
        "Wound Monster" : {
            "name" : "Wound", "effect" : "Change_Stats", "effect_specifics" : "Max_Health", "power" : 1, "targets" : "Monster", "cost" : 3, "cooldown" : 0, "cooldown_counter" : 2, "chance" : 100
        },
        "Wide Slash" : {
            "name" : "Wide Slash", "effect" : "Attack", "effect_specifics" : "Basic", "power" : 1, "targets" : "All_Monster", "cost" : 3, "cooldown" : 0, "cooldown_counter" : 2, "chance" : 100
        },
        "Wide Swing" : {
            "name" : "Wide Slash", "effect" : "Attack", "effect_specifics" : "Basic", "power" : 1, "targets" : "All_Hero", "cost" : 3, "cooldown" : 0, "cooldown_counter" : 2, "chance" : 100
        },
        }
        self.COMPOUND_SKILLS = {
        "_Test" : ["Test1", "Test2"],
        "Double Turret" : ["Summon Turret", "Summon Turret"]
        }