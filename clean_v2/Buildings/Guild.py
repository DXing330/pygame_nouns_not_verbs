from Buildings.Guild_Folder.Guild_Story import *
from Characters.Party import Party
from Utility.Draw import *


class Guild:
    def __init__(self, party: Party):
        self.party = party
        self.draw = Draw()
        self.oldman = True
        self.story = GStory(self.party.journal.guild_progress)

    def draw_text(self, text: str, line: int = 1):
        self.draw.draw_text(text, line)

    def draw_background(self):
        if self.party.journal.guild_progress < 2:
            self.draw.draw_background("Old_Guild")
        else:
            self.draw.draw_background("New_Guild")

    def enter(self):
        if self.party.journal.guild_progress < 2:
            self.old_man()
        if self.party.journal.guild_progress >= 2:
            pass

    def old_man(self):
        self.oldman = True
        if self.party.journal.guild_progress < 1:
            self.draw_background()
            self.draw_text("You see an old man huddled in the corner.")
            self.draw_text("Approach/Leave", 2)
            while self.oldman:
                keys = pygame.key.get_pressed()
                if keys.key == pygame.K_a:
                    self.old_man_talk()
                    self.oldman = False
                elif keys.key == pygame.K_l:
                    self.draw_background()
                    self.oldman = False
        if self.party.journal.guild_progress == 1:
            self.draw_background()
            self.draw_text("The old man is drawing blueprints on the ground.")
            self.draw_text("As you approach he looks up.", 2)
            self.draw_text("Do you have what we need?  Are you ready to start this?", 3)
            while self.oldman:
                keys = pygame.key.get_pressed()
                if keys.key == pygame.K_y:
                    if self.party.items.coins >= 1000:
                        self.old_man_talk()
                    else:
                        self.draw_background()
                        self.draw_text("Looks like you still don't have enough.")
                        pygame.time.delay(1000)
                        self.oldman = False
                elif keys.key == pygame.K_n:
                    self.draw_background()
                    self.draw_text("Oh, well take your time, I'll be waiting here.")
                    pygame.time.delay(1000)
                    self.oldman = False

    def old_man_talk(self):
        self.oldman = True
        if self.party.journal.guild_progress < 1:
            self.draw_background()
            self.draw_text("The old man stares at you as you approach.")
            self.draw_text("'Welcome to the hall of heroes.' says the old man, smiling.", 2)
            self.draw_text("'Or at least it used to be. Say, do want to hear a story?' asks the old man.", 3)
            self.draw_text("YES/NO", 4)
            while self.oldman:
                keys = pygame.key.get_pressed()
                if keys.key == pygame.K_y:
                    pygame.event.clear()
                    self.party.journal.guild_progress += 1
                    self.draw_background()
                    self.story.guild_story()
                    self.oldman = False
                elif keys.key == pygame.K_n:
                    self.draw_background()
                    self.draw_text("'Ah, young people, always so many things to do. Good luck out there.' waves the old man.")
                    pygame.time.delay(1000)
                    self.oldman = False
        if self.party.journal.guild_progress == 1:
            self.draw_background()
            self.party.items.coins -= 1000
            self.draw("You've worked hard for these I'm sure.")
            self.draw("I'll make sure to put it to good use.")
            self.party.journal.guild_progress += 1
            self.oldman = False
            self.enter()