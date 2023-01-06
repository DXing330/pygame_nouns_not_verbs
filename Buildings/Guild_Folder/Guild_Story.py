import pygame
from Utility.Draw import *

class GStory:
    def __init__(self, progress: int):
        self.progress = progress
        self.draw = Draw()

    def draw_text(self, text: str, line: int):
        self.draw.draw_text(text, line)

    def guild_story(self, progress: int):
        if progress <= 1:
            self.draw_text("There used to be a lot of monster hunters here.")
            pygame.time.delay(1000)
            self.draw_text("It's kinda funny how when the monsters began to swarm they all went away.", 2)
            pygame.time.delay(1000)
            self.draw_text("I can't blame them though, it's hard to survive out here.", 3)
            pygame.time.delay(1000)
            self.draw_text("Any hunter worth their metal will have gone to the big cities by now.", 4)
            pygame.time.delay(1000)
            self.draw_text("Ah but the story, a long time ago this village used to be a hub for travelers.", 5)
            pygame.time.delay(1000)
            self.draw_text("We were the biggest village within a weeks travel, and the safest too.", 6)
            pygame.time.delay(1000)
            self.draw_text("Times were good, all sorts of people wanted to come here.", 7)
            pygame.time.delay(1000)
            self.draw_text("We had traders from all around the country stopping by, we even had wandering circuses chose to path towards us.", 8)
            pygame.time.delay(1000)
            self.draw_text("'And it was all because of this guild here.' recalls the man as he runs his hand across a faded wall", 9)
            pygame.time.delay(1000)
            self.draw_text("My best friends faces used to be carved into this wall, but there's no one left to maintain the carvings.", 10)
            pygame.time.delay(3000)
            self.draw_text("Anyway, it was this guild that kept people feeling safe enough to come here.", 11)
            pygame.time.delay(1000)
            self.draw_text("Now that it's gone, things just haven't been the same.", 12)
            pygame.time.delay(1000)
            self.draw_text("The reason I'm saying this to you is because, I can see you're powerful.", 13)
            pygame.time.delay(1000)
            self.draw_text("I have an eye for these kinds of things and I can see you would be a great hunter.", 14)
            pygame.time.delay(1000)
            self.draw_text("Seeing you makes me feel like this guild might still have a second chance, what do you say?", 15)
            pygame.time.delay(1000)
            self.draw_text("If you could gather some funds and fix this place up, we could start it up again.", 16)
            pygame.time.delay(1000)
            self.draw_text("If we train some people or recruit them, we can make this place safe again.", 17)
            pygame.time.delay(1000)
            self.draw_text("You don't need to answer right away, I know it's a big ask.", 18)
            pygame.time.delay(1000)
            self.draw_text("But if you're interested I think for around 1000 coins we can fix this place up.", 19)
            pygame.time.delay(1000)