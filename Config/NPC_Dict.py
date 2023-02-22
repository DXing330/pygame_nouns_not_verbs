class NPC_Dict:
    def __init__(self):
        self.NPC_STORE_TYPES = {}
        self.EQUIPMENT_STORE = {}
        self.POTION_STORE = {0: "Health", 1: "Energy"}
        self.POTION_PRICES = {"Health": 50, "Energy": 50}
        self.NPC_STATS = {
        "Maid" : {
            "level" : 2, "health" : 10, "attack" : 1, "defense" : 1, "skill" : 0, "speed" : 10
        },
        "Warrior" : {
            "level" : 4, "health" : 10, "attack" : 3, "defense" : 2, "skill" : 1, "speed" : 10
        }
        }
        self.NPC_SKILLS = {
        "Maid" : {
            "Skills" : ["Cower"], "Passives" : [], "Conditionals" : []
        },
        "Warrior" : {
            "Skills" : ["Double Attack"], "Passives" : [], "Conditionals" : []
        }
        }