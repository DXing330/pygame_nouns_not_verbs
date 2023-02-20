class Location_Dict:
    def __init__(self):
        self.LOCATIONS = {
        0 : {"name" : "Starter Forest", "monsters" : ["Goblin", "Imp"], "treasure" : [], "weather" : ["None"], "dungeon_size" : 2, "events" : [], "image" : "Forest", "boss" : False, "bosses" : []},
        1 : {"name" : "Dark Forest", "monsters" : ["Goblin", "Imp", "Serpent"], "treasure" : [], "weather" : ["Rain", "None"], "dungeon_size" : 3, "events" : [], "image" : "Forest", "boss" : True, "bosses" : ["Hob Goblin", "Troll"]},
        2 : {"name" : "Wolf Den", "monsters" : ["Wolf", "Serpent"], "treasure" : [], "weather" : ["Darkness"], "dungeon_size" : 4, "events" : [], "image" : "Cave", "boss" : True, "bosses" : ["Werewolf"]},
        3 : {"name" : "Evil Forest", "monsters" : ["Troll", "Hob Goblin", "Orc"], "treasure" : [], "weather" : ["Fog", "Rain", "None"], "dungeon_size" : 5, "events" : [], "image" : "Forest", "boss" : True, "bosses" : ["Vampire", "Demon"]}
        }
        self.LOCATIONS_NAMES = {
        "None" : {"name" : "Town", "groups" : [], "treasure" : [], "weather" : ["None"], "dungeon_size" : 0, "events" : [], "image" : "Forest", "boss" : False, "bosses" : []},
        "Starter Forest" : {"name" : "Starter Forest", "groups" : ["SF1", "SF2", "SF3", "SF4", "SF5", "SF6"], "treasure" : [], "weather" : ["None"], "dungeon_size" : 2, "events" : [], "image" : "Forest", "boss" : False, "bosses" : []},
        "Dark Forest" : {"name" : "Dark Forest", "groups" : ["DF1", "DF2", "DF3", "DF4", "DF5", "DF6"], "treasure" : [], "weather" : ["Rain", "None"], "dungeon_size" : 3, "events" : [], "image" : "Forest", "boss" : True, "bosses" : ["Hob Goblin", "Troll"]},
        "Wolf Den" : {"name" : "Wolf Den", "groups" : ["WD1", "WD2", "WD3", "WD4", "WD5", "WD6"], "treasure" : [], "weather" : ["Darkness"], "dungeon_size" : 4, "events" : [], "image" : "Cave", "boss" : True, "bosses" : ["Werewolf"]},
        "Evil Forest" : {"name" : "Evil Forest", "groups" : ["EF1", "EF2", "EF3", "EF4", "EF5", "EF6"], "treasure" : [], "weather" : ["Fog", "Rain", "None"], "dungeon_size" : 5, "events" : [], "image" : "Forest", "boss" : True, "bosses" : ["Vampire", "Demon"]}
        }