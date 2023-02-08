from Utility.Draw import *
from Utility.Pick import *
from Characters.Party import *
from Config.Equip_Dict import *
E = Equip_Dict()

class Smith:
    def __init__(self, party: Party):
        self.party = party
        self.draw = Draw()
        self.bool = True

    def talk(self):
        while self.bool:
            self.choices()
            pick_option = Pick(self.options, False)
            choice = pick_option.pick()
            if choice == "SHOP":
                self.draw.draw_background("Smith")
                self.draw.draw_text("Who should I take the measurements for?")
                pygame.time.delay(1000)
                self.draw.draw_background("Smith")
                pick_from = Pick(self.party.heroes, False)
                hero = pick_from.pick()
                self.store(hero)
            elif choice == "LEAVE":
                self.bool = False

    def choices(self, option: int = 0):
        self.draw.draw_background("Smith")
        if option == -1:
            self.draw.draw_bg_and_text("Smith", "Don't waste my time.")
            pygame.time.delay(500)
            self.bool = False
        if option == 0:
            self.options = ["SHOP", "LEAVE"]
        if option == 1:
            self.options = ["ARMOR", "WEAPON", "LEAVE"]
        if option == 2:
            self.options = ["NEW", "UPGRADE", "LEAVE"]

    def store(self, hero: Hero):
        store = True
        self.choices(1)
        while store and self.bool:
            pick_option = Pick(self.options, False)
            choice = pick_option.pick()
            if choice == "LEAVE":
                store = False
                self.talk()
            elif choice == "ARMOR":
                self.armorer(hero)
            elif choice == "WEAPON":
                self.weaponsmith(hero)

    def armorer(self, hero: Hero):
        armorer = True
        self.choices(2)
        while armorer and self.bool:
            pick_option = Pick(self.options, False)
            choice = pick_option.pick()
            if choice == "LEAVE":
                armorer = False
                self.talk()
            if choice == "NEW":
                self.new_armor(hero)
            if choice == "UPGRADE":
                if hero.armor != None:
                    self.upgrade_equipment(hero, "Armor")
                else:
                    self.choices(-1)

    def weaponsmith(self, hero: Hero):
        armorer = True
        self.choices(2)
        while armorer and self.bool:
            pick_option = Pick(self.options, False)
            choice = pick_option.pick()
            if choice == "LEAVE":
                armorer = False
                self.talk()
            if choice == "NEW":
                self.new_weapon(hero)
            if choice == "UPGRADE":
                if hero.armor != None:
                    self.upgrade_equipment(hero, "Weapon")
                else:
                    self.choices(-1)

    def upgrade_equipment(self, hero, choice:str):
        if choice == "Weapon":
            equip = hero.weapon
        elif choice == "Armor":
            equip = hero.armor
        self.draw.draw_background("Smith")
        if "++" in equip:
            self.draw.draw_text("I can't upgrade this any further.")
        elif "+" in str(equip) and self.party.items.mana_crystals >= 100:
            if choice == "Weapon":
                hero.weapon += "+"
            elif choice == "Armor":
                hero.armor += "+"
            self.draw.draw_text("It's as strong as I can make it now.")
            self.party.items.mana_crystals -= 100
        elif "+" not in str(equip) and self.party.items.mana_crystals >= 100:
            if choice == "Weapon":
                hero.weapon += "+"
            elif choice == "Armor":
                hero.armor += "+"
            self.draw.draw_text("It's one of my best works.")
            self.party.items.mana_crystals -= 10
        else:
            self.draw.draw_text("I can't upgrade this.")
            self.draw.draw_text("Maybe if you had more mana crystals I could do something.", 2)
        pygame.time.delay(1000)
        self.talk()

    def new_armor(self, hero: Hero):
        self.draw.draw_background("Smith")
        equip_list = []
        # As the heroes get more respected more options will become available.
        for number in range(0, self.party.journal.rank):
            equipment = E.ARMOR_STORE.get(number)
            if equipment != None:
                equip_list.append(equipment)
        pick_from = Pick(equip_list, False)
        new_equip = pick_from.pick()
        cost = E.PRICES.get(new_equip)
        choice = self.confirm_purchase(new_equip, cost)
        self.draw.draw_background("Smith")
        if choice:
            if self.party.items.coins >= cost:
                self.party.items.coins -= cost
                hero.armor = new_equip
                self.draw.draw_text("Hope it keeps you safe.")
                pygame.time.delay(500)
            else:
                self.choices(-1)
        else:
            self.draw.draw_text("Want something else then?")
            pygame.time.delay(500)
            self.store(hero)

    def new_weapon(self, hero: Hero):
        self.draw.draw_background("Smith")
        equip_list = []
        # As the heroes get more respected more options will become available.
        for number in range(0, self.party.journal.rank):
            equipment = E.WEAPON_STORE.get(number)
            if equipment != None:
                equip_list.append(equipment)
        pick_from = Pick(equip_list, False)
        new_equip = pick_from.pick()
        cost = E.PRICES.get(new_equip)
        choice = self.confirm_purchase(new_equip, cost)
        self.draw.draw_background("Smith")
        if choice:
            if self.party.items.coins >= cost:
                self.party.items.coins -= cost
                hero.weapon = new_equip
                self.draw.draw_text("Hope it helps you.")
                pygame.time.delay(500)
            else:
                self.choices(-1)
        else:
            self.draw.draw_text("Want something else then?")
            pygame.time.delay(500)
            self.store(hero)

    def confirm_purchase(self, equip, cost):
        self.draw.draw_background("Smith")
        self.draw.draw_text(str(equip)+", COST: "+str(cost))
        self.draw.draw_text("Do you want to buy this one?", 2)
        self.draw.draw_text("Coins: "+str(self.party.items.coins), 3)
        pygame.time.delay(2000)
        options = ["YES", "NO"]
        pick_from = Pick(options, False)
        choice = pick_from.pick()
        if choice == "YES":
            return True
        if choice == "NO":
            return False