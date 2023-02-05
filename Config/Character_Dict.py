class Character_Dict:
    def __init__(self):
        self.HERO_STATS = {
        "Summoner" : {
            "health" : 10, "attack" : 2, "defense" : 1, "skill" : 2, "speed" : 10
        },
        "Warrior" : {
            "health" : 10, "attack" : 3, "defense" : 2, "skill" : 1, "speed" : 10
        },
        "Hunter" : {
            "health" : 10, "attack" : 2, "defense" : 1, "skill" : 2, "speed" : 10
        },
        "Mage" : {
            "health" : 10, "attack" : 1, "defense" : 1, "skill" : 2, "speed" : 10
        }
        }
        self.HERO_SKILLS = {
        "Summoner" : {
            0 : "Command Spirit", 2 : "Summon Turret", 4 : "Summon Turret+", 6 : "Summon Golem", 8 : "Summon Golem+"
        },
        "Warrior" : {
            0 : "Double Attack", 2 : "Shield Self", 4 : "Focus", 6 : "Wide Slash", 8 : "Triple Slash"
        },
        "Hunter" : {
            0 : "Poison Monster", 2 : "Blind Monster", 4 : "Spot Monster Weakness", 6 : "Bind Monster", 8 : "Stun Monster"
        }
        }
        self.SPIRIT_SKILLS = {
        "Angel" : {
            0 : "Heal Hero", 2 : "Shield Hero", 4 : "Cure Hero", 6 : "Heal Heroes", 8 : "Strike Monster", 10 : "Energize Hero"
        },
        "Fairy" : {
            0 : "Blind Monster"
        }
        }
        self.SPIRIT_PASSIVES = {
        "Angel" : {
            4 : "Heal Partner", 6 : "Shield Partner", 8 : "Cure Partner", 10 : "Strike Monster"
        },
        "Fairy" : {
            4 : "Blind Monster"
        }
        }
        self.MONSTER_STATS = {
        "Cocoon" : {
            "level" : 2, "variance" : 1, "health" : 10, "attack" : 0, "defense" : 3, "skill" : 0, "speed" : 5, "skills" : ["Nothing"], "passives" : [], "death_effect" : ["Create Moth"], "preemptives" : []
        },
        "Demon" : {
            "level" : 10, "variance" : 2, "health" : 12, "attack" : 5, "defense" : 2, "skill" : 1, "speed" : 10, "skills" : ["Double Slash", "Fireball Heroes"], "passives" : [], "death_effect" : [], "preemptives" : []
        },
        "Imp" : {
            "level" : 2, "variance" : 1, "health" : 8, "attack" : 2, "defense" : 1, "skill" : 1, "speed" : 10, "skills" : ["Flame Send"], "passives" : [], "death_effect" : [], "preemptives" : []
        },
        "Goblin" : {
            "level" : 1, "variance" : 1, "health" : 8, "attack" : 2, "defense" : 1, "skill" : 1, "speed" : 10, "skills" : ["Blind Hero"], "passives" : [], "death_effect" : [], "preemptives" : []
        },
        "Golem" : {
            "level" : 1, "variance" : 0, "health" : 10, "attack" : 3, "defense" : 3, "skill" : 1, "speed" : 10, "skills" : ["Fortify Hero"], "passives" : [], "death_effect" : [], "preemptives" : []
        },
        "Hob Goblin" : {
            "level" : 4, "variance" : 1, "health" : 10, "attack" : 3, "defense" : 1, "skill" : 2, "speed" : 10, "skills" : ["Blind Hero", "Call Goblin"], "passives" : [], "death_effect" : [], "preemptives" : ["Call Goblin"]
        },
        "Moth" : {
            "level" : 4, "variance" : 1, "health" : 8, "attack" : 2, "defense" : 1, "skill" : 1, "speed" : 10, "skills" : ["Poison Hero", "Poison Heroes"], "passives" : [], "death_effect" : [], "preemptives" : []
        },
        "Orc" : {
            "level" : 6, "variance" : 2, "health" : 10, "attack" : 4, "defense" : 2, "skill" : 1, "speed" : 10, "skills" : ["Wide Swing", "Double Slash"], "passives" : [], "death_effect" : [], "preemptives" : []
        },
        "Serpent" : {
            "level" : 3, "variance" : 1, "health" : 8, "attack" : 3, "defense" : 1, "skill" : 1, "speed" : 10, "skills" : ["Target Hero", "Bite Hero", "Poison Hero"], "passives" : ["Dodge"], "death_effect" : [], "preemptives" : ["Dodge"]
        },
        "Turret" : {
            "level" : 1, "variance" : 0, "health" : 5, "attack" : 4, "defense" : 1, "skill" : 0, "speed" : 10, "skills" : [], "passives" : [], "death_effect" : [], "preemptives" : []
        },
        "Troll" : {
            "level" : 6, "variance" : 2, "health" : 12, "attack" : 3, "defense" : 2, "skill" : 1, "speed" : 10, "skills" : ["Wide Swing", "Heal Self"], "passives" : [], "death_effect" : [], "preemptives" : []
        },
        "Vampire" : {
            "level" : 10, "variance" : 2, "health" : 10, "attack" : 3, "defense" : 1, "skill" : 2, "speed" : 10, "skills" : ["Drain Hero", "Stun Hero", "Bleed Hero"], "passives" : [], "death_effect" : [], "preemptives" : []
        },
        "Werewolf" : {
            "level" : 6, "variance" : 1, "health" : 8, "attack" : 5, "defense" : 2, "skill" : 2, "speed" : 10, "skills" : ["Double Slash"], "passives" : [], "death_effect" : [], "preemptives" : []
        },
        "Wolf" : {
            "level" : 3, "variance" : 1, "health" : 8, "attack" : 4, "defense" : 1, "skill" : 1, "speed" : 10, "skills" : ["Howl"], "passives" : [], "death_effect" : [], "preemptives" : []
        }
        }