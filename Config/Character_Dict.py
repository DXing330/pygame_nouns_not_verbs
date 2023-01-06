class Character_Dict:
    def __init__(self):
        self.HERO_STATS = {
        "Summoner" : {
            "health" : 10, "attack" : 2, "defense" : 1, "skill" : 2
        },
        "Warrior" : {
            "health" : 10, "attack" : 4, "defense" : 2, "skill" : 1

        }
        }
        self.HERO_SKILLS = {
        "Summoner" : {
            0 : "Command Spirit", 2 : "Summon Turret", 4 : "Summon Turret+", 6 : "Summon Golem"
        },
        "Warrior" : {
            0 : "Double Attack", 2 : "Shield Self", 4 : "Focus", 6 : "Wide Slash"
        }
        }
        self.SPIRIT_SKILLS = {
        "Angel" : {
            0 : "Heal Hero", 2 : "Shield Hero", 4 : "Cure Hero", 6 : "Heal Heroes", 8 : "Heal Hero+", 10 : "Weaken Monster"
        }
        }
        self.SPIRIT_PASSIVES = {
        "Angel" : {
            3 : "Heal Partner", 6 : "Shield Partner", 9 : "Cure Partner"
        }
        }
        self.MONSTER_STATS = {
        "Imp" : {
            "level" : 2, "variance" : 1, "health" : 10, "attack" : 2, "defense" : 1, "skill" : 1, "skills" : ["Flame Send"], "passives" : [], "death_effect" : []
        },
        "Goblin" : {
            "level" : 1, "variance" : 1, "health" : 10, "attack" : 2, "defense" : 1, "skill" : 1, "skills" : ["Blind Hero"], "passives" : [], "death_effect" : []
        },
        "Golem" : {
            "level" : 1, "variance" : 0, "health" : 10, "attack" : 4, "defense" : 4, "skill" : 0, "skills" : ["Fortify Hero"], "passives" : [], "death_effect" : []
        },
        "Hob Goblin" : {
            "level" : 4, "variance" : 1, "health" : 12, "attack" : 3, "defense" : 1, "skill" : 2, "skills" : ["Blind Hero", "Call Goblin"], "passives" : [], "death_effect" : []
        },
        "Turret" : {
            "level" : 1, "variance" : 0, "health" : 2, "attack" : 4, "defense" : 1, "skill" : 0, "skills" : [], "passives" : [], "death_effect" : []
        },
        "Troll" : {
            "level" : 6, "variance" : 1, "health" : 15, "attack" : 3, "defense" : 2, "skill" : 1, "skills" : ["Wide Swing", "Heal Self"], "passives" : ["Heal Self"], "death_effect" : []
        },
        "Werewolf" : {
            "level" : 6, "variance" : 1, "health" : 8, "attack" : 5, "defense" : 2, "skill" : 2, "skills" : ["Double Slash"], "passives" : [], "death_effect" : []
        },
        "Wolf" : {
            "level" : 3, "variance" : 1, "health" : 8, "attack" : 4, "defense" : 1, "skill" : 1, "skills" : ["Howl"], "passives" : [], "death_effect" : []
        }
        }