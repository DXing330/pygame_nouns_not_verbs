from dataclasses import dataclass


@dataclass
class Location:
    name: str
    groups: list
    treasure: list
    weather: list
    dungeon_size: int = 1
    events: list = None
    image: any = None
    boss: bool = False
    bosses: list = None
    quest: bool = False