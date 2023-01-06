from Buildings.Guild_Folder.Guild_Story import *
from Buildings.Guild_Folder.Smith import *
from Characters.Party import Party
from Characters.Hero import Hero
from Utility.Draw import *

class Candidate_Dict:
    def __init__(self):
        self.candidates = {
        "Warrior" : Hero("Warrior", 4, 0, 0, 0, 0, 0, 0, 0, 0, [], [], [], [])
        }


class Guild:
    def __init__(self, party: Party):
        self.party = party
        self.draw = Draw()
        self.cdict = Candidate_Dict()
        self.bool = True

    def draw_text(self, text: str, line: int = 1):
        self.draw.draw_text(text, line)

    def draw_background(self):
        self.draw.draw_background("Guild")

    def inside(self):
        self.entrance()
        while self.bool:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    pygame.event.clear()
                    if event.key == pygame.K_l:
                        self.bool = False
                    if event.key == pygame.K_e:
                        self.entrance()
                    if event.key == pygame.K_t:
                        self.recruit_stage()
                    if event.key == pygame.K_q:
                        self.quest()
                    if event.key == pygame.K_s and "Smith" in self.party.journal.guild_facilities:
                        self.bool = False
                        smith = Smith(self.party)
                        smith.talk()

    def entrance(self):
        self.draw_background()
        if self.party.journal.guild_progress <= -1:
            acceptable = False
            for hero in self.party.heroes:
                if hero.level >= 4:
                    acceptable = True
            if acceptable:
                self.draw_text("Seem's like you're strong enough to join.")
                self.draw_text("Well, we always need more people, feel free to come in and chat.", 2)
                self.draw_text("ENTER", 3)
                self.party.journal.guild_progress += 1
            else:
                self.draw_text("We may be understaffed, but we still can't just accept everyone.")
                self.draw_text("Come back when you're a bit stronger.", 2)
        elif self.party.journal.guild_progress >= 0:
            self.draw_text("Welcome.")
            self.draw_text("QUEST / TALK / LEAVE", 2)
            if "Smith" in self.party.journal.guild_facilities:
                self.draw_text("SMITH", 3)

    def recruit_stage(self):
        recruit, candidate = self.talk()
        while recruit:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    pygame.event.clear()
                    if event.key == pygame.K_l:
                        recruit = False
                    if event.key == pygame.K_a:
                        self.add_hero(candidate)
                        recruit = False
        self.inside()

    def add_hero(self, candidate):
        self.draw_background()
        if candidate == "Warrior":
            self.draw_text("Are you new too? I'm looking for a party, want to join up?")
            self.draw_text("You seem pretty smart, I'll let you make the choices.", 2)
            pygame.time.delay(500)
            new_hero = self.cdict.candidates.get(candidate)
            self.party.add_hero(new_hero)

    def talk(self):
        self.draw_background()
        if len(self.party.heroes) < 2:
            self.draw_text("There is a young man sitting alone at a table in the corner of the guild.")
            self.draw_text("APPROACH / LEAVE", 2)
            return True, "Warrior"
        else:
            self.draw_text("There doesn't seem to be anyone new to talk to.")
            pygame.time.delay(500)
            return False, None

    def quest(self):
        self.draw_background()
        if self.party.journal.rank == 1 and self.party.journal.rank_exp == 0:
            self.draw_text("Huh, you want a quest?")
            self.draw_text("Not many people here give requests.", 2)
            self.draw_text("Oh I know, how about you bring us 50 gold so we can fix that leak in our roof.", 3)
            pygame.time.delay(2000)
            self.party.journal.rank_exp += 1
        elif self.party.journal.rank == 1 and self.party.journal.rank_exp == 1 and self.party.items.coins >= 50:
            self.party.items.coins -= 50
            self.party.journal.rank += 1
            self.party.journal.rank_exp = 0
            self.draw_text("Wow, you actually did it.")
            self.draw_text("Good job. Now we'll be dry when the rain comes.", 2)
            pygame.time.delay(500)
        elif self.party.journal.rank == 2 and self.party.journal.rank_exp == 0 and self.party.items.mana_crystals > 0:
            self.draw_text("You again? Still nothing.")
            self.draw_text("Wait a second, is that a mana crystal!?", 2)
            self.draw_text("You must have fought something pretty tough to get one of those.", 3)
            self.draw_text("Tell you what, bring me 5 mana crystals and I'll give you something good.", 4)
            self.party.journal.rank_exp += 1
            pygame.time.delay(2000)
        elif self.party.journal.rank == 2 and self.party.journal.rank_exp == 1 and self.party.items.mana_crystals >= 5:
            self.draw_text("Took you awhile.")
            self.draw_text("Well thanks, these are pretty valuable.", 2)
            self.draw_text("We might be able to afford some new armor with this.", 3)
            self.draw_text("Reward? Oh right, here's some coins for your troubles.", 4)
            self.party.items.coins += 500
            self.draw_text("Look you can buy some armor when we get the next shipment, ok?", 5)
            self.party.journal.guild_facilities.append("Smith")
            self.party.journal.rank_exp = 0
            self.party.journal.rank += 1
            pygame.time.delay(2000)
        else:
            self.draw_text("Still no new quests, sorry kid.")
            pygame.time.delay(500)
        self.inside()