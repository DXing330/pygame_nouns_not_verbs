class Element_Dict:
    def __init__(self):
        self.ELEMENTS = {
        "Fire" : {
            "name" : "Fire", "strengths" : ["Air"], "weaknesses" : ["Water"]
        },
        "Water" : {
            "name" : "Water", "strengths" : ["Fire"], "weaknesses" : ["Earth"]
        },
        "Earth" : {
            "name" : "Earth", "strengths" : ["Water"], "weaknesses" : ["Air"]
        },
        "Air" : {
            "name" : "Air", "strengths" : ["Earth"], "weaknesses" : ["Fire"]
        },
        "Dark" : {
            "name" : "Dark", "strengths" : [], "weaknesses" : ["Light"]
        },
        "Light" : {
            "name" : "Light", "strengths" : ["Light"], "weaknesses" : []
        }
        }