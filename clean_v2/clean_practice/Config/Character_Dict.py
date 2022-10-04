class Character_Dict:
    def __init__(self):
        self.HERO_STATS = {
        "Summoner" : {
            "health" : 10, "attack" : 2, "defense" : 1, "skill" : 3, "mana" : 0
        }
        }
        self.HERO_SKILLS = {
        "Summoner" : {
            0 : "Command Spirit", 2 : "Summon Turret"
        }
        }
        self.SPIRIT_SKILLS = {
        "Angel" : {
            0 : "Heal Ally"
        }
        }
        self.MONSTER_STATS = {
        "Goblin" : {
            "level" : 2, "variance" : 1, "health" : 10, "attack" : 2, "defense" : 1, "skill" : 1, "skills" : ["Blind"], "passives" : [], "death_effect" : []
        },
        "Hob Goblin" : {
            "level" : 4, "variance" : 1, "health" : 12, "attack" : 3, "defense" : 1, "skill" : 2, "skills" : ["Blind"], "passives" : [], "death_effect" : []
        },
        "Turret" : {
            "level" : 1, "variance" : 0, "health" : 5, "attack" : 5, "defense" : 1, "skill" : 0, "skills" : [], "passives" : [], "death_effect" : []
        },
        "Wolf" : {
            "level" : 3, "variance" : 1, "health" : 10, "attack" : 4, "defense" : 1, "skill" : 1, "skills" : ["Howl"], "passives" : [], "death_effect" : []
        }
        }