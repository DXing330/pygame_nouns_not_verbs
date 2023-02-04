class Quest_Dict:
    def __init__(self):
        self.QUEST_RANKS = {
        1 : "Goblin Slaying",
        2 : "Hob-Goblin Slaying",
        3 : "Troll Hunting"
        }
        self.ALL_QUESTS = {
        "_Test" : {
            "giver" : None, "location" : None, "requirement" : None, "specifics" : None,  "specifics_amount" : 0, "start_day" : 0, "time_limit" : 0, "completed" : False, "failed" : False, "reward_type" : None, "reward_amount" : 0
        },
        "Goblin Slaying" : {
            "name" : "Goblin Slaying", "giver" : "Guild", "location" : "Starter Forest", "requirement" : "Kill", "specifics" : "Goblin",  "specifics_amount" : 5, "start_day" : 0, "time_limit" : 10, "completed" : False, "failed" : False, "reward_type" : "Coins", "reward_amount" : 1
        },
        "Hob-Goblin Slaying" : {
            "name" : "HobGoblin Slaying", "giver" : "Guild", "location" : "Dark Forest", "requirement" : "Kill", "specifics" : "Hob Goblin",  "specifics_amount" : 3, "start_day" : 0, "time_limit" : 10, "completed" : False, "failed" : False, "reward_type" : "Coins", "reward_amount" : 1
        },
        "Troll Hunting" : {
            "name" : "Troll Hunting", "giver" : "Guild", "location" : "Dark Forest", "requirement" : "Kill", "specifics" : "Troll",  "specifics_amount" : 1, "start_day" : 0, "time_limit" : 20, "completed" : False, "failed" : False, "reward_type" : "Coins", "reward_amount" : 5
        },
        "Mana Shipment" : {
            "name" : "Mana Shipment", "giver" : "Guild", "location" : "Any", "requirement" : "Deliver", "specifics" : "Mana Crystal",  "specifics_amount" : 5, "start_day" : 0, "time_limit" : 30, "completed" : False, "failed" : False, "reward_type" : "Coins", "reward_amount" : 50
        }
        }