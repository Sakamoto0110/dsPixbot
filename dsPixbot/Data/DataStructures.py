class PlayerInfo:
    def __init__(self, _nome, _nick):
        self.Nome = _nome
        self.Nick = _nick
    def AsDict(self):
        return{
            "Nome": self.Nome,
            "Nick": self.Nick
        }