class Sort:
    def __init__(self):
        pass

    def sort_by_speed(self, battlers: list):
        battlers_1 = []
        battlers_2 = []
        if len(battlers) > 1:
            n = len(battlers)//2
            for number in range(0, n):
                battlers_1.append(battlers[number])
            for number in range(n, len(battlers)):
                battlers_2.append(battlers[number])
            battlers_1 = self.sort_by_speed(battlers_1)
            battlers_2 = self.sort_by_speed(battlers_2)
            return self.merge_by_speed(battlers_1, battlers_2)
        return battlers

    def merge_by_speed(self, battlers_1: list, battlers_2: list):
        merged = []
        while len(battlers_1) > 0 and len(battlers_2) > 0:
            character_1 = battlers_1[0]
            character_2 = battlers_2[0]
            if character_1.speed >= character_2.speed:
                merged.append(character_1)
                battlers_1.remove(character_1)
            elif character_1.speed < character_2.speed:
                merged.append(character_2)
                battlers_2.remove(character_2)
        if len(battlers_1) > 0:
            for character in battlers_1:
                merged.append(character)
        if len(battlers_2) > 0:
            for character in battlers_2:
                merged.append(character)
        return merged