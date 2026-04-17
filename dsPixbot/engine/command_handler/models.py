# made by gemini

NULL_PARAM = -2147483647    

class Parameter:
    # made by gemini
    def __init__(self, name, info, dft_value=None, type=0) -> None:
        self.name = name
        self.info = info
        self.default_value = dft_value 
        self.preferedType = type

class Command:
    # made by gemini
    KEY = '!'    
    def __init__(self) -> None:
        self.header = ""
        self.args = []

class CommandTemplate:
    # made by gemini
    def __init__(self, _id=-1) -> None:
        self.roles = []
        self.description = "no_description"
        self.id = _id