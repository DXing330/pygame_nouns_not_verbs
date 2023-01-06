from dataclasses import dataclass


@dataclass
class Equipment:
    name: str
    # Weapon/Armor
    type: str
    target: str
    power: int
    effect: str
    effect_specifics: str
    # What kind of heroes can't use it. Warrior/Summoner/etc.
    disallowed_user: list