from dataclasses import dataclass


@dataclass
class Location:
    name: str
    monsters: list
    treasure: list
    dungeon_size: int = 1
    events: list = None
    image: any = None
    boss: bool = False
    bosses: list = None