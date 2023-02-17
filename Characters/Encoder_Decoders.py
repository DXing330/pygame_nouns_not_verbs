import json
from Skills.Effects import *
from Skills.Skill import Skill

class Skill_Encoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Skill):
            return {
                'name': obj.name,
                'effect' : obj.effect,
                'effect_specifics' : obj.effect_specifics,
                'power' : obj.power,
                'targets' : obj.targets,
                'cost' : obj.cost,
                'cooldown' : obj.cooldown,
                'cooldown_counter' : obj.cooldown_counter,
                'chance' : obj.chance,
                'condition' : obj.condition,
                'condition_specifics' : obj.condition_specifics
            }
        if isinstance(obj, Conditional_Effect):
            return {
                'name': obj.name,
                'timing' : obj.timing,
                'condition' : obj.condition,
                'condition_specifics' : obj.condition_specifics,
                'effect' : obj.effect,
                'effect_specifics' : obj.effect_specifics,
                'power' : obj.power
            }
        if isinstance(obj, Passive):
            return {
                'name': obj.name,
                'effect' : obj.effect,
                'effect_specifics' : obj.effect_specifics,
                'power' : obj.power,
                'turns' : obj.turns
            }
        return super().default(obj)
    
class Skill_Decoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        json.JSONDecoder.__init__(self, object_hook=self.object_hook, *args, **kwargs)

    def object_hook(self, obj):
        if 'name' in obj and 'effect' in obj and 'effect_specifics' in obj and 'power' in obj and 'targets' in obj and 'cost' in obj and 'cooldown' in obj and 'cooldown_counter' in obj and 'chance' in obj and 'condition' in obj and 'condition_specifics' in obj:
            return Skill(obj['name'], obj['effect'], obj['effect_specifics'], obj['power'], obj['targets'], obj['cost'], obj['cooldown'], obj['cooldown_counter'], obj['chance'], obj['condition'], obj['condition_specifics'])
        if 'name' in obj and 'effect' in obj and 'effect_specifics' in obj and 'power' in obj and 'condition' in obj and 'condition_specifics' in obj and 'timing' in obj:
            return Conditional_Effect(obj['name'], obj['timing'], obj['condition'], obj['condition_specifics'], obj['effect'], obj['effect_specifics'], obj['power'])
        if 'name' in obj and 'effect' in obj and 'effect_specifics' in obj and 'power' in obj and 'turns' in obj:
            return Passive(obj['name'], obj['effect'], obj['effect_specifics'], obj['power'], obj['turns'])
        return obj