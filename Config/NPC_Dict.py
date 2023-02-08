class NPC_Dict:
    def __init__(self):
        self.NPC_STORE_TYPES = {}
        self.EQUIPMENT_STORE = {}
        self.POTION_STORE = {0: "Health", 1: "Energy"}
        self.POTION_PRICES = {"Health": 50, "Energy": 50}