from dataclasses import dataclass


@dataclass
class Element:
    name : str
    strengths : list
    weaknesses : list