class Location_Dict:
    def __init__(self):
        self.LOCATIONS = {
        0 : {"name" : "Starter Forest", "monsters" : ["Goblin", "Imp"], "treasure" : [], "dungeon_size" : 2, "events" : [], "image" : "Forest", "boss" : False, "bosses" : []},
        1 : {"name" : "Dark Forest", "monsters" : ["Goblin", "Imp", "Serpent"], "treasure" : [], "dungeon_size" : 3, "events" : [], "image" : "Forest", "boss" : True, "bosses" : ["Hob Goblin", "Troll"]},
        2 : {"name" : "Wolf Den", "monsters" : ["Wolf", "Serpent"], "treasure" : [], "dungeon_size" : 4, "events" : [], "image" : "Cave", "boss" : True, "bosses" : ["Werewolf"]},
        3 : {"name" : "Evil Forest", "monsters" : ["Troll", "Hob Goblin", "Orc"], "treasure" : [], "dungeon_size" : 5, "events" : [], "image" : "Forest", "boss" : True, "bosses" : ["Vampire", "Demon"]}
        }