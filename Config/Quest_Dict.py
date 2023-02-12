class Quest_Dict:
    def __init__(self):
        self.QUEST_RANKS = {
        1 : "Goblin Slaying",
        2 : "Hob-Goblin Slaying",
        3 : "Troll Hunting"
        }
        self.ALL_QUESTS = {
        "_Test" : {
            "name" : "Test", "giver" : None, "location" : None, "requirement" : None, "specifics" : None,  "specifics_amount" : 0, "start_day" : 0, "time_limit" : 0, "completed" : False, "failed" : False, "reward_type" : None, "reward_amount" : 0
        },
        "Goblin Slaying" : {
            "name" : "Goblin Slaying", "giver" : "Guild", "location" : "Any", "requirement" : "Kill", "specifics" : "Goblin",  "specifics_amount" : 5, "start_day" : 0, "time_limit" : 10, "completed" : False, "failed" : False, "reward_type" : "Coins", "reward_amount" : 1
        },
        "Hob-Goblin Slaying" : {
            "name" : "Hob Goblin Slaying", "giver" : "Guild", "location" : "Any", "requirement" : "Kill", "specifics" : "Hob Goblin",  "specifics_amount" : 3, "start_day" : 0, "time_limit" : 10, "completed" : False, "failed" : False, "reward_type" : "Coins", "reward_amount" : 1
        },
        "Troll Hunting" : {
            "name" : "Troll Hunting", "giver" : "Guild", "location" : "Any", "requirement" : "Kill", "specifics" : "Troll",  "specifics_amount" : 1, "start_day" : 0, "time_limit" : 20, "completed" : False, "failed" : False, "reward_type" : "Coins", "reward_amount" : 5
        },
        "Mana Shipment" : {
            "name" : "Mana Shipment", "giver" : "Guild", "location" : "Any", "requirement" : "Deliver", "specifics" : "Mana Crystal",  "specifics_amount" : 5, "start_day" : 0, "time_limit" : 30, "completed" : False, "failed" : False, "reward_type" : "Coins", "reward_amount" : 50
        }
        }
        self.STORY_QUESTS = {
        "_Test" : {
            "name" : "Test", "giver" : None, "location" : None, "requirement" : None, "specifics" : None,  "specifics_amount" : 0, "start_day" : 0, "time_limit" : 0, "completed" : False, "failed" : False, "reward_type" : None, "reward_amount" : 0
        },
        "Save" : {
            "name" : "Rescue Maid", "giver" : "Guild", "location" : "Evil Forest", "requirement" : "Save", "specifics" : "Maid",  "specifics_amount" : 0, "start_day" : 0, "time_limit" : -1, "completed" : False, "failed" : False, "reward_type" : None, "reward_amount" : 0
        },
        "Test" : {
            "name" : "Clear Evil Forest", "giver" : "Guild", "location" : "Evil Forest", "requirement" : "Clear", "specifics" : None,  "specifics_amount" : 0, "start_day" : 0, "time_limit" : -1, "completed" : False, "failed" : False, "reward_type" : None, "reward_amount" : 0
        }
        }