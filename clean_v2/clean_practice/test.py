def generate_monsters(self):
        if len(self.monsters) <= 0:
            # Plus one here in case self.amount is zero.
            for number in range(0, self.amount + 1):
                monster_name = self.location.monsters[random.randint(0, len(self.location.monsters) - 1)]
                monster = Monster(monster_name)
                self.monsters.append(monster)
            difficulty = self.amount ** 2
        for monster in self.monsters:
            self.update_monster_for_battle(monster)