from dataclasses import dataclass


@dataclass
class NPC_Flag:
    type: str
    type_specifics: str
    condition: str
    condition_specifics: str
    result: str
    result_specifics: str
    triggered: bool = False


@dataclass
class NPC:
    name: str
    role: str
    role_specifics: str
    locations: list
    status: str = "Alive"
    attitude: int = 0

    def remove_flags(self):
        for flag in self.flags:
            if flag.triggered:
                self.flags.remove(flag)

    def store(self):
        pass


potion_seller = NPC("Bob", "Store", "Potions", ["Guild"], "Alive", 0)
join_party = NPC_Flag("Quest", "None", "Help", "Job", "Join_Party", "Mage")