from dataclasses import dataclass


@dataclass
class Skill:
    name: str
    effect: str
    effect_specifics: str
    power: int
    targets: str
    cost: int
    cooldown: int = 0
    cooldown_counter: int = 0
    chance: int = 100