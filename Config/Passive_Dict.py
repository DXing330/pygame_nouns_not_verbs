class Passive_Dict:
    def __init__(self):
        self.BUFFS = {
        "Adrenaline" : {
            "name" : "Adrenaline", "effect" : "Change_Stats", "effect_specifics" : "Attack", "power" : 1, "turns" : 5
        },
        "Curse" : {
            "name" : "Curse", "effect" : "Change_Stats", "effect_specifics" : "All_Base", "power" : -1, "turns" : 5
        },
        "Invisible" : {
            "name" : "Invisible", "effect" : "Change_Stats", "effect_specifics" : "Evasion", "power" : 10, "turns" : 5
        },
        "Regenerate" : {
            "name" : "Regenerate", "effect" : "Change_Stats", "effect_specifics" : "Health", "power" : 1, "turns" : 5
        }
        }
        self.STATUSES = {
        "Bleed" : {
            "name" : "Bleed", "effect" : "Change_Stats", "effect_specifics" : "Max_Health", "power" : -1, "turns" : 5
        },
        "Burn" : {
            "name" : "Burn", "effect" : "Change_Stats", "effect_specifics" : "All", "power" : -1, "turns" : 5
        },
        "Chill" : {
            "name" : "Chill", "effect" : "Change_Stats", "effect_specifics" : "Physical", "power" : -1, "turns" : 5
        },
        "Curse" : {
            "name" : "Curse", "effect" : "Change_Stats", "effect_specifics" : "All_Base", "power" : -1, "turns" : 5
        },
        "Entangle" : {
            "name" : "Entangle", "effect" : "Change_Stats", "effect_specifics" : "Attack", "power" : -1, "turns" : 5
        },
        "Envenomed" : {
            "name" : "Envenomed", "effect" : "Add_Status", "effect_specifics" : "Poison", "power" : 1, "turns" : 5
        },
        "Hemorrhage" : {
            "name" : "Hemorrhage", "effect" : "Add_Status", "effect_specifics" : "Bleed", "power" : 1, "turns" : 5
        },
        "Poison" : {
            "name" : "Poison", "effect" : "Change_Stats", "effect_specifics" : "All", "power" : -1, "turns" : 5
        },
        "Stun" : {
            "name" : "Stun", "effect" : "Disable", "effect_specifics" : "All", "power" : 0, "turns" : 2
        },
        "Wet" : {
            "name" : "Wet", "effect" : "Change_Stats", "effect_specifics" : "Damage_Dealt", "power" : -0.5, "turns" : 5
        }
        }
        self.AURAS = {
        "Darkness" : {
            "name" : "Darkness", "effect" : "Change_Stats", "effect_specifics" : "Accuracy", "targets" : "Heroes", "power" : -30, "turns" : -1, "chance" : 100, "type" : "None"
        },
        "Fog" : {
            "name" : "Fog", "effect" : "Change_Stats", "effect_specifics" : "Accuracy", "targets" : "ALL", "power" : -20, "turns" : -1, "chance" : 50, "type" : "None"
        },
        "Rain" : {
            "name" : "Rain", "effect" : "Add_Status", "effect_specifics" : "Wet", "targets" : "ALL", "power" : 1, "turns" : -1, "chance" : 100, "type" : "Weather"
        },
        "Snow" : {
            "name" : "Snow", "effect" : "Add_Status", "effect_specifics" : "Chill", "targets" : "ALL", "power" : 1, "turns" : -1, "chance" : 50, "type" : "Weather"
        }
        }
        self.CONDITIONALS = {
        "_Test" : {
            "name" : "_Test", "timing" : "None", "condition" : "None", "condition_specifics" : "None", "effect" : "None", "effect_specifics" : "None", "power" : 0
        },
        "Drain Blood" : {
            "name" : "Drain Blood", "timing" : "Attack", "condition" : "Status", "condition_specifics" : "Bleed", "effect" : "Change_Stats", "effect_specifics" : "Health", "power" : 2
        },
        "Goblin Slayer" : {
            "name" : "Goblin Slayer", "timing" : "Attack", "condition" : "Target", "condition_specifics" : "Goblin", "effect" : "Change_Stats", "effect_specifics" : "Damage_Dealt", "power" : 1
        },
        "High Morale" : {
            "name" : "High Morale", "timing" : "Passive", "condition" : "High_Health", "condition_specifics" : "80", "effect" : "Change_Stats", "effect_specifics" : "Damage_Dealt", "power" : 2
        },
        "Last Stand" : {
            "name" : "Last Stand", "timing" : "Passive", "condition" : "Low_Health", "condition_specifics" : "30", "effect" : "Change_Stats", "effect_specifics" : "Damage_Dealt", "power" : 5
        },
        "Troll Heal" : {
            "name" : "Troll Heal", "timing" : "Passive", "condition" : "Not_Status", "condition_specifics" : "Poison", "effect" : "Change_Stats", "effect_specifics" : "Health", "power" : 2
        }
        }