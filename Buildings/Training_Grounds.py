from Utility.Draw import *
from Utility.Pick import Pick

class Training_Area:
    def __init__(self, party):
        self.party = party
        self.draw = Draw()
        self.bool = True

    def entrance(self):
        while self.bool:
            self.draw.draw_background("Guild")
            choices = ["Train", "Leave"]
            pick_from = Pick(choices, False)
            choice = pick_from.pick()
            if choice == "Train":
                self.pick_trainee()
            elif choice == "Leave":
                self.bool = False

    def pick_trainee(self):
        pick_from = Pick(self.party.heroes, False)
        self.draw.draw_background("Guild")
        self.draw.draw_text("It's a bit too much for me to train so many people.", 1)
        pygame.time.delay(1000)
        self.draw.draw_text("Let's go one at a time.  Who wants to go first?", 2)
        pygame.time.delay(1000)
        self.draw.draw_background("Guild")
        hero = pick_from.pick()
        self.training(hero)

    def training(self, hero):
        self.draw.draw_background("Guild")
        if hero.name == "Warrior":
            self.draw.draw_text("I used to be quite the fighter back in my day.", 1)
            pygame.time.delay(1000)
            self.draw.draw_text("I may have lost that strength but I still have those skills.", 2)
            self.draw.draw_text("What do you want me to show you?", 3)
            pygame.time.delay(1000)
            self.train_skill(hero)
        elif hero.name == "Hunter":
            self.draw.draw_text("I used to be quite the hunter back in the day.", 1)
            pygame.time.delay(1000)
            self.draw.draw_text("I still remember all kinds of tricks.", 2)
            self.draw.draw_text("What do you want me to show you?", 3)
            pygame.time.delay(1000)
            self.train_skill(hero)
        else:
            self.draw.draw_text("Sorry I don't really know much about what you do.", 1)
            pygame.time.delay(1000)
            self.draw.draw_text("Maybe you'll find a proper master somewhere in your travels.", 2)
            pygame.time.delay(1000)

    def train_skill(self, hero):
        self.draw.draw_background("Guild")
        pick_from = Pick(hero.skill_list, False)
        skill = pick_from.pick()
        index = hero.skill_list.index(skill)
        self.draw.draw_background("Guild")
        if "+" in skill:
            self.draw.draw_text("Sorry you're already as good as I was at that.", 1)
            pygame.time.delay(2000)
        else:
            # It costs experience to strengthen skills.
            # Needs at least 100 exp so only level capped (or higher than level 10) characters can upgrade skills.
            if hero.exp > 100:
                hero.skill_list[index] += "+"
                hero.exp -= 100
                self.draw.draw_text("I hope this is useful for you.", 1)
                pygame.time.delay(1000)
            else:
                self.draw.draw_text("Seems like you need more experience before you can master this technique.", 1)
                pygame.time.delay(2000)