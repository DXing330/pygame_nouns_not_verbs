class Hero_Dict:
    def __init__(self):
        self.STATS = {
        "Summoner" : {
            "Health" : 10,
            "Attack" : 2,
            "Defense" : 1,
            "Skill" : 3,
            "Mana" : 3
        },
        "Cleric" : {
            "Health" : 10,
            "Attack" : 3,
            "Defense" : 1,
            "Skill" : 3,
            "Mana" : 3
        },
        "Warrior" : {
            "Health" : 15,
            "Attack" : 5,
            "Defense" : 2,
            "Skill" : 2,
            "Mana" : 0
        }
        }
        self.SKILLS = {
        "Summoner" : {
            0 : "Command"
        }
        }