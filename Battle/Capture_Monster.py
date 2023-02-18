from Characters.Party import *


class Capture_Monster:
    def __init__(self, party, catcher, monster):
        self.party: Party = party
        self.catcher: Hero = catcher
        self.monster: Monster = monster

    def determine_capture(self):
        pass

    def adjust_skills(self):
        pass

    def catch_monster(self):
        pass

    def absorb_monster(self):
        pass