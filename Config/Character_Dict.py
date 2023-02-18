class Character_Dict:
    def __init__(self):
        self.HERO_STATS = {
        "Summoner" : {
            "health" : 8, "attack" : 2, "defense" : 1, "skill" : 2, "speed" : 10, "bhealth" : 20, "battack" : 11, "bdefense" : 7, "bskill" : 11
        },
        "Warrior" : {
            "health" : 9, "attack" : 2, "defense" : 2, "skill" : 1, "speed" : 10, "bhealth" : 20, "battack" : 17, "bdefense" : 9, "bskill" : 7
        },
        "Hunter" : {
            "health" : 8, "attack" : 2, "defense" : 1, "skill" : 2, "speed" : 10, "bhealth" : 20, "battack" : 14, "bdefense" : 8, "bskill" : 9
        },
        "Mage" : {
            "health" : 7, "attack" : 1, "defense" : 1, "skill" : 3, "speed" : 10, "bhealth" : 18, "battack" : 10, "bdefense" : 6, "bskill" : 14
        },
        "Knight" : {
            "health" : 9, "attack" : 2, "defense" : 2, "skill" : 1, "speed" : 10, "bhealth" : 20, "battack" : 18, "bdefense" : 18, "bskill" : 2
        },
        "Rogue" : {
            "health" : 8, "attack" : 1, "defense" : 1, "skill" : 3, "speed" : 11, "bhealth" : 20, "battack" : 10, "bdefense" : 8, "bskill" : 11
        }
        }
        self.HERO_SKILLS = {
        "Summoner" : {
            0 : "Command Spirit", 2 : "Summon Turret", 4 : "Summon Two Turret", 6 : "Summon Golem", 8 : "Summon Strong Golem"
        },
        "Hunter" : {
            0 : "Poison Monster Attack", 2 : "Blind Monster", 4 : "Spot Monster Weakness", 6 : "Bind Monster", 8 : "Stun Monster Attack"
        },
        "Knight" : {
            0 : "Shield Self", 2 : "Fortify Self", 4 : "Taunt Monster", 6 : "Shield Heroes", 8 : "Taunt Monsters"
        },
        "Warrior" : {
            0 : "Double Attack", 2 : "Shield Self", 4 : "Focus", 6 : "Wide Slash", 8 : "Triple Slash"
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
            "level" : 1, "variance" : 1, "health" : 0, "attack" : 0, "defense" : 0, "skill" : 0, "speed" : 0, "skills" : [], "passives" : [], "death_effect" : [], "preemptives" : [], "conditionals" : []
        },
        "Assasin" : {
            "level" : 9, "variance" : 1, "health" : 7, "attack" : 4, "defense" : 1, "skill" : 3, "speed" : 11, "skills" : ["Assasinate Hero", "Identify Hero Weakness", "Invisible Self"], "passives" : [], "death_effect" : [], "preemptives" : [], "conditionals" : []
        },
        "Cocoon" : {
            "level" : 2, "variance" : 1, "health" : 10, "attack" : 0, "defense" : 3, "skill" : 0, "speed" : 5, "skills" : ["Nothing"], "passives" : [], "death_effect" : ["Create Moth"], "preemptives" : [], "conditionals" : []
        },
        "Demon" : {
            "level" : 10, "variance" : 2, "health" : 12, "attack" : 5, "defense" : 2, "skill" : 1, "speed" : 10, "skills" : ["Double Slash", "Fireball Heroes"], "passives" : [], "death_effect" : ["Fireball Heroes"], "preemptives" : [], "conditionals" : ["Last Stand"]
        },
        "Elemental" : {
            "level" : 8, "variance" : 2, "health" : 10, "attack" : 3, "defense" : 2, "skill" : 2, "speed" : 10, "skills" : [], "passives" : [], "death_effect" : [], "preemptives" : [], "conditionals" : []
        },
        "Imp" : {
            "level" : 1, "variance" : 1, "health" : 8, "attack" : 2, "defense" : 1, "skill" : 1, "speed" : 10, "skills" : ["Flame Send"], "passives" : [], "death_effect" : [], "preemptives" : [], "conditionals" : []
        },
        "Goblin" : {
            "level" : 1, "variance" : 1, "health" : 8, "attack" : 2, "defense" : 1, "skill" : 1, "speed" : 10, "skills" : ["Blind Hero"], "passives" : [], "death_effect" : [], "preemptives" : [], "conditionals" : ["High Morale"]
        },
        "Golem" : {
            "level" : 1, "variance" : 0, "health" : 10, "attack" : 3, "defense" : 3, "skill" : 1, "speed" : 10, "skills" : ["Fortify Hero"], "passives" : [], "death_effect" : [], "preemptives" : [], "conditionals" : []
        },
        "Hob Goblin" : {
            "level" : 4, "variance" : 1, "health" : 10, "attack" : 3, "defense" : 1, "skill" : 2, "speed" : 10, "skills" : ["Blind Hero", "Call Goblin"], "passives" : [], "death_effect" : [], "preemptives" : ["Call Goblin"], "conditionals" : ["High Morale"]
        },
        "Moth" : {
            "level" : 4, "variance" : 1, "health" : 8, "attack" : 2, "defense" : 1, "skill" : 1, "speed" : 10, "skills" : ["Poison Hero", "Poison Heroes"], "passives" : [], "death_effect" : [], "preemptives" : [], "conditionals" : []
        },
        "Orc" : {
            "level" : 6, "variance" : 2, "health" : 10, "attack" : 4, "defense" : 2, "skill" : 1, "speed" : 10, "skills" : ["Wide Swing", "Double Slash"], "passives" : [], "death_effect" : [], "preemptives" : [], "conditionals" : ["Last Stand"]
        },
        "Serpent" : {
            "level" : 3, "variance" : 1, "health" : 8, "attack" : 3, "defense" : 1, "skill" : 1, "speed" : 10, "skills" : ["Target Hero", "Bite Hero", "Poison Hero"], "passives" : ["Dodge"], "death_effect" : [], "preemptives" : ["Dodge"], "conditionals" : []
        },
        "Slime" : {
            "level" : 1, "variance" : 1, "health" : 10, "attack" : 1, "defense" : 0, "skill" : 0, "speed" : 10, "skills" : ["Nothing"], "passives" : [], "death_effect" : [], "preemptives" : [], "conditionals" : []
        },
        "Turret" : {
            "level" : 1, "variance" : 0, "health" : 5, "attack" : 4, "defense" : 1, "skill" : 0, "speed" : 10, "skills" : [], "passives" : [], "death_effect" : [], "preemptives" : [], "conditionals" : []
        },
        "Troll" : {
            "level" : 6, "variance" : 2, "health" : 12, "attack" : 3, "defense" : 2, "skill" : 1, "speed" : 10, "skills" : ["Wide Swing", "Heal Self"], "passives" : [], "death_effect" : [], "preemptives" : [], "conditionals" : ["Troll Heal"]
        },
        "Vampire" : {
            "level" : 10, "variance" : 2, "health" : 10, "attack" : 3, "defense" : 1, "skill" : 2, "speed" : 10, "skills" : ["Drain Hero", "Stun Hero", "Bleed Hero"], "passives" : [], "death_effect" : [], "preemptives" : [], "conditionals" : ["Drain Blood"]
        },
        "Werewolf" : {
            "level" : 8, "variance" : 2, "health" : 8, "attack" : 5, "defense" : 2, "skill" : 2, "speed" : 10, "skills" : ["Double Slash", "Call Wolf"], "passives" : [], "death_effect" : [], "preemptives" : ["Call Wolf", "Call Wolf"], "conditionals" : ["Last Stand"]
        },
        "Wolf" : {
            "level" : 4, "variance" : 1, "health" : 8, "attack" : 4, "defense" : 1, "skill" : 1, "speed" : 10, "skills" : ["Howl"], "passives" : [], "death_effect" : [], "preemptives" : [], "conditionals" : []
        }
        }
        self.MONSTER_DROPS = {
        "Demon" : {10: "Sharp_Material", 11: "Monster_Extract"},
        "Troll" : {6: "Hard_Material", 7: "Monster_Extract"},
        "Vampire" : {10: "Monster_Extract", 11: "Monster_Extract"},
        "Werewolf" : {8: "Sharp_Material"}
        }