class Skill_Dict:
    def __init__(self):
        self.ALL_SKILLS = {
        "_Test" : {
            "name" : "Test", "effect" : "None", "effect_specifics" : "None", "power" : 0, "targets" : "None", "cost" : 0, "cooldown" : 0, "cooldown_counter" : 0, "chance" : 100, "condition" : "Always", "condition_specifics" : "Always"
        },
        "Bind Hero" : {
            "name" : "Throw Net", "effect" : "Add_Status", "effect_specifics" : "Entangle", "power" : 1, "targets" : "Hero", "cost" : 2, "cooldown" : 0, "cooldown_counter" : 2, "chance" : 100, "condition" : "Always", "condition_specifics" : "Always"
        },
        "Bind Monster" : {
            "name" : "Throw Net", "effect" : "Add_Status", "effect_specifics" : "Entangle", "power" : 1, "targets" : "Monster", "cost" : 2, "cooldown" : 0, "cooldown_counter" : 2, "chance" : 100, "condition" : "Always", "condition_specifics" : "Always"
        },
        "Bleed Hero" : {
            "name" : "Bleeding Strike", "effect" : "Add_Status", "effect_specifics" : "Bleed", "power" : 1, "targets" : "Hero", "cost" : 3, "cooldown" : 0, "cooldown_counter" : 3, "chance" : 100, "condition" : "Always", "condition_specifics" : "Always"
        },
        "Bleed Monster" : {
            "name" : "Bleeding Strike", "effect" : "Add_Status", "effect_specifics" : "Bleed", "power" : 1, "targets" : "Monster", "cost" : 3, "cooldown" : 0, "cooldown_counter" : 3, "chance" : 100, "condition" : "Always", "condition_specifics" : "Always"
        },
        "Blind Hero" : {
            "name" : "Throw Sand", "effect" : "Change_Stats", "effect_specifics" : "Accuracy", "power" : -5, "targets" : "Hero", "cost" : 0, "cooldown" : 0, "cooldown_counter" : 1, "chance" : 100, "condition" : "Always", "condition_specifics" : "Always"
        },
        "Blind Monster" : {
            "name" : "Throw Sand", "effect" : "Change_Stats", "effect_specifics" : "Accuracy", "power" : -5, "targets" : "Monster", "cost" : 0, "cooldown" : 0, "cooldown_counter" : 1, "chance" : 100, "condition" : "Always", "condition_specifics" : "Always"
        },
        "Bite Hero" : {
            "name" : "Bite", "effect" : "Attack", "effect_specifics" : "Basic", "power" : 1, "targets" : "Hero", "cost" : 0, "cooldown" : 0, "cooldown_counter" : 0, "chance" : 100, "condition" : "Always", "condition_specifics" : "Always"
        },
        "Burn Hero" : {
            "name" : "Burn", "effect" : "Add_Status", "effect_specifics" : "Burn", "power" : 1, "targets" : "Hero", "cost" : 0, "cooldown" : 0, "cooldown_counter" : 0, "chance" : 100, "condition" : "Always", "condition_specifics" : "Always"
        },
        "Burn Heroes" : {
            "name" : "Burn", "effect" : "Add_Status", "effect_specifics" : "Burn", "power" : 1, "targets" : "All_Hero", "cost" : 2, "cooldown" : 0, "cooldown_counter" : 2, "chance" : 100, "condition" : "Always", "condition_specifics" : "Always"
        },
        "Call Goblin" : {
            "name" : "Call Goblin", "effect" : "Summon", "effect_specifics" : "Goblin", "power" : -1, "targets" : "None", "cost" : 3, "cooldown" : 0, "cooldown_counter" : 2, "chance" : 100, "condition" : "Always", "condition_specifics" : "Always"
        },
        "Call Wolf" : {
            "name" : "Call Wolf", "effect" : "Summon", "effect_specifics" : "Wolf", "power" : -1, "targets" : "None", "cost" : 3, "cooldown" : 0, "cooldown_counter" : 2, "chance" : 100, "condition" : "Always", "condition_specifics" : "Always"
        },
        "Cauterize Hero" : {
            "name" : "Cauterize", "effect" : "Cure_Status", "effect_specifics" : "Bleed", "power" : 1, "targets" : "Hero", "cost" : 1, "cooldown" : 0, "cooldown_counter" : 0, "chance" : 100, "condition" : "Always", "condition_specifics" : "Always"
        },
        "Create Moth" : {
            "name" : "Create Moth", "effect" : "Summon", "effect_specifics" : "Moth", "power" : -1, "targets" : "None", "cost" : 3, "cooldown" : 0, "cooldown_counter" : 2, "chance" : 100, "condition" : "Always", "condition_specifics" : "Always"
        },
        "Cure Hero" : {
            "name" : "Cleanse", "effect" : "Cure_Status", "effect_specifics" : "All", "power" : 1, "targets" : "Hero", "cost" : 2, "cooldown" : 0, "cooldown_counter" : 2, "chance" : 100, "condition" : "Always", "condition_specifics" : "Always"
        },
        "Cure Partner" : {
            "name" : "Cleanse", "effect" : "Cure_Status", "effect_specifics" : "All", "power" : 1, "targets" : "Partner", "cost" : 0, "cooldown" : 0, "cooldown_counter" : 0, "chance" : 100, "condition" : "Always", "condition_specifics" : "Always"
        },
        "Command Spirit" : {
            "name" : "Command Spirit", "effect" : "Command", "effect_specifics" : "Spirit", "power" : 1, "targets" : "Spirit", "cost" : 0, "cooldown" : 0, "cooldown_counter" : 0, "chance" : 100, "condition" : "Always", "condition_specifics" : "Always"
        },
        "Dodge" : {
            "name" : "Dodge", "effect" : "Change_Stats", "effect_specifics" : "Evasion", "power" : 5, "targets" : "Self", "cost" : 1, "cooldown" : 0, "cooldown_counter" : 0, "chance" : 100, "condition" : "Always", "condition_specifics" : "Always"
        },
        "Dodge+" : {
            "name" : "Dodge+", "effect" : "Change_Stats", "effect_specifics" : "Evasion", "power" : 10, "targets" : "Self", "cost" : 1, "cooldown" : 0, "cooldown_counter" : 0, "chance" : 100, "condition" : "Always", "condition_specifics" : "Always"
        },
        "Double Attack" : {
            "name" : "Double Attack", "effect" : "Attack", "effect_specifics" : "Basic", "power" : 2, "targets" : "Monster", "cost" : 2, "cooldown" : 0, "cooldown_counter" : 2, "chance" : 100, "condition" : "Always", "condition_specifics" : "Always"
        },
        "Double Attack+" : {
            "name" : "Double Attack", "effect" : "Attack", "effect_specifics" : "Basic", "power" : 2, "targets" : "Monster", "cost" : 1, "cooldown" : 0, "cooldown_counter" : 1, "chance" : 100, "condition" : "Always", "condition_specifics" : "Always"
        },
        "Double Attack++" : {
            "name" : "Double Attack", "effect" : "Attack", "effect_specifics" : "Basic", "power" : 2, "targets" : "Monster", "cost" : 0, "cooldown" : 0, "cooldown_counter" : 0, "chance" : 100, "condition" : "Always", "condition_specifics" : "Always"
        },
        "Double Slash" : {
            "name" : "Double Slash", "effect" : "Attack", "effect_specifics" : "Basic", "power" : 2, "targets" : "Hero", "cost" : 2, "cooldown" : 0, "cooldown_counter" : 2, "chance" : 100, "condition" : "Always", "condition_specifics" : "Always"
        },
        "Double Slash+" : {
            "name" : "Double Slash", "effect" : "Attack", "effect_specifics" : "Basic", "power" : 2, "targets" : "Hero", "cost" : 1, "cooldown" : 0, "cooldown_counter" : 1, "chance" : 100, "condition" : "Always", "condition_specifics" : "Always"
        },
        "Double Slash++" : {
            "name" : "Double Slash", "effect" : "Attack", "effect_specifics" : "Basic", "power" : 2, "targets" : "Hero", "cost" : 0, "cooldown" : 0, "cooldown_counter" : 0, "chance" : 100, "condition" : "Always", "condition_specifics" : "Always"
        },
        "Drain Hero" : {
            "name" : "Drain", "effect" : "Skill", "effect_specifics" : "Drain Hero", "power" : 1, "targets" : "None", "cost" : 3, "cooldown" : 0, "cooldown_counter" : 2, "chance" : 100, "condition" : "Always", "condition_specifics" : "Always"
        },
        "Energize Hero" : {
            "name" : "Energize", "effect" : "Change_Stats", "effect_specifics" : "Skill", "power" : 1, "targets" : "Hero", "cost" : 3, "cooldown" : 0, "cooldown_counter" : 0, "chance" : 100, "condition" : "Always", "condition_specifics" : "Always"
        },
        "Energize Hero+" : {
            "name" : "Energize", "effect" : "Change_Stats", "effect_specifics" : "Skill", "power" : 1, "targets" : "Hero", "cost" : 2, "cooldown" : 0, "cooldown_counter" : 0, "chance" : 100, "condition" : "Always", "condition_specifics" : "Always"
        },
        "Finish Monster" : {
            "name" : "Execute", "effect" : "Change_Stats", "effect_specifics" : "Health", "power" : -3, "targets" : "Monster", "cost" : 3, "cooldown" : 0, "cooldown_counter" : 3, "chance" : 100, "condition" : "Low_Health", "condition_specifics" : "20"
        },
        "Finish Monster+" : {
            "name" : "Execute", "effect" : "Change_Stats", "effect_specifics" : "Health", "power" : -5, "targets" : "Monster", "cost" : 3, "cooldown" : 0, "cooldown_counter" : 3, "chance" : 100, "condition" : "Low_Health", "condition_specifics" : "20"
        },
        "Fireball Heroes" : {
            "name" : "Fireball", "effect" : "Skill", "effect_specifics" : "Fireball Heroes", "power" : 0, "targets" : "None", "cost" : 3, "cooldown" : 0, "cooldown_counter" : 3, "chance" : 100, "condition" : "Always", "condition_specifics" : "Always"
        },
        "Flame Send" : {
            "name" : "Flame Send", "effect" : "Change_Stats", "effect_specifics" : "Health", "power" : -1, "targets" : "Hero", "cost" : 0, "cooldown" : 0, "cooldown_counter" : 0, "chance" : 100, "condition" : "Always", "condition_specifics" : "Always"
        },
        "Flame Send+" : {
            "name" : "Flame Send", "effect" : "Change_Stats", "effect_specifics" : "Health", "power" : -1, "targets" : "All_Hero", "cost" : 0, "cooldown" : 0, "cooldown_counter" : 0, "chance" : 100, "condition" : "Always", "condition_specifics" : "Always"
        },
        "Focus" : {
            "name" : "Focus", "effect" : "Change_Stats", "effect_specifics" : "Damage_Dealt", "power" : 5, "targets" : "Self", "cost" : 0, "cooldown" : 0, "cooldown_counter" : 0, "chance" : 100, "condition" : "Always", "condition_specifics" : "Always"
        },
        "Focus+" : {
            "name" : "Focus+", "effect" : "Change_Stats", "effect_specifics" : "Damage_Dealt", "power" : 7, "targets" : "Self", "cost" : 0, "cooldown" : 0, "cooldown_counter" : 0, "chance" : 100, "condition" : "Always", "condition_specifics" : "Always"
        },
        "Fortify Hero" : {
            "name" : "Fortify", "effect" : "Change_Stats", "effect_specifics" : "Defense", "power" : 2, "targets" : "Hero", "cost" : 2, "cooldown" : 0, "cooldown_counter" : 2, "chance" : 100, "condition" : "Always", "condition_specifics" : "Always"
        },
        "Freeze Monster" : {
            "name" : "Freeze", "effect" : "Disable", "effect_specifics" : "All", "power" : 2, "targets" : "Monster", "cost" : 1, "cooldown" : 0, "cooldown_counter" : 0, "chance" : 100, "condition" : "Status", "condition_specifics" : "Wet"
        },
        "Heal Hero" : {
            "name" : "Heal Hero", "effect" : "Change_Stats", "effect_specifics" : "Health", "power" : 1, "targets" : "Hero", "cost" : 2, "cooldown" : 0, "cooldown_counter" : 0, "chance" : 100, "condition" : "Always", "condition_specifics" : "Always"
        },
        "Heal Hero+" : {
            "name" : "Heal Hero+", "effect" : "Change_Stats", "effect_specifics" : "Health", "power" : 2, "targets" : "Hero", "cost" : 2, "cooldown" : 0, "cooldown_counter" : 2, "chance" : 100, "condition" : "Always", "condition_specifics" : "Always"
        },
        "Heal Heroes" : {
            "name" : "Heal Heroes", "effect" : "Change_Stats", "effect_specifics" : "Health", "power" : 1, "targets" : "All_Hero", "cost" : 4, "cooldown" : 0, "cooldown_counter" : 2, "chance" : 100, "condition" : "Always", "condition_specifics" : "Always"
        },
        "Heal Monster" : {
            "name" : "Heal Monster", "effect" : "Change_Stats", "effect_specifics" : "Health", "power" : 1, "targets" : "Monster", "cost" : 0, "cooldown" : 0, "cooldown_counter" : 0, "chance" : 100, "condition" : "Always", "condition_specifics" : "Always"
        },
        "Heal Monsters" : {
            "name" : "Heal Monsters", "effect" : "Change_Stats", "effect_specifics" : "Health", "power" : 1, "targets" : "All_Monster", "cost" : 3, "cooldown" : 0, "cooldown_counter" : 2, "chance" : 100, "condition" : "Always", "condition_specifics" : "Always"
        },
        "Heal Partner" : {
            "name" : "Heal Partner", "effect" : "Change_Stats", "effect_specifics" : "Health", "power" : 0.5, "targets" : "Partner", "cost" : 0, "cooldown" : 0, "cooldown_counter" : 0, "chance" : 100, "condition" : "Always", "condition_specifics" : "Always"
        },
        "Heal Self" : {
            "name" : "Heal Self", "effect" : "Change_Stats", "effect_specifics" : "Health", "power" : 1, "targets" : "Self", "cost" :0, "cooldown" : 0, "cooldown_counter" : 0, "chance" : 100, "condition" : "Always", "condition_specifics" : "Always"
        },
        "Heal Self+" : {
            "name" : "Heal Self", "effect" : "Change_Stats", "effect_specifics" : "Health", "power" : 2, "targets" : "Self", "cost" :0, "cooldown" : 0, "cooldown_counter" : 0, "chance" : 100, "condition" : "Always", "condition_specifics" : "Always"
        },
        "Howl" : {
            "name" : "Howl", "effect" : "Change_Stats", "effect_specifics" : "Attack", "power" : 2, "targets" : "All_Monster", "cost" : 2, "cooldown" : 0, "cooldown_counter" : 2, "chance" : 100, "condition" : "Always", "condition_specifics" : "Always"
        },
        "Howl+" : {
            "name" : "Howl", "effect" : "Add_Buff", "effect_specifics" : "Adrenaline", "power" : 1, "targets" : "All_Monster", "cost" : 3, "cooldown" : 0, "cooldown_counter" : 2, "chance" : 100, "condition" : "Always", "condition_specifics" : "Always"
        },
        "Magic Missles" : {
            "name" : "Magic Missles", "effect" : "Change_Stats", "effect_specifics" : "Health", "power" : -1, "targets" : "Monster", "cost" : 1, "cooldown" : 0, "cooldown_counter" : 0, "chance" : 100, "condition" : "Always", "condition_specifics" : "Always"
        },
        "Make Rain" : {
            "name" : "Make Rain", "effect" : "Aura", "effect_specifics" : "Rain", "power" : 0, "targets" : "None", "cost" : 5, "cooldown" : 0, "cooldown_counter" : 5, "chance" : 100, "condition" : "Always", "condition_specifics" : "Always"
        },
        "Nothing" : {
            "name" : "Nothing", "effect" : "None", "effect_specifics" : "None", "power" : 0, "targets" : "Self", "cost" : 0, "cooldown" : 0, "cooldown_counter" : 0, "chance" : 100, "condition" : "Always", "condition_specifics" : "Always"
        },
        "Poison Hero" : {
            "name" : "Poison", "effect" : "Add_Status", "effect_specifics" : "Poison", "power" : 1, "targets" : "Hero", "cost" : 1, "cooldown" : 0, "cooldown_counter" : 0, "chance" : 100, "condition" : "Always", "condition_specifics" : "Always"
        },
        "Poison Heroes" : {
            "name" : "Poison", "effect" : "Add_Status", "effect_specifics" : "Poison", "power" : 1, "targets" : "All_Hero", "cost" : "Scale", "cooldown" : 0, "cooldown_counter" : 0, "chance" : 100, "condition" : "Always", "condition_specifics" : "Always"
        },
        "Poison Monster" : {
            "name" : "Poison", "effect" : "Add_Status", "effect_specifics" : "Poison", "power" : 1, "targets" : "Monster", "cost" : 1, "cooldown" : 0, "cooldown_counter" : 2, "chance" : 100, "condition" : "Always", "condition_specifics" : "Always"
        },
        "Reveal Monsters" : {
            "name" : "Reveal", "effect" : "Change_Stats", "effect_specifics" : "Dodge", "power" : -2, "targets" : "All_Monster", "cost" : 1, "cooldown" : 0, "cooldown_counter" : 0, "chance" : 100, "condition" : "Always", "condition_specifics" : "Always"
        },
        "Shield Hero" : {
            "name" : "Shield", "effect" : "Change_Stats", "effect_specifics" : "Temp_Health", "power" : 2, "targets" : "Hero", "cost" : 2, "cooldown" : 0, "cooldown_counter" : 0, "chance" : 100, "condition" : "Always", "condition_specifics" : "Always"
        },
        "Shield Partner" : {
            "name" : "Shield", "effect" : "Change_Stats", "effect_specifics" : "Temp_Health", "power" : 1, "targets" : "Partner", "cost" : 0, "cooldown" : 0, "cooldown_counter" : 0, "chance" : 100, "condition" : "Always", "condition_specifics" : "Always"
        },
        "Shield Self" : {
            "name" : "Shield", "effect" : "Change_Stats", "effect_specifics" : "Temp_Health", "power" : 2, "targets" : "Self", "cost" : 0, "cooldown" : 0, "cooldown_counter" : 0, "chance" : 100, "condition" : "Always", "condition_specifics" : "Always"
        },
        "Spot Monster Weakness" : {
            "name" : "Spot Weakness", "effect" : "Change_Stats", "effect_specifics" : "Defense", "power" : -1, "targets" : "Monster", "cost" : 1, "cooldown" : 0, "cooldown_counter" : 1, "chance" : 100, "condition" : "Always", "condition_specifics" : "Always"
        },
        "Strike Monster" : {
            "name" : "Strike", "effect" : "Change_Stats", "effect_specifics" : "Health", "power" : -1, "targets" : "Monster", "cost" : 1, "cooldown" : 0, "cooldown_counter" : 0, "chance" : 100, "condition" : "Always", "condition_specifics" : "Always"
        },
        "Stun Hero" : {
            "name" : "Stun", "effect" : "Disable", "effect_specifics" : "All", "power" : 1, "targets" : "Hero", "cost" : "Target", "cooldown" : 0, "cooldown_counter" : 3, "chance" : 100, "condition" : "Always", "condition_specifics" : "Always"
        },
        "Stun Monster" : {
            "name" : "Stun", "effect" : "Disable", "effect_specifics" : "All", "power" : 1, "targets" : "Monster", "cost" : "Target", "cooldown" : 0, "cooldown_counter" : 3, "chance" : 100, "condition" : "Always", "condition_specifics" : "Always"
        },
        "Summon Golem" : {
            "name" : "Summon Golem", "effect" : "Summon", "effect_specifics" : "Golem", "power" : 1, "targets" : "None", "cost" : 5, "cooldown" : 0, "cooldown_counter" : 2, "chance" : 100, "condition" : "Always", "condition_specifics" : "Always"
        },
        "Summon Strong Golem" : {
            "name" : "Summon Big Golem", "effect" : "Summon", "effect_specifics" : "Golem", "power" : 8, "targets" : "None", "cost" : 10, "cooldown" : 0, "cooldown_counter" : 2, "chance" : 100, "condition" : "Always", "condition_specifics" : "Always"
        },
        "Summon Turret" : {
            "name" : "Summon Turret", "effect" : "Summon", "effect_specifics" : "Turret", "power" : 1, "targets" : "None", "cost" : 2, "cooldown" : 0, "cooldown_counter" : 0, "chance" : 100, "condition" : "Always", "condition_specifics" : "Always"
        },
        "Summon Two Turret" : {
            "name" : "Summon Two Turret", "effect" : "Skill", "effect_specifics" : "Double Turret", "power" : 1, "targets" : "None", "cost" : 5, "cooldown" : 0, "cooldown_counter" : 3, "chance" : 100, "condition" : "Always", "condition_specifics" : "Always"
        },
        "Target Hero" : {
            "name" : "Target", "effect" : "Target", "effect_specifics" : "None", "power" : 1, "targets" : "Hero", "cost" : 0, "cooldown" : 0, "cooldown_counter" : 0, "chance" : 100, "condition" : "Always", "condition_specifics" : "Always"
        },
        "Target Monster" : {
            "name" : "Target", "effect" : "Target", "effect_specifics" : "None", "power" : 1, "targets" : "Monster", "cost" : 0, "cooldown" : 0, "cooldown_counter" : 0, "chance" : 100, "condition" : "Always", "condition_specifics" : "Always"
        },
        "Triple Slash" : {
            "name" : "Triple Attack", "effect" : "Attack", "effect_specifics" : "Basic", "power" : 3, "targets" : "Monster", "cost" : 4, "cooldown" : 0, "cooldown_counter" : 3, "chance" : 100, "condition" : "Always", "condition_specifics" : "Always"
        },
        "Warm Hero" : {
            "name" : "Warm", "effect" : "Cure_Status", "effect_specifics" : "Chill", "power" : 1, "targets" : "Hero", "cost" : 1, "cooldown" : 0, "cooldown_counter" : 0, "chance" : 100, "condition" : "Always", "condition_specifics" : "Always"
        },
        "Weaken Monster" : {
            "name" : "Weaken", "effect" : "Change_Stats", "effect_specifics" : "Attack", "power" : 4, "targets" : "Monster", "cost" : 2, "cooldown" : 0, "cooldown_counter" : 0, "chance" : 100, "condition" : "Always", "condition_specifics" : "Always"
        },
        "Wound Hero" : {
            "name" : "Wound", "effect" : "Change_Stats", "effect_specifics" : "Max_Health", "power" : 1, "targets" : "Hero", "cost" : 3, "cooldown" : 0, "cooldown_counter" : 2, "chance" : 100, "condition" : "Always", "condition_specifics" : "Always"
        },
        "Wound Monster" : {
            "name" : "Wound", "effect" : "Change_Stats", "effect_specifics" : "Max_Health", "power" : 1, "targets" : "Monster", "cost" : 3, "cooldown" : 0, "cooldown_counter" : 2, "chance" : 100, "condition" : "Always", "condition_specifics" : "Always"
        },
        "Wide Slash" : {
            "name" : "Wide Slash", "effect" : "Attack", "effect_specifics" : "Basic", "power" : 1, "targets" : "All_Monster", "cost" : "Scale", "cooldown" : 0, "cooldown_counter" : 2, "chance" : 100, "condition" : "Always", "condition_specifics" : "Always"
        },
        "Wide Swing" : {
            "name" : "Wide Slash", "effect" : "Attack", "effect_specifics" : "Basic", "power" : 1, "targets" : "All_Hero", "cost" : "Scale", "cooldown" : 0, "cooldown_counter" : 2, "chance" : 100, "condition" : "Always", "condition_specifics" : "Always"
        },
        }
        self.COMPOUND_SKILLS = {
        "_Test" : ["Test1", "Test2"],
        "Double Turret" : ["Summon Turret", "Summon Turret"],
        "Drain Hero" : ["Heal Self", "Bite Hero"],
        "Fireball Heroes" : ["Flame Send+", "Burn Heroes"]
        }