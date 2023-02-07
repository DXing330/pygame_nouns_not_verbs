import pygame
from Characters.Party import Party
from Characters.Hero import Hero
from Utility.Draw import *
from Utility.Pick import *

class Candidate_Dict:
    def __init__(self):
        self.candidates = {
        "Warrior" : Hero("Warrior", [], [], [], [], [], 10, 4),
        "Hunter" : Hero("Hunter", [],[],[],[],[],10,6)
        }

class Tavern:
    def __init__(self, party: Party):
        self.party = party
        self.draw = Draw()
        self.cdict = Candidate_Dict()

    def draw_text(self, text: str, line: int = 1):
        self.draw.draw_text(text, line)

    def draw_background(self):
        self.draw.draw_background("Guild")

    def recruit_stage(self):
        recruit, candidate = self.talk()
        if recruit:
            self.draw_background()
            choices = ["Approach", "Leave"]
            pick_from = Pick(choices, False)
            choice = pick_from.pick()
            if choice == "Leave":
                recruit = False
            if choice == "Approach":
                self.add_hero(candidate)
                recruit = False

    def add_hero(self, candidate):
        self.draw_background()
        if candidate == "Warrior":
            self.draw_text("Are you new too? I'm looking for a party, want to join up?")
            self.draw_text("You seem pretty smart, I'll let you make the choices.", 2)
            pygame.time.delay(1000)
            new_hero = self.cdict.candidates.get(candidate)
            self.party.add_hero(new_hero)
        elif candidate == "Hunter":
            self.draw_text("Seems like you've been doing well.")
            self.draw_text("I've been looking for some new allies, why don't we work together?", 2)
            pygame.time.delay(1000)
            new_hero = self.cdict.candidates.get(candidate)
            self.party.add_hero(new_hero)

    def talk(self):
        self.draw_background()
        if len(self.party.heroes) < 2:
            self.draw_text("There is a young man sitting alone at a table in the corner of the guild.")
            pygame.time.delay(2000)
            return True, "Warrior"
        elif len(self.party.heroes) < 3:
            self.draw_text("You see someone tinkering with a strange device in the corner of the tavern.")
            pygame.time.delay(2000)
            return True, "Hunter"
        else:
            self.draw_text("There doesn't seem to be anyone new to talk to.")
            pygame.time.delay(1000)
            return False, None