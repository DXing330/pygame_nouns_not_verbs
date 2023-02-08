from Utility.Draw import *
from Utility.Pick import *
from Characters.Party import *
from Config.NPC_Dict import *
ND = NPC_Dict()

class Alchemist:
    def __init__(self, party: Party):
        self.party = party
        self.draw = Draw()
        self.bool = True

    def leave(self):
        self.bool = False
        self.draw.draw_bg_and_text("Guild", "Good luck out there.")
        pygame.time.delay(500)

    def choices(self, option: int = 0):
        self.draw.draw_background("Guild")
        if option == -1:
            self.draw.draw_bg_and_text("Guild", "Sorry that won't work.")
            pygame.time.delay(500)
            self.bool = False
        if option == 0:
            self.options = ["SHOP", "LEAVE"]
        if option == 1:
            self.options = ["POTIONS", "LEAVE"]

    def talk(self):
        while self.bool:
            self.draw.draw_background("Guild")
            self.choices()
            pick_option = Pick(self.options, False)
            choice = pick_option.pick()
            if choice == "SHOP":
                self.store()
            if choice == "LEAVE":
                self.leave()

    def store(self):
        self.choices(1)
        while self.bool:
            self.draw.draw_background("Guild")
            pick_option = Pick(self.options, False)
            choice = pick_option.pick()
            if "POTIONS" in choice:
                self.available_potions()
            if choice == "LEAVE":
                self.leave()

    def available_potions(self):
        possible_potions = []
        for number in range(0, self.party.journal.rank):
            potion = ND.POTION_STORE.get(number)
            if potion != None:
                possible_potions.append(potion)
        possible_potions.append("LEAVE")
        if len(possible_potions) <= 1:
            self.bool = False
        while self.bool:
            self.draw.draw_background("Guild")
            pick_potion = Pick(possible_potions, False)
            choice = pick_potion.pick()
            if choice == "LEAVE":
                self.leave()
            else:
                self.decide_quantity_price(choice)

    def decide_quantity_price(self, product):
        price = ND.POTION_PRICES.get(product)
        quantity = 1
        self.draw_current_purchase(product, price, quantity)
        while self.bool:
            for event in pygame.event.get():
                pygame.event.clear()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.check_out(product, quantity, price)
                    if event.key == pygame.K_DOWN and quantity > 1:
                        quantity -= 1
                        self.draw_current_purchase(product, price, quantity)
                    if event.key == pygame.K_UP:
                        if (quantity+1)*price <= self.party.items.coins:
                            quantity += 1
                            self.draw_current_purchase(product, price, quantity)
                        else:
                            self.draw.draw_background("Guild")
                            self.draw.draw_text("You can't afford more than that.")
                            pygame.time.delay(500)

    def draw_current_purchase(self, product, price, quantity):
        self.draw.draw_background("Guild")
        self.draw.draw_text("How many "+str(product)+" potions would you like?", 1)
        self.draw.draw_text("COINS: "+str(self.party.items.coins), 2)
        self.draw.draw_text("QUANTITY: "+str(quantity)+" COST: "+str(quantity*price), 3)

    def check_out(self, product, quantity, price):
        self.draw.draw_background("Guild")
        cost = quantity*price
        self.party.items.coins -= cost
        if product == "Health":
            self.party.items.health_potions += quantity
        if product == "Energy":
            self.party.items.energy_potions += quantity
        self.draw.draw_text("Anything else?")
        pygame.time.delay(1000)
        self.talk()
