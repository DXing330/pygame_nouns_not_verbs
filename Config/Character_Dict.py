class Character_Dict:
    def __init__(self):
        self.BASE_STATS = {
        "Blob" : {
            "health" : 20, "attack" : 5, "defense" : 5, "skill" : 5, "speed" : 9
        },
        "Dragon" : {
            "health" : 40, "attack" : 20, "defense" : 20, "skill" : 10, "speed" : 10
        },
        "Fodder" : {
            "health" : 10, "attack" : 5, "defense" : 1, "skill" : 2, "speed" : 9
        },
        "Glass_Cannon" : {
            "health" : 15, "attack" : 15, "defense" : 5, "skill" : 10, "speed" : 10
        },
        "God" : {
            "health" : 99, "attack" : 99, "defense" : 99, "skill" : 99, "speed" : 99
        },
        "Mob" : {
            "health" : 15, "attack" : 10, "defense" : 5, "skill" : 5, "speed" : 9
        },
        "Regular" : {
            "health" : 20, "attack" : 10, "defense" : 10, "skill" : 10, "speed" : 10
        },
        "Tank" : {
            "health" : 20, "attack" : 10, "defense" : 20, "skill" : 5, "speed" : 9
        }
        }
        self.GROWTH_STATS = {
        "Hero_1" : {
            "health" : 8, "attack" : 2, "defense" : 1, "skill" : 2
        },
        "Hero_2" : {
            "health" : 9, "attack" : 2, "defense" : 2, "skill" : 1
        },
        "Hero_3" : {
            "health" : 7, "attack" : 1, "defense" : 1, "skill" : 3
        },
        "Blob" : {
            "health" : 9, "attack" : 1, "defense" : 0, "skill" : 0
        },
        "Dragon" : {
            "health" : 18, "attack" : 4, "defense" : 4, "skill" : 2
        },
        "Fodder" : {
            "health" : 2, "attack" : 1, "defense" : 0, "skill" : 1
        },
        "Glass_Cannon" : {
            "health" : 6, "attack" : 4, "defense" : 1, "skill" : 2
        },
        "God" : {
            "health" : 99, "attack" : 99, "defense" : 99, "skill" : 99
        },
        "Mob" : {
            "health" : 5, "attack" : 2, "defense" : 1, "skill" : 1
        },
        "Regular" : {
            "health" : 8, "attack" : 3, "defense" : 2, "skill" : 1
        },
        "Tank" : {
            "health" : 9, "attack" : 1, "defense" : 3, "skill" : 1
        }
        }
        self.HERO_STATS = {
        "Summoner" : {
            "growth" : "Hero_1", "speed" : 10, "bhealth" : 20, "battack" : 11, "bdefense" : 7, "bskill" : 11
        },
        "Warrior" : {
            "growth" : "Hero_2", "speed" : 10, "bhealth" : 20, "battack" : 17, "bdefense" : 9, "bskill" : 7
        },
        "Hunter" : {
            "growth" : "Hero_1", "speed" : 10, "bhealth" : 20, "battack" : 14, "bdefense" : 8, "bskill" : 9
        },
        "Mage" : {
            "growth" : "Hero_3", "speed" : 10, "bhealth" : 18, "battack" : 8, "bdefense" : 6, "bskill" : 14
        },
        "Knight" : {
            "growth" : "Hero_2", "speed" : 10, "bhealth" : 20, "battack" : 16, "bdefense" : 16, "bskill" : 4
        },
        "Rogue" : {
            "growth" : "Hero_3", "speed" : 11, "bhealth" : 20, "battack" : 10, "bdefense" : 8, "bskill" : 11
        }
        }
        self.HERO_SKILLS = {
        "Summoner" : {
            0 : "Command Spirit", 2 : "Summon Turret"
        },
        "Hunter" : {
            0 : "Poison Monster Attack", 2 : "Blind Monster", 4 : "Spot Monster Weakness", 6 : "Bind Monster", 8 : "Stun Monster Attack"
        },
        "Knight" : {
            0 : "Shield Self", 2 : "Fortify Self", 4 : "Taunt Monster", 6 : "Shield Heroes", 8 : "Taunt Monsters"
        },
        "Warrior" : {
            0 : "Double Attack", 2 : "Focus", 4 : "Wide Slash", 6 : "Triple Slash"
        }
        }
        self.SPIRIT_SKILLS = {
        "Angel" : {
            0 : "Shield Hero", 2 : "Heal Hero", 4 : "Cure Hero", 6 : "Heal Heroes", 8 : "Strike Monster", 10 : "Energize Hero"
        },
        "Fairy" : {
            0 : "Blind Monster"
        }
        }
        self.SPIRIT_PASSIVES = {
        "Angel" : {
            4 : "Shield Partner", 6 : "Heal Partner", 8 : "Cure Partner", 10 : "Strike Monster"
        },
        "Fairy" : {
            4 : "Blind Monster"
        }
        }
        self.MONSTER_STATS = {
        "_Dummy" : {
            "level" : 1, "variance" : 1, "base" : "Mob", "growth" : "Mob", "skills" : [], "passives" : [], "death_effect" : [], "preemptives" : [], "conditionals" : []
        },
        "Assasin" : {
            "level" : 9, "variance" : 1, "base" : "Glass_Cannon", "growth" : "Glass_Cannon", "skills" : ["Assasinate Hero", "Identify Hero Weakness", "Invisible Self"], "passives" : [], "death_effect" : [], "preemptives" : [], "conditionals" : []
        },
        "Big Rat" : {
            "level" : 2, "variance" : 1, "base" : "Mob", "growth" : "Mob", "skills" : ["Bleed Hero"], "passives" : [], "death_effect" : ["Create Rat", "Create Rat"], "preemptives" : [], "conditionals" : []
        },
        "Big Slime" : {
            "level" : 6, "variance" : 1, "base" : "Blob", "growth" : "Blob", "skills" : ["Slime Split", "Poison Hero Attack"], "passives" : [], "death_effect" : ["Poison Heroes"], "preemptives" : [], "conditionals" : ["Poison Heal", "Poison Cure", "Bleed Heal", "Bleed Cure"]
        },
        "Cocoon" : {
            "level" : 2, "variance" : 1, "base" : "Tank", "growth" : "Tank", "skills" : ["Nothing"], "passives" : [], "death_effect" : ["Create Moth"], "preemptives" : [], "conditionals" : []
        },
        "Demon" : {
            "level" : 10, "variance" : 2, "base" : "Regular", "growth" : "Regular", "skills" : ["Double Slash", "Fireball Heroes"], "passives" : [], "death_effect" : ["Fireball Heroes"], "preemptives" : [], "conditionals" : ["Last Stand"]
        },
        "Elemental" : {
            "level" : 8, "variance" : 2, "base" : "Regular", "growth" : "Regular", "skills" : [], "passives" : [], "death_effect" : [], "preemptives" : [], "conditionals" : []
        },
        "Imp" : {
            "level" : 1, "variance" : 1, "base" : "Mob", "growth" : "Mob", "skills" : ["Flame Send"], "passives" : [], "death_effect" : [], "preemptives" : [], "conditionals" : []
        },
        "Giant Rat" : {
            "level" : 3, "variance" : 1, "base" : "Regular", "growth" : "Regular", "skills" : ["Bleed Hero"], "passives" : [], "death_effect" : ["Create Big Rat", "Create Big Rat"], "preemptives" : [], "conditionals" : []
        },
        "Goblin" : {
            "level" : 1, "variance" : 1, "base" : "Mob", "growth" : "Mob", "skills" : ["Blind Hero"], "passives" : [], "death_effect" : [], "preemptives" : [], "conditionals" : ["High Morale"]
        },
        "Gold Dragon" : {
            "level" : 20, "variance" : 1, "base" : "Dragon", "growth" : "Dragon", "skills" : ["Fireball Heroes"], "passives" : ["Cure Self", "Heal Self"], "death_effect" : [], "preemptives" : [], "conditionals" : []
        },
        "Golem" : {
            "level" : 1, "variance" : 0, "base" : "Regular", "growth" : "Regular", "skills" : ["Fortify Hero"], "passives" : [], "death_effect" : [], "preemptives" : [], "conditionals" : []
        },
        "Hob Goblin" : {
            "level" : 4, "variance" : 1, "base" : "Regular", "growth" : "Regular", "skills" : ["Blind Hero", "Call Goblin"], "passives" : [], "death_effect" : [], "preemptives" : ["Call Goblin"], "conditionals" : ["High Morale"]
        },
        "Moth" : {
            "level" : 4, "variance" : 1, "base" : "Regular", "growth" : "Regular", "skills" : ["Poison Hero", "Poison Heroes"], "passives" : [], "death_effect" : [], "preemptives" : [], "conditionals" : []
        },
        "Orc" : {
            "level" : 6, "variance" : 2, "base" : "Regular", "growth" : "Regular", "skills" : ["Wide Swing", "Double Slash"], "passives" : [], "death_effect" : [], "preemptives" : [], "conditionals" : ["Last Stand"]
        },
        "Rat" : {
            "level" : 1, "variance" : 1, "base" : "Fodder", "growth" : "Fodder", "skills" : ["Bleed Hero"], "passives" : [], "death_effect" : [], "preemptives" : [], "conditionals" : []
        },
        "Serpent" : {
            "level" : 3, "variance" : 1, "base" : "Mob", "growth" : "Mob", "skills" : ["Target Hero", "Bite Hero", "Poison Hero"], "passives" : ["Dodge"], "death_effect" : [], "preemptives" : ["Dodge"], "conditionals" : []
        },
        "Slime" : {
            "level" : 3, "variance" : 1, "base" : "Blob", "growth" : "Blob", "skills" : ["Slime Split", "Poison Hero Attack"], "passives" : [], "death_effect" : ["Poison Heroes"], "preemptives" : [], "conditionals" : ["Poison Heal", "Poison Cure", "Bleed Heal", "Bleed Cure"]
        },
        "Turret" : {
            "level" : 1, "variance" : 0, "base" : "Glass_Cannon", "growth" : "Glass_Cannon", "skills" : [], "passives" : [], "death_effect" : [], "preemptives" : [], "conditionals" : []
        },
        "Troll" : {
            "level" : 6, "variance" : 2, "base" : "Regular", "growth" : "Regular", "skills" : ["Wide Swing", "Heal Self"], "passives" : [], "death_effect" : [], "preemptives" : [], "conditionals" : ["Troll Heal"]
        },
        "Vampire" : {
            "level" : 10, "variance" : 2, "base" : "Regular", "growth" : "Regular", "skills" : ["Drain Hero", "Stun Hero", "Bleed Hero"], "passives" : [], "death_effect" : [], "preemptives" : [], "conditionals" : ["Drain Blood"]
        },
        "Werewolf" : {
            "level" : 8, "variance" : 2, "base" : "Glass_Cannon", "growth" : "Glass_Cannon", "skills" : ["Double Slash", "Call Wolf"], "passives" : ["Keen Smell"], "death_effect" : [], "preemptives" : ["Call Wolf", "Call Wolf"], "conditionals" : ["Last Stand"]
        },
        "Wolf" : {
            "level" : 4, "variance" : 1, "base" : "Glass_Cannon", "growth" : "Glass_Cannon", "skills" : ["Howl"], "passives" : ["Keen Smell"], "death_effect" : [], "preemptives" : [], "conditionals" : []
        }
        }
        self.MONSTER_GROUPS = {
        "SF1" : ["Goblin"],
        "SF2" : ["Imp"],
        "SF3" : ["Goblin", "Goblin"],
        "SF4" : ["Goblin", "Imp"],
        "SF5" : ["Goblin", "Goblin", "Goblin"],
        "SF6" : ["Imp", "Imp"],
        "DF1" : ["Serpent", "Serpent"],
        "DF2" : ["Imp", "Serpent"],
        "DF3" : ["Goblin", "Goblin", "Goblin"],
        "DF4" : ["Imp", "Imp", "Serpent"],
        "DF5" : ["Imp", "Imp", "Serpent", "Serpent"],
        "DF6" : ["Goblin", "Goblin", "Goblin", "Goblin"],
        "WD1" : ["Wolf", "Wolf"],
        "WD2" : ["Wolf", "Wolf", "Wolf"],
        "WD3" : ["Wolf", "Wolf", "Wolf", "Wolf"],
        "WD4" : ["Serpent", "Serpent"],
        "WD5" : ["Wolf", "Wolf", "Serpent", "Serpent"],
        "WD6" : ["Serpent", "Serpent", "Serpent", "Serpent"],
        "EF1" : ["Orc", "Orc"],
        "EF2" : ["Orc", "Orc", "Orc"],
        "EF3" : ["Orc", "Orc", "Orc", "Orc"],
        "EF4" : ["Troll", "Troll"],
        "EF5" : ["Troll", "Troll", "Orc", "Orc"],
        "EF6" : ["Troll", "Troll", "Troll"]
        }