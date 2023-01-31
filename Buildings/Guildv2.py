from Buildings.Guild_Folder.Guild_Story import *
from Buildings.Guild_Folder.Smith import *
from Buildings.Tavern import *
from Characters.Party import Party
from Characters.Hero import Hero
from Utility.Draw import *
from Config.Quest_Dict import *
Q = Quest_Dict()


class Guild:
    def __init__(self, party: Party):
        self.party = party
        self.draw = Draw()
        self.bool = True

    def draw_text(self, text: str, line: int = 1):
        self.draw.draw_text(text, line)

    def draw_background(self):
        self.draw.draw_background("Guild")

    def inside(self):
        while self.bool:
            self.entrance()
            pick_from = Pick(self.options, False)
            choice = pick_from.pick()
            if choice == "LEAVE":
                self.bool = False
            elif choice == "TALK":
                tavern = Tavern(self.party)
                tavern.recruit_stage()
                self.bool = False
            elif choice == "QUEST":
                self.quest()
            elif "FINISH" in choice:
                self.finish_quests()
            elif "SMITH" in choice:
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
                pygame.time.delay(1000)
                self.party.journal.guild_progress += 1
                self.inside()
            else:
                self.draw_text("We may be understaffed, but we still can't just accept everyone.")
                self.draw_text("Come back when you're a bit stronger.", 2)
                pygame.time.delay(2000)
                self.bool = False
        elif self.party.journal.guild_progress >= 0:
            self.options = ["QUEST", "TALK", "LEAVE"]
            if "Smith" in self.party.journal.guild_facilities:
                self.options.append("SMITH")
            if len(self.party.quests) > 0:
                self.options.append("FINISH QUEST")

    def random_quest(self):
            possible_quests = []
            for number in range(0, self.party.journal.rank):
                quest = Q.QUEST_RANKS.get(number)
                if quest != None:
                    possible_quests.append(quest)
            given_quest = possible_quests[random.randint(0, len(possible_quests)-1)]
            if len(self.party.quests) < self.party.journal.rank:
                self.draw_text("Here's a new request that we got "+str(given_quest)+".")
                new_quest = Quest(**Q.ALL_QUESTS.get(given_quest))
                new_quest.start_day = self.party.journal.days
                self.party.quests.append(new_quest)
            else:
                self.draw_text("Still no new quests, sorry kid.")
            pygame.time.delay(500)

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
            pygame.time.delay(500)
            self.draw_text("Wait a second, is that a mana crystal!?", 2)
            pygame.time.delay(500)
            self.draw_text("You must have fought something pretty tough to get one of those.", 3)
            self.draw_text("Tell you what, bring me 5 mana crystals and I'll give you something good.", 4)
            self.party.journal.rank_exp += 1
            pygame.time.delay(2000)
        elif self.party.journal.rank == 2 and self.party.journal.rank_exp == 1 and self.party.items.mana_crystals >= 5:
            self.draw_text("Took you awhile.")
            pygame.time.delay(500)
            self.draw_text("Well thanks, these are pretty valuable.", 2)
            self.draw_text("We might be able to afford some new armor with this.", 3)
            self.draw_text("Reward? Oh right, here's some coins for your troubles.", 4)
            self.party.items.coins += 50
            pygame.time.delay(500)
            self.draw_text("Look you can buy some armor when we get the next shipment, ok?", 5)
            self.party.journal.guild_facilities.append("Smith")
            self.party.journal.rank_exp = 0
            self.party.journal.rank += 1
            pygame.time.delay(2000)
        elif self.party.journal.rank == 3:
            strong = False
            for hero in self.party.heroes:
                if hero.level >= 8:
                    strong = True
            if strong:
                self.draw_text("Looks like you're pretty strong now.")
                pygame.time.delay(1000)
                self.draw_text("I'll let you know about a place full of tough monsters.", 2)
                self.draw_text("Be careful though, lots of strong people have died there.", 3)
                pygame.time.delay(1000)
                self.draw_text("Maybe try to find some more allies before you go.", 4)
                pygame.time.delay(1000)
                self.party.journal.rank += 1
            elif not strong:
                self.draw_text("Lot more requests to work on.")
                pygame.time.delay(1000)
                self.random_quest()
        elif self.party.journal.rank == 4:
            if self.party.journal.reputation > 10:
                self.draw_text("You've been helping a lot of people around here.")
                pygame.time.delay(1000)
                self.draw_text("It's been awhile since I've seen someone like you.", 2)
                self.draw_text("Most people move on from here when they're as strong as you are.", 3)
                pygame.time.delay(1000)
                self.draw_text("What I'm trying to say is thanks.", 4)
                pygame.time.delay(1000)
                self.draw_text("If you want, maybe I can teach you somethings.", 5)
                self.draw_text("I may be too old to work in the field now but I can at least share what I've learned.", 6)
                pygame.time.delay(1000)
                self.party.journal.rank += 1
                self.party.journal.guild_facilities.append("Trainer")
            else:
                self.draw_text("Lot more requests to work on.")
                pygame.time.delay(1000)
                self.random_quest()
        else:
            self.random_quest()
        self.inside()

    def check_delivery(self, quest: Quest):
        if self.party.journal.days > quest.start_day + quest.time_limit:
                quest.failed = True
        if quest.specifics_amount > 0 and not quest.failed:
            # Use things from inventory to try to complete the order.
            if quest.specifics == "Mana Crystal":
                while quest.specifics_amount > 0 and self.party.items.mana_crystals > 0:
                    self.party.items.mana_crystals -= 1
                    quest.specifics_amount -= 1
        if quest.specifics_amount <= 0 and not quest.failed:
            quest.completed = True

    def check_quest(self, quest: Quest):
        self.draw_background()
        if quest.requirement == "Deliver":
            self.check_delivery(quest)
        if quest.failed:
            self.party.journal.infamy += 1
            self.draw_text("It's unfortunate that you couldn't complete the task.")
            self.draw_text("I'm afraid we'll need to let the requester know about this.", 2)
            pygame.time.delay(1000)
        elif quest.completed:
            if quest.reward_type == "Coins":
                self.party.items.coins += quest.reward_amount
                self.party.journal.reputation += 1
                self.draw_text("Good job finishing that "+quest.name+" job.")
                pygame.time.delay(500)
        else:
            self.draw_text("Look's like you haven't finished this "+quest.name+" job yet.")
            self.draw_text("There's still time so hurry up and do it.", 2)
            pygame.time.delay(1000)

    def finish_quests(self):
        for quest in self.party.quests:
            if quest.giver == "Guild":
                self.check_quest(quest)
            for number in range(0, len(self.party.quests)):
                if quest.completed or quest.failed:
                    self.party.quests.remove(quest)
        self.inside()